# `tests/test_cursor_materialised_projection.py`

Source: [tests/test_cursor_materialised_projection.py](../../../tests/test_cursor_materialised_projection.py) | 64 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `eaf71b1b9e4f7fe76f0b0f96ad13be38b0750512d58f3b6f9245d265305aec56`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.resolvers.cursor_column_resolver import CursorColumnResolver
```

## Local dependency notes

- [converter/resolvers/cursor_column_resolver.py](../converter/resolvers/cursor_column_resolver.md)

## Symbol contracts and control points

### `_Mapping` - L6-L23

```python
class _Mapping()
```

### `_Mapping.rows_for_record` - L7-L23

```python
rows_for_record(self, record_name)
```

Observed calls (lexical order): `SimpleNamespace`.

### `_ColumnNameResolver` - L26-L30

```python
class _ColumnNameResolver()
```

### `_ColumnNameResolver.columns_for_record` - L28-L30

```python
columns_for_record(record_name)
```

### `_Unused` - L33-L34

```python
class _Unused()
```

### `test_materialised_projection_excludes_relationship_only_columns_without_source_field` - L37-L44

```python
test_materialised_projection_excludes_relationship_only_columns_without_source_field()
```

Observed calls (lexical order): `CursorColumnResolver.__new__`, `_Mapping`, `_ColumnNameResolver`, `resolver._materialised_record_columns`.

### `test_materialised_projection_falls_back_when_mapping_has_no_field_provenance` - L47-L64

```python
test_materialised_projection_falls_back_when_mapping_has_no_field_provenance()
```

Observed calls (lexical order): `CursorColumnResolver.__new__`, `SimpleNamespace`, `_ColumnNameResolver`, `resolver._materialised_record_columns`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
