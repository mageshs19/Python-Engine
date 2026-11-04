# `converter/resolvers/cursor_order_by_resolver.py`

Source: [converter/resolvers/cursor_order_by_resolver.py](../../../../converter/resolvers/cursor_order_by_resolver.py) | 491 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `cc0a3f88f7bfde23d8a05227e7841e76de6693f198397eeba90c2dffd4cebb92`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Resolves cursor ORDER BY columns.

## Module-level bindings

`WORD_SEPARATORS` (L80), `MESSAGE_PLACEHOLDER_DEFAULTS` (L84), `__all__` (L491)

## Import declarations

```python
from __future__ import annotations
from string import Formatter
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.access_type_classifier import AccessTypeClassifier
from converter.resolvers.cursor_column_filter import CursorColumnFilter
from converter.resolvers.relationship_resolver import RelationshipResolver
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_column_rules import CURSOR_ORDER_BY_MESSAGES, DESC_HINT_FIELDS, DESC_HINT_WORDS, EMIT_EXPLICIT_ASC, EMIT_ORDER_BY_DIRECTION, ENFORCE_ORDER_BY_COLUMN_VALIDATION, NON_COLUMN_SENTINELS, ORDER_BY_DIRECTION_ASC, ORDER_BY_DIRECTION_DESC, ORDER_HINT_WORDS
from rules.cursor_declaration_rules import ORDER_BY_KEY_MESSAGES, ORDER_BY_NARROWING_APPLIES_TO_CHILD, ORDER_BY_PREFER_IDENTITY_KEY, ORDER_BY_SOURCE_CHILD_KEY, ORDER_BY_SOURCE_PARENT_INTENT
from rules.key_naming_rules import IDENTITY_KEY_PREFIXES
```

## Local dependency notes

- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/access_type_classifier.py](access_type_classifier.md)
- [converter/resolvers/cursor_column_filter.py](cursor_column_filter.md)
- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/cursor_column_rules.py](../../rules/cursor_column_rules.md)
- [rules/cursor_declaration_rules.py](../../rules/cursor_declaration_rules.md)
- [rules/key_naming_rules.py](../../rules/key_naming_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/cursor_column_resolver.py](cursor_column_resolver.md)

## Symbol contracts and control points

### `_prefix_tuple` - L96-L102

```python
_prefix_tuple(prefixes) -> tuple[str, ...]
```

Normalised upper-case tuple - str.startswith() requires a tuple.

Observed calls (lexical order): `tuple`, `str`, `str(prefix or '').strip`, `str(prefix or '').strip().upper`.

### `CursorOrderByResolver` - L105-L488

```python
class CursorOrderByResolver()
```

Resolves cursor ORDER BY columns.

Declared class/data-model fields:

```python
MESSAGES = {**dict(ORDER_BY_KEY_MESSAGES or {}), **dict(CURSOR_ORDER_BY_MESSAGES or {})}
```

### `CursorOrderByResolver.__init__` - L115-L126

```python
__init__(self, mapping_repository: MappingRepository, relationship_resolver: RelationshipResolver, column_filter: CursorColumnFilter) -> None
```

Observed calls (lexical order): `_prefix_tuple`, `AccessTypeClassifier`.

### `CursorOrderByResolver.reset` - L131-L133

```python
reset(self) -> None
```

Clear per-program diagnostics.

### `CursorOrderByResolver.order_by_columns_for_record` - L138-L198

```python
order_by_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.access_type_classifier.is_calc_dn`, `self._log`, `self.relationship_resolver.has_foreign_keys`, `self.order_by_base_columns_for_record`, `self.explicit_parent_order_columns`, `self._valid_order_columns`, `self._narrowed_order_columns`, `self._expression`, `self.column_filter.unique`, `len`, `', '.join`.

Control points:

- L140: `if not record`
- L144: `if self.access_type_classifier.is_calc_dn(record)`
- L150: `if is_child`
- L163: `if not columns`
- L191: `if not EMIT_ORDER_BY_DIRECTION`

### `CursorOrderByResolver.explicit_parent_order_columns` - L203-L231

```python
explicit_parent_order_columns(self, record_name: str) -> list[str]
```

Parent/root columns whose Sheet Mapping row states order intent.

Observed calls (lexical order): `self.mapping_repository.rows_for_record`, `' '.join`, `' '.join([str(getattr(row, 'remarks', '') or ''), str(getattr(row, 'hopex_expression_type_remark', '') or '...`, `getattr`, `str`, `self._mentions_any`, `NameNormalizer.normalize`, `output.append`.

Control points:

- L212: `for row in rows or []`
- L222: `if not self._mentions_any(text, ORDER_HINT_WORDS)`
- L228: `if column`

