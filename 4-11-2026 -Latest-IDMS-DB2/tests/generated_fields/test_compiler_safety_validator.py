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
