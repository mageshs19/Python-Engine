# `tests/layout/test_move_alignment.py`

Source: [tests/layout/test_move_alignment.py](../../../../tests/layout/test_move_alignment.py) | 470 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e07fd30da7bdaf8cba2f1d7ef05f2760ae8d70fd1b96e2e86d0bc2ed8f9197cb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Contract tests for MoveAlignmentComposer.

## Module-level bindings

`SEQ` (L22), `RIGHT` (L23), `BODY_WIDTH` (L24)

## Import declarations

```python
from __future__ import annotations
from converter.composers.move_alignment_composer import MoveAlignmentComposer
```

## Local dependency notes

- [converter/composers/move_alignment_composer.py](../../converter/composers/move_alignment_composer.md)

## Symbol contracts and control points

### `_fixed` - L30-L43

```python
_fixed(body: str, seq: str=SEQ, right: str=RIGHT) -> str
```

One 80-column record: 6 sequence, 1 indicator, 65 body, 8 right.

Observed calls (lexical order): `len`, `body.ljust`.

### `_marked` - L46-L51

```python
_marked(mark: str, body: str='', seq: str=SEQ, right: str=RIGHT) -> str
```

A record carrying `mark` in the indicator column (7).

Observed calls (lexical order): `len`, `body.ljust`.

### `_bodies` - L54-L55

```python
_bodies(text: str) -> list[str]
```

Observed calls (lexical order): `line[7:72].rstrip`, `text.rstrip`, `text.rstrip('\n').split`.

### `_mask` - L58-L77

```python
_mask(body: str) -> str
```

Blank the inside of quoted literals, preserving length.

Observed calls (lexical order): `out.append`, `''.join`.

Control points:

- L67: `for character in body`
- L68: `if quote`
- L70: `if character == quote`
- L73: `if character in ("'", '"')`

### `_to_column` - L80-L82

```python
_to_column(body: str) -> int
```

Column of the TO keyword, ignoring any TO inside a literal.

Observed calls (lexical order): `_mask`, `_mask(body).index`.

### `_words` - L85-L87

```python
_words(text: str) -> list[str]
```

Every token in document order, whitespace discarded.

Observed calls (lexical order): `_bodies`, `body.split`.

### `_compose` - L90-L92

```python
_compose(lines: list[str]) -> tuple[list[str], MoveAlignmentComposer]
```

Observed calls (lexical order): `MoveAlignmentComposer`, `'\n'.join`, `_bodies`, `composer.compose`.

### `test_a_run_shares_one_to_column` - L98-L105

```python
test_a_run_shares_one_to_column()
```

Observed calls (lexical order): `_compose`, `_fixed`, `_to_column`, `len`.

### `test_the_to_column_clears_the_longest_source` - L108-L116

```python
test_the_to_column_clears_the_longest_source()
```

Observed calls (lexical order): `_compose`, `_fixed`, `body.split`, `body.split(' TO ')[0].rstrip`, `len`, `max`, `_to_column`.

### `test_a_split_move_is_joined_then_aligned` - L119-L129

```python
test_a_split_move_is_joined_then_aligned()
```

Observed calls (lexical order): `_compose`, `_fixed`, `len`, `_to_column`, `any`, `message.lower`.

### `test_a_blank_line_starts_a_new_column` - L135-L146

```python
test_a_blank_line_starts_a_new_column()
```

Observed calls (lexical order): `_compose`, `_fixed`, `_to_column`.

### `test_when_clauses_do_not_break_the_run` - L149-L158

```python
test_when_clauses_do_not_break_the_run()
```

WHEN sits at a lesser indent, so the table spans it.

Observed calls (lexical order): `_compose`, `_fixed`, `_to_column`.

### `test_a_statement_at_the_same_indent_breaks_the_run` - L161-L171

```python
test_a_statement_at_the_same_indent_breaks_the_run()
```

Observed calls (lexical order): `_compose`, `_fixed`, `out[1].strip`, `_to_column`.

### `test_a_different_indent_starts_a_new_run` - L174-L184

```python
test_a_different_indent_starts_a_new_run()
```

Observed calls (lexical order): `_compose`, `_fixed`, `_to_column`.

### `test_a_single_move_is_left_alone` - L187-L193

```python
test_a_single_move_is_left_alone()
```

Observed calls (lexical order): `_compose`, `_fixed`, `out[0].strip`.

### `test_a_comment_inside_a_run_survives_verbatim` - L196-L204

```python
test_a_comment_inside_a_run_survives_verbatim()
```

Observed calls (lexical order): `_compose`, `_fixed`, `_marked`, `out[1].strip`, `_to_column`.

### `test_a_multi_receiver_move_stands_alone` - L210-L219

```python
test_a_multi_receiver_move_stands_alone()
```

Observed calls (lexical order): `_compose`, `_fixed`, `out[1].strip`, `out[0].index`, `out[1].index`.

### `test_a_continuation_receiver_sits_under_the_first` - L222-L231

