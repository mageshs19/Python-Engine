from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
from tests.workspace_fixtures import generated_program
GENERATED = generated_program("VMDZ4310")
MANUAL = ROOT / "mainframe/workspace/Manual Output/VMDZ4310.txt"


def _sql_block(text: str, table: str) -> str:
    marker = f"FROM {table}"
    end = text.index(marker)
    start = text.rfind("SELECT", 0, end)
    return text[start:end]


def test_parent_select_projection_is_minimal_and_into_aligned():
    generated = GENERATED.read_text(encoding="utf-8", errors="replace")
    block = _sql_block(generated, "DZBEFFTV")
    projection = block[block.index("SELECT"):block.index("INTO")]
    into = block[block.index("INTO"):]
    columns = re.findall(r"\b([A-Z][A-Z0-9_]*_479BEFF)\b", projection)
    hosts = re.findall(r":DCLDZBEFFTV\.([A-Z0-9-]+-479BEFF)\b", into)
    assert len(columns) == len(hosts) == 12
    assert [c.replace("_", "-") for c in columns] == hosts
    assert "CT_RKTPRDX_479BEFF" not in projection
    assert "NX_CPFDUSK_479BEFF" not in projection
    assert "AM_CNDSTK_479BEFF" in projection  # used by downstream business logic
    assert columns.count("NX_CPCRESK_479BEFF") == 1


def test_input_and_treated_totals_are_both_counted_and_displayed():
    generated = GENERATED.read_text(encoding="utf-8", errors="replace")
    assert "PIC S9(11) COMP-3 VALUE +0" in generated
    assert "ADD 1 TO WS-TOTAL-INPUT" in generated
    assert re.search(r"DISPLAY\s+'TOTAL INPUTS\s*=\s*'\s+WS-TOTAL-INPUT", generated)
    assert "ADD 1 TO WS-COUNT-TREATED" in generated
    assert "DISPLAY '# TREATED" in generated


def test_bounded_lrf_is_singleton_and_fixed_format_is_clean():
    generated = GENERATED.read_text(encoding="utf-8", errors="replace")
    assert "DECLARE DZEVEFC1 CURSOR" not in generated
    assert "OPEN DZEVEFC1" not in generated
    assert "FETCH DZEVEFC1" not in generated
    assert "CLOSE DZEVEFC1" not in generated
    assert "FETCH FIRST 1 ROW ONLY" in generated
    assert "CT_RKTEVPR_479EVEF = '0092'" in generated
    assert all(len(line) == 80 for line in generated.splitlines())
    assert max(len(line[7:72].rstrip()) for line in generated.splitlines()) <= 65


def test_manual_reference_has_total_input_and_treated_counters():
    manual = MANUAL.read_text(encoding="utf-8", errors="replace")
    assert "WS-TOTAL-INPUT" in manual
    assert "WS-COUNT-TREATED" in manual
    assert "ADD 1 TO WS-TOTAL-INPUT" in manual
    assert "ADD 1        TO WS-COUNT-TREATED" in manual
