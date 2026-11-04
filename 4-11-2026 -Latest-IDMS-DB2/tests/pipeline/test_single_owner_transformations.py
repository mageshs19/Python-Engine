from __future__ import annotations

import ast
from pathlib import Path

from converter.composers.paragraph_entry_display_composer import ParagraphEntryDisplayComposer

ROOT = Path(__file__).resolve().parents[2]


def _call_counts(path: Path, method_name: str, stage_names: set[str]) -> dict[str, int]:
    tree = ast.parse(path.read_text(encoding="utf-8-sig"))
    counts = {name: 0 for name in stage_names}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not isinstance(func, ast.Attribute) or func.attr != method_name:
            continue
        if not node.args or not isinstance(node.args[0], ast.Constant):
            continue
        value = node.args[0].value
        if value in counts:
            counts[value] += 1
    return counts


def test_mutating_pipeline_stages_have_one_call_site_each():
    steps = ROOT / "converter/pipeline/conversion/conversion_pipeline_steps.py"
    pipeline = ROOT / "converter/pipeline/conversion/conversion_pipeline.py"
    counts = _call_counts(steps, "_stage", {"cursor_order_cleanup"})
    counts.update(_call_counts(pipeline, "_stage", {"update_restart_skip", "guarantee_cursor_close"}))
    assert counts == {
        "cursor_order_cleanup": 1,
        "guarantee_cursor_close": 1,
        "update_restart_skip": 1,
    }


def test_cursor_lifecycle_has_one_mutating_owner_in_production_pipeline():
    steps = (ROOT / "converter/pipeline/conversion/conversion_pipeline_steps.py").read_text(encoding="utf-8-sig")
    factory_path = ROOT / "converter/pipeline/conversion/conversion_component_factory.py"
    factory = factory_path.read_text(encoding="utf-8-sig")
    assert 'composers["cursor_flow"]' not in steps
    assert '"cursor_flow": CursorFlowComposer()' not in factory
    assert not (ROOT / "converter/composers/cursor_flow_composer.py").exists()
    assert '"cursor_close_guarantee": CursorCloseGuaranteeComposer()' in factory


def test_nonmatching_debug_display_is_preserved_and_entry_display_is_added():
    source = "\n".join([
        "000010 PROCEDURE DIVISION.".ljust(80),
        "000020 DO-WORK.".ljust(80),
        "000030D    DISPLAY 'BUSINESS DIAGNOSTIC'.".ljust(80),
        "000040     GOBACK.".ljust(80),
    ]) + "\n"
    output = ParagraphEntryDisplayComposer().compose(source)
    assert "DISPLAY 'DO-WORK.'." in output
    assert "DISPLAY 'BUSINESS DIAGNOSTIC'." in output


def test_vmdz4420_nested_cursor_flow_is_not_rewritten_twice():
    from converter.composers.cursor_close_guarantee_composer import CursorCloseGuaranteeComposer
    from converter.composers.lifecycle_standardization_composer import LifecycleStandardizationComposer

    fixture = ROOT / "tests/fixtures/VMDZ4420_nested_cursor_control_flow.cbl"
    source = fixture.read_text(encoding="utf-8", errors="replace")
    lifecycle = LifecycleStandardizationComposer()
    after_lifecycle = lifecycle.compose(source)
    composer = CursorCloseGuaranteeComposer()
    output = composer.compose(after_lifecycle)

    # Both parent and child loops already own their row-processing boundary.
    # The shared lifecycle planner must recognize this and avoid adding a
    # second PERFORM edge or moving the child's loop outside the parent.
    assert after_lifecycle == source
    assert output == source
    assert sum("PERFORM 2100-OPEN-DZBEFFC1" in line for line in output.splitlines()) == 1
    assert sum("PERFORM 2300-CLOSE-DZBEFFC1" in line for line in output.splitlines()) == 1
    assert sum("PERFORM 3100-OPEN-DZEVEFC1" in line for line in output.splitlines()) == 1
    assert sum("PERFORM 3300-CLOSE-DZEVEFC1" in line for line in output.splitlines()) == 1
    assert any("already driven by an external SPAN loop" in msg for msg in composer.messages)


