# `review/engine/sql_blocks.py`

Source: [review/engine/sql_blocks.py](../../../../review/engine/sql_blocks.py) | 166 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `85fc1969a10df40c1e9c834cff03440a26e7c106da2fb9f2c62444dc6bcc3e26`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared EXEC SQL block parsing for checks.

## Module-level bindings

`WS_RUN` (L16), `EXEC_SQL` (L17), `END_EXEC` (L18), `VERB` (L19), `EVIDENCE_WIDTH` (L20)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
```

## Importers (19)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_09_record_retrieval_conversion.py](../checks/chk_09_record_retrieval_conversion.md)
- [review/checks/chk_10_record_modification_conversion.py](../checks/chk_10_record_modification_conversion.md)
- [review/checks/chk_11_sqlcode_commit_conversion.py](../checks/chk_11_sqlcode_commit_conversion.md)
- [review/checks/chk_14_end_of_cursor_handling.py](../checks/chk_14_end_of_cursor_handling.md)
- [review/checks/chk_15_nested_cursor_processing.py](../checks/chk_15_nested_cursor_processing.md)
- [review/checks/chk_16_update_validation.py](../checks/chk_16_update_validation.md)
- [review/checks/chk_17_restart_logic.py](../checks/chk_17_restart_logic.md)
- [review/checks/chk_18_sql_statements.py](../checks/chk_18_sql_statements.md)
- [review/checks/chk_19_select_columns.py](../checks/chk_19_select_columns.md)
- [review/checks/chk_20_into_clause_binding.py](../checks/chk_20_into_clause_binding.md)
- [review/checks/chk_21_where_clause_child_cursor.py](../checks/chk_21_where_clause_child_cursor.md)
- [review/checks/chk_22_naming_authority.py](../checks/chk_22_naming_authority.md)
- 7 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `norm` - L23-L25

```python
norm(text: str) -> str
```

Uppercase, trimmed, internal whitespace runs collapsed.

Observed calls (lexical order): `WS_RUN.sub`, `str`, `str(text or '').strip`, `str(text or '').strip().upper`.

### `logical_statements` - L28-L60

```python
logical_statements(lines: list[str]) -> list[str]
```

Logical statements, with EXEC SQL ... END-EXEC. joined into one entry.

Observed calls (lexical order): `norm`, `line.startswith`, `' '.join`, `out.append`, `buffer.append`.

Control points:

- L38: `for raw in lines`
- L41: `if not inside and line.startswith(EXEC_SQL)`
- L44: `if END_EXEC in line`
- L49: `if inside`
- L51: `if END_EXEC in line`
- L58: `if buffer`

### `SqlBlock` - L64-L97

```python
class SqlBlock()
```

One EXEC SQL ... END-EXEC. statement.

Declared class/data-model fields:

```python
first_index: int
last_index: int
text: str
lines: list = field(default_factory=list)
```

### `SqlBlock.verb` - L73-L75

```python
verb(self) -> str
```

Observed calls (lexical order): `VERB.match`, `match.group`.

### `SqlBlock.line_number` - L78-L79

```python
line_number(self) -> int
```

### `SqlBlock.has` - L81-L82

```python
has(self, keyword: str) -> bool
```

Observed calls (lexical order): `norm`.

### `SqlBlock.render` - L84-L85

```python
render(self) -> str
```

Observed calls (lexical order): `str`.

### `SqlBlock.__str__` - L87-L97

```python
__str__(self) -> str
```

One readable evidence line.

Observed calls (lexical order): `len`.

Control points:

- L95: `if len(body) > EVIDENCE_WIDTH`

### `sql_blocks` - L100-L128

```python
sql_blocks(view) -> list[SqlBlock]
```

Every EXEC SQL block in the code lines of a CobolView.

Observed calls (lexical order): `enumerate`, `norm`, `logical.startswith`, `_build`, `out.append`, `buffer.append`, `len`.

Control points:

- L108: `for (index, line) in enumerate(code)`
- L111: `if not inside and logical.startswith(EXEC_SQL)`
- L115: `if END_EXEC in logical`
- L120: `if inside`
- L122: `if END_EXEC in logical`
- L126: `if buffer and start >= 0`

### `fetch_statements` - L130-L135

```python
fetch_statements(view) -> list[SqlBlock]
```

Every EXEC SQL FETCH block, in source order.

Observed calls (lexical order): `sql_blocks`.

### `_build` - L137-L141

```python
_build(first: int, last: int, lines: list) -> SqlBlock
```

Observed calls (lexical order): `' '.join`, `norm`, `SqlBlock`, `list`.

### `targets_restart` - L144-L152

```python
targets_restart(block: SqlBlock, hints) -> bool
```

True when a block reads or writes a restart or control table.

Observed calls (lexical order): `any`, `str`, `str(hint or '').upper`.

### `lines_before` - L155-L159

```python
lines_before(view, block: SqlBlock, count: int) -> list[str]
```

Normalised code lines immediately before a block.

Observed calls (lexical order): `int`, `max`, `norm`.

### `lines_after` - L162-L166

```python
lines_after(view, block: SqlBlock, count: int) -> list[str]
```

Normalised code lines immediately after a block.

Observed calls (lexical order): `int`, `len`, `min`, `norm`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
