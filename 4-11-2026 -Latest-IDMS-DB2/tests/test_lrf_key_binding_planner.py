from converter.analyzers.lr_access.lrf_key_binding_planner import LrfKeyBindingPlanner
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver


def _planner():
    rows = [
        SheetMappingRow(cobol_record_idms="VMBEFF", cobol_zone="04 CT-RK-TPROD", idms_key="CALC", idms_pic_clause="PIC X(4)", db2_key="Primary Key", new_db2_record="DZBEFFTB", new_db2_field_name="CT_RKTPROD_479BEFF", new_db2_data_type="CHAR (4)"),
        SheetMappingRow(cobol_record_idms="VMBEFF", cobol_zone="06 NR-ID-STOCK-CD", idms_key="CALC", idms_pic_clause="GROUP"),
        SheetMappingRow(cobol_record_idms="VMBEFF", cobol_zone="07 NR-ID-STOCK-R1", idms_key="CALC", idms_pic_clause="GROUP", db2_key="Primary Key", new_db2_record="DZBEFFTB", new_db2_field_name="NR_IDSTOCK_479BEFF", new_db2_data_type="CHAR (12)"),
        SheetMappingRow(cobol_record_idms="VMBEFF", cobol_zone="07 NR-CD-STOCK", idms_key="CALC", idms_pic_clause="PIC 9", length_of_field_bytes="1", db2_key="Primary Key", new_db2_record="DZBEFFTB", new_db2_field_name="NR_CDSTK_479BEFF", new_db2_data_type="DECIMAL (1)"),
        SheetMappingRow(cobol_record_idms="VMBEFF", cobol_zone="03 NS-DB-STOCK", idms_key="CALC", idms_pic_clause="PIC 9(2)", length_of_field_bytes="2", db2_key="Primary Key", new_db2_record="DZBEFFTB", new_db2_field_name="NS_DBSTK_479BEFF", new_db2_data_type="DECIMAL (2)"),
        *[
            SheetMappingRow(cobol_record_idms="VMBEVEF", cobol_zone="", db2_key="Foreign Key", new_db2_record="DZEVEFTB", new_db2_field_name=column, new_db2_data_type=dtype)
            for column, dtype in [
                ("CT_RKTPROD_479BEFF", "CHAR (4)"),
                ("NR_IDSTOCK_479BEFF", "CHAR (12)"),
                ("NR_CDSTK_479BEFF", "DECIMAL (1)"),
                ("NS_DBSTK_479BEFF", "DECIMAL (2)"),
            ]
        ],
    ]
    columns = []
    for table, fields in {
        "DZBEFFTV": ["CT_RKTPROD_479BEFF", "NR_IDSTOCK_479BEFF", "NR_CDSTK_479BEFF", "NS_DBSTK_479BEFF"],
        "DZEVEFTV": ["CT_RKTPROD_479BEFF", "NR_IDSTOCK_479BEFF", "NR_CDSTK_479BEFF", "NS_DBSTK_479BEFF"],
    }.items():
        columns.extend(DclgenColumn(table_name=table, column_name=field, cobol_host_name=field.replace("_", "-")) for field in fields)
    mapping = MappingRepository(rows)
    dclgen = DclgenRepository(columns)
    table_resolver = TableNameResolver(mapping, dclgen)
    host_resolver = HostVariableResolver(dclgen, table_resolver)
    return LrfKeyBindingPlanner(mapping, dclgen, table_resolver, host_resolver)


def test_composite_calc_group_splits_only_when_widths_are_proven():
    planner = _planner()
    source = """
       03 WS-IN-NR-TIT-BC PIC X(13).
       MOVE WS-IN-NR-TIT-BC TO NR-ID-STOCK-CD OF VMBEFF.
    """
    moves, diagnostics, required = planner.plan_parent_input(source, "VMBEFF")
    assert required is True
    assert diagnostics == []
    assert "MOVE WS-IN-NR-TIT-BC(1:12) TO NR-IDSTOCK-479BEFF OF DCLDZBEFFTV." in moves
    assert not any(item.startswith("IF ") for item in moves)
    assert any("MOVE WS-IN-NR-TIT-BC(13:1) TO NR-CDSTK-479BEFF OF DCLDZBEFFTV." == item for item in moves)


def test_ambiguous_or_missing_composite_source_fails_closed():
    planner = _planner()
    moves, diagnostics, required = planner.plan_parent_input("MOVE SPACES TO KY-EFFECT OF VMBEFF.", "VMBEFF")
    assert required is True
    assert moves == []
    assert any("keyed SELECT refused" in item for item in diagnostics)




def test_composite_calc_key_uses_copybook_width_when_input_field_is_not_inline():
    from converter.domain.models import CopybookField
    from converter.repositories.copybook_repository import CopybookRepository

    base = _planner()
    planner = LrfKeyBindingPlanner(
        mapping_repository=base.mapping,
        dclgen_repository=base.dclgen,
        table_name_resolver=base.table_resolver,
        host_variable_resolver=base.hosts,
        copybook_repository=CopybookRepository([
            CopybookField(level="05", name="NR-ST-FORM-AS", picture="X(13)")
        ]),
    )
    source = """
       COPY VMDZ205I.
       MOVE NR-ST-FORM-AS OF VMDZ205I TO NR-ID-STOCK-CD OF VMBEFF.
       OBTAIN CALC VMBEFF.
    """
    moves, diagnostics, required = planner.plan_parent_input(source, "VMBEFF")
    assert required is True
    assert diagnostics == []
    assert moves == [
        "MOVE NR-ST-FORM-AS(1:12) TO NR-IDSTOCK-479BEFF OF DCLDZBEFFTV.",
        "MOVE NR-ST-FORM-AS(13:1) TO NR-CDSTK-479BEFF OF DCLDZBEFFTV.",
    ]
