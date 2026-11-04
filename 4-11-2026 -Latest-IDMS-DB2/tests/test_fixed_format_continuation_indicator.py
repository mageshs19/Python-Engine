from converter.services.fixed_format_line_service import FixedFormatLineService


def test_emit_uses_blank_indicator_for_word_boundary_wraps():
    service = FixedFormatLineService()
    lines = service.emit("000100", " ", "       MOVE WS-IN-NR-TIT-BC(13:1) TO NR-CDSTK-479BEFF OF DCLDZBEFFTV", "00010000")
    assert len(lines) == 2
    assert lines[0][6] == " "
    assert lines[1][6] == " "
    assert "OF DCLDZBEFFTV" in lines[1]


def test_replace_body_wrapped_uses_blank_indicator_for_word_boundary_wraps():
    service = FixedFormatLineService()
    original = service.build("000100", " ", "       MOVE X TO Y", "00010000")
    lines = service.replace_body_wrapped(
        original,
        "       MOVE WS-IN-NR-TIT-BC(13:1) TO NR-CDSTK-479BEFF OF DCLDZBEFFTV",
    )
    assert len(lines) == 2
    assert lines[0][6] == " "
    assert lines[1][6] == " "


def test_wrapped_comments_remain_comments_not_executable_continuations():
    service = FixedFormatLineService()
    lines = service.emit("000100", "*", "*DB2: " + "long comment words " * 8, "00010000")
    assert len(lines) > 1
    assert all(line[6] == "*" for line in lines)
