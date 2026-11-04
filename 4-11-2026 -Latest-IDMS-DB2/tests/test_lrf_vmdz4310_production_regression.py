from __future__ import annotations

import logging
import re
from pathlib import Path

from runners.retrieval.retrieval_input_loader import load_shared_inputs
from runners.retrieval.retrieval_program_converter import convert_one_program


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = PROJECT_ROOT / "mainframe/workspace/Program/VM4BD310.cbl"


def test_vmdz4310_lrf_parent_child_access_is_structurally_safe(tmp_path, capsys):
    logger = logging.getLogger("test-vmdz4310-lrf-regression")
    logger.addHandler(logging.NullHandler())
    logger.setLevel(logging.CRITICAL)
    sheet_rows, dclgen_columns, copybook_fields, shared_diagnostics = load_shared_inputs(logger)

    output_path = convert_one_program(
        program_path=PROGRAM_PATH,
        sheet_rows=sheet_rows,
        dclgen_columns=dclgen_columns,
        copybook_fields=copybook_fields,
        shared_diagnostics=shared_diagnostics,
        output_dir=tmp_path,
        project_root=PROJECT_ROOT,
        src_dir=PROJECT_ROOT,
        logger=logger,
    )
    generated = output_path.read_text(encoding="utf-8", errors="replace")
    console = capsys.readouterr().out
    assert "REVIEW_ONLY" not in output_path.name

    logical_body = " ".join(
        line[7:72].strip() if len(line) >= 7 and line[:6].isdigit() else line.strip()
        for line in generated.splitlines()
    )

    # The source's 13-byte key is split on its original declared reference
    # modification. The final numeric piece must be checked before moving
    # into the packed-decimal DCLGEN host, without a named-program helper.
    assert "WS-IN-NR-TIT-BC(1:12) TO NR-IDSTOCK-479BEFF" in logical_body
    assert "WS-IN-NR-TIT-BC(13:1) TO NR-CDSTK-479BEFF" in logical_body
    assert "IF WS-IN-NR-TIT-BC(13:1) IS NUMERIC" in logical_body
    assert "NON-NUMERIC DB2 KEY COMPONENT" in generated
    assert "HELP-NR-ID-STOCK-CD" not in generated

    # Parent lookup and child cursor use the same proven parent DCLGEN keys.
    assert "FROM DZBEFFTV" in generated
    assert "NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF" in generated
    assert "CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF" in generated
    assert "NO DATA FOUND FOR SELECT DZBEFFTV" in generated
    # Relationship-only FK rows from other IDMS records must not leak into
    # the parent SELECT projection merely because they share a DB2 table.
    parent_select_start = generated.index("SELECT", generated.index("MOVE 442 TO SQL-LOCATION"))
    parent_select_end = generated.index("FROM DZBEFFTV", parent_select_start)
    parent_projection = generated[parent_select_start:parent_select_end]
    assert "CO_IDISSUS_479WCEF" not in parent_projection
    assert "NS_IRMOS_479WCEF" not in parent_projection
    assert "DA_UBSECIS_479WCEF" not in parent_projection

    # 1:N record-group references are expanded only when component and target
    # widths are proven; the 14th destination byte is explicitly padded.
    assert "NR-CI1POS-479EVEF OF DCLDZEVEFTV TO NR-CIO-FORM-AS OF VMDZ510I(1:1)" in logical_body
    assert "NR-CI26POS-479EVEF OF DCLDZEVEFTV TO NR-CIO-FORM-AS OF VMDZ510I(2:5)" in logical_body
    assert "MOVE NR-ST-FORM-AS OF VMDZ510I TO NR-STIN-OORD OF VMDZ510I" in logical_body

    # The bounded inline LRF search is rendered as a singleton SELECT. Its
    # projection and INTO list must remain positionally identical, including
    # both mapped components expanded from the source NR-CI group.
    assert "DECLARE DZEVEFC1 CURSOR" not in generated
    assert "FETCH FIRST 1 ROW ONLY" in generated
    assert "CT_RKTEVPR_479EVEF = '0092'" in generated
    assert "PERFORM UNTIL DZEVEFC1-EOC" not in generated
    assert "IF DZEVEFC1-EOC" not in generated
    # The no-child-match business path must survive cursor-to-singleton
    # rewriting; SQLCODE=100 now represents the SELECT no-data result.
    assert "IF SQLCODE = 100" in generated
    assert "CALL USERABEN" in generated
    assert "NO MORE VMBEVEF" in generated
    child_from = generated.index("FROM DZEVEFTV")
    child_select_start = generated.rfind("SELECT", 0, child_from)
    child_select_end = generated.index("INTO", child_select_start)
    child_into_end = child_from
    child_projection = generated[child_select_start:child_select_end]
    child_into = generated[generated.index("INTO", child_select_start):child_into_end]
    selected_columns = re.findall(r"\b([A-Z][A-Z0-9_]*_479EVEF)\b", child_projection)
    fetched_hosts = re.findall(r":DCLDZEVEFTV\.([A-Z0-9-]+-479EVEF)\b", child_into)
    assert [column.replace("_", "-") for column in selected_columns] == fetched_hosts
    assert "NR_CI1POS_479EVEF" in child_projection
    assert "NR_CI26POS_479EVEF" in child_projection
    assert "NR-CI1POS-479EVEF" in child_into
    assert "NR-CI26POS-479EVEF" in child_into

    # No generated cursor machinery may remain after singleton rendering.
    assert "710-OPEN-DZEVEFC1." not in generated
    assert "720-FETCH-DZEVEFC1." not in generated
    assert "730-CLOSE-DZEVEFC1." not in generated
    assert "DZEVEFC1-EOC" not in generated
    assert "LRF populator: cursor DZEVEFC1 already uses parent DCLGEN group DCLDZBEFFTV" in console
    assert "LrfHostVariablePopulator' object has no attribute '_log'" not in console
    assert "OPEN of cursor DZEVEFC1 is performed" not in console
    assert "ON ANY-ERROR-STATUS" not in generated
    assert "ERROR-STATUS is undefined after copybook removal" not in console
    assert "PERFORM IDMS-STATUS" not in generated
    assert "COPY IDMS IDMS-STATUS" not in generated

    # The fixed-format wrapper must split at word boundaries without a
    # continuation indicator that would concatenate adjacent COBOL tokens.
    assert all(len(line) == 80 for line in generated.splitlines() if len(line) >= 7 and line[:6].isdigit())
    assert "DB-REC-NOT-FOUND" not in generated
    assert "OBTAIN CALC" not in generated

    # No executable IDMS record references may survive for the LRF records.
    for line in generated.splitlines():
        if len(line) > 6 and line[6] not in ("*", "/"):
            assert not re.search(r"\b(?:OF|IN)\s+VMBEFF\b", line, re.I), line
            assert not re.search(r"\b(?:OF|IN)\s+VMBEVEF\b", line, re.I), line
            assert not re.match(r"^\s*DISPLAY\s+VMBEFF\b", line, re.I), line
            assert not re.match(r"^\s*DISPLAY\s+VMBEVEF\b", line, re.I), line

    # Generated fixed-format statements fit their source area, and comments
    # remain comments instead of becoming executable continuation lines.
    for line in generated.splitlines():
        if len(line) >= 7 and line[:6].isdigit():
            assert len(line[7:72].rstrip()) <= 65, line
            if line[6] == "*":
                assert line[6] == "*"

    # The reporting layer must not emit workbook-wide 1:N warnings for records
    # that this program never references.
    assert "Field decomposition: KY-VMBFAS OF VMBFAS" not in console
    assert "Field decomposition: AT-GDIFAR OF VMBFAR" not in console
    assert "LRF production gate: BLOCKED" not in console
    assert "CT-RKTPROD-479BEFF03160000" not in console

    # Manual parity and fixed-format/compiler-safety regressions.
    # Source member has no live data references, so generic liveness removes it.
    assert "COPY VMDZ05." not in generated
    assert "COPY VMBD05" not in generated.upper()
    assert "*DB2:" not in generated
    assert "WS-DATUMVELDEN" in generated
    assert "DA-CCYYMMDD-R TO DA-UB-FORM-AS OF VMDZ510I" in generated
    assert "DA-CCYYMMDD-R TO DA-EXEC-OORD OF VMDZ510I" in generated
    assert "MOVE 442 TO SQL-LOCATION." in generated
    assert "SQL-STATEMENT" not in generated
