from __future__ import annotations
import logging
from pathlib import Path

from runners.retrieval.retrieval_input_loader import load_shared_inputs
from runners.retrieval.retrieval_program_converter import convert_one_program

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "mainframe/workspace/Program/VM4BD310.cbl"


def _body(line: str) -> str:
    if len(line) >= 7 and line[:6].isdigit():
        return line[7:72].strip()
    return line.strip()


def _convert(tmp_path: Path) -> tuple[str, str]:
    logger = logging.getLogger("test-vmdz4310-multiline-access")
    logger.addHandler(logging.NullHandler())
    logger.setLevel(logging.CRITICAL)
    sheet_rows, dclgen_columns, copybook_fields, diagnostics = load_shared_inputs(logger)
    output_path = convert_one_program(
        program_path=SOURCE,
        sheet_rows=sheet_rows,
        dclgen_columns=dclgen_columns,
        copybook_fields=copybook_fields,
        shared_diagnostics=diagnostics,
        output_dir=tmp_path,
        project_root=ROOT,
        src_dir=ROOT,
        logger=logger,
    )
    return output_path.read_text(encoding="utf-8", errors="replace"), "\n".join(diagnostics)


def test_lrf_first_marker_is_recovered_even_when_comment_wraps(tmp_path: Path) -> None:
    generated, _ = _convert(tmp_path)
    # Final delivery output intentionally removes converter *DB2: narration;
    # the business predicate and the resulting singleton SELECT are the
    # durable evidence that the LRF path was converted.
    assert "*DB2: Expanded LRF" not in generated
    assert "FETCH FIRST 1 ROW ONLY" in generated
    assert "CT_RKTEVPR_479EVEF = '0092'" in generated
    # The LRF child lookup must not replace the keyed parent read or leak
    # the obsolete IDMS status pseudo-condition into DB2 COBOL.
    assert "FROM DZBEFFTV" in generated
    assert "MOVE 442 TO SQL-LOCATION." in generated
    assert "SELECT-VMBEFF" not in generated
    assert "ON ANY-ERROR-STATUS" not in generated


def test_vmdz4310_until_condition_is_split_across_physical_lines_but_preserved(
    tmp_path: Path,
) -> None:
    source_lines = SOURCE.read_text(encoding="utf-8", errors="replace").splitlines()
    first = next(i for i, line in enumerate(source_lines) if "PERFORM UNTIL LR-STATUS" in line)
    assert "NO-MORE-VMBEVEF" in _body(source_lines[first])
    assert "CT-EVENT OF VMBEVEF = '0092'" in _body(source_lines[first + 1])

    generated, _ = _convert(tmp_path)
    # The business predicate from the second physical line is recognized and
    # pushed into SQL rather than left as a COBOL loop condition.
    assert "CT_RKTEVPR_479EVEF = '0092'" in generated
    # The complete generated inline bounded-search block is rewritten to a
    # singleton SELECT; the physical source line break is not a blocker.
    assert "DECLARE DZEVEFC1 CURSOR" not in generated
    assert "FETCH FIRST 1 ROW ONLY" in generated
    assert "CT_RKTEVPR_479EVEF = '0092'" in generated
    assert "PERFORM UNTIL DZEVEFC1-EOC" not in generated
    assert "710-OPEN-DZEVEFC1." not in generated
    assert "720-FETCH-DZEVEFC1." not in generated
    assert "730-CLOSE-DZEVEFC1." not in generated
    assert "NR_CI1POS_479EVEF" in generated
    assert "NR_CI26POS_479EVEF" in generated
    assert all(len(line) <= 80 for line in generated.splitlines())
