# `converter/generators/cursor_paragraph/cursor_line_geometry.py`

Source: [converter/generators/cursor_paragraph/cursor_line_geometry.py](../../../../../converter/generators/cursor_paragraph/cursor_line_geometry.py) | 55 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `682771a43a8f1f79fc9219a998bb58c62a85bdae8dd0b4c9e221f73d2ddf2c0e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format width arithmetic for one generated body line.

## Module-level bindings

`BODY_COLUMN_OFFSET` (L24), `__all__` (L55)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_paragraph_rules import FETCH_KEY_BODY_END_COLUMN, IND_WHEN_BODY, IND_WHEN_BODY_CONT
```

## Local dependency notes

- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Symbol contracts and control points

### `fits` - L27-L29

```python
fits(line: str) -> bool
```

True when the body line ends on or before the window edge.

Observed calls (lexical order): `len`, `str`.

### `continuation` - L32-L52

```python
continuation(text: str) -> str
```

A continuation fragment at the widest indent that still fits.

Observed calls (lexical order): `str`, `str(text or '').strip`, `fits`.

Control points:

- L44: `if not body`
- L47: `for indent in (IND_WHEN_BODY_CONT, IND_WHEN_BODY)`
- L49: `if fits(candidate)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
