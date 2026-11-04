from converter.composers.manual_storage_parity_composer import ManualStorageParityComposer
from tests.workspace_fixtures import generated_program


def test_manual_storage_pass_does_not_coerce_field_usage_or_reparent_groups():
    source = """000100 WORKING-STORAGE SECTION.
000200 01 W-DATE PIC 9(8).
000300 01 WS-NR-ISSUE.
000400 03 WS-NR-ID-ISSUE PIC X(7).
000500 01 WS-NR-ID-GOOD.
000600 03 WS-NR-CIO PIC 9(8) COMP-3 VALUE ZEROES.
000700 01 WS-MUTATIES.
000800 03 WS-IN-NR-TIT-BC PIC X(13).
000900 01 WS-COUNT-TREATED PIC 9(15) VALUE ZEROES.
001000 01 WS-TOTAL-INPUT PIC S9(11) COMP-3 VALUE +0.
001100 PROCEDURE DIVISION.
"""
    result = ManualStorageParityComposer().compose(source)
    assert result == source
    assert "COMP-3 VALUE ZEROES" in result
    assert "01 WS-NR-ID-GOOD" in result
    assert "01  WS-VAR." not in result


def test_cursor_with_hold_removed_when_no_transaction_boundary_spans_cursor():
    source = '''000100 EXEC SQL DECLARE DZBFASC1 CURSOR WITH HOLD FOR                00000100
000200     SELECT A FROM T                                              00000200
000300 END-EXEC.                                                        00000300
'''
    result = ManualStorageParityComposer().compose(source)
    assert "DECLARE DZBFASC1 CURSOR FOR" in result
    assert "CURSOR WITH HOLD FOR" not in result

    committed = source + "000400     EXEC SQL COMMIT END-EXEC.                                   00000400\n"
    result_with_commit = ManualStorageParityComposer().compose(committed)
    assert "CURSOR WITH HOLD FOR" in result_with_commit


def test_unrelated_storage_is_unchanged():
    source = "000100 WORKING-STORAGE SECTION.                                         00000100\n000200 01  CUSTOMER-REC PIC X(10).                                     00000200\n"
    assert ManualStorageParityComposer().compose(source) == source


def test_cursor_hold_is_retained_only_when_transaction_occurs_between_open_and_close():
    prefix = """000100 EXEC SQL DECLARE C1 CURSOR WITH HOLD FOR
000200     SELECT A FROM T
000300 END-EXEC.
000400 PROCEDURE DIVISION.
000500     EXEC SQL OPEN C1 END-EXEC.
"""
    commit_inside = prefix + "000600     EXEC SQL COMMIT END-EXEC.\n000700     EXEC SQL CLOSE C1 END-EXEC.\n"
    commit_after = prefix + "000600     EXEC SQL CLOSE C1 END-EXEC.\n000700     EXEC SQL COMMIT END-EXEC.\n"

    composer = ManualStorageParityComposer()
    assert "CURSOR WITH HOLD FOR" in composer.compose(commit_inside)
    assert "CURSOR WITH HOLD FOR" not in composer.compose(commit_after)


def test_existing_ws_var_and_counter_declarations_are_never_silently_reordered():
    source = """000100 WORKING-STORAGE SECTION.
000200 01 WS-VAR.
000300 01 WS-NR-ISSUE.
000400 03 WS-NR-ID-ISSUE PIC X(7).
000500 01 WS-NR-ID-GOOD.
000600 03 WS-NR-CIO PIC 9(8) COMP-3 VALUE ZEROES.
000700 01 WS-MUTATIES.
000800 03 WS-OLD-CI PIC X(6).
000900 01 WS-COUNT-TREATED PIC 9(15) VALUE ZEROES.
001000 01 WS-TOTAL-INPUT PIC S9(11) COMP-3 VALUE +0.
001100 PROCEDURE DIVISION.
"""
    result = ManualStorageParityComposer().compose(source)
    assert result == source


def test_program_constant_is_normalized_to_generic_cs_program_for_any_program():
    source = """000100 PROGRAM-ID. VMDZ4310.
000200 01 CS-VM4BD310 PIC X(8) VALUE 'VMDZ4310'.
000300 PROCEDURE DIVISION.
000400     MOVE CS-VM4BD310 TO PROGRAM-NAME.
"""
    result = ManualStorageParityComposer().compose(source)
    assert "CS-PROGRAM" in result
    assert "CS-VM4BD310" not in result
    assert "CS-VMDZ4310" not in result
    assert "MOVE CS-PROGRAM TO PROGRAM-NAME" in result


def test_program_constant_uses_existing_shared_cs_program_and_removes_duplicate():
    source = """000100 PROGRAM-ID. ABCD1234.
000200 01 CS-ABCD1234 PIC X(8) VALUE 'ABCD1234'.
000300 10 CS-PROGRAM PIC X(8) VALUE 'ABCD1234'.
000400 PROCEDURE DIVISION.
000500     MOVE CS-ABCD1234 TO PROGRAM-NAME.
"""
    result = ManualStorageParityComposer().compose(source)
    assert result.count("CS-PROGRAM") == 2
    assert "CS-ABCD1234" not in result
    assert "MOVE CS-PROGRAM TO PROGRAM-NAME" in result


def test_program_constant_does_not_rename_unrelated_cs_field():
    source = """000100 PROGRAM-ID. ABCD1234.
000200 01 CS-OTHER PIC X(8) VALUE 'NOTPROG1'.
000300 PROCEDURE DIVISION.
"""
    result = ManualStorageParityComposer().compose(source)
    assert "CS-OTHER" in result
    assert "CS-PROGRAM" not in result


