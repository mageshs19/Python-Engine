from converter.generators.procedure_division_organizer import ProcedureDivisionOrganizer


def test_legacy_organizer_preserves_original_execution_order_and_emits_no_placeholders():
    source = """       PROCEDURE DIVISION.
           PERFORM 1000-INITIALIZE-PROGRAM.
           PERFORM 2000-TREAT-PROGRAM.
           PERFORM 3000-FINALIZE-PROGRAM.
           STOP RUN.
       1000-INITIALIZE-PROGRAM.
           CONTINUE.
       2000-TREAT-PROGRAM.
           PERFORM 710-OPEN-C1.
           PERFORM 720-FETCH-C1.
           PERFORM 730-CLOSE-C1.
       3000-FINALIZE-PROGRAM.
           CONTINUE.
"""
    organizer = ProcedureDivisionOrganizer(source)
    output = organizer.organize()
    assert output == source
    assert "PERFORM 2000-TREAT-PROGRAM." in output
    assert output.index("PERFORM 710-OPEN-C1.") < output.index("PERFORM 720-FETCH-C1.")
    assert "???" not in output
    assert any("Original business execution order preserved" in msg for msg in organizer.messages)
