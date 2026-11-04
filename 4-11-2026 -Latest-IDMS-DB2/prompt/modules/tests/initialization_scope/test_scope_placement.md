# `tests/initialization_scope/test_scope_placement.py`

Source: [tests/initialization_scope/test_scope_placement.py](../../../../tests/initialization_scope/test_scope_placement.py) | 129 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `199c42aefeb5307850f59fd238139a360fc2112beb45f66a7fa2ebc3edcd9b19`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `_placed_before` - L4-L8

```python
_placed_before(items: list[str], open_prefix: str) -> str
```

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`, `open_prefix.upper`, `items[position - 1].upper`.

Control points:

- L5: `for (position, body) in enumerate(items)`
- L6: `if body.upper().startswith(open_prefix.upper())`

### `test_single_cursor_is_initialized_before_its_open` - L11-L19

```python
test_single_cursor_is_initialized_before_its_open(program, run, bodies, single_cursor_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `_placed_before`, `_placed_before(items, 'PERFORM 710-OPEN-AAAC1').startswith`.

### `test_parent_and_child_are_each_initialized` - L22-L33

```python
test_parent_and_child_are_each_initialized(program, run, bodies, parent_child_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `_placed_before`, `_placed_before(items, 'PERFORM 710-OPEN-AAAC1').startswith`, `_placed_before(items, 'PERFORM 810-OPEN-BBBC1').startswith`.

### `test_the_child_initialize_sits_inside_the_business_paragraph` - L36-L46

```python
test_the_child_initialize_sits_inside_the_business_paragraph(program, run, bodies, index_of, parent_child_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `index_of`.

### `test_the_parent_initialize_sits_in_the_mainline` - L49-L59

```python
test_the_parent_initialize_sits_in_the_mainline(program, run, bodies, index_of, parent_child_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `index_of`.

### `test_three_nesting_levels_are_all_scoped` - L62-L73

```python
test_three_nesting_levels_are_all_scoped(program, run, bodies, three_level_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `_placed_before`, `_placed_before(items, open_prefix).startswith`.

Control points:

- L68: `for (open_prefix, group) in (('PERFORM 710-OPEN-AAAC1', 'INITIALIZE DCLAAATV'), ('PERFORM 810-OPEN-BBBC1', 'INITIALIZE DCLBBBTV'), ('PERFORM 910-OPEN-CCCC1', 'INITIALIZE DCLCCCTV'))`

### `test_each_group_is_initialized_exactly_once` - L76-L84

```python
test_each_group_is_initialized_exactly_once(program, run, bodies, count_of, three_level_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `count_of`.

### `test_the_legacy_startup_paragraph_is_removed` - L87-L94

```python
test_the_legacy_startup_paragraph_is_removed(program, run, bodies, count_of, legacy_startup_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `count_of`.

### `test_salvaged_statements_are_not_duplicated` - L97-L104

```python
test_salvaged_statements_are_not_duplicated(program, run, bodies, count_of, legacy_startup_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `count_of`.

### `test_legacy_program_is_rescoped_not_just_stripped` - L107-L118

```python
test_legacy_program_is_rescoped_not_just_stripped(program, run, bodies, legacy_startup_lines)
```

Observed calls (lexical order): `program`, `run`, `bodies`, `_placed_before`, `_placed_before(items, 'PERFORM 710-OPEN-AAAC1').startswith`, `_placed_before(items, 'PERFORM 810-OPEN-BBBC1').startswith`.

### `test_cursor_names_are_never_assumed` - L121-L129

```python
test_cursor_names_are_never_assumed(program, run, bodies, three_level_lines)
```

Observed calls (lexical order): `program`, `run`, `result.upper`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
