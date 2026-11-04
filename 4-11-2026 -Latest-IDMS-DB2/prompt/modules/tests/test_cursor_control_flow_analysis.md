# `tests/test_cursor_control_flow_analysis.py`

Source: [tests/test_cursor_control_flow_analysis.py](../../../tests/test_cursor_control_flow_analysis.py) | 249 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `1044ca9a1ee9d2781f8c535260f880b201e7f6d542ef32752e75c1ba2f10f5f8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.program_flow.cursor_control_flow_analysis import CursorControlFlowAnalyzer
```

## Local dependency notes

- [converter/analyzers/program_flow/cursor_control_flow_analysis.py](../converter/analyzers/program_flow/cursor_control_flow_analysis.md)

## Symbol contracts and control points

### `_source` - L6-L7

```python
_source(body)
```

### `test_single_cursor_indexes_declare_open_fetch_close` - L10-L21

```python
test_single_cursor_indexes_declare_open_fetch_close()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`.

### `test_two_independent_cursors_are_not_assumed_parent_child` - L24-L37

```python
test_two_independent_cursors_are_not_assumed_parent_child()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `' '.join`, `report.relationships.values`.

### `test_parent_child_candidate_requires_control_flow_evidence_not_names` - L40-L56

```python
test_parent_child_candidate_requires_control_flow_evidence_not_names()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `set`, `any`, `all`, `report.relationships.values`.

### `test_parent_child_relationship_is_inferred_only_from_successful_fetch_call_path` - L60-L86

```python
test_parent_child_relationship_is_inferred_only_from_successful_fetch_call_path()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`.

### `test_multiple_nested_cursor_levels_are_all_indexed` - L88-L105

```python
test_multiple_nested_cursor_levels_are_all_indexed()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `len`.

### `test_conditional_cursor_execution_is_flagged_for_review` - L108-L118

```python
test_conditional_cursor_execution_is_flagged_for_review()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `any`, `report.relationships.values`.

### `test_cursor_inside_loop_is_flagged_for_review` - L121-L131

```python
test_cursor_inside_loop_is_flagged_for_review()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `any`, `report.relationships.values`.

### `test_fetch_eoc_and_sql_error_logic_is_not_mistaken_for_cursor_operations` - L134-L146

```python
test_fetch_eoc_and_sql_error_logic_is_not_mistaken_for_cursor_operations()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `len`, `report.operations_for`.

### `test_open_fetch_close_sql_error_context_remains_in_source` - L149-L163

```python
test_open_fetch_close_sql_error_context_remains_in_source()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`.

### `test_restart_commit_and_checkpoint_statements_are_preserved` - L166-L182

```python
test_restart_commit_and_checkpoint_statements_are_preserved()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`.

### `test_perform_thru_and_renamed_paragraph_targets_are_resolved` - L185-L198

```python
test_perform_thru_and_renamed_paragraph_targets_are_resolved()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `next`.

### `test_program_without_cursors_is_valid_and_not_given_cursor_template` - L201-L210

```python
test_program_without_cursors_is_valid_and_not_given_cursor_template()
```

Observed calls (lexical order): `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `_source`, `any`.

### `test_ambiguous_relationship_is_flagged_not_guessed` - L213-L226

```python
test_ambiguous_relationship_is_flagged_not_guessed()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `any`, `all`, `report.relationships.values`.

### `test_child_open_in_when_other_is_not_inferred_as_parent_child` - L229-L249

```python
test_child_open_in_when_other_is_not_inferred_as_parent_child()
```

Observed calls (lexical order): `_source`, `CursorControlFlowAnalyzer`, `CursorControlFlowAnalyzer().analyze`, `report.relationships.get`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
