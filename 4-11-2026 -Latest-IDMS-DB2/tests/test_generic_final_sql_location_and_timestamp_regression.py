"""Structural regression cases observed by comparing converted COBOL with the manual.

The program names and statement identifiers in this fixture are deliberately generic.
"""
from converter.composers.paragraph_entry_display_composer import ParagraphEntryDisplayComposer
from converter.generators.timestamp.timestamp_paragraph_builder import TimestampParagraphBuilder
from converter.services.final_generated_output_service import FinalGeneratedOutputService


def fixed(n: int, body: str) -> str:
    return f"{n:06d} {body:<65}{n:08d}"


def bodies(source: str) -> list[str]:
    return [line[7:72].strip() for line in source.splitlines()]


def test_area_a_scope_terminators_must_not_be_treated_as_paragraphs():
    sample = "\n".join([
        fixed(100, "PROCEDURE DIVISION."),
        fixed(200, "MAIN."),
        fixed(300, "    IF WS-OK = 'Y'"),
        fixed(400, "       CONTINUE"),
        fixed(500, "END-IF."),
        fixed(600, "    GOBACK."),
    ]) + "\n"
    result = ParagraphEntryDisplayComposer().compose(sample)
    assert "DISPLAY 'MAIN.'." in result
    assert "DISPLAY 'END-IF.'." not in result
    assert bodies(result).count("END-IF.") == 1


def test_unnumbered_sql_paragraph_uses_real_query_identity_not_undeclared_name():
    sample = "\n".join([
        fixed(100, "PROCEDURE DIVISION."),
        fixed(200, "LOOKUP-ROW."),
        fixed(300, "    EXEC SQL"),
        fixed(400, "        SELECT COL FROM SOMETV"),
        fixed(500, "        QUERYNO 432"),
        fixed(600, "    END-EXEC"),
        fixed(700, "    EVALUATE SQLCODE"),
        fixed(800, "       WHEN OTHER PERFORM SQLERROR"),
        fixed(900, "    END-EVALUATE."),
    ]) + "\n"
    result = FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql(sample)
    assert "MOVE 432 TO SQL-LOCATION" in result
    assert "SQL-STATEMENT" not in result


def test_no_query_identity_is_not_fabricated():
    sample = "\n".join([
        fixed(100, "PROCEDURE DIVISION."),
        fixed(200, "LOOKUP-ROW."),
        fixed(300, "    EXEC SQL"),
        fixed(400, "       SELECT COL FROM SOMETV"),
        fixed(500, "    END-EXEC"),
    ]) + "\n"
    result = FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql(sample)
    assert "SQL-STATEMENT" not in result
    assert "TO SQL-LOCATION" not in result


def test_timestamp_is_placed_inside_unambiguous_mainline_initialization():
    sample = [
        fixed(100, "PROCEDURE DIVISION."),
        fixed(200, "MAIN."),
        fixed(300, "    PERFORM INIT-INPUT"),
        fixed(400, "    PERFORM PROCESS-ROW"),
        fixed(500, "    GOBACK."),
        fixed(600, "INIT-INPUT."),
        fixed(700, "    OPEN INPUT INPUT-FILE."),
        fixed(800, "PROCESS-ROW."),
        fixed(900, "    CONTINUE."),
    ]
    result = TimestampParagraphBuilder().ensure_perform(sample)
    b = [line[7:72].strip() if line[:6].isdigit() else line.strip() for line in result]
    assert b.count("PERFORM 600-GET-TIMESTAMP.") == 1
    assert b.index("INIT-INPUT.") < b.index("PERFORM 600-GET-TIMESTAMP.") < b.index("OPEN INPUT INPUT-FILE.")


def test_timestamp_keeps_existing_perform_and_ambiguous_initialization_unchanged():
    sample = [fixed(100, "PROCEDURE DIVISION."), fixed(200, "MAIN."),
              fixed(300, "    PERFORM 600-GET-TIMESTAMP."), fixed(400, "    GOBACK.")]
    assert TimestampParagraphBuilder().ensure_perform(sample) == sample
