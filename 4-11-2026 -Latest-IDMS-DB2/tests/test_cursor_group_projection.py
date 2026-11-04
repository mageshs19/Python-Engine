from types import SimpleNamespace

from converter.analyzers.field_usage_models import FieldUsage, FieldUsageAnalysis
from converter.resolvers.cursor_field_usage_column_selector import (
    CursorFieldUsageColumnSelector,
)


class _Mapping:
    def rows_for_record(self, record_name):
        assert record_name == "VMBEVEF"
        return [
            SimpleNamespace(cobol_zone="03 NR-ID-GOOD", new_db2_field_name="NR_IDGOOD_479EVEF"),
            SimpleNamespace(cobol_zone="02 DB-NR-CI", new_db2_field_name=""),
            SimpleNamespace(cobol_zone="03 NR-CI", new_db2_field_name=""),
            SimpleNamespace(cobol_zone="04 NR-CI-1-POS", new_db2_field_name="NR_CI1POS_479EVEF"),
            SimpleNamespace(cobol_zone="04 NR-CI-2-6-POS", new_db2_field_name="NR_CI26POS_479EVEF"),
            SimpleNamespace(cobol_zone="03 DA-CREA-VTPD", new_db2_field_name="DA_CREVTPD_479EVEF"),
        ]


def test_group_field_usage_expands_to_mapped_descendant_columns():
    analysis = FieldUsageAnalysis(
        usage_by_record={
            "VMBEVEF": FieldUsage(
                record_name="VMBEVEF",
                all_fields={"NR-CI", "NR-ID-GOOD", "DA-CREA-VTPD"},
            )
        }
    )

    columns = CursorFieldUsageColumnSelector(_Mapping()).columns_from_field_usage(
        "VMBEVEF", analysis
    )

    assert "NR_CI1POS_479EVEF" in columns
    assert "NR_CI26POS_479EVEF" in columns
    assert "NR_IDGOOD_479EVEF" in columns
    assert "DA_CREVTPD_479EVEF" in columns
    assert len(columns) == len(set(columns))


def test_group_expansion_stops_at_next_sibling_level():
    selector = CursorFieldUsageColumnSelector(_Mapping())

    columns = selector.columns_for_group_field(
        record_name="VMBEVEF",
        source_group_field="NR-CI",
    )

    assert columns == ["NR_CI1POS_479EVEF", "NR_CI26POS_479EVEF"]
