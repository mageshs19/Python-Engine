"""Renumber cursor-operation paragraphs without restructuring COBOL control flow.

The COBOL team's numbering convention is centralized in rules.cursor_rules:
C1 OPEN/FETCH/CLOSE = 2100/2200/2300, C2 = 3100/3200/3300, etc.
Only cursor-operation labels, their identifier references, and matching
SQL-LOCATION values are changed. Business paragraph names, PERFORM order,
PERFORM THRU ranges, and mainline structure are left untouched.
"""
from __future__ import annotations

from converter.composers.lifecycle_standardization_composer import (
    LifecycleStandardizationComposer,
)


class CursorParagraphNumberingComposer(LifecycleStandardizationComposer):
    """Apply only the shared cursor numbering rule; never wrap the mainline."""

    def compose(self, text: str) -> str:
        self.messages = []
        source = str(text or "")
        if not source:
            return source
        lines = source.splitlines()
        try:
            normalized = self._normalize_cursor_paragraph_numbers(lines)
        except (ValueError, IndexError, KeyError) as exc:
            self.messages.append(
                f"Cursor paragraph numbering skipped safely: {exc}; original flow preserved."
            )
            return source
        if normalized == lines:
            return source
        self.messages.append(
            "Cursor paragraph numbering applied using COBOL team convention; "
            "business paragraph names and execution flow preserved."
        )
        result = "\n".join(normalized)
        if source.endswith(("\n", "\r")):
            result += "\n"
        return result
