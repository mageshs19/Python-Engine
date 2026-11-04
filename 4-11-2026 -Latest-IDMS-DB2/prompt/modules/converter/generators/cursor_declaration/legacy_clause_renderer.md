# `converter/generators/cursor_declaration/legacy_clause_renderer.py`

Source: [converter/generators/cursor_declaration/legacy_clause_renderer.py](../../../../../converter/generators/cursor_declaration/legacy_clause_renderer.py) | 149 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `1c7d0fbe5983969780f0421c3c50790c1f92e4c819246959ffc5fca1d7338a7e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The LEGACY clause shape: 'SELECT <column>' on one line.

## Module-level bindings

`ORDER_BY_JOIN` (L52), `NO_TERMINATOR` (L53), `__all__` (L149)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_legacy import IND_WHERE_FIRST
from rules.cursor_declaration_rules import DECLARE_LINE_TEMPLATE, DECLARE_ON_EXEC_SQL_LINE, EMIT_QUERYNO, END_EXEC, FOR_READ_ONLY, FROM_TEMPLATE, IND_CLAUSE, IND_EXEC, IND_QUERYNO, IND_SELECT_FIRST, IND_SELECT_NEXT, IND_WHERE_NEXT, LAST_DECLARATION_TERMINATOR, ORDER_BY_TEMPLATE, QUERYNO_BASE, QUERYNO_STEP, QUERYNO_TEMPLATE, SELECT_FIRST_TEMPLATE, SELECT_NEXT_TEMPLATE, WHERE_FIRST_TEMPLATE, WHERE_NEXT_TEMPLATE
```

## Local dependency notes

- [rules/cursor_declaration_legacy.py](../../../rules/cursor_declaration_legacy.md)
- [rules/cursor_declaration_rules.py](../../../rules/cursor_declaration_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](cursor_declaration_generator.md)

## Symbol contracts and control points

### `LegacyClauseRenderer` - L56-L146

```python
class LegacyClauseRenderer()
```

Lays out one legacy DECLARE CURSOR statement.

### `LegacyClauseRenderer.render` - L59-L78

```python
render(self, cursor: str, table: str, columns: list[str], conditions: list[str], order_by: list[str], cursor_order: int, is_last: bool) -> list[str]
```

Observed calls (lexical order): `lines.extend`, `self._declare`, `self._select`, `FROM_TEMPLATE.format`, `lines.append`, `self._where`, `self._order_by`, `self._queryno`, `self._end_exec`.

### `LegacyClauseRenderer._declare` - L82-L88

```python
_declare(cursor: str) -> list[str]
```

Observed calls (lexical order): `DECLARE_LINE_TEMPLATE.format`.

Control points:

- L83: `if DECLARE_ON_EXEC_SQL_LINE`

### `LegacyClauseRenderer._select` - L91-L104

```python
_select(columns: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `out.append`, `SELECT_FIRST_TEMPLATE.format`, `SELECT_NEXT_TEMPLATE.format`.

Control points:

- L93: `for (position, column) in enumerate(columns or [])`
- L94: `if position == 0`

### `LegacyClauseRenderer._where` - L107-L120

```python
_where(conditions: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `out.append`, `WHERE_FIRST_TEMPLATE.format`, `WHERE_NEXT_TEMPLATE.format`.

Control points:

- L109: `for (position, condition) in enumerate(conditions or [])`
- L110: `if position == 0`

### `LegacyClauseRenderer._order_by` - L123-L127

```python
_order_by(columns: list[str]) -> list[str]
```

Observed calls (lexical order): `ORDER_BY_JOIN.join`, `ORDER_BY_TEMPLATE.format`.

Control points:

- L124: `if not columns`

### `LegacyClauseRenderer._queryno` - L130-L134

```python
_queryno(cls, cursor_order: int) -> list[str]
```

Observed calls (lexical order): `cls.queryno`, `QUERYNO_TEMPLATE.format`.

Control points:

- L131: `if not EMIT_QUERYNO`

### `LegacyClauseRenderer.queryno` - L137-L141

```python
queryno(cursor_order: int) -> int
```

1-BASED, matching CursorDeclareBuilder. See CORRECTION 3.

Observed calls (lexical order): `int`.

Control points:

- L139: `if not EMIT_QUERYNO`

### `LegacyClauseRenderer._end_exec` - L144-L146

```python
_end_exec(is_last: bool) -> str
```

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
