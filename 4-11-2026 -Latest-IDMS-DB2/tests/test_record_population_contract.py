from pathlib import Path
from mainframe.verification.record_population_contract import audit_record_population


def _program(body):
    return ("000100 DATA DIVISION.\n"
            "000200 WORKING-STORAGE SECTION.\n"
            "000300 01 OUT-BUFFER.\n"
            "000400    05 HEADER PIC X(2).\n"
            "000500    05 AMOUNT PIC S9(7)V99 COMP-3.\n"
            "000600    05 GROUP-DATE.\n"
            "000700       10 YEAR PIC 9(4).\n"
            "000800       10 MONTH PIC 9(2).\n"
            "000900    05 FILLER PIC X(4).\n"
            "001000 PROCEDURE DIVISION.\n"
            "001100 MAIN.\n"
            + ''.join(f'{1200 + n*100:06d}     {line}\n' for n,line in enumerate(body)) +
            "002500     GOBACK.\n")


def test_complete_numeric_coverage_passes():
    code = _program(['MOVE SPACES TO OUT-BUFFER', 'MOVE 99 TO AMOUNT',
                     'MOVE 2026 TO YEAR', 'MOVE 10 TO MONTH',
                     'WRITE FB-REC FROM OUT-BUFFER.'])
    assert audit_record_population(code) == ()


def test_missing_numeric_assignment_rejected_even_when_layout_correct():
    code = _program(['MOVE SPACES TO OUT-BUFFER', 'MOVE 99 TO AMOUNT',
                     'MOVE 2026 TO YEAR', 'WRITE FB-REC FROM OUT-BUFFER.'])
    defects = audit_record_population(code)
    assert len(defects) == 1
    assert defects[0].level == 'FAIL' and defects[0].field == 'MONTH'


def test_move_into_parent_group_covers_child_fields():
    code = _program(['MOVE 99 TO AMOUNT', 'MOVE DATE-STAGE TO GROUP-DATE',
                     'WRITE FB-REC FROM OUT-BUFFER.'])
    assert audit_record_population(code) == ()


def test_initialize_counts_as_numeric_assignment_not_move_spaces():
    code = _program(['INITIALIZE OUT-BUFFER', 'WRITE FB-REC FROM OUT-BUFFER.'])
    assert audit_record_population(code) == ()


def test_renamed_buffer_fields_same_generic_behavior():
    original = _program(['MOVE 99 TO AMOUNT', 'WRITE FB-REC FROM OUT-BUFFER.'])
    text = original.replace('OUT-BUFFER', 'OUT-DATA').replace('AMOUNT', 'TOTAL')
    assert {f.field for f in audit_record_population(text)} == {'YEAR', 'MONTH'}


def test_real_generated_7200_numeric_fields_have_assignments():
    root = Path(__file__).resolve().parents[1]
    members = sorted((root / 'mainframe/workspace/Output').glob('VMDZ7200_*.cbl'))
    if not members:
        import pytest
        pytest.skip('Optional immutable integration fixture not present')
    assert audit_record_population(members[-1].read_text(errors='replace')) == ()


def test_same_named_target_of_unrelated_group_does_not_cover_output():
    code = _program(['MOVE 9 TO AMOUNT OF OTHER-BUFFER',
                     'MOVE 2026 TO YEAR', 'MOVE 10 TO MONTH',
                     'WRITE FB-REC FROM OUT-BUFFER.'])
    assert {f.field for f in audit_record_population(code)} == {'AMOUNT'}


def test_generated_output_would_fail_if_mapped_numeric_move_were_dropped():
    root = Path(__file__).resolve().parents[1]
    members = sorted((root / 'mainframe/workspace/Output').glob('VMDZ7200_*.cbl'))
    if not members:
        import pytest
        pytest.skip('Optional immutable integration fixture not present')
    text = members[-1].read_text(errors='replace')
    # Simulate the generic converter dropping one mapped field assignment.
    # Preserve valid COBOL syntax by replacing the MOVE with CONTINUE.
    import re
    pattern = (r'(?m)^\d{6}\s+MOVE\s+NR-IDFMAS-479BFAS OF DCLDZBFASTV TO\s*\d{8}\n'
               r'\d{6}\s+NR-ID-FORM-AS OF VMBFAS')
    # A wrapped MOVE can have the source's target on the following fixed line.
    assert re.search(pattern, text)
    bad = re.sub(pattern, '999990     CONTINUE', text, count=1)
    assert any(f.field == 'NR-ID-FORM-AS' and f.level == 'FAIL'
               for f in audit_record_population(bad))
