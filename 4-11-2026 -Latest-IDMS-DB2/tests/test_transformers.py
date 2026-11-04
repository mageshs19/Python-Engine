from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.generators.sql_error_generator import SqlErrorGenerator
from converter.generators.sql_generator import SqlGenerator
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.transformers.cobol_transformer import CobolTransformer
from converter.transformers.field_reference_rewriter import FieldReferenceRewriter
from converter.transformers.idms_statement_transformer import (
    IdmsStatementTransformer,
)


def build_transformer_context():
    mapping_repository = MappingRepository(
        [
            SheetMappingRow(
                cobol_record_idms="VMB-FAR",
                cobol_zone="NR-ID",
                idms_key="CALC",
                db2_key="PRIMARY KEY",
                new_db2_record="DZBFARTB",
                new_db2_field_name="NR_ID",
            ),
            SheetMappingRow(
                cobol_record_idms="VMB-FAR",
                cobol_zone="CD-NAME",
                new_db2_record="DZBFARTB",
                new_db2_field_name="CD_NAME",
            ),
        ]
    )

    dclgen_repository = DclgenRepository(
        [
            DclgenColumn(
                table_name="DZBFARTV",
                column_name="NR_ID",
                cobol_host_name="NR-ID",
            ),
            DclgenColumn(
                table_name="DZBFARTV",
                column_name="CD_NAME",
                cobol_host_name="CD-NAME",
            ),
        ]
    )

    table_resolver = TableNameResolver(
        mapping_repository=mapping_repository,
        dclgen_repository=dclgen_repository,
    )

    column_resolver = ColumnNameResolver(
        mapping_repository=mapping_repository,
        dclgen_repository=dclgen_repository,
        table_name_resolver=table_resolver,
    )

    host_resolver = HostVariableResolver(
        dclgen_repository=dclgen_repository,
        table_name_resolver=table_resolver,
    )

    cursor_resolver = CursorNameResolver()

    sql_generator = SqlGenerator(
        mapping_repository=mapping_repository,
        dclgen_repository=dclgen_repository,
        table_name_resolver=table_resolver,
        column_name_resolver=column_resolver,
        host_variable_resolver=host_resolver,
    )

    statement_transformer = IdmsStatementTransformer(
        sql_generator=sql_generator,
        sql_error_generator=SqlErrorGenerator(),
        table_name_resolver=table_resolver,
        cursor_name_resolver=cursor_resolver,
    )

    return {
        "mapping_repository": mapping_repository,
        "dclgen_repository": dclgen_repository,
        "table_resolver": table_resolver,
        "host_resolver": host_resolver,
        "statement_transformer": statement_transformer,
    }


