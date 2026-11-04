"""Plan safe DB2 host-variable bindings for LRF keyed parent traversals.

This planner is deliberately metadata-driven. It does not know program IDs,
record names, table names, or column names. It only creates a key split when
Sheet Mapping proves that a CALC group consists of mapped direct key fields
whose widths exactly match a simple COBOL source field.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from converter.generators.initialization.line_geometry import LineGeometry
from converter.services.name_normalizer import NameNormalizer


@dataclass
class LrfKeyBindingPlan:
    parent_record: str
    parent_input_moves: list[str] = field(default_factory=list)
    child_record: str = ""
    child_dcl_group: str = ""
    child_key_moves: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)
    safe: bool = True


class LrfKeyBindingPlanner:
    """Build source-to-key and parent-to-child key bindings from metadata."""

    _FIELD_LEVEL = re.compile(r"^\s*(?P<level>\d{1,2})\s+(?P<name>[A-Z0-9-]+)", re.I)
    _PIC_WIDTH = re.compile(r"\bPIC(?:TURE)?\s+(?:X|9)\s*\(\s*(\d+)\s*\)", re.I)
    _MOVE_TO_GROUP = re.compile(
        r"\bMOVE\s+(?P<src>[A-Z][A-Z0-9-]*)"
        r"(?:\s+OF\s+[A-Z][A-Z0-9-]*)?\s+TO\s+"
        r"(?P<group>[A-Z][A-Z0-9-]*)\s+OF\s+(?P<record>[A-Z][A-Z0-9-]*)\b",
        re.I,
    )
    _DB2_WIDTH = re.compile(r"\b(?:CHAR|CHARACTER|DECIMAL|NUMERIC|INTEGER)\s*\(\s*(\d+)", re.I)

    def __init__(self, mapping_repository, dclgen_repository, table_name_resolver, host_variable_resolver, copybook_repository=None):
        self.mapping = mapping_repository
        self.dclgen = dclgen_repository
        self.table_resolver = table_name_resolver
        self.hosts = host_variable_resolver
        self.copybooks = copybook_repository
        self.geometry = LineGeometry()

    def plan_parent_input(self, source_text: str, parent_record: str) -> tuple[list[str], list[str], bool]:
        """Return moves that split a mapped composite CALC group into DCLGEN keys.

        Third return value says whether the record has a mapped composite CALC
        group and therefore requires a split. If metadata/source is ambiguous,
        the caller must refuse executable SQL instead of guessing.
        """
        record = NameNormalizer.normalize(parent_record)
        rows = self.mapping.rows_for_record(record)
        group_rows: list[tuple[int, str, object]] = []
        for row in rows:
            field = self._field_identity(getattr(row, "cobol_zone", ""))
            if not field:
                continue
            level, name = field
            key_kind = NameNormalizer.normalize(getattr(row, "idms_key", ""))
            pic = NameNormalizer.normalize(getattr(row, "idms_pic_clause", ""))
            if "CALC" in key_kind and "GROUP" in pic:
                group_rows.append((level, name, row))

        if not group_rows:
            return [], [], False

        logical = self._logical_source(source_text)
        moves = list(self._MOVE_TO_GROUP.finditer(logical))
        access_match = re.search(rf"\bOBTAIN\s+CALC\s+{re.escape(record)}\b", logical, re.I)
        access_position = access_match.start() if access_match else len(logical)
        # Only MOVEs that establish the CALC key BEFORE the keyed access are
        # candidates. Later output-field MOVEs can mention the same group but
        # cannot be inputs to the SELECT.
        moves = [match for match in moves if match.start() < access_position]
        # A composite CALC group is only handled when exactly one source MOVE
        # targets it. Ambiguous repeated/redefined group moves are refused.
        candidates = []
        for level, group_name, group_row in group_rows:
            found = [m for m in moves if NameNormalizer.normalize(m.group("record")) == record
                     and NameNormalizer.normalize(m.group("group")) == group_name]
            if not found:
                continue
            candidate = found[-1]
            candidate_source = str(candidate.group("src") or "").strip().upper()
            candidate_width = self._declared_width(logical, candidate_source)
            candidate_children = self._direct_key_children(rows, level)
            candidate_widths = [self._mapped_width(row) for row in candidate_children]
            # Ignore initialization moves such as MOVE SPACES TO KY-EFFECT:
            # they do not supply a fixed-width source key. Only a declared
            # source whose width exactly matches mapped key components proves
            # a usable composite key split.
            if candidate_width and candidate_children and all(w > 0 for w in candidate_widths) and sum(candidate_widths) == candidate_width:
                candidates.append((level, group_name, group_row, candidate, candidate_children, candidate_widths))

        if not candidates:
            return [], [f"LRF key binding: no provable source MOVE into a mapped CALC group for {record}; keyed SELECT refused."], True
        if len(candidates) != 1:
            return [], [f"LRF key binding: multiple provable CALC group sources for {record}; keyed SELECT refused."], True

        level, group_name, _group_row, match, direct_children, widths = candidates[0]
        # Preserve COBOL hyphens for emitted source references; NameNormalizer
        # uses DB2-style underscores and is only for identity comparisons.
        source = str(match.group("src") or "").strip().upper()
        source_width = self._declared_width(logical, source)
        if not source_width or not direct_children or any(width <= 0 for width in widths) or sum(widths) != source_width:
            return [], [
                f"LRF key binding: source/group layout for {record}.{group_name} is not provable "
                f"(source width={source_width}, component widths={widths}); keyed SELECT refused."
            ], True

        table = self.table_resolver.table_for_record(record)
        if not table:
            return [], [f"LRF key binding: no resolved DB2 table for {record}; keyed SELECT refused."], True
        dcl_group = self.hosts.group_for_table(table)
        output: list[str] = []
        offset = 1
        for row, width in zip(direct_children, widths):
            column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "") or getattr(row, "cross_application_db2_field_name", "")
            )
            host = self.hosts.host_for_column(table, column)
            if not column or not host:
                return [], [f"LRF key binding: DCLGEN host for {record}.{column or '?'} is missing; keyed SELECT refused."], True
            ref = f"{source}({offset}:{width})"
            target = f"{host} OF {dcl_group}"
            # Keep the key split as a data movement, not a new validation
            # branch. The legacy program's contract is to split the fixed-width
            # CALC key and let the normal SQL error path handle DB2 outcomes;
            # injecting an IF/ELSE/SQLERROR here changes business behavior and
            # can introduce sentence-terminating periods inside generated
            # control flow. Sheet Mapping still proves each component's width
            # and target host before this move is emitted.
            output.append(f"MOVE {ref} TO {target}.")
            offset += width
        return output, [], True

    def _direct_key_children(self, rows, parent_level: int) -> list[object]:
        output: list[object] = []
        for row in rows:
            field = self._field_identity(getattr(row, "cobol_zone", ""))
            if not field or field[0] != parent_level + 1:
                continue
            idms_key = NameNormalizer.normalize(getattr(row, "idms_key", ""))
            db2_key = NameNormalizer.normalize(getattr(row, "db2_key", ""))
            relation = NameNormalizer.normalize(getattr(row, "relation", ""))
            text = f"{idms_key} {db2_key} {relation}"
            if "FOREIGN" in text or not ("PRIMARY_KEY" in text or "PRIMARY" in text and "KEY" in text):
                continue
            column = NameNormalizer.normalize(getattr(row, "new_db2_field_name", "") or getattr(row, "cross_application_db2_field_name", ""))
            if column:
                output.append(row)
        return output

    def _mapped_width(self, row) -> int:
        direct = str(getattr(row, "length_of_field_bytes", "") or "").strip()
        if direct.isdigit():
            return int(direct)
        dtype = str(getattr(row, "new_db2_data_type", "") or getattr(row, "cross_application_db2_data_type", "") or "")
        match = self._DB2_WIDTH.search(dtype)
        return int(match.group(1)) if match else 0

    def _declared_width(self, logical: str, source: str) -> int:
        # First inspect inline declarations, restricting the match to the
        # declaration line so a neighboring PIC cannot leak in. Input fields
        # are often declared in COPY VMDZ205I, so they are absent from the
        # expanded program text; use the parsed copybook repository as the
        # second authoritative source rather than refusing a provable key split.
        for line in logical.splitlines():
            if re.search(rf"\b{re.escape(source)}\b", line, re.I) and re.search(r"\bPIC(?:TURE)?\b", line, re.I):
                match = self._PIC_WIDTH.search(line)
                if match:
                    return int(match.group(1))
        if self.copybooks is not None:
            try:
                picture = str(self.copybooks.effective_picture_for(source) or "").upper()
            except Exception:  # noqa: BLE001 - fail closed when metadata is unavailable
                picture = ""
            match = self._PIC_WIDTH.search("PIC " + picture) if picture else None
            if match:
                return int(match.group(1))
        return 0

    def _field_identity(self, raw: str) -> tuple[int, str] | None:
        text = " ".join(str(raw or "").split())
        match = self._FIELD_LEVEL.match(text)
        if not match:
            return None
        return int(match.group("level")), NameNormalizer.normalize(match.group("name"))

    def _logical_source(self, source_text: str) -> str:
        lines = []
        for raw in str(source_text or "").splitlines():
            body = self.geometry.body(raw)
            if not body or self.geometry.is_comment(raw):
                continue
            lines.append(body.upper())
        # The move syntax is matched across physical line breaks; declarations
        # remain line-separated so PIC widths are tied to their own field.
        return "\n".join(lines)
