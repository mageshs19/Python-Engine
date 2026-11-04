# `tests/test_sql_column_resolver_table_alias.py`

Source: [tests/test_sql_column_resolver_table_alias.py](../../../tests/test_sql_column_resolver_table_alias.py) | 45 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `626b12598e855362b14e935a9e5f17efee0cbf59e3220a8364cea0d81fde9380`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.generators.sql.sql_column_resolver import SqlColumnResolver
```

## Local dependency notes

- [converter/generators/sql/sql_column_resolver.py](../converter/generators/sql/sql_column_resolver.md)

## Symbol contracts and control points

### `MappingRepository` - L4-L16

```python
class MappingRepository()
```

### `MappingRepository.__init__` - L5-L6

```python
__init__(self)
```

### `MappingRepository.db2_table_for_record` - L8-L10

```python
db2_table_for_record(self, record_name)
```

### `MappingRepository.db2_columns_for_table` - L12-L16

```python
db2_columns_for_table(self, table_name)
```

Control points:

- L14: `if table_name == 'DZEVEFTB'`

### `DclgenRepository` - L19-L22

```python
class DclgenRepository()
```

### `DclgenRepository.column_names_for_table` - L20-L22

```python
column_names_for_table(self, table_name)
```

### `TableNameResolver` - L25-L27

```python
class TableNameResolver()
```

### `TableNameResolver.resolve_table` - L26-L27

```python
resolve_table(self, table_name)
```

Observed calls (lexical order): `{'DZEVEFTB': 'DZEVEFTV', 'DZEVEFTV': 'DZEVEFTV'}.get`.

### `test_insert_columns_use_sheet_mapping_base_table_and_dclgen_alias` - L30-L45

```python
test_insert_columns_use_sheet_mapping_base_table_and_dclgen_alias()
```

Observed calls (lexical order): `MappingRepository`, `SqlColumnResolver`, `DclgenRepository`, `TableNameResolver`, `resolver.insert_columns_for_record`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
