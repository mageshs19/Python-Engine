# `converter/repositories/mapping_repository.py`

Source: [converter/repositories/mapping_repository.py](../../../../converter/repositories/mapping_repository.py) | 283 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `a9a5d4bc934fcee0fd04e50327c98d69b336ffd7319786745b47b37fe277d7d4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Repository wrapper for Sheet Mapping rows.

## Module-level bindings

`LEVEL_NUMBER_MAX_WIDTH` (L32), `__all__` (L281)

## Import declarations

```python
from __future__ import annotations
from catalogs.db2_naming_catalog import DB2_TABLE_SUFFIX_EQUIVALENTS
from converter.domain.models import SheetMappingRow
from converter.repositories.mapping_column_resolver import MappingColumnResolver
from converter.repositories.mapping_key_resolver import MappingKeyResolver
from converter.repositories.mapping_row_query import MappingRowQuery
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [catalogs/db2_naming_catalog.py](../../catalogs/db2_naming_catalog.md)
- [converter/domain/models.py](../domain/models.md)
- [converter/repositories/mapping_column_resolver.py](mapping_column_resolver.md)
- [converter/repositories/mapping_key_resolver.py](mapping_key_resolver.md)
- [converter/repositories/mapping_row_query.py](mapping_row_query.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (35)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_analyzer.py](../analyzers/field_usage_analyzer.md)
- [converter/analyzers/field_usage_context_mapper.py](../analyzers/field_usage_context_mapper.md)
- [converter/composers/update_program_feedback_composer.py](../composers/update_program_feedback_composer.md)
- [converter/composers/update_sql_cleanup_base.py](../composers/update_sql_cleanup_base.md)
- [converter/generators/sql_generator.py](../generators/sql_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/postprocess/update_program_enhancer.py](../postprocess/update_program_enhancer.md)
- [converter/resolvers/access_type_classifier.py](../resolvers/access_type_classifier.md)
- [converter/resolvers/column_name_resolver.py](../resolvers/column_name_resolver.md)
- [converter/resolvers/cursor_column_resolver.py](../resolvers/cursor_column_resolver.md)
- [converter/resolvers/cursor_field_usage_column_selector.py](../resolvers/cursor_field_usage_column_selector.md)
- [converter/resolvers/cursor_order_by_resolver.py](../resolvers/cursor_order_by_resolver.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_field_reference_group_issue_scope.py](../../tests/test_field_reference_group_issue_scope.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)
- [tests/test_handwritten_obtain_calc_planner.py](../../tests/test_handwritten_obtain_calc_planner.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_lrf_key_binding_planner.py](../../tests/test_lrf_key_binding_planner.md)
- [tests/test_lrf_select_projection_analysis.py](../../tests/test_lrf_select_projection_analysis.md)
- [tests/test_repositories.py](../../tests/test_repositories.md)
- [tests/test_sql_insert_sequence_metadata.py](../../tests/test_sql_insert_sequence_metadata.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)
- [tests/test_unqualified_field_usage.py](../../tests/test_unqualified_field_usage.md)
- [tests/test_validators.py](../../tests/test_validators.md)
- 11 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `_cobol_name_of` - L35-L49

```python
_cobol_name_of(value: str) -> str
```

The bare COBOL data name from a Sheet Mapping COBOL Zone cell.

Observed calls (lexical order): `' '.join`, `str`, `str(value or '').split`, `text.split`, `len`, `parts[0].isdigit`, `parts[0].upper`.

Control points:

- L38: `if not text`
- L42: `if len(parts) > 1 and parts[0].isdigit() and (len(parts[0]) <= LEVEL_NUMBER_MAX_WIDTH)`

### `MappingRepository` - L52-L278

```python
class MappingRepository()
```

### `MappingRepository.__init__` - L53-L60

```python
__init__(self, rows: list[SheetMappingRow] | None=None) -> None
```

Observed calls (lexical order): `MappingRowQuery`, `MappingKeyResolver`, `MappingColumnResolver`.

### `MappingRepository.all` - L63-L64

```python
all(self) -> list[SheetMappingRow]
```

Observed calls (lexical order): `self._query.all`.

### `MappingRepository.count` - L66-L67

```python
count(self) -> int
```

Observed calls (lexical order): `self._query.count`.

### `MappingRepository.records` - L69-L70

```python
records(self) -> list[str]
```

