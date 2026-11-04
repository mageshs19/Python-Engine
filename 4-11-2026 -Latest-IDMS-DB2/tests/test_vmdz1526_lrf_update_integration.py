from pathlib import Path
import re
from tempfile import TemporaryDirectory

from converter.infrastructure.logger_factory import LoggerFactory
from runners.update.update_input_loader import load_shared_inputs
from runners.update.update_program_converter import convert_one_program


def _logical_cobol(text: str) -> str:
    logical_lines = []
    for line in text.splitlines():
        if len(line) >= 7 and line[:6].isdigit():
            logical_lines.append(line[7:72].strip())
        else:
            logical_lines.append(line.strip())
    return "\n".join(logical_lines)


def _matching_paren(text: str, open_index: int) -> int:
    depth = 0
    quoted = False
    index = open_index
    while index < len(text):
        char = text[index]
        if char == "'":
            if quoted and index + 1 < len(text) and text[index + 1] == "'":
                index += 2
                continue
            quoted = not quoted
        elif not quoted and char == "(":
            depth += 1
        elif not quoted and char == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    raise AssertionError("unbalanced SQL parentheses")


def _split_top_level_commas(text: str) -> list[str]:
    values = []
    start = 0
    depth = 0
    quoted = False
    index = 0
    while index < len(text):
        char = text[index]
        if char == "'":
            if quoted and index + 1 < len(text) and text[index + 1] == "'":
                index += 2
                continue
            quoted = not quoted
        elif not quoted and char == "(":
            depth += 1
        elif not quoted and char == ")":
            depth -= 1
        elif not quoted and depth == 0 and char == ",":
            values.append(text[start:index].strip())
            start = index + 1
        index += 1
    tail = text[start:].strip()
    if tail:
        values.append(tail)
    return values


