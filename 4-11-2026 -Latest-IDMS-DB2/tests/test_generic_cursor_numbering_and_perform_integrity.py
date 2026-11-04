from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
from rules.cursor_rules import cursor_paragraph_number


def test_cursor_numbering_is_central_and_scales_beyond_three_cursors():
    assert [cursor_paragraph_number(1, op) for op in ("open", "fetch", "close")] == [2100, 2200, 2300]
    assert [cursor_paragraph_number(2, op) for op in ("open", "fetch", "close")] == [3100, 3200, 3300]
    assert [cursor_paragraph_number(3, op) for op in ("open", "fetch", "close")] == [4100, 4200, 4300]
    assert [cursor_paragraph_number(4, op) for op in ("open", "fetch", "close")] == [5100, 5200, 5300]


def test_cursor_name_resolver_uses_same_numbers_for_all_paragraph_names():
    resolver = CursorNameResolver()
    first = resolver.cursor_spec(1, "DZEVEFTV")
    second = resolver.cursor_spec(2, "DZBEFFTV")
    assert (first["open_paragraph"], first["fetch_paragraph"], first["close_paragraph"]) == (
        "2100-OPEN-DZEVEFC1", "2200-FETCH-DZEVEFC1", "2300-CLOSE-DZEVEFC1"
    )
    assert (second["open_paragraph"], second["fetch_paragraph"], second["close_paragraph"]) == (
        "3100-OPEN-DZBEFFC1", "3200-FETCH-DZBEFFC1", "3300-CLOSE-DZBEFFC1"
    )


def test_release_validator_catches_stale_perform_after_renumbering():
    text = """       PROCEDURE DIVISION.
           PERFORM 2100-OPEN-C1.
           STOP RUN.
       2100-OPEN-C1.
           MOVE 2100 TO SQL-LOCATION.
           EXEC SQL OPEN C1 END-EXEC.
       2200-FETCH-C1.
           MOVE 2200 TO SQL-LOCATION.
           EXEC SQL FETCH C1 END-EXEC.
       2300-CLOSE-C1.
           MOVE 2300 TO SQL-LOCATION.
           EXEC SQL CLOSE C1 END-EXEC.
"""
    issues = validate_generated_cobol(text)
    assert not [issue for issue in issues if issue.code in {
        "PERFORM_CURSOR_TARGET_MISSING", "INCOMPLETE_CURSOR_PARAGRAPHS",
        "CURSOR_NUMBERING_MISMATCH", "CURSOR_SQL_LOCATION_MISMATCH",
    }]

    stale = text.replace("PERFORM 2100-OPEN-C1", "PERFORM 710-OPEN-C1")
    stale_issues = validate_generated_cobol(stale)
    assert any(issue.code == "PERFORM_CURSOR_TARGET_MISSING" for issue in stale_issues)


def test_release_validator_catches_mismatched_sql_location():
    text = """       PROCEDURE DIVISION.
           PERFORM 2100-OPEN-C1.
       2100-OPEN-C1.
           MOVE 710 TO SQL-LOCATION.
       2200-FETCH-C1.
           MOVE 2200 TO SQL-LOCATION.
       2300-CLOSE-C1.
           MOVE 2300 TO SQL-LOCATION.
"""
    issues = validate_generated_cobol(text)
    assert any(issue.code == "CURSOR_SQL_LOCATION_MISMATCH" for issue in issues)


def test_span_loop_planner_uses_four_digit_cursor_offsets_and_keeps_legacy_compatibility():
    from converter.composers.cursor_flow.span_loop_plan import SpanLoopPlanBuilder
    from converter.composers.cursor_flow.loop_shape import LoopShapeScanner

    lines = [
        "PERFORM BEHANDELING THRU BEHANDELING-EXIT UNTIL SQLCODE = 100.",
        "PERFORM 2100-OPEN-C1.",
        "2100-OPEN-C1.",
        "2200-FETCH-C1.",
        "2300-CLOSE-C1.",
    ]
    scanner = LoopShapeScanner()
    shapes = scanner.scan(lines)
    plans = SpanLoopPlanBuilder(scanner=scanner).build(lines, shapes)
    assert len(plans) == 1
    assert plans[0].fetch_paragraph == "2200-FETCH-C1"
    assert plans[0].close_paragraph == "2300-CLOSE-C1"

    legacy_lines = [
        "PERFORM BEHANDELING THRU BEHANDELING-EXIT UNTIL SQLCODE = 100.",
        "PERFORM 710-OPEN-C1.",
        "710-OPEN-C1.",
        "720-FETCH-C1.",
        "730-CLOSE-C1.",
    ]
    legacy_shapes = scanner.scan(legacy_lines)
    legacy_plans = SpanLoopPlanBuilder(scanner=scanner).build(legacy_lines, legacy_shapes)
    assert len(legacy_plans) == 1
    assert legacy_plans[0].fetch_paragraph == "720-FETCH-C1"
    assert legacy_plans[0].close_paragraph == "730-CLOSE-C1"


