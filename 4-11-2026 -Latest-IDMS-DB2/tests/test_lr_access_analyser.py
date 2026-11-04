from converter.analyzers.lr_access.lr_access_analyser import LrAccessAnalyser


def test_classifies_inline_bounded_search_without_program_specific_names():
    source = """000100 IDENTIFICATION DIVISION.
000200 PROCEDURE DIVISION.
000300     OBTAIN FIRST RECORD-A WITHIN SET-A.
000400     PERFORM UNTIL LR-STATUS = 'NO-MORE-RECORD-A'
000500                OR EVENT-CODE OF RECORD-A = '0092'
000600        OBTAIN NEXT RECORD-A WITHIN SET-A.
000700     END-PERFORM.
000800     GOBACK.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {
        "RECORD-A": "EVENT-CODE OF RECORD-A = '0092'"
    }
    assert any("rendering remains gated" in message for message in analyser.messages)


def test_does_not_classify_status_only_sweep_as_bounded_search():
    source = """000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     PERFORM UNTIL ERROR-STATUS NOT = '0000'
000300        OBTAIN NEXT RECORD-A WITHIN SET-A.
000400     END-PERFORM.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}


def test_ambiguous_multiple_sites_for_same_record_are_omitted():
    source = """000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     PERFORM UNTIL LR-STATUS = 'NO-MORE-RECORD-A'
000300                OR EVENT-CODE OF RECORD-A = '0092'
000400        OBTAIN NEXT RECORD-A WITHIN SET-A.
000500     END-PERFORM.
000600     OBTAIN FIRST RECORD-A WITHIN SET-A.
000700     PERFORM UNTIL LR-STATUS = 'NO-MORE-RECORD-A'
000800                OR EVENT-CODE OF RECORD-A = '0093'
000900        OBTAIN NEXT RECORD-A WITHIN SET-A.
001000     END-PERFORM.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any("multiple bounded-search sites" in message for message in analyser.messages)


def test_refuses_to_classify_loop_with_business_work():
    source = """000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     PERFORM UNTIL LR-STATUS = 'NO-MORE-RECORD-A'
000300                OR EVENT-CODE OF RECORD-A = '0092'
000400        MOVE FIELD-A TO FIELD-B
000500        OBTAIN NEXT RECORD-A WITHIN SET-A.
000600     END-PERFORM.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}


def test_real_vm4bd310_source_is_classified_without_hardcoded_program_rule():
    from pathlib import Path

    source_path = Path(__file__).resolve().parents[1] / "mainframe/workspace/Program/VM4BD310.cbl"
    analyser = LrAccessAnalyser()
    result = analyser.bounded_searches(source_path.read_text(encoding="utf-8", errors="replace"))
    assert result.get("VMBEVEF") == "CT-EVENT OF VMBEVEF = '0092'"


def test_paragraph_and_thru_lrf_loops_are_reported_but_never_classified_for_rewrite():
    source = """000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     PERFORM PROCESS-ROW THRU PROCESS-ROW-EXIT UNTIL DB-END-OF-SET.
000300     OBTAIN NEXT RECORD-A WITHIN SET-A.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any("paragraph-driven" in message and "THRU" in message for message in analyser.messages)


def test_nested_inline_loop_is_not_misclassified_from_partial_scope():
    source = """000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     PERFORM UNTIL LR-STATUS = 'NO-MORE-RECORD-A'
000300        PERFORM UNTIL INNER-DONE = 'Y'
000400           CONTINUE
000500        END-PERFORM
000600        OBTAIN NEXT RECORD-A WITHIN SET-A.
000700     END-PERFORM.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any("nested PERFORM UNTIL" in message for message in analyser.messages)


