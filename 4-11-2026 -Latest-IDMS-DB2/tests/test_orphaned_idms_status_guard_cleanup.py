from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.orphaned_idms_status_guard_cleanup import OrphanedIdmsStatusGuardCleanup


def test_removes_only_obsolete_bind_ready_status_guard():
    source = """000010     IF ERROR-STATUS NOT = '0000'                                 00010000
000020        DISPLAY 'BIND TABLE FAILED '                                00020000
000030        CALL USERABEN                                              00030000
000040     END-IF                                                        00040000
000050     IF ERROR-STATUS NOT = '0000'                                 00050000
000060        DISPLAY 'BUSINESS FAILED '                                  00060000
000070        CONTINUE                                                   00070000
000080     END-IF                                                        00080000
"""
    messages = CleanupMessageCollector()
    output = OrphanedIdmsStatusGuardCleanup(messages).apply(source)
    executable_lines = [line for line in output.splitlines() if "IF ERROR-STATUS" in line]
    assert len(executable_lines) == 1
    assert "00050000" in executable_lines[0]
    assert "CALL USERABEN" not in output
    assert messages.messages
