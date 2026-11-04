"""Generic flat FETCH/control-flow and final layout regressions."""
from __future__ import annotations

import re

from converter.composers.cursor_close_guarantee.flat_fetch_drive_normalizer import FlatFetchDriveNormalizer
from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import _body
from converter.composers.procedure_indent_normalizer import ProcedureIndentNormalizer


def _source(cursor='APARENT', business='PROCESS-ROW', extra=''):
    return f'''       IDENTIFICATION DIVISION.
       PROGRAM-ID. EXAMPLE.
       PROCEDURE DIVISION.
           PERFORM SETUP THRU SETUP-EXIT.
           PERFORM {business} THRU {business}-EXIT
                UNTIL {cursor}-EOC.
                PERFORM 2300-CLOSE-{cursor}.
           GOBACK.
       SETUP.
           OPEN OUTPUT OUTFILE.
           PERFORM 2100-OPEN-{cursor}.
           PERFORM 2200-FETCH-{cursor}.
       SETUP-EXIT.
           EXIT.
       {business}.
           IF ONE = TWO
               PERFORM WRITE-ROW
           END-IF.
           PERFORM 2200-FETCH-{cursor}.
       {business}-EXIT.
           EXIT.
       WRITE-ROW.
           WRITE OUTREC.
       2100-OPEN-{cursor}.
           EXEC SQL OPEN {cursor} END-EXEC
           EVALUATE SQLCODE
             WHEN ZERO
               SET {cursor}-NOT-EOC TO TRUE
             WHEN OTHER
               PERFORM SQLERROR
           END-EVALUATE.
       2200-FETCH-{cursor}.
           EXEC SQL FETCH {cursor} END-EXEC
           EVALUATE SQLCODE
             WHEN ZERO
               ADD 1 TO WS-ROW-COUNT
               CONTINUE
             WHEN 100
               SET {cursor}-EOC TO TRUE
             WHEN OTHER
               PERFORM SQLERROR
           END-EVALUATE.
       2300-CLOSE-{cursor}.
           EXEC SQL CLOSE {cursor} END-EXEC.
       {extra}
'''


def _logical(text):
    return [b for x in text.splitlines() if (b := _body(x).upper())]


def test_split_prime_and_advance_become_one_fetch_driver():
    t = _source()
    n = FlatFetchDriveNormalizer()
    new = n.apply(t)
    assert n.messages
    b = _logical(new)
    assert sum(re.match(r'PERFORM 2200-FETCH-APARENT\b', x) is not None for x in b) == 1
    assert 'PERFORM 2200-FETCH-APARENT UNTIL APARENT-EOC.' in b
    assert 'PERFORM PROCESS-ROW THRU PROCESS-ROW-EXIT' in b
    assert not any(x.startswith('PERFORM PROCESS-ROW THRU') and 'UNTIL' in x for x in b)
    assert 'PERFORM 2300-CLOSE-APARENT.' in b
    assert 'PERFORM WRITE-ROW' in b
    assert n.apply(new) == new


def test_identifiers_are_discovered_not_hardcoded():
    changed = _source(cursor='DIFFERENT', business='DO-BUSINESS')
    out = FlatFetchDriveNormalizer().apply(changed)
    assert 'PERFORM 2200-FETCH-DIFFERENT UNTIL DIFFERENT-EOC.' in out
    assert 'PERFORM DO-BUSINESS THRU DO-BUSINESS-EXIT' in out


def test_ambiguous_third_fetch_call_is_rejected():
    src = _source(extra='       EXTRA.\n           PERFORM 2200-FETCH-APARENT.')
    assert FlatFetchDriveNormalizer().apply(src) == src


def test_existing_fetch_business_action_is_rejected():
    src = _source().replace('               CONTINUE\n             WHEN 100',
                            '               PERFORM PROCESS-ROW\n             WHEN 100')
    assert FlatFetchDriveNormalizer().apply(src) == src


def test_nonterminal_fetch_is_rejected():
    src = _source().replace('           PERFORM 2200-FETCH-APARENT.\n       PROCESS-ROW-EXIT',
                            '           PERFORM 2200-FETCH-APARENT.\n           ADD 1 TO EXTRA\n       PROCESS-ROW-EXIT')
    assert FlatFetchDriveNormalizer().apply(src) == src


def test_final_indent_reanchors_close_after_multiline_perform():
    before = _source()
    after = ProcedureIndentNormalizer().compose(before)
    assert any(x.startswith('    PERFORM 2300-CLOSE-APARENT.') for x in after.splitlines())
    assert not any(x.startswith('            PERFORM 2300-CLOSE-APARENT.') for x in after.splitlines())


def test_unmatched_eoc_loop_is_rejected():
    src = _source().replace('UNTIL APARENT-EOC.', 'UNTIL OTHER-CURSOR-EOC.')
    assert FlatFetchDriveNormalizer().apply(src) == src


def test_fixed_format_rewrite_has_no_leaked_sequence_tokens():
    # Fixed-format records must contain exactly one six-digit sequence area,
    # one indicator, 65 body characters and one eight-digit identification.
    # The original manual is not used as an expected rewrite: this is a
    # geometry check of artificially numbered, otherwise generic input.
    source = _source(cursor='ACURSOR', business='HANDLE-ROW')
    fixed = []
    for i, line in enumerate(source.splitlines(), 1):
        logical = line.strip()
        if not logical:
            continue
        indicator = ' '
        if logical.startswith('*'):
            indicator = '*'
        area_a = logical in {'SETUP.', 'SETUP-EXIT.', 'HANDLE-ROW.', 'HANDLE-ROW-EXIT.',
                             'WRITE-ROW.', '2100-OPEN-ACURSOR.', '2200-FETCH-ACURSOR.',
                             '2300-CLOSE-ACURSOR.'}
        pad = 0 if area_a else 4
        body = ' ' * pad + logical
        if len(body) > 65:
            raise AssertionError(f'fixture line overflow {logical}')
        fixed.append(f'{i:06d}{indicator}{body:<65}{i:08d}')
    out = FlatFetchDriveNormalizer().apply('\n'.join(fixed) + '\n')
    assert out != '\n'.join(fixed) + '\n'
    records = [line for line in out.splitlines() if line.strip()]
    assert all(len(line) == 80 and line[:6].isdigit() and line[72:80].isdigit() for line in records)
    assert all(not re.match(r'\s*\d{6}\s+PERFORM', line[7:72]) for line in records)


def test_setup_reused_outside_mainline_refuses_rewrite():
    src = _source(extra='       ANOTHER.\n           PERFORM SETUP THRU SETUP-EXIT.')
    assert FlatFetchDriveNormalizer().apply(src) == src
