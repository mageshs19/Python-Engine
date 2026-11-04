# `converter/resolvers/cursor_join_resolver.py`

Source: [converter/resolvers/cursor_join_resolver.py](../../../../converter/resolvers/cursor_join_resolver.py) | 341 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `9016963090c8749d34a1579ff58cc40d492ee1d988d1e2da766c1a44ac6845fd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds child-cursor WHERE predicates from IDMS set relationships.

## Module-level bindings

`HOST_PREFIX` (L36), `GROUP_SEPARATOR` (L37), `__all__` (L341)

## Import declarations

```python
from __future__ import annotations
from converter.resolvers.relationship_resolver import RelationshipResolver
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_declaration_rules import CHILD_JOIN_PREDICATE_TEMPLATE, DRIVING_KEY_PREDICATE_TEMPLATE, EMIT_DRIVING_KEY_PREDICATE, JOIN_MESSAGES
```

## Local dependency notes

- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/cursor_declaration_rules.py](../../rules/cursor_declaration_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/cursor_where/_fixtures.py](../../tests/cursor_where/_fixtures.md)
- [tests/cursor_where/_support.py](../../tests/cursor_where/_support.md)
- [tests/cursor_where/test_join_resolver.py](../../tests/cursor_where/test_join_resolver.md)

## Symbol contracts and control points

### `CursorJoinResolver` - L40-L338

```python
class CursorJoinResolver()
```

Resolves the WHERE clause of a child cursor.

### `CursorJoinResolver.__init__` - L43-L59

```python
__init__(self, relationship_resolver: RelationshipResolver, column_name_resolver, host_variable_resolver, table_name_resolver=None) -> None
```

Observed calls (lexical order): `getattr`.

### `CursorJoinResolver.where_conditions` - L64-L120

```python
where_conditions(self, child_record: str, driving_host_reference: str='') -> list[str]
```

Join predicates for one child record.

Observed calls (lexical order): `NameNormalizer.normalize`, `self._resolve`, `self._log`, `self._driving_key_conditions`, `getattr`, `list`, `self.diagnostics.extend`, `self._owned_columns`, `set`, `self._predicate`, `seen.add`, `conditions.append`.

Control points:

- L81: `if not record`
- L86: `if resolution is None`
- L104: `for condition in list(getattr(resolution, 'conditions', []) or [])`
- L106: `if not predicate or predicate in seen`
- L111: `if conditions`

### `CursorJoinResolver._predicate` - L125-L160

```python
_predicate(self, condition, owned: set[str]) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `getattr`, `child_column.upper`, `self._log`, `self._parent_reference`, `CHILD_JOIN_PREDICATE_TEMPLATE.format`.

Control points:

- L133: `if not child_column`
- L136: `if owned and child_column.upper() not in owned`
- L147: `if not group or not host`

### `CursorJoinResolver._driving_key_conditions` - L165-L242

```python
_driving_key_conditions(self, child_record: str, resolution, driving_host_reference: str='') -> list[str]
```

Qualify on the child's own key against a PARENT host.

Observed calls (lexical order): `NameNormalizer.normalize`, `self._table_for_record`, `self._log`, `getattr`, `self._split_reference`, `self._owned_columns`, `self._primary_key_columns`, `set`, `child_column.upper`, `self._host_reference`, `DRIVING_KEY_PREDICATE_TEMPLATE.format`, `seen.add`, `conditions.append`.

Control points:

- L177: `if not EMIT_DRIVING_KEY_PREDICATE`
- L183: `if not child_table`
- L194: `if not parent_table and (not supplied_group)`
- L205: `for column in key_columns or []`
- L207: `if not child_column`
- L210: `if owned and child_column.upper() not in owned`
- L218: `if parent_table`
- L225: `if not group or not host`
- Another 2 conditions/loops exist in this source span.

### `CursorJoinResolver._resolve` - L247-L256

```python
_resolve(self, child_record: str)
```

resolve() on some paths, resolve_for_child_record() on others.

Observed calls (lexical order): `getattr`, `callable`, `method`.

Control points:

- L249: `for name in ('resolve', 'resolve_for_child_record')`
- L251: `if callable(method)`

### `CursorJoinResolver._table_for_record` - L258-L265

```python
_table_for_record(self, record: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `resolver.table_for_record`.

Control points:

- L260: `if resolver is None`

### `CursorJoinResolver._primary_key_columns` - L267-L277

```python
_primary_key_columns(self, record: str) -> list[str]
```

Observed calls (lexical order): `getattr`, `callable`, `list`, `method`.

Control points:

- L272: `if not callable(method)`

### `CursorJoinResolver._owned_columns` - L279-L290

```python
_owned_columns(self, table: str) -> set[str]
```

Observed calls (lexical order): `set`, `self.column_name_resolver.columns_for_table`, `NameNormalizer.normalize`, `NameNormalizer.normalize(str(column)).upper`, `str`, `str(column or '').strip`.

Control points:

- L280: `if not table`

### `CursorJoinResolver._host_reference` - L292-L299

```python
_host_reference(self, table: str, column: str) -> str
```

Observed calls (lexical order): `self.host_variable_resolver.host_reference_for_column`.

### `CursorJoinResolver._parent_reference` - L304-L315

```python
_parent_reference(self, condition) -> tuple[str, str]
```

Observed calls (lexical order): `str`, `str(getattr(condition, 'parent_host_reference', '') or '').strip`, `getattr`, `self._host_reference`, `NameNormalizer.normalize`, `self._split_reference`.

Control points:

- L309: `if not reference`

### `CursorJoinResolver._split_reference` - L318-L330

```python
_split_reference(reference: str) -> tuple[str, str]
```

Split the canonical ':DCLGROUP.HOST-FIELD' form into parts.

Observed calls (lexical order): `str`, `str(reference or '').strip`, `str(reference or '').strip().lstrip`, `text.partition`, `NameNormalizer.to_cobol`, `group.strip`, `host.strip`.

Control points:

- L321: `if GROUP_SEPARATOR not in text`
- L328: `if not group or not host`

### `CursorJoinResolver._log` - L335-L338

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `JOIN_MESSAGES.get`, `self.diagnostics.append`, `template.format`.

Control points:

- L337: `if template`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
