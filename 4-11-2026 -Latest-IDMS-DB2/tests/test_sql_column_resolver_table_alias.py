from converter.generators.sql.sql_column_resolver import SqlColumnResolver


class MappingRepository:
    def __init__(self):
        self.requested_table = None

    def db2_table_for_record(self, record_name):
        assert record_name == "VMBEVEF"
        return "DZEVEFTB"

    def db2_columns_for_table(self, table_name):
        self.requested_table = table_name
        if table_name == "DZEVEFTB":
            return ["NR_ID_479EVEF", "NR_IDGOOD_479EVEF", "TS_CREATE_479EVEF", "TS_UPDATE_479EVEF", "ID_USERID_479EVEF"]
        return []


class DclgenRepository:
    def column_names_for_table(self, table_name):
        assert table_name == "DZEVEFTV"
        return ["NR_ID_479EVEF", "NR_IDGOOD_479EVEF", "TS_CREATE_479EVEF", "TS_UPDATE_479EVEF", "ID_USERID_479EVEF"]


class TableNameResolver:
    def resolve_table(self, table_name):
        return {"DZEVEFTB": "DZEVEFTV", "DZEVEFTV": "DZEVEFTV"}.get(table_name, "")


def test_insert_columns_use_sheet_mapping_base_table_and_dclgen_alias():
    mapping = MappingRepository()
    resolver = SqlColumnResolver(
        mapping_repository=mapping,
        dclgen_repository=DclgenRepository(),
        table_name_resolver=TableNameResolver(),
    )

    columns = resolver.insert_columns_for_record("VMBEVEF", "DZEVEFTV")

    assert mapping.requested_table == "DZEVEFTB"
    assert "NR_ID_479EVEF" in columns
    assert "NR_IDGOOD_479EVEF" in columns
    assert "TS_CREATE_479EVEF" in columns
    assert "TS_UPDATE_479EVEF" in columns
    assert "ID_USERID_479EVEF" in columns
