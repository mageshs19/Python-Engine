# LOCATION: converter/resolvers/lrf_cursor_where_resolver.py
# ACTION: REPLACE ENTIRE FILE
"""Resolves WHERE clauses for LRF-expanded cursors.

LRF path expansion leaves a comment marker in the generated program:

    *DB2: Expanded LRF FIRST <logical-record> WHERE <keyword> -> <record>

This resolver reads that marker and generates the WHERE conditions that
belong on the resulting cursor, from parent-child key relationships.

CORRECTION - THE MARKER FORMAT HAD FOUR OWNERS

This module carried a PRIVATE copy of the marker regex. So did
converter/generators/lrf_host_variable_populator.py. The format is
owned and documented in patterns/cursor_spec/lrf_comment_patterns.py,
which publishes three forms: single-line, wrapped, and the continuation
record that opens a wrapped body.

The private copies drifted. The populator's copy anchored on the comment
indicator (\\*), which lives in column 7 - OUTSIDE the logical body - so
it could never match a stripped body and the pass was inert on every
program. This module's copy declared an optional WITHIN group and then
unpacked FIVE values from a FOUR-group match.

There is now ONE owner. The shared name is re-exported so existing
importers keep working; it is never re-assigned.

GROUP NAMES - READ BEFORE USING

The shared single-line pattern captures, in order:

    mode       FIRST | NEXT
    subschema  the LOGICAL RECORD name
    sweep      the PATH KEYWORD
    record     the TARGET RECORD

It does NOT capture a set or an area. A path keyword may resolve WITHIN
a SET (a join, which has a parent record) or WITHIN an AREA (an
unqualified sweep, which has no parent at all). Only the parsed
subschema knows which. Never infer it from the marker.
"""

from __future__ import annotations

import re

from converter.services.name_normalizer import NameNormalizer
from patterns.cursor_spec.lrf_comment_patterns import (
    LRF_ACCESS_MARKER_PROBE,
    LRF_CONTINUATION_ARROW_PATTERN,
    LRF_CONTINUATION_RECORD_PATTERN,
    LRF_EXPANSION_PATTERN as _SHARED_LRF_EXPANSION_PATTERN,
    LRF_EXPANSION_WRAPPED_PATTERN as _SHARED_LRF_WRAPPED_PATTERN,
    LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN as _SHARED_LRF_WRAPPED_NO_ARROW_PATTERN,
)

