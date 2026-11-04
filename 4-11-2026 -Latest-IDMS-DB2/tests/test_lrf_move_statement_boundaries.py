"""MOVE collectors must respect next-verb boundaries in period-free COBOL."""
from converter.composers.lrf_group_move_decomposer import LrfGroupMoveDecomposer


def _line(number: int, statement: str) -> str:
    return f"{number:06d}     {statement:<61}00000000"


def _collector() -> LrfGroupMoveDecomposer:
    # The MOVE collector uses only its geometry, not mapping/DCLGEN services.
    return LrfGroupMoveDecomposer(
        mapping_repository=None, dclgen_repository=None,
        copybook_repository=None, table_name_resolver=None,
        host_variable_resolver=None,
    )


def test_write_from_is_not_consumed_by_preceding_period_free_move():
    lines = [
        _line(100, "MOVE SOURCE-FIELD TO TARGET-FIELD"),
        _line(200, "WRITE OUTPUT-REC FROM OUTPUT-AREA"),
        _line(300, "END-IF."),
    ]
    statement, consumed = _collector()._collect_move(lines, 0)
    assert statement == "MOVE SOURCE-FIELD TO TARGET-FIELD"
    assert consumed == 1


def test_continued_receiving_fields_remain_part_of_move():
    lines = [
        _line(100, "MOVE 0 TO FIRST-FIELD"),
        _line(200, "SECOND-FIELD"),
        _line(300, "WRITE OUT-REC FROM OUT-AREA"),
    ]
    statement, consumed = _collector()._collect_move(lines, 0)
    assert statement == "MOVE 0 TO FIRST-FIELD SECOND-FIELD"
    assert consumed == 2


def test_other_cobol_verbs_terminate_multi_destination_collection():
    for verb in ("READ FILE-A", "REWRITE REC-A", "CLOSE FILE-A", "COMPUTE X = 2", "ADD 1 TO X"):
        lines = [_line(100, "MOVE A TO B"), _line(200, verb)]
        assert _collector()._collect_move(lines, 0) == ("MOVE A TO B", 1)
