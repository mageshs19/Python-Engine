from pathlib import Path
import pytest
from mainframe.verification.fixed_record_diff import compare, main


def _files(tmp_path: Path, a: bytes, b: bytes):
    m, g = tmp_path / 'manual.bin', tmp_path / 'generated.bin'
    m.write_bytes(a)
    g.write_bytes(b)
    return m, g


def test_equal_bytes_and_order(tmp_path):
    m, g = _files(tmp_path, b'AAAA' + b'BBBB', b'AAAA' + b'BBBB')
    v = compare(m, g, 4)
    assert v.passed and v.manual.records == 2


def test_changed_content_reports_byte_and_record(tmp_path):
    m, g = _files(tmp_path, b'AAAA' + b'BBBB', b'AAAA' + b'BCBB')
    v = compare(m, g, 4)
    assert not v.passed and v.first_mismatched_record == 2
    assert v.first_mismatched_byte == 2


def test_order_is_a_semantic_difference(tmp_path):
    m, g = _files(tmp_path, b'AAAA' + b'BBBB', b'BBBB' + b'AAAA')
    assert compare(m, g, 4).first_mismatched_record == 1


def test_record_count_mismatch(tmp_path):
    m, g = _files(tmp_path, b'AAAA' + b'BBBB', b'AAAA')
    assert compare(m, g, 4).reason == 'different record counts'


def test_reject_vb_or_text_newlines(tmp_path):
    m, g = _files(tmp_path, b'AAAA\nBBBB\n', b'AAAA\nBBBB\n')
    assert not compare(m, g, 4).passed


def test_empty_both_is_equal_but_requires_external_selection_proof(tmp_path):
    m, g = _files(tmp_path, b'', b'')
    assert compare(m, g, 530).passed


def test_filler_byte_changes_are_reported(tmp_path):
    m, g = _files(tmp_path, b'X' * 478 + b'Y' * 52, b'X' * 477 + b'Z' + b'Y' * 52)
    result = compare(m, g, 530)
    assert result.first_mismatched_record == 1
    assert result.first_mismatched_byte == 478


def test_same_file_is_rejected(tmp_path):
    m, _ = _files(tmp_path, b'AAAA', b'AAAA')
    with pytest.raises(ValueError):
        compare(m, m, 4)


def test_cli_nonzero_on_mismatch(tmp_path):
    m, g = _files(tmp_path, b'AAAA', b'AAAB')
    out = tmp_path / 'diff.json'
    assert main(['--manual', str(m), '--generated', str(g), '--record-size', '4', '--report', str(out)]) == 2
    assert 'first_mismatched_byte' in out.read_text()
