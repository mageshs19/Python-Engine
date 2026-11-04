# `tests/test_fetch_error_diagnostics.py`

Source: [tests/test_fetch_error_diagnostics.py](../../../tests/test_fetch_error_diagnostics.py) | 231 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `dee98bdfbda2f2d0cab31c34dd056d0221672968bc68b90028881939694c3215`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The FETCH error branch must identify the failing row.

## Module-level bindings

`CURSOR` (L31), `GROUP` (L32), `SQL_ERROR` (L33), `FIELDS` (L34), `HOSTS` (L39), `BODY_END_COLUMN` (L42)

## Import declarations

```python
import pytest
from converter.generators.cursor_paragraph.cursor_paragraph_body_builder import CursorParagraphBodyBuilder
from rules.cursor_paragraph_rules import FETCH_KEY_DIAGNOSTIC_LIMIT
```

## Local dependency notes

- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](../converter/generators/cursor_paragraph/cursor_paragraph_body_builder.md)
- [rules/cursor_paragraph_rules.py](../rules/cursor_paragraph_rules.md)

## Symbol contracts and control points

### `paragraphs` - L46-L47

```python
paragraphs()
```

Observed calls (lexical order): `CursorParagraphBodyBuilder`.

### `_bodies` - L50-L51

```python
_bodies(lines: list[str]) -> list[str]
```

Observed calls (lexical order): `line.strip`.

### `_fetch_lines` - L54-L60

```python
_fetch_lines(paragraphs, hosts)
```

Observed calls (lexical order): `paragraphs.fetch_paragraph`.

### `_fetch` - L63-L64

```python
_fetch(paragraphs, hosts)
```

Observed calls (lexical order): `_bodies`, `_fetch_lines`.

### `_when_other_block` - L67-L74

```python
_when_other_block(bodies: list[str]) -> list[str]
```

Statements between WHEN OTHER and END-EVALUATE.

Observed calls (lexical order): `bodies.index`, `next`, `enumerate`, `body.upper`, `body.upper().startswith`.

### `test_the_error_text_is_the_first_statement` - L80-L84

```python
test_the_error_text_is_the_first_statement(paragraphs)
```

The reference sets SQL-LOCATION at paragraph entry, not here.

Observed calls (lexical order): `_fetch`, `_when_other_block`, `block[0].startswith`.

### `test_the_error_branch_does_not_restate_sql_location` - L87-L90

```python
test_the_error_branch_does_not_restate_sql_location(paragraphs)
```

Observed calls (lexical order): `_fetch`, `_when_other_block`, `any`, `body.endswith`.

### `test_sql_location_is_set_once_at_paragraph_entry` - L93-L98

```python
test_sql_location_is_set_once_at_paragraph_entry(paragraphs)
```

Observed calls (lexical order): `_fetch`, `b.endswith`, `len`, `bodies.index`.

### `test_perform_sqlerror_is_still_the_last_statement` - L100-L103

```python
test_perform_sqlerror_is_still_the_last_statement(paragraphs)
```

Observed calls (lexical order): `_fetch`, `_when_other_block`.

### `test_diagnostics_sit_between_the_error_text_and_the_perform` - L106-L113

```python
test_diagnostics_sit_between_the_error_text_and_the_perform(paragraphs)
```

Observed calls (lexical order): `' '.join`, `_fetch`, `_when_other_block`, `joined.index`.

### `test_every_fetched_column_is_displayed` - L119-L123

```python
test_every_fetched_column_is_displayed(paragraphs)
```

Observed calls (lexical order): `' '.join`, `_fetch`, `_when_other_block`.

Control points:

- L122: `for field in FIELDS`

### `test_each_displayed_host_is_group_qualified` - L126-L130

```python
test_each_displayed_host_is_group_qualified(paragraphs)
```

An unqualified DISPLAY operand may not compile.

Observed calls (lexical order): `' '.join`, `_fetch`, `_when_other_block`, `joined.count`, `len`.

### `test_the_display_list_is_capped` - L133-L138

```python
test_the_display_list_is_capped(paragraphs)
```

Observed calls (lexical order): `range`, `_fetch`, `_when_other_block`, `b.startswith`, `len`.

### `test_the_of_host_form_is_accepted` - L144-L151

```python
test_the_of_host_form_is_accepted(paragraphs)
```

The resolver may deliver 'FIELD OF GROUP'.

Observed calls (lexical order): `' '.join`, `_fetch`, `_when_other_block`.

### `test_an_unqualified_host_is_skipped_not_guessed` - L154-L159

```python
test_an_unqualified_host_is_skipped_not_guessed(paragraphs)
```

Observed calls (lexical order): `_fetch`, `_when_other_block`, `any`, `block[0].startswith`.

### `test_no_hosts_leaves_the_generic_branch_intact` - L162-L167

```python
test_no_hosts_leaves_the_generic_branch_intact(paragraphs)
```

Observed calls (lexical order): `_fetch`, `_when_other_block`, `any`, `len`.

### `test_open_and_close_gain_no_diagnostics` - L172-L187

```python
test_open_and_close_gain_no_diagnostics(paragraphs)
```

Only FETCH has a fetched row worth reporting.

Observed calls (lexical order): `paragraphs.open_paragraph`, `paragraphs.close_paragraph`, `' '.join`, `_bodies`, `_when_other_block`, `any`.

Control points:

- L174: `for lines in (paragraphs.open_paragraph(cursor_name=CURSOR, paragraph_name=f'710-OPEN-{CURSOR}', sql_error_paragraph=SQL_ERROR), paragraphs.close_paragraph(cursor_name=CURSOR, parag...`

### `test_no_generated_body_line_passes_column_72` - L193-L198

```python
test_no_generated_body_line_passes_column_72(paragraphs)
```

A DISPLAY that overflows is wrapped, never truncated.

Observed calls (lexical order): `_fetch_lines`, `len`.

Control points:

- L197: `for line in _fetch_lines(paragraphs, [f':{GROUP}.{field}'])`

### `test_a_maximum_length_name_never_overflows` - L201-L206

```python
test_a_maximum_length_name_never_overflows(paragraphs)
```

A COBOL data-name may be 30 characters.

Observed calls (lexical order): `_fetch_lines`, `len`.

Control points:

- L205: `for line in _fetch_lines(paragraphs, [f':{GROUP}.{field}'])`

### `test_a_long_host_keeps_its_full_name` - L209-L217

```python
test_a_long_host_keeps_its_full_name(paragraphs)
```

Truncation would produce an undefined data-name.

Observed calls (lexical order): `' '.join`, `_fetch`, `_when_other_block`.

### `test_a_long_host_wraps_onto_three_lines` - L220-L231

```python
test_a_long_host_wraps_onto_three_lines(paragraphs)
```

43 fixed columns leave 22 for the operand; this one needs 29.

Observed calls (lexical order): `_fetch`, `_when_other_block`, `b.startswith`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
