# `converter/resolvers/relationship_table_lookup.py`

Source: [converter/resolvers/relationship_table_lookup.py](../../../../converter/resolvers/relationship_table_lookup.py) | 70 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `f7ff91da9bec7aa5f716f372b78c28a57ff3129edea56c3704fcf7b9b9772387`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/relationship_child_resolver.py](relationship_child_resolver.md)
- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)

## Symbol contracts and control points

### `RelationshipTableLookup` - L8-L70

```python
class RelationshipTableLookup()
```

Resolves records from DB2 tables and parent tables from key columns.

### `RelationshipTableLookup.__init__` - L13-L20

```python
__init__(self, *, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver) -> None
```

### `RelationshipTableLookup.record_for_table` - L22-L37

```python
record_for_table(self, table_name: str) -> str
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `self.mapping_repository.records`, `self.table_name_resolver.table_for_record`, `NameNormalizer.normalize`.

Control points:

- L28: `if not table`
- L31: `for record in self.mapping_repository.records()`
- L34: `if record_table == table`

### `RelationshipTableLookup.find_parent_table_by_column` - L39-L70

```python
find_parent_table_by_column(self, *, child_record: str, child_column: str, primary_key_columns_for_record) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.table_name_resolver.table_for_record`, `self.mapping_repository.records`, `primary_key_columns_for_record`.

Control points:

- L48: `if not column`
- L53: `for record in self.mapping_repository.records()`
- L56: `if normalized_record == child_record`
- L61: `if not table`
- L64: `if table == child_table`
- L67: `if column in primary_key_columns_for_record(normalized_record)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