class LrfCursorWhereResolver:
    """Generates WHERE conditions for LRF-expanded cursors."""

    # One owner for the marker format. This module READS markers; it does
    # not define what a marker looks like.
    LRF_EXPANSION_PATTERN = _SHARED_LRF_EXPANSION_PATTERN
    LRF_EXPANSION_WRAPPED_PATTERN = _SHARED_LRF_WRAPPED_PATTERN
    LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN = _SHARED_LRF_WRAPPED_NO_ARROW_PATTERN
    LRF_CONTINUATION_RECORD_PATTERN = LRF_CONTINUATION_RECORD_PATTERN
    LRF_CONTINUATION_ARROW_PATTERN = LRF_CONTINUATION_ARROW_PATTERN

    def __init__(
        self,
        *,
        relationship_resolver=None,
        cursor_column_resolver=None,
        host_variable_resolver=None,
        mapping_repository=None,
    ) -> None:
        self.relationship_resolver = relationship_resolver
        self.cursor_column_resolver = cursor_column_resolver
        self.host_variable_resolver = host_variable_resolver
        self.mapping_repository = mapping_repository
        self.messages: list[str] = []

    # ------------------------------------------------------------------
    # Marker extraction
    # ------------------------------------------------------------------

    def extract_lrf_cursors_from_cobol(
        self,
        cobol_text: str,
    ) -> dict[str, dict[str, str]]:
        """Extract LRF expansion markers from COBOL source.

        Returns:
            {"<record>": {"mode": ..., "lr_name": ..., "path_keyword": ...,
                          "is_lrf_expanded": True}, ...}

        The set name is deliberately NOT returned. It is not in the
        marker; it belongs to the parsed subschema.
        """
        self.messages = []
        lrf_cursors: dict[str, dict[str, str]] = {}
        extra_filters_by_keyword: dict[str, str] = {}
        marker_positions_by_keyword: dict[str, list[int]] = {}

        lines = str(cobol_text or "").splitlines()

        for index, line in enumerate(lines):
            body = self._logical_body(line)
            if "extra filter:" in body.lower():
                combined = body
                for next_index in range(index + 1, min(index + 4, len(lines))):
                    _seq, indicator, next_body = self._parts(lines[next_index])
                    if indicator not in ("*", "/"):
                        break
                    combined += " " + next_body
                    if "add to the generated cursor where" in combined.lower():
                        break
                filter_match = re.search(
                    r"LRF\s+(?P<keyword>[A-Z0-9-]+)\s+extra filter:\s*(?P<conditions>.*?)\s+-\s+add to the generated cursor WHERE\.?\s*$",
                    combined,
                    re.I,
                )
                if filter_match:
                    extra_filters_by_keyword[filter_match.group("keyword").upper()] = (
                        re.sub(r"\s+", " ", filter_match.group("conditions")).strip()
                    )
            body = self._logical_body(line)
            if not body.strip():
                continue

            match = self.LRF_EXPANSION_PATTERN.search(body)
            record_name = ""

            if match is not None:
                record_name = match.group("record")
            else:
                match = self.LRF_EXPANSION_WRAPPED_PATTERN.search(body)
                if match is not None:
                    record_name = self._continuation_record(lines, index)
                else:
                    match = self.LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN.search(body)
                    if match is not None:
                        record_name = self._continuation_arrow_record(lines, index)
                    elif LRF_ACCESS_MARKER_PROBE.search(body):
                        self.messages.append(
                            "LRF where resolver: line "
                            f"{index + 1} carries 'Expanded LRF' but does "
                            "not match the shared marker format."
                        )
                        continue
                    else:
                        continue
                if not record_name:
                    continue

            norm_record = NameNormalizer.normalize(record_name)
            if norm_record in lrf_cursors:
                continue

            keyword = str(match.group("sweep")).upper()
            lrf_cursors[norm_record] = {
                "mode": str(match.group("mode")).upper(),
                "lr_name": str(match.group("subschema")).upper(),
                "path_keyword": keyword,
                "record_name": str(record_name).upper(),
                "is_lrf_expanded": True,
            }
            marker_positions_by_keyword.setdefault(keyword, []).append(index)

        # Some legacy source programs document an additional LRF path filter
        # using a plain fixed-format comment rather than the newer structured
        # "LRF <keyword> extra filter:" marker. Honor only explicit equality
        # directives that literally say they must be added to the cursor WHERE.
        # Associate each directive with the closest preceding LRF marker; if
        # there is no preceding marker, accept it only when there is one LRF
        # path in scope. Mapping is still validated later and fails closed.
        directive_filters: dict[str, list[str]] = {}
        for index, line in enumerate(lines):
            _seq, indicator, body = self._parts(line)
            if indicator not in ("*", "/"):
                continue
            if "add to the generated cursor where" not in body.lower():
                continue
            combined = body
            for next_index in range(index + 1, min(index + 3, len(lines))):
                _seq2, indicator2, body2 = self._parts(lines[next_index])
                if indicator2 not in ("*", "/"):
                    break
                combined += " " + body2
                if "add to the generated cursor where" in combined.lower():
                    break
            predicate = re.search(
                r"\bAND\s+(?P<field>[A-Z][A-Z0-9-]*)\s*=\s*(?P<literal>'[^']*'|\"[^\"]*\"|[+-]?\d+)\s*-?\s*add to the generated cursor where",
                combined,
                re.I,
            )
            if not predicate:
                continue
            marker_candidates = [
                (marker_index, keyword)
                for keyword, positions in marker_positions_by_keyword.items()
                for marker_index in positions
                if marker_index < index
            ]
            if marker_candidates:
                _marker_index, target_keyword = max(marker_candidates)
            elif len(marker_positions_by_keyword) == 1:
                target_keyword = next(iter(marker_positions_by_keyword))
            else:
                continue
            directive_filters.setdefault(target_keyword, []).append(
                f"{predicate.group('field')} = {predicate.group('literal')}"
            )

        for keyword, filters in directive_filters.items():
            prior = extra_filters_by_keyword.get(keyword, "")
            combined_filters = (prior.split(" AND ") if prior else []) + filters
            # The structured marker and the legacy directive can describe the
            # same predicate. Keep first-seen order while preventing duplicates.
            unique_filters: list[str] = []
            for filter_text in combined_filters:
                filter_text = filter_text.strip()
                if filter_text and filter_text not in unique_filters:
                    unique_filters.append(filter_text)
            extra_filters_by_keyword[keyword] = " AND ".join(unique_filters)

        for info in lrf_cursors.values():
            keyword = str(info.get("path_keyword", "")).upper()
            if keyword in extra_filters_by_keyword:
                info["extra_filters"] = extra_filters_by_keyword[keyword]

        return lrf_cursors

    # ------------------------------------------------------------------
    # WHERE generation
    # ------------------------------------------------------------------

    def where_conditions_for_lrf_cursor(
        self,
        record_name: str,
        lrf_cursor_info: dict[str, str],
    ) -> list[str]:
        """WHERE predicates for an LRF-expanded cursor.

        Returns an empty list when the path carries no relationship -
        an unqualified sweep has no join predicate and must not be given
        an invented one.
        """
        if not lrf_cursor_info.get("is_lrf_expanded"):
            return []

        if self.relationship_resolver is None:
            return []

        relationship = self.relationship_resolver.resolve_for_child_record(
            record_name
        )
        if not relationship or not getattr(relationship, "conditions", None):
            return []

        where_conditions: list[str] = []
        for condition in relationship.conditions:
            child_col = str(getattr(condition, "child_column", "") or "")
            parent_host_ref = str(
                getattr(condition, "parent_host_reference", "") or ""
            )
            if child_col and parent_host_ref:
                where_conditions.append(f"{child_col} = {parent_host_ref}")

        extra_conditions = self.extra_filter_conditions_for_lrf_cursor(
            record_name, lrf_cursor_info
        )
        if extra_conditions is None:
            return []
        where_conditions.extend(extra_conditions)
        return where_conditions

    def extra_filter_conditions_for_lrf_cursor(
        self, record_name: str, lrf_cursor_info: dict[str, str]
    ) -> list[str] | None:
        """Resolve only source-proven extra predicates from an LRF marker."""
        extra_text = str(lrf_cursor_info.get("extra_filters", "") or "")
        if not extra_text:
            return []
        extra_conditions = self._mapped_extra_filter_conditions(record_name, extra_text)
        if extra_conditions is None:
            self.messages.append(
                "LRF where resolver: extra path filters could not be mapped "
                f"unambiguously for {record_name}; refusing to emit partial filters."
            )
            return None
        return extra_conditions

    def _mapped_extra_filter_conditions(
        self, record_name: str, text: str
    ) -> list[str] | None:
        """Map source LRF equality filters to target DB2 columns safely."""
        if self.mapping_repository is None:
            return None
        rows_for_record = getattr(self.mapping_repository, "rows_for_record", None)
        if not callable(rows_for_record):
            return None
        try:
            rows = rows_for_record(record_name) or []
        except Exception:
            return None

        import re

        parts = re.split(r"\s+AND\s+", text.strip(), flags=re.I)
        result: list[str] = []
        for part in parts:
            match = re.fullmatch(
                r"\s*(?P<field>[A-Z][A-Z0-9-]*)\s*=\s*(?P<literal>'[^']*'|\"[^\"]*\"|[+-]?\d+)\s*",
                part,
                re.I,
            )
            if not match:
                return None
            source_field = re.sub(r"[^A-Z0-9]", "", match.group("field").upper())
            candidates: set[str] = set()
            for row in rows:
                row_sources = [
                    str(getattr(row, "cobol_zone", "") or "").strip(),
                    str(getattr(row, "reference_field_name_copybook", "") or "").strip(),
                ]
                target_column = str(
                    getattr(row, "new_db2_field_name", "")
                    or getattr(row, "cross_application_db2_field_name", "")
                    or ""
                ).strip()
                if not target_column:
                    continue
                def normalized_source_name(value: str) -> str:
                    # Mapping-sheet COBOL zones commonly include a level
                    # number (for example "03 CT-RK-TEVPR"). It is metadata,
                    # not part of the field name; retaining it made legitimate
                    # LRF filter mappings silently fail to match.
                    value = re.sub(r"^\s*\d{1,2}\s+", "", value.strip())
                    return re.sub(r"[^A-Z0-9]", "", value.upper())

                if any(
                    source_name
                    and (
                        normalized_source_name(source_name) == source_field
                        or normalized_source_name(source_name).startswith(source_field)
                    )
                    for source_name in row_sources
                ):
                    candidates.add(target_column.upper())
            if len(candidates) != 1:
                return None
            result.append(f"{next(iter(candidates))} = {match.group('literal')}")
        return result

    def augment_select_for_lrf_keys(
        self,
        cursor_spec: dict[str, object],
        lrf_cursor_info: dict[str, str],
    ) -> None:
        """Ensure WHERE-referenced key columns appear in the SELECT.

        A predicate host variable that is never selected is never
        populated, so the cursor silently filters on spaces or zeroes.
        """
        if not lrf_cursor_info.get("is_lrf_expanded"):
            return

        where_conditions = cursor_spec.get("where_conditions", []) or []
        select_columns = list(cursor_spec.get("select_columns", []) or [])
        existing = {NameNormalizer.normalize(c) for c in select_columns}

        for condition in where_conditions:
            text = str(condition)
            if ":" not in text or "." not in text:
                continue

            host_part = text.split(":", 1)[1].strip()
            if "." not in host_part:
                continue

            _dcl_name, host_field = host_part.split(".", 1)
            parent_col = NameNormalizer.normalize(
                host_field.strip().replace("-", "_")
            )
            if parent_col and parent_col not in existing:
                select_columns.append(parent_col)
                existing.add(parent_col)

        cursor_spec["select_columns"] = select_columns

    def resolve_order_by_direction_for_lrf(
        self,
        record_name: str,
        lrf_cursor_info: dict[str, str],
        order_by_columns: list[str],
    ) -> list[str]:
        """Correct ORDER BY direction from the LRF access mode."""
        if not lrf_cursor_info.get("is_lrf_expanded"):
            return order_by_columns
        if not order_by_columns:
            return order_by_columns

        mode = str(lrf_cursor_info.get("mode", "FIRST")).upper()
        corrected: list[str] = []

        for expr in order_by_columns:
            expr_str = str(expr).strip()
            upper = expr_str.upper()
            has_asc = " ASC" in f" {upper}"
            has_desc = " DESC" in f" {upper}"

            if mode == "NEXT" and not has_asc and not has_desc:
                corrected.append(f"{expr_str} DESC")
            elif mode == "FIRST" and has_desc and not has_asc:
                corrected.append(expr_str.replace("DESC", "ASC").strip())
            else:
                corrected.append(expr_str)

        return corrected

    # ------------------------------------------------------------------
    # Private: fixed-format access
    # ------------------------------------------------------------------

    @staticmethod
    def _parts(line: str) -> tuple[str, str, str]:
        text = str(line or "").rstrip("\\r\\n")
        if len(text) >= 7 and text[:6].strip().isdigit():
            return text[:6], text[6:7], text[7:72].strip()
        return "", " ", text.strip()

    @staticmethod
    def _logical_body(line: str) -> str:
        """Columns 8-72 of a fixed-format record, indicator removed."""
        text = str(line or "").rstrip("\r\n")
        if len(text) >= 72 and text[:6].strip().isdigit():
            return text[7:72]
        return text

    def _continuation_arrow_record(self, lines: list[str], index: int) -> str:
        """Read the target record from a wrapped marker whose arrow is on line 2."""
        for offset in range(index + 1, min(index + 3, len(lines))):
            body = self._logical_body(lines[offset]).strip()
            if not body:
                continue
            match = self.LRF_CONTINUATION_ARROW_PATTERN.match(body)
            if match:
                return match.group("record")
            break
        return ""

    def _continuation_record(self, lines: list[str], index: int) -> str:
        """Record name opening the body after a wrapped marker."""
        for offset in range(index + 1, min(index + 3, len(lines))):
            body = self._logical_body(lines[offset]).strip()
            if not body:
                continue
            match = self.LRF_CONTINUATION_RECORD_PATTERN.match(body)
            if match:
                return match.group("record")
            break
        return ""


__all__ = ["LrfCursorWhereResolver"]
