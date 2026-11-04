from converter.validators.generated_cobol_release_validator import validate_generated_cobol


def test_retrieval_handwritten_obtain_calc_is_not_silently_removed(transformer_context):
    transformer = transformer_context["statement_transformer"]
    transformer.program_kind = "retrieval"
    transformer.lrf_calc_records = set()

    lines, _ = transformer.transform_line(
        line="OBTAIN CALC VMB-FAR.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    text = "\n".join(lines)

    assert "DB2-KEEP: OBTAIN CALC VMB-FAR lacks a verified keyed SELECT" in text
    assert "OBTAIN CALC VMB-FAR." in text
    assert "Removed OBTAIN CALC SELECT" not in text
    assert any("source retained" in message for message in transformer.messages)


def test_release_gate_blocks_unconverted_handwritten_retrieval_obtain_calc():
    text = """000100 PROCEDURE DIVISION.                                            00010000
000200*DB2-KEEP: OBTAIN CALC VMB-FAR lacks a verified keyed SELECT.       00020000
000300     OBTAIN CALC VMB-FAR.                                           00030000
"""
    issues = validate_generated_cobol(text)
    assert any(issue.code == "RESIDUAL_OBTAIN" for issue in issues)


def test_update_obtain_calc_legacy_removal_is_unchanged(transformer_context):
    transformer = transformer_context["statement_transformer"]
    transformer.program_kind = "update"
    transformer.lrf_calc_records = set()

    lines, _ = transformer.transform_line(
        line="OBTAIN CALC VMB-FAR.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    text = "\n".join(lines)
    assert "Removed OBTAIN CALC SELECT" in text
    assert "OBTAIN CALC VMB-FAR." not in text


def test_proven_handwritten_retrieval_calc_emits_keyed_select(transformer_context):
    transformer = transformer_context["statement_transformer"]
    transformer.program_kind = "retrieval"
    transformer.lrf_calc_records = set()
    transformer.handwritten_calc_plans = {
        "VMB-FAR": {
            "existence_column": "NR_ID",
            "dclgen_group": "DCLDZBFARTV",
            "table": "DZBFARTV",
            "key_columns": "NR_ID",
        }
    }

    lines, _ = transformer.transform_line(
        line="OBTAIN CALC VMB-FAR",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    text = "\n".join(lines)
    assert "EXEC SQL" in text
    assert "SELECT" in text
    assert "WHERE" in text
    assert "END-EXEC" in text
    assert "EVALUATE SQLCODE" not in text
    assert transformer._active_handwritten_calc_record == "VMB-FAR"


def test_handwritten_calc_status_guards_map_only_in_active_scope(transformer_context):
    transformer = transformer_context["statement_transformer"]
    transformer._active_handwritten_calc_record = "VMB-FAR"
    transformer._active_handwritten_calc_group = "DCLDZBFARTV"

    lines, _ = transformer.transform_line(
        line="IF ERROR-STATUS NOT = '0000'",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    assert lines == ["IF SQLCODE NOT = 0"]

    lines, _ = transformer.transform_line(
        line="IF ERROR-STATUS = '0000'",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    assert lines == ["IF SQLCODE = 0"]

    lines, _ = transformer.transform_line(
        line="DISPLAY 'VMB-FAR ' VMB-FAR",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    assert lines == ["DISPLAY 'VMB-FAR ' DCLDZBFARTV"]


def test_handwritten_calc_status_scope_ends_before_next_idms_access(transformer_context):
    transformer = transformer_context["statement_transformer"]
    transformer._active_handwritten_calc_record = "VMB-FAR"
    transformer._active_handwritten_calc_group = "DCLDZBFARTV"
    transformer.transform_line(
        line="OBTAIN FIRST CHILD-A WITHIN REC-A-CHILD-A",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )
    assert transformer._active_handwritten_calc_record == ""
