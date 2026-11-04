from converter.analyzers.program_flow.business_operation_parity_audit import (
    BusinessOperationParityAuditor,
)


def test_all_idms_dml_families_require_db2_counterparts():
    source = """000100 PROCEDURE DIVISION.
000200 1000-MAIN.
000300     OBTAIN CALC CUSTOMER.
000400     MODIFY CUSTOMER.
000500     STORE AUDIT-ROW.
000600     ERASE OLD-ROW.
"""
    target = """000100 PROCEDURE DIVISION.
000200 1000-MAIN.
000300     EXEC SQL SELECT CUSTOMER_ID INTO :WS-ID FROM CUSTOMER END-EXEC.
000400     EXEC SQL UPDATE CUSTOMER SET NAME = :WS-NAME END-EXEC.
000500     EXEC SQL INSERT INTO AUDIT_ROW (ID) VALUES (:WS-ID) END-EXEC.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert [issue.family for issue in report.issues] == ["DELETE"]
    assert len(report.source_operations) == 4
    assert report.target_sql_families == ("SELECT", "INSERT", "UPDATE")


def test_comments_and_literals_do_not_create_source_operations():
    source = """000100 1000-MAIN.
000200*    ERASE CUSTOMER.
000300     DISPLAY 'STORE CUSTOMER MODIFY CUSTOMER'.
000400     OBTAIN CALC CUSTOMER.
"""
    target = """000100 1000-MAIN.
000200     EXEC SQL
000210       SELECT CUSTOMER_ID INTO :WS-ID
000220       FROM CUSTOMER
000230     END-EXEC.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert [operation.family for operation in report.source_operations] == ["SELECT"]
    assert report.passed


def test_cursorized_reads_count_as_select_coverage_without_count_matching():
    source = """000100 1000-MAIN.
000200     OBTAIN FIRST CUSTOMER.
000300     OBTAIN NEXT CUSTOMER.
"""
    target = """000100 2100-OPEN-CUSTOMER.
000200     EXEC SQL DECLARE C1 CURSOR FOR SELECT CUSTOMER_ID FROM CUSTOMER END-EXEC.
000300 2200-FETCH-CUSTOMER.
000400     EXEC SQL FETCH C1 INTO :WS-ID END-EXEC.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert report.passed
    assert len(report.source_operations) == 2
    assert report.target_sql_families == ("SELECT",)


def test_per_operation_audit_checks_the_mapped_db2_table(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,New DB2 Record \\n"
        "CUSTOMER,DZCUSTTB \\n".replace(" \\n", "\n"),
        encoding="utf-8",
    )
    source = """000100 PROCEDURE DIVISION.
000200 1000-MAIN.
000300     MODIFY CUSTOMER.
"""
    target = """000100 2000-UPDATE.
000200     EXEC SQL UPDATE WRONGTB SET NAME = :WS-NAME END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not report.passed
    assert [issue.code for issue in report.issues] == ["SOURCE_OPERATION_TABLE_NOT_FOUND_IN_TARGET_SQL"]
    assert "DZCUSTTB" in report.issues[0].message


def test_per_operation_audit_accepts_mapping_to_db2_table(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,New DB2 Record \nCUSTOMER,DZCUSTTB\n",
        encoding="utf-8",
    )
    source = """000100 PROCEDURE DIVISION.
000200 1000-MAIN.
000300     MODIFY CUSTOMER.
"""
    target = """000100 2000-UPDATE.
000200     EXEC SQL UPDATE DZCUSTTB SET NAME = :WS-NAME END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert report.passed
    assert not report.reviews


def test_unmapped_lrf_set_operand_is_review_not_false_failure(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text("Cobol Recrd IDMS,New DB2 Record \nCUSTOMER,DZCUSTTB\n", encoding="utf-8")
    source = """000100 1000-MAIN.
000200     OBTAIN FIRST CUSTOMER-SET.
"""
    target = """000100 2100-OPEN.
