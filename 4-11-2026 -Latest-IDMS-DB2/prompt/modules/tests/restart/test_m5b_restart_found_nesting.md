# `tests/restart/test_m5b_restart_found_nesting.py`

Source: [tests/restart/test_m5b_restart_found_nesting.py](../../../../tests/restart/test_m5b_restart_found_nesting.py) | 95 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `6a5acc23098c956fcc55422c2c9ff5140c4ca8bd1ccaebcc04ccee8e32e1449d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The restart_found paragraph's BLOCK STRUCTURE, not just its tokens.

## Import declarations

```python
from __future__ import annotations
import pytest
from rules import restart_statement_templates as tpl
from rules import update_standard_generator_templates as legacy
```

## Local dependency notes

- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_statement_templates.py](../../rules/restart_statement_templates.md)
- [rules/update_standard_generator_templates.py](../../rules/update_standard_generator_templates.md)

## Symbol contracts and control points

### `_index` - L31-L32

```python
_index(lines: list[str], needle: str) -> int
```

Observed calls (lexical order): `enumerate`, `next`.

### `body` - L39-L40

```python
body() -> list[str]
```

Observed calls (lexical order): `list`.

### `test_the_loop_opens_before_the_reader_is_performed` - L43-L44

```python
test_the_loop_opens_before_the_reader_is_performed(body) -> None
```

Observed calls (lexical order): `_index`.

### `test_the_counter_move_is_inside_the_loop` - L47-L52

```python
test_the_counter_move_is_inside_the_loop(body) -> None
```

The defect this file exists for.

Observed calls (lexical order): `_index`.

### `test_the_loop_closes_before_the_if` - L55-L56

```python
test_the_loop_closes_before_the_if(body) -> None
```

Observed calls (lexical order): `_index`.

### `test_each_scope_is_closed_exactly_once` - L59-L62

```python
test_each_scope_is_closed_exactly_once(body) -> None
```

Observed calls (lexical order): `' '.join`, `joined.count`.

### `test_the_paragraph_ends_on_a_terminated_sentence` - L65-L67

```python
test_the_paragraph_ends_on_a_terminated_sentence(body) -> None
```

A bare scope terminator runs into the next paragraph header.

Observed calls (lexical order): `body[-1].rstrip`, `body[-1].rstrip().endswith`.

### `test_both_obligations_survive` - L70-L74

```python
test_both_obligations_survive(body) -> None
```

Block a completed run; reposition a resumed one.

Observed calls (lexical order): `' '.join`.

### `legacy_body` - L81-L82

```python
legacy_body() -> list[str]
```

Observed calls (lexical order): `str`, `str(legacy.RESTART_FOUND_TEMPLATE).splitlines`.

### `test_the_legacy_copy_nests_the_move_the_same_way` - L85-L89

```python
test_the_legacy_copy_nests_the_move_the_same_way(legacy_body) -> None
```

Observed calls (lexical order): `_index`.

### `test_the_legacy_copy_closes_each_scope_once` - L92-L95

```python
test_the_legacy_copy_closes_each_scope_once(legacy_body) -> None
```

Observed calls (lexical order): `' '.join`, `joined.count`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
