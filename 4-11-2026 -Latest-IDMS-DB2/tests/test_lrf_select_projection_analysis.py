"""Source-driven projection tests for generic LRF keyed parent SELECTs."""
from converter.pipeline.conversion.conversion_pipeline_steps import ConversionPipelineSteps


def test_lrf_projection_uses_only_mapped_fields_referenced_after_keyed_read(
    transformer_context,
):
    mapping = transformer_context["mapping_repository"]
    source = """
       MOVE INPUT-ID TO NR-ID OF VMB-FAR.
       OBTAIN CALC VMB-FAR.
       MOVE CD-NAME OF VMB-FAR TO WS-NAME.
       DISPLAY NR-ID OF VMB-FAR.
    """

    columns = ConversionPipelineSteps._source_proven_lrf_select_columns(
        source, mapping, "VMB-FAR"
    )

    assert columns == ["NR_ID", "CD_NAME"]


def test_lrf_projection_ignores_fields_used_only_before_keyed_read(
    transformer_context,
):
    mapping = transformer_context["mapping_repository"]
    source = """
       MOVE INPUT-ID TO NR-ID OF VMB-FAR.
       DISPLAY CD-NAME OF VMB-FAR.
       OBTAIN CALC VMB-FAR.
       MOVE CD-NAME OF VMB-FAR TO WS-NAME.
    """

    columns = ConversionPipelineSteps._source_proven_lrf_select_columns(
        source, mapping, "VMB-FAR"
    )

    assert columns == ["CD_NAME"]


def test_keyed_select_projection_and_into_are_aligned(transformer_context):
    generator = transformer_context["statement_transformer"].sql_generator
    sql = generator.select_by_key(
        "VMB-FAR", for_lrf_parent=True, required_columns=["CD_NAME"]
    )
    text = "\n".join(sql).upper()

    assert "SELECT" in text
    assert "CD_NAME" in text
    assert "NR_ID," not in text
    assert ":DCLDZBFARTV.CD-NAME" in text
    into_clause = text.split("INTO", 1)[1].split("FROM DZBFARTV", 1)[0]
    assert ":DCLDZBFARTV.NR-ID" not in into_clause
    assert ":DCLDZBFARTV.CD-NAME" in into_clause
    assert text.count("CD_NAME") == 1


def test_empty_source_proven_projection_fails_closed(transformer_context):
    generator = transformer_context["statement_transformer"].sql_generator
    sql = generator.select_by_key(
        "VMB-FAR", for_lrf_parent=True, required_columns=[]
    )
    text = "\n".join(sql).upper()

    assert "EXEC SQL" not in text
    assert "CONTINUE" in text or "RETAIN" in text or "MISSING" in text


def test_group_move_includes_mapped_descendants_but_diagnostic_display_does_not():
    from converter.domain.models import SheetMappingRow
    from converter.repositories.mapping_repository import MappingRepository

    mapping = MappingRepository(
        [
            SheetMappingRow(
                cobol_record_idms="REC",
                cobol_zone="02 GROUP-A",
                new_db2_record="T_REC",
            ),
            SheetMappingRow(
                cobol_record_idms="REC",
                cobol_zone="03 FIELD-A",
                new_db2_record="T_REC",
                new_db2_field_name="FIELD_A",
            ),
            SheetMappingRow(
                cobol_record_idms="REC",
                cobol_zone="03 FIELD-B",
                new_db2_record="T_REC",
                new_db2_field_name="FIELD_B",
            ),
        ]
    )

    moved_group = ConversionPipelineSteps._source_proven_lrf_select_columns(
        "OBTAIN CALC REC.\nMOVE GROUP-A OF REC TO WS-GROUP.", mapping, "REC"
    )
    displayed_group = ConversionPipelineSteps._source_proven_lrf_select_columns(
        "OBTAIN CALC REC.\nDISPLAY GROUP-A OF REC.", mapping, "REC"
    )

    assert moved_group == ["FIELD_A", "FIELD_B"]
    assert displayed_group == []


def test_vmdz4310_projection_is_derived_from_real_mapping_and_expanded_source():
    from pathlib import Path

    from converter.parsers.sheet_mapping_parser import SheetMappingParser
    from converter.repositories.mapping_repository import MappingRepository

    root = Path(__file__).resolve().parents[1]
    from tests.workspace_fixtures import mapping_export, expanded_program
    mapping_path = mapping_export()
    source_path = expanded_program("VMDZ4310")

    class _UploadedMapping:
        name = mapping_path.name

        def getvalue(self):
            return mapping_path.read_bytes()

    mapping_rows = SheetMappingParser().parse_uploaded_file(_UploadedMapping())
    columns = ConversionPipelineSteps._source_proven_lrf_select_columns(
        source_path.read_text(encoding="utf-8", errors="replace"),
        MappingRepository(mapping_rows),
        "VMBEFF",
    )

    assert len(columns) == 12
    assert "AM_CNDSTK_479BEFF" in columns
    assert "CT_RKTPRDX_479BEFF" not in columns
    assert "NX_CPFDUSK_479BEFF" not in columns
    assert "NR_CDSTK_479BEFF" not in columns
