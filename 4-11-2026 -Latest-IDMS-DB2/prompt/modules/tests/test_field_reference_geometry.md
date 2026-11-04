# `tests/test_field_reference_geometry.py`

Source: [tests/test_field_reference_geometry.py](../../../tests/test_field_reference_geometry.py) | 104 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a9ba8a7c495b16329041f658060f41c9f794db68b7b190126bd1500e9a70f469`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format geometry of the qualified field rewrite.

## Module-level bindings

`QUOTE` (L27), `ZERO8` (L28), `SOURCE` (L36)

## Import declarations

```python
import pytest
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.transformers.field_reference_rewriter import FieldReferenceRewriter
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../converter/services/fixed_format_line_service.md)
- [converter/transformers/field_reference_rewriter.py](../converter/transformers/field_reference_rewriter.md)

## Symbol contracts and control points

### `fixed` - L31-L33

```python
fixed(seq: str, body: str, right: str) -> str
```

Observed calls (lexical order): `len`, `body.ljust`.

### `rewriter` - L49-L55

```python
rewriter(transformer_context)
```

Reuses the shared repositories from tests/conftest.py.

Observed calls (lexical order): `FieldReferenceRewriter`.

### `test_every_emitted_record_keeps_its_geometry` - L58-L68

```python
test_every_emitted_record_keeps_its_geometry(rewriter)
```

Observed calls (lexical order): `rewriter.rewrite`, `output.splitlines`, `line.strip`, `line[:6].isdigit`, `len`, `line[72:80].isdigit`.

Control points:

- L61: `for line in output.splitlines()`
- L62: `if not line.strip()`
- L64: `if not line[:6].isdigit()`

### `test_no_stray_sequence_digit_leaks_into_the_body` - L71-L76

```python
test_no_stray_sequence_digit_leaks_into_the_body(rewriter)
```

Observed calls (lexical order): `rewriter.rewrite`, `output.splitlines`, `len`, `line[7:72].rstrip`, `body.endswith`.

Control points:

- L74: `for line in output.splitlines()`

### `test_trailing_blanks_are_preserved` - L79-L85

```python
test_trailing_blanks_are_preserved(rewriter)
```

Blanks in columns 8-72 position the right sequence at column 73.

Observed calls (lexical order): `rewriter.rewrite`, `line[:6].isdigit`, `output.splitlines`, `all`, `len`.

### `test_a_line_with_no_reference_is_untouched` - L88-L93

```python
test_a_line_with_no_reference_is_untouched(rewriter)
```

Observed calls (lexical order): `rewriter.rewrite`, `any`, `output.splitlines`.

### `test_existing_db2_host_does_not_hide_another_qualified_legacy_field` - L95-L104

```python
test_existing_db2_host_does_not_hide_another_qualified_legacy_field(rewriter)
```

Observed calls (lexical order): `rewriter._build_reference_maps`, `next`, `rewriter.record_field_map.items`, `fields.items`, `iter`, `record.replace`, `rewriter.rewrite`, `' '.join`, `line[7:72].strip`, `output.splitlines`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