### `CursorOrderByResolver.order_by_base_columns_for_record` - L233-L237

```python
order_by_base_columns_for_record(self, record_name: str) -> list[str]
```

Child columns derived from the record's own key.

Observed calls (lexical order): `self.relationship_resolver.order_by_columns_for_record`.

### `CursorOrderByResolver._valid_order_columns` - L242-L291

```python
_valid_order_columns(self, *, record_name: str, columns: list[str]) -> list[str]
```

Keep only real, non-audit DB2 columns of this record.

Observed calls (lexical order): `list`, `set`, `NameNormalizer.normalize`, `column.upper`, `self._log`, `str`, `str(raw or '').strip`, `self.column_filter.column_exists_for_record`, `self.column_filter.is_audit_column`, `seen.add`, `kept.append`.

Control points:

- L253: `if not ENFORCE_ORDER_BY_COLUMN_VALIDATION`
- L259: `for raw in columns or []`
- L262: `if not column or column.upper() in NON_COLUMN_SENTINELS`
- L270: `if column in seen`
- L273: `if not self.column_filter.column_exists_for_record(record_name, column)`
- L284: `if self.column_filter.is_audit_column(column)`

### `CursorOrderByResolver._narrowed_order_columns` - L296-L351

```python
_narrowed_order_columns(self, *, record_name: str, columns: list[str], is_child: bool=False) -> list[str]
```

The minimal key that is still deterministic.

Observed calls (lexical order): `len`, `self._log`, `', '.join`, `self._is_identity_key_column`.

Control points:

- L313: `if not ORDER_BY_PREFER_IDENTITY_KEY or len(columns) <= 1`
- L314: `if columns`
- L322: `if is_child and (not ORDER_BY_NARROWING_APPLIES_TO_CHILD)`
- L336: `if not identity`

### `CursorOrderByResolver._expression` - L356-L367

```python
_expression(self, *, record_name: str, column: str) -> str
```

'<column>', '<column> ASC' or '<column> DESC'.

Observed calls (lexical order): `self.should_order_desc`.

Control points:

- L358: `if EMIT_ORDER_BY_DIRECTION and self.should_order_desc(record_name=record_name, column_name=column)`
- L364: `if EMIT_EXPLICIT_ASC`

### `CursorOrderByResolver.should_order_desc` - L369-L426

```python
should_order_desc(self, record_name: str, column_name: str) -> bool
```

True when a DEDICATED field states a descending sort.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.access_type_classifier.is_calc_dl`, `self.access_type_classifier.has_seq_no_field`, `self.relationship_resolver.key_column_resolver.primary_key_columns_for_record`, `len`, `self._log`, `self.access_type_classifier.is_via_accessed`, `self.mapping_repository.rows_for_record`, `getattr`, `' '.join`, `' '.join((str(getattr(row, field, '') or '') for field in DESC_HINT_FIELDS)).upper`, `str`, `self._mentions_any`.

Control points:

- L380: `if not EMIT_ORDER_BY_DIRECTION`
- L387: `if self.access_type_classifier.is_calc_dl(record)`
- L388: `if self.access_type_classifier.has_seq_no_field(record)`
- L390: `if len(primary_keys) > 1`
- L399: `if self.access_type_classifier.is_via_accessed(record)`
- L400: `if self.access_type_classifier.has_seq_no_field(record)`
- L402: `if len(primary_keys) == 1`
- L411: `for row in self.mapping_repository.rows_for_record(record) or []`
- Another 2 conditions/loops exist in this source span.

### `CursorOrderByResolver._is_identity_key_column` - L432-L445

```python
_is_identity_key_column(column_name: str) -> bool
```

True if column is a surrogate identity key (NR_ID_, NS_ID_, etc).

Observed calls (lexical order): `str`, `str(column_name or '').strip`, `str(column_name or '').strip().upper`, `normalized.startswith`.

### `CursorOrderByResolver._mentions_any` - L448-L461

```python
_mentions_any(text: str, words) -> bool
```

Whole-WORD membership test.

Observed calls (lexical order): `str`, `str(text or '').upper`, `haystack.replace`, `haystack.split`, `any`, `str(word or '').strip`, `str(word or '').strip().upper`.

Control points:

- L456: `for separator in WORD_SEPARATORS`

### `CursorOrderByResolver._log` - L463-L488

```python
_log(self, key: str, **values) -> None
```

Diagnostics must never abort the resolver that emits them.

Observed calls (lexical order): `self.MESSAGES.get`, `dict`, `arguments.update`, `Formatter`, `Formatter().parse`, `set`, `template.format`, `message.strip`, `self.messages.append`.

Control points:

- L466: `if not template`
- L479: `for name in missing`
- L487: `if message and message not in self.messages`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
