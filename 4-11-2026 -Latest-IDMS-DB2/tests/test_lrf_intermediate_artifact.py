"""The LRF-to-ordinary-IDMS stage is persisted as an inspectable artifact."""
from pathlib import Path

from converter.domain.models import ConversionInput
from converter.pipeline.conversion.conversion_pipeline import ConversionPipeline


def test_lrf_intermediate_is_written_to_configured_directory(monkeypatch, tmp_path):
    monkeypatch.setenv("IDMS_DB2_LRF_INTERMEDIATE_DIR", str(tmp_path / "LRF"))
    monkeypatch.delenv("DUMP_EXPANDED", raising=False)
    source = "IDENTIFICATION DIVISION.\nPROGRAM-ID. VMDZ1526.\nOBTAIN FIRST VMBEVEF.\n"
    conversion_input = ConversionInput(
        idms_cobol_text=source,
        target_program_id="VMDZ1526",
    )

    ConversionPipeline._dump_expanded(conversion_input, source)

    artifact = tmp_path / "LRF" / "VMDZ1526_lrf_to_idms.cbl"
    assert artifact.is_file()
    assert artifact.read_text(encoding="utf-8") == source


def test_lrf_intermediate_sanitizes_program_id(monkeypatch, tmp_path):
    monkeypatch.setenv("IDMS_DB2_LRF_INTERMEDIATE_DIR", str(tmp_path))
    monkeypatch.delenv("DUMP_EXPANDED", raising=False)
    conversion_input = ConversionInput(target_program_id="BAD/PROGRAM:ID")

    ConversionPipeline._dump_expanded(conversion_input, "normalized")

    assert (tmp_path / "BAD_PROGRAM_ID_lrf_to_idms.cbl").read_text() == "normalized"


def test_default_intermediate_folder_is_mainframe_output_lrf(monkeypatch):
    """Guard the agreed output location when no override is configured."""
    import converter.pipeline.conversion.conversion_pipeline as module

    monkeypatch.delenv("IDMS_DB2_LRF_INTERMEDIATE_DIR", raising=False)
    monkeypatch.delenv("DUMP_EXPANDED", raising=False)
    root = Path(module.__file__).resolve().parents[3]
    expected = root / "mainframe" / "workspace" / "Output" / "LRF"
    assert expected.name == "LRF"
    assert expected.parent.name == "Output"
