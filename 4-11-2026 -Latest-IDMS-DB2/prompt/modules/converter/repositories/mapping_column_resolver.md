# `converter/repositories/mapping_column_resolver.py`

Source: [converter/repositories/mapping_column_resolver.py](../../../../converter/repositories/mapping_column_resolver.py) | 136 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `856b6e8953662e3ee6e0559f9a32aab611085e1a58dd46675515b186c2b35359`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sheet Mapping column resolution.

## Import declarations

```python
from __future__ import annotations
from converter.repositories.mapping_key_resolver import MappingKeyResolver
from converter.repositories.mapping_row_query import MappingRowQuery
from converter.services.name_normalizer import NameNormalizer
from rules.field_naming_rules import INSERT_ONLY_AUDIT_PREFIXES, UPDATE_AUDIT_PREFIXES, canonical_field_key
```

## Local dependency notes

- [converter/repositories/mapping_key_resolver.py](mapping_key_resolver.md)
- [converter/repositories/mapping_row_query.py](mapping_row_query.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/field_naming_rules.py](../../rules/field_naming_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/repositories/mapping_repository.py](mapping_repository.md)

## Symbol contracts and control points

### `MappingColumnResolver` - L26-L136

```python
class MappingColumnResolver()
```

### `MappingColumnResolver.__init__` - L27-L33

```python
__init__(self, query: MappingRowQuery, key_resolver: MappingKeyResolver) -> None
```

### `MappingColumnResolver.column_for_source_field` - L35-L66

```python
column_for_source_field(self, record_name: str, source_field_name: str) -> str
```

Resolve a COBOL source field to its DB2 column via the Sheet Mapping row directly. Each row pairs the COBOL-side identifier with the DB2 column, so this is an exact canonical-key lookup. Deterministic only.

Observed calls (lexical order): `canonical_field_key`, `self.query.rows_for_record`, `NameNormalizer.normalize`.

Control points:

- L46: `if not source_key`
- L49: `for row in self.query.rows_for_record(record_name)`
- L53: `if not column`
- L56: `for candidate in (row.cobol_zone, row.reference_field_name_copybook, row.new_db2_field_name, row.cross_application_db2_field_name)`
- L62: `if canonical_field_key(candidate) == source_key`

### `MappingColumnResolver.update_audit_columns_for_record` - L68-L88

```python
update_audit_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `set`, `self.query.rows_for_record`, `NameNormalizer.normalize`, `column.startswith`, `seen.add`, `output.append`.

Control points:

- L75: `for row in self.query.rows_for_record(record_name)`
- L77: `if not column`
- L79: `if column.startswith(INSERT_ONLY_AUDIT_PREFIXES)`
- L81: `if not column.startswith(UPDATE_AUDIT_PREFIXES)`
- L83: `if column in seen`

### `MappingColumnResolver.update_candidate_columns_for_record` - L90-L136

```python
update_candidate_columns_for_record(self, record_name: str, changed_source_fields: list[str] | None=None) -> list[str]
```

Return conservative UPDATE candidate columns.

Observed calls (lexical order): `set`, `self.key_resolver.primary_key_columns_for_record`, `NameNormalizer.normalize`, `self.column_for_source_field`, `column.startswith`, `seen.add`, `output.append`, `self.update_audit_columns_for_record`.

Control points:

- L111: `for source_field in changed_source_fields or []`
- L118: `if not column`
- L120: `if column in key_columns`
- L122: `if column.startswith(INSERT_ONLY_AUDIT_PREFIXES)`
- L124: `if column in seen`
- L129: `for column in self.update_audit_columns_for_record(record_name)`
- L131: `if not column or column in key_columns or column in seen`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
