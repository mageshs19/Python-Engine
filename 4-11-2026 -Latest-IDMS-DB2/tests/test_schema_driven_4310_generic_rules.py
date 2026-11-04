"""Production-oriented generic COBOL conversion rules; no program names or fixed business fields."""
from pathlib import Path

from converter.domain.models import DclgenColumn, CopybookField
from converter.repositories.copybook_repository import CopybookRepository
from converter.parsers.copybook_parser import CopybookParser
from converter.composers.schema_date_transfer_composer import SchemaDateTransferComposer
from converter.composers.schema_numeric_key_guard import SchemaNumericKeyGuard
from converter.services.final_generated_output_service import FinalGeneratedOutputService
from converter.composers.paragraph_entry_display_composer import _is_paragraph


def test_date_conversion_uses_dclgen_type_and_copybook_width_with_renamed_business_fields():
    cols=[DclgenColumn(table_name="DZTSTTV", cobol_host_name="DT-EVENT-500", db2_type="DATE NOT NULL", cobol_picture="X(10).")]
    repo=CopybookRepository([CopybookField(level="05",name="DT-ARCH-RESULT",picture="9(8)")])
    text=("000100 WORKING-STORAGE SECTION.\n"
          "000200 01  WS-VAR PIC X.\n"
          "000300 PROCEDURE DIVISION.\n"
          "000400 MAIN.\n"
          "000500     MOVE DT-EVENT-500 OF DCLDZTSTTV TO\n"
          "000600          DT-ARCH-RESULT OF TARGET-REC.\n")
    rule=SchemaDateTransferComposer(cols,repo)
    result=rule.compose(text)
    assert len(rule.messages)==1
    assert "MOVE DT-EVENT-500 OF DCLDZTSTTV TO DA-DD-MM-CCYY" in result
    assert "MOVE DA-CCYYMMDD-R TO DT-ARCH-RESULT OF TARGET-REC" in result
    assert "WHEN DA-DD-MM-CCYY = '01.01.0001'" in result
    assert "01 WS-DATUMVELDEN." in result or "01  WS-DATUMVELDEN." in result
    assert rule.compose(result)==result


def test_date_conversion_refuses_unproven_schema_and_ten_byte_destinations():
    cols=[DclgenColumn(table_name="DZTSTTV",cobol_host_name="DT-EVENT-500",db2_type="CHAR(10)",cobol_picture="X(10)")]
    repo=CopybookRepository([CopybookField(level="05",name="DT-ARCH-RESULT",picture="9(8)")])
    text="PROCEDURE DIVISION.\nMOVE DT-EVENT-500 OF DCLDZTSTTV TO DT-ARCH-RESULT OF TARGET-REC.\n"
    assert SchemaDateTransferComposer(cols,repo).compose(text)==text
    cols[0].db2_type="DATE"
    repo=CopybookRepository([CopybookField(level="05",name="DT-ARCH-RESULT",picture="X(10)")])
    assert SchemaDateTransferComposer(cols,repo).compose(text)==text


def test_copybook_redefines_filler_does_not_expand_storage_size():
    copybook="""01 REC.
 05 DATUM.
  10 D-YYYY PIC X(4).
  10 D-MM PIC XX.
  10 D-DD PIC XX.
 05 FILLER REDEFINES DATUM.
  10 DATE-NUM PIC 9(8).
 05 TRAILER PIC X.
"""
    repo=CopybookRepository(CopybookParser().parse(copybook))
    assert repo.group_width_for("DATUM")==8
    assert repo.group_width_for("REC")==9


