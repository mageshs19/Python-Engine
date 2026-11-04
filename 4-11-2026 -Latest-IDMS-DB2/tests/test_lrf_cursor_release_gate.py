from pathlib import Path

from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter
from converter.validators.generated_cobol_release_validator import validate_generated_cobol

ROOT = Path(__file__).resolve().parents[1]
STALE = ROOT / "tests" / "fixtures" / "legacy_generated" / "VMDZ4310_21-10-2026_164736.cbl"


def test_release_gate_rejects_stale_bounded_lrf_cursor_artifact():
    source = STALE.read_text(encoding="utf-8", errors="replace")
    issues = validate_generated_cobol(source)
    assert any(issue.code == "LRF_BOUNDED_CURSOR_REMAINS" for issue in issues)


def test_singleton_rewrite_removes_cursor_and_matches_manual_projection():
    source = STALE.read_text(encoding="utf-8", errors="replace")
    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed, result.diagnostic
    assert "DECLARE DZEVEFC1 CURSOR" not in result.text
    assert "OPEN DZEVEFC1" not in result.text
    assert "FETCH DZEVEFC1" not in result.text
    assert "CLOSE DZEVEFC1" not in result.text
    assert "DZEVEFC1-EOC" not in result.text
    assert "710-OPEN-DZEVEFC1." not in result.text
    assert "720-FETCH-DZEVEFC1." not in result.text
    assert "730-CLOSE-DZEVEFC1." not in result.text
    assert "AND CT_RKTEVPR_479EVEF = '0092'" in result.text
    assert "ORDER BY NR_ID_479EVEF DESC" in result.text
    assert "FETCH FIRST 1 ROW ONLY" in result.text
    for column in (
        "NR_IDGOOD_479EVEF",
        "NR_CI1POS_479EVEF",
        "NR_CI26POS_479EVEF",
        "DA_CREVTPD_479EVEF",
    ):
        assert column in result.text
    assert max(map(len, result.text.splitlines())) <= 80
    issues = validate_generated_cobol(result.text)
    assert not any(issue.code == "LRF_BOUNDED_CURSOR_REMAINS" for issue in issues)


def test_rewriter_refuses_stale_cursor_when_downstream_child_fields_were_not_fetched():
    stale_projection = ROOT / "tests" / "fixtures" / "legacy_generated" / "VMDZ4310_21-10-2026_153528.cbl"
    source = stale_projection.read_text(encoding="utf-8", errors="replace")
    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is False
    assert result.text == source
    assert "NR-CI1POS-479EVEF" in source
    assert "NR_CI1POS_479EVEF" not in source
