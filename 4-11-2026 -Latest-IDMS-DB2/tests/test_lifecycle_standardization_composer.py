from pathlib import Path

from converter.composers.lifecycle_standardization_composer import (
    LifecycleStandardizationComposer,
)
from converter.services.final_generated_output_service import FinalGeneratedOutputService


def _fixed(seq: int, body: str, indicator: str = " ") -> str:
    return f"{seq:06d}{indicator}{body:<65}{seq:08d}"


def _flat_cursor_program() -> str:
    rows = [
        _fixed(100, "PROCEDURE DIVISION USING PARM."),
        _fixed(200, "    PERFORM 600-GET-TIMESTAMP."),
        _fixed(300, "    PERFORM BEGIN-PROGRAMMA THRU BEGIN-PROGRAMMA-EXIT."),
        _fixed(400, "    PERFORM BEHANDELING THRU BEHANDELING-EXIT",),
        _fixed(500, "            UNTIL C1-EOC."),
        _fixed(600, "    PERFORM 2300-CLOSE-C1."),
        _fixed(700, "    PERFORM EINDE-PROGRAMMA THRU EINDE-PROGRAMMA-EXIT."),
        _fixed(800, "    DISPLAY 'TOTAL RECORDS: ' WS-COUNT"),
        _fixed(900, "    GOBACK."),
        _fixed(1000, "BEGIN-PROGRAMMA."),
        _fixed(1100, "    INITIALIZE DCL-ROW."),
        _fixed(1200, "    PERFORM 2100-OPEN-C1."),
        _fixed(1300, "    PERFORM 2200-FETCH-C1."),
        _fixed(1400, "BEGIN-PROGRAMMA-EXIT."),
        _fixed(1500, "    EXIT."),
        _fixed(1600, "BEHANDELING."),
        _fixed(1700, "    IF C1-KEY > ZERO"),
        _fixed(1800, "       PERFORM WRITE-REC"),
        _fixed(1900, "    END-IF."),
        _fixed(2000, "    PERFORM 2200-FETCH-C1."),
        _fixed(2100, "WRITE-REC."),
        _fixed(2200, "    ADD 1 TO WS-WRITTEN"),
        _fixed(2300, "    WRITE OUTPUT-REC."),
        _fixed(2400, "BEHANDELING-EXIT."),
        _fixed(2500, "    EXIT."),
        _fixed(2600, "EINDE-PROGRAMMA."),
        _fixed(2700, "    CLOSE OUTPUT-FILE."),
        _fixed(2800, "EINDE-PROGRAMMA-EXIT."),
        _fixed(2900, "    EXIT."),
        _fixed(3000, "2100-OPEN-C1."),
        _fixed(3100, "    EXEC SQL"),
        _fixed(3200, "      OPEN C1"),
        _fixed(3300, "    END-EXEC"),
        _fixed(3400, "    EVALUATE SQLCODE"),
        _fixed(3500, "      WHEN ZERO"),
        _fixed(3600, "        SET C1-NOT-EOC TO TRUE"),
        _fixed(3700, "      WHEN OTHER"),
        _fixed(3800, "        PERFORM SQLERROR"),
        _fixed(3900, "    END-EVALUATE."),
        _fixed(4000, "2200-FETCH-C1."),
        _fixed(4100, "    EXEC SQL"),
        _fixed(4200, "      FETCH C1 INTO :DCL-ROW"),
        _fixed(4300, "    END-EXEC"),
        _fixed(4400, "    EVALUATE SQLCODE"),
        _fixed(4500, "      WHEN ZERO"),
        _fixed(4600, "        ADD 1 TO WS-READ"),
        _fixed(4700, "        CONTINUE"),
        _fixed(4800, "      WHEN 100"),
        _fixed(4900, "        SET C1-EOC TO TRUE"),
        _fixed(5000, "      WHEN OTHER"),
        _fixed(5100, "        PERFORM SQLERROR"),
        _fixed(5200, "    END-EVALUATE."),
        _fixed(5300, "2300-CLOSE-C1."),
        _fixed(5400, "    EXEC SQL"),
        _fixed(5500, "      CLOSE C1"),
        _fixed(5600, "    END-EXEC"),
        _fixed(5700, "    EVALUATE SQLCODE"),
        _fixed(5800, "      WHEN ZERO"),
        _fixed(5900, "        CONTINUE"),
        _fixed(6000, "      WHEN OTHER"),
        _fixed(6100, "        PERFORM SQLERROR"),
        _fixed(6200, "    END-EVALUATE."),
        _fixed(6250, "2400-OPEN-C2."),
        _fixed(6251, "    EXEC SQL"),
        _fixed(6252, "      OPEN C2"),
        _fixed(6253, "    END-EXEC"),
        _fixed(6254, "    EVALUATE SQLCODE"),
        _fixed(6255, "      WHEN ZERO"),
        _fixed(6256, "        CONTINUE"),
        _fixed(6257, "      WHEN OTHER"),
        _fixed(6258, "        PERFORM SQLERROR"),
        _fixed(6259, "    END-EVALUATE."),
        _fixed(6260, "2500-FETCH-C2."),
        _fixed(6261, "    EXEC SQL"),
        _fixed(6262, "      FETCH C2 INTO :DCL-ROW"),
        _fixed(6263, "    END-EXEC"),
        _fixed(6264, "    EVALUATE SQLCODE"),
        _fixed(6265, "      WHEN ZERO"),
        _fixed(6266, "        CONTINUE"),
        _fixed(6267, "      WHEN 100"),
        _fixed(6268, "        SET C2-EOC TO TRUE"),
        _fixed(6269, "      WHEN OTHER"),
        _fixed(6270, "        PERFORM SQLERROR"),
        _fixed(6271, "    END-EVALUATE."),
        _fixed(6272, "2600-CLOSE-C2."),
        _fixed(6273, "    EXEC SQL"),
        _fixed(6274, "      CLOSE C2"),
        _fixed(6275, "    END-EXEC"),
        _fixed(6276, "    EVALUATE SQLCODE"),
        _fixed(6277, "      WHEN ZERO"),
        _fixed(6278, "        CONTINUE"),
        _fixed(6279, "      WHEN OTHER"),
        _fixed(6280, "        PERFORM SQLERROR"),
        _fixed(6281, "    END-EVALUATE."),
        _fixed(6300, "SQLERROR."),
        _fixed(6400, "    EXEC SQL INCLUDE SQLERROR END-EXEC."),
        _fixed(6500, "600-GET-TIMESTAMP."),
        _fixed(6600, "    CONTINUE."),
    ]
    return "\n".join(rows) + "\n"


