from types import SimpleNamespace

from converter.composers.record_materialisation.record_entry_renderer import (
    RecordEntryRenderer,
)


def test_record_layout_preserves_comp3_and_does_not_add_value_zeroes():
    field = SimpleNamespace(
        picture="PIC S9(3)V9(3)",
        usage="COMP-3",
        is_redefinition=False,
        redefines="",
    )

    assert RecordEntryRenderer.record_picture_of(field) == "PIC S9(3)V9(3) COMP-3"


def test_record_layout_preserves_numeric_display_without_value_clause():
    field = SimpleNamespace(
        picture="PIC 9(8)",
        usage="",
        is_redefinition=False,
        redefines="",
    )

    assert RecordEntryRenderer.record_picture_of(field) == "PIC 9(8)"


def test_existing_work_field_normalization_is_unchanged():
    field = SimpleNamespace(
        picture="PIC 9(8)",
        usage="COMP-3",
        is_redefinition=False,
        redefines="",
    )

    assert RecordEntryRenderer.picture_of(field) == "PIC 9(8) VALUE ZEROES"


def test_record_layout_generator_uses_storage_preserving_picture_renderer():
    from converter.composers.record_materialisation.record_field import RecordFieldPlan
    from converter.composers.record_materialisation.record_layout_generator import RecordLayoutGenerator
    from converter.composers.record_materialisation.record_plan import RecordMaterialisationPlan

    plan = RecordMaterialisationPlan(
        record_name="REC",
        fields=[
            RecordFieldPlan(
                level="05",
                name="AMOUNT",
                picture="PIC S9(3)V9(3)",
                usage="COMP-3",
                declared_bytes=4,
            )
        ],
    )
    rendered = "\n".join(RecordLayoutGenerator().generate(plan))
    assert "PIC S9(3)V9(3) COMP-3" in rendered
    assert "VALUE ZEROES" not in rendered
