# `converter/generators/cursor_paragraph/cursor_fetch_paragraph.py`

Source: [converter/generators/cursor_paragraph/cursor_fetch_paragraph.py](../../../../../converter/generators/cursor_paragraph/cursor_fetch_paragraph.py) | 295 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `bbf03d58f1678f57b13ed2aa25be91cab7ff7396883f6d87095dec44c6e4efc8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The FETCH paragraph body. The only cursor paragraph with branches.

## Module-level bindings

`__all__` (L295)

## Import declarations

```python
from __future__ import annotations
from converter.generators.counter_generator import CounterGenerator
from converter.generators.cursor_paragraph import cursor_host_reference as hosts
from rules.cursor_paragraph_rules import COUNT_PARENT_FETCH_ONLY, CURSOR_EOC_SUFFIX, CURSOR_NOT_EOC_SUFFIX, ENFORCE_FETCH_PROLOGUE, ERROR_FETCH_TEMPLATE, FETCH_STATEMENT_TEMPLATE, IND_SQL_BODY, IND_STATEMENT, IND_WHEN, IND_WHEN_BODY, INITIALIZE_HOST_GROUP_TEMPLATE, SET_EOC_TEMPLATE, SET_NOT_EOC_TEMPLATE, TOKEN_CONTINUE, TOKEN_END_EXEC, TOKEN_EVALUATE_SQLCODE, TOKEN_EXEC_SQL, TOKEN_WHEN_100, TOKEN_WHEN_ZERO
```

## Local dependency notes

- [converter/generators/counter_generator.py](../counter_generator.md)
- [converter/generators/cursor_paragraph/__init__.py](__init__.md)
- [converter/generators/cursor_paragraph/cursor_host_reference.py](cursor_host_reference.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/__init__.py](__init__.md)
- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](cursor_paragraph_body_builder.md)

## Symbol contracts and control points

### `FetchParagraphBuilder` - L114-L292

```python
class FetchParagraphBuilder()
```

Renders one FETCH paragraph.

### `FetchParagraphBuilder.__init__` - L122-L125

```python
__init__(self, blocks, sql_location, error_branch) -> None
```

### `FetchParagraphBuilder.build` - L130-L156

```python
build(self, cursor_name: str, paragraph_name: str, host_variables: list[str], sql_error_paragraph: str, where_conditions: list[str] | None=None, table_name: str='', is_parent_cursor: bool=False) -> list[str]
```

Observed calls (lexical order): `self.blocks.header`, `lines.extend`, `self._prologue`, `self._sql_block`, `self._evaluate`, `self._error_branch`.

### `FetchParagraphBuilder._prologue` - L161-L189

```python
_prologue(self, cursor_name: str, paragraph_name: str, host_variables: list[str]) -> list[str]
```

Optional host INITIALIZE, the EOC reset, the SQL-LOCATION move.

Observed calls (lexical order): `hosts.group_of`, `lines.append`, `INITIALIZE_HOST_GROUP_TEMPLATE.format`, `SET_NOT_EOC_TEMPLATE.format`, `self.sql_location.statement`.

Control points:

- L170: `if ENFORCE_FETCH_PROLOGUE`
- L174: `if group`

### `FetchParagraphBuilder._sql_block` - L194-L207

```python
_sql_block(self, cursor_name: str, host_variables: list[str]) -> list[str]
```

Observed calls (lexical order): `FETCH_STATEMENT_TEMPLATE.format`, `lines.extend`, `self.blocks.into_lines`, `lines.append`.

### `FetchParagraphBuilder._evaluate` - L212-L241

```python
_evaluate(self, cursor_name: str, table_name: str, is_parent_cursor: bool) -> list[str]
```

Observed calls (lexical order): `self._counter_line`, `lines.append`, `SET_EOC_TEMPLATE.format`.

Control points:

- L224: `if counter_line`

### `FetchParagraphBuilder._counter_line` - L244-L262

```python
_counter_line(table_name: str, is_parent_cursor: bool) -> str
```

ADD 1 TO WS-NB-<token>-COUNT, or "" when this cursor does not count.

Observed calls (lexical order): `CounterGenerator`, `counter.counter_name_for_table`, `counter.increment`.

Control points:

- L249: `if not table_name`
- L252: `if COUNT_PARENT_FETCH_ONLY and (not is_parent_cursor)`
- L257: `if not name`

### `FetchParagraphBuilder._error_branch` - L267-L292

```python
_error_branch(self, cursor_name: str, paragraph_name: str, host_variables: list[str], sql_error_paragraph: str, where_conditions: list[str] | None, is_parent_cursor: bool) -> list[str]
```

CORRECTION 2. Three cases, decided here and nowhere else.

Observed calls (lexical order): `self.error_branch.build`, `ERROR_FETCH_TEMPLATE.format`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