def test_numeric_paragraph_loop_with_lrf_access_is_reported_even_when_until_is_eof():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 200-VERWERK-INFIL UNTIL EOF.
000300     GOBACK.
000400 200-VERWERK-INFIL.
000500     OBTAIN FIRST RECORD-A WITHIN SET-A.
000600     PERFORM 210-READ-NEXT UNTIL ERROR-STATUS NOT = '0000'.
000700 210-READ-NEXT.
000800     OBTAIN NEXT RECORD-A WITHIN SET-A.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 200-VERWERK-INFIL" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_numeric_paragraph_through_loop_is_reported_without_rewrite():
    source = """000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     PERFORM 100-START THROUGH 200-END UNTIL EOF.
000300 100-START.
000400     OBTAIN NEXT RECORD-A WITHIN SET-A.
000500 200-END.
000600     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any("PERFORM 100-START THRU 200-END" in message for message in analyser.messages)


def test_outer_eof_loop_follows_nested_perform_calls_to_find_lrf_access():
    source = """000100     PERFORM 200-INPUT-ROW UNTIL EOF.
000200 200-INPUT-ROW.
000300     PERFORM 300-PROCESS-ROW.
000400 300-PROCESS-ROW.
000500     PERFORM 400-READ-CHILD.
000600 400-READ-CHILD.
000700     OBTAIN FIRST CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any("PERFORM 200-INPUT-ROW" in message for message in analyser.messages)


def test_refuses_bounded_search_when_store_precedes_next_access():
    source = """000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     PERFORM UNTIL LR-STATUS = 'NO-MORE-RECORD-A'
000300                OR EVENT-CODE OF RECORD-A = '0092'
000400        STORE AUDIT-REC.
000500        OBTAIN NEXT RECORD-A WITHIN SET-A.
000600     END-PERFORM.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}


def test_vmdz1526_lrf_intermediate_reports_outer_eof_loop_that_calls_lrf_work():
    from pathlib import Path

    source_path = (
        Path(__file__).resolve().parents[1]
        / "mainframe/workspace/Output/LRF/VMDZ1526_lrf_to_idms.cbl"
    )
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source_path.read_text(encoding="utf-8", errors="replace")) == {}
    assert any(
        "PERFORM 200-VERWERK-INFIL" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_paragraph_scanner_keeps_same_line_statement_after_paragraph_label():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-READ-ROW UNTIL EOF.
000300 100-READ-ROW. OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-READ-ROW" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_paragraph_scanner_does_not_treat_program_id_as_a_paragraph():
    source = """000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID. SAMPLE-PROGRAM.
000300 PROCEDURE DIVISION.
000400     PERFORM 100-READ-ROW UNTIL EOF.
000500 100-READ-ROW. OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    paragraphs = LrAccessAnalyser._paragraph_bodies(
        LrAccessAnalyser._logical_text(source)
    )
    assert "PROGRAM-ID" not in paragraphs
    assert "100-READ-ROW" in paragraphs
    assert "OBTAIN NEXT CHILD-REC" in paragraphs["100-READ-ROW"]


def test_paragraph_scanner_does_not_split_on_end_exec_terminator():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-READ-ROW UNTIL EOF.
000300 100-READ-ROW.
000400     EXEC SQL
000500       SELECT COL-A FROM TABLE-A
000600     END-EXEC.
000700     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any("PERFORM 100-READ-ROW" in message for message in analyser.messages)


def test_paragraph_scanner_ignores_lrf_and_perform_words_inside_literals():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-LOG-ROW UNTIL EOF.
000300 100-LOG-ROW.
000400     DISPLAY 'OBTAIN NEXT CHILD-REC; PERFORM 900-LRF'.
000500     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert not any("paragraph-driven" in message for message in analyser.messages)


def test_inline_comment_words_do_not_create_lrf_access_or_paragraph_calls():
    source = """000100 PROCEDURE DIVISION.
000200     DISPLAY 'normal' *> OBTAIN NEXT CHILD-REC; PERFORM 900-LRF.
000300     PERFORM 100-LOG-ROW UNTIL EOF.
000400 100-LOG-ROW.
000500     CONTINUE. *> OBTAIN NEXT CHILD-REC.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert not any("paragraph-driven" in message for message in analyser.messages)


def test_inline_comment_marker_inside_quoted_literal_is_preserved():
    source = """000100 PROCEDURE DIVISION.
