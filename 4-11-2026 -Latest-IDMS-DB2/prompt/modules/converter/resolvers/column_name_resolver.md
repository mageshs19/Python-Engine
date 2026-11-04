# `converter/resolvers/column_name_resolver.py`

Source: [converter/resolvers/column_name_resolver.py](../../../../converter/resolvers/column_name_resolver.py) | 148 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `d0a09b289b9cf24f335ea1d3075ad2da70072dfe68c452d183515b732e75720e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/unmapped_record_block_composer.py](../composers/unmapped_record_block_composer.md)
- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [converter/generators/sql_generator.py](../generators/sql_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/resolvers/cursor_column_filter.py](cursor_column_filter.md)
- [converter/resolvers/cursor_column_resolver.py](cursor_column_resolver.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `ColumnNameResolver` - L7-L148

```python
class ColumnNameResolver()
```

Resolves DB2 column names.

### `ColumnNameResolver.__init__` - L16-L24

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository, table_name_resolver: TableNameResolver) -> None
```

### `ColumnNameResolver.columns_for_record` - L26-L44

```python
columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self.table_name_resolver.table_for_record`, `self.mapping_repository.db2_columns_for_table`, `self.mapping_repository.db2_table_for_record`, `self._filter_to_existing_dclgen_columns`.

Control points:

- L32: `if not table_name`
- L37: `if not mapped_columns`

### `ColumnNameResolver.columns_for_table` - L46-L63

```python
columns_for_table(self, table_name: str) -> list[str]
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `self.mapping_repository.db2_columns_for_table`, `self._filter_to_existing_dclgen_columns`, `self.dclgen_repository.column_names_for_table`.

Control points:

- L52: `if not resolved_table`
- L57: `if mapped_columns`

### `ColumnNameResolver.key_columns_for_record` - L65-L79

```python
key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self.table_name_resolver.table_for_record`, `self.mapping_repository.key_columns_for_record`, `self._filter_to_existing_dclgen_columns`.

Control points:

- L71: `if not table_name`

### `ColumnNameResolver.has_column` - L81-L95

```python
has_column(self, table_name: str, column_name: str) -> bool
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `NameNormalizer.normalize`, `self.dclgen_repository.has_column`.

Control points:

- L89: `if not resolved_table or not normalized_column`

### `ColumnNameResolver._filter_to_existing_dclgen_columns` - L97-L127

```python
_filter_to_existing_dclgen_columns(self, table_name: str, columns: list[str]) -> list[str]
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `set`, `self.dclgen_repository.column_names_for_table`, `self._unique`, `NameNormalizer.normalize`, `output.append`.

Control points:

- L104: `if not resolved_table`
- L111: `if not dclgen_columns`
- L116: `for column in columns`
- L119: `if not normalized`
- L122: `if normalized not in dclgen_columns`

### `ColumnNameResolver._unique` - L129-L148

```python
_unique(self, values: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L136: `for value in values`
- L139: `if not normalized`
- L142: `if normalized in seen`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
