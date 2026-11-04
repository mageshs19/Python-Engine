# `converter/composers/lrf_key_binding_composer.py`

Source: [converter/composers/lrf_key_binding_composer.py](../../../../converter/composers/lrf_key_binding_composer.py) | 157 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `d4f716b45ae556faa36f595de11720effee1e2cb31a41a4c907638510f9a326c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Apply validated LRF key bindings and status ownership to generated COBOL.

## Module-level bindings

`__all__` (L157)

## Import declarations

```python
from __future__ import annotations
import re
from converter.generators.initialization.line_geometry import LineGeometry
from rules.lrf_conversion_rules import LRF_PARENT_NOT_FOUND_TOKEN
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../generators/initialization/line_geometry.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [rules/lrf_conversion_rules.py](../../rules/lrf_conversion_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_lrf_key_binding_composer.py](../../tests/test_lrf_key_binding_composer.md)

## Symbol contracts and control points

### `LrfKeyBindingComposer` - L14-L154

```python
class LrfKeyBindingComposer()
```

### `LrfKeyBindingComposer.__init__` - L15-L17

```python
__init__(self) -> None
```

Observed calls (lexical order): `LineGeometry`.

### `LrfKeyBindingComposer.compose` - L19-L118

```python
compose(self, text: str, child_moves_by_group: dict[str, list[str]] | None=None) -> str
```

Observed calls (lexical order): `self.geometry.split`, `list`, `str`, `str(group or '').strip`, `str(group or '').strip().upper`, `(child_moves_by_group or {}).items`, `set`, `len`, `self.geometry.body`, `body.upper`, `body.upper().strip`, `re.escape`, `re.search`, `self.geometry.body(lines[index]).upper`, `self.geometry.body(lines[index]).upper().strip`, `re.match`.
Another 15 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L33: `while index < len(lines)`
- L41: `if re.search(f'\\bIF\\s+{re.escape(LRF_PARENT_NOT_FOUND_TOKEN)}\\b', upper)`
- L44: `while index < len(lines) and depth`
- L46: `if re.match('^IF\\b', nested)`
- L48: `if re.match('^END-IF\\b', nested)`
- L60: `if re.match('^PERFORM\\s+UNTIL\\s+SQLCODE\\s*=\\s*100\\b', upper)`
- L62: `if cursor`
- L82: `if init_match`
- Another 7 conditions/loops exist in this source span.

### `LrfKeyBindingComposer._fetch_cursor_before_end` - L120-L135

```python
_fetch_cursor_before_end(self, lines: list[str], start: int) -> str
```

Observed calls (lexical order): `len`, `range`, `self.geometry.body`, `self.geometry.body(lines[index]).upper`, `self.geometry.body(lines[index]).upper().strip`, `self._is_paragraph_header`, `re.match`, `re.search`, `fetch.group`.

Control points:

- L122: `for index in range(start, len(lines))`
- L124: `if index > start and self._is_paragraph_header(body)`
- L126: `if re.match('^PERFORM\\s+UNTIL\\b', body)`
- L129: `if fetch`
- L131: `if re.match('^END-PERFORM\\b', body)`
- L133: `if depth <= 0`

### `LrfKeyBindingComposer._replace_body` - L137-L148

```python
_replace_body(self, line: str, body: str) -> str
```

Observed calls (lexical order): `FixedFormatLineService`, `fixed.is_fixed_line`, `fixed.replace_body`, `len`, `line.lstrip`.

Control points:

- L142: `if fixed.is_fixed_line(line)`

### `LrfKeyBindingComposer._is_paragraph_header` - L151-L154

```python
_is_paragraph_header(body: str) -> bool
```

Observed calls (lexical order): `body.startswith`, `bool`, `re.match`.

Control points:

- L152: `if not body or body.startswith(('*', '/'))`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
