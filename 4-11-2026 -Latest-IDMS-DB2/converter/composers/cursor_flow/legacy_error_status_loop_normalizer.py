"""Normalize legacy IDMS status-driven loops only when cursor ownership is proven.

A loop is rewritten only when a generated FETCH paragraph's WHEN ZERO branch
calls a business paragraph, and that same business paragraph advances that
FETCH at its tail. This identifies the original mainline-driven pattern and
avoids guessing which cursor an ERROR-STATUS loop belongs to.
"""
from __future__ import annotations

import re

from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter

_NAME = r"[A-Z0-9][A-Z0-9-]*"
_FETCH_HEADER = re.compile(rf"^\d{{3,6}}-FETCH-(?P<cursor>{_NAME})\s*\.$", re.I)
_PARAGRAPH_HEADER = re.compile(rf"^(?P<name>{_NAME})\s*\.$", re.I)
_PERFORM = re.compile(rf"^PERFORM\s+(?P<name>{_NAME})(?:\s+(?:THRU|THROUGH)\s+{_NAME})?\s*\.?$", re.I)
_LEGACY_LOOP = re.compile(
    rf"^(?P<head>PERFORM\s+(?P<business>{_NAME})(?:\s+(?:THRU|THROUGH)\s+{_NAME})?\s+UNTIL\s+)"
    r"ERROR-STATUS\s+NOT\s*=\s*(['\"])0000\3\s*(?P<period>\.)?$", re.I
)


class LegacyErrorStatusLoopNormalizer:
    def __init__(self, formatter: CursorFlowLineFormatter | None = None) -> None:
        self.formatter = formatter or CursorFlowLineFormatter()
        self.messages: list[str] = []

    def compose(self, text: str) -> str:
        self.messages = []
        lines = self.formatter.normalize_line_endings(str(text or "")).splitlines()
        logical = [self.formatter.logical(line) for line in lines]
        spans: dict[str, tuple[int, int]] = {}
        for i, body in enumerate(logical):
            match = _PARAGRAPH_HEADER.fullmatch(body)
            if match and self._is_paragraph_header(lines[i]):
                spans[match.group("name").upper()] = (i, len(lines))
        ordered = sorted((start, name) for name, (start, _end) in spans.items())
        for pos, (start, name) in enumerate(ordered):
            spans[name] = (start, ordered[pos + 1][0] - 1 if pos + 1 < len(ordered) else len(lines) - 1)

        # A business paragraph that advances a generated cursor at its tail
        # owns the matching legacy ERROR-STATUS loop. This relationship is
        # available before WHEN ZERO business binding is applied.
        business_fetches: dict[str, set[str]] = {}
        for business, (start, end) in spans.items():
            executable = [
                (j, logical[j]) for j in range(start + 1, end + 1)
                if logical[j] and not self._is_comment(lines[j])
            ]
            if not executable:
                continue
            _last_index, last_body = executable[-1]
            fetch_match = re.fullmatch(
                rf"PERFORM\s+\d{{3,6}}-FETCH-(?P<cursor>{_NAME})\s*\.?",
                last_body, re.I,
            )
            if fetch_match:
                business_fetches.setdefault(business, set()).add(
                    fetch_match.group("cursor").upper()
                )

        replacements = 0
        for i, body in enumerate(logical):
            match = _LEGACY_LOOP.fullmatch(body)
            if not match:
                continue
            business = match.group("business").upper()
            proven = list(business_fetches.get(business, set()))
            # Ambiguous/missing cursor ownership is intentionally left untouched.
            if len(set(proven)) != 1:
                continue
            cursor = proven[0]
            period = match.group("period") or ""
            # Clear the paired diagnostic comments from the removed IDMS
            # ERROR-STATUS predicate while preserving source record numbers.
            for previous in range(max(0, i - 2), i):
                if self._is_obsolete_warning(logical[previous]):
                    lines[previous] = self._blank_comment(lines[previous])
                    logical[previous] = self.formatter.logical(lines[previous])
            replacement = f"{match.group('head')}{cursor}-EOC{period}"
            lines[i] = self.formatter.format_like_line(lines[i], replacement)
            logical[i] = replacement
            replacements += 1
        if replacements:
            self.messages.append(f"normalized {replacements} proven ERROR-STATUS cursor loop(s) to cursor EOC")
        return "\n".join(lines).rstrip() + "\n"

    @staticmethod
    def _is_obsolete_warning(logical: str) -> bool:
        upper = str(logical or "").upper()
        return "ERROR-STATUS IS UNDEFINED AFTER COPYBOOK REMOVAL" in upper or "SHARES A LINE WITH LIVE OPERANDS" in upper

    @staticmethod
    def _blank_comment(line: str) -> str:
        value = str(line or "")
        if len(value) >= 80 and value[:6].isdigit():
            return f"{value[:6]}*{' ' * 65}{value[72:80]}"
        return "*"

    @staticmethod
    def _is_comment(line: str) -> bool:
        value = str(line or "")
        if len(value) >= 7 and value[:6].isdigit():
            return value[6] in {"*", "/", "D", "d"}
        return value.lstrip().startswith(("*", "/*"))

    @staticmethod
    def _is_paragraph_header(line: str) -> bool:
        value = str(line or "")
        if len(value) >= 8 and value[:6].isdigit():
            return bool(value[7:72]) and not value[7:72].startswith(" ")
        return bool(value) and not value.startswith(" ")
