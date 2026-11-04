from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
from tests.workspace_fixtures import generated_program
LATEST = generated_program("VMDZ4310")


def test_latest_vmdz4310_artifact_is_singleton_not_cursor_based():
    text = LATEST.read_text(encoding="utf-8", errors="replace")
    upper = text.upper()

    # This file is the fresh full-pipeline conversion, not the historical
    # 164736 cursor-stage fixture used by the focused rewriter unit tests.
    assert "DECLARE DZEVEFC1 CURSOR" not in upper
    assert "OPEN DZEVEFC1" not in upper
    assert "FETCH DZEVEFC1" not in upper
    assert "CLOSE DZEVEFC1" not in upper
    assert "DZEVEFC1-EOC" not in upper

    assert "FETCH FIRST 1 ROW ONLY" in upper
    assert "CT_RKTEVPR_479EVEF = '0092'" in upper
    assert "ORDER BY NR_ID_479EVEF DESC" in upper

    # Fixed-format COBOL contract: 6-column sequence + indicator + 65-column
    # source area + 8-column identification area.
    for line in text.splitlines():
        if len(line) >= 7 and line[:6].isdigit():
            assert len(line[7:72].rstrip()) <= 65, line
            assert len(line) <= 80, line

    # A SELECT/INTO mismatch would make the singleton conversion unsafe.
    from_start = upper.index("FROM DZEVEFTV")
    select_start = upper.rfind("SELECT", 0, from_start)
    block = upper[select_start:from_start]
    selected = re.findall(r"\b[A-Z][A-Z0-9_]*_479EVEF\b", block.split("INTO", 1)[0])
    into = block.split("INTO", 1)[1]
    hosts = re.findall(r":DCLDZEVEFTV\.([A-Z0-9-]+-479EVEF)\b", into)
    assert selected and len(selected) == len(hosts)
    assert [column.replace("_", "-") for column in selected] == hosts
