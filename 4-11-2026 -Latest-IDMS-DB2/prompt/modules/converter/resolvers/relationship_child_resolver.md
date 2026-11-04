# `converter/resolvers/relationship_child_resolver.py`

Source: [converter/resolvers/relationship_child_resolver.py](../../../../converter/resolvers/relationship_child_resolver.py) | 250 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `003f792556660c05f1e1a02e7d043c385470a1d1f3015337ef5c5c4c295eaf43`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from typing import Any
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.relationship_key_classifier import RelationshipKeyClassifier
from converter.resolvers.relationship_key_column_resolver import RelationshipKeyColumnResolver
from converter.resolvers.relationship_models import RelationshipCondition, RelationshipResolution
from converter.resolvers.relationship_table_lookup import RelationshipTableLookup
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](host_variable_resolver.md)
- [converter/resolvers/relationship_key_classifier.py](relationship_key_classifier.md)
- [converter/resolvers/relationship_key_column_resolver.py](relationship_key_column_resolver.md)
- [converter/resolvers/relationship_models.py](relationship_models.md)
- [converter/resolvers/relationship_table_lookup.py](relationship_table_lookup.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)

## Symbol contracts and control points

### `RelationshipChildResolver` - L22-L250

```python
class RelationshipChildResolver()
```

Resolves full parent-child relationship conditions for one child record.

### `RelationshipChildResolver.__init__` - L27-L42

```python
__init__(self, *, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver, host_variable_resolver: HostVariableResolver, key_column_resolver: RelationshipKeyColumnResolver, table_lookup: RelationshipTableLookup, classifier: RelationshipKeyClassifier | None=None) -> None
```

Observed calls (lexical order): `RelationshipKeyClassifier`.

### `RelationshipChildResolver.resolve_for_child_record` - L44-L99

```python
resolve_for_child_record(self, child_record: str) -> RelationshipResolution
```

Observed calls (lexical order): `NameNormalizer.normalize`, `RelationshipResolution`, `result.diagnostics.append`, `self.table_name_resolver.table_for_record`, `self.mapping_repository.rows_for_record`, `self.classifier.is_foreign_key_row`, `self._infer_parent_record`, `self._append_conditions_from_fk_rows`, `len`.

Control points:

- L51: `if not child`
- L65: `if not fk_rows`
- L78: `if parent_record`

### `RelationshipChildResolver._append_conditions_from_fk_rows` - L101-L166

```python
_append_conditions_from_fk_rows(self, *, result: RelationshipResolution, child: str, child_table: str, fk_rows: list[Any], parent_record: str, parent_table: str) -> None
```

Observed calls (lexical order): `NameNormalizer.normalize`, `getattr`, `self.table_name_resolver.resolve_table`, `self.table_lookup.find_parent_table_by_column`, `result.diagnostics.append`, `self.table_lookup.record_for_table`, `self._append_condition`.

Control points:

- L113: `for row in fk_rows`
- L119: `if not child_column`
- L133: `if not effective_parent_table`
- L142: `if not effective_parent_table`
- L149: `if not resolved_parent_record`
- L155: `if not result.parent_table`

### `RelationshipChildResolver._append_condition` - L168-L202

```python
_append_condition(self, *, result: RelationshipResolution, child: str, child_table: str, child_column: str, parent_record: str, parent_table: str, parent_column: str) -> None
```

Observed calls (lexical order): `self.host_variable_resolver.host_reference_for_column`, `result.diagnostics.append`, `result.conditions.append`, `RelationshipCondition`.

Control points:

- L184: `if not parent_host`

### `RelationshipChildResolver._infer_parent_record` - L204-L250

```python
_infer_parent_record(self, *, child_record: str, fk_rows: list[Any]) -> str
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `getattr`, `self.table_lookup.record_for_table`, `NameNormalizer.normalize`, `self.mapping_repository.records`, `set`, `self.key_column_resolver.primary_key_columns_for_record`, `len`, `parent_keys.intersection`.

Control points:

- L210: `for row in fk_rows`
- L215: `if parent_table`
- L217: `if record`
- L231: `for record in self.mapping_repository.records()`
- L234: `if record == child_record`
- L241: `if not parent_keys`
- L246: `if match_count > best_count`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