def test_external_business_loop_removes_existing_fetch_to_business_edge():
    from converter.composers.cursor_close_guarantee_composer import (
        CursorCloseGuaranteeComposer,
    )

    source = "\n".join([
        "000010 PROCEDURE DIVISION.".ljust(80),
        "000020 MAIN-PROCEDURE.".ljust(80),
        "000030     PERFORM 2100-OPEN-DZBEFFC1.".ljust(80),
        "000040     PERFORM 2200-FETCH-DZBEFFC1.".ljust(80),
        "000050     PERFORM VERWERK-EFFEKT UNTIL ERROR-STATUS NOT = '0000'.".ljust(80),
        "000060     PERFORM 2300-CLOSE-DZBEFFC1.".ljust(80),
        "000070 VERWERK-EFFEKT.".ljust(80),
        "000080     PERFORM 3100-OPEN-DZEVEFC1.".ljust(80),
        "000090     PERFORM 3200-FETCH-DZEVEFC1.".ljust(80),
        "000100     PERFORM NEXT-VMBEVEF UNTIL DZEVEFC1-EOC.".ljust(80),
        "000110     PERFORM 3300-CLOSE-DZEVEFC1.".ljust(80),
        "000120     PERFORM 2200-FETCH-DZBEFFC1.".ljust(80),
        "000130 NEXT-VMBEVEF.".ljust(80),
        "000140     DISPLAY 'DCLDZEVEFTV' ".ljust(80),
        "000150     PERFORM 3200-FETCH-DZEVEFC1.".ljust(80),
        "000160 2100-OPEN-DZBEFFC1.".ljust(80),
        "000170     CONTINUE.".ljust(80),
        "000180 2200-FETCH-DZBEFFC1.".ljust(80),
        "000190     EXEC SQL FETCH DZBEFFC1 END-EXEC.".ljust(80),
        "000200     EVALUATE SQLCODE".ljust(80),
        "000210       WHEN ZERO".ljust(80),
        "000220            PERFORM VERWERK-EFFEKT".ljust(80),
        "000230       WHEN 100 SET DZBEFFC1-EOC TO TRUE".ljust(80),
        "000240     END-EVALUATE.".ljust(80),
        "000250 2300-CLOSE-DZBEFFC1.".ljust(80),
        "000260     CONTINUE.".ljust(80),
        "000270 3100-OPEN-DZEVEFC1.".ljust(80),
        "000280     CONTINUE.".ljust(80),
        "000290 3200-FETCH-DZEVEFC1.".ljust(80),
        "000300     EXEC SQL FETCH DZEVEFC1 END-EXEC.".ljust(80),
        "000310     EVALUATE SQLCODE".ljust(80),
        "000320       WHEN ZERO".ljust(80),
        "000330            PERFORM NEXT-VMBEVEF".ljust(80),
        "000340       WHEN 100 SET DZEVEFC1-EOC TO TRUE".ljust(80),
        "000350     END-EVALUATE.".ljust(80),
        "000360 3300-CLOSE-DZEVEFC1.".ljust(80),
        "000370     CONTINUE.".ljust(80),
    ]) + "\n"

    composer = CursorCloseGuaranteeComposer()
    output = composer.compose(source)
    from converter.composers.cursor_guarantee.cursor_lines import CursorLines
    lines = [CursorLines().logical(line).upper() for line in output.splitlines()]

    assert any(line.startswith("PERFORM VERWERK-EFFEKT UNTIL DZBEFFC1-EOC") for line in lines)
    assert sum(line.startswith("PERFORM VERWERK-EFFEKT") for line in lines) == 1
    assert any(line.startswith("PERFORM NEXT-VMBEVEF UNTIL DZEVEFC1-EOC") for line in lines)
    assert sum(line.startswith("PERFORM NEXT-VMBEVEF") for line in lines) == 1
    assert any("duplicate_fetch_business_edge_removed" in msg for msg in composer.messages)
    assert any("rewrote the DZBEFFC1 loop exit condition" in msg for msg in composer.messages)


