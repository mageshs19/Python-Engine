# `tests/initialization_scope/test_refusals_and_idempotency.py`

Source: [tests/initialization_scope/test_refusals_and_idempotency.py](../../../../tests/initialization_scope/test_refusals_and_idempotency.py) | 101 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `53f2ec283510291492682a0f372b7864c8bfddf343d9b796375575632955c8f1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_a_program_with_no_dclgen_group_is_untouched` - L4-L15

```python
test_a_program_with_no_dclgen_group_is_untouched(program, run)
```

Observed calls (lexical order): `program`, `run`.

### `test_a_program_with_no_procedure_division_is_untouched` - L18-L28

```python
test_a_program_with_no_procedure_division_is_untouched(program, run)
```

Observed calls (lexical order): `program`, `run`.

### `test_a_program_with_no_cursor_open_and_no_dclgen_write_is_untouched` - L31-L52

```python
test_a_program_with_no_cursor_open_and_no_dclgen_write_is_untouched(program, run)
```

Was: "no cursor means nothing to do" - which IS the defect.

Observed calls (lexical order): `program`, `run`.

### `test_an_unresolvable_group_rolls_the_pass_back` - L54-L67

```python
test_an_unresolvable_group_rolls_the_pass_back(program, run)
```

Observed calls (lexical order): `program`, `run`, `any`, `message.lower`.

### `test_the_pass_is_idempotent` - L70-L75

```python
test_the_pass_is_idempotent(program, run, parent_child_lines)
```

Observed calls (lexical order): `program`, `run`.

### `test_a_second_run_adds_no_duplicate_initialize` - L78-L86

```python
test_a_second_run_adds_no_duplicate_initialize(program, run, bodies, count_of, parent_child_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `count_of`.

### `test_every_run_reports_something` - L89-L91

```python
test_every_run_reports_something(program, run, single_cursor_lines)
```

Observed calls (lexical order): `program`, `run`.

### `test_empty_input_is_safe` - L94-L95

```python
test_empty_input_is_safe(run)
```

Observed calls (lexical order): `run`.

### `test_whitespace_input_is_safe` - L98-L101

```python
test_whitespace_input_is_safe(run)
```

Observed calls (lexical order): `run`, `result.strip`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
