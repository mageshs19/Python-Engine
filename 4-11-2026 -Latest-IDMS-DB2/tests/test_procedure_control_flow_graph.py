from converter.analyzers.program_flow.procedure_control_flow_graph import (
    ProcedureControlFlowGraphBuilder,
)


def test_graph_resolves_named_perform_and_physical_thru_range():
    source = """       PROCEDURE DIVISION.
           PERFORM START-PARA THRU END-PARA.
           STOP RUN.
       START-PARA.
           PERFORM WORK-PARA.
       WORK-PARA.
           CONTINUE.
       END-PARA.
           CONTINUE.
"""
    graph = ProcedureControlFlowGraphBuilder().build(source)
    range_edge = next(edge for edge in graph.edges if edge.target == "START-PARA")
    nested_edge = next(edge for edge in graph.edges if edge.target == "WORK-PARA")
    assert range_edge.resolution == "local"
    assert range_edge.covered_nodes == ("START-PARA", "WORK-PARA", "END-PARA")
    assert nested_edge.source == "START-PARA"
    assert nested_edge.covered_nodes == ("WORK-PARA",)


def test_graph_resolves_section_target_and_multiline_thru():
    source = """       PROCEDURE DIVISION.
           PERFORM PROCESS-SECTION.
       PROCESS-SECTION SECTION.
       FIRST-PARA.
           CONTINUE.
       LAST-PARA.
           CONTINUE.
           PERFORM
             FIRST-PARA THRU
             LAST-PARA.
"""
    graph = ProcedureControlFlowGraphBuilder().build(source)
    edge = next(edge for edge in graph.edges if edge.target == "FIRST-PARA")
    assert edge.through == "LAST-PARA"
    assert edge.covered_nodes == ("FIRST-PARA", "LAST-PARA")
    section_edge = next(edge for edge in graph.edges if edge.target == "PROCESS-SECTION")
    assert section_edge.resolution == "local"


def test_graph_flags_ambiguous_duplicate_target_and_reversed_thru():
    source = """       PROCEDURE DIVISION.
           PERFORM DUPLICATE-PARA.
           PERFORM LATER THRU EARLIER.
       EARLIER.
           CONTINUE.
       LATER.
           CONTINUE.
       DUPLICATE-PARA.
           CONTINUE.
       DUPLICATE-PARA.
           CONTINUE.
"""
    graph = ProcedureControlFlowGraphBuilder().build(source)
    assert any(edge.target == "DUPLICATE-PARA" and edge.resolution == "ambiguous" for edge in graph.edges)
    assert any("reversed PERFORM THRU range LATER -> EARLIER" in item for item in graph.diagnostics)


def test_graph_does_not_mistake_inline_perform_until_for_paragraph_call():
    source = """       PROCEDURE DIVISION.
       DRIVER.
           PERFORM UNTIL EOF = 'Y'
               PERFORM PROCESS-ROW
           END-PERFORM.
       PROCESS-ROW.
           CONTINUE.
"""
    graph = ProcedureControlFlowGraphBuilder().build(source)
    assert len(graph.edges) == 1
    assert graph.edges[0].target == "PROCESS-ROW"


def test_graph_ignores_table_perform_times_as_non_paragraph_call():
    source = """       PROCEDURE DIVISION.
       DRIVER.
           PERFORM NB-READ OF WS-RESTART-REC TIMES
               PERFORM PROCESS-ROW
           END-PERFORM.
       PROCESS-ROW.
           CONTINUE.
"""
    graph = ProcedureControlFlowGraphBuilder().build(source)
    assert [edge.target for edge in graph.edges] == ["PROCESS-ROW"]


def test_section_target_covers_all_paragraphs_until_next_section():
    source = """       PROCEDURE DIVISION.
           PERFORM FIRST-SECTION.
       FIRST-SECTION SECTION.
       FIRST-PARA.
           CONTINUE.
       SECOND-PARA.
           CONTINUE.
       SECOND-SECTION SECTION.
       THIRD-PARA.
           CONTINUE.
"""
    graph = ProcedureControlFlowGraphBuilder().build(source)
    edge = next(edge for edge in graph.edges if edge.target == "FIRST-SECTION")
    assert edge.covered_nodes == ("FIRST-PARA", "SECOND-PARA")


def test_section_node_span_ends_at_next_section_not_first_paragraph():
    source = """       PROCEDURE DIVISION.
       FIRST-SECTION SECTION.
       FIRST-PARA.
           CONTINUE.
       SECOND-PARA.
           CONTINUE.
       SECOND-SECTION SECTION.
       THIRD-PARA.
           CONTINUE.
"""
    graph = ProcedureControlFlowGraphBuilder().build(source)
    first_section = next(node for node in graph.nodes if node.name == "FIRST-SECTION")
    second_section = next(node for node in graph.nodes if node.name == "SECOND-SECTION")
    assert first_section.end_line == second_section.start_line - 1


def test_graph_expands_plain_procedure_copybook_and_resolves_target(tmp_path):
    program_dir = tmp_path / "Program"
    copybook_dir = tmp_path / "Copybook"
    program_dir.mkdir()
    copybook_dir.mkdir()
    (copybook_dir / "PROCWORK.cpy").write_text(
        "       COPY PROCNEST.\n       COPIED-WORK.\n           CONTINUE.\n",
        encoding="utf-8",
    )
    (copybook_dir / "PROCNEST.cpy").write_text(
        "       NESTED-WORK.\n           CONTINUE.\n",
        encoding="utf-8",
    )
    source = program_dir / "MAIN.cbl"
    source.write_text(
        "       PROCEDURE DIVISION.\n"
        "       DRIVER.\n"
        "           PERFORM COPIED-WORK.\n"
        "           COPY PROCWORK.\n"
        "           PERFORM NESTED-WORK.\n",
        encoding="utf-8",
    )

    graph = ProcedureControlFlowGraphBuilder().build(source)

    assert "COPIED-WORK" in graph.paragraph_names
    assert "NESTED-WORK" in graph.paragraph_names
    assert not any("not resolved locally" in item for item in graph.diagnostics)
    assert all(edge.resolution == "local" for edge in graph.edges)


def test_graph_reports_missing_procedure_copybook_without_guessing(tmp_path):
    source = tmp_path / "MAIN.cbl"
    source.write_text(
        "       PROCEDURE DIVISION.\n"
        "       DRIVER.\n"
        "           COPY MISSING-PROC.\n"
        "           PERFORM MISSING-PARA.\n",
        encoding="utf-8",
    )
    graph = ProcedureControlFlowGraphBuilder().build(source)
    assert any("procedure COPY member MISSING-PROC not found" in item for item in graph.diagnostics)
    assert any("PERFORM target MISSING-PARA not resolved locally" in item for item in graph.diagnostics)
