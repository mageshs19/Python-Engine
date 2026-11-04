# `converter/repositories/mapping_key_resolver.py`

Source: [converter/repositories/mapping_key_resolver.py](../../../../converter/repositories/mapping_key_resolver.py) | 126 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `c2597ac90b2a90b198a03d834d7b60d2076e6cbe888ae5e5d0a755f4aa4c3976`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sheet Mapping key-column resolution.

## Import declarations

```python
from __future__ import annotations
from converter.repositories.mapping_row_query import MappingRowQuery
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/repositories/mapping_row_query.py](mapping_row_query.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/repositories/mapping_column_resolver.py](mapping_column_resolver.md)
- [converter/repositories/mapping_repository.py](mapping_repository.md)

## Symbol contracts and control points

### `MappingKeyResolver` - L16-L126

```python
class MappingKeyResolver()
```

### `MappingKeyResolver.__init__` - L17-L21

```python
__init__(self, query: MappingRowQuery) -> None
```

### `MappingKeyResolver.primary_key_columns_for_record` - L23-L72

```python
primary_key_columns_for_record(self, record_name: str) -> list[str]
```

Return all primary-key-style columns for DB2 WHERE clauses.

Observed calls (lexical order): `set`, `self.query.rows_for_record`, `NameNormalizer.normalize`, `getattr`, `' '.join`, `seen.add`, `output.append`.

Control points:

- L38: `for row in self.query.rows_for_record(record_name)`
- L46: `if not column`
- L52: `if 'FOREIGN' in key_text`
- L54: `if ' FK ' in padded_key_text`
- L64: `if not is_key_column`
- L66: `if column in seen`

### `MappingKeyResolver.foreign_key_columns_for_record` - L74-L107

```python
foreign_key_columns_for_record(self, record_name: str) -> list[str]
```

Return FK / FOREIGN / relationship columns for a record.

Observed calls (lexical order): `set`, `self.query.rows_for_record`, `NameNormalizer.normalize`, `getattr`, `' '.join`, `seen.add`, `output.append`.

Control points:

- L87: `for row in self.query.rows_for_record(record_name)`
- L94: `if not is_foreign`
- L101: `if not column or column in seen`

### `MappingKeyResolver.non_key_columns_for_record` - L109-L126

```python
non_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `set`, `self.primary_key_columns_for_record`, `self.query.rows_for_record`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L119: `for row in self.query.rows_for_record(record_name)`
- L121: `if not column or column in key_columns or column in seen`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
