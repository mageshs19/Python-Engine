# `converter/resolvers/update_sql_plan_resolver.py`

Source: [converter/resolvers/update_sql_plan_resolver.py](../../../../converter/resolvers/update_sql_plan_resolver.py) | 179 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `dce2f83feab7005162b2b09ffd37ad99c9582b1277777dcb300b7aee05dfde3c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from dataclasses import dataclass, field
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/sql_generator.py](../generators/sql_generator.md)

## Symbol contracts and control points

### `UpdateSqlPlan` - L11-L25

```python
class UpdateSqlPlan()
```

Declared class/data-model fields:

```python
record_name: str = ''
table_name: str = ''
key_columns: list[str] = field(default_factory=list)
update_columns: list[str] = field(default_factory=list)
diagnostics: list[str] = field(default_factory=list)
```

### `UpdateSqlPlan.is_complete` - L19-L25

```python
is_complete(self) -> bool
```

Observed calls (lexical order): `bool`.

### `UpdateSqlPlanResolver` - L28-L179

```python
class UpdateSqlPlanResolver()
```

Resolves conservative UPDATE SQL plans.

### `UpdateSqlPlanResolver.__init__` - L41-L51

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository, table_name_resolver: TableNameResolver, host_variable_resolver: HostVariableResolver) -> None
```

### `UpdateSqlPlanResolver.resolve` - L53-L104

```python
resolve(self, record_name: str, changed_source_fields: list[str] | None=None) -> UpdateSqlPlan
```

Observed calls (lexical order): `NameNormalizer.normalize`, `UpdateSqlPlan`, `plan.diagnostics.append`, `self.mapping_repository.db2_table_for_record`, `self.table_name_resolver.resolve_table`, `self._primary_key_columns_for_record`, `self._filter_to_dclgen_columns`, `self.mapping_repository.update_candidate_columns_for_record`, `self._unique`.

Control points:

- L61: `if not record`
- L68: `if not resolved_table`
- L82: `if not key_columns`
- L96: `if not update_columns`

### `UpdateSqlPlanResolver._primary_key_columns_for_record` - L106-L125

```python
_primary_key_columns_for_record(self, record_name: str) -> list[str]
```

Return DB2 primary-key columns only.

Observed calls (lexical order): `hasattr`, `self.mapping_repository.primary_key_columns_for_record`.

Control points:

- L122: `if not hasattr(self.mapping_repository, 'primary_key_columns_for_record')`

### `UpdateSqlPlanResolver._filter_to_dclgen_columns` - L127-L158

```python
_filter_to_dclgen_columns(self, table_name: str, columns: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self.dclgen_repository.column_names_for_table`, `NameNormalizer.normalize`, `self.host_variable_resolver.has_host_for_column`, `output.append`, `self._unique`.

Control points:

- L136: `if not dclgen_columns`
- L141: `for column in columns`
- L144: `if not normalized`
- L147: `if normalized not in dclgen_columns`
- L150: `if not self.host_variable_resolver.has_host_for_column(table_name=table_name, column_name=normalized)`

### `UpdateSqlPlanResolver._unique` - L160-L179

```python
_unique(self, values: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L167: `for value in values`
- L170: `if not normalized`
- L173: `if normalized in seen`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
