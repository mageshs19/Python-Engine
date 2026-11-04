from types import SimpleNamespace

from converter.generators.db2_infrastructure.spec_builder.cursor_spec_builder import (
    CursorSpecBuilder,
)


def fixed(body, indicator=" "):
    return f"000100{indicator}{body:<65}00010000"


class Mapping:
    def __init__(self, rows):
        self.rows = rows

    def rows_for_record(self, record):
        assert record == "VMBEVEF"
        return self.rows


def _builder(mapping):
    builder = CursorSpecBuilder.__new__(CursorSpecBuilder)
    builder.owner = SimpleNamespace(mapping_repository=mapping)
    builder.messages = []
    return builder


def _source():
    return "\n".join([
        fixed(
            "DB2: Expanded LRF FIRST VMBTL07-R01 WHERE "
            "ALL-VMBEVEF-BY-VMBEFF",
            "*",
        ),
        fixed("-> VMBEVEF WITHIN VMBEFF-VMBEVEF.", "*"),
        fixed(
            "DB2: LRF ALL-VMBEVEF-BY-VMBEFF extra filter: "
            "CT-RK-TEVPR = '0168'",
            "*",
        ),
        fixed(
            "AND CT-RK-TGDSV = '0219' - add to the generated cursor WHERE.",
            "*",
        ),
        fixed("OBTAIN FIRST VMBEVEF WITHIN VMBEFF-VMBEVEF."),
    ])


def test_actual_modular_cursor_spec_builder_adds_both_vmdz1526_path_filters():
    mapping = Mapping([
        SimpleNamespace(
            cobol_zone="03 CT-RK-TEVPR",
            reference_field_name_copybook="",
            new_db2_field_name="CT_RKTEVPR_479EVEF",
            cross_application_db2_field_name="",
        ),
        SimpleNamespace(
            cobol_zone="04 CT-RK-TGDSV",
            reference_field_name_copybook="",
            new_db2_field_name="CT_RKTGDSV_479EVEF",
            cross_application_db2_field_name="",
        ),
    ])
    builder = _builder(mapping)
    specs = [{
        "record_name": "VMBEVEF",
        "where_conditions": [
            "CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF",
            "NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF",
        ],
    }]

    builder._apply_lrf_extra_filters(specs, _source())

    where = specs[0]["where_conditions"]
    assert "CT_RKTEVPR_479EVEF = '0168'" in where
    assert "CT_RKTGDSV_479EVEF = '0219'" in where
    assert len(where) == 4


def test_lrf_extra_filter_mapping_failure_fails_closed_in_real_spec_path():
    builder = _builder(Mapping([]))
    specs = [{"record_name": "VMBEVEF", "where_conditions": ["PARENT_ID = :DCLP.ID"]}]

    builder._apply_lrf_extra_filters(specs, _source())

    assert "1 = 0" in specs[0]["where_conditions"]
    assert any("could not be mapped unambiguously" in message for message in builder.messages)


def test_lrf_scanner_uses_expanded_source_when_transformed_output_drops_markers():
    from converter.generators.db2_infrastructure.spec_builder.spec_build_context import (
        SpecBuildContext,
    )
    from converter.generators.db2_infrastructure.spec_builder.spec_lrf_scanner import (
        SpecLrfScanner,
    )
    from converter.generators.db2_infrastructure.spec_builder.spec_navigation_scanner import (
        SpecNavigationScanner,
    )

    transformed = "000100 WORKING-STORAGE SECTION.                                      00010000"
    context = SpecBuildContext.create(
        operations=[],
        cobol_text=transformed,
        field_usage_analysis=object(),
        navigation=SpecNavigationScanner(),
        lrf=SpecLrfScanner(),
        lrf_source_text=_source(),
    )

    assert "VMBEVEF" in context.lrf_cursors
    assert "VMBEVEF" not in SpecLrfScanner().cursors(transformed)
