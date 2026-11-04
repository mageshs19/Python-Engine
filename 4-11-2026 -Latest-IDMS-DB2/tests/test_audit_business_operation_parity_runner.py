from pathlib import Path

from runners.audit_business_operation_parity import latest_candidate


def test_latest_candidate_includes_stable_names_and_uses_modification_time(tmp_path):
    old = tmp_path / "VMDZ1526_25-10-2026_090000.cbl"
    newest = tmp_path / "VMDZ1526_GENERIC_LOGIC_FIXED_V25.cbl"
    old.write_text("old", encoding="utf-8")
    newest.write_text("new", encoding="utf-8")
    old.touch()
    newest.touch()
    assert latest_candidate(tmp_path, "VMDZ1526") == newest


def test_latest_candidate_returns_none_when_no_candidate_exists(tmp_path):
    assert latest_candidate(tmp_path, "VMDZ1526") is None
