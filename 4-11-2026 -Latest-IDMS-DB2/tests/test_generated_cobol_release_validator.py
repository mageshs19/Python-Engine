from pathlib import Path

from converter.validators.generated_cobol_release_validator import validate_generated_cobol

ROOT = Path(__file__).resolve().parents[1]


def test_generated_vmdz4310_passes_structural_release_checks():
    # Always read the freshly regenerated member; timestamps are run artifacts.
    candidates = sorted((ROOT / "mainframe/workspace/Output").glob("VMDZ4310_*.cbl"))
    assert len(candidates) == 1, "one fresh generated member required"
    path = candidates[0]
    issues = validate_generated_cobol(path.read_text(encoding="utf-8", errors="replace"), path=str(path))
    assert issues == []


def test_validator_catches_projection_mismatch():
    source = """000010 PROCEDURE DIVISION.                                         00010000
000020     EXEC SQL                                                     00020000
000030       SELECT A, B INTO :HOST-A FROM T                            00030000
000040     END-EXEC.                                                    00040000
"""
    issues = validate_generated_cobol(source)
    assert any(issue.code == "SQL_PROJECTION_MISMATCH" for issue in issues)


def test_validator_catches_residual_idms_but_ignores_comments():
    source = """000010* OBTAIN NEXT RECORD-A is documented here.                    00010000
000020     OBTAIN NEXT RECORD-A.                                        00020000
"""
    issues = validate_generated_cobol(source)
    assert [issue.code for issue in issues] == ["RESIDUAL_OBTAIN"]


def test_validator_catches_unbalanced_inline_perform():
    source = """000010     PERFORM UNTIL EOF                                           00010000
"""
    issues = validate_generated_cobol(source)
    assert any(issue.code == "PERFORM_SCOPE_MISMATCH" for issue in issues)


def test_validator_catches_fixed_format_overflow():
    source = "000010 " + ("X" * 75) + "00010000"
    issues = validate_generated_cobol(source)
    assert any(issue.code == "FIXED_WIDTH" for issue in issues)


def test_validator_counts_inline_times_scope_and_ignores_paragraph_perform_until():
    source = """000010     PERFORM 200-READ UNTIL EOF                                  00010000
000020     PERFORM NB-READ OF WS-RESTART-REC TIMES                        00020000
000030         PERFORM 900-READ-INPUT                                    00030000
000040     END-PERFORM                                                  00040000
"""
    issues = validate_generated_cobol(source)
    assert not any(issue.code == "PERFORM_SCOPE_MISMATCH" for issue in issues)


def test_validator_counts_varying_inline_scope():
    source = """000010     PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > 5               00010000
000020         CONTINUE.                                                00020000
000030     END-PERFORM.                                                 00030000
"""
    issues = validate_generated_cobol(source)
    assert not any(issue.code == "PERFORM_SCOPE_MISMATCH" for issue in issues)


def test_validator_ignores_syntax_like_tokens_inside_literals_and_inline_comments():
    source = """       DISPLAY 'OBTAIN NEXT RECORD-A'.
       DISPLAY 'PERFORM UNTIL EOF END-PERFORM'.
       DISPLAY 'EXEC SQL END-EXEC'.
       CONTINUE. *> OBTAIN NEXT RECORD-B END-PERFORM
"""
    issues = validate_generated_cobol(source)
    assert issues == []


def test_sql_terminator_inside_quoted_sql_literal_does_not_close_block():
    source = """       EXEC SQL
         SELECT 'END-EXEC' INTO :HOST-A FROM TABLE_A
       END-EXEC.
"""
    issues = validate_generated_cobol(source)
    assert issues == []


def test_sql_terminator_inside_doubled_quote_literal_does_not_close_block():
    source = """       EXEC SQL
         SELECT 'IT''S END-EXEC' INTO :HOST-A FROM TABLE_A
       END-EXEC.
"""
    issues = validate_generated_cobol(source)
    assert issues == []


