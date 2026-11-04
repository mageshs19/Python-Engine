"""Safely rewrite proven LRF cursor access to a singleton DB2 SELECT.

This pass supports both bounded searches with a source-proven literal stop
predicate and source-proven FIRST-only access with no matching NEXT. It retains
all generated WHERE predicates, refuses to rewrite when source LRF extra-filter
literals are absent from the generated SQL, and fails closed on ambiguous
cursor/host-variable geometry.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class RewriteResult:
    text: str
    changed: bool = False
    diagnostic: str = ""


class BoundedLrfSingletonRewriter:
    _DECLARE = re.compile(r"\bDECLARE\s+(?P<cursor>[A-Z0-9-]+)\s+CURSOR\b", re.I)
    _PERFORM_UNTIL = re.compile(r"\bPERFORM\s+UNTIL\b", re.I)
    _END_PERFORM = re.compile(r"\bEND-PERFORM\b", re.I)
    _PREDICATE = re.compile(
        r"\b(?P<field>[A-Z][A-Z0-9-]*)\s+(?:OF\s+[A-Z][A-Z0-9-]*)?\s*=\s*(?P<literal>'[^']*'|\"[^\"]*\"|\d+)",
        re.I,
    )
    _HOST = re.compile(r":(?P<host>[A-Z][A-Z0-9-]*(?:\.[A-Z][A-Z0-9-]*)?)", re.I)

    @staticmethod
    def _parts(line: str) -> tuple[str, str, str]:
        if len(line) >= 7 and line[:6].isdigit():
            return line[:6], line[6:7], line[7:72].rstrip()
        return "", " ", line.rstrip()

    @classmethod
    def _body(cls, line: str) -> str:
        return cls._parts(line)[2].strip()

    @staticmethod
    def _fixed(body: str, indicator: str = " ") -> str:
        if len(body) > 65:
            raise ValueError(f"fixed-format body exceeds 65 columns: {body}")
        return f"000000{indicator}{body:<65}00000000"

    @staticmethod
    def _sql_identifier(field: str) -> str:
        return re.sub(r"-+", "_", field.strip().upper())

    def rewrite(self, cobol_text: str, *, original_idms_text: str = "") -> RewriteResult:
        """Rewrite every independently provable bounded cursor in the program.

        Each pass rewrites at most one cursor. Re-scanning the resulting text
        keeps all spans local to one parse and lets unrelated/unsupported
        cursors remain untouched. A hard pass limit protects against a broken
        rewriter that does not remove the selected declaration.
        """
        original = str(cobol_text or "")
        current = original
        diagnostics: list[str] = []
        changed = False
        for _ in range(32):
            result = self._rewrite_one(current, original_idms_text=original_idms_text)
            if not result.changed:
                # Once at least one cursor has been rewritten, the absence of
                # any remaining generated cursor is the normal fixed point,
                # not a diagnostic worth surfacing to conversion users.
                if result.diagnostic and not (
                    changed and "No generated WITH HOLD cursor declaration found" in result.diagnostic
                ):
                    diagnostics.append(result.diagnostic)
                break
            if result.diagnostic:
                diagnostics.append(result.diagnostic)
            if result.text == current:
                diagnostics.append("Rewrite reported success without changing text; stopped safely.")
                break
            current = result.text
            changed = True
        else:
            diagnostics.append("Stopped after 32 rewrite passes; remaining cursors were left unchanged.")

        if changed:
            return RewriteResult(
                current,
                True,
                f"Applied bounded singleton rewrite(s). {len(diagnostics)} diagnostic(s): "
                + " | ".join(diagnostics[-4:]),
            )
        return RewriteResult(original, False, diagnostics[-1] if diagnostics else "")

    def _rewrite_one(self, cobol_text: str, *, original_idms_text: str = "") -> RewriteResult:
        original = str(cobol_text or "")
        lines = original.splitlines()
        bodies = [self._body(line) for line in lines]
        upper = "\n".join(bodies).upper()
        source_first_only = self._source_proves_first_only(original_idms_text)
        marker_first = (
            "EXPANDED LRF FIRST" in upper
            or "EXPANDED LRF FIRST" in str(original_idms_text or "").upper()
        )
        # A FIRST marker is provenance for the operation, but it must not
        # override an explicit NEXT for that same target record in the source.
        marker_first_only = marker_first and not self._source_has_next_for_lrf_first(
            original_idms_text
        )
        lrf_cursor_provenance = marker_first or source_first_only
        if not lrf_cursor_provenance:
            return RewriteResult(original, False, "")

        # The generated LRF marker is also valid provenance when the IDMS
        # statement itself is no longer present in the expanded source passed
        # to this finishing pass. In that case, permit a non-WITH-HOLD cursor
        # only when the program contains exactly one cursor declaration; this
        # keeps the fallback scoped and avoids rewriting an unrelated cursor.
        lrf_first_only_proven = source_first_only or marker_first_only
        declarations = []
        for idx, body in enumerate(bodies):
            match = self._DECLARE.search(body)
            if match and ("WITH HOLD" in body.upper() or lrf_cursor_provenance):
                declarations.append((idx, match.group("cursor").upper()))
        if not declarations:
            return RewriteResult(original, False, "No generated WITH HOLD cursor declaration found; unchanged.")

        # Multiple cursors are allowed, but only one fully provable bounded
        # candidate is rewritten per pass. Unsupported cursors remain intact.
        candidates = []
        candidate_diagnostics = []
        for candidate_start, candidate_cursor in declarations:
            candidate_end = self._find_end_exec(bodies, candidate_start, lines)
            if candidate_end is None:
                candidate_diagnostics.append(f"{candidate_cursor}: declaration has no END-EXEC")
                continue
            candidate_sql = "\n".join(self._body(lines[i]) for i in range(candidate_start, candidate_end + 1))
            if not re.search(r"\bORDER\s+BY\b", candidate_sql, re.I) or not re.search(r"\bWHERE\b", candidate_sql, re.I):
                candidate_diagnostics.append(f"{candidate_cursor}: missing WHERE or ORDER BY")
                continue
            required_literals = self._source_lrf_filter_literals(original_idms_text)
            missing_literals = [
                literal for literal in required_literals
                if not re.search(r"=\s*" + re.escape(literal) + r"(?![A-Z0-9])", candidate_sql, re.I)
            ]
            if missing_literals:
                candidate_diagnostics.append(
                    f"{candidate_cursor}: source LRF path filters are absent from generated SQL "
                    f"({', '.join(missing_literals)}); cursor retained."
                )
                continue
            candidate_loop = self._find_bounded_loop(bodies, candidate_cursor, lines)
            if candidate_loop is None and lrf_first_only_proven and len(declarations) == 1:
                candidate_loop = self._find_first_only_loop(bodies, candidate_cursor, lines)
            if candidate_loop is None:
                candidate_diagnostics.append(f"{candidate_cursor}: no safe bounded/first-only LRF access")
                continue
            candidates.append((candidate_start, candidate_cursor, candidate_end, candidate_loop))

        if not candidates:
            detail = "; ".join(candidate_diagnostics[:4])
            return RewriteResult(original, False, f"No safe bounded cursor candidate; unchanged. {detail}")

        decl_start, cursor, decl_end, loop = candidates[0]
        loop_start, loop_end, predicate_field, predicate_literal, fetch_paragraph = loop
        cursor_sql_lines = [self._body(lines[i]) for i in range(decl_start, decl_end + 1)]
        cursor_sql = "\n".join(cursor_sql_lines)

        open_paragraph = self._paragraph_name(bodies, rf"\d+-OPEN-{re.escape(cursor)}")
        fetch_para = self._paragraph_name(bodies, rf"\d+-FETCH-{re.escape(cursor)}")
        close_para = self._paragraph_name(bodies, rf"\d+-CLOSE-{re.escape(cursor)}")
        if not (open_paragraph and fetch_para and close_para):
            return RewriteResult(original, False, "Matching OPEN/FETCH/CLOSE paragraphs are incomplete; unchanged.")
        if fetch_paragraph.upper() != fetch_para.upper():
            return RewriteResult(original, False, "Loop fetch does not match the cursor FETCH paragraph; unchanged.")

        fetch_start, fetch_end = self._paragraph_span(bodies, fetch_para)
        open_start, open_end = self._paragraph_span(bodies, open_paragraph)
        close_start, close_end = self._paragraph_span(bodies, close_para)
        if fetch_start is None or open_start is None or close_start is None:
            return RewriteResult(original, False, "OPEN/FETCH/CLOSE paragraph span cannot be resolved; unchanged.")
        fetch_text = "\n".join(bodies[fetch_start:fetch_end + 1])
        hosts = [m.group("host") for m in self._HOST.finditer(fetch_text)]
        # The FETCH cursor name itself is not a host variable. Verify the
        # positional SELECT/FETCH contract before converting cursor to INTO.
        selected_columns = self._select_columns(cursor_sql)
        if not hosts or not selected_columns:
            return RewriteResult(original, False, "SELECT/FETCH projection could not be parsed safely; unchanged.")
        if len(hosts) != len(selected_columns):
            return RewriteResult(
                original,
                False,
                f"SELECT/FETCH projection mismatch for {cursor}: {len(selected_columns)} columns vs {len(hosts)} host variables; unchanged.",
            )

        # Cursor FETCH lists often include columns used only to test the stop
        # condition or to order the cursor. A singleton SELECT should project
        # only child fields consumed by business logic after the loop. Resolve
        # those fields from qualified DCLGEN references, not name similarity.
        excluded_spans = (
            (open_start, open_end),
            (fetch_start, fetch_end),
            (close_start, close_end),
        )
        # FIRST-only LRF MODIFY/UPDATE is a record-resolution operation, not
        # a business-row scan. Select only the column(s) used to identify the
        # row in the subsequent UPDATE WHERE clause. Selecting SET columns
        # (for example NR_IDGOOD) overwrites the new input value in its DCLGEN
        # host variable with the old database value fetched from the cursor.
        first_only_candidate = not loop[2]
        update_key_projection = (
            self._update_where_projection(
                selected_columns,
                hosts,
                bodies,
                after=loop_end,
                excluded_spans=excluded_spans,
                source_lines=lines,
            )
            if first_only_candidate else None
        )
        if update_key_projection is not None:
            projection = update_key_projection
        else:
            projection = self._business_projection(
                selected_columns,
                hosts,
                bodies,
                after=loop_end,
                excluded_spans=excluded_spans,
            )
        if projection is None:
            return RewriteResult(original, False, "Could not prove a non-empty downstream SELECT projection; unchanged.")
        selected_columns, hosts = projection

        # A cursor paragraph can be removed only when the generated program
        # calls it in exactly the expected places: OPEN once, FETCH initially
        # and once in the loop, CLOSE once. Additional calls may be business
        # control flow, so fail closed rather than leaving dangling behavior.
        call_counts = {
            open_paragraph: self._count_calls(bodies, open_paragraph),
            fetch_para: self._count_calls(bodies, fetch_para),
            close_para: self._count_calls(bodies, close_para),
        }
        first_only = not predicate_field
        expected_fetch_calls = 1 if first_only else 2
        if (
            call_counts.get(open_paragraph) != 1
            or call_counts.get(fetch_para) != expected_fetch_calls
            or call_counts.get(close_para) != 1
        ):
            return RewriteResult(original, False, f"Unexpected cursor paragraph call counts {call_counts}; unchanged.")

        sql_lines = self._build_singleton_sql(
            cursor_sql_lines,
            cursor=cursor,
            selected_columns=selected_columns,
            hosts=hosts,
            predicate_field=predicate_field,
            predicate_literal=predicate_literal,
        )
        if not sql_lines:
            return RewriteResult(original, False, "Could not safely construct singleton SQL; unchanged.")

        # Locate the generated OPEN/CLOSE calls. A source-proven FIRST-only
        # access has a single inline FETCH UNTIL EOC and no initial FETCH call.
        open_call = self._find_call(bodies, open_paragraph, before=loop_start)
        close_call = self._find_call(bodies, close_para, after=loop_end)
        if open_call is None or close_call is None:
            return RewriteResult(original, False, "OPEN/CLOSE call sequence is incomplete; unchanged.")

        error_guard = [
            "    IF SQLCODE NOT = 0 AND SQLCODE NOT = 100",
            "       DISPLAY 'ERROR ON LRF SINGLETON SELECT'",
            "       PERFORM SQLERROR",
            "    END-IF.",
        ]

        replacements: list[tuple[int, int, list[str]]] = []
        replacements.append((decl_start, decl_end, ["*DB2: LRF cursor declaration replaced by singleton SELECT."]))
        if first_only:
            if any(
                self._body(lines[i]) and not self._body(lines[i]).startswith("*")
                for i in range(open_call + 1, loop_start)
            ):
                return RewriteResult(original, False, "Business statements between OPEN and FIRST fetch; unchanged.")
            replacements.append((open_call, loop_end, sql_lines + error_guard))
        else:
            first_fetch_call = self._find_call(bodies, fetch_para, before=loop_start, after=open_call)
            if first_fetch_call is None:
                return RewriteResult(original, False, "OPEN/initial FETCH/CLOSE call sequence is incomplete; unchanged.")
            if any(self._body(lines[i]) for i in range(open_call + 1, first_fetch_call)):
                return RewriteResult(original, False, "Business statements occur between OPEN and initial FETCH; unchanged.")
            replacements.append((open_call, first_fetch_call, sql_lines + error_guard))
            replacements.append((loop_start, loop_end, ["*DB2: Removed bounded loop; predicate moved to SQL."]))
        replacements.append((close_call, close_call, ["*DB2: Cursor CLOSE removed with singleton rewrite."]))

        # A source EOC branch may contain required business behavior (for
        # example DISPLAY diagnostics followed by CALL USERABEN). Do not delete
        # it. The old CLOSE overwrote SQLCODE before the branch, but this rewrite
        # replaces OPEN/FETCH/CLOSE with a singleton SELECT, so SQLCODE now
        # carries the SELECT's not-found result at this exact point. Rebind only
        # the condition and preserve every statement in the branch.
        eoc_if = next((i for i in range(close_call + 1, len(bodies))
                       if re.search(rf"\bIF\s+{re.escape(cursor)}-EOC\b", bodies[i], re.I)), None)
        if eoc_if is not None:
            eoc_end = self._matching_end_if(bodies, source_lines=lines, start=eoc_if)
            if eoc_end is None:
                return RewriteResult(original, False, "Post-CLOSE EOC branch is incomplete; unchanged.")
            # Inspect the complete outer branch, not merely the first END-IF.
            # A nested EOC reference after an inner END-IF would otherwise be
            # left behind when the cursor flag declaration is removed.
            if any(re.search(rf"\b{re.escape(cursor)}-EOC\b", bodies[i], re.I)
                   for i in range(eoc_if + 1, eoc_end + 1)):
                return RewriteResult(original, False, "Nested cursor EOC reference in not-found branch; unchanged.")
            replacements.append((eoc_if, eoc_if, [
                re.sub(rf"\bIF\s+{re.escape(cursor)}-EOC\b", "IF SQLCODE = 100", bodies[eoc_if], flags=re.I)
            ]))

        # The cursor flag is generated infrastructure, not business state.
        # Remove only declarations whose names are derived from this cursor.
        for idx, body in enumerate(bodies):
            if re.search(rf"\bWS-{re.escape(cursor)}-FLAG\b", body, re.I) or re.search(
                rf"\b88\s+{re.escape(cursor)}-(?:NOT-)?EOC\b", body, re.I
            ):
                replacements.append((idx, idx, ["*DB2: Removed obsolete cursor EOC flag declaration."]))

        for paragraph in (open_paragraph, fetch_para, close_para):
            start, end = self._paragraph_span(bodies, paragraph)
            if start is None:
                return RewriteResult(original, False, f"Could not locate generated paragraph {paragraph}; unchanged.")
            replacements.append((start, end, ["*DB2: Removed obsolete cursor paragraph."]))

        # Drop exact duplicate/overlapping replacement spans only if they are
        # identical; overlapping non-identical spans mean the pattern was not
        # sufficiently isolated, so refuse instead of risking code loss.
        ordered = sorted(replacements, key=lambda item: (item[0], item[1]))
        for left, right in zip(ordered, ordered[1:]):
            if right[0] <= left[1]:
                return RewriteResult(original, False, "Rewrite spans overlap; unchanged.")
        out = list(lines)
        for start, end, replacement in sorted(replacements, key=lambda item: item[0], reverse=True):
            out[start:end + 1] = [self._fixed(body[1:], "*") if body.startswith("*DB2:") else self._fixed(body) for body in replacement]

        # Correct the stale cursor-oriented diagnostic before re-sequencing;
        # replace only the source area so fixed-format columns stay intact.
        corrected = []
        for line in out:
            prefix, indicator, body = self._parts(line)
            body = re.sub(
                r"DISPLAY\s+'[^']*\s+NOT FOUND\s*:\s*'",
                "DISPLAY 'NO DATA FOUND FOR BOUNDED LRF SELECT'",
                body,
                flags=re.I,
            )
            body = re.sub(
                r"DB2: Parent not-found is handled by the keyed SELECT SQLCODE.*",
                "DB2: Bounded singleton SELECT no-data handling follows.",
                body,
                flags=re.I,
            )
            if body.strip() == "check.":
                body = ""
            corrected.append(f"{prefix}{indicator}{body:<65}" if prefix else body)
        out = corrected

        # Re-sequence fixed-format records after structural edits. Preserve
        # indicator columns and source-area bodies for untouched records.
        resequenced = []
        for index, line in enumerate(out, start=1):
            _old_seq, indicator, body = self._parts(line)
            if len(body) > 65:
                return RewriteResult(original, False, f"Output line {index} exceeds fixed-format source area; unchanged.")
            sequence = index * 10
            resequenced.append(f"{sequence:06d}{indicator}{body:<65}{sequence * 1000:08d}")
        rewritten = "\n".join(resequenced) + ("\n" if original.endswith("\n") else "")
        if predicate_field and predicate_literal:
            reason = f"using predicate {predicate_field} = {predicate_literal}"
        else:
            reason = "for source-proven FIRST-only access"
        return RewriteResult(rewritten, True, f"Rewrote cursor {cursor} to singleton SELECT {reason}.")

    @classmethod
    def _select_columns(cls, cursor_sql: str) -> list[str]:
        """Parse the generated simple-column SELECT projection or fail closed."""
        match = re.search(r"\bSELECT\s+(.*?)\s+FROM\b", cursor_sql, re.I | re.S)
        if not match:
            return []
        columns = [part.strip().lstrip(",").strip() for part in match.group(1).split(",")]
        if not columns or any(not re.fullmatch(r"[A-Z][A-Z0-9_]*", column, re.I) for column in columns):
            return []
        return columns

    @classmethod
    def _update_where_projection(
        cls,
        selected_columns: list[str],
        hosts: list[str],
        bodies: list[str],
        *,
        after: int,
        excluded_spans: tuple[tuple[int | None, int | None], ...],
        source_lines: list[str] | None = None,
    ) -> tuple[list[str], list[str]] | None:
        """Project only cursor columns used by a following UPDATE's WHERE.

        This preserves input values bound in UPDATE SET. It intentionally
        returns None unless a complete UPDATE statement and a resolvable WHERE
        host-variable set are found, leaving other FIRST-only patterns on the
        established conservative projection path.
        """
        if len(selected_columns) != len(hosts) or not selected_columns:
            return None
        excluded: set[int] = set()
        for start, end in excluded_spans:
            if start is None or end is None:
                return None
            excluded.update(range(start, end + 1))

        for start in range(after + 1, len(bodies)):
            if start in excluded or not re.search(r"\bEXEC\s+SQL\b", bodies[start], re.I):
                continue
            # Reuse the validated SQL-boundary scanner: UPDATE statements can
            # also be long, and comment text must not masquerade as END-EXEC.
            # Unlike a fixed look-ahead, this handles long statements while
            # refusing to cross into another SQL block or a paragraph label.
            end = cls._find_end_exec(bodies, start, source_lines)
            if end is None:
                continue
            statement = " ".join(
                bodies[idx] for idx in range(start, end + 1) if idx not in excluded
            )
            if not re.search(r"\bUPDATE\s+[A-Z][A-Z0-9_]*\b", statement, re.I):
                continue
            where_match = re.search(r"\bWHERE\b(?P<where>.*?)(?:\bQUERYNO\b|\bEND-EXEC\b|$)",
                                    statement, re.I | re.S)
            if not where_match:
                continue
            where_hosts = [m.group("host") for m in cls._HOST.finditer(where_match.group("where"))]
            if not where_hosts:
                continue
            selected_by_host = {host.upper(): (column, host) for column, host in zip(selected_columns, hosts)}
            if any(host.upper() not in selected_by_host for host in where_hosts):
                return None
            ordered_hosts: list[str] = []
            ordered_columns: list[str] = []
            for host in where_hosts:
                pair = selected_by_host[host.upper()]
                if host.upper() not in {value.upper() for value in ordered_hosts}:
                    ordered_columns.append(pair[0])
                    ordered_hosts.append(pair[1])
            return (ordered_columns, ordered_hosts) if ordered_columns else None
        return None

    @classmethod
    def _business_projection(
        cls,
        selected_columns: list[str],
        hosts: list[str],
        bodies: list[str],
        *,
        after: int,
        excluded_spans: tuple[tuple[int | None, int | None], ...],
    ) -> tuple[list[str], list[str]] | None:
        """Return SELECT/FETCH pairs actually consumed by downstream logic.

        Only fully qualified references to the child DCLGEN are considered.
        Ordering follows the first downstream use, which keeps the generated
        SELECT/INTO readable and aligns it with business usage. If the source
        projection cannot be mapped unambiguously, refuse the rewrite.
        """
        if len(selected_columns) != len(hosts) or not selected_columns:
            return None

        excluded: set[int] = set()
        for start, end in excluded_spans:
            if start is None or end is None:
                return None
            excluded.update(range(start, end + 1))

        tail = [(idx, body) for idx, body in enumerate(bodies) if idx > after and idx not in excluded]

        # Fail closed if business code reads a child-DCLGEN field that the
        # cursor never selected/fetched. This catches the subtle stale-output
        # defect where NR-CI1POS / NR-CI26POS are consumed after FETCH but are
        # absent from both cursor SELECT and FETCH lists. A singleton rewrite
        # must not turn that pre-existing projection bug into a green release.
        host_fields = {host.split(".", 1)[1].upper() for host in hosts}
        host_groups = {host.split(".", 1)[0].upper() for host in hosts}
        for line_index, body in tail:
            if body.lstrip().startswith("*"):
                continue
            for ref in re.finditer(
                r"\b(?P<field>[A-Z][A-Z0-9-]*)\s+OF\s+(?P<group>DCL[A-Z0-9-]*)\b",
                body,
                re.I,
            ):
                field = ref.group("field").upper()
                group = ref.group("group").upper()
                if group not in host_groups:
                    continue
                before = body[:ref.start()].upper().rstrip()
                # A reference after TO is a receiving field, not a value
                # read by the business statement. Do not require it in SELECT.
                if re.search(r"\bTO\s*$", before):
                    continue
                if field not in host_fields:
                    return None

        pairs: list[tuple[int, str, str]] = []
        seen_hosts: set[str] = set()
        for column, host in zip(selected_columns, hosts):
            # Generated FETCH hosts have the form DCLDZEVEFTV.FIELD-NAME.
            if not re.fullmatch(r"DCL[A-Z0-9-]*\.[A-Z][A-Z0-9-]*", host, re.I):
                return None
            group, field = host.split(".", 1)
            host_key = f"{group.upper()}.{field.upper()}"
            if host_key in seen_hosts:
                return None
            seen_hosts.add(host_key)
            ref = re.compile(
                rf"(?:\b{re.escape(field)}\s+OF\s+{re.escape(group)}\b|"
                rf"\b{re.escape(group)}\s*\.\s*{re.escape(field)}\b)",
                re.I,
            )
            first_use = None
            for line_index, body in tail:
                if body.lstrip().startswith("*"):
                    continue
                match = ref.search(body)
                if match:
                    first_use = (line_index * 1000) + match.start()
                    break
            if first_use is not None:
                pairs.append((first_use, column, host))

        if not pairs:
            return None
        pairs.sort(key=lambda item: item[0])
        return [item[1] for item in pairs], [item[2] for item in pairs]

    @staticmethod
    def _count_calls(bodies: list[str], paragraph: str) -> int:
        pattern = re.compile(rf"\bPERFORM\s+{re.escape(paragraph)}\b", re.I)
        return sum(bool(pattern.search(body)) for body in bodies)

    @staticmethod
    def _sql_terminator_on_line(
        body: str,
        in_block_comment: bool = False,
        quote: str | None = None,
    ) -> tuple[bool, bool, str | None]:
        """Return whether END-EXEC occurs outside SQL/COBOL lexical comments.

        Terminator-like text inside SQL string literals, quoted identifiers,
        SQL comments, or COBOL inline comments is data, not a block boundary.
        The block-comment and quote states are carried between physical lines.
        """
        index = 0
        while index < len(body):
            if in_block_comment:
                close = body.find("*/", index)
                if close < 0:
                    return False, True, quote
                index = close + 2
                in_block_comment = False
                continue

            char = body[index]
            if quote:
                if char == quote:
                    # SQL escapes quote delimiters by doubling them.
                    if index + 1 < len(body) and body[index + 1] == quote:
                        index += 2
                        continue
                    quote = None
                index += 1
                continue

            if char in {"'", '"'}:
                quote = char
                index += 1
                continue
            if body.startswith("--", index) or body.startswith("*>", index):
                return False, False, quote
            if body.startswith("/*", index):
                in_block_comment = True
                index += 2
                continue
            terminator = re.match(r"END-EXEC\b", body[index:], re.I)
            if terminator and (index == 0 or not (body[index - 1].isalnum() or body[index - 1] in "_-")):
                return True, False, quote
            index += 1
        return False, in_block_comment, quote

    @classmethod
    def _find_end_exec(
        cls,
        bodies: list[str],
        start: int,
        source_lines: list[str] | None = None,
    ) -> int | None:
        """Find the matching SQL terminator without an arbitrary line limit.

        Long generated SELECT statements can legitimately exceed 80 physical
        lines. Search to the end of the source, while respecting quoted data
        and SQL/COBOL comments so terminator-like text cannot truncate a block.
        Fail closed if a new EXEC SQL or a fixed-format numeric paragraph label
        appears before the real terminator.
        """
        in_block_comment = False
        quote: str | None = None
        for idx in range(start, len(bodies)):
            if source_lines is not None and idx < len(source_lines):
                _sequence, indicator, _body = cls._parts(source_lines[idx])
                if indicator in ("*", "/", "D", "d"):
                    continue
            body = bodies[idx]
            is_terminator, in_block_comment, quote = cls._sql_terminator_on_line(
                body, in_block_comment, quote
            )
            if is_terminator:
                return idx
            if in_block_comment:
                continue
            if idx == start:
                continue
            if re.search(r"\bEXEC\s+SQL\b", body, re.I):
                return None
            # A missing END-EXEC must not let the scan drift through an
            # ordinary named COBOL paragraph and accidentally bind a later
            # terminator to this SQL block. Fixed-format paragraph labels
            # belong in Area A (columns 8-11); use the original physical line
            # to distinguish them from indented SQL clauses. Keep the legacy
            # numeric-label check for helper callers without source context.
            if source_lines is not None and idx < len(source_lines):
                _sequence, _indicator, source_body = cls._parts(source_lines[idx])
                is_area_a_label = (
                    len(source_body) - len(source_body.lstrip()) <= 3
                    and re.fullmatch(r"\s*[A-Z][A-Z0-9-]*\.\s*", source_body, re.I)
                    is not None
                )
                if is_area_a_label:
                    return None
            elif re.match(r"^\s*\d{1,6}-[A-Z0-9-]+\.\s*$", body, re.I):
                return None
        return None

    @classmethod
    def _source_lrf_filter_literals(cls, source_text: str) -> list[str]:
        """Extract literals from explicit LRF extra-filter comments for a safety check."""
        if not source_text:
            return []
        lines = source_text.splitlines()
        collected: list[str] = []
        for index, line in enumerate(lines):
            _seq, indicator, body = cls._parts(line)
            if "extra filter:" not in body.lower() and "add to the generated cursor where" not in body.lower():
                continue
            combined = body
            for next_index in range(index + 1, min(index + 4, len(lines))):
                _seq2, indicator2, body2 = cls._parts(lines[next_index])
                if indicator2 not in ("*", "/"):
                    break
                combined += " " + body2
                if "add to the generated cursor where" in combined.lower():
                    break
            if "add to the generated cursor where" not in combined.lower():
                continue
            condition_text = combined
            if "extra filter:" in combined.lower():
                condition_text = re.split(r"extra filter:", combined, maxsplit=1, flags=re.I)[-1]
            condition_text = re.split(r"-\s*add to the generated cursor WHERE", condition_text, maxsplit=1, flags=re.I)[0]
            collected.extend(
                match.group(1)
                for match in re.finditer(r"=\s*('[^']*'|\"[^\"]*\"|[+-]?\d+)", condition_text)
            )
        return list(dict.fromkeys(collected))

    @classmethod
    def _source_accesses(cls, source_text: str) -> list[tuple[str, str]]:
        """Return active OBTAIN/FIND FIRST/NEXT accesses across wrapped lines.

        IDMS statements are frequently wrapped in the source listing. Scanning
        each physical record independently misses a NEXT when its verb, access
        kind, or record name is split across records and can incorrectly prove
        FIRST-only semantics. Mask comments/literals per physical record first,
        then scan the joined executable text so quoted examples and comments
        still cannot act as source evidence.
        """
        if not source_text:
            return []
        executable_lines: list[str] = []
        for line in source_text.splitlines():
            _prefix, indicator, body = cls._parts(line)
            if indicator in ("*", "/", "D", "d"):
                executable_lines.append("")
                continue
            executable_lines.append(cls._mask_literals_and_inline_comment(body))
        executable = " ".join(executable_lines)
        pattern = re.compile(
            r"\b(?:OBTAIN|FIND)\s+(?P<verb>FIRST|NEXT)\s+"
            r"(?P<record>[A-Z][A-Z0-9-]*)\b",
            re.I,
        )
        return [
            (match.group("verb").upper(), match.group("record").upper())
            for match in pattern.finditer(executable)
        ]

    @classmethod
    def _source_proves_first_only(cls, source_text: str) -> bool:
        """Prove one source OBTAIN/FIND FIRST with no matching NEXT."""
        accesses = cls._source_accesses(source_text)
        firsts = [record for verb, record in accesses if verb == "FIRST"]
        if len(firsts) != 1:
            return False
        record = firsts[0]
        return not any(verb == "NEXT" and candidate == record for verb, candidate in accesses)

    @classmethod
    def _source_has_next_for_lrf_first(cls, source_text: str) -> bool:
        """Guard marker-only fallback against an explicit NEXT of its target."""
        if not source_text:
            return False
        marker_records: list[str] = []
        for line in source_text.splitlines():
            _prefix, _indicator, body = cls._parts(line)
            if "EXPANDED LRF FIRST" not in body.upper():
                continue
            match = re.search(r"->\s*(?P<record>[A-Z][A-Z0-9-]*)", body, re.I)
            if match:
                marker_records.append(match.group("record").upper())
        accesses = cls._source_accesses(source_text)
        if marker_records:
            return any(
                verb == "NEXT" and record in marker_records
                for verb, record in accesses
            )
        # Without an explicit target on the marker, be conservative if any
        # active NEXT appears in the source.
        return any(verb == "NEXT" for verb, _record in accesses)

    @classmethod
    def _find_first_only_loop(cls, bodies: list[str], cursor: str, source_lines: list[str]):
        """Find a generated single-line FETCH UNTIL EOC for source FIRST-only access."""
        fetch_pattern = re.compile(
            rf"^\s*PERFORM\s+(?P<para>\d+-FETCH-{re.escape(cursor)})\s+UNTIL\s+{re.escape(cursor)}-EOC\.?\s*$",
            re.I,
        )
        matches = []
        for index, body in enumerate(bodies):
            if cls._parts(source_lines[index])[1] in ("*", "/"):
                continue
            match = fetch_pattern.match(body.strip())
            if match:
                matches.append((index, index, "", "", match.group("para").upper()))
        return matches[0] if len(matches) == 1 else None

    def _find_bounded_loop(self, bodies: list[str], cursor: str, source_lines: list[str]):
        candidates = []
        for start, body in enumerate(bodies):
            if self._parts(source_lines[start])[1] in ("*", "/"):
                continue
            until_match = self._PERFORM_UNTIL.search(body)
            if not until_match:
                continue
            # Match the END-PERFORM belonging to this loop, not merely the
            # first one that appears in the next 30 physical lines. COBOL can
            # nest inline PERFORM blocks; using the first terminator can make
            # the rewrite remove only an inner block and leave invalid or
            # semantically changed control flow behind.
            depth = 1
            end = None
            search_end = min(len(bodies), start + 200)
            for index in range(start + 1, search_end):
                if self._parts(source_lines[index])[1] in ("*", "/"):
                    continue
                body_i = bodies[index]
                opens = len(re.findall(r"\bPERFORM\s+UNTIL\b", body_i, re.I))
                closes = len(self._END_PERFORM.findall(body_i))
                depth += opens - closes
                if depth <= 0:
                    end = index
                    break
            if end is None:
                continue
            block_lines = [
                "" if self._parts(source_lines[index])[1] in ("*", "/") else bodies[index]
                for index in range(start, end + 1)
            ]
            # This renderer cannot preserve arbitrary nested control flow.
            # Even if nesting is balanced, reject any nested inline loop
            # instead of treating its END-PERFORM as the singleton loop end.
            if any(
                re.search(r"\bPERFORM\s+UNTIL\b", line, re.I)
                for line in block_lines[1:]
            ):
                continue
            fetch_matches = []
            fetch_pattern = re.compile(
                rf"\bPERFORM\s+(?P<para>\d+-FETCH-{re.escape(cursor)})\b",
                re.I,
            )
            for offset, line in enumerate(block_lines):
                for match in fetch_pattern.finditer(line):
                    fetch_matches.append((offset, match.group("para")))
            if len(fetch_matches) != 1:
                continue
            fetch_offset, fetch_paragraph = fetch_matches[0]

            # The loop may contain only the cursor FETCH. A loop with business
            # work cannot be deleted just because one FETCH call was found.
            tail = block_lines[fetch_offset + 1:]
            if any(line.strip() and not self._END_PERFORM.search(line) for line in tail):
                continue
            if not self._END_PERFORM.search(block_lines[-1]):
                continue

            # Parse the complete UNTIL condition after joining physical lines.
            # This handles a field name and its equality operator being split
            # across fixed-format records without treating the line break as
            # a semantic boundary.
            condition = " ".join(block_lines[:fetch_offset])
            condition = re.sub(r"^.*?\bPERFORM\s+UNTIL\b", "", condition, count=1, flags=re.I)
            condition = re.sub(r"\s+", " ", condition).strip()
            if re.search(r"\bSQLCODE\s*=\s*100\b", condition, re.I):
                continue
            if re.search(r"\b(?:MOVE|DISPLAY|CALL|COMPUTE|ADD|SUBTRACT|MULTIPLY|DIVIDE)\b", condition, re.I):
                continue
            predicates = [
                match for match in self._PREDICATE.finditer(condition)
                if match.group("field").upper() not in {"SQLCODE", "EOC", "END-OF-CURSOR"}
            ]
            if len(predicates) != 1:
                continue
            pred = predicates[0]
            # A bounded rewrite is valid only when the loop condition consists
            # of the end-of-cursor guard plus exactly one literal equality.
            without_predicate = condition[:pred.start()] + " " + condition[pred.end():]
            without_predicate = re.sub(r"\b(?:OR|AND)\b", " ", without_predicate, flags=re.I)
            without_predicate = re.sub(r"[()]+", " ", without_predicate)
            without_predicate = re.sub(r"\b(?:[A-Z0-9-]+-EOC|EOC|END-OF-CURSOR)\b", " ", without_predicate, flags=re.I)
            if re.sub(r"\s+", "", without_predicate):
                continue
            candidates.append((start, end, pred.group("field").upper(), pred.group("literal"), fetch_paragraph))
        return candidates[0] if len(candidates) == 1 else None

    @classmethod
    def _matching_end_if(
        cls,
        bodies: list[str],
        *,
        source_lines: list[str],
        start: int,
    ) -> int | None:
        """Find the matching END-IF for a branch, balancing nested IF blocks.

        Comments and quoted literals are masked before counting tokens so text
        such as DISPLAY 'END-IF' cannot close a business branch prematurely.
        """
        depth = 0
        for index in range(start, len(bodies)):
            _sequence, indicator, _body = cls._parts(source_lines[index])
            if indicator in ("*", "/", "D", "d"):
                continue
            code = cls._mask_literals_and_inline_comment(bodies[index])
            closes = len(re.findall(r"\bEND-IF\b", code, re.I))
            without_closes = re.sub(r"\bEND-IF\b", " ", code, flags=re.I)
            opens = len(re.findall(r"\bIF\b", without_closes, re.I))
            depth += opens - closes
            if depth <= 0 and index >= start:
                return index
        return None

    @staticmethod
    def _mask_literals_and_inline_comment(text: str) -> str:
        """Mask COBOL quoted literals and inline comments while retaining code."""
        chars = list(text)
        quote = None
        index = 0
        while index < len(chars):
            char = chars[index]
            if quote:
                chars[index] = " "
                if char == quote:
                    if index + 1 < len(chars) and chars[index + 1] == quote:
                        chars[index + 1] = " "
                        index += 2
                        continue
                    quote = None
            elif char in ("'", '"'):
                quote = char
                chars[index] = " "
            elif char == "*" and index + 1 < len(chars) and chars[index + 1] == ">":
                for rest in range(index, len(chars)):
                    chars[rest] = " "
                break
            index += 1
        return "".join(chars)

    @staticmethod
    def _paragraph_name(bodies: list[str], pattern: str) -> str | None:
        regex = re.compile(rf"^\s*(?P<name>{pattern})\.?\s*$", re.I)
        for body in bodies:
            match = regex.match(body.strip())
            if match:
                return match.group("name").upper()
        return None

    @staticmethod
    def _paragraph_span(bodies: list[str], paragraph: str) -> tuple[int | None, int | None]:
        start = next((i for i, body in enumerate(bodies) if re.match(rf"^\s*{re.escape(paragraph)}\.?\s*$", body, re.I)), None)
        if start is None:
            return None, None
        header = re.compile(r"^\s*(?:\d{1,6}-[A-Z0-9-]+|[A-Z][A-Z0-9-]*)\.\s*$", re.I)
        end = len(bodies) - 1
        for idx in range(start + 1, len(bodies)):
            if header.match(bodies[idx].strip()):
                end = idx - 1
                break
        return start, end

    @staticmethod
    def _find_call(bodies: list[str], paragraph: str, *, before: int | None = None, after: int | None = None) -> int | None:
        regex = re.compile(rf"\bPERFORM\s+{re.escape(paragraph)}\b", re.I)
        for idx, body in enumerate(bodies):
            if before is not None and idx >= before:
                continue
            if after is not None and idx <= after:
                continue
            if regex.search(body):
                return idx
        return None

    def _build_singleton_sql(self, declaration_lines: list[str], *, cursor: str, selected_columns: list[str], hosts: list[str], predicate_field: str, predicate_literal: str) -> list[str]:
        bodies = [self._body(line) for line in declaration_lines]
        sql = "\n".join(bodies)
        sql = re.sub(rf"\bEXEC\s+SQL\s+DECLARE\s+{re.escape(cursor)}\s+CURSOR(?:\s+WITH\s+HOLD)?\s+FOR\b", "EXEC SQL", sql, flags=re.I)
        sql = re.sub(r"\bFOR\s+READ\s+ONLY\b", "", sql, flags=re.I)
        sql = re.sub(r"\bDECLARE\s+\w+\s+CURSOR(?:\s+WITH\s+HOLD)?\s+FOR\b", "", sql, flags=re.I)
        sql = re.sub(r"\bEND-EXEC\.?\s*$", "", sql, flags=re.I).strip()
        # Replace the cursor's broad FETCH projection with only the fields
        # consumed by downstream business logic. Pair order is derived from
        # those uses, and INTO is generated from the exact same ordered pairs.
        from_match = re.search(r"\bFROM\s+", sql, re.I)
        select_match = re.search(r"\bSELECT\s+.*?\s+FROM\s+", sql, re.I | re.S)
        if not from_match or not select_match or len(selected_columns) != len(hosts) or not hosts:
            return []
        select_projection = "SELECT " + ",\n   ".join(selected_columns) + "\n"
        sql = sql[:select_match.start()] + select_projection + sql[select_match.end() - len("FROM "):]
        from_match = re.search(r"\bFROM\s+", sql, re.I)
        if not from_match:
            return []
        into = ["INTO"] + [f"   :{host}," if i < len(hosts) - 1 else f"   :{host}" for i, host in enumerate(hosts)]
        sql = sql[:from_match.start()] + "\n" + "\n".join(into) + "\n" + sql[from_match.start():]
        order_match = re.search(r"\bORDER\s+BY\b", sql, re.I)
        if not order_match:
            return []
        if predicate_field and predicate_literal:
            predicate = f"AND {self._sql_identifier(predicate_field)} = {predicate_literal}"
            sql = sql[:order_match.start()] + predicate + "\n" + sql[order_match.start():]
        queryno_match = re.search(r"\bQUERYNO\s+\d+\b", sql, re.I)
        if queryno_match:
            sql = sql[:queryno_match.start()] + "FETCH FIRST 1 ROW ONLY\n" + sql[queryno_match.start():]
        else:
            sql = sql.rstrip() + "\nFETCH FIRST 1 ROW ONLY"
        # Rebuild SQL with one line per logical clause/column, then fixed-format.
        logical_lines = [part.strip() for part in sql.splitlines() if part.strip()]
        if not logical_lines[0].upper().startswith("EXEC SQL"):
            logical_lines.insert(0, "EXEC SQL")
        if not any("FETCH FIRST 1 ROW ONLY" in line.upper() for line in logical_lines):
            return []
        # Apply standard fixed-format Area A / Area B placement. The SQL
        # block is embedded in COBOL: EXEC SQL / END-EXEC are in Area B,
        # SQL clauses are indented under them, and list items/predicates are
        # indented one additional level. No body may exceed columns 8-72.
        output: list[str] = []
        clause_prefixes = (
            "SELECT", "INTO", "FROM", "WHERE", "AND", "OR ",
            "ORDER BY", "FETCH FIRST", "QUERYNO",
        )
        for line in logical_lines:
            line = re.sub(r"\s+", " ", line).strip()
            upper_line = line.upper()
            if upper_line == "FOR READ ONLY":
                continue

            if upper_line.startswith("EXEC SQL"):
                rendered = "    " + line
            elif upper_line == "END-EXEC":
                rendered = "    END-EXEC"
            elif upper_line.startswith(clause_prefixes):
                rendered = "       " + line
            else:
                rendered = "          " + line

            if len(rendered) <= 65:
                output.append(rendered)
                continue

            # A long WHERE/AND equality commonly has a long DCLGEN host
            # variable. Break before the RHS; COBOL/SQL tokens stay intact.
            predicate_match = re.match(
                r"^(WHERE|AND|OR)\s+(.+?)\s*=\s*(.+)$",
                line,
                flags=re.IGNORECASE,
            )
            if predicate_match:
                keyword, lhs, rhs = predicate_match.groups()
                first = "       " + keyword.upper() + " " + lhs.strip() + " ="
                second = "          " + rhs.strip()
                if len(first) <= 65 and len(second) <= 65:
                    output.extend([first, second])
                    continue

            # General SQL wrapping: break only at whitespace and never split
            # an identifier, host variable, quoted literal, or numeric token.
            words = line.split()
            first_indent = "          " if not upper_line.startswith(clause_prefixes) else "       "
            current = first_indent
            wrapped: list[str] = []
            for word in words:
                candidate = current + ("" if current.endswith(" ") else " ") + word
                if len(candidate) > 65 and current.strip():
                    wrapped.append(current.rstrip())
                    current = "          " + word
                else:
                    current = candidate
            if current.strip():
                wrapped.append(current.rstrip())
            if any(len(item) > 65 for item in wrapped):
                return []
            output.extend(wrapped)

        if not output or not any(line.strip().upper() == "    END-EXEC" for line in output):
            output.append("    END-EXEC")
        return output


__all__ = ["BoundedLrfSingletonRewriter", "RewriteResult"]
