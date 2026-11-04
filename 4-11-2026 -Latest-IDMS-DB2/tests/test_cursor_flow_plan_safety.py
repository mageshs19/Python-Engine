from converter.composers.cursor_flow_plan_discoverer import CursorFlowPlanDiscoverer
from converter.composers.cursor_flow_rewriter import CursorFlowRewriter


def _simple_flow(cursor, open_no, fetch_no, close_no, business):
    return [
        f"PERFORM {open_no}-OPEN-{cursor}.",
        f"PERFORM {fetch_no}-FETCH-{cursor}.",
        f"PERFORM {business}.",
        f"UNTIL {cursor}-EOC.",
        f"PERFORM {close_no}-CLOSE-{cursor}.",
    ]


def test_simple_cursor_plan_uses_actual_operation_numbers_and_close_location():
    lines = _simple_flow("C1", 710, 720, 730, "PROCESS-C1")
    discoverer = CursorFlowPlanDiscoverer()
    plans = discoverer.discover(lines)
    assert len(plans) == 1
    assert plans[0].fetch_number == 720
    assert plans[0].close_number == 730
    assert plans[0].close_index == 4


def test_rewriter_does_not_leave_duplicate_original_close_call():
    lines = _simple_flow("C1", 710, 720, 730, "PROCESS-C1")
    discoverer = CursorFlowPlanDiscoverer()
    plans = discoverer.discover(lines)
    rewritten = CursorFlowRewriter().rewrite_main_flow(lines, plans)
    assert sum("PERFORM 730-CLOSE-C1" in line for line in rewritten) == 1
    assert any("PERFORM 720-FETCH-C1 UNTIL C1-EOC." in line for line in rewritten)


def test_two_sequential_independent_cursors_are_both_discovered():
    lines = _simple_flow("C1", 710, 720, 730, "PROCESS-C1") + _simple_flow(
        "C2", 810, 820, 830, "PROCESS-C2"
    )
    plans = CursorFlowPlanDiscoverer().discover(lines)
    assert [plan.cursor_name for plan in plans] == ["C1", "C2"]


def test_interleaved_cursor_operation_is_not_rewritten_by_guess():
    lines = [
        "PERFORM 710-OPEN-C1.",
        "PERFORM 810-OPEN-C2.",
        "PERFORM 720-FETCH-C1.",
        "PERFORM PROCESS-C1.",
        "UNTIL C1-EOC.",
        "PERFORM 730-CLOSE-C1.",
    ]
    discoverer = CursorFlowPlanDiscoverer()
    plans = discoverer.discover(lines)
    assert plans == []
    assert any("interleaved operation" in message for message in discoverer.messages)
