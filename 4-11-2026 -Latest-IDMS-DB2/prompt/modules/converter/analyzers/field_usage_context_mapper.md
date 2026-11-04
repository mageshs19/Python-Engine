# `converter/analyzers/field_usage_context_mapper.py`

Source: [converter/analyzers/field_usage_context_mapper.py](../../../../converter/analyzers/field_usage_context_mapper.py) | 78 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `b2db4353bab3878562f9cd44414d5487bfcda5618a07aa646a12502edd66b1e9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
from rules.field_usage_rules import DCLGEN_GROUP_PREFIX
```

## Local dependency notes

- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/field_usage_rules.py](../../rules/field_usage_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_analyzer.py](field_usage_analyzer.md)

## Symbol contracts and control points

### `FieldUsageContextMapper` - L9-L78

```python
class FieldUsageContextMapper()
```

Builds reusable record and DCLGEN-group context for field usage analysis.

### `FieldUsageContextMapper.__init__` - L14-L21

```python
__init__(self, *, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver) -> None
```

### `FieldUsageContextMapper.mapping_records` - L23-L33

```python
mapping_records(self) -> set[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.records`, `set`.

### `FieldUsageContextMapper.unique_source_field_to_record_map` - L35-L61

```python
unique_source_field_to_record_map(self) -> dict[str, str]
```

Map an unqualified COBOL field to one record only when unique.

Observed calls (lexical order): `self.mapping_records`, `self.mapping_repository.rows_for_record`, `getattr`, `' '.join`, `str`, `str(raw or '').replace`, `str(raw or '').replace('.', ' ').split`, `text.split`, `len`, `parts[0].isdigit`, `NameNormalizer.normalize`, `owners.setdefault`, `owners.setdefault(field, set()).add`, `set`, `iter`, `next`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L44: `for record in self.mapping_records()`
- L45: `for row in self.mapping_repository.rows_for_record(record) or []`
- L46: `for raw in (getattr(row, 'cobol_zone', ''), getattr(row, 'reference_field_name_copybook', ''))`
- L51: `if not text`
- L54: `if len(parts) > 1 and parts[0].isdigit()`
- L56: `if not parts`
- L59: `if field`

### `FieldUsageContextMapper.group_to_record_map` - L63-L78

```python
group_to_record_map(self) -> dict[str, str]
```

Observed calls (lexical order): `self.mapping_records`, `NameNormalizer.normalize`, `self.table_name_resolver.table_for_record`, `NameNormalizer.to_cobol`.

Control points:

- L68: `for record in self.mapping_records()`
- L72: `if not table`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
