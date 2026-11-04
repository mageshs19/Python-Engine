from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.output_write_placement_cleanup import (
    OutputWritePlacementCleanup,
)


def _nested_parent_child_program() -> str:
    """Use four-digit cursor numbers so numeric thresholds cannot infer depth."""
    return """PROCEDURE DIVISION.
    PERFORM 2100-OPEN-DZBEFFC1.
    PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC.
    PERFORM 2300-CLOSE-DZBEFFC1.
    STOP RUN.
HOOFDVERWERKING.
    PERFORM 3100-OPEN-DZEVEFC1.
    PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.
    PERFORM 3300-CLOSE-DZEVEFC1.
VERWERK-VMBEVEF.
    IF WS-STATUS = 'C'
       WRITE UITRECORD
    END-IF.
2100-OPEN-DZBEFFC1.
    CONTINUE.
2200-FETCH-DZBEFFC1.
    EVALUATE SQLCODE
      WHEN ZERO
        PERFORM HOOFDVERWERKING
      WHEN 100 CONTINUE
    END-EVALUATE.
2300-CLOSE-DZBEFFC1.
    CONTINUE.
3100-OPEN-DZEVEFC1.
    CONTINUE.
3200-FETCH-DZEVEFC1.
    EVALUATE SQLCODE
      WHEN ZERO
        PERFORM VERWERK-VMBEVEF
      WHEN 100 CONTINUE
    END-EVALUATE.
3300-CLOSE-DZEVEFC1.
    CONTINUE.
"""


def test_write_moves_after_child_close_not_after_parent_close():
    collector = CleanupMessageCollector()
    cleanup = OutputWritePlacementCleanup(collector)

    result = cleanup.move_output_write_after_child_loop(
        _nested_parent_child_program()
    )

    child_close = result.index("PERFORM 3300-CLOSE-DZEVEFC1.")
    write_guard = result.index("IF NOT SW-STATUS-D = 'Y'")
    stop_run = result.index("STOP RUN.")

    # Paragraph definitions follow the mainline in source order. The
    # write therefore appears textually after STOP RUN, but executes from
    # HOOFDVERWERKING before control returns to the mainline.
    assert child_close < write_guard < result.index("VERWERK-VMBEVEF.")
    assert write_guard > stop_run
    assert result.count("WRITE UITRECORD") == 1
    assert any(
        "moved output write block from VERWERK-VMBEVEF to HOOFDVERWERKING" in message
        for message in collector.messages
    )
    assert not any(
        "moved output write block from HOOFDVERWERKING to (unnamed)" in message
        for message in collector.messages
    )


def test_nested_cursor_parent_is_not_reclassified_as_child_row_paragraph():
    collector = CleanupMessageCollector()
    cleanup = OutputWritePlacementCleanup(collector)

    result = cleanup.move_output_write_after_child_loop(
        _nested_parent_child_program()
    )

    # The write remains within the parent business paragraph after the
    # child cursor closes; it must not be placed after the outer cursor.
    child_close = result.index("PERFORM 3300-CLOSE-DZEVEFC1.")
    write_guard = result.index("IF NOT SW-STATUS-D = 'Y'")
    stop_run = result.index("STOP RUN.")
    assert child_close < write_guard < result.index("VERWERK-VMBEVEF.")
    assert write_guard > stop_run


def test_early_stop_targets_nested_cursor_not_paragraph_number():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    collector = CleanupMessageCollector()
    cleanup = ChildFetchEarlyStopCleanup(collector)
    source = _nested_parent_child_program().replace(
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.",
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
    ).replace(
        "VERWERK-VMBEVEF.\n    IF WS-STATUS = 'C'",
        "VERWERK-VMBEVEF.\n    MOVE 'Y' TO SW-STATUS-D.\n    IF WS-STATUS = 'C'",
    ) + "\n01 SW-STATUS-D PIC X.\n"

    result = cleanup.ensure_child_fetch_early_stop(source)

    # The outer cursor is a root scan, despite its four-digit paragraph
    # number. Only the structurally nested child cursor gets early-stop.
    assert "PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC." in result
    assert "PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC OR" not in result
    assert "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR" in result
    assert "SW-STATUS-D = 'Y'" in result


def test_nested_child_without_reachable_yes_assignment_does_not_get_early_stop():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = _nested_parent_child_program().replace(
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.",
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
    ) + "\n01 SW-STATUS-D PIC X.\n"

    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)

    assert "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC." in result
    assert "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR" not in result
    assert "PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC OR" not in result