def test_release_validator_rejects_reversed_perform_thru_range():
    text = """       PROCEDURE DIVISION.
           PERFORM FIRST-PARA THRU LAST-PARA.
           STOP RUN.
       LAST-PARA.
           CONTINUE.
       FIRST-PARA.
           CONTINUE.
"""
    issues = validate_generated_cobol(text)
    assert any(issue.code == "PERFORM_THRU_REVERSED" for issue in issues)


def test_release_validator_rejects_business_thru_range_crossing_cursor_paragraphs():
    text = """       PROCEDURE DIVISION.
           PERFORM BUSINESS-START THRU BUSINESS-END.
           STOP RUN.
       BUSINESS-START.
           CONTINUE.
       2100-OPEN-C1.
           MOVE 2100 TO SQL-LOCATION.
       2200-FETCH-C1.
           MOVE 2200 TO SQL-LOCATION.
       2300-CLOSE-C1.
           MOVE 2300 TO SQL-LOCATION.
       BUSINESS-END.
           CONTINUE.
"""
    issues = validate_generated_cobol(text)
    assert any(issue.code == "PERFORM_THRU_CROSSES_CURSOR_PARAGRAPH" for issue in issues)


def test_release_validator_ignores_terminators_when_indexing_paragraphs():
    text = """       PROCEDURE DIVISION.
           PERFORM BUSINESS-START THRU BUSINESS-END.
           STOP RUN.
       BUSINESS-START.
           IF FLAG = 'Y'
               CONTINUE
           END-IF.
       BUSINESS-END.
           CONTINUE.
"""
    issues = validate_generated_cobol(text)
    assert not any(issue.code in {"PERFORM_THRU_REVERSED", "PERFORM_THRU_CROSSES_CURSOR_PARAGRAPH"} for issue in issues)


def test_release_validator_checks_multiline_perform_thru_ranges():
    text = """       PROCEDURE DIVISION.
           PERFORM
             LATER-PARA THRU
             EARLIER-PARA.
           STOP RUN.
       EARLIER-PARA.
           CONTINUE.
       LATER-PARA.
           CONTINUE.
"""
    issues = validate_generated_cobol(text)
    assert any(issue.code == "PERFORM_THRU_REVERSED" for issue in issues)


def test_release_validator_rejects_duplicate_business_paragraph_labels():
    text = """       PROCEDURE DIVISION.
           PERFORM PROCESS-ROW.
           STOP RUN.
       PROCESS-ROW.
           CONTINUE.
       PROCESS-ROW.
           CONTINUE.
"""
    issues = validate_generated_cobol(text)
    assert any(issue.code == "DUPLICATE_PARAGRAPH_LABEL" for issue in issues)


