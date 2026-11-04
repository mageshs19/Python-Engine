# `converter/postprocess/update_business_sql/update_counter_declarer.py`

Source: [converter/postprocess/update_business_sql/update_counter_declarer.py](../../../../../converter/postprocess/update_business_sql/update_counter_declarer.py) | 166 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `a7c6ff5cbad04f7f8364e0303b6ae68898b7c6267c816c82590f06b11cc4e3a1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Declares the row counter the business UPDATE increments.

## Module-level bindings

`PICTURE_TOKEN` (L46), `__all__` (L166)

## Import declarations

```python
from __future__ import annotations
from typing import List, Optional
from rules.update_business_sql_rules import ENSURE_UPDATE_COUNTER_DECLARED, UPDATE_COUNTER_DIAGNOSTICS, UPDATE_COUNTER_PICTURE
from rules.update_restart_rules import UPDATE_RESTART_WS_NAMES
```

## Local dependency notes

- [rules/update_business_sql_rules.py](../../../rules/update_business_sql_rules.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_business_sql_standardizer.py](../update_business_sql_standardizer.md)

## Symbol contracts and control points

### `UpdateCounterDeclarer` - L49-L163

```python
class UpdateCounterDeclarer()
```

Places the update row counter beside the input counter.

### `UpdateCounterDeclarer.__init__` - L52-L53

```python
__init__(self, line_utils) -> None
```

### `UpdateCounterDeclarer.ensure` - L58-L81

```python
ensure(self, *, lines: List[str], diagnostics=None) -> List[str]
```

Observed calls (lexical order): `names.get`, `str`, `str(names.get('update_counter') or '').strip`, `str(names.get('update_counter') or '').strip().upper`, `str(names.get('input_counter') or '').strip`, `str(names.get('input_counter') or '').strip().upper`, `self._declared`, `self._say`, `self._declaration_index`, `self._clone`.

Control points:

- L59: `if not ENSURE_UPDATE_COUNTER_DECLARED`
- L65: `if not counter or not sibling`
- L68: `if self._declared(lines, counter)`
- L73: `if anchor < 0`

### `UpdateCounterDeclarer._declared` - L86-L87

```python
_declared(self, lines: List[str], name: str) -> bool
```

Observed calls (lexical order): `self._declaration_index`.

### `UpdateCounterDeclarer._declaration_index` - L89-L112

```python
_declaration_index(self, lines: List[str], name: str) -> int
```

Index of `NN <name> PIC ...`, or -1.

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `enumerate`, `self._logical`, `self._logical(line).upper`, `body.split`, `len`, `parts[0].isdigit`, `parts[1].rstrip`, `any`, `token.startswith`.

Control points:

- L96: `if not wanted`
- L99: `for (index, line) in enumerate(lines)`
- L102: `if len(parts) < 3`
- L104: `if not parts[0].isdigit()`
- L106: `if parts[1].rstrip('.') != wanted`
- L108: `if not any((token.startswith(PICTURE_TOKEN) for token in parts[2:]))`

### `UpdateCounterDeclarer._clone` - L114-L128

```python
_clone(self, reference: str, sibling: str, counter: str) -> str
```

The sibling's line, renamed and re-pictured.

Observed calls (lexical order): `self._logical`, `body.partition`, `len`, `tail.lstrip`, `max`, `counter.ljust`, `self._like`.

### `UpdateCounterDeclarer._logical` - L130-L134

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`, `str`.

### `UpdateCounterDeclarer._like` - L136-L150

```python
_like(self, reference: str, body: str) -> str
```

Render `body` with the reference line's fixed-format geometry.

Observed calls (lexical order): `getattr`, `callable`, `renderer`.

Control points:

- L138: `for name in ('active_line_like', 'line_like', 'replace_body')`
- L140: `if callable(renderer)`

### `UpdateCounterDeclarer._say` - L153-L163

```python
_say(diagnostics, key, **values) -> None
```

Observed calls (lexical order): `UPDATE_COUNTER_DIAGNOSTICS.get`, `diagnostics.append`, `template.format`.

Control points:

- L154: `if diagnostics is None`
- L157: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
