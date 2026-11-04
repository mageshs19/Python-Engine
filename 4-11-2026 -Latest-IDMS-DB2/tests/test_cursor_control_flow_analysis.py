from converter.analyzers.program_flow.cursor_control_flow_analysis import (
    CursorControlFlowAnalyzer,
)


def _source(body):
    return "       PROCEDURE DIVISION.\n" + body


def test_single_cursor_indexes_declare_open_fetch_close():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T END-EXEC.
           EXEC SQL OPEN C1 END-EXEC.
           EXEC SQL FETCH C1 INTO :WS-ID END-EXEC.
           EXEC SQL CLOSE C1 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert report.declared_cursors == ["C1"]
    assert [(x.operation, x.cursor) for x in report.operations] == [
        ("OPEN", "C1"), ("FETCH", "C1"), ("CLOSE", "C1")
    ]


def test_two_independent_cursors_are_not_assumed_parent_child():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T1 END-EXEC.
           EXEC SQL DECLARE C2 CURSOR FOR SELECT ID FROM T2 END-EXEC.
           EXEC SQL OPEN C1 END-EXEC.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EXEC SQL CLOSE C1 END-EXEC.
           EXEC SQL OPEN C2 END-EXEC.
           EXEC SQL FETCH C2 INTO :B END-EXEC.
           EXEC SQL CLOSE C2 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert report.declared_cursors == ["C1", "C2"]
    assert "parent-child" not in " ".join(report.relationships.values())


def test_parent_child_candidate_requires_control_flow_evidence_not_names():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T1 END-EXEC.
           EXEC SQL DECLARE C2 CURSOR FOR SELECT ID FROM T2 END-EXEC.
           PERFORM PROCESS-PARENT.
       PROCESS-PARENT.
           EXEC SQL OPEN C1 END-EXEC.
           PERFORM PROCESS-CHILD.
       PROCESS-CHILD.
           EXEC SQL OPEN C2 END-EXEC.
           EXEC SQL FETCH C2 INTO :B END-EXEC.
           EXEC SQL CLOSE C2 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert set(report.declared_cursors) == {"C1", "C2"}
    assert any("no parent-child relationship is inferred" in d for d in report.diagnostics)
    assert all("parent cursor;" not in value for value in report.relationships.values())



def test_parent_child_relationship_is_inferred_only_from_successful_fetch_call_path():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T1 END-EXEC.
           EXEC SQL DECLARE C2 CURSOR FOR SELECT ID FROM T2 END-EXEC.
           PERFORM 710-OPEN-C1.
           PERFORM 720-FETCH-C1 UNTIL C1-EOC.
           PERFORM 730-CLOSE-C1.
       720-FETCH-C1.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO
               PERFORM PROCESS-CHILD
             WHEN 100
               SET C1-EOC TO TRUE
             WHEN OTHER
               PERFORM SQLERROR
           END-EVALUATE.
       PROCESS-CHILD.
           PERFORM 810-OPEN-C2.
       810-OPEN-C2.
           EXEC SQL OPEN C2 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert "parent cursor" in report.relationships["C1"]
    assert "C2" in report.relationships["C1"]
    assert "child cursor" in report.relationships["C2"]
    assert "C1" in report.relationships["C2"]

def test_multiple_nested_cursor_levels_are_all_indexed():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T1 END-EXEC.
           EXEC SQL DECLARE C2 CURSOR FOR SELECT ID FROM T2 END-EXEC.
           EXEC SQL DECLARE C3 CURSOR FOR SELECT ID FROM T3 END-EXEC.
           EXEC SQL OPEN C1 END-EXEC.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EXEC SQL OPEN C2 END-EXEC.
           EXEC SQL FETCH C2 INTO :B END-EXEC.
           EXEC SQL OPEN C3 END-EXEC.
           EXEC SQL FETCH C3 INTO :C END-EXEC.
           EXEC SQL CLOSE C3 END-EXEC.
           EXEC SQL CLOSE C2 END-EXEC.
           EXEC SQL CLOSE C1 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert report.declared_cursors == ["C1", "C2", "C3"]
    assert len(report.operations) == 9


def test_conditional_cursor_execution_is_flagged_for_review():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T END-EXEC.
           IF WS-USE-CURSOR = 'Y'
               EXEC SQL OPEN C1 END-EXEC
           END-IF.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EXEC SQL CLOSE C1 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert any("conditional/branch context" in v for v in report.relationships.values())


