from converter.composers.unnecessary_comments_cleanup_composer import (
    UnnecessaryCommentsCleanupComposer,
)
from converter.services.final_generated_output_service import (
    FinalGeneratedOutputService,
)


def _fixed(body: str, seq: int = 100) -> str:
    indicator = "*" if body.startswith("*") else " "
    source_body = body[1:] if indicator == "*" else body
    return f"{seq:06d}{indicator}{source_body:<65}"[:72].ljust(72) + f"{seq * 100:08d}"


def _body(line: str) -> str:
    return line[7:72].rstrip()


def test_removes_generated_db2_narration_and_orphaned_continuations():
    source = "\n".join(
        [
            _fixed("*DB2: Removed obsolete cursor EOC flag declaration.", 100),
            _fixed("*DB2: Removed redundant key-group clear; all mapped CALC key", 200),
            _fixed("*components are initialized and assigned before SELECT.", 300),
            _fixed("*DB2: Removed cursor EOC branch; SQLCODE handles no-data.", 400),
            _fixed("*Business rule: keep this explanation.", 500),
            _fixed("*DB2-KEEP: retain this review decision.", 600),
        ]
    ) + "\n"

    composer = UnnecessaryCommentsCleanupComposer()
    result = composer.compose(source)
    bodies = [_body(line) for line in result.splitlines()]

    assert not any("Removed obsolete cursor" in body for body in bodies)
    assert not any("Removed redundant key-group" in body for body in bodies)
    assert not any("components are initialized" in body for body in bodies)
    assert not any("Removed cursor EOC branch" in body for body in bodies)
    assert any("Business rule: keep this explanation." in body for body in bodies)
    assert any("DB2-KEEP: retain this review decision." in body for body in bodies)


def test_final_output_pass_cleans_comments_and_resequences_afterward():
    source = "\n".join(
        [
            _fixed("IDENTIFICATION DIVISION.", 100),
            _fixed("PROGRAM-ID. SAMPLE.", 200),
            _fixed("PROCEDURE DIVISION.", 300),
            _fixed("MAIN.", 400),
            _fixed("    DISPLAY 'OK'.", 500),
            _fixed("*DB2: Removed obsolete cursor EOC flag declaration.", 600),
            _fixed("*DB2: Expanded LRF FIRST VMBTL07-R01 WHERE ALL-VMBEVEF-BY-VMBEFF", 650),
            _fixed("*  -> VMBEVEF WITHIN VMBEFF-VMBEVEF.", 660),
            _fixed("*DB2-KEEP: retain this review decision.", 670),
            _fixed("    STOP RUN.", 700),
        ]
    ) + "\n"

    service = FinalGeneratedOutputService()
    result = service.apply(source)
    lines = result.splitlines()

    assert all(len(line) == 80 for line in lines)
    assert [int(line[:6]) for line in lines] == sorted(int(line[:6]) for line in lines)
    assert not any("Removed obsolete cursor" in line for line in lines)
    assert not any("*DB2: Expanded LRF" in line for line in lines)
    assert not any("VMBEVEF WITHIN VMBEFF" in line for line in lines)
    assert any("DB2-KEEP: retain this review decision." in _body(line) for line in lines)
    assert any("DISPLAY 'OK'." in _body(line) for line in lines)
    assert any("STOP RUN." in _body(line) for line in lines)


def test_final_output_removes_orphaned_record_label_comment_before_sql():
    source = "\n".join(
        [
            _fixed("IDENTIFICATION DIVISION.", 100),
            _fixed("PROGRAM-ID. SAMPLE.", 200),
            _fixed("PROCEDURE DIVISION.", 300),
            _fixed("MAIN.", 400),
            _fixed("    MOVE 220 TO SQL-LOCATION.", 500),
            _fixed("*  VMBEVEF.", 600),
            _fixed("    EXEC SQL", 700),
            _fixed("       UPDATE SAMPLETV", 800),
            _fixed("    END-EXEC.", 900),
            _fixed("    STOP RUN.", 1000),
        ]
    ) + "\n"

    result = FinalGeneratedOutputService().apply(source)

    assert not any(_body(line).strip() == "VMBEVEF." for line in result.splitlines())
    assert any("UPDATE SAMPLETV" in _body(line) for line in result.splitlines())


