# `converter/generators/restart/restart_sql_builder.py`

Source: [converter/generators/restart/restart_sql_builder.py](../../../../../converter/generators/restart/restart_sql_builder.py) | 339 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `57434d97d93bb0ffde4dcaa524f2a8851d963062e66c8afb46f9089c40abf015`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the three SQL paragraphs on the restart table.

## Module-level bindings

`VERB_SELECT` (L93), `VERB_UPDATE` (L94), `VERB_INSERT` (L95), `__all__` (L333)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from catalogs.restart_paragraph_catalog import DEFAULT_SQL_LOCATION_FIELD
from converter.generators.restart.restart_config import RestartConfig
from patterns.restart_patterns import PARAGRAPH_NUMBER_PATTERN
from rules.restart_sql_templates import BLANK_LINE, BRANCH_CONTINUE, BRANCH_DISPLAY, BRANCH_PERFORM, DEBUG_TRACE, ERROR_TEXT, EVALUATE_CLOSE, EVALUATE_OPEN, EXEC_SQL_CLOSE, EXEC_SQL_OPEN, INSERT_HEADER, INSERT_VALUES_HOST, PARAGRAPH_HEADER, PARAGRAPH_TERMINATOR_LINE, QUERYNO_CLAUSE, SELECT_FIRST_COLUMN, SELECT_FIRST_INTO, SELECT_FROM, SELECT_NEXT_COLUMN, SELECT_NEXT_INTO, SQL_LOCATION_MOVE, UPDATE_FIRST_SET, UPDATE_HEADER, UPDATE_NEXT_SET, WHEN_OTHER, WHEN_VALUE, WHERE_FIRST_PREDICATE, WHERE_NEXT_PREDICATE
from rules.restart_standard_rules import EMIT_SQL_LOCATION, EMIT_SQL_LOCATION_IN_ERROR_BRANCH, ROLE_INSERT, ROLE_SELECT, ROLE_UPDATE, SQLCODE_NOT_FOUND, SQLCODE_OK, SQL_LOCATION_USES_PARAGRAPH_NUMBER
```

## Local dependency notes

- [catalogs/restart_paragraph_catalog.py](../../../catalogs/restart_paragraph_catalog.md)
- [converter/generators/restart/restart_config.py](restart_config.md)
- [patterns/restart_patterns.py](../../../patterns/restart_patterns.md)
- [rules/restart_sql_templates.py](../../../rules/restart_sql_templates.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](../../composers/restart/restart_injection_composer.md)
- [tests/restart/test_m4_sql_builder.py](../../../tests/restart/test_m4_sql_builder.md)

## Symbol contracts and control points

### `SqlParagraph` - L99-L109

```python
class SqlParagraph()
```

One generated paragraph, ready for the geometry renderer.

Declared class/data-model fields:

```python
role: str
name: str
debug_trace: str
body: tuple[str, ...]
```

### `SqlParagraph.lines` - L107-L109

```python
lines(self) -> tuple[str, ...]
```

Header plus body. The trace carries its own indicator.

Observed calls (lexical order): `PARAGRAPH_HEADER.format`.

### `RestartSqlBuilder` - L112-L330

```python
class RestartSqlBuilder()
```

Renders select / update / insert against the restart table.

### `RestartSqlBuilder.__init__` - L115-L122

```python
__init__(self, config: RestartConfig, sql_location_field: str=DEFAULT_SQL_LOCATION_FIELD) -> None
```

### `RestartSqlBuilder.build_all` - L128-L139

```python
build_all(self) -> list[SqlParagraph]
```

Observed calls (lexical order): `self.build_select`, `self.build_update`, `self.build_insert`, `self.messages.append`, `len`.

### `RestartSqlBuilder.build_select` - L141-L157

```python
build_select(self) -> SqlParagraph
```

Observed calls (lexical order): `self._select_columns`, `self._select_into`, `SELECT_FROM.format`, `self._where`, `QUERYNO_CLAUSE.format`, `self._paragraph`.

### `RestartSqlBuilder.build_update` - L159-L174

```python
build_update(self) -> SqlParagraph
```

Observed calls (lexical order): `UPDATE_HEADER.format`, `self._set_clause`, `self._where`, `QUERYNO_CLAUSE.format`, `self._paragraph`.

### `RestartSqlBuilder.build_insert` - L176-L195

```python
build_insert(self) -> SqlParagraph
```

INSERT binds the whole DCLGEN host-structure group.

Observed calls (lexical order): `INSERT_HEADER.format`, `INSERT_VALUES_HOST.format`, `self._paragraph`.

### `RestartSqlBuilder._select_columns` - L201-L208

```python
_select_columns(self) -> list[str]
```

Observed calls (lexical order): `self.config.role.columns`, `SELECT_FIRST_COLUMN.format`, `lines.extend`, `SELECT_NEXT_COLUMN.format`.

### `RestartSqlBuilder._select_into` - L210-L218

```python
_select_into(self) -> list[str]
```

Observed calls (lexical order): `self.config.role.host_fields`, `SELECT_FIRST_INTO.format`, `lines.extend`, `SELECT_NEXT_INTO.format`.

### `RestartSqlBuilder._set_clause` - L220-L236

```python
_set_clause(self) -> list[str]
```

Observed calls (lexical order): `UPDATE_FIRST_SET.format`, `lines.extend`, `UPDATE_NEXT_SET.format`.

### `RestartSqlBuilder._where` - L238-L250

```python
_where(self) -> list[str]
```

Observed calls (lexical order): `self.config.role.key_pairs`, `WHERE_FIRST_PREDICATE.format`, `lines.extend`, `WHERE_NEXT_PREDICATE.format`.

### `RestartSqlBuilder._evaluate` - L256-L276

```python
_evaluate(self, normal_values: tuple[int, ...], verb: str) -> list[str]
```

Observed calls (lexical order): `WHEN_VALUE.format`, `lines.extend`, `lines.append`, `BRANCH_DISPLAY.format`, `ERROR_TEXT.format`, `BRANCH_PERFORM.format`.

### `RestartSqlBuilder._sql_location_lines` - L282-L296

```python
_sql_location_lines(self, paragraph_name: str) -> list[str]
```

Observed calls (lexical order): `self._location_value`, `self.messages.append`, `SQL_LOCATION_MOVE.format`.

Control points:

- L283: `if not EMIT_SQL_LOCATION or not self.sql_location_field`
- L286: `if not location`

### `RestartSqlBuilder._location_value` - L299-L303

```python
_location_value(paragraph_name: str) -> str
```

Observed calls (lexical order): `PARAGRAPH_NUMBER_PATTERN.match`, `str`, `match.group`.

Control points:

- L300: `if not SQL_LOCATION_USES_PARAGRAPH_NUMBER`

### `RestartSqlBuilder._paragraph` - L309-L330

```python
_paragraph(self, role: str, statement: list[str], normal_values: tuple[int, ...], verb: str) -> SqlParagraph
```

Observed calls (lexical order): `self.config.paragraph`, `self._sql_location_lines`, `self._evaluate`, `SqlParagraph`, `DEBUG_TRACE.format`, `tuple`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
