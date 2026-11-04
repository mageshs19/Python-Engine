"""Executable SQL contract for retrieval-side LRF keyed parent reads."""


def test_lrf_parent_select_populates_mapped_record_and_uses_key(
    transformer_context,
):
    sql = transformer_context["statement_transformer"].sql_generator.select_by_key(
        "VMB-FAR", for_lrf_parent=True
    )
    text = "\n".join(sql).upper()

    assert "EXEC SQL" in text
    assert "SELECT" in text
    assert "INTO" in text
    assert "FROM DZBFARTV" in text
    assert "WHERE" in text
    assert "NR_ID = :DCLDZBFARTV.NR-ID" in text
    assert ":DCLDZBFARTV.NR-ID" in text
    assert ":DCLDZBFARTV.CD-NAME" in text
    assert "WHEN 100" in text
    assert "WHEN 100" in text
    assert "REMOVED OBTAIN CALC SELECT" not in text


def test_ordinary_obtain_calc_keeps_legacy_update_behavior(transformer_context):
    sql = transformer_context["statement_transformer"].sql_generator.select_by_key(
        "VMB-FAR"
    )
    text = "\n".join(sql).upper()
    assert "REMOVED OBTAIN CALC SELECT" in text
    assert "EXEC SQL" not in text


def test_lrf_parent_select_sets_sql_location_before_sql_and_not_inside_when_other(
    transformer_context,
):
    sql = transformer_context["statement_transformer"].sql_generator.select_by_key(
        "VMB-FAR", for_lrf_parent=True
    )
    text = "\n".join(sql).upper()
    evaluate = text.index("EVALUATE SQLCODE")
    end_evaluate = text.index("END-EVALUATE", evaluate)
    branch = text[evaluate:end_evaluate]
    assert "MOVE 'SELECT-VMB-FAR' TO SQL-LOCATION." not in branch
    assert text.index("MOVE 'SELECT-VMB-FAR' TO SQL-LOCATION.") < text.index("EXEC SQL")
    assert "WHEN OTHER" in branch
    assert "PERFORM SQLERROR" in branch
