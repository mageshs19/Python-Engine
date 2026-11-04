from types import SimpleNamespace
from converter.domain.models import SheetMappingRow, DclgenColumn
from converter.repositories.mapping_repository import MappingRepository
from converter.repositories.dclgen_repository import DclgenRepository
from converter.transformers.field_reference_rewriter import FieldReferenceRewriter
from converter.services.name_normalizer import NameNormalizer
from review.checks.chk_32_scope_balance import ScopeBalanceCheck
from review.engine.cobol_view import CobolView


def rewriter(rows):
    maps = {}
    for row in rows:
        maps.setdefault(NameNormalizer.normalize(row.cobol_record_idms), {})[row.cobol_zone.split()[1]] = row.new_db2_field_name.replace("_", "-") + " OF DCLACCOUNT"
    hosts = SimpleNamespace(dclgen_repository=DclgenRepository([
        DclgenColumn(table_name="ACCOUNT", cobol_host_name="DA-POSTED", db2_type="DATE NOT NULL", cobol_picture="X(10)")]))
    obj = FieldReferenceRewriter(MappingRepository(rows), None, hosts)
    obj.context_builder = SimpleNamespace(messages=[], build_reference_maps=lambda: (maps, {}, {}, {}))
    return obj


def row(record="ACCOUNT", field="BALANCE", target="AMOUNT", pic="PIC S9(7)V99 COMP-3", kind="DECIMAL(9,2)"):
    return SheetMappingRow(cobol_record_idms=record, cobol_zone="02 " + field,
        new_db2_field_name=target, idms_pic_clause=pic, new_db2_data_type=kind)


def test_unique_scalar_without_active_record_and_literal_safety():
    obj = rewriter([row()])
    text = "       PROCEDURE DIVISION.\n           MOVE BALANCE TO OUT-AMOUNT.\n           DISPLAY 'BALANCE'.\n"
    output = obj.rewrite(text)
    assert "AMOUNT OF DCLACCOUNT" in output
    assert "DISPLAY 'BALANCE'" in output
    assert obj.rewrite(output) == output


def test_ambiguous_or_local_scalar_is_not_guessed():
    text = "       PROCEDURE DIVISION.\n           MOVE BALANCE TO OUT-AMOUNT.\n"
    assert "MOVE BALANCE" in rewriter([row(), row(record="OTHER", target="OTHER_AMT")]).rewrite(text)
    text = "       DATA DIVISION.\n       WORKING-STORAGE SECTION.\n       01 BALANCE PIC 9(9).\n" + text
    assert "MOVE BALANCE" in rewriter([row()]).rewrite(text)


def test_date_only_qualifies_comparisons_with_proven_date_host():
    obj = rewriter([row(field="DA-OLD", target="DA_POSTED", pic="GROUP", kind="DATE")])
    text = "       PROCEDURE DIVISION.\n           IF DA-OLD < WS-CUTOFF\n              CONTINUE\n           END-IF.\n           MOVE WS-DATE TO DA-OLD.\n"
    output = obj.rewrite(text)
    assert "DA-POSTED OF DCLACCOUNT" in output
    assert "MOVE WS-DATE TO DA-OLD" in output


def test_period_closes_implicit_if_but_later_end_if_is_orphan():
    check = ScopeBalanceCheck()
    text = "       PROCEDURE DIVISION.\n       MAIN.\n           IF A = B\n              DISPLAY 'IF END-IF.'.\n"
    assert check._walk(CobolView(text)) == ([], [])
    orphan, unclosed = check._walk(CobolView(text + "           END-IF.\n"))
    assert len(orphan) == 1 and not unclosed


def test_inline_scopes_comments_sql_and_decimal_points():
    check = ScopeBalanceCheck()
    text = """       PROCEDURE DIVISION.
       MAIN.
      *    IF IGNORED = 1
           IF A = 1.25
              EXEC SQL SELECT A.B INTO :X FROM A END-EXEC
              IF B = 2 CONTINUE END-IF
           END-IF.
"""
    assert check._walk(CobolView(text)) == ([], [])


def test_missing_scope_is_still_reported():
    orphan, unclosed = ScopeBalanceCheck()._walk(CobolView("       MAIN.\n           IF A = B\n              CONTINUE\n"))
    assert not orphan and unclosed == [("MAIN", "IF", 1)]


def test_end_of_set_review_does_not_require_eoc_for_singleton_failure_test():
    from review.checks.chk_29_lr_status_field_replacement import LRStatusFieldReplacementCheck
    check = LRStatusFieldReplacementCheck()
    assert not check._requires_end_of_set("           IF LR-STATUS NOT = 'LR-FOUND'\n")
    assert check._requires_end_of_set("           IF LR-STATUS = 'NO-MORE-ROW'\n")


def test_stale_status_warning_removed_only_after_last_executable_reference():
    from converter.services.final_generated_output_service import FinalGeneratedOutputService
    warning = "000100*DB2 WARNING: ERROR-STATUS is undefined after copybook removal but\n000200*shares a line with live operands; left for manual review.\n"
    clean = FinalGeneratedOutputService._remove_resolved_status_warning
    assert "DB2 WARNING" not in clean(warning + "           CONTINUE.\n")
    assert clean(warning + "           DISPLAY ERROR-STATUS.\n").startswith(warning)


def test_conflicting_columns_for_same_owner_are_not_guessed():
    obj = rewriter([row(), row(target="OTHER_AMOUNT")])
    assert "MOVE BALANCE" in obj.rewrite("       PROCEDURE DIVISION.\n           MOVE BALANCE TO OUT-AMOUNT.\n")


def test_date_comparison_pass_runs_again_after_host_qualification():
    from converter.composers.db2_date_comparison_composer import Db2DateComparisonComposer
    source = """000100 PROCEDURE DIVISION.
000200 MAIN.
000300     IF WS-CUTOFF < DA-CREVTPD-479EVEF
000400       OF DCLDZEVEFTV
000500        CONTINUE
000600     END-IF.
"""
    composer = Db2DateComparisonComposer()
    result = composer.compose(source)
    assert "realigned 1 DATE host" in composer.messages[-1]
    assert "IF WS-CUTOFF < HELP-DA-CREVTPD-479EVEF" in result
    assert composer.compose(result) == result
