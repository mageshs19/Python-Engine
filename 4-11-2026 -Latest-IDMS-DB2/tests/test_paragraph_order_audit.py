from converter.analyzers.program_flow.paragraph_order_audit import ParagraphOrderAuditor


def test_order_audit_allows_generated_paragraphs_between_original_paragraphs():
    original = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       B-PARA.
           CONTINUE.
"""
    converted = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       2100-OPEN-C1.
           CONTINUE.
       B-PARA.
           CONTINUE.
"""
    result = ParagraphOrderAuditor().audit(original, converted)
    assert result.order_preserved
    assert result.shared_in_original_order == ("A-PARA", "B-PARA")


def test_order_audit_flags_original_business_paragraph_reordering():
    original = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       B-PARA.
           CONTINUE.
       C-PARA.
           CONTINUE.
"""
    converted = """       PROCEDURE DIVISION.
       B-PARA.
           CONTINUE.
       A-PARA.
           CONTINUE.
       C-PARA.
           CONTINUE.
"""
    result = ParagraphOrderAuditor().audit(original, converted)
    assert not result.order_preserved
    assert result.reordered_shared


def test_order_audit_reports_missing_original_paragraphs_for_review():
    original = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       B-PARA.
           CONTINUE.
"""
    converted = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
"""
    result = ParagraphOrderAuditor().audit(original, converted)
    assert result.missing_from_converted == ("B-PARA",)
    assert result.diagnostics



def test_order_audit_treats_idms_abort_hook_removal_as_intentional():
    original = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       IDMS-ABORT.
           EXIT.
       B-PARA.
           CONTINUE.
"""
    converted = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       B-PARA.
           CONTINUE.
"""
    result = ParagraphOrderAuditor().audit(original, converted)
    assert result.order_preserved
    assert result.missing_from_converted == ()
    assert not result.diagnostics


def test_order_audit_does_not_hide_nontrivial_idms_abort_business_body():
    original = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       IDMS-ABORT.
           MOVE 'Y' TO WS-ABORTED.
           EXIT.
       B-PARA.
           CONTINUE.
"""
    converted = """       PROCEDURE DIVISION.
       A-PARA.
           CONTINUE.
       B-PARA.
           CONTINUE.
"""
    result = ParagraphOrderAuditor().audit(original, converted)
    assert result.missing_from_converted == ("IDMS-ABORT",)
    assert result.diagnostics