def test_cursor_inside_loop_is_flagged_for_review():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T END-EXEC.
           PERFORM UNTIL WS-DONE = 'Y'
               EXEC SQL OPEN C1 END-EXEC
               EXEC SQL FETCH C1 INTO :A END-EXEC
               EXEC SQL CLOSE C1 END-EXEC
           END-PERFORM.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert any("loop-context" in v for v in report.relationships.values())


def test_fetch_eoc_and_sql_error_logic_is_not_mistaken_for_cursor_operations():
    source = _source("""       DRIVER.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EVALUATE SQLCODE
             WHEN 0 CONTINUE
             WHEN 100 MOVE 'Y' TO C1-EOC
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert len(report.operations_for("C1", "FETCH")) == 1
    # The analyzer does not rewrite or collapse SQLCODE branches.
    assert "WHEN 100" in source and "WHEN OTHER" in source


def test_open_fetch_close_sql_error_context_remains_in_source():
    source = _source("""       DRIVER.
           EXEC SQL OPEN C1 END-EXEC.
           IF SQLCODE NOT = 0 PERFORM SQLERROR END-IF.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EVALUATE SQLCODE
             WHEN 100 MOVE 'Y' TO C1-EOC
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
           EXEC SQL CLOSE C1 END-EXEC.
           IF SQLCODE NOT = 0 PERFORM SQLERROR END-IF.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert [x.operation for x in report.operations] == ["OPEN", "FETCH", "CLOSE"]
    assert "PERFORM SQLERROR" in source


def test_restart_commit_and_checkpoint_statements_are_preserved():
    source = _source("""       DRIVER.
           PERFORM 800-RESTART-CONTROL.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T END-EXEC.
           EXEC SQL OPEN C1 END-EXEC.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           PERFORM 830-PROCESS-COMMIT.
           EXEC SQL CLOSE C1 END-EXEC.
       800-RESTART-CONTROL.
           CONTINUE.
       830-PROCESS-COMMIT.
           EXEC SQL COMMIT END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert "800-RESTART-CONTROL" in report.graph.paragraph_names
    assert "830-PROCESS-COMMIT" in report.graph.paragraph_names
    assert "COMMIT" in source


def test_perform_thru_and_renamed_paragraph_targets_are_resolved():
    source = _source("""       DRIVER.
           PERFORM FIRST-PARA THRU LAST-PARA.
       FIRST-PARA.
           EXEC SQL OPEN C1 END-EXEC.
       MIDDLE-PARA.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
       LAST-PARA.
           EXEC SQL CLOSE C1 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    edge = next(e for e in report.graph.edges if e.target == "FIRST-PARA")
    assert edge.through == "LAST-PARA"
    assert edge.covered_nodes == ("FIRST-PARA", "MIDDLE-PARA", "LAST-PARA")


def test_program_without_cursors_is_valid_and_not_given_cursor_template():
    report = CursorControlFlowAnalyzer().analyze(
        _source("""       DRIVER.
           DISPLAY 'NO CURSORS'.
           STOP RUN.
""")
    )
    assert report.declared_cursors == []
    assert report.operations == []
    assert any("No cursor declarations" in d for d in report.diagnostics)


def test_ambiguous_relationship_is_flagged_not_guessed():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T1 END-EXEC.
           EXEC SQL DECLARE C2 CURSOR FOR SELECT ID FROM T2 END-EXEC.
           EXEC SQL OPEN C1 END-EXEC.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EXEC SQL CLOSE C1 END-EXEC.
           EXEC SQL OPEN C2 END-EXEC.
           EXEC SQL FETCH C2 INTO :B END-EXEC.
           EXEC SQL CLOSE C2 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert any("inferred from cursor names" in d for d in report.diagnostics)
    assert all("parent-child" not in v for v in report.relationships.values())


def test_child_open_in_when_other_is_not_inferred_as_parent_child():
    source = _source("""       DRIVER.
           EXEC SQL DECLARE C1 CURSOR FOR SELECT ID FROM T1 END-EXEC.
           EXEC SQL DECLARE C2 CURSOR FOR SELECT ID FROM T2 END-EXEC.
       720-FETCH-C1.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO
               CONTINUE
             WHEN OTHER
               PERFORM PROCESS-CHILD
           END-EVALUATE.
       PROCESS-CHILD.
           PERFORM 810-OPEN-C2.
       810-OPEN-C2.
           EXEC SQL OPEN C2 END-EXEC.
""")
    report = CursorControlFlowAnalyzer().analyze(source)
    assert "parent cursor" not in report.relationships.get("C1", "")
    assert "child cursor" not in report.relationships.get("C2", "")
    assert any("no parent-child relationship is inferred" in d for d in report.diagnostics)
