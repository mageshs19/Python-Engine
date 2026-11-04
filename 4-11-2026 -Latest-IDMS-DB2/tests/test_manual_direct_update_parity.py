"""Generic manual-DB2 equivalence evidence must never hide a source conflict."""

from converter.analyzers.program_flow.business_operation_parity_audit import OperationParityReview
from mainframe.verification.manual_direct_update_parity import manually_confirmed_direct_updates

SOURCE = """000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID. LEGACY.
000300 PROCEDURE DIVISION.
000400 PROCESS-ONE.
000500     MOVE 'A' TO KEY OF CUSTOMER
000600     OBTAIN CALC CUSTOMER
000700     MOVE TODAY TO MODIFIED OF CUSTOMER
000800     MODIFY CUSTOMER.
"""


def program(sql_code="""
           EVALUATE SQLCODE
             WHEN 0 ADD 1 TO WS-UPDATED
             WHEN OTHER
               DISPLAY 'ERROR ON UPDATE'
               PERFORM SQLERROR
           END-EVALUATE
""", where="ACCOUNT_ID = :DCLCUSTOMER.ACCOUNT-ID", set_expr="MODIFIED = :DCLCUSTOMER.MODIFIED"):
    return f"""IDENTIFICATION DIVISION.
PROGRAM-ID. NEWPROG.
PROCEDURE DIVISION.
UPDATE-CUSTOMER.
    EXEC SQL
       UPDATE CUSTTBL
       SET {set_expr}
       WHERE {where}
       QUERYNO 200
    END-EXEC
{sql_code}
"""

REVIEWS = (
    OperationParityReview("SELECT", 6, "CUSTOMER", "OBTAIN CALC CUSTOMER has no SELECT on mapped table"),
    OperationParityReview("UPDATE", 8, "CUSTOMER", "no operation-local affected-row check"),
)


def check(source=SOURCE, generated=None, manual=None, reviews=REVIEWS):
    generated = generated if generated is not None else program()
    manual = manual if manual is not None else program()
    return manually_confirmed_direct_updates(source, generated, manual, reviews, {"CUSTOMER": {"CUSTTBL"}})


def test_identical_manual_db2_update_with_unconditional_source_pair_is_manual_parity():
    confirmed, remaining = check()
    assert confirmed == {"CUSTOMER"}
    assert remaining == ()


def test_reordered_set_and_key_predicates_are_equivalent_when_pairs_match():
    generated = program(where="A = :DCLCUSTOMER.A AND B = :DCLCUSTOMER.B",
                        set_expr="MODIFIED = :DCLCUSTOMER.MODIFIED, USER_ID = :DCLCUSTOMER.USER-ID")
    manual = program(where="B = :DCLCUSTOMER.B AND A = :DCLCUSTOMER.A",
                     set_expr="USER_ID = :DCLCUSTOMER.USER-ID, MODIFIED = :DCLCUSTOMER.MODIFIED")
    assert check(generated=generated, manual=manual)[1] == ()


def test_mismatched_update_key_or_updated_value_remains_blocked():
    for manual in (
        program(where="OTHER_ID = :DCLCUSTOMER.ACCOUNT-ID"),
        program(set_expr="MODIFIED = :DCLCUSTOMER.WRONG"),
        program(where="ACCOUNT_ID = :DCLCUSTOMER.ACCOUNT-ID OR FLAG = 1"),
    ):
        confirmed, remaining = check(manual=manual)
        assert not confirmed and remaining == REVIEWS


def test_source_explicit_not_found_or_fetched_value_dependency_is_never_waived():
    sources = (
        SOURCE.replace("OBTAIN CALC CUSTOMER", "OBTAIN CALC CUSTOMER\n000601       ON DB-REC-NOT-FOUND MOVE 'Y' TO FLAG"),
        SOURCE.replace("MOVE TODAY TO MODIFIED OF CUSTOMER", "MOVE STATUS OF CUSTOMER TO FLAG\n000701     MOVE TODAY TO MODIFIED OF CUSTOMER"),
        SOURCE.replace("MOVE TODAY TO MODIFIED OF CUSTOMER", "IF ERROR-STATUS = '0000'\n000701         MOVE TODAY TO MODIFIED OF CUSTOMER\n000702     END-IF"),
    )
    for source in sources:
        confirmed, remaining = check(source=source)
        assert not confirmed and remaining == REVIEWS


def test_wrong_manual_program_or_different_sqlcode_action_never_waived():
    assert check(manual=program().replace("NEWPROG", "ANOTHER"))[1] == REVIEWS
    assert check(manual=program().replace("ADD 1 TO WS-UPDATED", "ADD 1 TO OTHER-COUNTER"))[1] == REVIEWS
    assert check(manual=program().replace("PERFORM SQLERROR", "CONTINUE"))[1] == REVIEWS
    assert check(manual=program().replace("WHEN OTHER", "WHEN 100"))[1] == REVIEWS
    assert check(manual=program().replace("WHEN OTHER", "WHEN OTHER\n               IF FLAG = 'Y'"))[1] == REVIEWS


def test_unrelated_business_reviews_stay_blocked_after_local_manual_evidence():
    unrelated = OperationParityReview("INSERT", 20, "OTHER", "missing INSERT")
    confirmed, remaining = check(reviews=REVIEWS + (unrelated,))
    assert confirmed == {"CUSTOMER"}
    assert remaining == (unrelated,)
