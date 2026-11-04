# `converter/repositories/dclgen_repository.py`

Source: [converter/repositories/dclgen_repository.py](../../../../converter/repositories/dclgen_repository.py) | 156 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `ef358ef54ffdab21b03041118591eff3b008c6a6755846c58eeed5740fb24112`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import DclgenColumn
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (25)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/dclgen_include_cleanup.py](../composers/cleanup/dclgen_include_cleanup.md)
- [converter/composers/cobol_cleanup_composer.py](../composers/cobol_cleanup_composer.md)
- [converter/composers/update_program_feedback_composer.py](../composers/update_program_feedback_composer.md)
- [converter/composers/update_sql_cleanup_base.py](../composers/update_sql_cleanup_base.md)
- [converter/generators/sql_generator.py](../generators/sql_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/resolvers/column_name_resolver.py](../resolvers/column_name_resolver.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [converter/resolvers/record_context_resolver.py](../resolvers/record_context_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [converter/resolvers/update_sql_plan_resolver.py](../resolvers/update_sql_plan_resolver.md)
- [converter/validators/mapping_validator.py](../validators/mapping_validator.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/generated_fields/test_compiler_safety_validator.py](../../tests/generated_fields/test_compiler_safety_validator.md)
- [tests/test_compiler_safety_validator.py](../../tests/test_compiler_safety_validator.md)
- [tests/test_field_reference_group_issue_scope.py](../../tests/test_field_reference_group_issue_scope.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)
- [tests/test_handwritten_obtain_calc_planner.py](../../tests/test_handwritten_obtain_calc_planner.md)
- [tests/test_lrf_key_binding_planner.py](../../tests/test_lrf_key_binding_planner.md)
- [tests/test_repositories.py](../../tests/test_repositories.md)
- [tests/test_sql_insert_sequence_metadata.py](../../tests/test_sql_insert_sequence_metadata.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)
- [tests/test_validators.py](../../tests/test_validators.md)
- 2 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `DclgenRepository` - L5-L156

```python
class DclgenRepository()
```

Repository wrapper for DCLGEN columns.

### `DclgenRepository.__init__` - L13-L17

```python
__init__(self, columns: list[DclgenColumn] | None=None) -> None
```

### `DclgenRepository.all` - L19-L22

```python
all(self) -> list[DclgenColumn]
```

Observed calls (lexical order): `list`.

### `DclgenRepository.count` - L24-L27

```python
count(self) -> int
```

Observed calls (lexical order): `len`.

### `DclgenRepository.tables` - L29-L38

```python
tables(self) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `sorted`.

### `DclgenRepository.columns_for_table` - L40-L53

```python
columns_for_table(self, table_name: str) -> list[DclgenColumn]
```

Observed calls (lexical order): `NameNormalizer.normalize`.

Control points:

- L46: `if not target`

### `DclgenRepository.column_names_for_table` - L55-L74

```python
column_names_for_table(self, table_name: str) -> list[str]
```

Observed calls (lexical order): `set`, `self.columns_for_table`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L62: `for column in self.columns_for_table(table_name)`
- L65: `if not name`
- L68: `if name in seen`

### `DclgenRepository.has_table` - L76-L80

```python
has_table(self, table_name: str) -> bool
```

Observed calls (lexical order): `bool`, `self.columns_for_table`.

### `DclgenRepository.has_column` - L82-L92

```python
has_column(self, table_name: str, column_name: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.column_names_for_table`.

Control points:

- L89: `if not target_column`

### `DclgenRepository.host_for_column` - L94-L110

```python
host_for_column(self, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.columns_for_table`, `NameNormalizer.to_cobol`.

Control points:

- L101: `if not target_column`
- L104: `for column in self.columns_for_table(table_name)`
- L105: `if NameNormalizer.normalize(column.column_name) == target_column`

### `DclgenRepository.group_for_table` - L112-L121

```python
group_for_table(self, table_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.to_cobol`.

Control points:

- L118: `if not table`

### `DclgenRepository.host_reference_for_column` - L123-L137

```python
host_reference_for_column(self, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `self.group_for_table`, `self.host_for_column`.

Control points:

- L134: `if not group or not host`

### `DclgenRepository.valid_host_references` - L139-L156

```python
valid_host_references(self) -> set[str]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `self.group_for_table`, `NameNormalizer.to_cobol`, `output.add`.

Control points:

- L144: `for column in self.columns`
- L151: `if group and host`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