000200     DISPLAY 'literal *> OBTAIN NEXT CHILD-REC'.
000300     GOBACK.
"""
    logical = LrAccessAnalyser._logical_text(source)
    assert "LITERAL *> OBTAIN NEXT CHILD-REC" in logical
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert analyser.messages == []


def test_inline_comment_after_real_lrf_statement_preserves_statement():
    source = """000100 PROCEDURE DIVISION.
000200     OBTAIN FIRST RECORD-A WITHIN SET-A. *> fake PERFORM 900-X
000300     PERFORM UNTIL LR-STATUS = 'NO-MORE-RECORD-A'
000400        OBTAIN NEXT RECORD-A WITHIN SET-A. *> fake STORE ROW-A
000500     END-PERFORM.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert not any("paragraph-driven" in message for message in analyser.messages)


def test_finite_perform_through_with_lrf_access_is_reported_for_review():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-START THRU 200-END.
000300 100-START.
000400     PERFORM 150-READ-ROW.
000500 150-READ-ROW.
000600     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
000700 200-END.
000800     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-START THRU 200-END" in message and "retained" in message
        for message in analyser.messages
    )


def test_through_in_comment_does_not_trigger_paragraph_diagnostic():
    source = """000100 PROCEDURE DIVISION.
000200     CONTINUE. *> PERFORM 100-START THROUGH 200-END.
000300 100-START.
000400     CONTINUE.
000500 200-END.
000600     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert not any("paragraph-driven" in message for message in analyser.messages)


def test_paragraph_modify_without_obtain_is_still_reported_for_review():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-UPDATE-ROW UNTIL EOF.
000300 100-UPDATE-ROW.
000400     MODIFY CHILD-REC.
000500     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-UPDATE-ROW" in message and "paragraph-driven" in message
        for message in analyser.messages
    )


def test_inline_perform_varying_is_not_misread_as_paragraph_call():
    source = """000100 PROCEDURE DIVISION.
000200     OBTAIN FIRST RECORD-A WITHIN SET-A.
000300     PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > 3
000400         OBTAIN NEXT RECORD-A WITHIN SET-A
000500     END-PERFORM.
000600     GOBACK.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "inline PERFORM VARYING/TEST/TIMES loop contains LRF work" in message
        and "retained for review" in message
        for message in analyser.messages
    )


def test_unresolved_thru_endpoint_is_explicitly_flagged_when_lrf_is_present():
    source = """000100 PROCEDURE DIVISION.
000200     OBTAIN FIRST RECORD-A WITHIN SET-A.
000300     PERFORM 100-START THRU 900-MISSING.
000400 100-START.
000500     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-START THRU 900-MISSING" in message
        and "unresolved or ambiguous paragraph endpoint" in message
        and "retained for review" in message
        for message in analyser.messages
    )


def test_reversed_thru_range_is_explicitly_flagged():
    source = """000100 PROCEDURE DIVISION.
000200     OBTAIN FIRST RECORD-A WITHIN SET-A.
000300     PERFORM 200-END THRU 100-START.
000400 100-START.
000500     OBTAIN NEXT RECORD-A WITHIN SET-A.
000600 200-END.
000700     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 200-END THRU 100-START" in message
        and "reversed paragraph range" in message
        for message in analyser.messages
    )


def test_inline_perform_times_is_not_misread_as_paragraph_call():
    source = """000100 PROCEDURE DIVISION.
000200     OBTAIN FIRST RECORD-A WITHIN SET-A.
000300     PERFORM 3 TIMES
000400         OBTAIN NEXT RECORD-A WITHIN SET-A
000500     END-PERFORM.
000600     GOBACK.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any("inline PERFORM VARYING/TEST/TIMES loop contains LRF work" in message
               for message in analyser.messages)
    assert not any("PERFORM 3" in message for message in analyser.messages)


def test_paragraph_erase_without_obtain_is_reported_for_review():
    """ERASE-only paragraph flows are LRF work even without OBTAIN/NEXT."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-DELETE-ROW UNTIL EOF.