def test_vmdz1526_lrf_store_and_update_generate_singleton_sql_without_cursor(tmp_path):
    root = Path(__file__).resolve().parents[1]
    from tests.workspace_fixtures import expanded_program
    source = expanded_program("VMDZ1526")
    assert source.exists(), "VMDZ1526 expanded integration fixture is required"

    logger = LoggerFactory.create_logger(
        name="test_vmdz1526_lrf_update_integration",
        logs_dir=tmp_path / "vmdz1526_lrf_update_integration_logs",
    )
    sheet_rows, dclgen_columns, copybook_fields, diagnostics = load_shared_inputs(logger)

    with TemporaryDirectory(prefix="vmdz1526_lrf_update_") as temp_dir:
        output_path = convert_one_program(
            program_path=source,
            sheet_rows=sheet_rows,
            dclgen_columns=dclgen_columns,
            copybook_fields=copybook_fields,
            shared_diagnostics=diagnostics,
            output_dir=Path(temp_dir),
            project_root=root,
            src_dir=root,
            logger=logger,
        )
        generated = output_path.read_text(encoding="utf-8", errors="replace")

    assert not re.search(r"\bDECLARE\s+\w+\s+CURSOR\b", generated, re.I)
    assert not re.search(r"\b(?:OPEN|FETCH|CLOSE)\s+DZEVEFC1\b", generated, re.I)
    assert len(re.findall(r"\bINSERT\s+INTO\s+DZEVEFTV\b", generated, re.I)) == 1
    assert len(re.findall(r"\bSELECT\s+NR_ID_479EVEF\b", generated, re.I)) == 1
    assert "FETCH FIRST 1 ROW ONLY" in generated
    insert_match = re.search(
        r"INSERT INTO DZEVEFTV(?P<body>.*?)END-EXEC", generated, re.I | re.S
    )
    assert insert_match, "business INSERT must be generated"
    insert_sql = insert_match.group("body")
    logical = _logical_cobol(generated)
    insert_start = logical.upper().index("INSERT INTO DZEVEFTV")
    column_open = logical.index("(", insert_start)
    column_close = _matching_paren(logical, column_open)
    values_start = logical.upper().index("VALUES", column_close)
    values_open = logical.index("(", values_start)
    values_close = _matching_paren(logical, values_open)
    insert_columns = _split_top_level_commas(logical[column_open + 1:column_close])
    insert_values = _split_top_level_commas(logical[values_open + 1:values_close])
    assert len(insert_columns) == 16, f"expected all 16 manual-contract columns, got {len(insert_columns)}"
    assert len(insert_values) == len(insert_columns), "INSERT column/value arity must match"
    for required in (
        "NR_ID_479EVEF", "TS_CREATE_479EVEF", "TS_UPDATE_479EVEF",
        "ID_USERID_479EVEF", "NS_IDMSKEY_479EVEF",
        "NEXT VALUE FOR DZEVEFSQ", "RIGHT(DIGITS",
    ):
        assert required in insert_sql, f"missing required INSERT logic: {required}"
    assert "9999-12-31-23.59.59.999999" in generated
    assert "TO TS-UPDATE-479EVEF OF DCLDZEVEFTV" in generated
    assert "MOVE ZERO TO NS-IDMSKEY-479EVEF OF DCLDZEVEFTV" in generated
    assert "INITIALIZE DCLDZBEFFTV DCLDZEVEFTV" in generated
    init_position = logical.index("INITIALIZE DCLDZBEFFTV DCLDZEVEFTV")
    parent_move_position = logical.index("MOVE '1002' TO CT-RKTPROD-479BEFF OF DCLDZBEFFTV")
    assert init_position < parent_move_position, "record buffers must be initialized before field population"
    assert not any(
        len(line) >= 8
        and line[:6].isdigit()
        and line[6] in (" ", "*")
        and line[7:72].strip() == "VMBEVEF."
        for line in generated.splitlines()
    ), "continuation operand must not survive as a label or orphan comment"
    assert not re.search(r"IF SQLCODE = 100 OR 'LR-ERROR'", generated, re.I)
    assert "MOVE 0 TO NR-IDISSUE-479BEFF OF DCLDZBEFFTV." in generated
    assert "MOVE 0 TO NR-CDISSUE-479BEFF OF DCLDZBEFFTV." in generated, \
        "a COBOL MOVE with multiple receiving fields must preserve both targets"
    assert re.search(
        r"MOVE NS-DB-STOCK-FORM-AS-R TO NS-DBSTK-479BEFF\s*\n\s*OF DCLDZBEFFTV\.",
        logical,
        re.I,
    ), "a precision-matched numeric child must be used instead of moving a group to a packed host"
    assert "MOVE NS-DB-STOCK-FORM-AS TO NS-DBSTK-479BEFF OF DCLDZBEFFTV." not in generated
    assert not re.search(r"^[0-9]{6}\s+NR-CDISSUE-479BEFF OF DCLDZBEFFTV\.", generated, re.I | re.M), \
        "the second MOVE target must not survive as a bare invalid COBOL statement"
    assert "AND CT_RKTEVPR_479EVEF = '0168'" in generated
    assert "AND CT_RKTGDSV_479EVEF = '0219'" in generated
    assert len(re.findall(r"\bFROM\s+DZBEFFTV\b", generated, re.I)) == 1
    assert len(re.findall(r"^[0-9]{6}\s+UPDATE\s+DZEVEFTV\b", generated, re.I | re.M)) == 1
    assert "NR_ID_479EVEF = :DCLDZEVEFTV.NR-ID-479EVEF" in generated
    assert "MOVE CT-RKTPROD-479BEFF OF DCLDZBEFFTV" in generated
    assert "TO CT-RKTPROD-479BEFF OF DCLDZEVEFTV" in generated

    # COBOL periods terminate every open scope. The parent-success IF must
    # remain open across all setup moves, the INSERT, and its SQLCODE handler;
    # a period on TS-CREATE/TS-UPDATE used to close it early and allow orphan
    # child inserts when the parent SELECT returned SQLCODE 100.
    parent_select_end = logical.upper().index("FROM DZBEFFTV")
    parent_gate_start = logical.upper().index("IF SQLCODE = 0", parent_select_end)
    parent_gate_end = logical.upper().index("END-IF.", parent_gate_start)
    gated_block = logical[parent_gate_start:parent_gate_end]
    assert "INSERT INTO DZEVEFTV" in gated_block, "child INSERT must be inside the parent-success IF"
    assert not any(line.strip() == "." for line in gated_block.splitlines()), "no standalone period may close the parent IF early"
    assert not any(
        line.rstrip().endswith(".") and line.strip().upper().startswith(("MOVE ", "INITIALIZE ", "PERFORM "))
        for line in gated_block.splitlines()
    ), "setup statements inside the parent IF must not terminate the scope"
    assert "EXEC SQL INCLUDE DZ01RSTV END-EXEC." in generated
    assert "SELECT NM_ID_RS_PROGRAM" in generated
    assert "INSERT INTO DZ01RSTV" in generated
    assert "UPDATE DZ01RSTV" in generated
    assert re.search(r"\bCOMMIT\b", generated, re.I)
    assert "DB2-KEEP" not in generated
    assert not re.search(r"^[0-9]{6}\*=.*(?:OBTAIN|STORE|WHERE|CALCKEY)", generated, re.M | re.I)
