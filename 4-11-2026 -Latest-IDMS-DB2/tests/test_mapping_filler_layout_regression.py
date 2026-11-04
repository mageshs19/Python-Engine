"""Regression: mapping-defined FILLER rows must survive record expansion."""

from pathlib import Path

from converter.composers.record_materialisation.record_layout_generator import (
    RecordLayoutGenerator,
)
from converter.composers.record_materialisation.record_plan import (
    RecordMaterialisationPlan,
)
from converter.composers.record_materialisation.record_row_reader import (
    RecordRowReader,
)
from converter.parsers.sheet_mapping_parser import SheetMappingParser


PROJECT_ROOT = Path(__file__).resolve().parents[1]
from tests.workspace_fixtures import mapping_export
MAPPING_PATH = mapping_export()


def _mapped_vmbfas_x14_filler():
    rows = SheetMappingParser().parse_csv_text(
        MAPPING_PATH.read_text(encoding="utf-8-sig")
    )
    row = next(
        row
        for row in rows
        if row.cobol_record_idms.strip().upper() == "VMBFAS"
        and " ".join(row.cobol_zone.split()).upper() == "02 FILLER"
        and row.idms_pic_clause.strip().upper() == "PIC X(0014)"
    )
    return RecordRowReader().read(row)


def test_mapping_filler_x14_is_emitted_in_vmbfas_expansion():
    field = _mapped_vmbfas_x14_filler()
    assert field is not None
    assert field.name == "FILLER"
    assert field.picture == "PIC X(0014)"
    assert field.declared_bytes == 14
    assert field.is_declarable
    assert not field.is_movable

    plan = RecordMaterialisationPlan(record_name="VMBFAS", fields=[field])
    generated = RecordLayoutGenerator().generate(
        plan,
        base_level=5,
        base_indent="     ",
    )
    generated_text = "\n".join(generated)

    assert "07  FILLER" in generated_text
    assert "PIC X(0014)" in generated_text
    assert plan.total_bytes == 14


def test_explicit_mapping_filler_is_not_suppressed_with_remainder_filler_disabled():
    from rules.record_materialisation_rules import EMIT_REMAINDER_FILLER

    # The synthetic tail is optional; an explicit Sheet Mapping field is not.
    assert EMIT_REMAINDER_FILLER is True
    field = _mapped_vmbfas_x14_filler()
    plan = RecordMaterialisationPlan(record_name="VMBFAS", fields=[field])
    assert len(plan.filler_fields) == 1
    assert len(plan.declarable_fields) == 1


def test_full_sheet_mapping_preserves_original_record_byte_length():
    """The sheet's 432-byte prefix must fit its 478-byte target exactly."""
    from converter.composers.record_materialisation.record_field import RecordFieldPlan
    from converter.composers.record_materialisation.record_materialisation_guard import RecordMaterialisationGuard

    rows = SheetMappingParser().parse_csv_text(MAPPING_PATH.read_text(encoding="utf-8-sig"))
    reader = RecordRowReader()
    fields = [reader.read(row) for row in rows if row.cobol_record_idms.strip().upper() == "VMBFAS"]
    plan = RecordMaterialisationPlan(record_name="VMBFAS", fields=[field for field in fields if field])
    assert plan.total_bytes == 432
    assert plan.remainder_bytes(478) == 46
    assert RecordMaterialisationGuard.check_length(plan, "F-FORM", 478) is None
    # The filler belongs beside, not inside, the mapped record group.
    lines = RecordLayoutGenerator().remainder_line(level=6, byte_count=plan.remainder_bytes(478), base_indent="    ")
    assert len(lines) == 1
    assert "06" in lines[0]
    assert "PIC X(0046)" in lines[0]
    assert plan.total_bytes + plan.remainder_bytes(478) == 478
    # No padding for exact fit; never silently truncate an overflowing layout.
    assert plan.remainder_bytes(432) == 0
    assert RecordLayoutGenerator().remainder_line(level=6, byte_count=0) == []
    assert RecordMaterialisationGuard.check_length(plan, "F-FORM", 400).key == "skipped_too_long"
    assert RecordMaterialisationGuard.check_length(plan, "F-FORM", 0).key == "skipped_no_declared_length"


def test_filler_rendering_respects_fixed_format_columns():
    from converter.composers.record_materialisation.record_block_writer import RecordBlockWriter
    from converter.composers.record_materialisation.record_layout_generator import RecordLayoutGenerator
    from converter.composers.record_materialisation.record_move_generator import RecordMoveGenerator
    from converter.composers.record_materialisation.record_line_utils import RecordLineUtils
    from converter.composers.record_materialisation.record_field import RecordFieldPlan

    plan = RecordMaterialisationPlan(record_name="SAMPLE", fields=[RecordFieldPlan(level="02", name="ONE-FIELD", picture="PIC X(13)", declared_bytes=13)])
    writer = RecordBlockWriter(layout_generator=RecordLayoutGenerator(), move_generator=RecordMoveGenerator())
    base = "000100     05  SAMPLE-AREA        PIC X(36).".ljust(72) + "00010000"
    produced = writer.expand_target([base], 0, "SAMPLE-AREA", plan, target_level=5, declared_bytes=36)
    filler = [line for line in produced if "FILLER" in line and "PIC X(" in line]
    assert len(filler) == 1
    assert "06  FILLER" in filler[0]
    assert "PIC X(0023)" in filler[0]
    assert all(len(line[:72]) == 72 for line in filler)
    assert filler[0][6] == " "
    assert 11 <= filler[0].index("06", 7) < 72
