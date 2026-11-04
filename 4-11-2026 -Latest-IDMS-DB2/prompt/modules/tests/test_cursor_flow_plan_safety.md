# `tests/test_cursor_flow_plan_safety.py`

Source: [tests/test_cursor_flow_plan_safety.py](../../../tests/test_cursor_flow_plan_safety.py) | 54 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `7eddae1db08aee0fedfcb18ecedceaec3e2d469353f9486f88ecd5fe6b72d18e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.cursor_flow_plan_discoverer import CursorFlowPlanDiscoverer
from converter.composers.cursor_flow_rewriter import CursorFlowRewriter
```

## Local dependency notes

- [converter/composers/cursor_flow_plan_discoverer.py](../converter/composers/cursor_flow_plan_discoverer.md)
- [converter/composers/cursor_flow_rewriter.py](../converter/composers/cursor_flow_rewriter.md)

## Symbol contracts and control points

### `_simple_flow` - L5-L12

```python
_simple_flow(cursor, open_no, fetch_no, close_no, business)
```

### `test_simple_cursor_plan_uses_actual_operation_numbers_and_close_location` - L15-L22

```python
test_simple_cursor_plan_uses_actual_operation_numbers_and_close_location()
```

Observed calls (lexical order): `_simple_flow`, `CursorFlowPlanDiscoverer`, `discoverer.discover`, `len`.

### `test_rewriter_does_not_leave_duplicate_original_close_call` - L25-L31

```python
test_rewriter_does_not_leave_duplicate_original_close_call()
```

Observed calls (lexical order): `_simple_flow`, `CursorFlowPlanDiscoverer`, `discoverer.discover`, `CursorFlowRewriter`, `CursorFlowRewriter().rewrite_main_flow`, `sum`, `any`.

### `test_two_sequential_independent_cursors_are_both_discovered` - L34-L39

```python
test_two_sequential_independent_cursors_are_both_discovered()
```

Observed calls (lexical order): `_simple_flow`, `CursorFlowPlanDiscoverer`, `CursorFlowPlanDiscoverer().discover`.

### `test_interleaved_cursor_operation_is_not_rewritten_by_guess` - L42-L54

```python
test_interleaved_cursor_operation_is_not_rewritten_by_guess()
```

Observed calls (lexical order): `CursorFlowPlanDiscoverer`, `discoverer.discover`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
