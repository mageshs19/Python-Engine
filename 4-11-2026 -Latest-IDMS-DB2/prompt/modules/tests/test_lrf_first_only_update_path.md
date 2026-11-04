# `tests/test_lrf_first_only_update_path.py`

Source: [tests/test_lrf_first_only_update_path.py](../../../tests/test_lrf_first_only_update_path.py) | 293 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `20dfa32c323eee4793d71f8e0d643484e4af1304992796475a863198e13ae4c6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter
from converter.resolvers.lrf_cursor_where_resolver import LrfCursorWhereResolver
```

## Local dependency notes

- [converter/composers/bounded_lrf_singleton_rewriter.py](../converter/composers/bounded_lrf_singleton_rewriter.md)
- [converter/resolvers/lrf_cursor_where_resolver.py](../converter/resolvers/lrf_cursor_where_resolver.md)

## Symbol contracts and control points

### `fixed` - L7-L8

```python
fixed(body, indicator=' ')
```

### `test_wrapped_lrf_marker_preserves_path_filters_and_maps_them_to_db2_columns` - L11-L34

```python
test_wrapped_lrf_marker_preserves_path_filters_and_maps_them_to_db2_columns()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `SimpleNamespace`, `LrfCursorWhereResolver`, `Mapping`, `resolver.extract_lrf_cursors_from_cobol`, `resolver.extra_filter_conditions_for_lrf_cursor`.

### `test_wrapped_lrf_marker_preserves_path_filters_and_maps_them_to_db2_columns.Mapping` - L23-L26

```python
class Mapping()
```

### `test_wrapped_lrf_marker_preserves_path_filters_and_maps_them_to_db2_columns.Mapping.rows_for_record` - L24-L26

```python
rows_for_record(self, record)
```

### `test_source_proven_first_only_cursor_is_rewritten_to_singleton_select` - L37-L96

```python
test_source_proven_first_only_cursor_is_rewritten_to_singleton_select()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `output.splitlines`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_lrf_extra_filter_resolution_fails_closed_when_mapping_is_ambiguous` - L101-L120

```python
test_lrf_extra_filter_resolution_fails_closed_when_mapping_is_ambiguous()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `SimpleNamespace`, `LrfCursorWhereResolver`, `Mapping`, `resolver.extract_lrf_cursors_from_cobol`, `resolver.extra_filter_conditions_for_lrf_cursor`, `any`.

### `test_lrf_extra_filter_resolution_fails_closed_when_mapping_is_ambiguous.Mapping` - L113-L115

```python
class Mapping()
```

### `test_lrf_extra_filter_resolution_fails_closed_when_mapping_is_ambiguous.Mapping.rows_for_record` - L114-L115

```python
rows_for_record(self, record)
```

### `test_ordinary_program_without_lrf_source_is_unchanged` - L123-L127

```python
test_ordinary_program_without_lrf_source_is_unchanged()
```

Observed calls (lexical order): `fixed`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_legacy_add_to_cursor_where_directive_becomes_mapped_lrf_filter` - L131-L156

```python
test_legacy_add_to_cursor_where_directive_becomes_mapped_lrf_filter()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `SimpleNamespace`, `LrfCursorWhereResolver`, `Mapping`, `resolver.extract_lrf_cursors_from_cobol`, `resolver.extra_filter_conditions_for_lrf_cursor`.

### `test_legacy_add_to_cursor_where_directive_becomes_mapped_lrf_filter.Mapping` - L146-L149

```python
class Mapping()
```

### `test_legacy_add_to_cursor_where_directive_becomes_mapped_lrf_filter.Mapping.rows_for_record` - L147-L149

```python
rows_for_record(self, record)
```

### `test_marker_first_fallback_does_not_rewrite_when_matching_next_exists` - L159-L188

```python
test_marker_first_fallback_does_not_rewrite_when_matching_next_exists()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_first_only_rewrite_refuses_when_legacy_cursor_where_filter_is_missing` - L191-L220

```python
test_first_only_rewrite_refuses_when_legacy_cursor_where_filter_is_missing()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_first_only_update_selects_only_update_key_not_set_payload` - L223-L268

```python
test_first_only_update_selects_only_update_key_not_set_payload()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`, `result.text.index`.

### `test_lrf_filter_mapping_ignores_cobol_level_prefix_in_mapping_sheet` - L271-L293

```python
test_lrf_filter_mapping_ignores_cobol_level_prefix_in_mapping_sheet()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `SimpleNamespace`, `LrfCursorWhereResolver`, `Mapping`, `resolver.extract_lrf_cursors_from_cobol`, `resolver.extra_filter_conditions_for_lrf_cursor`.

### `test_lrf_filter_mapping_ignores_cobol_level_prefix_in_mapping_sheet.Mapping` - L283-L286

```python
class Mapping()
```

### `test_lrf_filter_mapping_ignores_cobol_level_prefix_in_mapping_sheet.Mapping.rows_for_record` - L284-L286

```python
rows_for_record(self, record)
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
