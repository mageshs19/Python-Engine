"""Generic COPY provenance and output-buffer data-flow regressions."""
from pathlib import Path

import pytest

from mainframe.verification.cobol_storage_layout import group_byte_length
from mainframe.verification.copybook_provenance import resolve_copybooks
from mainframe.verification.record_population_contract import audit_record_population
from mainframe.verification.record_write_contract import audit_fixed_record_writes
from mainframe.zowe_copybook_upload import require_copybook_upload_configuration


def test_fixed_occurs_group_and_leaf_and_redefines():
    text = '''01 RECORD-A.
 05 HEAD PIC X(2).
 05 REPEAT-GROUP OCCURS 3 TIMES.
   10 AMOUNT PIC S9(3) COMP-3.
   10 FLAG PIC X.
 05 REPEAT-LEAF PIC X(4) OCCURS 2 TIMES.
 05 OTHER REDEFINES REPEAT-LEAF PIC X(8).
'''
    assert group_byte_length(text, 'RECORD-A') == 2 + 3 * 3 + 8


@pytest.mark.parametrize('clause', ['OCCURS 1 TO 7 TIMES DEPENDING ON N',
                                    'OCCURS XX', 'OCCURS 0 TIMES'])
def test_variable_or_unsafe_occurs_is_not_assumed_fixed(clause):
    with pytest.raises(ValueError):
        group_byte_length(f'01 A.\n 05 X PIC X {clause}.', 'A')


def test_derived_copybook_expands_only_when_source_copy_proves_name(tmp_path):
    inputs = tmp_path / 'input'
    inputs.mkdir()
    (inputs / 'VMBD123I.cpy').write_text('01 VMBD123I.\n 05 N PIC 9(3) COMP-3.\n 05 FILLER PIC X(2).\n')
    source = 'COPY VMBD123I.\n'
    target = 'FILE SECTION.\nFD OUTFILE RECORD CONTAINS 4 CHARACTERS.\n01 OUTREC PIC X(4).\nWORKING-STORAGE SECTION.\nCOPY VMDZ123I.\nPROCEDURE DIVISION.\nP.\n INITIALIZE VMDZ123I.\n WRITE OUTREC FROM VMDZ123I.\n'
    result = resolve_copybooks(source, target, inputs, tmp_path / 'stage')
    assert not result.errors
    assert result.staged_members == (tmp_path / 'stage' / 'VMDZ123I.cpy',)
    assert 'COPY VMDZ123I' in target
    assert '01 VMDZ123I.' in result.expanded_text
    assert not audit_fixed_record_writes(result.expanded_text)
    assert not audit_record_population(result.expanded_text)


def test_no_original_copy_provenance_blocks_derivation(tmp_path):
    result = resolve_copybooks('', 'COPY VMDZ123I.', tmp_path, tmp_path / 'stage')
    assert result.errors and not result.staged_members


def test_source_copybook_with_nested_copy_is_blocked(tmp_path):
    (tmp_path / 'VMBD123I.cpy').write_text('01 VMBD123I.\n 05 X PIC X.\nCOPY OTHER.\n')
    result = resolve_copybooks('COPY VMBD123I.', 'COPY VMDZ123I.', tmp_path, tmp_path / 'stage')
    assert result.errors and not result.staged_members


def test_missing_output_copybook_dataset_blocks_before_network(tmp_path, monkeypatch):
    (tmp_path / 'Generated Copybooks').mkdir()
    (tmp_path / 'Generated Copybooks' / 'VMDZ123I.cpy').write_text('01 VMDZ123I PIC X.')
    monkeypatch.delenv('ZOWE_GENERATED_COPYBOOK_DATASET', raising=False)
    with pytest.raises(ValueError, match='ZOWE_GENERATED_COPYBOOK_DATASET'):
        require_copybook_upload_configuration(tmp_path)


def test_sequential_initializer_proves_other_paragraph_write():
    text = '''FILE SECTION.
FD OUTFILE RECORD CONTAINS 2 CHARACTERS.
01 OUTREC PIC X(2).
WORKING-STORAGE SECTION.
01 DATA-REC.
 05 NUM PIC 9(2).
PROCEDURE DIVISION.
DRIVER.
 PERFORM PREPARE.
 PERFORM EMIT.
PREPARE.
 INITIALIZE DATA-REC.
EMIT.
 WRITE OUTREC FROM DATA-REC.
'''
    assert not audit_record_population(text)
    broken = text.replace(' PERFORM PREPARE.\n', '')
    assert any(item.level == 'FAIL' for item in audit_record_population(broken))


def test_conditional_initializer_is_not_accepted_as_proof():
    text = '''FILE SECTION.
FD OUTFILE RECORD CONTAINS 2 CHARACTERS.
01 OUTREC PIC X(2).
WORKING-STORAGE SECTION.
01 DATA-REC.
 05 NUM PIC 9(2).
PROCEDURE DIVISION.
DRIVER.
 PERFORM PREPARE.
 PERFORM EMIT.
PREPARE.
 IF SWITCH = 'Y' INITIALIZE DATA-REC END-IF.
EMIT.
 WRITE OUTREC FROM DATA-REC.
'''
    assert any(item.level == 'FAIL' for item in audit_record_population(text))


def test_real_source_copybook_matches_documented_output_layout(tmp_path):
    workspace = Path(__file__).resolve().parents[1] / 'mainframe' / 'workspace'
    source = (workspace / 'Program' / 'VM4BD310.cbl').read_text(encoding='latin1')
    target = next((workspace / 'Output').glob('VMDZ4310_*.cbl')).read_text(encoding='latin1')
    result = resolve_copybooks(source, target, workspace / 'Copybook', tmp_path)
    assert not result.errors
    assert not audit_fixed_record_writes(result.expanded_text)
    assert not audit_record_population(result.expanded_text)
    assert group_byte_length((tmp_path / 'VMDZ510I.cpy').read_text(encoding='latin1'), 'VMDZ510I') == 1500


def test_copybook_name_is_not_rewritten_inside_value_literal(tmp_path):
    (tmp_path / 'VMBD123I.cpy').write_text(
        "01 VMBD123I.\n 05 DATA-NAME PIC X(8) VALUE 'VMBD123I'.\n"
    )
    result = resolve_copybooks('COPY VMBD123I.', 'COPY VMDZ123I.',
                               tmp_path, tmp_path / 'staged')
    assert not result.errors
    staged = result.staged_members[0].read_text()
    assert '01 VMDZ123I.' in staged
    assert "VALUE 'VMBD123I'" in staged


def test_copybook_replacing_without_period_is_blocked(tmp_path):
    (tmp_path / 'VMBD123I.cpy').write_text(
        "01 VMBD123I.\n COPY NESTED REPLACING ==A== BY ==B==.\n"
    )
    result = resolve_copybooks('COPY VMBD123I.', 'COPY VMDZ123I.',
                               tmp_path, tmp_path / 'staged')
    assert result.errors and 'nested COPY' in result.errors[0]