def test_single_cursor_never_gets_shared_child_early_stop_condition():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = """PROCEDURE DIVISION.
    PERFORM 710-OPEN-DZBEFFC1.
    PERFORM 720-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC.
    PERFORM 730-CLOSE-DZBEFFC1.
    GOBACK.
710-OPEN-DZBEFFC1.
    CONTINUE.
720-FETCH-DZBEFFC1.
    EVALUATE SQLCODE
      WHEN ZERO
        PERFORM PROCESS-ROW
      WHEN 100 CONTINUE
    END-EVALUATE.
PROCESS-ROW.
    MOVE 'Y' TO SW-STATUS-D.
    CONTINUE.
730-CLOSE-DZBEFFC1.
    CONTINUE.
01 SW-STATUS-D PIC X.
"""

    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)

    assert "PERFORM 720-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC." in result
    assert "PERFORM 720-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC OR" not in result


def test_nested_cursor_classification_is_independent_of_numbering_scheme():
    from converter.composers.cleanup.cursor_nesting_analyser import (
        CursorNestingAnalyser,
    )

    source = _nested_parent_child_program()
    source = source.replace("2100-", "710-").replace("2200-", "720-").replace("2300-", "730-")
    source = source.replace("3100-", "810-").replace("3200-", "820-").replace("3300-", "830-")
    lines = source.splitlines()
    analyser = CursorNestingAnalyser()

    assert not analyser.is_nested_fetch(lines, "720-FETCH-DZBEFFC1")
    assert analyser.is_nested_fetch(lines, "820-FETCH-DZEVEFC1")


def test_child_flag_reset_is_not_borrowed_from_previous_paragraph():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = _nested_parent_child_program()
    # A reset at the end of the preceding paragraph must not count as the
    # reset for this child cursor. Otherwise a prior Y state can leak in.
    source = source.replace(
        "STOP RUN.\nHOOFDVERWERKING.",
        "MOVE 'N' TO SW-STATUS-D.\nSTOP RUN.\nHOOFDVERWERKING.",
    )
    source = source.replace(
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.",
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
    ).replace(
        "VERWERK-VMBEVEF.\n    IF WS-STATUS = 'C'",
        "VERWERK-VMBEVEF.\n    MOVE 'Y' TO SW-STATUS-D.\n    IF WS-STATUS = 'C'",
    )
    source += "\n01 SW-STATUS-D PIC X.\n"

    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)
    parent_body = result.split("HOOFDVERWERKING.", 1)[1].split("VERWERK-VMBEVEF.", 1)[0]
    assert "MOVE 'N' TO SW-STATUS-D" in parent_body
    assert "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR" in parent_body


def test_child_flag_is_reset_again_after_a_previous_child_loop():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = _nested_parent_child_program().replace(
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.",
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
    ).replace(
        "VERWERK-VMBEVEF.\n    IF WS-STATUS = 'C'",
        "VERWERK-VMBEVEF.\n    MOVE 'Y' TO SW-STATUS-D.\n    IF WS-STATUS = 'C'",
    )
    source = source.replace(
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.\n    PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
        1,
    )
    source += "\n01 SW-STATUS-D PIC X.\n"
    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)
    assert result.count("MOVE 'N' TO SW-STATUS-D") >= 2



def test_child_flag_reset_is_repeated_after_intervening_perform_call():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = _nested_parent_child_program().replace(
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.",
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
    ).replace(
        "HOOFDVERWERKING.\n    PERFORM 3100-OPEN-DZEVEFC1.",
        "HOOFDVERWERKING.\n    MOVE 'N' TO SW-STATUS-D.\n    PERFORM 777-CHECK-STATUS.\n    PERFORM 3100-OPEN-DZEVEFC1.",
    ).replace(
        "VERWERK-VMBEVEF.\n    IF WS-STATUS = 'C'",
        "VERWERK-VMBEVEF.\n    MOVE 'Y' TO SW-STATUS-D.\n    IF WS-STATUS = 'C'",
    )
    source += "\n01 SW-STATUS-D PIC X.\n"

    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)
    child_loop = result.index("PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR")
    preceding = result[:child_loop]
    assert preceding.rstrip().endswith("MOVE 'N' TO SW-STATUS-D")
    assert preceding.count("MOVE 'N' TO SW-STATUS-D") >= 2