Observed calls (lexical order): `self._query.records`.

### `MappingRepository.tables` - L72-L73

```python
tables(self) -> list[str]
```

Observed calls (lexical order): `self._query.tables`.

### `MappingRepository.rows_for_record` - L75-L79

```python
rows_for_record(self, record_name: str) -> list[SheetMappingRow]
```

Observed calls (lexical order): `self._query.rows_for_record`.

### `MappingRepository.rows_for_table` - L81-L85

```python
rows_for_table(self, table_name: str) -> list[SheetMappingRow]
```

Observed calls (lexical order): `self._query.rows_for_table`.

### `MappingRepository.db2_columns_for_table` - L87-L91

```python
db2_columns_for_table(self, table_name: str) -> list[str]
```

Observed calls (lexical order): `self._query.db2_columns_for_table`.

### `MappingRepository.db2_table_for_record` - L93-L97

```python
db2_table_for_record(self, record_name: str) -> str
```

Observed calls (lexical order): `self._query.db2_table_for_record`.

### `MappingRepository.has_record` - L99-L100

```python
has_record(self, record_name: str) -> bool
```

Observed calls (lexical order): `bool`, `self._query.rows_for_record`.

### `MappingRepository.has_table` - L102-L103

```python
has_table(self, table_name: str) -> bool
```

Observed calls (lexical order): `bool`, `self._query.rows_for_table`.

### `MappingRepository.key_columns_for_record` - L106-L110

```python
key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self._keys.primary_key_columns_for_record`.

### `MappingRepository.primary_key_columns_for_record` - L112-L116

```python
primary_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self._keys.primary_key_columns_for_record`.

### `MappingRepository.foreign_key_columns_for_record` - L118-L122

```python
foreign_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self._keys.foreign_key_columns_for_record`.

### `MappingRepository.non_key_columns_for_record` - L124-L128

```python
non_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self._keys.non_key_columns_for_record`.

### `MappingRepository.column_for_source_field` - L131-L139

```python
column_for_source_field(self, record_name: str, source_field_name: str) -> str
```

Observed calls (lexical order): `self._columns.column_for_source_field`.

### `MappingRepository.update_audit_columns_for_record` - L141-L145

```python
update_audit_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self._columns.update_audit_columns_for_record`.

### `MappingRepository.update_candidate_columns_for_record` - L147-L155

```python
update_candidate_columns_for_record(self, record_name: str, changed_source_fields: list[str] | None=None) -> list[str]
```

Observed calls (lexical order): `self._columns.update_candidate_columns_for_record`.

### `MappingRepository.cobol_field_for_column` - L173-L237

```python
cobol_field_for_column(self, table_name: str='', column_name: str='') -> str
```

The COBOL Zone this DB2 column was mapped FROM.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.records`, `self.db2_table_for_record`, `self.rows_for_record`, `getattr`, `_cobol_name_of`.

Control points:

- L204: `if not target`
- L209: `for restrict_to_table in (True, False)`
- L210: `if restrict_to_table and (not wanted_table)`
- L213: `for record in self.records()`
- L214: `if restrict_to_table`
- L218: `if record_table and record_table != wanted_table`
- L221: `for row in self.rows_for_record(record) or []`
- L226: `if column != target`
- Another 2 conditions/loops exist in this source span.

### `MappingRepository._restart_table_candidates` - L240-L264

```python
_restart_table_candidates(self, table_name: str) -> list[str]
```

All equivalent DB2 table spellings (TB/TV) for confirmation.

Observed calls (lexical order): `NameNormalizer.normalize`, `normalized.endswith`, `candidates.append`, `len`, `set`, `seen.add`, `output.append`.

Control points:

- L247: `if not normalized`
- L251: `for (source_suffix, target_suffix) in DB2_TABLE_SUFFIX_EQUIVALENTS`
- L252: `if normalized.endswith(source_suffix)`
- L260: `for candidate in candidates`
- L261: `if candidate and candidate not in seen`

### `MappingRepository.confirms_restart_table` - L266-L278

```python
confirms_restart_table(self, table_name: str) -> bool
```

True when the Sheet Mapping contains this DB2 table under ANY equivalent TB/TV spelling.

Observed calls (lexical order): `self._restart_table_candidates`, `self.has_table`.

Control points:

- L275: `for candidate in self._restart_table_candidates(table_name)`
- L276: `if self.has_table(candidate)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