def test_final_output_removes_empty_sqlcode_guard_before_next_paragraph():
    source = "\n".join(
        [
            _fixed("IDENTIFICATION DIVISION.", 100),
            _fixed("PROGRAM-ID. SAMPLE.", 200),
            _fixed("PROCEDURE DIVISION.", 300),
            _fixed("MAIN.", 400),
            _fixed("    IF SQLCODE NOT = 0.", 500),
            _fixed("220-NEXT-PARA.", 600),
            _fixed("    CONTINUE.", 700),
        ]
    ) + "\n"

    result = FinalGeneratedOutputService().apply(source)
    bodies = [_body(line).strip() for line in result.splitlines()]

    assert "IF SQLCODE NOT = 0." not in bodies
    assert "220-NEXT-PARA." in bodies


def test_final_output_removes_extra_filter_note_only_when_sql_consumed_it():
    consumed = "\n".join([
        _fixed("PROCEDURE DIVISION.", 100),
        _fixed("*  AND CT-RK-TGDSV = '0219' - add to the generated cursor WHERE.", 200),
        _fixed("    EXEC SQL", 300),
        _fixed("       SELECT NR_ID_479EVEF", 400),
        _fixed("         FROM DZEVEFTV", 500),
        _fixed("        WHERE CT_RKTGDSV_479EVEF = '0219'", 600),
        _fixed("    END-EXEC", 700),
    ]) + "\n"
    result = FinalGeneratedOutputService().apply(consumed)
    assert not any("add to the generated cursor WHERE" in line for line in result.splitlines())

    unconsumed = "\n".join([
        _fixed("PROCEDURE DIVISION.", 100),
        _fixed("*  AND CT-RK-TGDSV = '0219' - add to the generated cursor WHERE.", 200),
        _fixed("    EXEC SQL", 300),
        _fixed("       SELECT NR_ID_479EVEF", 400),
        _fixed("         FROM DZEVEFTV", 500),
        _fixed("        WHERE CT_RKTGDSV_479EVEF = '0168'", 600),
        _fixed("    END-EXEC", 700),
    ]) + "\n"
    result = FinalGeneratedOutputService().apply(unconsumed)
    assert any("add to the generated cursor WHERE" in line for line in result.splitlines())


def test_final_output_adds_sql_location_for_legacy_runtime_sql_without_one():
    source = "\n".join([
        _fixed("PROCEDURE DIVISION.", 100),
        _fixed("700-SELECT-RESTART.", 200),
        _fixed("    EXEC SQL", 300),
        _fixed("       SELECT CO_ID_RS", 400),
        _fixed("         FROM DZ01RSTV", 500),
        _fixed("    END-EXEC", 600),
        _fixed("    EVALUATE SQLCODE", 700),
        _fixed("       WHEN OTHER", 800),
        _fixed("          PERFORM SQLERROR", 900),
        _fixed("    END-EVALUATE", 1000),
    ]) + "\n"
    result = FinalGeneratedOutputService().apply(source)
    bodies = [_body(line).strip() for line in result.splitlines()]
    location_index = next(i for i, body in enumerate(bodies) if body == "MOVE 700 TO SQL-LOCATION")
    select_index = next(i for i, body in enumerate(bodies) if body == "EXEC SQL")
    assert location_index < select_index



def test_final_output_removes_obsolete_conversion_breadcrumb_but_keeps_neighboring_comments():
    source = "\n".join([
        _fixed("PROCEDURE DIVISION.", 100),
        _fixed("MAIN.", 200),
        _fixed("*Business rule: retain this explanation.", 300),
        _fixed("*DB2: deleted by the IDMS conversion. Original: OBTAIN FIRST SAMPLE.", 400),
        _fixed("*DB2-KEEP: retain this review decision.", 500),
        _fixed("    DISPLAY 'OK'.", 600),
     ]) + "\n"

    result = FinalGeneratedOutputService().apply(source)
    bodies = [_body(line).strip() for line in result.splitlines()]

    assert not any("deleted by the IDMS conversion. Original:" in body for body in bodies)
    assert any("Business rule: retain this explanation." in body for body in bodies)
    assert any("DB2-KEEP: retain this review decision." in body for body in bodies)
    assert any("DISPLAY 'OK'." in body for body in bodies)


def test_lrf_error_condition_keeps_scope_over_following_stop_perform():
    source = "\n".join(
        [
            _fixed("PROCEDURE DIVISION.", 100),
            _fixed("    IF SQLCODE = 100 OR 'LR-ERROR'", 200),
            _fixed("       PERFORM IDMS-STOP.", 300),
            _fixed("NEXT-PARA.", 400),
            _fixed("    CONTINUE.", 500),
        ]
    ) + "\n"

    result = FinalGeneratedOutputService().apply(source)
    bodies = [_body(line).strip() for line in result.splitlines()]
    condition_index = bodies.index("IF SQLCODE NOT = 0")
    assert bodies[condition_index + 1] == "PERFORM IDMS-STOP."
    assert "IF SQLCODE NOT = 0." not in bodies
