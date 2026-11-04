"""Conservative planner for hand-written retrieval OBTAIN CALC reads.

A read is eligible only when Sheet Mapping and DCLGEN prove every CALC key,
source shows an unconditional MOVE to every key field before the access in the
same paragraph, and the following status logic uses the supported
ERROR-STATUS zero/non-zero guards. No program or table names are hardcoded.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from converter.services.name_normalizer import NameNormalizer


@dataclass(frozen=True)
class HandwrittenCalcReadPlan:
    record: str
    table: str
    key_columns: tuple[str, ...]
    existence_column: str
    dclgen_group: str


class HandwrittenObtainCalcPlanner:
    _FIELD = re.compile(r"^\s*(?P<level>\d{1,2})\s+(?P<name>[A-Z0-9-]+)", re.I)
    _ACCESS = re.compile(r"\bOBTAIN\s+CALC\s+(?P<record>[A-Z][A-Z0-9-]*)\b", re.I)
    _PARAGRAPH = re.compile(r"^[A-Z0-9][A-Z0-9-]*\.$", re.I)
    _MOVE_TO_FIELD = re.compile(
        r"\bMOVE\s+(?!CORR\b)(?P<src>[A-Z0-9-]+(?:\s+OF\s+[A-Z0-9-]+)?)\s+TO\s+"
        r"(?P<field>[A-Z][A-Z0-9-]*)\s+(?:OF|IN)\s+(?P<record>[A-Z][A-Z0-9-]*)\b",
        re.I,
    )
    _IF_OPEN = re.compile(r"^IF\b", re.I)
    _IF_CLOSE = re.compile(r"^END-IF\b", re.I)
    _EVALUATE_OPEN = re.compile(r"^EVALUATE\b", re.I)
    _EVALUATE_CLOSE = re.compile(r"^END-EVALUATE\b", re.I)
    _SUPPORTED_STATUS_IF = re.compile(
        r"^IF\s+ERROR-STATUS\s+(?:NOT\s+)?=\s*(['\"])0000\1\s*\.?$", re.I
    )

    def __init__(self, mapping_repository, table_name_resolver, host_variable_resolver):
        self.mapping = mapping_repository
        self.table_resolver = table_name_resolver
        self.hosts = host_variable_resolver

    def plan(self, source_text: str, *, excluded_records=()) -> tuple[dict[str, dict[str, str]], list[str]]:
        lines = self._logical_lines(source_text)
        excluded = {NameNormalizer.normalize(value) for value in (excluded_records or ())}
        accesses: dict[str, list[int]] = {}
        for index, line in enumerate(lines):
            match = self._ACCESS.search(line)
            if match:
                record = NameNormalizer.normalize(match.group("record"))
                accesses.setdefault(record, []).append(index)

        plans: dict[str, dict[str, str]] = {}
        diagnostics: list[str] = []
        for record, positions in accesses.items():
            if record in excluded:
                continue
            if len(positions) != 1:
                diagnostics.append(
                    f"Hand-written OBTAIN CALC {record}: found {len(positions)} accesses; "
                    "per-access key state is ambiguous, so source is retained."
                )
                continue
            access_index = positions[0]
            plan, reason = self._plan_one(lines, access_index, record)
            if plan is None:
                diagnostics.append(f"Hand-written OBTAIN CALC {record}: {reason}; source retained.")
                continue
            plans[record] = {
                "table": plan.table,
                "existence_column": plan.existence_column,
                "dclgen_group": plan.dclgen_group,
                "key_columns": " ".join(plan.key_columns),
            }
            diagnostics.append(
                f"Hand-written OBTAIN CALC {record}: proved {len(plan.key_columns)} key host(s) "
                f"and status guards; keyed existence SELECT is enabled."
            )
        return plans, diagnostics

    def _plan_one(self, lines: list[str], access_index: int, record: str):
        try:
            rows = list(self.mapping.rows_for_record(record) or [])
        except Exception:  # noqa: BLE001
            return None, "mapping lookup failed"
        table = self.table_resolver.table_for_record(record)
        if not table:
            return None, "no DB2 table is resolved"

        key_fields: list[tuple[str, str]] = []
        for row in rows:
            raw_zone = str(getattr(row, "cobol_zone", "") or "")
            field_match = self._FIELD.match(raw_zone)
            if not field_match:
                continue
            field_name = NameNormalizer.to_cobol(field_match.group("name"))
            idms_key = NameNormalizer.normalize(getattr(row, "idms_key", ""))
            db2_key = NameNormalizer.normalize(getattr(row, "db2_key", ""))
            column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            if not field_name or not column:
                continue
            key_text = f"{idms_key} {db2_key}"
            if "CALC" not in idms_key:
                continue
            if "FOREIGN" in key_text or db2_key == "FK":
                continue
            # Match the shared mapping key resolver: CALC is a key even when
            # the spreadsheet's DB2-key label is blank. Do not under-count a
            # key that the SQL builder will later place in the WHERE clause.
            is_key = (
                "PRIMARY" in db2_key
                or db2_key == "KEY"
                or "PRIMARY" in idms_key
                or idms_key == "KEY"
                or "CALC" in idms_key
            )
            if not is_key:
                continue
            if not self.hosts.host_reference_for_column(table, column):
                return None, f"DCLGEN host for key column {column} is missing"
            key_fields.append((field_name, column))

        # Preserve mapping order while dropping duplicates.
        key_fields = list(dict.fromkeys(key_fields))
        if not key_fields:
            return None, "Sheet Mapping has no complete mapped CALC key"

        paragraph_start = 0
        for index in range(access_index - 1, -1, -1):
            if self._PARAGRAPH.match(lines[index].strip()):
                paragraph_start = index + 1
                break
        segment = lines[paragraph_start:access_index]

        assigned: dict[str, int] = {}
        nesting = 0
        for offset, line in enumerate(segment):
            code = line.strip()
            if self._IF_OPEN.match(code) or self._EVALUATE_OPEN.match(code):
                nesting += 1
            move = self._MOVE_TO_FIELD.search(code)
            if move and NameNormalizer.normalize(move.group("record")) == record:
                field = NameNormalizer.to_cobol(move.group("field"))
                if any(field == expected for expected, _column in key_fields):
                    if nesting:
                        return None, f"key field {field} is assigned inside conditional logic"
                    assigned[field] = paragraph_start + offset
            if self._IF_CLOSE.match(code) or self._EVALUATE_CLOSE.match(code):
                nesting = max(0, nesting - 1)

        missing = [field for field, _column in key_fields if field not in assigned]
        if missing:
            return None, "key fields are not all assigned before access: " + ", ".join(missing)

        # A whole-record write after the last key assignment can invalidate
        # the proof. A prior MOVE SPACES/INITIALIZE is allowed because each
        # key component is subsequently assigned explicitly.
        last_key_assignment = max(assigned.values())
        for line in lines[last_key_assignment + 1:access_index]:
            code = line.strip().upper()
            if re.search(rf"\b(?:INITIALIZE|MOVE\b.+\bTO)\s+{re.escape(record)}\b", code):
                return None, "whole-record write occurs after key assignment"

        # Require the next status-dependent branch to be expressible in the
        # SQLCODE domain. Stop before another data access or paragraph.
        following: list[str] = []
        for line in lines[access_index + 1:]:
            code = line.strip()
            if self._PARAGRAPH.match(code) or self._ACCESS.search(code):
                break
            if re.search(r"\b(?:OBTAIN|FIND|STORE|MODIFY|ERASE)\s+(?:FIRST|NEXT|CALC|CURRENT)\b", code, re.I):
                break
            following.append(code)
        status_ifs = [line for line in following if re.search(r"^IF\s+ERROR-STATUS\b", line, re.I)]
        if not status_ifs or any(not self._SUPPORTED_STATUS_IF.match(line) for line in status_ifs):
            return None, "following ERROR-STATUS branches are absent or unsupported"
        if not any(re.search(r"^IF\s+ERROR-STATUS\s+NOT\s*=", line, re.I) for line in status_ifs):
            return None, "non-zero ERROR-STATUS branch is not present"
        if not any(re.search(r"^IF\s+ERROR-STATUS\s*=", line, re.I) for line in status_ifs):
            return None, "zero ERROR-STATUS branch is not present"

        # The first mapped key column is sufficient to prove parent existence;
        # key columns remain in WHERE and are already populated by source MOVEs.
        existence_column = key_fields[0][1]
        dclgen_group = self.hosts.group_for_table(table)
        if not dclgen_group:
            return None, "DCLGEN group is missing"
        return HandwrittenCalcReadPlan(
            record=record,
            table=table,
            key_columns=tuple(column for _field, column in key_fields),
            existence_column=existence_column,
            dclgen_group=dclgen_group,
        ), ""

    @staticmethod
    def _logical_lines(source_text: str) -> list[str]:
        output: list[str] = []
        for raw in str(source_text or "").splitlines():
            line = raw.rstrip("\r\n")
            if len(line) > 6 and line[:6].strip().isdigit():
                indicator = line[6]
                if indicator in "*/":
                    output.append("")
                    continue
                line = line[7:72]
            elif line.lstrip().startswith(("*", "/")):
                output.append("")
                continue
            output.append(line.upper())
        return output


__all__ = ["HandwrittenCalcReadPlan", "HandwrittenObtainCalcPlanner"]
