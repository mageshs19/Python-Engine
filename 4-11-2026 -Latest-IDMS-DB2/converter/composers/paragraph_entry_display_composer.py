"""Ensure every local COBOL procedure paragraph has an active entry DISPLAY.

The rule is concept-driven: it applies to every paragraph found after PROCEDURE
DIVISION, without program-name allowlists. Existing paragraph-entry debug DISPLAYs
are promoted to active DISPLAYs and normalized to the exact paragraph name.
"""
from __future__ import annotations

import re


def _logical(line: str) -> str:
    text = str(line or "").rstrip("\r\n")
    if len(text) >= 7 and text[:6].isdigit():
        return text[7:72].strip()
    return text.strip()


def _is_comment(line: str) -> bool:
    text = str(line or "")
    if len(text) >= 7 and text[:6].isdigit() and text[6] in "*/":
        return True
    return text.lstrip().startswith(("*", "/"))


def _is_paragraph(line: str) -> bool:
    if _is_comment(line):
        return False
    body = _logical(line)
    if not re.fullmatch(r"[A-Z0-9][A-Z0-9-]*\.", body, re.I):
        return False
    # A sentence-ending scope terminator in Area A is still a statement,
    # never a paragraph header (e.g. END-IF. or END-EVALUATE.).
    word = body[:-1].upper()
    if word.startswith("END-") or word in {
        "ELSE", "CONTINUE", "EXIT", "GOBACK", "NEXT", "STOP",
        "INITIALIZE", "CANCEL", "COMMIT", "ROLLBACK", "RETURN",
    }:
        return False
    raw = str(line or "")
    area = raw[7:72] if len(raw) >= 7 and raw[:6].isdigit() else raw
    return len(area) - len(area.lstrip()) <= 3


def _format_body(line: str, body: str, indicator: str | None = None) -> str:
    raw = str(line or "")
    if len(raw) >= 7 and raw[:6].isdigit():
        if len(body) > 65:
            raise ValueError(f"paragraph DISPLAY exceeds fixed-format Area B: {body}")
        mark = raw[6] if indicator is None else indicator
        return raw[:6] + mark + body.ljust(65) + raw[72:]
    return body


class ParagraphEntryDisplayComposer:
    """Insert or normalize a paragraph-name DISPLAY at each local paragraph entry."""

    def __init__(self) -> None:
        self.messages: list[str] = []

    def compose(self, text: str) -> str:
        self.messages = []
        source = str(text or "")
        if not source:
            return source
        lines = source.splitlines()
        procedure_idx = next(
            (i for i, line in enumerate(lines)
             if re.match(r"^PROCEDURE\s+DIVISION\b", _logical(line), re.I)),
            -1,
        )
        if procedure_idx < 0:
            self.messages.append("Paragraph DISPLAY rule skipped: PROCEDURE DIVISION not found.")
            return source

        paragraph_starts = [i for i in range(procedure_idx + 1, len(lines)) if _is_paragraph(lines[i])]
        if not paragraph_starts:
            return source

        output = list(lines)
        inserted = 0
        normalized = 0
        # Work backwards so insertion does not invalidate later paragraph indices.
        for start_idx in reversed(paragraph_starts):
            name = _logical(output[start_idx])
            expected = f"    DISPLAY '{name}'."
            next_idx = start_idx + 1
            while next_idx < len(output) and (not _logical(output[next_idx]) or _is_comment(output[next_idx])):
                next_idx += 1
            if next_idx < len(output):
                body = _logical(output[next_idx])
                is_display = re.match(r"DISPLAY\b", body, re.I) is not None
                is_entry_name = re.fullmatch(
                    r"DISPLAY\s+(['\"])(.*?)\1\s*\.?", body, re.I
                )
                if is_display and is_entry_name and is_entry_name.group(2).upper() == name.upper():
                    # A debug-indicator DISPLAY is not guaranteed to execute; promote it.
                    raw = output[next_idx]
                    if len(raw) >= 7 and raw[:6].isdigit() and raw[6] in "Dd":
                        output[next_idx] = _format_body(raw, expected, " ")
                        normalized += 1
                    continue
                # Never overwrite a non-matching DISPLAY. It may be a real
                # business diagnostic/output statement, even when it uses the
                # COBOL debug indicator. Preserve it and add the mandatory
                # paragraph-entry DISPLAY separately. Only an exact paragraph
                # label above is eligible for promotion from debug to active.
            new_line = expected
            output.insert(start_idx + 1, new_line)
            inserted += 1

        result = "\n".join(output)
        if source.endswith(("\n", "\r")):
            result += "\n"
        self.messages.append(
            f"Paragraph DISPLAY rule applied: {len(paragraph_starts)} paragraphs checked; "
            f"{inserted} DISPLAY statements inserted; {normalized} legacy debug DISPLAYs activated."
        )
        return result
