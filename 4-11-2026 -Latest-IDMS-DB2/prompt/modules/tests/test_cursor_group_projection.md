# `tests/test_cursor_group_projection.py`

Source: [tests/test_cursor_group_projection.py](../../../tests/test_cursor_group_projection.py) | 51 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `c7293f0026abaa9ca43b4fef7324c769c0b67a0614570eaf52220c2522b79a8e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.analyzers.field_usage_models import FieldUsage, FieldUsageAnalysis
from converter.resolvers.cursor_field_usage_column_selector import CursorFieldUsageColumnSelector
```

## Local dependency notes

- [converter/analyzers/field_usage_models.py](../converter/analyzers/field_usage_models.md)
- [converter/resolvers/cursor_field_usage_column_selector.py](../converter/resolvers/cursor_field_usage_column_selector.md)

## Symbol contracts and control points

### `_Mapping` - L9-L19

```python
class _Mapping()
```

### `_Mapping.rows_for_record` - L10-L19

```python
rows_for_record(self, record_name)
```

Observed calls (lexical order): `SimpleNamespace`.

### `test_group_field_usage_expands_to_mapped_descendant_columns` - L22-L40

```python
test_group_field_usage_expands_to_mapped_descendant_columns()
```

Observed calls (lexical order): `FieldUsageAnalysis`, `FieldUsage`, `CursorFieldUsageColumnSelector`, `CursorFieldUsageColumnSelector(_Mapping()).columns_from_field_usage`, `_Mapping`, `len`, `set`.

### `test_group_expansion_stops_at_next_sibling_level` - L43-L51

```python
test_group_expansion_stops_at_next_sibling_level()
```

Observed calls (lexical order): `CursorFieldUsageColumnSelector`, `_Mapping`, `selector.columns_for_group_field`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
