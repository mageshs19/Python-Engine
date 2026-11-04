# `tests/test_procedure_control_flow_graph.py`

Source: [tests/test_procedure_control_flow_graph.py](../../../tests/test_procedure_control_flow_graph.py) | 167 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `2b5ed102f8306f0800211cf6f1243dca44c572959189d0fde0037043f81fccf9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.program_flow.procedure_control_flow_graph import ProcedureControlFlowGraphBuilder
```

## Local dependency notes

- [converter/analyzers/program_flow/procedure_control_flow_graph.py](../converter/analyzers/program_flow/procedure_control_flow_graph.md)

## Symbol contracts and control points

### `test_graph_resolves_named_perform_and_physical_thru_range` - L6-L23

```python
test_graph_resolves_named_perform_and_physical_thru_range()
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `next`.

### `test_graph_resolves_section_target_and_multiline_thru` - L26-L43

```python
test_graph_resolves_section_target_and_multiline_thru()
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `next`.

### `test_graph_flags_ambiguous_duplicate_target_and_reversed_thru` - L46-L61

```python
test_graph_flags_ambiguous_duplicate_target_and_reversed_thru()
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `any`.

### `test_graph_does_not_mistake_inline_perform_until_for_paragraph_call` - L64-L75

```python
test_graph_does_not_mistake_inline_perform_until_for_paragraph_call()
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `len`.

### `test_graph_ignores_table_perform_times_as_non_paragraph_call` - L78-L88

```python
test_graph_ignores_table_perform_times_as_non_paragraph_call()
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`.

### `test_section_target_covers_all_paragraphs_until_next_section` - L91-L105

```python
test_section_target_covers_all_paragraphs_until_next_section()
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `next`.

### `test_section_node_span_ends_at_next_section_not_first_paragraph` - L108-L122

```python
test_section_node_span_ends_at_next_section_not_first_paragraph()
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `next`.

### `test_graph_expands_plain_procedure_copybook_and_resolves_target` - L125-L153

```python
test_graph_expands_plain_procedure_copybook_and_resolves_target(tmp_path)
```

Observed calls (lexical order): `program_dir.mkdir`, `copybook_dir.mkdir`, `(copybook_dir / 'PROCWORK.cpy').write_text`, `(copybook_dir / 'PROCNEST.cpy').write_text`, `source.write_text`, `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `any`, `all`.

### `test_graph_reports_missing_procedure_copybook_without_guessing` - L156-L167

```python
test_graph_reports_missing_procedure_copybook_without_guessing(tmp_path)
```

Observed calls (lexical order): `source.write_text`, `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
