# `tests/test_output_write_paragraph_composer.py`

Source: [tests/test_output_write_paragraph_composer.py](../../../tests/test_output_write_paragraph_composer.py) | 142 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `5c9fa0f00900958801618a5f5a9da11c204a062fd8b01f76e06348b7b4538f52`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Output write paragraph extraction tests.

## Import declarations

```python
from converter.composers.output_write_paragraph_composer import OutputWriteParagraphComposer
```

## Local dependency notes

- [converter/composers/output_write_paragraph_composer.py](../converter/composers/output_write_paragraph_composer.md)

## Symbol contracts and control points

### `_fixed` - L11-L13

```python
_fixed(body: str, seq: str='001000', right: str='01000000') -> str
```

One 80-column fixed-format line.

Observed calls (lexical order): `body[:65].ljust`.

### `_program` - L16-L30

```python
_program() -> str
```

Observed calls (lexical order): `'\n'.join`, `_fixed`.

### `test_write_block_is_extracted_into_its_own_paragraph` - L33-L38

```python
test_write_block_is_extracted_into_its_own_paragraph()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `_program`, `out.count`.

### `test_population_statements_move_into_the_new_paragraph` - L41-L46

```python
test_population_statements_move_into_the_new_paragraph()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `_program`, `out.split`.

### `test_counter_increment_is_added_at_the_call_site` - L49-L53

```python
test_counter_increment_is_added_at_the_call_site()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `_program`, `out.split`.

### `test_guard_conditions_are_left_untouched` - L56-L60

```python
test_guard_conditions_are_left_untouched()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `_program`.

### `test_every_line_stays_eighty_columns` - L63-L68

```python
test_every_line_stays_eighty_columns()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `_program`, `out.splitlines`, `line.strip`, `len`, `repr`.

Control points:

- L66: `for line in out.splitlines()`
- L67: `if line.strip()`

### `test_diagnostics_report_the_extraction` - L71-L77

```python
test_diagnostics_report_the_extraction()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `_program`, `composer.compose`, `' '.join`.

### `test_two_writes_are_left_alone` - L80-L89

```python
test_two_writes_are_left_alone()
```

Observed calls (lexical order): `_program`, `_program().replace`, `_fixed`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`.

### `test_extraction_is_idempotent` - L92-L97

```python
test_extraction_is_idempotent()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `_program`, `composer.compose`.

### `test_program_without_a_write_is_unchanged` - L100-L110

```python
test_program_without_a_write_is_unchanged()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`.

### `test_every_guard_stays_at_the_call_site` - L119-L130

```python
test_every_guard_stays_at_the_call_site()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `_program`, `out.partition`.

### `test_the_counter_is_guarded_by_the_write_decision` - L133-L142

```python
test_the_counter_is_guarded_by_the_write_decision()
```

ADD 1 must sit INSIDE the condition that decides the write.

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `_program`, `len`, `line[7:72].strip`, `out.splitlines`, `bodies.index`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
