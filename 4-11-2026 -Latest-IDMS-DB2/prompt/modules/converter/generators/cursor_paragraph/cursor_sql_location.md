# `converter/generators/cursor_paragraph/cursor_sql_location.py`

Source: [converter/generators/cursor_paragraph/cursor_sql_location.py](../../../../../converter/generators/cursor_paragraph/cursor_sql_location.py) | 57 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `79931c607548ebd2178875bfbb0e15e2bb0881afea14c541219f30b6f5d779c7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> MOVE <paragraph identity> TO SQL-LOCATION, cursor-path entry point.

## Module-level bindings

`PARAGRAPH_NUMBER_SEPARATOR` (L34), `__all__` (L57)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.sql_location_move_builder import SqlLocationMoveBuilder
from rules.cursor_paragraph_rules import IND_STATEMENT
```

## Local dependency notes

- [converter/generators/db2_infrastructure/sql_location_move_builder.py](../db2_infrastructure/sql_location_move_builder.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_error_branch.py](cursor_error_branch.md)
- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](cursor_paragraph_body_builder.md)
- [converter/generators/cursor_paragraph/cursor_statement_blocks.py](cursor_statement_blocks.md)

## Symbol contracts and control points

### `SqlLocationBuilder` - L37-L54

```python
class SqlLocationBuilder()
```

Renders the SQL-LOCATION move in its two indent forms.

### `SqlLocationBuilder.__init__` - L40-L41

```python
__init__(self, mover: SqlLocationMoveBuilder | None=None) -> None
```

Observed calls (lexical order): `SqlLocationMoveBuilder`.

### `SqlLocationBuilder.statement` - L43-L45

```python
statement(self, paragraph_name: str) -> str
```

Paragraph-level form, carrying its own indent. No period.

Observed calls (lexical order): `self.body`.

### `SqlLocationBuilder.body` - L47-L54

```python
body(self, paragraph_name: str) -> str
```

Un-indented body, for use inside a WHEN branch.

Observed calls (lexical order): `self.mover.body`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
