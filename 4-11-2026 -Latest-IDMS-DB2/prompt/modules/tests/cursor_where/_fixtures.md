# `tests/cursor_where/_fixtures.py`

Source: [tests/cursor_where/_fixtures.py](../../../../tests/cursor_where/_fixtures.py) | 289 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `f19e9d0e07b9365a74e9b9ba81eb766e448cf247729bbef111d763f4a4aabf33`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared names, stubs and assertions for the cursor WHERE suite.

## Module-level bindings

`BODY_COLUMN_OFFSET` (L19), `CURSOR` (L21), `CHILD_RECORD` (L23), `CHILD_TABLE` (L24), `CHILD_GROUP` (L25), `PARENT_RECORD` (L27), `PARENT_TABLE` (L28), `PARENT_GROUP` (L29), `KEY_COLUMN` (L31), `DATA_COLUMN` (L32), `FOREIGN_COLUMN` (L33), `UNOWNED_COLUMN` (L34), `CHILD_COLUMNS` (L36), `EXPECTED_PREDICATE` (L38), `UNOWNED_PREDICATE` (L39)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from converter.resolvers.cursor_join_resolver import CursorJoinResolver
from rules.cursor_declaration_rules import BODY_LAST_COLUMN
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_spec.py](../../converter/generators/db2_infrastructure/cursor_spec.md)
- [converter/resolvers/cursor_join_resolver.py](../../converter/resolvers/cursor_join_resolver.md)
- [rules/cursor_declaration_rules.py](../../rules/cursor_declaration_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/cursor_where/conftest.py](conftest.md)
- [tests/cursor_where/test_declare_clauses.py](test_declare_clauses.md)

## Symbol contracts and control points

### `bodies` - L45-L47

```python
bodies(lines: list[str]) -> list[str]
```

Non-blank lines, trimmed. Indentation is not under test here.

Observed calls (lexical order): `line.strip`.

### `clause_index` - L50-L54

```python
clause_index(rendered: list[str], token: str) -> int
```

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`.

Control points:

- L51: `for (index, body) in enumerate(rendered)`
- L52: `if body.upper().startswith(token)`

### `has_clause` - L57-L58

```python
has_clause(rendered: list[str], token: str) -> bool
```

Observed calls (lexical order): `clause_index`.

### `assert_refusal` - L61-L95

```python
assert_refusal(rendered: list[str], *expected_tokens: str) -> None
```

A refusal is a DB2 WARNING block, not SQL.

Observed calls (lexical order): `all`, `len`, `any`, `body.upper`, `body.upper().startswith`, `' '.join`.

Control points:

- L94: `for token in expected_tokens`

### `LineUtils` - L101-L120

```python
class LineUtils()
```

Minimal stand-in for the infrastructure line utils.

### `LineUtils.and_lines` - L109-L113

```python
and_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `LineUtils.comma_lines` - L116-L120

```python
comma_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `Condition` - L123-L137

```python
class Condition()
```

A fully populated RelationshipCondition.

### `Condition.__init__` - L126-L137

```python
__init__(self, child_column: str=KEY_COLUMN, parent_host_reference: str=f':{PARENT_GROUP}.KY-SIFORM') -> None
```

### `PartialCondition` - L140-L146

```python
class PartialCondition()
```

D-5: a condition missing child_table entirely.

### `PartialCondition.__init__` - L143-L146

```python
__init__(self) -> None
```

### `Resolution` - L149-L160

```python
class Resolution()
```

### `Resolution.__init__` - L150-L160

```python
__init__(self, conditions: list | None=None, parent_table: str=PARENT_TABLE) -> None
```

Observed calls (lexical order): `list`.

### `ColumnNameResolver` - L163-L172

```python
class ColumnNameResolver()
```

### `ColumnNameResolver.__init__` - L164-L165

```python
__init__(self, columns: list[str] | None=None) -> None
```

Observed calls (lexical order): `list`.

### `ColumnNameResolver.columns_for_table` - L167-L172

```python
columns_for_table(self, table_name: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(table_name or '').upper`, `list`.

Control points:

- L168: `if str(table_name or '').upper() == CHILD_TABLE`
- L170: `if str(table_name or '').upper() == PARENT_TABLE`

### `HostVariableResolver` - L175-L198

```python
class HostVariableResolver()
```

The REAL resolver surface.

### `HostVariableResolver.group_for_table` - L182-L188

```python
group_for_table(self, table: str) -> str
```

Observed calls (lexical order): `str`, `str(table or '').upper`.

Control points:

- L184: `if table == CHILD_TABLE`
- L186: `if table == PARENT_TABLE`

### `HostVariableResolver.host_reference_for_column` - L190-L198

```python
host_reference_for_column(self, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `self.group_for_table`, `str`, `str(column_name or '').replace`.

Control points:

- L196: `if not group`

### `TableNameResolver` - L201-L209

```python
class TableNameResolver()
```

### `TableNameResolver.table_for_record` - L203-L209

```python
table_for_record(record_name: str) -> str
```

Observed calls (lexical order): `str`, `str(record_name or '').upper`.

Control points:

- L205: `if record == CHILD_RECORD`
- L207: `if record == PARENT_RECORD`

### `KeyColumnResolver` - L212-L219

```python
class KeyColumnResolver()
```

### `KeyColumnResolver.__init__` - L213-L216

```python
__init__(self, primary_keys: list[str] | None=None) -> None
```

Observed calls (lexical order): `list`.

### `KeyColumnResolver.primary_key_columns_for_record` - L218-L219

```python
primary_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `list`.

### `RelationshipResolver` - L222-L235

```python
class RelationshipResolver()
```

Facade exposing resolve(), as most call paths do.

### `RelationshipResolver.__init__` - L225-L232

```python
__init__(self, resolution=None, primary_keys: list[str] | None=None) -> None
```

Observed calls (lexical order): `TableNameResolver`, `KeyColumnResolver`.

### `RelationshipResolver.resolve` - L234-L235

```python
resolve(self, child_record: str)
```

### `LegacyRelationshipResolver` - L238-L247

```python
class LegacyRelationshipResolver()
```

D-4: facade exposing ONLY resolve_for_child_record().

### `LegacyRelationshipResolver.__init__` - L241-L244

```python
__init__(self, resolution=None) -> None
```

Observed calls (lexical order): `TableNameResolver`, `KeyColumnResolver`.

### `LegacyRelationshipResolver.resolve_for_child_record` - L246-L247

```python
resolve_for_child_record(self, child_record: str)
```

### `join` - L253-L261

```python
join(relationship_resolver, columns: list[str] | None=None) -> CursorJoinResolver
```

Observed calls (lexical order): `CursorJoinResolver`, `ColumnNameResolver`, `HostVariableResolver`.

### `spec` - L264-L289

```python
spec(order: int=0, cursor_name: str=CURSOR, table_name: str=CHILD_TABLE, select_columns: list[str] | None=None, where_conditions: list[str] | None=None, order_by_columns: list[str] | None=None) -> CursorSpec
```

CursorSpec.read() is the door the production path uses.

Observed calls (lexical order): `CursorSpec.read`, `list`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
