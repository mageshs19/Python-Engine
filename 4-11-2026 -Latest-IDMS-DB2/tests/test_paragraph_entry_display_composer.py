from __future__ import annotations

import re

from converter.composers.paragraph_entry_display_composer import ParagraphEntryDisplayComposer


def _logical(line: str) -> str:
    if len(line) >= 7 and line[:6].isdigit():
        return line[7:72].strip()
    return line.strip()


def _paragraphs(text: str) -> list[tuple[str, int]]:
    lines = text.splitlines()
    procedure = next(i for i, line in enumerate(lines) if re.match(r"^PROCEDURE\s+DIVISION", _logical(line), re.I))
    result = []
    for i in range(procedure + 1, len(lines)):
        body = _logical(lines[i])
        if (re.fullmatch(r"[A-Z0-9][A-Z0-9-]*\.", body, re.I)
                and (len(lines[i]) < 7 or not lines[i][:6].isdigit() or len(lines[i][7:72]) - len(lines[i][7:72].lstrip()) <= 3)
                and not (len(lines[i]) >= 7 and lines[i][:6].isdigit() and lines[i][6] in "*/Dd")):
            result.append((body[:-1], i))
    return result


def test_every_paragraph_gets_active_exact_name_display_and_is_idempotent():
    def fixed(seq: int, body: str, indicator: str = " ") -> str:
        return f"{seq:06d}{indicator}{body:<65}{seq:08d}"

    source = "\n".join([
        fixed(10, "PROCEDURE DIVISION."),
        fixed(20, "0000-MAIN-PROCEDURE."),
        fixed(30, "    GOBACK."),
        fixed(40, "2110-OPEN-CURSOR."),
        fixed(50, "    DISPLAY 'OLD-OPEN.'.", "D"),
        fixed(60, "    EXIT."),
    ]) + "\n"
    composer = ParagraphEntryDisplayComposer()
    output = composer.compose(source)
    lines = output.splitlines()
    paragraphs = _paragraphs(output)
    assert paragraphs
    for name, index in paragraphs:
        next_idx = index + 1
        while next_idx < len(lines) and not _logical(lines[next_idx]):
            next_idx += 1
        body = _logical(lines[next_idx])
        assert body == f"DISPLAY '{name}.' .".replace("' .", "'."), (name, body)
        assert not (len(lines[next_idx]) >= 7 and lines[next_idx][:6].isdigit() and lines[next_idx][6] in "Dd")
    assert composer.compose(output) == output


def test_inserts_entry_display_when_paragraph_has_no_existing_display():
    source = "000010 PROCEDURE DIVISION.".ljust(80) + "\n"
    source += "000020 DO-WORK.".ljust(80) + "\n"
    source += "000030     MOVE 1 TO WS-X.".ljust(80) + "\n"
    output = ParagraphEntryDisplayComposer().compose(source)
    assert "DISPLAY 'DO-WORK.'." in output


def test_all_vmdz7200_lifecycle_v99_paragraphs_have_exact_active_entry_display():
    from pathlib import Path

    path = Path("mainframe/workspace/Validated Output/LIFECYCLE_V99/VMDZ7200_lifecycle_standardized_v99.cbl")
    if not path.exists():
        return
    output = path.read_text(encoding="utf-8", errors="replace")
    lines = output.splitlines()
    paragraphs = _paragraphs(output)
    assert len(paragraphs) == 17
    for name, index in paragraphs:
        next_idx = index + 1
        while next_idx < len(lines) and not _logical(lines[next_idx]):
            next_idx += 1
        assert next_idx < len(lines), name
        assert _logical(lines[next_idx]).upper() == f"DISPLAY '{name}.' .".replace("' .", "'.").upper(), name
        assert not (len(lines[next_idx]) >= 7 and lines[next_idx][:6].isdigit() and lines[next_idx][6] in "Dd"), name
    assert all(len(line) == 80 for line in lines)


def test_nonmatching_debug_display_is_not_overwritten():
    source = "\n".join([
        "000010 PROCEDURE DIVISION.".ljust(80),
        "000020 DO-WORK.".ljust(80),
        "000030D    DISPLAY 'BUSINESS DIAGNOSTIC'.".ljust(80),
        "000040     GOBACK.".ljust(80),
    ]) + "\n"
    output = ParagraphEntryDisplayComposer().compose(source)
    assert "DISPLAY 'DO-WORK.'." in output
    assert "DISPLAY 'BUSINESS DIAGNOSTIC'." in output