def test_lifecycle_standardization_moves_flat_cursor_loop_to_standard_wrappers():
    source = _flat_cursor_program()
    composer = LifecycleStandardizationComposer()
    output = composer.compose(source)

    assert output != source
    assert "0000-MAIN-PROCEDURE." in output
    assert "PERFORM 1000-INITIALIZE-PROGRAM." in output
    assert "PERFORM 2000-PROCESS-PROGRAM." in output
    assert "PERFORM 3000-FINALIZE-PROGRAM." in output
    assert "1000-INITIALIZE-PROGRAM." in output
    assert "PERFORM 1100-GET-TIMESTAMP." in output
    assert "PERFORM 1200-BEGIN-PROGRAMMA THRU 1200-BEGIN-PROGRAMMA-EXIT." in output
    assert "2000-PROCESS-PROGRAM." in output
    assert "PERFORM 2000-TREAT-PROGRAM." in output
    assert "PERFORM 2100-OPEN-C1." in output
    # Keep the original row loop and THRU range intact. The processing wrapper
    # owns the moved OPEN/initial FETCH, original loop, and CLOSE in that order.
    assert "PERFORM 2200-FETCH-C1 UNTIL C1-EOC." not in output
    assert "PERFORM BEHANDELING THRU BEHANDELING-EXIT" in output
    assert output.index("PERFORM 2100-OPEN-C1.") < output.index("PERFORM 2200-FETCH-C1.") < output.index("PERFORM BEHANDELING THRU BEHANDELING-EXIT") < output.index("PERFORM 2300-CLOSE-C1.")
    assert "3000-FINALIZE-PROGRAM." in output
    assert "DISPLAY 'TOTAL RECORDS: ' WS-COUNT." in output
    assert "PERFORM WRITE-REC" in output
    assert "WRITE-REC." in output
    assert "PERFORM 2200-FETCH-C1." in output
    assert "PERFORM BEHANDELING THRU BEHANDELING-EXIT" in output
    assert any("Lifecycle standardization applied" in msg for msg in composer.messages)


def test_lifecycle_standardization_is_idempotent_for_standardized_output():
    source = FinalGeneratedOutputService().apply(_flat_cursor_program(), standardize_lifecycle=True)
    composer = LifecycleStandardizationComposer()
    assert composer.compose(source) == source


