# `converter/generators/sql_generator.py`

Source: [converter/generators/sql_generator.py](../../../../converter/generators/sql_generator.py) | 189 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `ddb5efaf702e993483764f813bb12074f1fa10b0b3587bd3ae18741dddff4be3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generates DB2 embedded SQL snippets.

## Module-level bindings

`__all__` (L189)

## Import declarations

```python
from __future__ import annotations
from converter.generators.sql.sql_column_resolver import SqlColumnResolver
from converter.generators.sql.sql_date_move_builder import SqlDateMoveBuilder
from converter.generators.sql.sql_line_builder import SqlLineBuilder
from converter.generators.sql.sql_statement_builder import SqlStatementBuilder
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.resolvers.update_sql_plan_resolver import UpdateSqlPlanResolver
```

## Local dependency notes

- [converter/generators/sql/sql_column_resolver.py](sql/sql_column_resolver.md)
- [converter/generators/sql/sql_date_move_builder.py](sql/sql_date_move_builder.md)
- [converter/generators/sql/sql_line_builder.py](sql/sql_line_builder.md)
- [converter/generators/sql/sql_statement_builder.py](sql/sql_statement_builder.md)
- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/column_name_resolver.py](../resolvers/column_name_resolver.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [converter/resolvers/update_sql_plan_resolver.py](../resolvers/update_sql_plan_resolver.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `SqlGenerator` - L61-L186

```python
class SqlGenerator()
```

### `SqlGenerator.__init__` - L62-L101

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository, table_name_resolver: TableNameResolver, column_name_resolver: ColumnNameResolver, host_variable_resolver: HostVariableResolver) -> None
```

Observed calls (lexical order): `UpdateSqlPlanResolver`, `SqlColumnResolver`, `SqlLineBuilder`, `SqlDateMoveBuilder`, `SqlStatementBuilder`.

### `SqlGenerator._relay` - L106-L114

```python
_relay(self, lines: list[str]) -> list[str]
```

Return the builder's lines and SNAPSHOT its diagnostics.

Observed calls (lexical order): `getattr`, `list`.

### `SqlGenerator.select_by_key` - L119-L136

```python
select_by_key(self, record_name: str, *, for_lrf_parent: bool=False, required_columns: list[str] | tuple[str, ...] | set[str] | None=None, status_handling: bool=True, read_kind: str='LRF keyed parent') -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.select_by_key`.

### `SqlGenerator.insert` - L138-L139

```python
insert(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.insert`.

### `SqlGenerator.update` - L141-L151

```python
update(self, record_name: str, changed_source_fields: list[str] | None=None) -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.update`.

### `SqlGenerator.delete` - L153-L154

```python
delete(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.delete`.

### `SqlGenerator.commit` - L156-L157

```python
commit(self) -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.commit`.

### `SqlGenerator.rollback` - L159-L160

```python
rollback(self) -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.rollback`.

### `SqlGenerator.changed_field_move` - L162-L174

```python
changed_field_move(self, record_name: str, source_value: str, target_source_field: str) -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.changed_field_move`.

### `SqlGenerator.missing_mapping` - L176-L186

```python
missing_mapping(self, record_name: str, reason: str) -> list[str]
```

Observed calls (lexical order): `self._relay`, `self._statements.missing_mapping`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
