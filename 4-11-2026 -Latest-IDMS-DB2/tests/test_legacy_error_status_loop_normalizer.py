from converter.composers.cursor_flow.legacy_error_status_loop_normalizer import LegacyErrorStatusLoopNormalizer


def test_normalizes_only_proven_cursor_owned_error_status_loops():
    source = """000010 PROCEDURE DIVISION.                                           00010000
000020     PERFORM PROCESS-ROW UNTIL ERROR-STATUS NOT = '0000'.          00020000
000030 PROCESS-ROW.                                                     00030000
000040     MOVE A TO B.                                                 00040000
000050     PERFORM 720-FETCH-CUR1.                                      00050000
000060 720-FETCH-CUR1.                                                  00060000
000070     EVALUATE SQLCODE                                             00070000
000080       WHEN ZERO                                                  00080000
000090            PERFORM PROCESS-ROW                                   00090000
000100       WHEN 100                                                   00100000
000110            SET CUR1-EOC TO TRUE                                  00110000
000120     END-EVALUATE.                                                00120000
"""
    normalizer = LegacyErrorStatusLoopNormalizer()
    output = normalizer.compose(source)
    assert "PERFORM PROCESS-ROW UNTIL CUR1-EOC." in output
    assert normalizer.messages


def test_leaves_ambiguous_error_status_loop_unchanged():
    source = """000010     PERFORM PROCESS-ROW UNTIL ERROR-STATUS NOT = '0000'.      00010000
000020 PROCESS-ROW.                                                     00020000
000030     CONTINUE.                                                    00030000
"""
    output = LegacyErrorStatusLoopNormalizer().compose(source)
    assert "UNTIL ERROR-STATUS NOT = '0000'" in output