def test_validator_blocks_residual_executable_error_status_but_ignores_comment():
    source = """000010* ERROR-STATUS is mentioned in a comment.                      00010000
000020     IF ERROR-STATUS NOT = '0000'                                 00020000
"""
    issues = validate_generated_cobol(source)
    assert [issue.code for issue in issues] == ["RESIDUAL_ERROR_STATUS", "PERFORM_SCOPE_MISMATCH"] or any(
        issue.code == "RESIDUAL_ERROR_STATUS" for issue in issues
    )


def test_validator_blocks_period_that_makes_idms_stop_unconditional():
    source = """000010 PROCEDURE DIVISION.                                         00010000
000020     IF SQLCODE NOT = 0.                                          00020000
000030         PERFORM IDMS-STOP.                                       00030000
000040 IDMS-STOP.                                                       00040000
000050     EXEC SQL ROLLBACK END-EXEC.                                  00050000
"""
    issues = validate_generated_cobol(source)
    assert any(issue.code == "IDMS_STOP_IF_SCOPE_BROKEN" for issue in issues)


def test_validator_accepts_scoped_idms_stop_and_local_target():
    source = """000010 PROCEDURE DIVISION.                                         00010000
000020     IF SQLCODE NOT = 0                                           00020000
000030         PERFORM IDMS-STOP.                                       00030000
000040 IDMS-STOP.                                                       00040000
000050     EXEC SQL ROLLBACK END-EXEC.                                  00050000
"""
    issues = validate_generated_cobol(source)
    assert not any(issue.code in {"IDMS_STOP_IF_SCOPE_BROKEN", "IDMS_STOP_TARGET_MISSING"} for issue in issues)


def test_validator_blocks_unresolved_idms_stop_call():
    source = """000010 PROCEDURE DIVISION.                                         00010000
000020     PERFORM IDMS-STOP.                                           00020000
"""
    issues = validate_generated_cobol(source)
    assert any(issue.code == "IDMS_STOP_TARGET_MISSING" for issue in issues)


def test_validator_blocks_residual_idms_dml_and_access_commands():
    source = """000010     MODIFY CUSTOMER-REC.                                       00010000
000020     STORE CUSTOMER-REC.                                         00020000
000030     ERASE CUSTOMER-REC.                                         00030000
000040     BIND RUN-UNIT.                                              00040000
000050     READY CUSTOMER-AREA USAGE-MODE IS RETRIEVAL.                00050000
000060     FINISH.                                                     00060000
"""
    codes = [issue.code for issue in validate_generated_cobol(source)]
    assert codes == [
        "RESIDUAL_MODIFY", "RESIDUAL_STORE", "RESIDUAL_ERASE",
        "RESIDUAL_BIND", "RESIDUAL_READY", "RESIDUAL_FINISH",
    ]


def test_validator_ignores_idms_dml_words_in_comments_and_literals():
    source = """000010* MODIFY CUSTOMER-REC; STORE CUSTOMER-REC; ERASE CUSTOMER-REC. 00010000
000020     DISPLAY 'BIND RUN-UNIT READY AREA USAGE-MODE FINISH.'.       00020000
000030     CONTINUE. *> MODIFY CUSTOMER-REC
"""
    assert validate_generated_cobol(source) == []


def test_validator_refuses_move_to_reserved_statement_verbs():
    source = """000100     MOVE SOURCE TO WRITE.                                       00010000
000200     MOVE SOURCE TO FROM.                                        00020000
"""
    issues = validate_generated_cobol(source)
    assert [issue.code for issue in issues] == ["INVALID_MOVE_RECEIVER", "INVALID_MOVE_RECEIVER"]


def test_validator_accepts_normal_move_followed_by_write():
    source = """000100     MOVE SRC TO DEST                                            00010000
000200     WRITE OUTPUT-REC FROM OUTPUT-AREA.                          00020000
"""
    assert not any(issue.code == "INVALID_MOVE_RECEIVER" for issue in validate_generated_cobol(source))
