from converter.validators.compiler_safety_validator import CompilerSafetyValidator


def test_flags_value_clause_on_redefines_declaration():
    source = """       01 BASE-KEY PIC X(8).
       01 ALT-KEY REDEFINES BASE-KEY PIC 9(8) VALUE ZEROES.
"""
    messages = CompilerSafetyValidator().validate(source)
    assert any("REDEFINES declaration has a VALUE clause" in m for m in messages)


def test_accepts_redefines_without_value_clause():
    source = """       01 BASE-KEY PIC X(8).
       01 ALT-KEY REDEFINES BASE-KEY PIC 9(8).
"""
    messages = CompilerSafetyValidator().validate(source)
    assert not any("REDEFINES declaration has a VALUE clause" in m for m in messages)


def test_flags_cursor_select_fetch_count_mismatch():
    source = """       EXEC SQL DECLARE C1 CURSOR FOR
         SELECT COL_A, COL_B FROM TABLE_A
       END-EXEC.
       EXEC SQL FETCH C1 INTO :DCLTAB.COL-A END-EXEC.
"""
    messages = CompilerSafetyValidator().validate(source)
    assert any("cursor C1 selects 2 column(s) but FETCH binds 1" in m for m in messages)


def test_accepts_matching_cursor_select_fetch_counts():
    source = """       EXEC SQL DECLARE C1 CURSOR FOR
         SELECT COL_A, COL_B FROM TABLE_A
       END-EXEC.
       EXEC SQL FETCH C1 INTO :DCLTAB.COL-A, :DCLTAB.COL-B END-EXEC.
"""
    messages = CompilerSafetyValidator().validate(source)
    assert not any("cursor C1 selects" in m for m in messages)


def test_flags_unbalanced_exec_sql_block():
    source = """       EXEC SQL DECLARE C1 CURSOR FOR
         SELECT COL_A FROM TABLE_A
"""
    messages = CompilerSafetyValidator().validate(source)
    assert any("lack END-EXEC" in m for m in messages)


def test_production_validator_includes_compiler_preflight_findings():
    from converter.repositories.dclgen_repository import DclgenRepository
    from converter.validators.production_validator import ProductionValidator

    validator = ProductionValidator(dclgen_repository=DclgenRepository([]))
    text = """\n       EXEC SQL DECLARE C1 CURSOR FOR
         SELECT COL_A, COL_B FROM TABLE_A
       END-EXEC.
       EXEC SQL FETCH C1 INTO :DCLTAB.COL-A END-EXEC.
    """
    messages = validator.validate(text)
    assert any("cursor C1 selects 2 column(s) but FETCH binds 1" in m for m in messages)


def test_flags_sentence_terminator_inside_sqlcode_evaluate():
    source = """       EVALUATE SQLCODE
           WHEN OTHER
               MOVE 'SELECT-VMBEFF' TO SQL-LOCATION.
               PERFORM SQLERROR
       END-EVALUATE
       .
"""
    messages = CompilerSafetyValidator().validate(source)
    assert any("sentence-ending period inside EVALUATE SQLCODE" in m for m in messages)


def test_accepts_sqlcode_evaluate_with_period_after_scope_terminator():
    source = """       EVALUATE SQLCODE
           WHEN OTHER
               DISPLAY 'ERROR ON SELECT.'
               PERFORM SQLERROR
       END-EVALUATE
       .
"""
    messages = CompilerSafetyValidator().validate(source)
    assert not any("sentence-ending period inside EVALUATE SQLCODE" in m for m in messages)


def test_sql_terminator_inside_literal_does_not_close_block():
    source = """       EXEC SQL SELECT 'END-EXEC' FROM SYSIBM.SYSDUMMY1
       END-EXEC.
       EXEC SQL FETCH C1 INTO :DCLTAB.COL-A END-EXEC.
"""
    messages = CompilerSafetyValidator().validate(source)
    assert not any("END-EXEC without matching" in m for m in messages)
    assert not any("lack END-EXEC" in m for m in messages)


def test_sql_terminator_inside_sql_line_comment_does_not_close_block():
    source = """       EXEC SQL DECLARE C1 CURSOR FOR
         SELECT COL_A, COL_B FROM TABLE_A -- END-EXEC
       END-EXEC.
       EXEC SQL FETCH C1 INTO :DCLTAB.COL-A, :DCLTAB.COL-B END-EXEC.
"""
    messages = CompilerSafetyValidator().validate(source)
    assert not any("lack END-EXEC" in m for m in messages)
    assert not any("cursor C1 selects" in m for m in messages)


def test_sql_terminator_inside_multiline_block_comment_does_not_close_block():
    source = """       EXEC SQL DECLARE C1 CURSOR FOR
         SELECT COL_A, COL_B FROM TABLE_A /* fake END-EXEC
         still comment */
       END-EXEC.
       EXEC SQL FETCH C1 INTO :DCLTAB.COL-A, :DCLTAB.COL-B END-EXEC.
"""
    messages = CompilerSafetyValidator().validate(source)
    assert not any("lack END-EXEC" in m for m in messages)
    assert not any("END-EXEC without matching" in m for m in messages)
    assert not any("cursor C1 selects" in m for m in messages)


def test_fixed_format_comment_line_does_not_close_sql_block():
    source = """000100 EXEC SQL DECLARE C1 CURSOR FOR
000200* END-EXEC.
000300     SELECT COL_A FROM TABLE_A
000400 END-EXEC.
"""
    messages = CompilerSafetyValidator().validate(source)
    assert not any("END-EXEC without matching" in m for m in messages)
    assert not any("lack END-EXEC" in m for m in messages)
