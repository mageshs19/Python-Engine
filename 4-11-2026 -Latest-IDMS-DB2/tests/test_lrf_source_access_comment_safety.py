from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter


def test_source_access_scanner_ignores_idms_tokens_inside_quoted_literals():
    source = '''000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     DISPLAY "OBTAIN NEXT RECORD-A".
000300     DISPLAY 'FIND NEXT RECORD-A'.
'''
    assert BoundedLrfSingletonRewriter._source_accesses(source) == [("FIRST", "RECORD-A")]
    assert BoundedLrfSingletonRewriter._source_proves_first_only(source) is True


def test_source_access_scanner_ignores_inline_comments():
    source = '''000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     DISPLAY "OK" *> OBTAIN NEXT RECORD-A
'''
    assert BoundedLrfSingletonRewriter._source_accesses(source) == [("FIRST", "RECORD-A")]
    assert BoundedLrfSingletonRewriter._source_proves_first_only(source) is True


def test_real_executable_next_still_blocks_first_only_proof():
    source = '''000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     OBTAIN NEXT RECORD-A WITHIN SET-A.
000300     DISPLAY "OBTAIN NEXT RECORD-B".
'''
    assert BoundedLrfSingletonRewriter._source_accesses(source) == [
        ("FIRST", "RECORD-A"), ("NEXT", "RECORD-A")
    ]
    assert BoundedLrfSingletonRewriter._source_proves_first_only(source) is False


def test_source_access_scanner_detects_next_wrapped_across_physical_lines():
    source = '''000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     OBTAIN
000300-        NEXT
000400-        RECORD-A WITHIN SET-A.
'''
    assert BoundedLrfSingletonRewriter._source_accesses(source) == [
        ("FIRST", "RECORD-A"), ("NEXT", "RECORD-A")
    ]
    assert BoundedLrfSingletonRewriter._source_proves_first_only(source) is False


def test_source_access_scanner_does_not_detect_wrapped_tokens_inside_literals_or_comments():
    source = '''000100     OBTAIN FIRST RECORD-A WITHIN SET-A.
000200     DISPLAY "OBTAIN
000300-        NEXT RECORD-A".
000400     DISPLAY "OK" *> OBTAIN
000500-        NEXT RECORD-A
'''
    assert BoundedLrfSingletonRewriter._source_accesses(source) == [("FIRST", "RECORD-A")]
    assert BoundedLrfSingletonRewriter._source_proves_first_only(source) is True
