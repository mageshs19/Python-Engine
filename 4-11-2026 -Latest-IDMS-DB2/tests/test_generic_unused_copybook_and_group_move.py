"""Generic safety contracts for data-dependent COPYs and composite MOVEs."""
from __future__ import annotations

from pathlib import Path

from converter.composers.unused_copybook_pruner import UnusedCopybookPruner
from converter.domain.models import CopybookField
from converter.repositories.copybook_repository import CopybookRepository
from converter.composers.lrf_group_move_decomposer import LrfGroupMoveDecomposer


def fixed(body: str) -> str:
    return f"000100 {body:<65}00010000\n"


def test_prune_derived_copy_only_when_all_source_fields_are_dead():
    source = fixed("01 VMBD77-R01.") + fixed("05 SOURCE-ONLY PIC X(4).")
    program = (fixed("WORKING-STORAGE SECTION.") + fixed("COPY VMDZ77.")
               + fixed("01 OTHER-FIELD PIC X(4).") + fixed("PROCEDURE DIVISION.")
               + fixed("DISPLAY OTHER-FIELD.") + fixed("GOBACK."))
    pruner = UnusedCopybookPruner({"VMBD77": source})
    result = pruner.apply(program)
    assert "COPY VMDZ77." not in result
    assert "DISPLAY OTHER-FIELD" in result
    assert pruner.apply(result) == result


def test_keep_live_and_unknown_copybook_and_comments():
    source = fixed("01 VMBD77-R01.") + fixed("05 SOURCE-ONLY PIC X(4).")
    for statement in ("DISPLAY SOURCE-ONLY.", "MOVE ZERO TO VMBD77-R01."):
        program = (fixed("WORKING-STORAGE SECTION.") + fixed("COPY VMDZ77.")
                   + fixed("PROCEDURE DIVISION.") + fixed(statement))
        assert "COPY VMDZ77." in UnusedCopybookPruner({"VMBD77": source}).apply(program)
    assert "COPY VMDZ77." in UnusedCopybookPruner({}).apply(program)
    assert "COPY VMDZ77." in UnusedCopybookPruner({"VMBD77": fixed("COPY ANOTHER.")}).apply(program)
    assert "COPY VMDZ77." in UnusedCopybookPruner({"VMBD77": source}).apply(
        fixed("WORKING-STORAGE SECTION.") + "000100*COPY VMDZ77.\n"
    )


def test_generic_typed_children_require_exact_width_match():
    fields = [
        CopybookField(level="15", name="NUMERIC-ALIAS", redefines="NUMERIC-BODY"),
        CopybookField(level="20", name="TWELVE-CHAR-GROUP"),
        CopybookField(level="25", name="PART-A", picture="X(12)"),
        CopybookField(level="20", name="SINGLE-DIGIT", picture="9"),
    ]
    copybooks = CopybookRepository(fields)
    # _width_matched_children only depends on parsed copybook metadata.
    decomposer = object.__new__(LrfGroupMoveDecomposer)
    decomposer.copybooks = copybooks
    assert decomposer._width_matched_children("NUMERIC-ALIAS", [12, 1]) == [
        "TWELVE-CHAR-GROUP", "SINGLE-DIGIT"
    ]
    assert decomposer._width_matched_children("NUMERIC-ALIAS", [11, 2]) == []


def test_real_source_copybook_is_unused_in_generated_layout():
    root = Path(__file__).resolve().parents[1]
    src = root / "mainframe/workspace/Copybook/VMBD05.cpy"
    generated = next((root / "mainframe/workspace/Output").glob("VMDZ4310*.cbl"))
    output = UnusedCopybookPruner({"VMBD05": src.read_text(encoding="utf-8")}).apply(
        generated.read_text(encoding="utf-8")
    )
    assert "COPY VMDZ05." not in output
