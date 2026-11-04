# `tests/cursor_where/_support.py`

Source: [tests/cursor_where/_support.py](../../../../tests/cursor_where/_support.py) | 308 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ffa4bc9d4b1ddfc6a2ab5387e32a3018d0d537c8ead169bb83aa2e0c66266ed9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared fixtures, stubs and assertions for the cursor WHERE suite.

## Module-level bindings

`BODY_COLUMN_OFFSET` (L18), `CURSOR` (L20), `CHILD_RECORD` (L22), `CHILD_TABLE` (L23), `CHILD_GROUP` (L24), `PARENT_RECORD` (L26), `PARENT_TABLE` (L27), `PARENT_GROUP` (L28), `KEY_COLUMN` (L30), `DATA_COLUMN` (L31), `FOREIGN_COLUMN` (L32), `UNOWNED_COLUMN` (L33), `CHILD_COLUMNS` (L35), `PARENT_HOST_REFERENCE` (L39), `EXPECTED_PREDICATE` (L41), `UNOWNED_PREDICATE` (L42)

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

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/cursor_where/test_join_resolver.py](test_join_resolver.md)

## Symbol contracts and control points

### `bodies` - L48-L50

```python
bodies(lines: list[str]) -> list[str]
```

Non-blank lines, trimmed. Indentation is not under test here.

Observed calls (lexical order): `line.strip`.

### `clause_index` - L53-L57

```python
clause_index(rendered: list[str], token: str) -> int
```

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`.

Control points:

- L54: `for (index, body) in enumerate(rendered)`
- L55: `if body.upper().startswith(token)`

### `has_clause` - L60-L61

```python
has_clause(rendered: list[str], token: str) -> bool
```

Observed calls (lexical order): `clause_index`.

### `assert_refusal` - L64-L86

```python
assert_refusal(rendered: list[str], *expected_tokens: str) -> None
```

A refusal is a DB2 WARNING block, not SQL.

Observed calls (lexical order): `all`, `len`, `any`, `body.upper`, `body.upper().startswith`, `' '.join`.

Control points:

- L85: `for token in expected_tokens`

### `LineUtils` - L92-L111

```python
class LineUtils()
```

Minimal stand-in for the infrastructure line utils.

### `LineUtils.and_lines` - L100-L104

```python
and_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `LineUtils.comma_lines` - L107-L111

```python
comma_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `Condition` - L114-L128

```python
class Condition()
```

A fully populated RelationshipCondition.

### `Condition.__init__` - L117-L128

```python
__init__(self, child_column: str=KEY_COLUMN, parent_host_reference: str=PARENT_HOST_REFERENCE) -> None
```

### `PartialCondition` - L131-L142

```python
class PartialCondition()
```

D-5: a condition missing child_table entirely.

### `PartialCondition.__init__` - L139-L142

```python
__init__(self) -> None
```

### `Resolution` - L145-L163

```python
class Resolution()
```

One RelationshipResolution.

### `Resolution.__init__` - L153-L163

```python
__init__(self, conditions: list | None=None, parent_table: str=PARENT_TABLE) -> None
```

Observed calls (lexical order): `list`.

### `ColumnNameResolver` - L166-L183

```python
class ColumnNameResolver()
```

columns_for_table() is the ONLY lookup the guard may call.

### `ColumnNameResolver.__init__` - L174-L175

```python
__init__(self, columns: list[str] | None=None) -> None
```

Observed calls (lexical order): `list`.

### `ColumnNameResolver.columns_for_table` - L177-L183

```python
columns_for_table(self, table_name: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(table_name or '').upper`, `list`.

Control points:

- L179: `if table == CHILD_TABLE`
- L181: `if table == PARENT_TABLE`

### `HostVariableResolver` - L186-L210

```python
class HostVariableResolver()
```

The REAL resolver surface.

### `HostVariableResolver.group_for_table` - L194-L200

```python
group_for_table(self, table: str) -> str
```

Observed calls (lexical order): `str`, `str(table or '').upper`.

Control points:

- L196: `if table == CHILD_TABLE`
- L198: `if table == PARENT_TABLE`

### `HostVariableResolver.host_reference_for_column` - L202-L210

```python
host_reference_for_column(self, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `self.group_for_table`, `str`, `str(column_name or '').replace`.

Control points:

- L208: `if not group`

### `TableNameResolver` - L213-L221

```python
class TableNameResolver()
```

### `TableNameResolver.table_for_record` - L215-L221

```python
table_for_record(record_name: str) -> str
```

Observed calls (lexical order): `str`, `str(record_name or '').upper`.

Control points:

- L217: `if record == CHILD_RECORD`
- L219: `if record == PARENT_RECORD`

### `KeyColumnResolver` - L224-L231

```python
class KeyColumnResolver()
```

### `KeyColumnResolver.__init__` - L225-L228

```python
__init__(self, primary_keys: list[str] | None=None) -> None
```

Observed calls (lexical order): `list`.

### `KeyColumnResolver.primary_key_columns_for_record` - L230-L231

```python
primary_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `list`.

### `RelationshipResolver` - L234-L247

```python
class RelationshipResolver()
```

Facade exposing resolve(), as most call paths do.

### `RelationshipResolver.__init__` - L237-L244

```python
__init__(self, resolution=None, primary_keys: list[str] | None=None) -> None
```

Observed calls (lexical order): `TableNameResolver`, `KeyColumnResolver`.

### `RelationshipResolver.resolve` - L246-L247

```python
resolve(self, child_record: str)
```

### `LegacyRelationshipResolver` - L250-L263

```python
class LegacyRelationshipResolver()
```

D-4: facade exposing ONLY resolve_for_child_record().

### `LegacyRelationshipResolver.__init__` - L257-L260

```python
__init__(self, resolution=None) -> None
```

Observed calls (lexical order): `TableNameResolver`, `KeyColumnResolver`.

### `LegacyRelationshipResolver.resolve_for_child_record` - L262-L263

```python
resolve_for_child_record(self, child_record: str)
```

### `join` - L269-L278

```python
join(relationship_resolver, columns: list[str] | None=None) -> CursorJoinResolver
```

A CursorJoinResolver wired to the stubs above.

Observed calls (lexical order): `CursorJoinResolver`, `ColumnNameResolver`, `HostVariableResolver`.

### `spec` - L281-L308

```python
spec(order: int=0, cursor_name: str=CURSOR, table_name: str=CHILD_TABLE, select_columns: list[str] | None=None, where_conditions: list[str] | None=None, order_by_columns: list[str] | None=None) -> CursorSpec
```

CursorSpec.read() is the door the production path uses.

Observed calls (lexical order): `CursorSpec.read`, `list`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