000300 100-DELETE-ROW.
000400     ERASE CHILD-REC.
000500     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-DELETE-ROW" in message and "paragraph-driven" in message
        for message in analyser.messages
    )


def test_erase_in_literal_does_not_trigger_paragraph_diagnostic():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-LOG-ROW UNTIL EOF.
000300 100-LOG-ROW.
000400     DISPLAY 'ERASE CHILD-REC'.
000500     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert not any("paragraph-driven" in message for message in analyser.messages)


def test_fixed_format_continuation_does_not_merge_perform_and_paragraph_tokens():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM
000300-    100-READ-ROW UNTIL EOF.
000400 100-READ-ROW.
000500     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-READ-ROW" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_nested_unresolved_thru_range_keeps_enclosing_lrf_flow_for_review():
    """An unresolved nested THRU must not be reduced to its first paragraph."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-OUTER UNTIL EOF.
000300 100-OUTER.
000400     PERFORM 110-START THRU 190-MISSING.
000500 110-START.
000600     CONTINUE.
000700 150-READ-ROW.
000800     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "nested PERFORM 110-START THRU 190-MISSING" in message
        and "unresolved or ambiguous paragraph endpoint" in message
        for message in analyser.messages
    )
    assert any(
        "PERFORM 100-OUTER" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_nested_unresolved_paragraph_call_is_not_silently_ignored():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-OUTER UNTIL EOF.
000300 100-OUTER.
000400     PERFORM 190-MISSING-PARA.
000500 150-READ-ROW.
000600     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "nested PERFORM 190-MISSING-PARA cannot be resolved" in message
        for message in analyser.messages
    )
    assert any(
        "PERFORM 100-OUTER" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_inline_varying_loop_following_paragraph_call_detects_indirect_lrf_access():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 5
000300         PERFORM 300-READ-CHILD
000400     END-PERFORM.
000500 300-READ-CHILD.
000600     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
000700     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "inline PERFORM loop calls paragraph(s) that reach LRF operations" in message
        for message in analyser.messages
    )


def test_inline_times_loop_with_nested_perform_calls_and_lrf_is_detected():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 3 TIMES
000300         PERFORM 300-READ-CHILD
000400     END-PERFORM.
000500 300-READ-CHILD.
000600     MODIFY CHILD-REC.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "inline PERFORM loop calls paragraph(s) that reach LRF operations" in message
        for message in analyser.messages
    )


def test_inline_loop_nested_scope_does_not_hide_outer_paragraph_call():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 5
000300         PERFORM UNTIL WS-DONE = 'Y'
000400             CONTINUE
000500         END-PERFORM
000600         PERFORM 300-READ-CHILD
000700     END-PERFORM.
000800 300-READ-CHILD.
000900     ERASE CHILD-REC.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "inline PERFORM loop calls paragraph(s) that reach LRF operations" in message
        for message in analyser.messages
    )


def test_paragraph_call_detects_obtain_owner_form():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-READ-OWNER UNTIL EOF.
000300     GOBACK.
000400 100-READ-OWNER.
000500     OBTAIN OWNER WITHIN VMBFORM-M1.
000600     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-READ-OWNER" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_paragraph_call_detects_direct_obtain_and_set_membership_side_effects():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-UPDATE-SET UNTIL EOF.
000300     GOBACK.
000400 100-UPDATE-SET.
000500     OBTAIN CHILD-REC.
000600     DISCONNECT CHILD-REC FROM PARENT-CHILD.
000700     CONNECT CHILD-REC TO PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-UPDATE-SET" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_obtain_owner_inside_literal_does_not_create_false_paragraph_access():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-PRINT-MESSAGE.
000300     GOBACK.
000400 100-PRINT-MESSAGE.
000500     DISPLAY 'OBTAIN OWNER WITHIN VMBFORM-M1'.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert not any("paragraph-driven" in message for message in analyser.messages)


def test_paragraph_find_access_is_reported_for_review():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-READ-RECORD UNTIL EOF.
000300     GOBACK.
000400 100-READ-RECORD.
000500     FIND FIRST RECORD-A WITHIN SET-A.
000600     FIND NEXT RECORD-A WITHIN SET-A.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-READ-RECORD" in message and "paragraph-driven" in message
        for message in analyser.messages
    )


def test_find_words_inside_literal_do_not_trigger_paragraph_review():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-DISPLAY-MESSAGE.
000300     GOBACK.
000400 100-DISPLAY-MESSAGE.
000500     DISPLAY 'FIND FIRST RECORD-A OBTAIN NEXT RECORD-A'.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert not any("paragraph-driven" in message for message in analyser.messages)


def test_duplicate_paragraph_names_union_bodies_for_conservative_lrf_detection():
    """A later duplicate label must not overwrite an earlier LRF-bearing body."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-READ-ROW UNTIL EOF.
