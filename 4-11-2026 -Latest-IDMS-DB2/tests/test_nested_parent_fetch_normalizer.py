"""Reusable nested parent loop semantics, not a program-specific COBOL patch."""
import re
from pathlib import Path

from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import (
    NestedParentFetchNormalizer,
    _body,
)


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / 'tests/fixtures/legacy_generated/VMDZ4420_26-10-2026_052553.cbl'


def _sample():
    # Check a stable fixture rather than transient Output files.
    # The legacy fixture may differ from V111; normalize a minimal verified
    # record-independent example for deterministic assertions.
    return '''
       IDENTIFICATION DIVISION.
       PROGRAM-ID. NESTED.
       PROCEDURE DIVISION.
           PERFORM 2100-OPEN-APARENT
           PERFORM 2200-FETCH-APARENT.
           PERFORM HANDLE-ROW
             UNTIL APARENT-EOC.
           PERFORM 2300-CLOSE-APARENT.
           STOP RUN.
       HANDLE-ROW.
           PERFORM 3100-OPEN-BCHILD
           PERFORM 3200-FETCH-BCHILD UNTIL BCHILD-EOC
           PERFORM 3300-CLOSE-BCHILD
           PERFORM WRITE-ROW
           PERFORM 2200-FETCH-APARENT.
       WRITE-ROW.
           WRITE OUTPUT-REC.
       2100-OPEN-APARENT.
           EXEC SQL OPEN APARENT END-EXEC.
       2200-FETCH-APARENT.
           EXEC SQL FETCH APARENT END-EXEC
           EVALUATE SQLCODE
             WHEN ZERO
               ADD 1 TO ROWS-READ
               CONTINUE
             WHEN 100
               SET APARENT-EOC TO TRUE
             WHEN OTHER
               PERFORM SQLERROR
           END-EVALUATE.
       2300-CLOSE-APARENT.
           EXEC SQL CLOSE APARENT END-EXEC.
       3100-OPEN-BCHILD.
           EXEC SQL OPEN BCHILD END-EXEC.
       3200-FETCH-BCHILD.
           EXEC SQL FETCH BCHILD END-EXEC.
       3300-CLOSE-BCHILD.
           EXEC SQL CLOSE BCHILD END-EXEC.
'''


def test_successful_parent_fetch_calls_exactly_one_business_paragraph():
    source = _sample()
    normalizer = NestedParentFetchNormalizer()
    result = normalizer.apply(source)
    assert normalizer.messages
    lines = [_body(line).upper() for line in result.splitlines()]
    assert 'PERFORM 2200-FETCH-APARENT UNTIL APARENT-EOC.' in lines
    assert 'PERFORM HANDLE-ROW UNTIL APARENT-EOC.' not in lines
    assert 'PERFORM HANDLE-ROW' in lines
    assert lines.count('PERFORM HANDLE-ROW') == 1
    assert lines.count('PERFORM 2200-FETCH-APARENT') == 0
    assert 'PERFORM 3100-OPEN-BCHILD' in lines
    assert 'PERFORM 3300-CLOSE-BCHILD' in lines
    assert normalizer.apply(result) == result


def test_renaming_cursor_business_paragraph_and_child_is_supported():
    source = (_sample().replace('APARENT', 'PARENTX')
              .replace('BCHILD', 'EVENTX')
              .replace('HANDLE-ROW', 'DO-WORK'))
    normalizer = NestedParentFetchNormalizer()
    result = normalizer.apply(source)
    assert normalizer.messages
    assert 'PERFORM DO-WORK' in result
    assert 'PERFORM 2200-FETCH-PARENTX UNTIL PARENTX-EOC' in result


def test_rejects_ambiguous_graph_without_touching_source():
    source = _sample().replace('PERFORM 2200-FETCH-APARENT.\n       WRITE-ROW.',
                               'PERFORM 2200-FETCH-APARENT.\n           PERFORM EXTRA-WORK\n       WRITE-ROW.')
    assert NestedParentFetchNormalizer().apply(source) == source


def test_rejects_existing_row_business_link():
    source = _sample().replace('               CONTINUE\n             WHEN 100',
                               '               PERFORM HANDLE-ROW\n             WHEN 100')
    assert NestedParentFetchNormalizer().apply(source) == source


def test_real_nested_parent_cursor_fixture():
    # Immutable V111 generated baseline, not an Output directory artifact.
    source = (ROOT / 'tests/fixtures/parent_nested_cursor_before_normalization.cbl').read_text()
    normalizer = NestedParentFetchNormalizer()
    result = normalizer.apply(source)
    assert len(normalizer.messages) == 1
    body = '\n'.join(_body(line).upper() for line in result.splitlines())
    assert 'PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC' in body
    assert 'PERFORM HOOFDVERWERKING' in body
    assert len(re.findall(r'\bPERFORM HOOFDVERWERKING\b', body)) == 1
    assert 'PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR' in body
    assert "SW-STATUS-D = 'Y'" in body
    assert 'PERFORM VERWERK-VMBEVEF' in body
    assert 'PERFORM WRITE-UITRECORD' in body
    assert 'WRITE UITRECORD' in body
    assert 'PERFORM 2300-CLOSE-DZBEFFC1' in body
    assert 'PERFORM 3300-CLOSE-DZEVEFC1' in body
    assert normalizer.apply(result) == result
