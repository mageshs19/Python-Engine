# `converter/resolvers/relationship_resolver.py`

Source: [converter/resolvers/relationship_resolver.py](../../../../converter/resolvers/relationship_resolver.py) | 123 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `1c26b5533d99e1babac554d53ca0985a46f2162cf6911cef0a66c5a6b2483e01`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L119)

## Import declarations

```python
from __future__ import annotations
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.relationship_child_resolver import RelationshipChildResolver
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
- [converter/resolvers/relationship_child_resolver.py](relationship_child_resolver.md)
- [converter/resolvers/relationship_key_classifier.py](relationship_key_classifier.md)
- [converter/resolvers/relationship_key_column_resolver.py](relationship_key_column_resolver.md)
- [converter/resolvers/relationship_models.py](relationship_models.md)
- [converter/resolvers/relationship_table_lookup.py](relationship_table_lookup.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [converter/resolvers/cursor_column_resolver.py](cursor_column_resolver.md)
- [converter/resolvers/cursor_join_resolver.py](cursor_join_resolver.md)
- [converter/resolvers/cursor_order_by_resolver.py](cursor_order_by_resolver.md)

## Symbol contracts and control points

### `RelationshipResolver` - L23-L116

```python
class RelationshipResolver()
```

Resolves parent-child DB2 relationships using Sheet Mapping metadata.

### `RelationshipResolver.__init__` - L30-L56

```python
__init__(self, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver, host_variable_resolver: HostVariableResolver) -> None
```

Observed calls (lexical order): `RelationshipKeyClassifier`, `RelationshipKeyColumnResolver`, `RelationshipTableLookup`, `RelationshipChildResolver`.

### `RelationshipResolver.resolve_for_child_record` - L58-L62

```python
resolve_for_child_record(self, child_record: str) -> RelationshipResolution
```

Observed calls (lexical order): `self.child_resolver.resolve_for_child_record`.

### `RelationshipResolver.foreign_key_columns_for_record` - L64-L68

```python
foreign_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self.key_column_resolver.foreign_key_columns_for_record`.

### `RelationshipResolver.primary_key_columns_for_record` - L70-L74

```python
primary_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self.key_column_resolver.primary_key_columns_for_record`.

### `RelationshipResolver.parent_key_columns_required_by_children` - L76-L104

```python
parent_key_columns_required_by_children(self, parent_record: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `set`, `self.mapping_repository.records`, `self.resolve_for_child_record`, `seen.add`, `output.append`.

Control points:

- L84: `for child in self.mapping_repository.records()`
- L87: `if child == parent`
- L92: `if relation.parent_record != parent`
- L95: `for condition in relation.conditions`
- L98: `if not column or column in seen`

### `RelationshipResolver.order_by_columns_for_record` - L106-L110

```python
order_by_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self.key_column_resolver.order_by_columns_for_record`.

### `RelationshipResolver.has_foreign_keys` - L112-L116

```python
has_foreign_keys(self, record_name: str) -> bool
```

Observed calls (lexical order): `self.key_column_resolver.has_foreign_keys`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
