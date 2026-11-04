# `converter/resolvers/access_type_classifier.py`

Source: [converter/resolvers/access_type_classifier.py](../../../../converter/resolvers/access_type_classifier.py) | 127 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `54c7505ae4e8b7c3789cda40ef9e1f7a424873cddb35780380f306bed85bc421`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Classifies IDMS record access types (CALC DN, CALC DL, VIA).

## Module-level bindings

`__all__` (L127)

## Import declarations

```python
from __future__ import annotations
from typing import Any
from converter.repositories.mapping_repository import MappingRepository
from converter.services.name_normalizer import NameNormalizer
from rules.key_naming_rules import IDENTITY_KEY_PREFIXES
```

## Local dependency notes

- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/key_naming_rules.py](../../rules/key_naming_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/cursor_order_by_resolver.py](cursor_order_by_resolver.md)

## Symbol contracts and control points

### `AccessTypeClassifier` - L19-L124

```python
class AccessTypeClassifier()
```

Determines if record is CALC DN, CALC DL, or VIA accessed.

### `AccessTypeClassifier.__init__` - L22-L23

```python
__init__(self, mapping_repository: MappingRepository) -> None
```

### `AccessTypeClassifier.is_calc_dn` - L25-L45

```python
is_calc_dn(self, record_name: str) -> bool
```

CALC DN - no duplicate key values allowed.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `getattr`, `self._is_seq_no_field`.

Control points:

- L34: `for row in rows`
- L36: `if 'CALC' in idms_key`
- L42: `if self._is_seq_no_field(column_name)`

### `AccessTypeClassifier.is_calc_dl` - L47-L67

```python
is_calc_dl(self, record_name: str) -> bool
```

CALC DL - duplicate key values allowed (newest kept).

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `getattr`, `self._is_seq_no_field`.

Control points:

- L56: `for row in rows`
- L58: `if 'CALC' in idms_key`
- L64: `if self._is_seq_no_field(column_name)`

### `AccessTypeClassifier.is_via_accessed` - L69-L85

```python
is_via_accessed(self, record_name: str) -> bool
```

VIA - accessed through set relationship (child record).

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `getattr`.

Control points:

- L75: `for row in rows`
- L79: `if 'FOREIGN' in db2_key or 'FK' in db2_key`
- L82: `if 'CALC' not in idms_key`

### `AccessTypeClassifier.has_seq_no_field` - L87-L99

```python
has_seq_no_field(self, record_name: str) -> bool
```

True if record has a seq.no field (NR_ID_ with underscore).

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `getattr`, `self._is_seq_no_field`.

Control points:

- L92: `for row in rows`
- L96: `if self._is_seq_no_field(column_name)`

### `AccessTypeClassifier.seq_no_field_count` - L101-L114

```python
seq_no_field_count(self, record_name: str) -> int
```

Count of seq.no fields (NR_ID_ fields) in the record.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `getattr`, `self._is_seq_no_field`.

Control points:

- L107: `for row in rows`
- L111: `if self._is_seq_no_field(column_name)`

### `AccessTypeClassifier._is_seq_no_field` - L117-L124

```python
_is_seq_no_field(column_name: str) -> bool
```

True if column name starts with NR_ID_ (with underscore).

Observed calls (lexical order): `str`, `str(column_name or '').strip`, `str(column_name or '').strip().upper`, `normalized.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