def test_release_validator_enforces_global_cursor_identity_numbering():
    text = """       PROCEDURE DIVISION.
           PERFORM 2100-OPEN-C1.
           PERFORM 3100-OPEN-C2.
           STOP RUN.
       2100-OPEN-C1.
           MOVE 2100 TO SQL-LOCATION.
           EXEC SQL OPEN C1 END-EXEC.
       2200-FETCH-C1.
           MOVE 2200 TO SQL-LOCATION.
           EXEC SQL FETCH C1 END-EXEC.
       2300-CLOSE-C1.
           MOVE 2300 TO SQL-LOCATION.
           EXEC SQL CLOSE C1 END-EXEC.
       3100-OPEN-C2.
           MOVE 3100 TO SQL-LOCATION.
           EXEC SQL OPEN C2 END-EXEC.
       3200-FETCH-C2.
           MOVE 3200 TO SQL-LOCATION.
           EXEC SQL FETCH C2 END-EXEC.
       3300-CLOSE-C2.
           MOVE 3300 TO SQL-LOCATION.
           EXEC SQL CLOSE C2 END-EXEC.
"""
    issues = validate_generated_cobol(text)
    assert not [issue for issue in issues if issue.code in {
        "CURSOR_IDENTITY_NUMBERING_MISMATCH", "CURSOR_NUMBERING_MISMATCH",
        "CURSOR_SQL_LOCATION_MISMATCH", "INCOMPLETE_CURSOR_PARAGRAPHS",
    }]

    incorrect = text.replace("3100-OPEN-C2", "2400-OPEN-C2")
    incorrect = incorrect.replace("3200-FETCH-C2", "2500-FETCH-C2")
    incorrect = incorrect.replace("3300-CLOSE-C2", "2600-CLOSE-C2")
    incorrect = incorrect.replace("PERFORM 3100-OPEN-C2", "PERFORM 2400-OPEN-C2")
    incorrect = incorrect.replace("MOVE 3100 TO SQL-LOCATION", "MOVE 2400 TO SQL-LOCATION")
    incorrect = incorrect.replace("MOVE 3200 TO SQL-LOCATION", "MOVE 2500 TO SQL-LOCATION")
    incorrect = incorrect.replace("MOVE 3300 TO SQL-LOCATION", "MOVE 2600 TO SQL-LOCATION")
    bad_issues = validate_generated_cobol(incorrect)
    assert any(issue.code == "CURSOR_IDENTITY_NUMBERING_MISMATCH" for issue in bad_issues)


def test_cursor_four_and_later_continue_in_three_hundred_number_blocks():
    assert [cursor_paragraph_number(4, op) for op in ("open", "fetch", "close")] == [5100, 5200, 5300]
    assert [cursor_paragraph_number(5, op) for op in ("open", "fetch", "close")] == [6100, 6200, 6300]


def test_cursor_paragraph_generator_emits_standard_multi_cursor_output():
    from converter.generators.cursor_paragraph_generator import CursorParagraphGenerator
    from converter.generators.sql_error_generator import SqlErrorGenerator

    resolver = CursorNameResolver()
    specs = []
    for order, table in enumerate(("DZEVEFTV", "DZBEFFTV", "DZBFASTV"), start=1):
        spec = resolver.cursor_spec(order, table)
        spec.update({
            "host_variables": [],
            "where_conditions": [],
            "table_name": table,
            "is_parent_cursor": order == 1,
        })
        specs.append(spec)

    generator = CursorParagraphGenerator(
        db2_infrastructure_generator=None,
        host_variable_resolver=None,
        sql_error_generator=SqlErrorGenerator(),
    )
    generated = generator.paragraph_block(specs, "SQLERROR")

    expected = (
        "2100-OPEN-DZEVEFC1.", "2200-FETCH-DZEVEFC1.", "2300-CLOSE-DZEVEFC1.",
        "3100-OPEN-DZBEFFC1.", "3200-FETCH-DZBEFFC1.", "3300-CLOSE-DZBEFFC1.",
        "4100-OPEN-DZBFASC1.", "4200-FETCH-DZBFASC1.", "4300-CLOSE-DZBFASC1.",
    )
    for label in expected:
        assert label in generated
    for number in (2100, 2200, 2300, 3100, 3200, 3300, 4100, 4200, 4300):
        assert f"MOVE {number}    TO SQL-LOCATION" in generated
    assert "WHEN 100" in generated
    assert "PERFORM SQLERROR" in generated
    generated_issues = validate_generated_cobol("       PROCEDURE DIVISION.\n" + generated)
    assert not [issue for issue in generated_issues if issue.code in {
        "CURSOR_IDENTITY_NUMBERING_MISMATCH", "CURSOR_NUMBERING_MISMATCH",
        "CURSOR_SQL_LOCATION_MISMATCH", "INCOMPLETE_CURSOR_PARAGRAPHS",
        "CURSOR_SQLCODE_EVALUATE_MISSING", "CURSOR_SQLCODE_EVALUATE_UNCLOSED",
        "CURSOR_SQLCODE_WHEN_OTHER_MISSING", "CURSOR_SQLERROR_PERFORM_MISSING",
        "CURSOR_FETCH_EOC_BRANCH_MISSING", "CURSOR_NON_FETCH_100_BRANCH",
    }]


