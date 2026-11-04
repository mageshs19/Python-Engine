# `tests/generated_fields/test_program_name_binding.py`

Source: [tests/generated_fields/test_program_name_binding.py](../../../../tests/generated_fields/test_program_name_binding.py) | 99 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `898ad6ecf678b31df03d73204c5740b359a06329329768d7126a65edbff653b6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.generators.timestamp.program_name_binder import ProgramNameBinder
```

## Local dependency notes

- [converter/generators/timestamp/program_name_binder.py](../../converter/generators/timestamp/program_name_binder.md)

## Symbol contracts and control points

### `bind` - L11-L16

```python
bind()
```

### `bind._bind` - L12-L14

```python
_bind(lines: list[str])
```

Observed calls (lexical order): `ProgramNameBinder`, `binder.bind`, `list`.

### `declared` - L20-L29

```python
declared() -> list[str]
```

### `undeclared` - L33-L42

```python
undeclared() -> list[str]
```

### `test_the_literal_is_replaced_by_the_constant` - L45-L52

```python
test_the_literal_is_replaced_by_the_constant(program, bind, bodies, declared)
```

Observed calls (lexical order): `bind`, `program`, `bodies`, `any`, `b.startswith`.

### `test_the_terminator_is_preserved` - L55-L59

```python
test_the_terminator_is_preserved(program, bind, bodies, declared)
```

Observed calls (lexical order): `bind`, `program`, `b.startswith`, `bodies`, `moves[0].endswith`.

### `test_the_rewrite_is_reported` - L62-L64

```python
test_the_rewrite_is_reported(program, bind, declared)
```

Observed calls (lexical order): `bind`, `program`, `any`.

### `test_an_undeclared_constant_refuses_the_rewrite` - L67-L74

```python
test_an_undeclared_constant_refuses_the_rewrite(program, bind, bodies, undeclared)
```

Observed calls (lexical order): `bind`, `program`, `bodies`, `any`.

### `test_binding_is_idempotent` - L77-L82

```python
test_binding_is_idempotent(program, bind, declared)
```

Observed calls (lexical order): `bind`, `program`, `any`.

### `test_a_business_literal_move_is_untouched` - L85-L99

```python
test_a_business_literal_move_is_untouched(program, bind, bodies)
```

Observed calls (lexical order): `program`, `bind`, `any`, `bodies`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