000200     EXEC SQL
000210       DECLARE C1 CURSOR FOR
000220       SELECT ID FROM DZCUSTTB
000230     END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert report.passed
    assert len(report.reviews) == 1
    assert report.reviews[0].operand == "CUSTOMER-SET"


def test_update_must_reference_every_mapped_primary_key(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        """Cobol Recrd IDMS,DB2 key,New DB2_Field name,New DB2 Record 
CUSTOMER,Primary Key,CUSTOMER_ID,DZCUSTTB
CUSTOMER,Primary Key,BRANCH_ID,DZCUSTTB
""",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     MODIFY CUSTOMER.
"""
    target = """000100 1100-UPDATE.
000200     EXEC SQL
000210       UPDATE DZCUSTTB
000220       SET NAME = :WS-NAME
000230       WHERE CUSTOMER_ID = :WS-ID
000240     END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not report.passed
    assert len(report.issues) == 1
    assert report.issues[0].code == "TARGET_KEY_PREDICATE_MISSING_MAPPED_KEY"
    assert "BRANCH_ID" in report.issues[0].message


def test_lrf_where_keyword_resolves_logical_record_for_table_audit(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,New DB2 Record \nVMBEVEF,DZEVEFTB\n",
        encoding="utf-8",
    )
    dclgen = tmp_path / "DCLGen"
    dclgen.mkdir()
    (dclgen / "DZEVEFTV.txt").write_text("DCLGEN fixture", encoding="utf-8")
    source = """000100 1000-MAIN.
000200     OBTAIN FIRST VMBTL07-R01 WHERE ALL-VMBEVEF-BY-VMBEFF.
"""
    target = """000100 2100-OPEN.
000200     EXEC SQL
000210       DECLARE C1 CURSOR FOR
000220       SELECT NR_IDGOOD_479EVEF FROM DZEVEFTV
000230     END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping, dclgen_dir=dclgen).audit(source, target)
    assert report.passed
    assert not report.reviews
    assert report.source_operations[0].operand == "VMBEVEF"


def test_update_set_must_include_explicitly_changed_mapped_field(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,Cobol Zone,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,03 CUSTOMER-ID,Primary Key,DZCUSTTB,CUSTOMER_ID\n"
        "CUSTOMER,03 CUSTOMER-STATUS,,DZCUSTTB,CUSTOMER_STATUS\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     MOVE 'A' TO CUSTOMER-STATUS OF CUSTOMER.
000300     MODIFY CUSTOMER.
"""
    target = """000100 1100-UPDATE.
000200     EXEC SQL
000210       UPDATE DZCUSTTB
000220          SET CUSTOMER_ID = :WS-ID
000230        WHERE CUSTOMER_ID = :WS-ID
000240     END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not report.passed
    assert any(issue.code == "TARGET_UPDATE_SET_MISSING_SOURCE_FIELD" for issue in report.issues)
    assert "CUSTOMER_STATUS" in next(
        issue.message for issue in report.issues
        if issue.code == "TARGET_UPDATE_SET_MISSING_SOURCE_FIELD"
    )


def test_update_set_accepts_mapped_changed_field_and_additional_audit_columns(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,Cobol Zone,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,03 CUSTOMER-ID,Primary Key,DZCUSTTB,CUSTOMER_ID\n"
        "CUSTOMER,03 CUSTOMER-STATUS,,DZCUSTTB,CUSTOMER_STATUS\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     MOVE 'A' TO CUSTOMER-STATUS OF CUSTOMER.
000300     MODIFY CUSTOMER.
"""
    target = """000100 1100-UPDATE.
000200     EXEC SQL
000210       UPDATE DZCUSTTB
000220          SET CUSTOMER_STATUS = :WS-STATUS,
000230              UPDATE_USER = :WS-USER
000240        WHERE CUSTOMER_ID = :WS-ID
000250     END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert report.passed


def test_update_set_audit_resolves_unqualified_record_field_from_mapping(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,Cobol Zone,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "VMBFAR,03 DA-INFSD-GDIFAR,,DZBFARTB,DA_INFSDGD_479BFAR\n"
        "VMBFAR,05 CT-RK-TGDSV,Primary Key,DZBFARTB,CT_TGDSERV_479BFAR\n",
        encoding="utf-8",
    )
    source = """000100 VERWERKING.
000200     OBTAIN CALC VMBFAR
000300     MOVE DATE-YMD8 TO DA-INFSD-GDIFAR
000400     MODIFY VMBFAR.
"""
    target = """000100 1100-UPDATE.
000200     EXEC SQL
000210       UPDATE DZBFARTB
000220          SET DA_INFSDGD_479BFAR = :WS-DATE
000230        WHERE CT_TGDSERV_479BFAR = :WS-KEY
000240     END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert report.passed
    assert not [review for review in report.reviews if "DA-INFSD-GDIFAR" in review.message]


def test_obtain_downstream_field_read_requires_select_projection(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,Cobol Zone,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,03 CUSTOMER-ID,Primary Key,DZCUSTTB,CUSTOMER_ID\n"
        "CUSTOMER,03 CUSTOMER-STATUS,,DZCUSTTB,CUSTOMER_STATUS\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER.
000300     IF CUSTOMER-STATUS OF CUSTOMER = 'A'
000400        DISPLAY CUSTOMER-ID OF CUSTOMER
000500     END-IF.
"""
    target = """000100 1100-UPDATE.
000200     EXEC SQL UPDATE DZCUSTTB SET CUSTOMER_STATUS = :WS-STATUS
000300       WHERE CUSTOMER_ID = :WS-ID END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not report.passed
    assert any(issue.code == "TARGET_SELECT_MISSING_DOWNSTREAM_FIELD_READ" for issue in report.issues)


def test_obtain_select_projection_must_include_downstream_fields(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,Cobol Zone,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,03 CUSTOMER-ID,Primary Key,DZCUSTTB,CUSTOMER_ID\n"
        "CUSTOMER,03 CUSTOMER-STATUS,,DZCUSTTB,CUSTOMER_STATUS\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER.
000300     IF CUSTOMER-STATUS OF CUSTOMER = 'A'
000400        DISPLAY CUSTOMER-ID OF CUSTOMER
000500     END-IF.
"""
    target = """000100 1100-SELECT.
000200     EXEC SQL SELECT CUSTOMER_ID INTO :WS-ID FROM DZCUSTTB
000300       WHERE CUSTOMER_ID = :WS-ID END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not report.passed
    issue = next(issue for issue in report.issues if issue.code == "TARGET_SELECT_PROJECTION_MISSING_SOURCE_FIELD")
    assert "CUSTOMER_STATUS" in issue.message


def test_obtain_projection_passes_when_required_fields_are_selected(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,Cobol Zone,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,03 CUSTOMER-ID,Primary Key,DZCUSTTB,CUSTOMER_ID\n"
        "CUSTOMER,03 CUSTOMER-STATUS,,DZCUSTTB,CUSTOMER_STATUS\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER.
000300     IF CUSTOMER-STATUS OF CUSTOMER = 'A'
000400        DISPLAY CUSTOMER-ID OF CUSTOMER
000500     END-IF.
"""
    target = """000100 1100-SELECT.
000200     EXEC SQL SELECT CUSTOMER_ID, CUSTOMER_STATUS
000300       INTO :WS-ID, :WS-STATUS FROM DZCUSTTB
000400       WHERE CUSTOMER_ID = :WS-ID END-EXEC.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert report.passed
    assert not [issue for issue in report.issues if issue.code.startswith("TARGET_SELECT_")]


def test_transaction_boundaries_require_matching_db2_sql():
    source = """000100 1000-MAIN.
000200     COMMIT.
000300     PERFORM PROCESS-COMMIT.
000400 2000-ERROR.
000500     ROLLBACK.
"""
    target = """000100 800-COMMIT.
000200     EXEC SQL COMMIT END-EXEC.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert [op.family for op in report.source_operations] == ["COMMIT", "ROLLBACK"]
    assert [issue.family for issue in report.issues] == ["ROLLBACK"]
    assert report.target_sql_families == ("COMMIT",)


def test_transaction_boundary_keywords_in_comments_and_literals_are_ignored():
    source = """000100 1000-MAIN.
000200*    COMMIT.
000300     DISPLAY 'ROLLBACK COMMIT'.
000400     CONTINUE.
"""
    target = """000100 1000-MAIN.
000200     DISPLAY 'EXEC SQL ROLLBACK END-EXEC'.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert report.source_operations == ()
    assert report.passed


def test_commit_and_rollback_are_recognized_only_inside_embedded_db2_sql():
    source = """000100 1000-MAIN.
000200     COMMIT.
000300     ROLLBACK.
"""
    target = """000100 1000-MAIN.
000200     DISPLAY 'COMMIT'.
000300     EXEC SQL COMMIT END-EXEC.
000400     EXEC SQL ROLLBACK END-EXEC.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert report.passed
    assert report.target_sql_families == ("COMMIT", "ROLLBACK")


def test_idms_not_found_handler_without_db2_sqlcode_100_is_reviewed():
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER
000300       ON DB-REC-NOT-FOUND MOVE 'N' TO SW-FOUND.
"""
    target = """000100 1000-MAIN.
000200     EXEC SQL SELECT CUSTOMER_ID INTO :WS-ID
000300       FROM DZCUSTTB WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     IF SQLCODE NOT = 0 PERFORM SQLERROR END-IF.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert any("ON DB-REC-NOT-FOUND" in review.message for review in report.reviews)


def test_idms_not_found_handler_with_local_db2_when_100_is_recognized(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text("Cobol Recrd IDMS,New DB2 Record \nCUSTOMER,DZCUSTTB\n", encoding="utf-8")
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER
000300       ON DB-REC-NOT-FOUND MOVE 'N' TO SW-FOUND.
"""
    target = """000100 1000-MAIN.
000200     EXEC SQL SELECT CUSTOMER_ID INTO :WS-ID
000300       FROM DZCUSTTB WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     EVALUATE SQLCODE
000500       WHEN 0 CONTINUE
000600       WHEN 100 MOVE 'N' TO SW-FOUND
000700       WHEN OTHER PERFORM SQLERROR
000800     END-EVALUATE.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not any("ON DB-REC-NOT-FOUND" in review.message for review in report.reviews)


def test_unrelated_sqlcode_100_does_not_satisfy_not_found_parity(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,New DB2 Record \nCUSTOMER,DZCUSTTB\nAUDIT-ROW,DZAUDTTB\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER
000300       ON DB-REC-NOT-FOUND MOVE 'N' TO SW-FOUND.
"""
    target = """000100 1000-MAIN.
000200     EXEC SQL SELECT CUSTOMER_ID INTO :WS-ID
000300       FROM DZCUSTTB WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     IF SQLCODE NOT = 0 PERFORM SQLERROR END-IF.
000500     EXEC SQL SELECT AUDIT_ID INTO :WS-AUDIT
000600       FROM DZAUDTTB WHERE AUDIT_ID = :WS-AUDIT END-EXEC.
000700     EVALUATE SQLCODE
000800       WHEN 100 CONTINUE
000900       WHEN OTHER CONTINUE
001000     END-EVALUATE.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert any("mapped SELECT-local SQLCODE +100/WHEN 100 branch" in review.message for review in report.reviews)


def test_not_found_branch_in_later_paragraph_does_not_satisfy_select(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text("Cobol Recrd IDMS,New DB2 Record \nCUSTOMER,DZCUSTTB\n", encoding="utf-8")
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER
000300       ON DB-REC-NOT-FOUND MOVE 'N' TO SW-FOUND.
"""
    target = """000100 1000-MAIN.
000200     EXEC SQL SELECT CUSTOMER_ID INTO :WS-ID
000300       FROM DZCUSTTB WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     IF SQLCODE NOT = 0 PERFORM SQLERROR END-IF.
000500 2000-OTHER-PARAGRAPH.
000600     EVALUATE SQLCODE
000700       WHEN 100 MOVE 'N' TO SW-FOUND
000800       WHEN OTHER CONTINUE
000900     END-EVALUATE.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert any("mapped SELECT-local SQLCODE +100/WHEN 100 branch" in review.message for review in report.reviews)


def test_direct_update_replacement_requires_operation_local_affected_row_check(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,Primary Key,DZCUSTTB,CUSTOMER_ID\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER.
000300     MODIFY CUSTOMER.
"""
    target = """000100 1100-UPDATE-CUSTOMER.
000200     EXEC SQL UPDATE DZCUSTTB SET CUSTOMER_STATUS = :WS-STATUS
000300       WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     EVALUATE SQLCODE
000500       WHEN 0 ADD 1 TO WS-UPDATED
000600       WHEN OTHER PERFORM SQLERROR
000700     END-EVALUATE.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert any("no operation-local affected-row check" in review.message for review in report.reviews)


def test_direct_update_replacement_recognizes_sqlerrd_three_guard(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,Primary Key,DZCUSTTB,CUSTOMER_ID\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER.
000300     MODIFY CUSTOMER.
"""
    target = """000100 1100-UPDATE-CUSTOMER.
000200     EXEC SQL UPDATE DZCUSTTB SET CUSTOMER_STATUS = :WS-STATUS
000300       WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     IF SQLCODE = 0 AND SQLERRD(3) = 0
000500       MOVE 'N' TO WS-FOUND
000600     END-IF.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not any("no operation-local affected-row check" in review.message for review in report.reviews)


def test_direct_update_row_count_mention_without_zero_guard_does_not_pass(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,Primary Key,DZCUSTTB,CUSTOMER_ID\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER.
000300     MODIFY CUSTOMER.
"""
    target = """000100 1100-UPDATE-CUSTOMER.
000200     EXEC SQL UPDATE DZCUSTTB SET CUSTOMER_STATUS = :WS-STATUS
000300       WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     ADD SQLERRD(3) TO WS-UPDATED-ROWS.
000500     EVALUATE SQLCODE
000600       WHEN 0 CONTINUE
000700       WHEN OTHER PERFORM SQLERROR
000800     END-EVALUATE.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert any("no operation-local affected-row check" in review.message for review in report.reviews)


def test_select_and_update_for_mapped_table_is_not_misclassified_as_direct_update_replacement(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "RESTART-REC,Primary Key,DZ01RSTV,NM_ID_RS_PROGRAM\n",
        encoding="utf-8",
    )
    source = """000100 800-TEST-RESTART.
000200     OBTAIN CALC RESTART-REC.
000300     MODIFY RESTART-REC.
"""
    target = """000100 700-SELECT-RESTART.
000200     EXEC SQL SELECT NM_ID_RS_PROGRAM INTO :WS-NAME FROM DZ01RSTV END-EXEC.
000300     EVALUATE SQLCODE
000400       WHEN 0 CONTINUE
000500       WHEN 100 CONTINUE
000600     END-EVALUATE.
000700 710-UPDATE-RESTART.
000800     EXEC SQL UPDATE DZ01RSTV SET NM_ID_RS_PROGRAM = :WS-NAME
000900       WHERE NM_ID_RS_PROGRAM = :WS-NAME END-EXEC.
001000     EVALUATE SQLCODE
001100       WHEN 0 CONTINUE
001200       WHEN OTHER PERFORM SQLERROR
001300     END-EVALUATE.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert not any("no operation-local affected-row check" in review.message for review in report.reviews)


def test_direct_update_without_mapped_select_still_requires_zero_row_review(tmp_path):
    mapping = tmp_path / "mapping.csv"
    mapping.write_text(
        "Cobol Recrd IDMS,DB2 key,New DB2 Record ,New DB2_Field name\n"
        "CUSTOMER,Primary Key,DZCUSTTB,CUSTOMER_ID\n",
        encoding="utf-8",
    )
    source = """000100 1000-MAIN.
000200     OBTAIN CALC CUSTOMER.
000300     MODIFY CUSTOMER.
"""
    target = """000100 1100-UPDATE-CUSTOMER.
000200     EXEC SQL UPDATE DZCUSTTB SET CUSTOMER_STATUS = :WS-STATUS
000300       WHERE CUSTOMER_ID = :WS-ID END-EXEC.
000400     EVALUATE SQLCODE
000500       WHEN 0 CONTINUE
000600       WHEN OTHER PERFORM SQLERROR
000700     END-EVALUATE.
"""
    report = BusinessOperationParityAuditor(mapping_csv=mapping).audit(source, target)
    assert any("no operation-local affected-row check" in review.message for review in report.reviews)


def test_physical_write_is_required_independently_of_db2_select():
    source = """000100 1000-MAIN.
000200     MOVE A TO B
000300     WRITE RESULT-RECORD FROM OUTPUT-BUFFER
"""
    lost_write = """000100 1000-MAIN.
000200     MOVE A TO B.
000300     EXEC SQL SELECT ID INTO :H FROM T END-EXEC.
"""
    report = BusinessOperationParityAuditor().audit(source, lost_write)
    assert any(issue.code == "SOURCE_FILE_WRITE_MISSING" for issue in report.issues)
    kept_write = lost_write + "000400     WRITE RESULT-RECORD FROM OUTPUT-BUFFER.\n"
    report = BusinessOperationParityAuditor().audit(source, kept_write)
    assert not any(issue.code == "SOURCE_FILE_WRITE_MISSING" for issue in report.issues)


def test_same_name_business_paragraph_cannot_silently_become_display_only():
    source = """000100 PROCEDURE DIVISION.
000200 800-TEST-CONTROL.
000300     IF FLAG = 'Y'
000400         OBTAIN CALC CONTROL-RECORD
000500         MODIFY CONTROL-RECORD
000600     END-IF.
"""
    target = """000100 PROCEDURE DIVISION.
000200 800-TEST-CONTROL.
000300     DISPLAY '800-TEST-CONTROL'.
000400 900-FINISH.
000500     CONTINUE.
000600     EXEC SQL UPDATE CONTROL SET A = 1 END-EXEC.
"""
    report = BusinessOperationParityAuditor().audit(source, target)
    assert any(issue.code == "SOURCE_BUSINESS_PARAGRAPH_EMPTIED" for issue in report.issues)
    resolved = target.replace("DISPLAY '800-TEST-CONTROL'.", "PERFORM 700-UPDATE-CONTROL.")
    report = BusinessOperationParityAuditor().audit(source, resolved)
    assert not any(issue.code == "SOURCE_BUSINESS_PARAGRAPH_EMPTIED" for issue in report.issues)


def test_tab_export_populates_all_semantic_mapping_indexes(tmp_path):
    import csv
    mapping = tmp_path / "renamed_export.csv"
    with mapping.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["Cobol Recrd IDMS", "Cobol Zone", "DB2 key", "New DB2 Record ", "New DB2_Field name"])
        writer.writerow(["ACCOUNT", "02 ACCOUNT-NUMBER", "PRIMARY KEY", "ACCOUNT_TABLE", "ACCOUNT_ID"])
    auditor = BusinessOperationParityAuditor(mapping_csv=mapping)
    assert auditor.mapping_tables == {"ACCOUNT": {"ACCOUNT_TABLE"}}
    assert auditor.mapping_key_columns == {"ACCOUNT": {"ACCOUNT_ID"}}
    assert auditor.mapping_record_fields == {"ACCOUNT": {"ACCOUNT-NUMBER": {"ACCOUNT_ID"}}}
    report = auditor.audit("000100     MODIFY ACCOUNT.",
        "000100     EXEC SQL UPDATE WRONG_TABLE SET X = :Y END-EXEC.")
    assert any(i.code == "SOURCE_OPERATION_TABLE_NOT_FOUND_IN_TARGET_SQL" for i in report.issues)
