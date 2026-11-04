"""Program-flow diagnostics must use the shared DB2 table resolver."""

from converter.analyzers.program_flow.program_flow_analyzer import ProgramFlowAnalyzer
from converter.domain.models import IdmsOperation


class FakeTableResolver:
    def table_for_record(self, record_name: str) -> str:
        return {"VMBEVEF": "DZBEVEFTV"}.get(record_name, "")


def test_flow_analyzer_resolves_record_to_db2_table_and_uses_table_cursor_name():
    analyzer = ProgramFlowAnalyzer(table_name_resolver=FakeTableResolver())

    result = analyzer.analyze(
        cobol_text="PROCEDURE DIVISION.\nMAIN-LOGIC.\n    CONTINUE.\n",
        operations=[
            IdmsOperation(
                operation="OBTAIN_FIRST",
                record_name="VMBEVEF",
                set_name="VMBEFF-VMBEVEF",
                line_number=10,
            )
        ],
    )

    assert len(result.cursor_loops) == 1
    loop = result.cursor_loops[0]
    assert loop.record_name == "VMBEVEF"
    assert loop.table_name == "DZBEVEFTV"
    assert loop.cursor_name != ""
    assert not any("no table resolver" in item.lower() for item in result.diagnostics)


def test_flow_analyzer_reports_missing_table_mapping_without_inventing_one():
    analyzer = ProgramFlowAnalyzer(table_name_resolver=FakeTableResolver())

    result = analyzer.analyze(
        cobol_text="PROCEDURE DIVISION.\nMAIN-LOGIC.\n    CONTINUE.\n",
        operations=[IdmsOperation(operation="OBTAIN_FIRST", record_name="UNKNOWN-REC")],
    )

    assert result.cursor_loops[0].table_name == ""
    assert any("UNKNOWN-REC" in item for item in result.diagnostics)
