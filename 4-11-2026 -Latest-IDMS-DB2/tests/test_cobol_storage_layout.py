from pathlib import Path
import pytest
from mainframe.verification.cobol_storage_layout import group_byte_length, child_byte_lengths

BASE = Path(__file__).resolve().parents[1] / 'mainframe' / 'workspace' / 'Manual Output'
GENERATED = Path(__file__).resolve().parents[1] / 'mainframe' / 'workspace' / 'Output'


def test_redefines_preserves_offsets_not_double_count():
    s = '''01 TEST-REC.\n  05 A PIC X(4).\n  05 B REDEFINES A PIC 9(4).\n  05 C PIC S9(13)V99 COMP-3.\n'''
    assert group_byte_length(s, 'TEST-REC') == 12


def test_unknown_storage_fails_closed():
    s = '''01 TEST-REC.\n  05 A PIC X(4) OCCURS 1 TO 3 TIMES DEPENDING ON COUNT.\n'''
    with pytest.raises(ValueError):
        group_byte_length(s, 'TEST-REC')


def test_vmdz7200_manual_layout_contract():
    s = (BASE / 'VMDZ7200.cbl').read_text(errors='replace')
    assert group_byte_length(s, 'REC-FORM') == 530
    assert child_byte_lengths(s, 'REC-FORM')['F-FORM'] == 478


def test_vmdz7200_generated_layout_contract():
    p = sorted(GENERATED.glob('VMDZ7200_*.cbl'))
    assert len(p) == 1
    s = p[0].read_text(errors='replace')
    assert group_byte_length(s, 'REC-FORM') == 530
    assert child_byte_lengths(s, 'REC-FORM')['F-FORM'] == 478