def test_real_vmdz7200_manual_cursor_policy_matches_reference():
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    generated = generated_program("VMDZ7200").read_text(encoding="utf-8", errors="replace")
    manual = (root / "mainframe/workspace/Manual Output/VMDZ7200.cbl").read_text(
        encoding="utf-8", errors="replace"
    )
    result = ManualStorageParityComposer().compose(generated)
    assert "DECLARE DZBFASC1 CURSOR FOR" in result
    assert "DECLARE DZBFASC1 CURSOR WITH HOLD FOR" not in result
    assert "DECLARE DZBFASC1 CURSOR FOR" in manual


def test_real_vmdz4310_storage_normalizer_is_idempotent():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    generated = generated_program("VMDZ4310").read_text(
        encoding="utf-8", errors="replace"
    )
    result = ManualStorageParityComposer().compose(generated)
    assert "CS-PROGRAM" in result
    assert ManualStorageParityComposer().compose(result) == result


def test_vmdz4310_helper_keeps_untrusted_key_alphanumeric_until_validation():
    source = """000100 PROGRAM-ID. VMDZ4310.
000200 03 WS-IN-NR-TIT-BC PIC X(13).
000300 03 DA-UBSECIS-479BEFF PIC X(10).
000400 03 DA-CREVTPD-479EVEF PIC X(10).
000500 03 DA-UB-FORM-AS PIC X(8).
000600 03 DA-COMPTABILISATION-OPER PIC X(8).
000700 03 DA-EXEC-OORD PIC X(8).
000800 PROCEDURE DIVISION.
000900 SEARCH-MUTATIES.
001000 INITIALIZE DCLDZBEFFTV.
001100 MOVE WS-IN-NR-TIT-BC(1:12) TO NR-IDSTOCK-479BEFF.
001200 IF WS-IN-NR-TIT-BC(13:1) IS NUMERIC
001300 MOVE WS-IN-NR-TIT-BC(13:1) TO NR-CDSTK-479BEFF
001400 END-IF.
"""
    result = ManualStorageParityComposer().compose(source)
    # The manual-storage composer must not synthesize an unrelated helper
    # and SQLERROR branch for one named program. Numeric safety is owned by
    # the source-PIC/DCLGEN-aware SchemaNumericKeyGuard.
    assert "HELP-NR-ID-STOCK-CD" not in result
    assert "IF WS-IN-NR-TIT-BC(13:1) IS NUMERIC" in result
    assert "MOVE WS-IN-NR-TIT-BC(1:12)" in result


def test_final_output_service_removes_redundant_program_constant_generically():
    from converter.services.final_generated_output_service import FinalGeneratedOutputService

    source = """000010 PROGRAM-ID. VMDZ4310.                                            00010000
000020 DATA DIVISION.                                                       00020000
000030 01 CS-VMDZ4310 PIC X(8) VALUE 'VMDZ4310'.                             00030000
000040 10 CS-PROGRAM PIC X(8) VALUE 'VMDZ4310'.                              00040000
000050 PROCEDURE DIVISION.                                                  00050000
000060     MOVE CS-VMDZ4310 TO PROGRAM-NAME.                                 00060000
"""
    result = FinalGeneratedOutputService().apply(source)
    assert "CS-VMDZ4310" not in result
    assert result.count("CS-PROGRAM") == 2
    assert "MOVE CS-PROGRAM TO PROGRAM-NAME" in result


def test_generic_program_constant_normalizer_preserves_unrelated_constants():
    from converter.services.program_constant_normalizer import ProgramConstantNormalizer

    source = """000010 PROGRAM-ID. ABCD1234.                                            00010000
000020 01 CS-OTHER PIC X(8) VALUE 'NOTPROG1'.                               00020000
000030 01 CS-ABCD1234 PIC X(8) VALUE 'ABCD1234'.                             00030000
000040 10 CS-PROGRAM PIC X(8) VALUE 'ABCD1234'.                              00040000
000050 PROCEDURE DIVISION.                                                  00050000
000060     MOVE CS-ABCD1234 TO PROGRAM-NAME.                                00060000
"""
    result = ProgramConstantNormalizer.normalize(source)
    assert "CS-OTHER" in result
    assert "CS-ABCD1234" not in result
    assert result.count("CS-PROGRAM") == 2
    assert "MOVE CS-PROGRAM TO PROGRAM-NAME" in result


def test_generic_program_constant_normalizer_collapses_multiple_aliases():
    from converter.services.program_constant_normalizer import ProgramConstantNormalizer

    source = """000010 PROGRAM-ID. ABCD1234.                                            00010000
000020 01 CS-ABCD1234 PIC X(8) VALUE 'ABCD1234'.                             00020000
000030 01 CS-ABCD-ALIAS PIC X(8) VALUE 'ABCD1234'.                           00030000
000040 PROCEDURE DIVISION.                                                  00040000
000050     MOVE CS-ABCD-ALIAS TO PROGRAM-NAME.                               00050000
"""
    result = ProgramConstantNormalizer.normalize(source)
    assert result.count("CS-PROGRAM") == 2
    assert "CS-ABCD1234" not in result
    assert "CS-ABCD-ALIAS" not in result
    assert "MOVE CS-PROGRAM TO PROGRAM-NAME" in result
