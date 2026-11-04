from types import SimpleNamespace

from review.checks.chk_15_nested_cursor_processing import NestedCursorProcessingCheck
from review.checks.chk_25_copybook_and_record_usage import CopybookAndRecordUsageCheck
from review.engine.cobol_view import CobolView
from review.engine.context import ReviewContext


def _mapping(record, source, target):
    return SimpleNamespace(
        cobol_record_idms=record,
        cobol_zone=f"02 {source}",
        reference_field_name_copybook="",
        new_db2_field_name=target,
        cross_application_db2_field_name="",
    )


def test_child_early_stop_is_not_inferred_from_unrelated_generated_y_flag():
    ctx = ReviewContext(source_cobol="""
       PROCEDURE DIVISION.
       PARENT.
           PERFORM CHILD UNTIL ERROR-STATUS NOT = '0000'.
    """)
    assert not NestedCursorProcessingCheck._source_requires_business_early_stop(ctx)


def test_compound_source_traversal_requires_business_early_stop():
    ctx = ReviewContext(source_cobol="""
       PROCEDURE DIVISION.
       PARENT.
           PERFORM UNTIL LR-STATUS = 'NO-MORE-ROW'
                      OR CT-EVENT = '0092'
              CONTINUE
           END-PERFORM.
    """)
    assert NestedCursorProcessingCheck._source_requires_business_early_stop(ctx)


def test_unmaterialised_mapped_legacy_field_is_reported():
    ctx = ReviewContext(
        source_cobol="""
       PROCEDURE DIVISION.
       BUSINESS.
           MOVE AM-CN-STOCK TO OUT-AMOUNT.
        """,
        sheet_mapping_rows=[_mapping("VMBEFF", "AM-CN-STOCK", "AM_CNSTK_479BEFF")],
    )
    view = CobolView("""
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 OUT-AMOUNT PIC 9(9).
       PROCEDURE DIVISION.
       BUSINESS.
           MOVE AM-CN-STOCK TO OUT-AMOUNT.
    """)
    assert CopybookAndRecordUsageCheck._unmaterialised_legacy_fields(ctx, view, {"OUT-AMOUNT"}) == [
        "AM-CN-STOCK (mapped from VMBEFF)"
    ]


def test_materialised_or_declared_legacy_name_is_not_reported():
    ctx = ReviewContext(
        source_cobol="""
       PROCEDURE DIVISION.
       BUSINESS.
           MOVE AM-CN-STOCK TO OUT-AMOUNT.
        """,
        sheet_mapping_rows=[_mapping("VMBEFF", "AM-CN-STOCK", "AM_CNSTK_479BEFF")],
    )
    view = CobolView("""
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 AM-CN-STOCK PIC 9(9).
       01 OUT-AMOUNT PIC 9(9).
       PROCEDURE DIVISION.
       BUSINESS.
           MOVE AM-CN-STOCK TO OUT-AMOUNT.
    """)
    assert CopybookAndRecordUsageCheck._unmaterialised_legacy_fields(
        ctx, view, {"AM-CN-STOCK", "OUT-AMOUNT"}
    ) == []


def test_ambiguous_legacy_field_is_not_guessed():
    ctx = ReviewContext(
        source_cobol="""
       PROCEDURE DIVISION.
       BUSINESS.
           MOVE STATUS-FIELD TO OUT-FIELD.
        """,
        sheet_mapping_rows=[
            _mapping("REC-A", "STATUS-FIELD", "STATUS_A"),
            _mapping("REC-B", "STATUS-FIELD", "STATUS_B"),
        ],
    )
    view = CobolView("""
       PROCEDURE DIVISION.
       BUSINESS.
           MOVE STATUS-FIELD TO OUT-FIELD.
    """)
    assert CopybookAndRecordUsageCheck._unmaterialised_legacy_fields(ctx, view, set()) == []


def test_declared_materialised_idms_record_group_is_not_residual_qualifier():
    # A generated local record may intentionally retain the legacy group name
    # to preserve business layout. Its qualification is local COBOL storage,
    # not an executable IDMS database reference.
    declared = {"VMBFAS"}
    qualifiers = {("AM-CNS-FORM-AS", "VMBFAS")}
    records = {"VMBFAS"}
    residual = sorted(
        f"{field} OF {group}"
        for field, group in qualifiers
        if group in records and group not in declared
    )
    assert residual == []


def test_undeclared_legacy_record_group_still_counts_as_residual():
    declared = set()
    qualifiers = {("NM-ID-FF", "FFRECAB")}
    records = {"FFRECAB"}
    residual = sorted(
        f"{field} OF {group}"
        for field, group in qualifiers
        if group in records and group not in declared
    )
    assert residual == ["NM-ID-FF OF FFRECAB"]