000300 100-READ-ROW.
000400     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
000500 200-OTHER-ROW.
000600     CONTINUE.
000700 100-READ-ROW.
000800     CONTINUE.
"""
    paragraphs = LrAccessAnalyser._paragraph_bodies(LrAccessAnalyser._logical_text(source))
    assert "OBTAIN NEXT CHILD-REC" in paragraphs["100-READ-ROW"]

    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-READ-ROW" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_thru_range_keeps_duplicate_named_paragraphs_in_physical_order():
    """A duplicate label inside a THRU range must not disappear from the range."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-START THRU 200-END.
000300 150-READ-ROW.
000400     CONTINUE.
000500 100-START.
000600     CONTINUE.
000700 150-READ-ROW.
000800     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
000900 200-END.
001000     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-START THRU 200-END" in message
        and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_thru_range_with_duplicate_endpoint_is_flagged_as_ambiguous():
    """A name-only THRU endpoint repeated in the source cannot be resolved safely."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-START THRU 200-END.
000300 100-START.
000400     CONTINUE.
000500 200-END.
000600     CONTINUE.
000700 200-END.
000800     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM 100-START THRU 200-END" in message
        and "unresolved or ambiguous paragraph endpoint" in message
        for message in analyser.messages
    )


def test_unmatched_nested_inline_perform_does_not_hide_lrf_access():
    """A single END-PERFORM closes the inner scope, not the outer scope."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 5
000300         PERFORM UNTIL WS-DONE = 'Y'
000400             OBTAIN NEXT RECORD-A WITHIN SET-A.
000500         END-PERFORM.
000600     GOBACK.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "unmatched inline PERFORM scope" in message and "LRF work" in message
        for message in analyser.messages
    )


def test_unresolved_perform_target_is_not_assumed_free_of_lrf_access():
    """A missing paragraph/section target cannot be proven side-effect free."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM INPUT-SECTION UNTIL EOF.
000300     GOBACK.
000400 900-CHECK-STATUS.
000500     OBTAIN NEXT RECORD-A WITHIN SET-A.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM target INPUT-SECTION cannot be resolved" in message
        and "retained for review" in message
        for message in analyser.messages
    )


def test_nested_unresolved_perform_target_keeps_outer_lrf_control_flow_for_review():
    """An unresolved nested PERFORM must conservatively taint its caller."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-INPUT-ROW UNTIL EOF.
000300 100-INPUT-ROW.
000400     PERFORM PROCESS-COPYBOOK-ROW.
000500 900-OTHER-ACCESS.
000600     FIND NEXT RECORD-A WITHIN SET-A.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM target PROCESS-COPYBOOK-ROW cannot be resolved" in message
        for message in analyser.messages
    )
    assert any(
        "PERFORM 100-INPUT-ROW" in message and "business control flow is retained" in message
        for message in analyser.messages
    )


