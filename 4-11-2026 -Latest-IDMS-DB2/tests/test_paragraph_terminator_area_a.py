from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.paragraph_terminator_cleanup import ParagraphTerminatorCleanup


def test_area_b_single_word_continuation_is_not_misread_as_paragraph_header():
    source = "\n".join(
        [
            "000100 PROCEDURE DIVISION.",
            "000200 210-STORE-EFF.",
            "000300     MOVE SPACES TO VMBEFF                                  00030000",
            "000400                    VMBEVEF.                                00040000",
            "000500     MOVE '1002' TO CT-RK-TPROD OF VMBEFF.",
            "000600 220-MOD-EVEF.",
            "000700     CONTINUE.",
        ]
    ) + "\n"
    cleanup = ParagraphTerminatorCleanup(CleanupMessageCollector())

    result = cleanup.ensure_paragraph_termination(source)

    # The MOVE remains one logical statement until the period on its second
    # physical line; the cleanup must not punctuate the first operand early.
    assert "MOVE SPACES TO VMBEFF                                  00030000" in result
    assert "INITIALIZE" not in result
    assert "000300     MOVE SPACES TO VMBEFF." not in result


def test_area_a_paragraph_header_still_terminates_previous_paragraph():
    source = "\n".join(
        [
            "000100 PROCEDURE DIVISION.",
            "000200 210-STORE-EFF.",
            "000300     CONTINUE",
            "000400 220-MOD-EVEF.",
            "000500     CONTINUE.",
        ]
    ) + "\n"
    cleanup = ParagraphTerminatorCleanup(CleanupMessageCollector())

    result = cleanup.ensure_paragraph_termination(source)

    assert "CONTINUE." in result