def test_idms_statement_transformer_converts_obtain_calc():
    context = build_transformer_context()

    lines, _opened_set = context["statement_transformer"].transform_line(
        line="OBTAIN VMB-FAR CALC.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )

    text = "\n".join(lines)

    assert "Removed OBTAIN CALC SELECT" in text
    assert "Direct UPDATE will use mapped composite key WHERE clause" in text
    assert "CONTINUE." in text


def test_idms_statement_transformer_converts_store_to_insert_or_skips_safely():
    context = build_transformer_context()

    lines, _opened_set = context["statement_transformer"].transform_line(
        line="STORE VMB-FAR.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )

    text = "\n".join(lines)

    assert (
        "Converted STORE" in text
        or "INSERT conversion skipped" in text
    )

    assert (
        "INSERT INTO DZBFARTV" in text
        or "missing insert columns" in text
        or "Missing Sheet Mapping or DCLGEN" in text
    )


def test_idms_statement_transformer_removes_bind():
    context = build_transformer_context()

    lines, _opened_set = context["statement_transformer"].transform_line(
        line="BIND RUN-UNIT.",
        current_division="PROCEDURE",
        sql_error_paragraph="SQL-ERROR",
    )

    text = "\n".join(lines)

    assert "Removed IDMS BIND statement" in text
    assert "CONTINUE." in text


def test_cobol_transformer_converts_program_id_and_idms_statement():
    context = build_transformer_context()

    transformer = CobolTransformer(
        idms_statement_transformer=context["statement_transformer"],
    )

    source = """
IDENTIFICATION DIVISION.
PROGRAM-ID. OLDPROG.
PROCEDURE DIVISION.
OBTAIN VMB-FAR CALC.
END PROGRAM OLDPROG.
"""

    converted, messages, operations = transformer.transform(
        cobol_text=source,
        target_program_id="NEWPROG",
    )

    assert "PROGRAM-ID. NEWPROG." in converted
    assert "Removed OBTAIN CALC SELECT" in converted
    assert "Direct UPDATE will use mapped composite key WHERE clause" in converted
    assert len(operations) == 1

    # CORRECTION - this asserted `messages == []`, an exact-list match.
    #
    # The test source carries no CBL line, so the transformer now inserts
    # CBL ARITH(EXTEND) and reports it. That diagnostic is correct and
    # required: CHK-04.01 fails without the compiler option, and every
    # hand-written reference program in Manual Output begins with it.
    #
    # The intent of the original assertion was "no UNEXPECTED diagnostic",
    # so that is what is asserted now. An exact-list match on diagnostics
    # breaks whenever any unrelated pass gains a message, which is a
    # maintenance tax with no safety benefit.
    assert any("Compiler option:" in m for m in messages), messages
    assert [m for m in messages if "Compiler option:" not in m] == []

def test_field_reference_rewriter_rewrites_qualified_reference():
    context = build_transformer_context()

    rewriter = FieldReferenceRewriter(
        mapping_repository=context["mapping_repository"],
        table_name_resolver=context["table_resolver"],
        host_variable_resolver=context["host_resolver"],
    )

    result = rewriter.rewrite("MOVE NR-ID OF VMB-FAR TO WS-NR-ID.")

    assert "NR-ID OF DCLDZBFARTV" in result
    assert "VMB-FAR" not in result



def test_cobol_transformer_never_converts_fixed_format_commented_store():
    """Commented subschema STORE examples must not become executable INSERTs."""
    context = build_transformer_context()
    transformer = CobolTransformer(
        idms_statement_transformer=context["statement_transformer"],
    )
    source = "\n".join([
        "000100 IDENTIFICATION DIVISION.",
        "000200 PROGRAM-ID. COMMENTEDST.",
        "000300 PROCEDURE DIVISION.",
        "000400*STORE VMBEVEF.",
        "000500*=      STORE VMBEVEF",
        "000600 END PROGRAM COMMENTEDST.",
    ]) + "\n"

    converted, _messages, _operations = transformer.transform(
        cobol_text=source,
        target_program_id="COMMENTEDST",
    )

    assert "000400*STORE VMBEVEF." in converted
    assert "000500*=      STORE VMBEVEF" in converted
    assert "INSERT INTO DZEVEFTV" not in converted


def test_cobol_transformer_preserves_idms_abort_cleanup_paragraph():
    """IDMS-specific status copy may go, but valid COBOL cleanup must survive."""
    context = build_transformer_context()
    transformer = CobolTransformer(
        idms_statement_transformer=context["statement_transformer"],
    )
    source = "\n".join([
        "IDENTIFICATION DIVISION.",
        "PROGRAM-ID. ABORTCLEAN.",
        "PROCEDURE DIVISION.",
        "EINDE-PROGRAMMA.",
        "    CLOSE FORM.",
        "IDMS-ABORT.",
        "    CLOSE FORM.",
        "    COPY IDMS IDMS-STATUS.",
        "AFTER-ABORT.",
        "    CONTINUE.",
        "END PROGRAM ABORTCLEAN.",
    ]) + "\n"

    converted, _messages, _operations = transformer.transform(
        cobol_text=source,
        target_program_id="ABORTCLEAN",
    )

    assert "IDMS-ABORT." not in converted
    assert "ABORT-CLEANUP." in converted
    assert converted.count("CLOSE FORM.") == 2
    assert "Removed residual IDMS control statement: COPY IDMS IDMS-STATUS." in converted
    assert converted.index("ABORT-CLEANUP.") < converted.index("AFTER-ABORT.")


def test_empty_idms_abort_paragraph_is_removed_generically():
    context = build_transformer_context()
    transformer = CobolTransformer(
        idms_statement_transformer=context["statement_transformer"],
    )
    source = "\n".join([
        "IDENTIFICATION DIVISION.",
        "PROGRAM-ID. EMPTYABT.",
        "PROCEDURE DIVISION.",
        "BEFORE-ABORT.",
        "    CONTINUE.",
        "IDMS-ABORT.",
        "    EXIT.",
        "AFTER-ABORT.",
        "    CONTINUE.",
        "END PROGRAM EMPTYABT.",
    ]) + "\n"

    converted, _messages, _operations = transformer.transform(
        cobol_text=source,
        target_program_id="EMPTYABT",
    )

    assert "IDMS-ABORT." not in converted
    assert "ABORT-CLEANUP." not in converted
    assert "AFTER-ABORT." in converted
    assert converted.index("BEFORE-ABORT.") < converted.index("AFTER-ABORT.")


def test_idms_abort_paragraph_with_real_cleanup_is_preserved():
    context = build_transformer_context()
    transformer = CobolTransformer(
        idms_statement_transformer=context["statement_transformer"],
    )
    source = "\n".join([
        "IDENTIFICATION DIVISION.",
        "PROGRAM-ID. CLEANABT.",
        "PROCEDURE DIVISION.",
        "IDMS-ABORT.",
        "    CLOSE FORM.",
        "AFTER-ABORT.",
        "    CONTINUE.",
        "END PROGRAM CLEANABT.",
    ]) + "\n"

    converted, _messages, _operations = transformer.transform(
        cobol_text=source,
        target_program_id="CLEANABT",
    )

    assert "IDMS-ABORT." not in converted
    assert "ABORT-CLEANUP." in converted
    assert "CLOSE FORM." in converted
    assert "AFTER-ABORT." in converted


def test_referenced_empty_idms_abort_paragraph_is_preserved():
    context = build_transformer_context()
    transformer = CobolTransformer(
        idms_statement_transformer=context["statement_transformer"],
    )
    source = "\n".join([
        "IDENTIFICATION DIVISION.",
        "PROGRAM-ID. REFABT.",
        "PROCEDURE DIVISION.",
        "    GO TO IDMS-ABORT.",
        "IDMS-ABORT.",
        "    EXIT.",
        "AFTER-ABORT.",
        "    CONTINUE.",
        "END PROGRAM REFABT.",
    ]) + "\n"

    converted, _messages, _operations = transformer.transform(
        cobol_text=source,
        target_program_id="REFABT",
    )

    assert "GO TO ABORT-CLEANUP" in converted
    assert "IDMS-ABORT." not in converted
    assert "ABORT-CLEANUP." in converted
