from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "converter/pipeline/conversion/conversion_pipeline.py"


def test_source_proven_sql_lowering_is_part_of_standard_two_stage_path():
    source = PIPELINE.read_text(encoding="utf-8")
    assert "self._expand_logical_records(" in source
    assert "Source-proven SQL lowering is part of the ordinary IDMS -> DB2 stage" in source
    assert "BoundedLrfSingletonRewriter().rewrite(" in source
    assert "original_idms_text=source_text" in source
    assert "correctness must not depend on an opt-in environment setting" in source


def test_lrf_normalization_still_precedes_db2_transform():
    source = PIPELINE.read_text(encoding="utf-8")
    normalize = source.index("self._expand_logical_records(")
    transform = source.index('transformers[\n            "cobol"\n        ].transform(', normalize)
    lower = source.index("BoundedLrfSingletonRewriter().rewrite(", transform)
    assert normalize < transform < lower


def test_lrf_marker_probe_only_flags_access_markers_not_update_markers():
    from patterns.cursor_spec.lrf_comment_patterns import LRF_ACCESS_MARKER_PROBE

    assert LRF_ACCESS_MARKER_PROBE.search(
        "*DB2: Expanded LRF FIRST VMBTL07-R01 WHERE ALL-VMBEVEF-BY-VMBEFF"
    )
    assert not LRF_ACCESS_MARKER_PROBE.search(
        "*DB2: Expanded LRF MODIFY VMBTL07-R01 WHERE MO-VMBEVEF"
    )
    assert not LRF_ACCESS_MARKER_PROBE.search(
        "*DB2: Expanded LRF STORE VMBTL07-R01 WHERE ST-VMBEVEF"
    )
