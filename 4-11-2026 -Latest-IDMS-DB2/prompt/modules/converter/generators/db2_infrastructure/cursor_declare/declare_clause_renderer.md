# `converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.py) | 246 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `6391a9e153574241634cb8c6caaf738300c81fd31ca78d539fa725eeb1b97394`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders the clauses of one DECLARE, in SQL order.

## Module-level bindings

`NO_QUERYNO` (L97), `_SEPARATOR_WIDTH` (L102), `IND_SELECT_CONTINUATION` (L111), `IND_ORDER_BY_CONTINUATION` (L112), `__all__` (L241)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_rules import DECLARE_LINE_TEMPLATE, DECLARE_ON_EXEC_SQL_LINE, EMIT_QUERYNO, END_EXEC, LAST_DECLARATION_TERMINATOR, QUERYNO_BASE, QUERYNO_STEP, QUERYNO_TEMPLATE, SELECT_FIRST_TEMPLATE, SELECT_NEXT_TEMPLATE, WHERE_FIRST_TEMPLATE, WHERE_NEXT_TEMPLATE
from rules.db2_infrastructure_rules import DECLARE_TEMPLATE, FROM_TEMPLATE, IND_EXEC, IND_SQL_BODY, IND_WHERE_NEXT, TOKEN_END_EXEC, TOKEN_EXEC_SQL, TOKEN_FOR_READ_ONLY, TOKEN_ORDER_BY, TOKEN_SELECT, TOKEN_WHERE
```

## Local dependency notes

- [rules/cursor_declaration_rules.py](../../../../rules/cursor_declaration_rules.md)
- [rules/db2_infrastructure_rules.py](../../../../rules/db2_infrastructure_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](cursor_declare_builder.md)

## Symbol contracts and control points

### `_continuation_indent` - L105-L108

```python
_continuation_indent(keyword: str) -> str
```

Indent that lines a continued item up under the first one.

Observed calls (lexical order): `len`, `max`.

### `DeclareClauseRenderer` - L115-L238

```python
class DeclareClauseRenderer()
```

Lays out one DECLARE CURSOR statement.

### `DeclareClauseRenderer.__init__` - L118-L119

```python
__init__(self, line_utils) -> None
```

### `DeclareClauseRenderer.render` - L121-L139

```python
render(self, spec, columns: list[str], conditions: list[str], order_by: list[str], is_last: bool=True) -> list[str]
```

Observed calls (lexical order): `self.open_lines`, `lines.extend`, `self.select_lines`, `lines.append`, `FROM_TEMPLATE.format`, `self.where_lines`, `self.order_by_lines`, `self.queryno_lines`, `self.close_line`.

### `DeclareClauseRenderer.open_lines` - L143-L154

```python
open_lines(cursor_name: str) -> list[str]
```

One line in the manual form, two when the flag is False.

Observed calls (lexical order): `DECLARE_LINE_TEMPLATE.format`, `DECLARE_TEMPLATE.format`.

Control points:

- L145: `if DECLARE_ON_EXEC_SQL_LINE`

### `DeclareClauseRenderer.close_line` - L158-L162

```python
close_line(is_last: bool=True) -> str
```

Bare END-EXEC, except on the declaration that ends the sentence.

Control points:

- L160: `if is_last`

### `DeclareClauseRenderer.select_lines` - L166-L186

```python
select_lines(columns: list[str]) -> list[str]
```

First column on the SELECT line, the rest comma-leading.

Observed calls (lexical order): `SELECT_FIRST_TEMPLATE.format`, `out.extend`, `SELECT_NEXT_TEMPLATE.format`.

Control points:

- L174: `if not columns`

### `DeclareClauseRenderer.where_lines` - L189-L203

```python
where_lines(self, conditions: list[str]) -> list[str]
```

First predicate on the WHERE line, the rest AND-leading.

Observed calls (lexical order): `WHERE_FIRST_TEMPLATE.format`, `out.extend`, `WHERE_NEXT_TEMPLATE.format`.

Control points:

- L191: `if not conditions`

### `DeclareClauseRenderer.order_by_lines` - L206-L222

```python
order_by_lines(self, columns: list[str]) -> list[str]
```

First entry on the ORDER BY line, the rest comma-leading.

Observed calls (lexical order): `out.extend`.

Control points:

- L214: `if not columns`

### `DeclareClauseRenderer.queryno_lines` - L226-L230

```python
queryno_lines(cls, cursor_order: int) -> list[str]
```

Observed calls (lexical order): `cls.queryno`, `QUERYNO_TEMPLATE.format`.

Control points:

- L227: `if not EMIT_QUERYNO`

### `DeclareClauseRenderer.queryno` - L233-L238

```python
queryno(cursor_order: int) -> int
```

DERIVED, never hardcoded, so repeated runs are byte-identical and two cursors in one program can never collide.

Observed calls (lexical order): `int`.

Control points:

- L236: `if not EMIT_QUERYNO`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
