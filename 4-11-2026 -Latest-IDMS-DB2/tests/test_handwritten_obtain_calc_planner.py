from converter.analyzers.lr_access.handwritten_obtain_calc_planner import HandwrittenObtainCalcPlanner
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver


def _planner():
    rows = [
        SheetMappingRow(
            cobol_record_idms="REC-A",
            cobol_zone="03 KEY-A",
            idms_key="CALC",
            idms_pic_clause="PIC X(4)",
            db2_key="Primary Key",
            new_db2_record="DZWCEFTB",
            new_db2_field_name="KEY_A",
            new_db2_data_type="CHAR (4)",
        ),
        SheetMappingRow(
            cobol_record_idms="REC-A",
            cobol_zone="03 DATA-A",
            idms_pic_clause="PIC X(10)",
            new_db2_record="DZWCEFTB",
            new_db2_field_name="DATA_A",
            new_db2_data_type="CHAR (10)",
        ),
    ]
    mapping = MappingRepository(rows)
    dclgen = DclgenRepository([
        DclgenColumn(table_name="DZWCEFTV", column_name="KEY_A", cobol_host_name="KEY-A"),
        DclgenColumn(table_name="DZWCEFTV", column_name="DATA_A", cobol_host_name="DATA-A"),
    ])
    table_resolver = TableNameResolver(mapping, dclgen)
    hosts = HostVariableResolver(dclgen, table_resolver)
    return HandwrittenObtainCalcPlanner(mapping, table_resolver, hosts)


def _source(key_move="MOVE INPUT-KEY TO KEY-A OF REC-A"):
    return f"""       PROCEDURE DIVISION.
       PROCESS-ROW.
           {key_move}
           OBTAIN CALC REC-A
           IF ERROR-STATUS NOT = '0000'
              DISPLAY 'REC-A ' REC-A
           END-IF
           IF ERROR-STATUS = '0000'
              OBTAIN FIRST CHILD-A WITHIN REC-A-CHILD-A
           END-IF.
"""


def test_plans_keyed_existence_read_when_all_key_and_status_proofs_exist():
    plans, diagnostics = _planner().plan(_source())
    assert "REC_A" in plans
    assert plans["REC_A"]["existence_column"] == "KEY_A"
    assert plans["REC_A"]["dclgen_group"] == "DCLDZWCEFTV"
    assert any("keyed existence SELECT is enabled" in item for item in diagnostics)


def test_refuses_when_any_key_is_not_assigned_before_access():
    plans, diagnostics = _planner().plan(_source("MOVE INPUT-KEY TO OTHER-FIELD OF REC-A"))
    assert plans == {}
    assert any("key fields are not all assigned" in item for item in diagnostics)


def test_refuses_conditional_key_assignment():
    source = _source().replace(
        "           MOVE INPUT-KEY TO KEY-A OF REC-A",
        "           IF INPUT-KEY NOT = SPACES\n              MOVE INPUT-KEY TO KEY-A OF REC-A\n           END-IF",
    )
    plans, diagnostics = _planner().plan(source)
    assert plans == {}
    assert any("inside conditional logic" in item for item in diagnostics)


def test_refuses_missing_zero_or_nonzero_status_guard():
    source = _source().replace("IF ERROR-STATUS = '0000'", "IF OTHER-FLAG = 'Y'")
    plans, diagnostics = _planner().plan(source)
    assert plans == {}
    assert any("zero ERROR-STATUS branch" in item for item in diagnostics)
