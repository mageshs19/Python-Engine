"""Generate the keyed parent read required by an LRF STORE path."""
from __future__ import annotations

import re


class LrfStoreParentSelectComposer:
    _MARKER = re.compile(r"DB2-LRF-STORE-PARENT:\s*(?P<record>[A-Z][A-Z0-9-]*)", re.I)

    def __init__(self, *, sql_generator) -> None:
        self.sql = sql_generator
        self.messages: list[str] = []

    @staticmethod
    def _body(line: str) -> str:
        text = str(line or "").rstrip("\r\n")
        if len(text) >= 7 and text[:6].isdigit():
            return text[7:72].strip()
        return text.strip()

    def compose(self, text: str) -> str:
        self.messages = []
        lines = str(text or "").splitlines()
        output: list[str] = []
        index = 0
        while index < len(lines):
            body = self._body(lines[index])
            marker = self._MARKER.search(body)
            if not marker:
                output.append(lines[index])
                index += 1
                continue

            parent = marker.group("record").upper()
            insert_start = next(
                (
                    pos for pos in range(index + 1, min(index + 40, len(lines)))
                    if re.search(r"\bEXEC\s+SQL\b", self._body(lines[pos]), re.I)
                    and any(
                        re.search(r"\bINSERT\s+INTO\b", self._body(lines[look]), re.I)
                        for look in range(pos + 1, min(pos + 8, len(lines)))
                    )
                ),
                None,
            )
            if insert_start is None:
                output.append(lines[index])
                self.messages.append(
                    f"LRF STORE parent SELECT: could not find the generated INSERT after parent {parent}; marker retained."
                )
                index += 1
                continue

            insert_end_exec = next(
                (pos for pos in range(insert_start + 1, min(insert_start + 100, len(lines)))
                 if re.search(r"\bEND-EXEC\b", self._body(lines[pos]), re.I)),
                None,
            )
            if insert_end_exec is None:
                output.append(lines[index])
                self.messages.append(
                    f"LRF STORE parent SELECT: INSERT block for parent {parent} is incomplete; marker retained."
                )
                index += 1
                continue

            end_evaluate = next(
                (pos for pos in range(insert_end_exec + 1, min(insert_end_exec + 25, len(lines)))
                 if re.search(r"\bEND-EVALUATE\b", self._body(lines[pos]), re.I)),
                None,
            )
            period_line = next(
                (pos for pos in range((end_evaluate + 1) if end_evaluate is not None else insert_end_exec + 1,
                                      min(((end_evaluate + 8) if end_evaluate is not None else insert_end_exec + 8), len(lines)))
                 if self._body(lines[pos]) == "."),
                None,
            )
            if end_evaluate is None or period_line is None:
                output.append(lines[index])
                self.messages.append(
                    f"LRF STORE parent SELECT: INSERT SQLCODE block for parent {parent} is incomplete; marker retained."
                )
                index += 1
                continue

            parent_select = self.sql.select_by_key(parent, for_lrf_parent=True)
            if not parent_select or not any(re.search(r"\bSELECT\b", str(line), re.I) for line in parent_select):
                output.append(lines[index])
                self.messages.append(
                    f"LRF STORE parent SELECT: no keyed SELECT plan resolved for parent {parent}; marker retained."
                )
                index += 1
                continue

            # The SELECT owns its own SQLCODE handling. Gate the INSERT on
            # SQLCODE=0 as well, so a missing parent cannot create an orphan.
            # Preserve executable setup between the marker and INSERT SQL: SQL-
            # LOCATION and audit/technical defaults are COBOL logic, not comments
            # that may be discarded when the parent SELECT is inserted.
            setup_lines = [
                line for line in lines[index + 1:insert_start]
                if self._body(line)
                and not self._is_comment(line)
                and self._body(line).upper() != "CONTINUE."
            ]
            # SQL-LOCATION must be set BEFORE the SELECT so its WHEN OTHER
            # handler reports the failing statement. Audit/default setup belongs
            # inside the parent-success gate because it feeds the child INSERT.
            sql_location_lines = [
                line for line in setup_lines
                if re.search(r"\bMOVE\b.*\bTO\s+SQL-LOCATION\b", self._body(line), re.I)
            ]
            child_setup_lines = [line for line in setup_lines if line not in sql_location_lines]
            insert_text = " ".join(self._body(line) for line in lines[insert_start:period_line])
            child_table_match = re.search(r"\bINSERT\s+INTO\s+([A-Z][A-Z0-9_]*)", insert_text, re.I)
            child_table = child_table_match.group(1).upper() if child_table_match else "LRF-CHILD"
            output.extend(sql_location_lines)
            output.extend(parent_select)
            output.append("IF SQLCODE = 0")
            # In COBOL, a period terminates every open scope, not merely the
            # current MOVE/EVALUATE. Generated setup statements often carry a
            # trailing period; leaving one here would close this IF before the
            # INSERT and permit an orphan child row when the parent is absent.
            # Strip statement terminators throughout the gated region and let
            # the final END-IF own the period.
            gated_lines = [
                *self._parent_to_child_key_moves(parent, lines[insert_start:period_line]),
                *child_setup_lines,
                # Keep error diagnostics attributable to the INSERT. Do not
                # put a period here: it would close the parent-success IF.
                f"MOVE 'INSERT-{child_table}' TO SQL-LOCATION",
                *lines[insert_start:period_line],
            ]
            output.extend(self._strip_statement_terminators(gated_lines))
            output.append("END-IF.")
            index = period_line + 1
            self.messages.append(
                f"LRF STORE parent SELECT: generated keyed SELECT for {parent} and gated the child INSERT on SQLCODE 0."
            )

        result = "\n".join(output)
        if str(text or "").endswith(("\n", "\r")):
            result += "\n"
        return result


    @classmethod
    def _strip_statement_terminators(cls, lines: list[str]) -> list[str]:
        """Remove trailing COBOL periods inside a generated nested scope.

        Periods inside quoted literals are data, not statement terminators.
        Fixed-format sequence/indicator columns are preserved when present.
        """
        result: list[str] = []
        for line in lines:
            raw = str(line or "").rstrip("\r\n")
            body = cls._body(raw)
            if not body.endswith("."):
                result.append(line)
                continue

            quoted = False
            index = 0
            last_char_quoted = False
            while index < len(body):
                char = body[index]
                if char == "'":
                    if quoted and index + 1 < len(body) and body[index + 1] == "'":
                        index += 2
                        continue
                    quoted = not quoted
                if index == len(body) - 1:
                    last_char_quoted = quoted
                index += 1

            if last_char_quoted:
                result.append(line)
                continue

            # Remove only the final source statement terminator. Composer
            # input is normally free-format here; for fixed-format lines,
            # replace the matching body occurrence without touching columns.
            dot_pos = raw.rfind(".")
            if dot_pos >= 0:
                result.append(raw[:dot_pos] + raw[dot_pos + 1:])
            else:
                result.append(line)
        return result

    @staticmethod
    def _is_comment(line: str) -> bool:
        text = str(line or "")
        if len(text) >= 7 and text[:6].isdigit() and text[6] in ("*", "/"):
            return True
        return text.lstrip().startswith(("*", "/"))

    def _parent_to_child_key_moves(self, parent_record: str, insert_lines: list[str]) -> list[str]:
        """Copy shared parent key values into child INSERT host variables."""
        generator = self.sql
        mapping = getattr(generator, "mapping_repository", None)
        dclgen = getattr(generator, "dclgen_repository", None)
        table_resolver = getattr(generator, "table_name_resolver", None)
        hosts = getattr(generator, "host_variable_resolver", None)
        if not all((mapping, dclgen, table_resolver, hosts)):
            self.messages.append(
                f"LRF STORE parent SELECT: could not resolve parent-to-child host moves for {parent_record}."
            )
            return []

        insert_text = " ".join(self._body(line) for line in insert_lines)
        insert_match = re.search(
            r"\bINSERT\s+INTO\s+(?P<table>[A-Z][A-Z0-9_]*)\s*\((?P<columns>.*?)\)\s*VALUES\b",
            insert_text,
            re.I | re.S,
        )
        if not insert_match:
            return []
        child_table = table_resolver.resolve_table(insert_match.group("table"))
        insert_columns = [
            value.strip().upper()
            for value in insert_match.group("columns").split(",")
            if value.strip()
        ]
        mapped_parent_table = mapping.db2_table_for_record(parent_record)
        parent_table = table_resolver.resolve_table(mapped_parent_table) if mapped_parent_table else ""
        if not parent_table or not child_table:
            return []

        parent_columns = set(dclgen.column_names_for_table(parent_table))
        child_columns = set(dclgen.column_names_for_table(child_table))
        shared_columns = [
            column for column in insert_columns
            if column in parent_columns and column in child_columns
        ]
        moves: list[str] = []
        for column in shared_columns:
            source = hosts.host_reference_for_column(parent_table, column)
            target = hosts.host_reference_for_column(child_table, column)
            if not source or not target:
                continue
            moves.append(f"MOVE {source.lstrip(':')} TO {target.lstrip(':')}.")
        if not moves:
            self.messages.append(
                f"LRF STORE parent SELECT: no shared parent/child INSERT columns resolved for {parent_record}."
            )
        return moves