def test_release_validator_requires_shared_sqlerror_routing_at_every_cursor_level():
    source = """       PROCEDURE DIVISION.
           PERFORM 2100-OPEN-C1.
           PERFORM 2200-FETCH-C1.
           PERFORM 2300-CLOSE-C1.
           PERFORM 3100-OPEN-C2.
           PERFORM 2500-FETCH-C2.
           PERFORM 2600-CLOSE-C2.
       2100-OPEN-C1.
           MOVE 2100 TO SQL-LOCATION.
           EXEC SQL OPEN C1 END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO CONTINUE
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
       2200-FETCH-C1.
           MOVE 2200 TO SQL-LOCATION.
           EXEC SQL FETCH C1 INTO :A END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO CONTINUE
             WHEN 100 SET C1-EOC TO TRUE
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
       2300-CLOSE-C1.
           MOVE 2300 TO SQL-LOCATION.
           EXEC SQL CLOSE C1 END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO CONTINUE
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
       3100-OPEN-C2.
           MOVE 3100 TO SQL-LOCATION.
           EXEC SQL OPEN C2 END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO CONTINUE
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
       3200-FETCH-C2.
           MOVE 3200 TO SQL-LOCATION.
           EXEC SQL FETCH C2 INTO :B END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO CONTINUE
             WHEN 100 SET C2-EOC TO TRUE
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
       3300-CLOSE-C2.
           MOVE 3300 TO SQL-LOCATION.
           EXEC SQL CLOSE C2 END-EXEC.
           EVALUATE SQLCODE
             WHEN ZERO CONTINUE
             WHEN OTHER PERFORM SQLERROR
           END-EVALUATE.
"""
    assert not [issue for issue in validate_generated_cobol(source) if issue.code.startswith("CURSOR_")]

    # A child cursor must not lose error routing merely because it is a
    # different level; and +100 must not be treated as EOC on CLOSE.
    broken = source.replace(
        "WHEN OTHER PERFORM SQLERROR\n           END-EVALUATE.\n       3300-CLOSE-C2.",
        "WHEN OTHER CONTINUE\n           END-EVALUATE.\n       3300-CLOSE-C2.",
    ).replace(
        "3300-CLOSE-C2.\n           MOVE 3300 TO SQL-LOCATION.\n           EXEC SQL CLOSE C2 END-EXEC.\n           EVALUATE SQLCODE\n             WHEN ZERO CONTINUE\n             WHEN OTHER PERFORM SQLERROR",
        "3300-CLOSE-C2.\n           MOVE 3300 TO SQL-LOCATION.\n           EXEC SQL CLOSE C2 END-EXEC.\n           EVALUATE SQLCODE\n             WHEN ZERO CONTINUE\n             WHEN 100 CONTINUE\n             WHEN OTHER PERFORM SQLERROR",
    )
    codes = {issue.code for issue in validate_generated_cobol(broken)}
    assert "CURSOR_SQLERROR_PERFORM_MISSING" in codes
    assert "CURSOR_NON_FETCH_100_BRANCH" in codes


def test_access_error_policy_distinguishes_cursor_singleton_and_lr_outcomes():
    from converter.analyzers.access_error_policy import AccessPattern, classify_access, policy_for

    assert classify_access(cursor_operation="fetch") is AccessPattern.CURSOR_FETCH
    assert policy_for(AccessPattern.CURSOR_FETCH).sqlcode_100 == "set_this_cursor_eoc_only"
    assert classify_access(cursor_operation="open") is AccessPattern.CURSOR_OPEN
    assert policy_for(AccessPattern.CURSOR_OPEN).sqlcode_100 == "unexpected_result"
    assert classify_access(sql="SELECT A INTO :WS-A FROM T WHERE ID = :WS-ID") is AccessPattern.SINGLETON_SELECT
    assert policy_for(AccessPattern.SINGLETON_SELECT).sqlcode_100 == "apply_original_not_found_behavior"
    assert classify_access(source_statement="OBTAIN FIRST EMPLOYEE WITHIN DEPT-EMP") is AccessPattern.LR_OBTAIN_FIRST
    assert classify_access(source_statement="OBTAIN NEXT EMPLOYEE WITHIN DEPT-EMP") is AccessPattern.LR_OBTAIN_NEXT
    assert classify_access(sql="SELECT A FROM T") is AccessPattern.UNKNOWN
