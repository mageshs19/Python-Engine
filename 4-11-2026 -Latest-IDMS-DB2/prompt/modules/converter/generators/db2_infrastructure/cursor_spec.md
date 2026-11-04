# `converter/generators/db2_infrastructure/cursor_spec.py`

Source: [converter/generators/db2_infrastructure/cursor_spec.py](../../../../../converter/generators/db2_infrastructure/cursor_spec.py) | 139 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `1be0c1639aef60ec4c93004795960880ec8ee872b810480027c4f2d8f611013a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Typed, cleaned view of a cursor spec dictionary.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (10)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](../cursor_declaration/cursor_declaration_generator.md)
- [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](cursor_declare/cursor_declare_builder.md)
- [converter/generators/db2_infrastructure/cursor_flag_builder.py](cursor_flag_builder.md)
- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](infrastructure_block_builder.md)
- [tests/cursor_contract/conftest.py](../../../tests/cursor_contract/conftest.md)
- [tests/cursor_contract/test_cursor_spec_order.py](../../../tests/cursor_contract/test_cursor_spec_order.md)
- [tests/cursor_where/_fixtures.py](../../../tests/cursor_where/_fixtures.md)
- [tests/cursor_where/_support.py](../../../tests/cursor_where/_support.md)
- [tests/test_cursor_order_by_retention.py](../../../tests/test_cursor_order_by_retention.md)
- [tests/test_cursor_select_column_parity.py](../../../tests/test_cursor_select_column_parity.md)

## Symbol contracts and control points

### `CursorSpec` - L24-L139

```python
class CursorSpec()
```

One cursor, ready to render.

Declared class/data-model fields:

```python
cursor_name: str = ''
table_name: str = ''
record_name: str = ''
select_columns: list[str] = field(default_factory=list)
where_conditions: list[str] = field(default_factory=list)
order_by_columns: list[str] = field(default_factory=list)
cursor_order: int = 0
```

### `CursorSpec.is_declarable` - L36-L37

```python
is_declarable(self) -> bool
```

Observed calls (lexical order): `bool`.

### `CursorSpec.is_child` - L40-L42

```python
is_child(self) -> bool
```

A cursor with a WHERE clause is a child of another cursor.

Observed calls (lexical order): `bool`.

### `CursorSpec.not_eoc_suffix_source` - L45-L46

```python
not_eoc_suffix_source(self) -> str
```

### `CursorSpec.read` - L52-L76

```python
read(cls, spec: dict[str, object], fallback_order: int=0) -> 'CursorSpec'
```

Observed calls (lexical order): `cls`, `NameNormalizer.to_cobol`, `source.get`, `str`, `NameNormalizer.normalize`, `cls._columns`, `cls._items`, `cls._order`.

### `CursorSpec.read_all` - L79-L91

```python
read_all(cls, specs: list[dict[str, object]]) -> list['CursorSpec']
```

Read every spec, preserving order.

Observed calls (lexical order): `cls.read`, `enumerate`.

### `CursorSpec._columns` - L97-L109

```python
_columns(value: object) -> list[str]
```

Normalised column names, de-duplicated, order preserved.

Observed calls (lexical order): `set`, `list`, `NameNormalizer.normalize`, `str`, `seen.add`, `out.append`.

Control points:

- L102: `for column in list(value or [])`
- L104: `if not normalized or normalized in seen`

### `CursorSpec._items` - L112-L124

```python
_items(value: object) -> list[str]
```

Trimmed free-text clause items, de-duplicated, order preserved.

Observed calls (lexical order): `set`, `list`, `str`, `str(item or '').strip`, `seen.add`, `out.append`.

Control points:

- L117: `for item in list(value or [])`
- L119: `if not text or text in seen`

### `CursorSpec._order` - L127-L139

```python
_order(value: object, fallback: int=0) -> int
```

Cursor position as a non-negative int, never raising.

Observed calls (lexical order): `int`, `str`, `str(value).strip`, `max`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
