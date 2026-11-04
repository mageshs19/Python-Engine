# `converter/composers/cursor_flow/legacy_error_status_loop_normalizer.py`

Source: [converter/composers/cursor_flow/legacy_error_status_loop_normalizer.py](../../../../../converter/composers/cursor_flow/legacy_error_status_loop_normalizer.py) | 113 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `35a359b175eb55c47c2766782750a3babbdd054e871673342f0ae2de80373dc8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Normalize legacy IDMS status-driven loops only when cursor ownership is proven.

## Module-level bindings

`_NAME` (L14), `_FETCH_HEADER` (L15), `_PARAGRAPH_HEADER` (L16), `_PERFORM` (L17), `_LEGACY_LOOP` (L18)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
```

## Local dependency notes

- [converter/composers/cursor_flow_line_formatter.py](../cursor_flow_line_formatter.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_legacy_error_status_loop_normalizer.py](../../../tests/test_legacy_error_status_loop_normalizer.md)

## Symbol contracts and control points

### `LegacyErrorStatusLoopNormalizer` - L24-L113

```python
class LegacyErrorStatusLoopNormalizer()
```

### `LegacyErrorStatusLoopNormalizer.__init__` - L25-L27

```python
__init__(self, formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `LegacyErrorStatusLoopNormalizer.compose` - L29-L87

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self.formatter.normalize_line_endings`, `self.formatter.normalize_line_endings(str(text or '')).splitlines`, `str`, `self.formatter.logical`, `enumerate`, `_PARAGRAPH_HEADER.fullmatch`, `self._is_paragraph_header`, `len`, `match.group`, `match.group('name').upper`, `sorted`, `spans.items`, `range`, `self._is_comment`, `re.fullmatch`, `business_fetches.setdefault`.
Another 15 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L34: `for (i, body) in enumerate(logical)`
- L36: `if match and self._is_paragraph_header(lines[i])`
- L39: `for (pos, (start, name)) in enumerate(ordered)`
- L46: `for (business, (start, end)) in spans.items()`
- L51: `if not executable`
- L58: `if fetch_match`
- L64: `for (i, body) in enumerate(logical)`
- L66: `if not match`
- Another 4 conditions/loops exist in this source span.

### `LegacyErrorStatusLoopNormalizer._is_obsolete_warning` - L90-L92

```python
_is_obsolete_warning(logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').upper`.

### `LegacyErrorStatusLoopNormalizer._blank_comment` - L95-L99

```python
_blank_comment(line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `value[:6].isdigit`.

Control points:

- L97: `if len(value) >= 80 and value[:6].isdigit()`

### `LegacyErrorStatusLoopNormalizer._is_comment` - L102-L106

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `value[:6].isdigit`, `value.lstrip`, `value.lstrip().startswith`.

Control points:

- L104: `if len(value) >= 7 and value[:6].isdigit()`

### `LegacyErrorStatusLoopNormalizer._is_paragraph_header` - L109-L113

```python
_is_paragraph_header(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `value[:6].isdigit`, `bool`, `value[7:72].startswith`, `value.startswith`.

Control points:

- L111: `if len(value) >= 8 and value[:6].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
