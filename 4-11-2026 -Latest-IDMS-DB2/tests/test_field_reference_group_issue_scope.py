from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.transformers.field_reference_context_builder import FieldReferenceContextBuilder


def test_group_decomposition_facts_are_stored_without_workbook_wide_warnings():
    rows = [
        SheetMappingRow(cobol_record_idms="REC-A", cobol_zone="02 KEY-GROUP", idms_pic_clause="GROUP"),
        SheetMappingRow(cobol_record_idms="REC-A", cobol_zone="03 KEY-PART-A", new_db2_record="TABLEATB", new_db2_field_name="COL_A", new_db2_data_type="CHAR(4)"),
        SheetMappingRow(cobol_record_idms="REC-A", cobol_zone="03 KEY-PART-B", new_db2_record="TABLEATB", new_db2_field_name="COL_B", new_db2_data_type="CHAR(2)"),
        SheetMappingRow(cobol_record_idms="REC-B", cobol_zone="02 OTHER-GROUP", idms_pic_clause="GROUP"),
        SheetMappingRow(cobol_record_idms="REC-B", cobol_zone="03 OTHER-A", new_db2_record="TABLEBTB", new_db2_field_name="COL_C", new_db2_data_type="CHAR(2)"),
        SheetMappingRow(cobol_record_idms="REC-B", cobol_zone="03 OTHER-B", new_db2_record="TABLEBTB", new_db2_field_name="COL_D", new_db2_data_type="CHAR(2)"),
    ]
    dclgen = DclgenRepository([
        DclgenColumn(table_name="TABLEATV", column_name="COL_A", cobol_host_name="COL-A"),
        DclgenColumn(table_name="TABLEATV", column_name="COL_B", cobol_host_name="COL-B"),
        DclgenColumn(table_name="TABLEBTV", column_name="COL_C", cobol_host_name="COL-C"),
        DclgenColumn(table_name="TABLEBTV", column_name="COL_D", cobol_host_name="COL-D"),
    ])
    mapping = MappingRepository(rows)
    table_resolver = TableNameResolver(mapping, dclgen)
    host_resolver = HostVariableResolver(dclgen, table_resolver)
    builder = FieldReferenceContextBuilder(
        mapping_repository=mapping,
        table_name_resolver=table_resolver,
        host_variable_resolver=host_resolver,
    )
    builder.build_reference_maps()

    assert builder.messages == []
    assert "KEY-GROUP" in builder.group_issues["REC_A"]
    assert "OTHER-GROUP" in builder.group_issues["REC_B"]