def test_lifecycle_standardization_preserves_nested_cursor_work_verbatim():
    source = _flat_cursor_program()
    nested = (
        _fixed(1650, "    PERFORM 2400-OPEN-C2") + "\n"
        + _fixed(1660, "    PERFORM 2500-FETCH-C2 UNTIL C2-EOC") + "\n"
        + _fixed(1670, "    PERFORM 2600-CLOSE-C2")
    )
    source = source.replace(_fixed(1700, "    IF C1-KEY > ZERO"), nested + "\n" + _fixed(1700, "    IF C1-KEY > ZERO"))
    composer = LifecycleStandardizationComposer()
    output = composer.compose(source)
    assert "0000-MAIN-PROCEDURE." in output
    assert "PERFORM 3100-OPEN-C2" in output
    assert "PERFORM 3200-FETCH-C2 UNTIL C2-EOC" in output
    assert "PERFORM 3300-CLOSE-C2" in output
    assert output.index("PERFORM 3100-OPEN-C2") < output.index("PERFORM 3200-FETCH-C2 UNTIL C2-EOC") < output.index("PERFORM 3300-CLOSE-C2")


def test_lifecycle_standardization_fails_closed_on_unresolved_numbered_target():
    source = _flat_cursor_program().replace(
        _fixed(600, "    PERFORM 2300-CLOSE-C1."),
        _fixed(600, "    PERFORM 2200-CLOSE-C1."),
    )
    composer = LifecycleStandardizationComposer()
    assert composer.compose(source) == source
    assert any("numbered PERFORM target 2200-CLOSE-C1 is unresolved" in msg for msg in composer.messages)


def test_real_vmdz7200_output_standardizes_without_breaking_fixed_format():
    path = Path("mainframe/workspace/Output/VMDZ7200_26-10-2026_052554.cbl")
    if not path.exists():
        return
    service = FinalGeneratedOutputService()
    output = service.apply(path.read_text(encoding="utf-8", errors="replace"), standardize_lifecycle=True)
    assert "0000-MAIN-PROCEDURE." in output
    assert "2000-TREAT-PROGRAM." in output
    assert "PERFORM BEHANDELING THRU BEHANDELING-EXIT" in output
    assert "PERFORM 2200-FETCH-DZBFASC1." in output
    assert "PERFORM 2200-FETCH-DZBFASC1 UNTIL DZBFASC1-EOC." not in output
    assert all(len(line) == 80 for line in output.splitlines())
    assert "PERFORM BEHANDELING THRU BEHANDELING-EXIT" in output
    assert "WRITE-FORM-REC." in output


def test_generic_cursor_bounded_flow_standardizes_vmdz4420_without_rewriting_business_logic():
    path = Path("mainframe/workspace/Output/VMDZ4420_26-10-2026_051659.cbl")
    if not path.exists():
        return
    source = path.read_text(encoding="utf-8", errors="replace")
    service = FinalGeneratedOutputService()
    output = service.apply(source, standardize_lifecycle=True)
    assert "0000-MAIN-PROCEDURE." in output
    assert "1000-INITIALIZE-PROGRAM." in output
    assert "2000-PROCESS-PROGRAM." in output
    assert "3000-FINALIZE-PROGRAM." in output
    # Initialization/date preparation and output-file opening remain before
    # the parent cursor; parent OPEN/FETCH/CLOSE are grouped in processing.
    assert output.index("PERFORM 1100-GET-TIMESTAMP.") < output.index("OPEN OUTPUT UITBST.")
    assert output.index("OPEN OUTPUT UITBST.") < output.index("PERFORM 2100-OPEN-DZBEFFC1.")
    assert output.index("PERFORM 2100-OPEN-DZBEFFC1.") < output.index("PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC.")
    assert output.index("PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC.") < output.index("PERFORM 2300-CLOSE-DZBEFFC1.")
    assert output.index("PERFORM 2300-CLOSE-DZBEFFC1.") < output.index("CLOSE UITBST.")
    # Child cursor logic and business predicates are retained verbatim.
    assert "PERFORM 3100-OPEN-DZEVEFC1" in output
    assert "PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR" in output
    assert "PERFORM 3300-CLOSE-DZEVEFC1." in output
    assert "IF NOT SW-STATUS-D = 'Y'" in output
    assert "PERFORM WRITE-UITRECORD" in output
    assert "STOP RUN." in output
    assert all(len(line) == 80 for line in output.splitlines())


def test_generic_cursor_bounded_flow_is_idempotent():
    path = Path("mainframe/workspace/Output/VMDZ4420_26-10-2026_051659.cbl")
    if not path.exists():
        return
    service = FinalGeneratedOutputService()
    once = service.apply(path.read_text(encoding="utf-8", errors="replace"))
    twice = service.apply(once)
    assert twice == once