def test_numeric_refmod_guard_is_proven_by_input_and_dclgen_not_names():
    cols=[DclgenColumn(table_name="DZXYTV",cobol_host_name="NU-CODE",db2_type="SMALLINT",cobol_picture="S9(1)V",cobol_usage="COMP-3")]
    src="""000100 WORKING-STORAGE SECTION.
000200 03 WS-INPUT PIC X(13).
000300 PROCEDURE DIVISION.
000400      MOVE WS-INPUT(13:1) TO
000500         NU-CODE OF DCLDZXYTV.
000600      PERFORM SQLERROR.
"""
    composer=SchemaNumericKeyGuard(cols)
    out=composer.compose(src)
    assert "IF WS-INPUT(13:1) IS NUMERIC" in out
    assert "MOVE WS-INPUT(13:1) TO NU-CODE OF DCLDZXYTV" in out
    assert "NON-NUMERIC DB2 KEY COMPONENT" in out
    assert composer.compose(out)==out


def test_numeric_guard_refuses_non_numeric_dclgen_dest_and_unproven_abort_policy():
    cols=[DclgenColumn(table_name="DZXYTV",cobol_host_name="NU-CODE",db2_type="CHAR",cobol_picture="X(1)")]
    src="""000100 03 WS-INPUT PIC X(13).
000200 PROCEDURE DIVISION.
000300 MOVE WS-INPUT(13:1) TO NU-CODE OF DCLDZXYTV.
000400 PERFORM SQLERROR.
"""
    assert SchemaNumericKeyGuard(cols).compose(src)==src
    cols[0].cobol_picture="9(1)"
    assert SchemaNumericKeyGuard(cols).compose(src.replace("PERFORM SQLERROR.","CONTINUE.") )==src.replace("PERFORM SQLERROR.","CONTINUE.")


def test_fixed_area_a_scope_terminator_is_not_a_paragraph():
    assert not _is_paragraph("000100 END-IF.                         00000100")
    assert not _is_paragraph("000100 END-EVALUATE.                   00000100")
    assert _is_paragraph("000100 " + "SEARCH-MUTATIES.".ljust(65) + "00000100")


def test_sql_location_uses_source_proven_query_number_without_undefined_identifier():
    src="""000100 PROCEDURE DIVISION.
000200 SEARCH-MUTATIES.
000300 EXEC SQL
000400 SELECT A INTO :Z FROM T
000500 QUERYNO 234
000600 END-EXEC.
"""
    result=FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql(src)
    assert "MOVE 234 TO SQL-LOCATION" in result
    assert "SQL-STATEMENT" not in result


def test_no_named_program_parity_override_remains():
    source=(Path(__file__).resolve().parents[1] / 'converter/composers/manual_storage_parity_composer.py').read_text()
    assert '_normalize_vmdz4310_manual_parity' not in source
    assert 'VMDZ4310' not in source


def test_symbolic_location_before_singleton_sql_becomes_queryno_without_field_name_patch():
    text="""000100 PROCEDURE DIVISION.
000200 SEARCH-SOMETHING.
000300 MOVE 'SELECT-SOMETHING' TO SQL-LOCATION.
000400 EXEC SQL
000500 SELECT VALUE INTO :H FROM TABLE_A
000600 QUERYNO 314
000700 END-EXEC.
"""
    output=FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql(text)
    assert "MOVE 314 TO SQL-LOCATION." in output
    assert "SELECT-SOMETHING" not in output
    assert "SQL-STATEMENT" not in output


def test_sql_body_area_b_alignment_is_generic_and_token_preserving():
    from converter.composers.sql_body_area_b_normalizer import SqlBodyAreaBNormalizer
    def fixed(n,s):return f'{n:06d} '+s.ljust(65)+f'{n*100:08d}'
    src='\n'.join([
       fixed(100,'PROCEDURE DIVISION.'),
       fixed(200,'    EXEC SQL'),
       fixed(300,'   SELECT A'),
       fixed(400,'   FROM T'),
       fixed(500,'    END-EXEC'),
    ])+'\n'
    r=SqlBodyAreaBNormalizer();out=r.compose(src)
    assert out.splitlines()[2][7:72].startswith('    SELECT A')
    assert out.splitlines()[3][7:72].startswith('    FROM T')
    assert all(len(line)==80 for line in out.splitlines())
    assert r.compose(out)==out
