# `tests/generated_output/test_initialization_scope.py`

Source: [tests/generated_output/test_initialization_scope.py](../../../../tests/generated_output/test_initialization_scope.py) | 107 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `642298b16905bf15df3917e4cfd57971e792afed42cec2603defb23ee6bec3cb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`OPEN_PERFORM` (L6), `FETCH_HEADER` (L10), `INITIALIZE_GROUP` (L14), `STARTUP_PARAGRAPH` (L15), `TIMESTAMP_PERFORM` (L16)

## Import declarations

```python
from __future__ import annotations
import re
import pytest
```

## Symbol contracts and control points

### `_open_indexes` - L19-L24

```python
_open_indexes(bodies: list[str]) -> list[int]
```

Observed calls (lexical order): `enumerate`, `OPEN_PERFORM.match`.

### `test_the_program_opens_at_least_one_cursor` - L27-L29

```python
test_the_program_opens_at_least_one_cursor(generated_bodies)
```

Observed calls (lexical order): `_open_indexes`, `pytest.skip`.

Control points:

- L28: `if not _open_indexes(generated_bodies)`

### `test_a_dclgen_group_is_initialized_somewhere` - L32-L36

```python
test_a_dclgen_group_is_initialized_somewhere(generated_bodies)
```

Observed calls (lexical order): `any`, `body.upper`, `body.upper().startswith`.

### `test_every_cursor_open_is_preceded_by_its_initialize` - L39-L50

```python
test_every_cursor_open_is_preceded_by_its_initialize(generated_bodies, previous_body)
```

Observed calls (lexical order): `_open_indexes`, `pytest.skip`, `previous_body`, `previous_body(index).upper`, `before.startswith`.

Control points:

- L43: `if not indexes`
- L45: `for index in indexes`

### `test_each_cursor_initializes_a_distinct_group` - L53-L61

```python
test_each_cursor_initializes_a_distinct_group(generated_bodies, previous_body)
```

Observed calls (lexical order): `_open_indexes`, `pytest.skip`, `previous_body`, `previous_body(index).upper`, `previous_body(index).upper().split`, `previous_body(index).upper().split()[1].rstrip`, `len`, `set`.

Control points:

- L55: `if not indexes`

### `test_no_startup_initialize_paragraph_remains` - L64-L70

```python
test_no_startup_initialize_paragraph_remains(generated_bodies)
```

Observed calls (lexical order): `body.upper`, `body.upper().rstrip`, `body.endswith`.

### `test_no_perform_of_the_startup_paragraph_remains` - L73-L77

```python
test_no_perform_of_the_startup_paragraph_remains(generated_bodies)
```

Observed calls (lexical order): `any`, `body.upper`, `body.upper().startswith`.

### `test_the_timestamp_paragraph_is_performed_at_most_once` - L80-L86

```python
test_the_timestamp_paragraph_is_performed_at_most_once(generated_bodies)
```

Observed calls (lexical order): `body.upper`, `body.upper().startswith`, `len`.

### `test_no_fetch_paragraph_clears_its_host_group` - L89-L102

```python
test_no_fetch_paragraph_clears_its_host_group(generated_bodies)
```

Observed calls (lexical order): `enumerate`, `FETCH_HEADER.match`, `pytest.skip`, `any`, `body.upper`, `body.upper().startswith`.

Control points:

- L95: `if not fetches`
- L98: `for index in fetches`

### `test_no_empty_initialize_statement` - L105-L107

```python
test_no_empty_initialize_statement(generated_bodies)
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
