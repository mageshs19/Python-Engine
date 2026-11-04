from pathlib import Path

from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
    ChildFetchEarlyStopCleanup,
)
from converter.composers.cleanup.cleanup_message_collector import (
    CleanupMessageCollector,
)


def test_sw_status_child_loop_uses_fetch_driven_business_processing():
    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root
        / "tests"
        / "fixtures"
        / "VMDZ4420_nested_cursor_control_flow.cbl"
    )
    source = source_path.read_text(encoding="utf-8", errors="replace")

    cleanup = ChildFetchEarlyStopCleanup(CleanupMessageCollector())
    output = cleanup.ensure_child_fetch_early_stop(source)

    logical_lines = [
        cleanup._logical(line).strip()
        for line in output.splitlines()
    ]
    joined = "\n".join(logical_lines)

    loop = (
        "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR\n"
        "SW-STATUS-D = 'Y'"
    )
    assert loop in joined
    assert "PERFORM VERWERK-VMBEVEF UNTIL DZEVEFC1-EOC" not in joined

    fetch_start = next(
        i for i, line in enumerate(logical_lines)
        if line == "3200-FETCH-DZEVEFC1."
    )
    fetch_end = next(
        i for i in range(fetch_start + 1, len(logical_lines))
        if logical_lines[i] == "END-EVALUATE"
    )
    fetch_branch = "\n".join(logical_lines[fetch_start:fetch_end + 1])
    assert "WHEN ZERO" in fetch_branch
    assert "PERFORM VERWERK-VMBEVEF" in fetch_branch
    assert "WHEN 100" in fetch_branch
    assert "SET DZEVEFC1-EOC TO TRUE" in fetch_branch

    business_start = next(
        i for i, line in enumerate(logical_lines)
        if line == "VERWERK-VMBEVEF."
    )
    next_paragraph = next(
        i for i in range(business_start + 1, len(logical_lines))
        if logical_lines[i].endswith(".")
        and logical_lines[i].upper().startswith(("WRITE-UITRECORD.", "3100-OPEN-", "3200-FETCH-", "3300-CLOSE-"))
    )
    business_body = "\n".join(logical_lines[business_start:next_paragraph])
    assert "PERFORM 3200-FETCH-DZEVEFC1" not in business_body
    assert "IF NOT SQLCODE = 100" not in business_body

    close_index = next(
        i for i, line in enumerate(logical_lines)
        if line == "PERFORM 3300-CLOSE-DZEVEFC1."
    )
    guard_index = next(
        i for i, line in enumerate(logical_lines)
        if i > close_index and line == "IF NOT SW-STATUS-D = 'Y'"
    )
    parent_fetch_index = next(
        i for i, line in enumerate(logical_lines)
        if i > guard_index and line == "PERFORM 2200-FETCH-DZBEFFC1."
    )
    assert close_index < guard_index < parent_fetch_index
    assert output.count("PERFORM 3300-CLOSE-DZEVEFC1") == 1


def test_fetch_driven_normalization_preserves_program_specific_output_logic():
    """Generic loop repair must lift the source output block, not synthesize one."""
    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root
        / "tests"
        / "fixtures"
        / "VMDZ4420_nested_cursor_control_flow.cbl"
    )
    source = source_path.read_text(encoding="utf-8", errors="replace")
    source = source.replace("SW-STATUS-D", "SW-STATUS-X")
    source = source.replace("WRITE-UITRECORD", "WRITE-OUTRECORD")
    source = source.replace("WS-NB-OUTPUT-COUNT", "WS-NB-RESULT-COUNT")

    cleanup = ChildFetchEarlyStopCleanup(CleanupMessageCollector())
    output = cleanup.ensure_child_fetch_early_stop(source)
    logical_lines = [cleanup._logical(line).strip() for line in output.splitlines()]
    joined = "\n".join(logical_lines)

    assert "MOVE 'N' TO SW-STATUS-X" in joined
    assert "SW-STATUS-X = 'Y'" in joined
    assert "IF NOT SW-STATUS-X = 'Y'" in joined
    assert "IF WS-STATUS = 'C'" in joined
    assert "PERFORM WRITE-OUTRECORD" in joined
    assert "ADD 1 TO WS-NB-RESULT-COUNT" in joined
    assert "SW-STATUS-D" not in joined
    assert "WS-NB-OUTPUT-COUNT" not in joined
    assert "PERFORM 3200-FETCH-DZEVEFC1" not in "\n".join(
        logical_lines[
            next(i for i, line in enumerate(logical_lines) if line == "VERWERK-VMBEVEF."):
            next(i for i, line in enumerate(logical_lines) if line == "3300-CLOSE-DZEVEFC1.")
        ]
    )


