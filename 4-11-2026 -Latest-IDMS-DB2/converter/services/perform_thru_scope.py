"""Reusable paragraph-range inspection for fixed-format COBOL.

Named PERFORM THRU targets are resolved against actual paragraph definitions,
never guessed from naming conventions or program identifiers.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from converter.services.fixed_format_line_service import FixedFormatLineService

_HEADER = re.compile(r"^([A-Z0-9][A-Z0-9-]*)\.$", re.I)
_SPAN = re.compile(r"\bPERFORM\s+([A-Z0-9][A-Z0-9-]*)\s+(?:THRU|THROUGH)\s+([A-Z0-9][A-Z0-9-]*)\b", re.I)
_QUOTED = re.compile(r"(?:'(?:[^']|'')*'|\"(?:[^\"]|\"\")*\")")
_NOT_PARAGRAPHS = frozenset({"EXIT", "CONTINUE", "GOBACK", "STOP", "END-EXEC", "END-IF", "END-PERFORM", "END-EVALUATE", "END-READ", "END-WRITE"})

@dataclass(frozen=True)
class PerformSpan:
    start: str
    end: str
    start_index: int
    end_index: int


def paragraph_indices(lines: list[str]) -> dict[str, int]:
    fixed = FixedFormatLineService()
    in_procedure = False
    result = {}
    for index, line in enumerate(lines):
        if fixed.is_comment_or_control_line(line):
            continue
        logical = fixed.logical(line).strip().upper()
        if logical.startswith("PROCEDURE DIVISION"):
            in_procedure = True
            continue
        if not in_procedure:
            continue
        match = _HEADER.fullmatch(logical)
        if match and match.group(1) not in _NOT_PARAGRAPHS:
            result.setdefault(match.group(1), index)
    return result


def perform_spans(lines: list[str]) -> list[PerformSpan]:
    fixed = FixedFormatLineService()
    labels = paragraph_indices(lines)
    # Periods terminate statements, but may separate other PERFORM calls;
    # scanning executable lines preserves continued PERFORM THRU syntax.
    code = " ".join(
        _QUOTED.sub(" ", fixed.logical(line)).strip().upper()
        for line in lines
        if not fixed.is_comment_or_control_line(line)
    )
    result = []
    for match in _SPAN.finditer(code):
        start, end = match.groups()
        if start in labels and end in labels and labels[start] <= labels[end]:
            result.append(PerformSpan(start, end, labels[start], labels[end]))
    return result
