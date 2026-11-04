from pathlib import Path
from mainframe.verification.record_write_contract import audit_fixed_record_writes

BASE = Path(__file__).resolve().parents[1] / 'mainframe' / 'workspace' / 'Output'


def _text(name):
    return next(BASE.glob(f'{name}_*.cbl')).read_text(errors='replace')


def test_physical_write_contracts_hold_for_retrieval_programs():
    for name in ('VMDZ4302', 'VMDZ7200'):
        problems = [p for p in audit_fixed_record_writes(_text(name)) if p.level == 'FAIL']
        assert not problems, (name, problems)


def test_missing_filler_is_a_release_failure():
    text = _text('VMDZ7200')
    import re
    broken = re.sub(r'^.*06\s+FILLER\s+PIC\s+X\(0046\).*$\n?', '', text, flags=re.M)
    assert broken != text
    findings = audit_fixed_record_writes(broken)
    assert any(p.level == 'FAIL' and '484 bytes' in p.reason for p in findings)


def test_unsupported_layout_does_not_fake_success():
    text = '''FILE SECTION.\nFD TEST-OUT\n RECORD CONTAINS 4 CHARACTERS.\n01 OUT-REC PIC X(4).\nWORKING-STORAGE SECTION.\n01 DATA-REC.\n 05 A PIC X OCCURS 1 TO 4 TIMES DEPENDING ON N.\nPROCEDURE DIVISION.\n WRITE OUT-REC FROM DATA-REC.\n'''
    findings = audit_fixed_record_writes(text)
    assert any(f.level == 'UNVERIFIED' for f in findings)


def test_write_literal_is_not_a_file_operation():
    source = """FILE SECTION.
FD TEST-OUT
 RECORD CONTAINS 4 CHARACTERS.
01 OUT-REC PIC X(4).
WORKING-STORAGE SECTION.
PROCEDURE DIVISION.
 DISPLAY 'WRITE OUT-REC FROM FAKE-NAME'.
"""
    assert not audit_fixed_record_writes(source)
