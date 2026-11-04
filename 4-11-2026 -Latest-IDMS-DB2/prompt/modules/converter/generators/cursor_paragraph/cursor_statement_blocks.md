# `converter/generators/cursor_paragraph/cursor_statement_blocks.py`

Source: [converter/generators/cursor_paragraph/cursor_statement_blocks.py](../../../../../converter/generators/cursor_paragraph/cursor_statement_blocks.py) | 153 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `1da3cdccf3ddc8cae681e8858392f42817657856b37611909331e17a0604ac31`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Paragraph header, debug trace, EXEC SQL wrapper and the INTO clause.

## Module-level bindings

`__all__` (L153)

## Import declarations

```python
from __future__ import annotations
from converter.generators.cursor_paragraph.cursor_sql_location import SqlLocationBuilder
from rules.cursor_paragraph_rules import DEBUG_BODY_INDENT, DEBUG_INDICATOR, DEBUG_TRACE_TEMPLATE, EMIT_DEBUG_TRACE_LINES, IND_SQL_BODY, IND_SQL_INTO, IND_SQL_INTO_NEXT, IND_STATEMENT, PARAGRAPH_HEADER_TEMPLATE, TOKEN_END_EXEC, TOKEN_EXEC_SQL, TOKEN_HOST_SEPARATOR, TOKEN_INTO
```

## Local dependency notes

- [converter/generators/cursor_paragraph/cursor_sql_location.py](cursor_sql_location.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](cursor_paragraph_body_builder.md)

## Symbol contracts and control points

### `StatementBlockBuilder` - L68-L150

```python
class StatementBlockBuilder()
```

Renders the non-decisional parts of a cursor paragraph.

### `StatementBlockBuilder.__init__` - L71-L72

```python
__init__(self, sql_location: SqlLocationBuilder | None=None) -> None
```

Observed calls (lexical order): `SqlLocationBuilder`.

### `StatementBlockBuilder.header` - L77-L91

```python
header(self, paragraph_name: str) -> list[str]
```

Paragraph header plus the optional D-indicator trace line.

Observed calls (lexical order): `PARAGRAPH_HEADER_TEMPLATE.format`, `DEBUG_TRACE_TEMPLATE.format`, `lines.append`.

Control points:

- L87: `if EMIT_DEBUG_TRACE_LINES`

### `StatementBlockBuilder.prologue` - L96-L120

```python
prologue(self, paragraph_name: str, statement: str, close_exec: bool=True) -> list[str]
```

Header, trace, SQL-LOCATION move and the EXEC SQL opening.

Observed calls (lexical order): `self.header`, `lines.extend`, `self.sql_location.statement`, `lines.append`.

Control points:

- L116: `if close_exec`

### `StatementBlockBuilder.into_lines` - L126-L150

```python
into_lines(host_variables: list[str]) -> list[str]
```

INTO clause in manual form: first host on INTO, leading commas.

Observed calls (lexical order): `str`, `str(host).strip`, `str(host or '').strip`, `output.extend`.

Control points:

- L142: `if not hosts`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
