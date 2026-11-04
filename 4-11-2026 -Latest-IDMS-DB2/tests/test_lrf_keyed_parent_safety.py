"""Safety contract for retrieval-side LRF-generated keyed parent reads."""


def test_lrf_calc_read_generates_executable_parent_select(statement_transformer):
    transformer = statement_transformer
    transformer.program_kind = "retrieval"
    transformer.lrf_calc_records = {"VMB-FAR"}

    lines, _opened = transformer.transform_line(
        line="OBTAIN CALC VMB-FAR.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    text = "\n".join(lines).upper()

    assert "EXEC SQL" in text
    assert "SELECT" in text
    assert "INTO" in text
    assert "FROM DZBFARTV" in text
    assert "WHERE" in text
    assert "LRF KEYED READ BLOCKED" not in text
    assert "REMOVED OBTAIN CALC SELECT" not in text