def test_perform_section_with_direct_lrf_access_is_resolved_and_flagged():
    """A section target is a real callable scope, not an unresolved paragraph."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM INPUT-SECTION UNTIL EOF.
000300     GOBACK.
000400 INPUT-SECTION SECTION.
000500 INPUT-ROW.
000600     OBTAIN NEXT RECORD-A WITHIN SET-A.
000700     EXIT.
000800 INPUT-SECTION-END.
000900     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM INPUT-SECTION" in message and "business control flow is retained" in message
        for message in analyser.messages
    )
    assert not any("PERFORM target INPUT-SECTION cannot be resolved" in message for message in analyser.messages)


def test_perform_section_follows_nested_paragraph_call_to_lrf_access():
    """Section call-graph traversal must include paragraphs called by that section."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM INPUT-SECTION UNTIL EOF.
000300     GOBACK.
000400 INPUT-SECTION SECTION.
000500 INPUT-ROW.
000600     PERFORM READ-CHILD.
000700 READ-CHILD.
000800     FIND NEXT CHILD-REC WITHIN PARENT-CHILD.
000900 INPUT-SECTION-END.
001000     CONTINUE.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM INPUT-SECTION" in message and "business control flow is retained" in message
        for message in analyser.messages
    )
    assert not any("PERFORM target INPUT-SECTION cannot be resolved" in message for message in analyser.messages)


def test_duplicate_performed_section_name_is_ambiguous_and_kept_for_review():
    """Repeated section names must not resolve to an arbitrary section body."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM INPUT-SECTION UNTIL EOF.
000300 INPUT-SECTION SECTION.
000400 INPUT-ROW.
000500     CONTINUE.
000600 OTHER-SECTION SECTION.
000700     CONTINUE.
000800 INPUT-SECTION SECTION.
000900 INPUT-ROW-2.
001000     OBTAIN NEXT RECORD-A WITHIN SET-A.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM target INPUT-SECTION is ambiguous" in message
        and "retained for review" in message
        for message in analyser.messages
    )


def test_name_only_perform_to_duplicate_paragraph_is_explicitly_ambiguous():
    """Unioning duplicate bodies prevents missed access but cannot resolve a call target."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-READ-ROW UNTIL EOF.
000300 100-READ-ROW.
000400     CONTINUE.
000500 200-OTHER-ROW.
000600     CONTINUE.
000700 100-READ-ROW.
000800     OBTAIN NEXT CHILD-REC WITHIN PARENT-CHILD.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM target 100-READ-ROW has duplicate paragraph definitions" in message
        for message in analyser.messages
    )
    assert any("PERFORM 100-READ-ROW" in message and "business control flow is retained" in message
               for message in analyser.messages)


def test_duplicate_paragraph_target_without_visible_access_is_still_reviewed():
    """A duplicate call target is ambiguous even when neither body exposes an LRF verb."""
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM 100-LOG-ROW UNTIL EOF.
000300 100-LOG-ROW.
000400     DISPLAY 'first'.
000500 200-OTHER-ROW.
000600     CONTINUE.
000700 100-LOG-ROW.
000800     DISPLAY 'second'.
000900 300-IDMS-ACCESS.
001000     OBTAIN FIRST AUDIT-REC WITHIN AUDIT-SET.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM target 100-LOG-ROW has duplicate paragraph definitions" in message
        for message in analyser.messages
    )


def test_procedure_copybook_keeps_unresolved_perform_target_on_review_path():
    """An access hidden in a procedure copybook must not be assumed absent."""
    source = """000100 IDENTIFICATION DIVISION.
000200 DATA DIVISION.
000300 WORKING-STORAGE SECTION.
000400 COPY WS-FIELDS.
000500 PROCEDURE DIVISION.
000600     PERFORM PROCESS-COPYBOOK-ROW UNTIL EOF.
000700     GOBACK.
000800     COPY PROC-ACCESS-LOGIC.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert any(
        "PERFORM target PROCESS-COPYBOOK-ROW cannot be resolved" in message
        and "retained for review" in message
        for message in analyser.messages
    )


def test_data_division_copybook_alone_does_not_enable_procedure_unknown_target_diagnostics():
    """A data declaration COPY should not create a false procedure-flow warning."""
    source = """000100 DATA DIVISION.