def test_fetch_driven_normalization_refuses_to_invent_missing_output_branch():
    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root
        / "tests"
        / "fixtures"
        / "VMDZ4420_nested_cursor_control_flow.cbl"
    )
    source = source_path.read_text(encoding="utf-8", errors="replace")
    # Without the SQLCODE=100 branch containing the original output decision,
    # this cleanup must not fabricate a WRITE paragraph or output counter.
    source = source.replace("IF SQLCODE = 100", "IF SQLCODE = 101")
    cleanup = ChildFetchEarlyStopCleanup(CleanupMessageCollector())
    output = cleanup._normalize_sw_status_child_loop(source)
    assert output == source


def test_fetch_driven_normalization_resequences_inserted_fixed_format_lines():
    """Inserted COBOL records must not clone the anchor's sequence fields."""
    from converter.composers.fixed_format_composer import FixedFormatComposer

    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root
        / "tests"
        / "fixtures"
        / "VMDZ4420_nested_cursor_control_flow.cbl"
    )
    source = source_path.read_text(encoding="utf-8", errors="replace")
    cleanup = ChildFetchEarlyStopCleanup(CleanupMessageCollector())
    # The cleanup pass is semantic-only; physical layout is owned by the
    # enclosing composer / final renderer.
    output = FixedFormatComposer().format(
        cleanup.ensure_child_fetch_early_stop(source)
    )

    formatter = FixedFormatComposer()
    assert formatter.validate_fixed_format(output) == []

    physical_lines = [line for line in output.splitlines() if line.strip()]
    left_sequences = [int(line[:6]) for line in physical_lines]
    right_sequences = [int(line[72:80]) for line in physical_lines]
    assert len(left_sequences) == len(set(left_sequences))
    assert len(right_sequences) == len(set(right_sequences))
    assert all(
        current - previous == 10
        for previous, current in zip(left_sequences, left_sequences[1:])
    )
    assert all(
        current - previous == 10000
        for previous, current in zip(right_sequences, right_sequences[1:])
    )

    logical_lines = [cleanup._logical(line).strip() for line in output.splitlines()]
    assert "MOVE 'N' TO SW-STATUS-D" in logical_lines
    assert "IF NOT SW-STATUS-D = 'Y'" in logical_lines
    assert "PERFORM WRITE-UITRECORD" in logical_lines


def test_child_fetch_semantic_rewrite_does_not_run_global_formatter(monkeypatch):
    """Semantic cleanup must not own physical layout or resequencing."""
    from converter.composers.fixed_format_composer import FixedFormatComposer

    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root
        / "tests"
        / "fixtures"
        / "VMDZ4420_nested_cursor_control_flow.cbl"
    )
    source = source_path.read_text(encoding="utf-8", errors="replace")

    def forbidden_format(*args, **kwargs):
        raise AssertionError("semantic cleanup must not invoke physical formatter")

    monkeypatch.setattr(FixedFormatComposer, "format", forbidden_format)
    cleanup = ChildFetchEarlyStopCleanup(CleanupMessageCollector())
    output = cleanup.ensure_child_fetch_early_stop(source)

    assert "MOVE 'N' TO SW-STATUS-D" in "\n".join(
        cleanup._logical(line).strip() for line in output.splitlines()
    )
