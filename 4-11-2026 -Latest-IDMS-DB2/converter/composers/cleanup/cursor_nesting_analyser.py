"""Structural parent/child cursor classification for generated COBOL.

Cursor paragraph numbers are not a reliable depth signal: one conversion
may use 710/810 while another uses 2100/3100. This analyser determines
whether a cursor is nested by following the actual PERFORM relationships:

1. find the paragraph that performs the candidate cursor's OPEN/FETCH/CLOSE;
2. prove that another cursor's WHEN ZERO branch performs that owner paragraph.

No program, record, table, cursor, or paragraph names are hardcoded.
"""

from __future__ import annotations

from converter.composers.cleanup.cobol_cleanup_line_utils import (
    CobolCleanupLineUtils,
)
from patterns.cobol_cleanup_patterns import (
    PARAGRAPH_HEADER_PATTERN,
    PERFORM_CURSOR_PARAGRAPH_PATTERN,
    PERFORM_PARAGRAPH_PATTERN,
    WHEN_ZERO_PATTERN,
)
from rules.cobol_cleanup_rules import NON_PARAGRAPH_SINGLE_WORDS


class CursorNestingAnalyser:
    def __init__(self, line_utils: CobolCleanupLineUtils | None = None) -> None:
        self.lines = line_utils or CobolCleanupLineUtils()

    def is_nested_fetch(self, lines: list[str], fetch_paragraph: str) -> bool:
        """Return true only when the cursor is structurally nested in a parent row."""
        candidate = str(fetch_paragraph or "").strip().upper()
        marker = "-FETCH-"
        if marker not in candidate:
            return False
        cursor = candidate.split(marker, 1)[1].strip()
        if not cursor:
            return False

        spans = self._paragraph_spans(lines)
        if not spans:
            return False

        # A nested cursor's lifecycle lives in an orchestration/business
        # paragraph, rather than in the mainline.
        owners: set[str] = set()
        cursor_suffix = f"-{cursor}"
        for owner, (start, end) in spans.items():
            for index in range(start + 1, min(end + 1, len(lines))):
                logical = self.lines.logical(lines[index]).upper().rstrip(".")
                match = PERFORM_CURSOR_PARAGRAPH_PATTERN.match(logical)
                if match and logical.endswith(cursor_suffix):
                    owners.add(owner)
                    break

        if not owners:
            return False

        # Prove that some other FETCH paragraph invokes the lifecycle owner
        # under WHEN ZERO. Merely having a cursor in a paragraph is not
        # enough: a standalone cursor paragraph can also call another
        # cursor for unrelated work.
        for fetch_name, (start, end) in spans.items():
            if "-FETCH-" not in fetch_name:
                continue
            if fetch_name == candidate:
                continue

            seen_when_zero = False
            for index in range(start + 1, min(end + 1, len(lines))):
                logical = self.lines.logical(lines[index])
                if not logical or logical.startswith(("*", "/")):
                    continue
                if WHEN_ZERO_PATTERN.match(logical):
                    seen_when_zero = True
                    continue
                if not seen_when_zero:
                    continue
                if logical.upper().startswith(("WHEN ", "WHEN-OTHER", "END-EVALUATE")):
                    break
                perform = PERFORM_PARAGRAPH_PATTERN.match(logical)
                if perform and perform.group("paragraph").upper() in owners:
                    return True

        return False

    def paragraph_spans(self, lines: list[str]) -> dict[str, tuple[int, int]]:
        """Expose paragraph spans for cooperating cleanup passes."""
        return self._paragraph_spans(lines)

    def _paragraph_spans(self, lines: list[str]) -> dict[str, tuple[int, int]]:
        spans: dict[str, tuple[int, int]] = {}
        current = ""
        start = -1

        for index, line in enumerate(lines):
            logical = self.lines.logical(line)
            if not logical or logical.startswith(("*", "/")):
                continue
            if not logical.endswith(".") or not PARAGRAPH_HEADER_PATTERN.match(logical):
                continue
            name = logical.rstrip(".").upper()
            if name in NON_PARAGRAPH_SINGLE_WORDS:
                continue
            if current:
                spans[current] = (start, index - 1)
            current = name
            start = index

        if current and start >= 0:
            spans[current] = (start, len(lines) - 1)
        return spans


__all__ = ["CursorNestingAnalyser"]
