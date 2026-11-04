# `converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.py`

Source: [converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.py](../../../../../converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.py) | 153 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `217a19e2456a9b98646e9d15ac4594f354bf0a37f9f1042f702fd7a5c435ebb5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Conservatively make nested parent cursors FETCH-driven.

## Module-level bindings

`_NAME` (L19), `_HEADER` (L20), `_FETCH` (L21), `_PROCEDURE` (L22), `_PERFORM` (L23)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.py](flat_fetch_drive_normalizer.md)
- [converter/pipeline/conversion/conversion_pipeline.py](../../pipeline/conversion/conversion_pipeline.md)
- [tests/test_generic_flat_fetch_drive_normalizer.py](../../../tests/test_generic_flat_fetch_drive_normalizer.md)
- [tests/test_nested_parent_fetch_normalizer.py](../../../tests/test_nested_parent_fetch_normalizer.md)

## Symbol contracts and control points

### `_body` - L26-L34

```python
_body(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line).rstrip`, `len`, `text[:6].isdigit`, `text[7:72].strip`, `text.lstrip`, `text.lstrip().startswith`, `text.strip`.

Control points:

- L28: `if len(text) >= 7 and text[:6].isdigit()`
- L29: `if text[6] in '*/Dd-'`
- L32: `if text.lstrip().startswith('*')`

### `_as_intermediate` - L37-L39

```python
_as_intermediate(body: str) -> str
```

### `NestedParentFetchNormalizer` - L42-L153

```python
class NestedParentFetchNormalizer()
```

### `NestedParentFetchNormalizer.__init__` - L43-L44

```python
__init__(self) -> None
```

### `NestedParentFetchNormalizer.apply` - L46-L153

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `_body`, `_body(x).upper`, `_PROCEDURE.match`, `enumerate`, `next`, `len`, `range`, `_HEADER.fullmatch`, `raw.lstrip`, `raw[:6].isdigit`, `bodies[i].startswith`, `headers.append`, `m.group`, `_FETCH.fullmatch`, `any`.
Another 15 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L51: `if procedure < 0`
- L55: `for i in range(procedure + 1, len(lines))`
- L61: `if m and area_a and (not bodies[i].startswith(('END-', 'STOP ')))`
- L63: `if not headers`
- L72: `for (fetch, fetch_start) in headers`
- L74: `if not m`
- L82: `if end_zero < 0 or not any((bodies[i] == 'CONTINUE' for i in range(zero_at + 1, end_zero)))`
- L84: `if not any((bodies[i].startswith('WHEN 100') for i in range(end_zero, fe)))`
- Another 16 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
