# `converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.py`

Source: [converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.py](../../../../../converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.py) | 187 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `680118c715653dbad94764e6d4efc0212fd4d84a8dc454bba30a03a96937148e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Normalize a proven split COBOL cursor loop to one FETCH-driven loop.

## Module-level bindings

`_NAME` (L21), `_PARA` (L22), `_FETCH_NAME` (L23), `_SETUP_CALL` (L24), `_DRIVER` (L25), `__all__` (L187)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import _body
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.py](nested_parent_fetch_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../../pipeline/conversion/conversion_pipeline.md)
- [tests/test_generic_flat_fetch_drive_normalizer.py](../../../tests/test_generic_flat_fetch_drive_normalizer.md)

## Symbol contracts and control points

### `_replace` - L28-L42

```python
_replace(line: str, logical: str) -> str
```

Rebuild all 80 columns, not just the new executable body.

Observed calls (lexical order): `len`, `ValueError`, `line[:6].isdigit`.

Control points:

- L37: `if len(body) > 65`
- L39: `if len(line) >= 7 and line[:6].isdigit()`

Explicit raises: `ValueError('cursor rewrite would overflow the fixed-format body')`.

### `FlatFetchDriveNormalizer` - L45-L184

```python
class FlatFetchDriveNormalizer()
```

### `FlatFetchDriveNormalizer.__init__` - L46-L47

```python
__init__(self) -> None
```

### `FlatFetchDriveNormalizer.apply` - L49-L184

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).splitlines`, `_body`, `_body(line).upper`, `enumerate`, `item.startswith`, `next`, `len`, `range`, `_PARA.fullmatch`, `matched.group`, `line[:6].isdigit`, `line.lstrip`, `headers.append`, `_FETCH_NAME.fullmatch`, `cm.group`.
Another 25 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L54: `if proc < 0`
- L57: `for i in range(proc + 1, len(lines))`
- L60: `if not matched or matched.group(1) in {'EXIT', 'GOBACK', 'CONTINUE', 'END-EXEC'}`
- L63: `if len(line) >= 7 and line[:6].isdigit()`
- L67: `if area_a`
- L69: `if not headers`
- L77: `for fetch in spans`
- L79: `if not cm`
- Another 29 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
