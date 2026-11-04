from types import SimpleNamespace

from converter.resolvers.cursor_column_resolver import CursorColumnResolver


class _Mapping:
    def rows_for_record(self, record_name):
        assert record_name == "VMBFAS"
        return [
            SimpleNamespace(
                cobol_zone="09 NR-CIO-FORM-AS",
                reference_field_name_copybook="",
                new_db2_field_name="NR_CIOFMAS_479BFAS",
                cross_application_db2_field_name="",
            ),
            SimpleNamespace(
                cobol_zone="",
                reference_field_name_copybook="",
                new_db2_field_name="NR_CIOFMAS_479SIAS",
                cross_application_db2_field_name="",
                relation="Foreign Key",
            ),
        ]


class _ColumnNameResolver:
    @staticmethod
    def columns_for_record(record_name):
        assert record_name == "VMBFAS"
        return ["NR_CIOFMAS_479BFAS", "NR_CIOFMAS_479SIAS"]


class _Unused:
    pass


def test_materialised_projection_excludes_relationship_only_columns_without_source_field():
    resolver = CursorColumnResolver.__new__(CursorColumnResolver)
    resolver.mapping_repository = _Mapping()
    resolver.column_name_resolver = _ColumnNameResolver()

    assert resolver._materialised_record_columns("VMBFAS") == [
        "NR_CIOFMAS_479BFAS"
    ]


def test_materialised_projection_falls_back_when_mapping_has_no_field_provenance():
    resolver = CursorColumnResolver.__new__(CursorColumnResolver)
    resolver.mapping_repository = SimpleNamespace(
        rows_for_record=lambda _record: [
            SimpleNamespace(
                cobol_zone="",
                reference_field_name_copybook="",
                new_db2_field_name="NR_CIOFMAS_479SIAS",
                cross_application_db2_field_name="",
            )
        ]
    )
    resolver.column_name_resolver = _ColumnNameResolver()

    assert resolver._materialised_record_columns("VMBFAS") == [
        "NR_CIOFMAS_479BFAS",
        "NR_CIOFMAS_479SIAS",
    ]
