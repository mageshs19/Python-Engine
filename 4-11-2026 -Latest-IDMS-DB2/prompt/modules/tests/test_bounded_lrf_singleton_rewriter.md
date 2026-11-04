# `tests/test_bounded_lrf_singleton_rewriter.py`

Source: [tests/test_bounded_lrf_singleton_rewriter.py](../../../tests/test_bounded_lrf_singleton_rewriter.py) | 310 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `2afced81c218bd97ed37206553fe1147b21a98b4ed242c8a1b47fb9cfe5b8e4a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L7), `GENERATED` (L8)

## Import declarations

```python
from pathlib import Path
from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter
```

## Local dependency notes

- [converter/composers/bounded_lrf_singleton_rewriter.py](../converter/composers/bounded_lrf_singleton_rewriter.md)

## Symbol contracts and control points

### `test_bounded_inline_lrf_cursor_becomes_singleton_select` - L11-L30

```python
test_bounded_inline_lrf_cursor_becomes_singleton_select()
```

Observed calls (lexical order): `GENERATED.read_text`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`, `map`, `max`, `result.text.splitlines`.

### `test_rewriter_fails_closed_without_expanded_lrf_marker` - L33-L37

```python
test_rewriter_fails_closed_without_expanded_lrf_marker()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_rewriter_can_process_safe_cursor_when_unrelated_cursor_exists` - L40-L55

```python
test_rewriter_can_process_safe_cursor_when_unrelated_cursor_exists()
```

Observed calls (lexical order): `GENERATED.read_text`, `source.splitlines`, `enumerate`, `next`, `len`, `range`, `line.replace`, `'\n'.join`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_rewriter_fails_closed_on_select_fetch_projection_mismatch` - L58-L70

```python
test_rewriter_fails_closed_on_select_fetch_projection_mismatch()
```

Observed calls (lexical order): `GENERATED.read_text`, `source.splitlines`, `enumerate`, `line[7:72].strip`, `next`, `len`, `range`, `'\n'.join`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_multiline_equality_predicate_is_joined_before_classification` - L73-L87

```python
test_multiline_equality_predicate_is_joined_before_classification()
```

Observed calls (lexical order): `GENERATED.read_text`, `source.splitlines`, `enumerate`, `next`, `original_line[7:72].replace`, `lines.insert`, `'\n'.join`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_rewriter_refuses_to_remove_loop_that_contains_business_work` - L90-L99

```python
test_rewriter_refuses_to_remove_loop_that_contains_business_work()
```

Observed calls (lexical order): `GENERATED.read_text`, `source.splitlines`, `enumerate`, `next`, `lines.insert`, `'\n'.join`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_rewriter_refuses_nested_inline_perform_even_when_end_perform_is_same_line` - L102-L113

```python
test_rewriter_refuses_nested_inline_perform_even_when_end_perform_is_same_line()
```

Observed calls (lexical order): `GENERATED.read_text`, `source.splitlines`, `enumerate`, `next`, `lines.insert`, `'\n'.join`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_rewriter_refuses_nested_cursor_eoc_reference_after_inner_end_if` - L116-L135

```python
test_rewriter_refuses_nested_cursor_eoc_reference_after_inner_end_if()
```

Observed calls (lexical order): `GENERATED.read_text`, `source.splitlines`, `enumerate`, `next`, `len`, `range`, `lines.insert`, `'\n'.join`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_matching_eoc_branch_ignores_end_if_text_inside_literal` - L138-L148

```python
test_matching_eoc_branch_ignores_end_if_text_inside_literal()
```

Observed calls (lexical order): `GENERATED.read_text`, `source.splitlines`, `enumerate`, `next`, `lines.insert`, `'\n'.join`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

### `test_find_end_exec_supports_long_sql_declarations_beyond_80_lines` - L151-L153

```python
test_find_end_exec_supports_long_sql_declarations_beyond_80_lines()
```

Observed calls (lexical order): `range`, `BoundedLrfSingletonRewriter._find_end_exec`, `len`.

### `test_find_end_exec_fails_closed_at_new_sql_block_before_terminator` - L156-L164

```python
test_find_end_exec_fails_closed_at_new_sql_block_before_terminator()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_find_end_exec_fails_closed_at_numeric_paragraph_before_terminator` - L167-L175

```python
test_find_end_exec_fails_closed_at_numeric_paragraph_before_terminator()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_find_end_exec_fails_closed_at_named_area_a_paragraph_before_terminator` - L180-L193

```python
test_find_end_exec_fails_closed_at_named_area_a_paragraph_before_terminator()
```

Observed calls (lexical order): `enumerate`, `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_find_end_exec_does_not_treat_indented_sql_clause_as_paragraph` - L196-L208

```python
test_find_end_exec_does_not_treat_indented_sql_clause_as_paragraph()
```

Observed calls (lexical order): `enumerate`, `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_update_where_projection_supports_sql_statement_beyond_100_lines` - L211-L232

```python
test_update_where_projection_supports_sql_statement_beyond_100_lines()
```

Observed calls (lexical order): `bodies.extend`, `range`, `bodies.append`, `enumerate`, `BoundedLrfSingletonRewriter._update_where_projection`.

### `test_update_where_projection_ignores_end_exec_in_fixed_format_comment` - L235-L258

```python
test_update_where_projection_ignores_end_exec_in_fixed_format_comment()
```

Observed calls (lexical order): `enumerate`, `body.startswith`, `source_lines.append`, `BoundedLrfSingletonRewriter._update_where_projection`.

Control points:

- L244: `for (index, body) in enumerate(bodies, start=1)`

### `test_find_end_exec_ignores_terminator_text_in_sql_literal` - L261-L268

```python
test_find_end_exec_ignores_terminator_text_in_sql_literal()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_find_end_exec_ignores_terminator_text_in_sql_line_comment` - L271-L278

```python
test_find_end_exec_ignores_terminator_text_in_sql_line_comment()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_find_end_exec_ignores_terminator_text_in_multiline_sql_block_comment` - L281-L290

```python
test_find_end_exec_ignores_terminator_text_in_multiline_sql_block_comment()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_find_end_exec_ignores_terminator_text_after_cobol_inline_comment_marker` - L293-L300

```python
test_find_end_exec_ignores_terminator_text_after_cobol_inline_comment_marker()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._find_end_exec`.

### `test_find_end_exec_keeps_quote_state_across_physical_lines` - L303-L310

```python
test_find_end_exec_keeps_quote_state_across_physical_lines()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._find_end_exec`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
