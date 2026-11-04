from __future__ import annotations

from typing import List
import re

from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.timestamp.timestamp_anchors import (
    NOT_FOUND,
    TimestampAnchors,
)
from rules.timestamp_audit_rules import (
    EMIT_TIMESTAMP_DEBUG_LINE,
    TIMESTAMP_MESSAGES,
    TIMESTAMP_MOVE_ALIGN_COLUMN,
    TIMESTAMP_MOVE_FIELDS,
    TIMESTAMP_PARAGRAPH_DEBUG_TEMPLATE,
    TIMESTAMP_PARAGRAPH_DISPLAY,
    TIMESTAMP_PARAGRAPH_FIELD_MOVE_TEMPLATE,
    TIMESTAMP_PARAGRAPH_HEADER_TEMPLATE,
    TIMESTAMP_PARAGRAPH_NAME,
    TIMESTAMP_PARAGRAPH_SOURCE_MOVE,
    TIMESTAMP_PARAGRAPH_TERMINATOR,
    TIMESTAMP_PERFORM_TEMPLATE,
)

SOURCE_MOVE_PREFIX = "     MOVE {field} OF TS-SYSTEM"


class TimestampParagraphBuilder:

    def __init__(
        self,
        geometry: LineGeometry | None = None,
        anchors: TimestampAnchors | None = None,
        paragraph_name: str = TIMESTAMP_PARAGRAPH_NAME,
    ) -> None:
        self.geometry = geometry or LineGeometry()
        self.anchors = anchors or TimestampAnchors(self.geometry)
        self.paragraph_name = paragraph_name
        self.messages: List[str] = []

    def block(self) -> List[str]:
        lines = [
            TIMESTAMP_PARAGRAPH_HEADER_TEMPLATE.format(
                paragraph_name=self.paragraph_name
            )
        ]
        if EMIT_TIMESTAMP_DEBUG_LINE:
            lines.append(
                TIMESTAMP_PARAGRAPH_DEBUG_TEMPLATE.format(
                    paragraph_name=self.paragraph_name
                )
            )
        lines.append(TIMESTAMP_PARAGRAPH_SOURCE_MOVE)
        for field in TIMESTAMP_MOVE_FIELDS:
            lines.append(self._move_line(field))
        lines.append(TIMESTAMP_PARAGRAPH_DISPLAY)
        lines.append(TIMESTAMP_PARAGRAPH_TERMINATOR)
        return lines

    def ensure_paragraph(self, lines: List[str]) -> List[str]:
        self.messages = []

        if self.anchors.has_paragraph(lines, self.paragraph_name):
            self._log("paragraph_present", paragraph=self.paragraph_name)
            return list(lines)

        block = [""] + self.block()
        index = self.anchors.paragraph_insert_index(lines)

        self._log("paragraph_added", paragraph=self.paragraph_name)

        if index >= len(lines):
            return list(lines) + block

        return lines[:index] + block + [""] + lines[index:]

    def ensure_perform(self, lines: List[str]) -> List[str]:
        self.messages = []

        if self.anchors.perform_count(lines, self.paragraph_name) > 0:
            self._log("perform_present", paragraph=self.paragraph_name)
            return list(lines)

        division = self.anchors.procedure_division_index(lines)
        if division == NOT_FOUND:
            return list(lines)

        index = self._initialization_entry(lines, division)
        if index == NOT_FOUND:
            index = self.anchors.first_statement_index(lines, division)
        if index == NOT_FOUND:
            index = division + 1

        statement = TIMESTAMP_PERFORM_TEMPLATE.format(
            paragraph_name=self.paragraph_name
        )
        self._log("perform_added", paragraph=self.paragraph_name)
        return lines[:index] + [statement] + lines[index:]

    def _initialization_entry(self, lines: List[str], division: int) -> int:
        """Put timestamp in a proven, mainline-performed initialization paragraph.

        A source program may have an explicit MAIN paragraph. Inserting a
        statement between PROCEDURE DIVISION and MAIN changes the implicit
        entry path, rather than retaining initialization ownership. Require a
        unique INIT/BEGIN paragraph, a MAIN call before its processing calls,
        and an unambiguous paragraph boundary. Otherwise preserve the old
        insertion point rather than guessing a new control-flow edge.
        """
        names: list[tuple[str, int]] = []
        for index in range(division + 1, len(lines)):
            if self.geometry.is_comment_or_blank(lines[index]):
                continue
            raw = str(lines[index])
            body = self.geometry.body(raw).strip().upper()
            area = raw[7:72] if len(raw) >= 7 and raw[:6].isdigit() else raw
            if len(area) - len(area.lstrip()) > 3:
                continue
            match = re.fullmatch(r"([A-Z0-9][A-Z0-9-]*)\.", body)
            if match and not match.group(1).startswith("END-"):
                names.append((match.group(1), index))
        if len(names) < 2:
            return NOT_FOUND
        main_name, main_index = names[0]
        init_candidates = [(name, index) for name, index in names[1:]
                           if re.search(r"(?:^|[-_])(?:INIT|BEGIN)(?:[-_]|$)", name)
                           and not name.endswith("-EXIT")]
        if len(init_candidates) != 1:
            return NOT_FOUND
        init_name, init_index = init_candidates[0]
        main_end = names[1][1]
        main_code = " ".join(
            self.geometry.body(line).upper()
            for line in lines[main_index + 1:main_end]
            if not self.geometry.is_comment_or_blank(line)
        )
        if not re.search(r"\bPERFORM\s+" + re.escape(init_name) + r"\b", main_code):
            return NOT_FOUND
        if init_index <= main_end - 1:
            # Main procedure may not be adjacent to init; still require its
            # single-call site rather than guessing a nested entry.
            return NOT_FOUND
        return init_index + 1

    def _move_line(self, field: str) -> str:
        source = SOURCE_MOVE_PREFIX.format(field=field)
        pad = " " * max(1, TIMESTAMP_MOVE_ALIGN_COLUMN - len(source))
        return TIMESTAMP_PARAGRAPH_FIELD_MOVE_TEMPLATE.format(
            field=field,
            pad=pad,
        )

    def _log(self, key: str, **values) -> None:
        template = TIMESTAMP_MESSAGES.get(str(key or ""), "")
        if not template:
            return
        try:
            self.messages.append(template.format(**values))
        except (IndexError, KeyError):
            self.messages.append(f"{template} [{key}: {values}]")


__all__ = ["TimestampParagraphBuilder"]