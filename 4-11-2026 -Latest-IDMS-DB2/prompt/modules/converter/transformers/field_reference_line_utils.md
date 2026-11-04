# `converter/transformers/field_reference_line_utils.py`

Source: [converter/transformers/field_reference_line_utils.py](../../../../converter/transformers/field_reference_line_utils.py) | 108 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `182f0fd291cf654923a33f2efd2fa19b2256eafc5ffc383ef49efbc492c22807`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.field_reference_rewriter_patterns import DCL_DOT_REFERENCE_PATTERN, HOST_OF_DCL_REFERENCE_PATTERN, STRING_PATTERN
```

## Local dependency notes

- [patterns/field_reference_rewriter_patterns.py](../../patterns/field_reference_rewriter_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference_rewriter.py](field_reference_rewriter.md)

## Symbol contracts and control points

### `FieldReferenceLineUtils` - L10-L108

```python
class FieldReferenceLineUtils()
```

Line-level helpers for field reference rewriting.

### `FieldReferenceLineUtils.logical_line` - L17-L37

```python
logical_line(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `left.strip`, `left.strip().isdigit`, `body.rstrip`, `body.strip`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[6:].strip`, `text.strip`.

Control points:

- L23: `if len(text) >= 80`
- L28: `if left.strip().isdigit()`
- L29: `if indicator in {'*', '/'}`
- L34: `if len(text) > 6 and text[:6].strip().isdigit()`

### `FieldReferenceLineUtils.is_comment_or_blank` - L39-L55

```python
is_comment_or_blank(self, line: str) -> bool
```

Observed calls (lexical order): `self.logical_line`, `str`, `str(logical or '').strip`, `stripped.startswith`.

Control points:

- L46: `if not stripped`
- L49: `if stripped.startswith('*')`
- L52: `if stripped.startswith('/')`

### `FieldReferenceLineUtils.has_existing_dclgen_reference` - L57-L72

```python
has_existing_dclgen_reference(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').upper`, `DCL_DOT_REFERENCE_PATTERN.search`, `HOST_OF_DCL_REFERENCE_PATTERN.search`.

Control points:

- L63: `if ' OF DCL' in upper`
- L66: `if DCL_DOT_REFERENCE_PATTERN.search(upper)`
- L69: `if HOST_OF_DCL_REFERENCE_PATTERN.search(upper)`

### `FieldReferenceLineUtils.split_string_segments` - L74-L108

```python
split_string_segments(self, line: str) -> list[tuple[str, bool]]
```

Observed calls (lexical order): `str`, `STRING_PATTERN.finditer`, `match.start`, `output.append`, `match.group`, `match.end`, `len`.

Control points:

- L82: `for match in STRING_PATTERN.finditer(text)`
- L83: `if match.start() > last_index`
- L100: `if last_index < len(text)`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
