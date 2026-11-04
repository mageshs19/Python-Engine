# `converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.py) | 103 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `1b848d94eceabf321aca9c476ca9050ca5ace6a7e6e1277e524d12d04e18c10d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Adds the columns a cursor must project but usage analysis missed.

## Module-level bindings

`__all__` (L103)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.spec_builder.spec_where_builder import SpecWhereBuilder
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_spec import SPEC_HOST_VARIABLES, SPEC_ORDER_BY_COLUMNS, SPEC_SELECT_COLUMNS, SPEC_TABLE_NAME, SPEC_WHERE_CONDITIONS
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/spec_where_builder.py](spec_where_builder.md)
- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)
- [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)
- [tests/spec_builder/conftest.py](../../../../tests/spec_builder/conftest.md)

## Symbol contracts and control points

### `SpecSelectAugmenter` - L36-L100

```python
class SpecSelectAugmenter()
```

Grows SELECT lists, then re-syncs the INTO lists.

### `SpecSelectAugmenter.__init__` - L39-L41

```python
__init__(self, host_variable_resolver, where_builder: SpecWhereBuilder) -> None
```

### `SpecSelectAugmenter.augment` - L43-L54

```python
augment(self, specs: list[dict[str, object]]) -> None
```

Observed calls (lexical order): `NameNormalizer.normalize`, `spec.get`, `str`, `str(spec.get(SPEC_TABLE_NAME, '')).strip`, `self._add_own_order_by`, `self._add_parent_join_columns`, `self._resync_host_variables`.

Control points:

- L50: `for spec in specs`

### `SpecSelectAugmenter._add_own_order_by` - L57-L61

```python
_add_own_order_by(self, spec: dict[str, object]) -> None
```

Observed calls (lexical order): `spec.get`, `str`, `str(expression).strip`, `str(expression).strip().split`, `self.add_column`.

Control points:

- L58: `for expression in spec.get(SPEC_ORDER_BY_COLUMNS, []) or []`
- L60: `if words`

### `SpecSelectAugmenter._add_parent_join_columns` - L64-L76

```python
_add_parent_join_columns(self, spec: dict[str, object], by_table: dict[str, dict[str, object]]) -> None
```

Observed calls (lexical order): `spec.get`, `self.where_builder.parent_reference`, `str`, `by_table.get`, `self.add_column`.

Control points:

- L69: `for condition in spec.get(SPEC_WHERE_CONDITIONS, []) or []`
- L71: `if not table or not column`
- L75: `if parent_spec is not None`

### `SpecSelectAugmenter._resync_host_variables` - L79-L86

```python
_resync_host_variables(self, specs: list[dict[str, object]]) -> None
```

Observed calls (lexical order): `self.host_variable_resolver.host_references_for_columns`, `spec.get`, `str`, `list`.

Control points:

- L80: `for spec in specs`

### `SpecSelectAugmenter.add_column` - L89-L100

```python
add_column(spec: dict[str, object], column: str) -> None
```

Observed calls (lexical order): `NameNormalizer.normalize`, `list`, `spec.get`, `columns.append`.

Control points:

- L91: `if not normalized`
- L96: `if normalized in existing`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