000200 WORKING-STORAGE SECTION.
000300 COPY WS-FIELDS.
000400 PROCEDURE DIVISION.
000500     PERFORM LOCAL-LOGGING.
000600 LOCAL-LOGGING.
000700     DISPLAY 'done'.
"""
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert analyser.messages == []


def test_copy_text_inside_procedure_literal_is_not_treated_as_copy_statement():
    source = """000100 PROCEDURE DIVISION.
000200     DISPLAY 'COPY PROC-ACCESS-LOGIC'.
000300     PERFORM LOCAL-LOGGING.
000400 LOCAL-LOGGING.
000500     CONTINUE.
"""
    assert not LrAccessAnalyser._has_procedure_copy(LrAccessAnalyser._logical_text(source))
    analyser = LrAccessAnalyser()
    assert analyser.bounded_searches(source) == {}
    assert analyser.messages == []


def test_supplied_procedure_copybook_is_expanded_for_control_flow_analysis_only():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM PROCESS-COPYBOOK-ROW UNTIL EOF.
000300     GOBACK.
000400     COPY PROC-ACCESS-LOGIC.
"""
    copybooks = {
        "PROC-ACCESS-LOGIC.cpy": """PROCESS-COPYBOOK-ROW.
    OBTAIN NEXT AUDIT-REC WITHIN AUDIT-SET.
"""
    }
    analyser = LrAccessAnalyser()

    assert analyser.bounded_searches(source, procedure_copybooks=copybooks) == {}
    assert any(
        "PERFORM PROCESS-COPYBOOK-ROW" in message and "retained" in message
        for message in analyser.messages
    )
    # Analysis expands a separate in-memory representation; caller's source is unchanged.
    assert "COPY PROC-ACCESS-LOGIC." in source


def test_nested_procedure_copybooks_are_expanded_recursively():
    source = """000100 PROCEDURE DIVISION.
000200     PERFORM PROCESS-ROW UNTIL EOF.
000300     COPY PROC-A.
"""
    copybooks = {
        "PROC-A": "    COPY PROC-B.",
        "PROC-B": "PROCESS-ROW.\n    FIND NEXT AUDIT-REC WITHIN AUDIT-SET.",
    }
    analyser = LrAccessAnalyser()

    analyser.bounded_searches(source, procedure_copybooks=copybooks)
    assert any("PERFORM PROCESS-ROW" in message and "retained" in message
               for message in analyser.messages)
    assert not any("COPY PROC-A is unresolved" in message for message in analyser.messages)


def test_unresolved_procedure_copybook_is_reported_explicitly():
    source = """000100 PROCEDURE DIVISION.
000200     COPY MISSING-PROC.
000300     GOBACK.
"""
    analyser = LrAccessAnalyser()

    analyser.bounded_searches(source, procedure_copybooks={})
    # Without a supplied library we cannot resolve the copybook; when a library
    # is supplied but the member is absent, the uncertainty is made explicit.
    analyser.bounded_searches(source, procedure_copybooks={"OTHER-PROC": "CONTINUE."})
    assert any("procedure COPY MISSING-PROC is unresolved" in message
               for message in analyser.messages)


def test_procedure_copy_replacing_is_not_expanded_with_unmodified_text():
    source = """000100 PROCEDURE DIVISION.
000200     COPY PROC-ACCESS-LOGIC REPLACING ==ROW-NAME== BY ==AUDIT-REC==.
"""
    analyser = LrAccessAnalyser()

    analyser.bounded_searches(
        source,
        procedure_copybooks={"PROC-ACCESS-LOGIC": "ROW-NAME.\n    OBTAIN NEXT ROW-NAME."},
    )
    assert any("COPY PROC-ACCESS-LOGIC uses REPLACING" in message
               for message in analyser.messages)
