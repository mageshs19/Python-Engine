# `mainframe/zowe_step_output.py`

Source: [mainframe/zowe_step_output.py](../../../mainframe/zowe_step_output.py) | 122 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `383196e635ef6802fa9e8f9fda6ecb1d6f96ab789b53b5394cbf09af44c16fb9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reads meaning out of a runner's console output.

## Module-level bindings

`MAPPING_ROWS` (L26), `DCLGEN_COLUMNS` (L29), `COPYBOOK_FIELDS` (L32), `LRF_RECORDS` (L35), `OUTPUT_FILE` (L40), `REVIEW_SUMMARY` (L44), `LOG_LINE` (L53), `ERROR_LINE` (L57), `TRACEBACK` (L58), `ATTENTION_LEVELS` (L61), `ATTENTION_MAX` (L64), `__all__` (L122)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_steps.py](zowe_steps.md)

## Symbol contracts and control points

### `_count` - L67-L69

```python
_count(pattern: re.Pattern, text: str) -> int
```

Observed calls (lexical order): `pattern.search`, `int`, `match.group`.

### `_attention` - L72-L90

```python
_attention(text: str) -> tuple[list[str], int, int]
```

(shown, total_attention, total_messages) from the log lines.

Observed calls (lexical order): `text.splitlines`, `LOG_LINE.match`, `match.group`, `match.group('message').strip`, `len`, `shown.append`.

Control points:

- L78: `for raw in text.splitlines()`
- L80: `if not match`
- L83: `if match.group('level') not in ATTENTION_LEVELS`
- L87: `if message and len(shown) < ATTENTION_MAX and (message not in shown)`

### `digest` - L93-L119

```python
digest(text: str) -> dict
```

Facts worth printing. Never raises, never returns None.

Observed calls (lexical order): `str`, `_attention`, `REVIEW_SUMMARY.search`, `_count`, `OUTPUT_FILE.finditer`, `m.group`, `m.group('path').strip`, `int`, `review_match.group`, `ERROR_LINE.finditer`, `m.group('message').strip`, `TRACEBACK.search`, `bool`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
