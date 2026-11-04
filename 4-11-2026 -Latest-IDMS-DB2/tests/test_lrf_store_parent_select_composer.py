from converter.composers.lrf_store_parent_select_composer import LrfStoreParentSelectComposer


class Mapping:
    def db2_table_for_record(self, record):
        assert record == "VMBEFF"
        return "DZBEFFTB"


class Dclgen:
    def column_names_for_table(self, table):
        return {
            "DZBEFFTV": ["CT_RKTPROD_479BEFF", "NR_IDSTOCK_479BEFF", "NR_CDSTK_479BEFF", "NS_DBSTK_479BEFF"],
            "DZEVEFTV": ["CT_RKTPROD_479BEFF", "NR_IDSTOCK_479BEFF", "NR_CDSTK_479BEFF", "NS_DBSTK_479BEFF", "NR_IDGOOD_479EVEF"],
        }[table]


class TableResolver:
    def resolve_table(self, table):
        return {"DZBEFFTB": "DZBEFFTV", "DZBEFFTV": "DZBEFFTV", "DZEVEFTV": "DZEVEFTV"}.get(table, "")


class Hosts:
    def host_reference_for_column(self, table, column):
        group = "DCLDZBEFFTV" if table == "DZBEFFTV" else "DCLDZEVEFTV"
        field = {
            "CT_RKTPROD_479BEFF": "CT-RKTPROD-479BEFF",
            "NR_IDSTOCK_479BEFF": "NR-IDSTOCK-479BEFF",
            "NR_CDSTK_479BEFF": "NR-CDSTK-479BEFF",
            "NS_DBSTK_479BEFF": "NS-DBSTK-479BEFF",
            "NR_IDGOOD_479EVEF": "NR-IDGOOD-479EVEF",
        }[column]
        return f":{group}.{field}"


class SqlGenerator:
    mapping_repository = Mapping()
    dclgen_repository = Dclgen()
    table_name_resolver = TableResolver()
    host_variable_resolver = Hosts()

    def select_by_key(self, record, *, for_lrf_parent=False):
        assert record == "VMBEFF"
        assert for_lrf_parent is True
        return [
            "EXEC SQL",
            " SELECT CT_RKTPROD_479BEFF",
            " INTO :DCLDZBEFFTV.CT-RKTPROD-479BEFF",
            " FROM DZBEFFTV",
            "END-EXEC",
            "EVALUATE SQLCODE",
            " WHEN 0 CONTINUE",
            " WHEN OTHER PERFORM SQLERROR",
            "END-EVALUATE",
            ".",
        ]


def test_lrf_store_generates_parent_select_and_gates_child_insert():
    source = "\n".join([
        "*DB2-LRF-STORE-PARENT: VMBEFF",
        "MOVE 'SELECT-VMBEFF' TO SQL-LOCATION.",
        "EXEC SQL",
        " INSERT INTO DZEVEFTV",
        " (CT_RKTPROD_479BEFF, NR_IDSTOCK_479BEFF, NR_CDSTK_479BEFF, NS_DBSTK_479BEFF, NR_IDGOOD_479EVEF)",
        " VALUES (:DCLDZEVEFTV.CT-RKTPROD-479BEFF, :DCLDZEVEFTV.NR-IDSTOCK-479BEFF, :DCLDZEVEFTV.NR-CDSTK-479BEFF, :DCLDZEVEFTV.NS-DBSTK-479BEFF, :DCLDZEVEFTV.NR-IDGOOD-479EVEF)",
        "END-EXEC",
        "EVALUATE SQLCODE",
        " WHEN 0 CONTINUE",
        " WHEN OTHER PERFORM SQLERROR",
        "END-EVALUATE",
        ".",
        "NEXT-PARAGRAPH.",
    ]) + "\n"

    composer = LrfStoreParentSelectComposer(sql_generator=SqlGenerator())
    result = composer.compose(source)

    assert "DB2-LRF-STORE-PARENT" not in result
    assert "FROM DZBEFFTV" in result
    assert result.index("MOVE 'SELECT-VMBEFF' TO SQL-LOCATION.") < result.index("EXEC SQL")
    assert result.index("MOVE 'SELECT-VMBEFF' TO SQL-LOCATION.") < result.index("IF SQLCODE = 0")
    assert "IF SQLCODE = 0" in result
    assert "MOVE DCLDZBEFFTV.CT-RKTPROD-479BEFF TO DCLDZEVEFTV.CT-RKTPROD-479BEFF" in result
    assert "MOVE DCLDZBEFFTV.NR-IDSTOCK-479BEFF TO DCLDZEVEFTV.NR-IDSTOCK-479BEFF" in result
    assert "INSERT INTO DZEVEFTV" in result
    assert result.index("MOVE 'INSERT-DZEVEFTV' TO SQL-LOCATION") < result.index("INSERT INTO DZEVEFTV")
    gated = result.split("IF SQLCODE = 0", 1)[1].split("END-IF.", 1)[0]
    assert not any(line.strip() == "." for line in gated.splitlines())
    assert not any(line.rstrip().endswith(".") for line in gated.splitlines() if line.strip().upper().startswith("MOVE "))
    assert "END-IF." in result
    assert "NEXT-PARAGRAPH." in result
