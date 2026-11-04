# `converter/resolvers/table_name_resolver.py`

Source: [converter/resolvers/table_name_resolver.py](../../../../converter/resolvers/table_name_resolver.py) | 128 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `f09dd49e737e812977fc311c9c9b7652237fa3a57754d94036161ff40d391d97`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from catalogs.db2_naming_catalog import DB2_TABLE_SUFFIX_EQUIVALENTS
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [catalogs/db2_naming_catalog.py](../../catalogs/db2_naming_catalog.md)
- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (28)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_analyzer.py](../analyzers/field_usage_analyzer.md)
- [converter/analyzers/field_usage_context_mapper.py](../analyzers/field_usage_context_mapper.md)
- [converter/composers/unmapped_record_block_composer.py](../composers/unmapped_record_block_composer.md)
- [converter/composers/update_program_feedback_composer.py](../composers/update_program_feedback_composer.md)
- [converter/composers/update_sql_cleanup_base.py](../composers/update_sql_cleanup_base.md)
- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [converter/generators/sql_generator.py](../generators/sql_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/resolvers/column_name_resolver.py](column_name_resolver.md)
- [converter/resolvers/cursor_column_filter.py](cursor_column_filter.md)
- [converter/resolvers/cursor_column_resolver.py](cursor_column_resolver.md)
- [converter/resolvers/host_variable_resolver.py](host_variable_resolver.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_field_reference_group_issue_scope.py](../../tests/test_field_reference_group_issue_scope.md)
- [tests/test_handwritten_obtain_calc_planner.py](../../tests/test_handwritten_obtain_calc_planner.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_lrf_key_binding_planner.py](../../tests/test_lrf_key_binding_planner.md)
- [tests/test_sql_insert_sequence_metadata.py](../../tests/test_sql_insert_sequence_metadata.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)
- [tests/test_validators.py](../../tests/test_validators.md)
- 8 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `TableNameResolver` - L7-L128

```python
class TableNameResolver()
```

Resolves DB2 table names.

### `TableNameResolver.__init__` - L22-L28

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository) -> None
```

### `TableNameResolver.resolve_table` - L30-L43

```python
resolve_table(self, table_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.table_candidates`, `self.dclgen_repository.has_table`.

Control points:

- L36: `if not normalized`
- L39: `for candidate in self.table_candidates(normalized)`
- L40: `if self.dclgen_repository.has_table(candidate)`

### `TableNameResolver.table_for_record` - L45-L54

```python
table_for_record(self, record_name: str) -> str
```

Observed calls (lexical order): `self.mapping_repository.db2_table_for_record`, `self.resolve_table`.

Control points:

- L51: `if not mapped_table`

### `TableNameResolver.table_candidates` - L56-L95

```python
table_candidates(self, table_name: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `normalized.endswith`, `output.append`, `len`, `NameNormalizer.to_cobol`, `NameNormalizer.compact`, `final.append`.

Control points:

- L62: `if not normalized`
- L67: `for (source_suffix, target_suffix) in DB2_TABLE_SUFFIX_EQUIVALENTS`
- L68: `if normalized.endswith(source_suffix)`
- L76: `if cobol_name`
- L79: `if compact_name`
- L84: `for item in output`
- L87: `if not normalized_item`
- L90: `if normalized_item in final`

### `TableNameResolver.known_dclgen_tables` - L97-L100

```python
known_dclgen_tables(self) -> list[str]
```

Observed calls (lexical order): `self.dclgen_repository.tables`.

### `TableNameResolver.known_mapping_tables` - L102-L105

```python
known_mapping_tables(self) -> list[str]
```

Observed calls (lexical order): `self.mapping_repository.tables`.

### `TableNameResolver.has_resolved_table` - L107-L116

```python
has_resolved_table(self, table_name: str) -> bool
```

Observed calls (lexical order): `self.resolve_table`, `self.dclgen_repository.has_table`.

Control points:

- L113: `if not resolved`

### `TableNameResolver.context_strength` - L118-L128

```python
context_strength(self, record_name: str) -> int
```

Observed calls (lexical order): `self.mapping_repository.has_record`.

Control points:

- L122: `if not record_name`
- L125: `if self.mapping_repository.has_record(record_name)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