```python
test_a_continuation_receiver_sits_under_the_first()
```

Observed calls (lexical order): `_compose`, `_fixed`, `len`, `out[0].index`, `out[1].lstrip`.

### `test_a_literal_containing_to_is_not_split_on` - L237-L245

```python
test_a_literal_containing_to_is_not_split_on()
```

Observed calls (lexical order): `_compose`, `_fixed`, `out[0].rstrip`, `out[0].rstrip().endswith`, `_to_column`.

### `test_a_quoted_date_literal_is_preserved` - L248-L255

```python
test_a_quoted_date_literal_is_preserved()
```

Observed calls (lexical order): `_compose`, `_fixed`, `_to_column`.

### `test_sql_bodies_are_never_touched` - L261-L272

```python
test_sql_bodies_are_never_touched()
```

Synthetic: SQL has no MOVE, but the guard must hold regardless.

Observed calls (lexical order): `_fixed`, `_compose`, `'\n'.join`, `_bodies`.

### `test_a_fetch_block_is_returned_unchanged` - L275-L286

```python
test_a_fetch_block_is_returned_unchanged()
```

Observed calls (lexical order): `_fixed`, `_compose`, `'\n'.join`, `_bodies`.

### `test_an_over_wide_run_is_refused_not_truncated` - L292-L315

```python
test_an_over_wide_run_is_refused_not_truncated()
```

A short source with a long target, pulled right by a long neighbour.

Observed calls (lexical order): `_compose`, `_fixed`, `' '.join`, `any`.

### `test_excessive_padding_is_refused` - L317-L324

```python
test_excessive_padding_is_refused()
```

Observed calls (lexical order): `_compose`, `_fixed`, `_to_column`, `any`.

### `test_a_refused_run_with_an_interior_line_does_not_crash` - L326-L348

```python
test_a_refused_run_with_an_interior_line_does_not_crash()
```

Heterogeneous AND refused - the combination that silently disabled the whole pass for a session.

Observed calls (lexical order): `_compose`, `_fixed`, `any`.

### `test_the_sentence_terminator_survives` - L350-L357

```python
test_the_sentence_terminator_survives()
```

Observed calls (lexical order): `_compose`, `_fixed`, `out[1].rstrip`, `out[1].rstrip().endswith`, `_to_column`.

### `test_no_token_is_lost_or_invented` - L360-L373

```python
test_no_token_is_lost_or_invented()
```

Observed calls (lexical order): `_fixed`, `'\n'.join`, `MoveAlignmentComposer`, `MoveAlignmentComposer().compose`, `_words`.

### `test_internal_spacing_inside_a_source_is_preserved` - L376-L384

```python
test_internal_spacing_inside_a_source_is_preserved()
```

'MM OF X' is the author's column alignment. Keep it.

Observed calls (lexical order): `_compose`, `_fixed`.

### `test_running_the_pass_twice_equals_running_it_once` - L390-L404

```python
test_running_the_pass_twice_equals_running_it_once()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `MoveAlignmentComposer`, `MoveAlignmentComposer().compose`.

### `test_an_already_aligned_run_reports_no_join` - L407-L416

```python
test_an_already_aligned_run_reports_no_join()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `MoveAlignmentComposer`, `composer.compose`, `any`, `message.lower`.

### `test_every_emitted_line_is_eighty_columns` - L422-L430

```python
test_every_emitted_line_is_eighty_columns()
```

Observed calls (lexical order): `'\n'.join`, `MoveAlignmentComposer`, `MoveAlignmentComposer().compose`, `_fixed`, `result.rstrip`, `result.rstrip('\n').split`, `len`.

Control points:

- L429: `for line in result.rstrip('\n').split('\n')`

### `test_no_body_reaches_column_seventy_three` - L433-L440

```python
test_no_body_reaches_column_seventy_three()
```

Observed calls (lexical order): `'\n'.join`, `MoveAlignmentComposer`, `MoveAlignmentComposer().compose`, `_fixed`, `_bodies`, `len`.

Control points:

- L439: `for body in _bodies(result)`

### `test_the_right_sequence_area_is_preserved` - L443-L450

```python
test_the_right_sequence_area_is_preserved()
```

Observed calls (lexical order): `'\n'.join`, `MoveAlignmentComposer`, `MoveAlignmentComposer().compose`, `_fixed`, `result.rstrip`, `result.rstrip('\n').split`.

Control points:

- L449: `for line in result.rstrip('\n').split('\n')`

### `test_empty_input_is_returned_unchanged` - L456-L457

```python
test_empty_input_is_returned_unchanged()
```

Observed calls (lexical order): `MoveAlignmentComposer`, `MoveAlignmentComposer().compose`.

### `test_a_document_with_no_moves_is_untouched` - L460-L470

```python
test_a_document_with_no_moves_is_untouched()
```

Observed calls (lexical order): `_fixed`, `_compose`, `'\n'.join`, `_bodies`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
