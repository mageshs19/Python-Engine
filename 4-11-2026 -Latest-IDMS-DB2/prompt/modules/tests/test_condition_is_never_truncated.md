# `tests/test_condition_is_never_truncated.py`

Source: [tests/test_condition_is_never_truncated.py](../../../tests/test_condition_is_never_truncated.py) | 73 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `4d77eace119492443317d9f7ef7f425c793df8a9f08fe4439940b01a229a0dd1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> No pass may lose characters from a PROCEDURE DIVISION statement.

## Module-level bindings

`QUOTE` (L20), `ZERO8` (L21), `SOURCE` (L29)

## Import declarations

```python
from converter.composers.procedure_indent_normalizer import ProcedureIndentNormalizer
```

## Local dependency notes

- [converter/composers/procedure_indent_normalizer.py](../converter/composers/procedure_indent_normalizer.md)

## Symbol contracts and control points

### `fixed` - L24-L26

```python
fixed(seq: str, body: str, right: str) -> str
```

Observed calls (lexical order): `len`, `body.ljust`.

### `_tokens` - L43-L51

```python
_tokens(text: str) -> str
```

Every non-blank character of every body, order preserved.

Observed calls (lexical order): `text.splitlines`, `len`, `''.join`, `body.split`, `out.append`.

Control points:

- L47: `for line in text.splitlines()`

### `test_no_character_is_lost` - L54-L57

```python
test_no_character_is_lost()
```

Observed calls (lexical order): `ProcedureIndentNormalizer`, `ProcedureIndentNormalizer().compose`, `_tokens`.

### `test_no_identifier_is_cut_in_half` - L60-L65

```python
test_no_identifier_is_cut_in_half()
```

Observed calls (lexical order): `ProcedureIndentNormalizer`, `ProcedureIndentNormalizer().compose`, `result.count`.

### `test_every_record_stays_eighty_columns` - L68-L73

```python
test_every_record_stays_eighty_columns()
```

Observed calls (lexical order): `ProcedureIndentNormalizer`, `ProcedureIndentNormalizer().compose`, `result.splitlines`, `line[:6].isdigit`, `len`.

Control points:

- L71: `for line in result.splitlines()`
- L72: `if line[:6].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
