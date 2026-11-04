"""IDMS-STOP may carry program-specific rollback and abend semantics."""

from patterns.cobol_transformer_patterns import IDMS_ABORT_PARAGRAPH_PATTERN


def test_idms_stop_paragraph_is_not_treated_as_orphan_idms_abort():
    assert IDMS_ABORT_PARAGRAPH_PATTERN.match("IDMS-ABORT.")
    assert not IDMS_ABORT_PARAGRAPH_PATTERN.match("IDMS-STOP.")


def test_perform_idms_stop_is_retained_instead_of_silently_removed(transformer_context):
    transformer = transformer_context["statement_transformer"]
    lines, _ = transformer.transform_line(
        line="PERFORM IDMS-STOP.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQLERROR",
    )
    joined = "\n".join(lines).upper()
    assert "PERFORM IDMS-STOP" in joined
    assert "REMOVED IDMS PERFORM IDMS-STOP" not in joined


def test_rollback_is_emitted_as_db2_sql(transformer_context):
    transformer = transformer_context["statement_transformer"]
    lines, _ = transformer.transform_line(
        line="ROLLBACK.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQLERROR",
    )
    joined = "\n".join(lines).upper()
    assert "EXEC SQL" in joined
    assert "ROLLBACK" in joined
    assert "END-EXEC" in joined
