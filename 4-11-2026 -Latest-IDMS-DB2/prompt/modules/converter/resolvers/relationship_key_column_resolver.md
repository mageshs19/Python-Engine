# `converter/resolvers/relationship_key_column_resolver.py`

Source: [converter/resolvers/relationship_key_column_resolver.py](../../../../converter/resolvers/relationship_key_column_resolver.py) | 162 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `9b6c1a0b6ae755fc1e1f6d95fd83ef2c1d00db62893c462753cf101cbc42965d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.relationship_key_classifier import RelationshipKeyClassifier
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_declaration_rules import CURSOR_ORDER_BY_MESSAGES, ORDER_BY_SOURCE_PRIMARY_KEY
```

## Local dependency notes

- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/relationship_key_classifier.py](relationship_key_classifier.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/cursor_declaration_rules.py](../../rules/cursor_declaration_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/relationship_child_resolver.py](relationship_child_resolver.md)
- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)

## Symbol contracts and control points

### `RelationshipKeyColumnResolver` - L13-L162

```python
class RelationshipKeyColumnResolver()
```

Resolves primary-key, foreign-key, and order-by columns for records.

### `RelationshipKeyColumnResolver.__init__` - L18-L26

```python
__init__(self, *, mapping_repository: MappingRepository, classifier: RelationshipKeyClassifier | None=None) -> None
```

Observed calls (lexical order): `RelationshipKeyClassifier`.

### `RelationshipKeyColumnResolver.foreign_key_columns_for_record` - L28-L52

```python
foreign_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `set`, `self.classifier.is_foreign_key_row`, `getattr`, `seen.add`, `output.append`.

Control points:

- L37: `for row in rows`
- L38: `if not self.classifier.is_foreign_key_row(row)`
- L46: `if not column or column in seen`

### `RelationshipKeyColumnResolver.primary_key_columns_for_record` - L54-L77

```python
primary_key_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `set`, `self.classifier.is_primary_key_row`, `getattr`, `seen.add`, `output.append`.

Control points:

- L63: `for row in rows`
- L64: `if not self.classifier.is_primary_key_row(row)`
- L71: `if not column or column in seen`

### `RelationshipKeyColumnResolver.order_by_columns_for_record` - L82-L118

```python
order_by_columns_for_record(self, record_name: str) -> list[str]
```

ORDER BY columns inferred from the record's own key.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.primary_key_columns_for_record`, `self.foreign_key_columns_for_record`, `set`, `output.append`, `self._report_order_by`.

Control points:

- L103: `for column in primary_keys`
- L106: `if not normalized`
- L108: `if normalized in foreign_keys`
- L110: `if normalized not in output`

### `RelationshipKeyColumnResolver._report_order_by` - L120-L156

```python
_report_order_by(self, *, record: str, primary_keys: list[str], output: list[str]) -> None
```

Say where the ORDER BY came from, or why there is none.

Observed calls (lexical order): `getattr`, `messages.append`, `CURSOR_ORDER_BY_MESSAGES['resolved'].format`, `len`, `', '.join`, `CURSOR_ORDER_BY_MESSAGES['empty_all_foreign'].format`, `CURSOR_ORDER_BY_MESSAGES['empty_no_primary_key'].format`.

Control points:

- L129: `if messages is None`
- L133: `if output`
- L144: `if primary_keys`

### `RelationshipKeyColumnResolver.has_foreign_keys` - L158-L162

```python
has_foreign_keys(self, record_name: str) -> bool
```

Observed calls (lexical order): `bool`, `self.foreign_key_columns_for_record`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
