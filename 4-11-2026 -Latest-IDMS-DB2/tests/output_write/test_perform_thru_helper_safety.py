from converter.composers.output_write_paragraph_composer import OutputWriteParagraphComposer
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
from converter.services.perform_thru_scope import perform_spans, paragraph_indices


def fmt(text):
    if text.endswith('DIVISION.') or (text.endswith('.') and ' ' not in text):
        return '       ' + text
    return '           ' + text


def source():
    content = [
        'PROCEDURE DIVISION.',
        'PERFORM BEGINNING THRU BEGINNING-EXIT',
        'PERFORM BUSINESS THRU BUSINESS-EXIT UNTIL EOF',
        'GOBACK.',
        'BEGINNING.',
        'MOVE SPACES TO REC-FORM',
        'BEGINNING-EXIT.',
        'EXIT.',
        'BUSINESS.',
        "IF WS-DATE < CUTOFF",
        'ADD 1 TO WS-TELLER',
        'MOVE WS-TELLER TO F-TELLER',
        'MOVE FIELD-A TO F-A',
        'WRITE FORM-REC FROM REC-FORM',
        'END-IF',
        'PERFORM FETCH-NEXT',
        'BUSINESS-EXIT.',
        'EXIT.',
        'FETCH-NEXT.',
        'CONTINUE.',
    ]
    return '\n'.join(map(fmt, content))


def test_extracted_paragraph_is_after_thru_exit_and_reset_per_record():
    code = OutputWriteParagraphComposer().compose(source())
    lines = code.splitlines()
    labels = paragraph_indices(lines)
    assert labels['BUSINESS'] < labels['BUSINESS-EXIT'] < labels['WRITE-FORM-REC']
    helper = code.upper().split('WRITE-FORM-REC.')[1].split('FETCH-NEXT.')[0]
    assert 'MOVE SPACES TO REC-FORM' in helper
    assert helper.index('MOVE SPACES TO REC-FORM') < helper.index('MOVE WS-TELLER')
    assert not any(i.code == 'WRITE_HELPER_INSIDE_PERFORM_THRU' for i in validate_generated_cobol(code))
    assert len(perform_spans(lines)) == 2


def test_release_gate_rejects_unguarded_helper_inside_thru():
    source_text = source()
    broken = source_text.replace(
        fmt('BUSINESS-EXIT.'),
        '\n'.join([fmt('WRITE-FORM-REC.'), fmt('WRITE FORM-REC FROM REC-FORM.'), fmt('BUSINESS-EXIT.')]),
    ).replace(fmt('MOVE FIELD-A TO F-A'), fmt('PERFORM WRITE-FORM-REC'))
    assert any(i.code == 'WRITE_HELPER_INSIDE_PERFORM_THRU' for i in validate_generated_cobol(broken))


def test_no_duplicate_reset_without_proven_source_clear():
    code = source().replace(fmt('MOVE SPACES TO REC-FORM'), fmt('CONTINUE'))
    result = OutputWriteParagraphComposer().compose(code)
    assert 'MOVE SPACES TO REC-FORM' not in result