def _business_paragraph_driven_nested_cursor_program() -> str:
    """VMDZ4420-style loop: business paragraph performs the next child FETCH."""
    return """PROCEDURE DIVISION.
    PERFORM 2100-OPEN-DZBEFFC1.
    PERFORM 2200-FETCH-DZBEFFC1.
    PERFORM HOOFDVERWERKING UNTIL DZBEFFC1-EOC.
    PERFORM 2300-CLOSE-DZBEFFC1.
    STOP RUN.
HOOFDVERWERKING.
    MOVE SPACE TO WS-STATUS.
    PERFORM 3100-OPEN-DZEVEFC1.
    PERFORM 3200-FETCH-DZEVEFC1.
    PERFORM VERWERK-VMBEVEF
      UNTIL DZEVEFC1-EOC.
    PERFORM 3300-CLOSE-DZEVEFC1.
    PERFORM 2200-FETCH-DZBEFFC1.
VERWERK-VMBEVEF.
    IF EVENT-CODE = '0168'
       MOVE 'Y' TO SW-STATUS-D
    END-IF.
    IF NOT SQLCODE = 100
       PERFORM 3200-FETCH-DZEVEFC1
    END-IF.
2100-OPEN-DZBEFFC1.
    CONTINUE.
2200-FETCH-DZBEFFC1.
    CONTINUE.
2300-CLOSE-DZBEFFC1.
    CONTINUE.
3100-OPEN-DZEVEFC1.
    CONTINUE.
3200-FETCH-DZEVEFC1.
    EVALUATE SQLCODE
      WHEN ZERO CONTINUE
      WHEN 100 CONTINUE
    END-EVALUATE.
3300-CLOSE-DZEVEFC1.
    CONTINUE.
01 SW-STATUS-D PIC X.
"""


def test_business_paragraph_loop_preserves_sw_status_d_early_stop():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = _business_paragraph_driven_nested_cursor_program()
    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)

    assert "MOVE 'N' TO SW-STATUS-D\n    PERFORM VERWERK-VMBEVEF UNTIL DZEVEFC1-EOC OR" in result
    assert "SW-STATUS-D = 'Y'" in result
    assert result.index("MOVE 'N' TO SW-STATUS-D") < result.index(
        "PERFORM VERWERK-VMBEVEF UNTIL DZEVEFC1-EOC OR"
    )


def test_business_paragraph_loop_does_not_add_flag_without_business_assignment():
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = _business_paragraph_driven_nested_cursor_program().replace(
        "       MOVE 'Y' TO SW-STATUS-D\n", "       CONTINUE\n"
    )
    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)

    assert "PERFORM VERWERK-VMBEVEF\n      UNTIL DZEVEFC1-EOC." in result
    assert "PERFORM VERWERK-VMBEVEF UNTIL DZEVEFC1-EOC OR" not in result


def test_business_stop_flag_is_discovered_from_logic_not_its_name():
    """A differently named business flag gets the same proven loop treatment."""
    from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
        ChildFetchEarlyStopCleanup,
    )

    source = _nested_parent_child_program().replace(
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.",
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC.",
    ).replace(
        "VERWERK-VMBEVEF.\n    IF WS-STATUS = 'C'",
        "VERWERK-VMBEVEF.\n    MOVE 'Y' TO SW-CHILD-STOP.\n    IF WS-STATUS = 'C'",
    ).replace("SW-STATUS-D", "SW-CHILD-STOP")
    source += "\n01 SW-CHILD-STOP PIC X.\n"

    result = ChildFetchEarlyStopCleanup(
        CleanupMessageCollector()
    ).ensure_child_fetch_early_stop(source)

    assert "MOVE 'N' TO SW-CHILD-STOP" in result
    assert "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR" in result
    assert "SW-CHILD-STOP = 'Y'" in result
    assert "SW-STATUS-D" not in result


def test_output_guard_uses_the_flag_found_in_the_child_loop():
    source = _nested_parent_child_program().replace(
        "SW-STATUS-D", "SW-CHILD-STOP"
    )
    result = OutputWritePlacementCleanup(
        CleanupMessageCollector()
    ).move_output_write_after_child_loop(source)

    assert "IF NOT SW-CHILD-STOP = 'Y'" in result
    assert "IF NOT SW-STATUS-D = 'Y'" not in result