def test_business_resolver_skips_exit_paragraphs_before_cursor_business_body():
    from converter.composers.cursor_guarantee.business_paragraph_resolver import (
        BusinessParagraphResolver,
    )
    from converter.composers.cursor_guarantee.cursor_models import CursorParagraphSet

    lines = [
        "000010 PROCEDURE DIVISION.".ljust(80),
        "000020 BEGIN-PROGRAMMA.".ljust(80),
        "000030     PERFORM 2100-OPEN-DZBFASC1.".ljust(80),
        "000040 BEGIN-PROGRAMMA-EXIT.".ljust(80),
        "000050     EXIT.".ljust(80),
        "000060 BEHANDELING.".ljust(80),
        "000070     DISPLAY 'DCLDZBFASV'.".ljust(80),
        "000080     PERFORM 2200-FETCH-DZBFASC1.".ljust(80),
        "000090 2100-OPEN-DZBFASC1.".ljust(80),
        "000100     CONTINUE.".ljust(80),
        "000110 2200-FETCH-DZBFASC1.".ljust(80),
        "000120     EXEC SQL FETCH DZBFASC1 INTO :DCLDZBFASV.FIELD END-EXEC.".ljust(80),
        "000130 2300-CLOSE-DZBFASC1.".ljust(80),
        "000140     CONTINUE.".ljust(80),
    ]
    cursor_set = CursorParagraphSet(
        cursor="DZBFASC1",
        names={"OPEN": "2100-OPEN-DZBFASC1", "FETCH": "2200-FETCH-DZBFASC1", "CLOSE": "2300-CLOSE-DZBFASC1"},
    )
    assert BusinessParagraphResolver().resolve(lines, cursor_set) == "BEHANDELING"


def test_cursor_numbering_composer_changes_only_cursor_labels_not_business_flow():
    from converter.composers.cursor_paragraph_numbering_composer import (
        CursorParagraphNumberingComposer,
    )

    source = "\n".join([
        "PROCEDURE DIVISION.",
        "           PERFORM BEGIN-PROGRAMMA THRU BEGIN-PROGRAMMA-EXIT.",
        "           PERFORM 2110-OPEN-C1.",
        "           PERFORM 2120-FETCH-C1.",
        "           PERFORM BEHANDELING THRU BEHANDELING-EXIT UNTIL C1-EOC.",
        "           PERFORM 2130-CLOSE-C1.",
        "           GOBACK.",
        "BEGIN-PROGRAMMA.",
        "           CONTINUE.",
        "BEGIN-PROGRAMMA-EXIT.",
        "           EXIT.",
        "BEHANDELING.",
        "           PERFORM 2120-FETCH-C1.",
        "BEHANDELING-EXIT.",
        "           EXIT.",
        "2110-OPEN-C1.",
        "           MOVE 2110 TO SQL-LOCATION.",
        "           EXEC SQL OPEN C1 END-EXEC.",
        "2120-FETCH-C1.",
        "           MOVE 2120 TO SQL-LOCATION.",
        "           EXEC SQL FETCH C1 INTO :HV END-EXEC.",
        "2130-CLOSE-C1.",
        "           MOVE 2130 TO SQL-LOCATION.",
        "           EXEC SQL CLOSE C1 END-EXEC.",
    ]) + "\n"

    output = CursorParagraphNumberingComposer().compose(source)
    assert "0000-MAIN-PROCEDURE." not in output
    assert "1000-INITIALIZE-PROGRAM." not in output
    assert "2000-PROCESS-PROGRAM." not in output
    assert "3000-FINALIZE-PROGRAM." not in output
    assert "PERFORM BEGIN-PROGRAMMA THRU BEGIN-PROGRAMMA-EXIT." in output
    assert "PERFORM BEHANDELING THRU BEHANDELING-EXIT UNTIL C1-EOC." in output
    assert "PERFORM 2100-OPEN-C1." in output
    assert "PERFORM 2200-FETCH-C1." in output
    assert "PERFORM 2300-CLOSE-C1." in output
    assert "2200-FETCH-C1." in output
    assert "MOVE 2100 TO SQL-LOCATION." in output
    assert "MOVE 2200 TO SQL-LOCATION." in output
    assert "MOVE 2300 TO SQL-LOCATION." in output
