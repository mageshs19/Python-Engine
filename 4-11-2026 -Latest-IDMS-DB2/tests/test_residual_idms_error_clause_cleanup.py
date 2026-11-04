from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.residual_idms_error_clause_cleanup import ResidualIdmsErrorClauseCleanup


def test_removes_known_idms_status_handler_pair():
    collector = CleanupMessageCollector()
    cleanup = ResidualIdmsErrorClauseCleanup(collector)
    source = """       BIND VMBEFF
       ON ANY-ERROR-STATUS
         PERFORM IDMS-STATUS.
       PERFORM READ-MUTATIES.
"""
    result = cleanup.apply(source)
    assert "ON ANY-ERROR-STATUS" not in result
    assert "PERFORM IDMS-STATUS" not in result
    assert "PERFORM READ-MUTATIES." in result
    assert any("removed 1 orphaned IDMS" in message for message in collector.messages)


def test_removes_orphaned_clause_when_prior_cleanup_reports_removed_handler():
    collector = CleanupMessageCollector()
    cleanup = ResidualIdmsErrorClauseCleanup(collector)
    source = """*DB2 WARNING: ERROR-STATUS is undefined after copybook removal
       ON ANY-ERROR-STATUS

       PERFORM READ-MUTATIES.
"""
    result = cleanup.apply(source)
    assert "ON ANY-ERROR-STATUS" not in result
    assert "ERROR-STATUS is undefined after copybook removal" not in result
    assert "PERFORM READ-MUTATIES." in result


def test_unknown_handler_is_preserved_and_reported():
    collector = CleanupMessageCollector()
    cleanup = ResidualIdmsErrorClauseCleanup(collector)
    source = """       ON ANY-ERROR-STATUS
         DISPLAY 'UNEXPECTED HANDLER'.
"""
    result = cleanup.apply(source)
    assert "ON ANY-ERROR-STATUS" not in result
    assert "DISPLAY 'UNEXPECTED HANDLER'." in result
    assert any("unrecognized handler" in message for message in collector.messages)
