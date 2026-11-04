from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.generators.sql.sql_column_resolver import SqlColumnResolver
from converter.generators.sql.sql_line_builder import SqlLineBuilder
from converter.generators.sql.sql_statement_builder import SqlStatementBuilder
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver


def _builder(rows, columns):
    mapping = MappingRepository(rows)
    dclgen = DclgenRepository(columns)
    table_resolver = TableNameResolver(mapping, dclgen)
    column_resolver = SqlColumnResolver(mapping, dclgen, table_resolver)
    hosts = HostVariableResolver(dclgen, table_resolver)
    line_builder = SqlLineBuilder(hosts)
    return SqlStatementBuilder(
        column_resolver=column_resolver,
        line_builder=line_builder,
        date_builder=None,
        host_variable_resolver=hosts,
        mapping_repository=mapping,
        update_plan_resolver=None,
    )


def test_insert_sequence_is_inferred_from_mapping_not_program_or_table_literals():
    rows = [
        SheetMappingRow(
            cobol_record_idms="ORDER",
            new_db2_record="ORDERTB",
            new_db2_field_name="ORDER_ID",
            new_db2_data_type="DECIMAL (12)",
            db2_key="Primary Key",
            remarks="auto increment sequence key",
        ),
        SheetMappingRow(
            cobol_record_idms="ORDER",
            cobol_zone="  05 ORDER-DESCRIPTION",
            new_db2_record="ORDERTB",
            new_db2_field_name="ORDER_DESCRIPTION",
            new_db2_data_type="CHAR(30)",
        ),
    ]
    dclgen_columns = [
        DclgenColumn(
            table_name="ORDERTV", column_name="ORDER_ID", db2_type="DECIMAL(12,0)",
            cobol_host_name="ORDER-ID", cobol_picture="S9(12)", nullable=False,
        ),
        DclgenColumn(
            table_name="ORDERTV", column_name="ORDER_DESCRIPTION", db2_type="CHAR(30)",
            cobol_host_name="ORDER-DESCRIPTION", cobol_picture="X(30)", nullable=False,
        ),
    ]

    sql = "\n".join(_builder(rows, dclgen_columns).insert("ORDER"))

    assert "INSERT INTO ORDERTV" in sql
    assert "RIGHT(DIGITS(NEXT VALUE FOR ORDERSQ), 12)" in sql
    assert ":DCLORDERTV.ORDER-ID" not in sql
    assert ":DCLORDERTV.ORDER-DESCRIPTION" in sql


def test_sequence_key_without_supported_sequence_convention_fails_closed():
    rows = [
        SheetMappingRow(
            cobol_record_idms="ORDER",
            new_db2_record="ORDERTABLE",
            new_db2_field_name="ORDER_ID",
            new_db2_data_type="DECIMAL (12)",
            db2_key="Primary Key",
            remarks="auto increment sequence key",
        ),
    ]
    dclgen_columns = [
        DclgenColumn(
            table_name="ORDERTABLE", column_name="ORDER_ID", db2_type="DECIMAL(12,0)",
            cobol_host_name="ORDER-ID", cobol_picture="S9(12)", nullable=False,
        ),
    ]
    sql = "\n".join(_builder(rows, dclgen_columns).insert("ORDER"))

    assert "INSERT INTO ORDERTV" not in sql
    assert "sequence-key metadata" in sql
    assert "CONTINUE." in sql
