from converter.composers.counter_declaration_composer import CounterDeclarationComposer


SOURCE = """000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID. SAMPLE.
000300 DATA DIVISION.
000400 FILE SECTION.
000500 WORKING-STORAGE SECTION.
000600 01 COUNT-TREATED PIC 9(15) VALUE ZEROES.
000700 PROCEDURE DIVISION.
000800 MAIN.
000900     PERFORM READ-INPUT
000950     ADD 1 TO COUNT-TREATED
001000     DISPLAY '# TREATED  = ' COUNT-TREATED
001100     STOP RUN.
001200 READ-INPUT.
001300     READ INPUT-FILE INTO INPUT-REC
001400       AT END
001500         SET INPUT-EOF TO TRUE
001600       NOT AT END
001700         CONTINUE
001800     END-READ.
"""


def test_adds_successful_input_counter_and_preserves_treated_total():
    composer = CounterDeclarationComposer()
    generated = composer.compose(SOURCE)

    assert "01 WS-TOTAL-INPUT PIC S9(11) COMP-3 VALUE +0." in generated
    assert "ADD 1 TO WS-TOTAL-INPUT" in generated
    assert "DISPLAY '# TREATED    = ' WS-COUNT-TREATED" in generated
    assert "DISPLAY 'TOTAL INPUTS ='  WS-TOTAL-INPUT" in generated
    assert "01 WS-COUNT-TREATED PIC 9(15) VALUE ZEROES." in generated


def test_input_counter_is_only_incremented_once_and_composer_is_idempotent():
    composer = CounterDeclarationComposer()
    once = composer.compose(SOURCE)
    twice = composer.compose(once)

    assert twice.count("ADD 1 TO WS-TOTAL-INPUT") == 1
    assert twice.count("DISPLAY 'TOTAL INPUTS ='  WS-TOTAL-INPUT") == 1
    assert twice.count("01 WS-TOTAL-INPUT PIC S9(11) COMP-3 VALUE +0.") == 1


def test_eof_is_not_counted_as_an_input_record():
    composer = CounterDeclarationComposer()
    generated = composer.compose(SOURCE)
    read_block = generated.split("READ INPUT-FILE", 1)[1].split("END-READ", 1)[0]

    assert "AT END" in read_block
    assert "NOT AT END" in read_block
    assert read_block.index("NOT AT END") < read_block.index("ADD 1 TO WS-TOTAL-INPUT")



def test_does_not_add_input_totals_to_programs_without_treated_counter_convention():
    source = """\
000100 IDENTIFICATION DIVISION.
000200 DATA DIVISION.
000300 WORKING-STORAGE SECTION.
000400 PROCEDURE DIVISION.
000500     READ INPUT-FILE INTO INPUT-REC
000600       NOT AT END
000700         CONTINUE
000800     END-READ.
000900     STOP RUN.
"""
    generated = CounterDeclarationComposer().compose(source)
    assert "WS-TOTAL-INPUT" not in generated
