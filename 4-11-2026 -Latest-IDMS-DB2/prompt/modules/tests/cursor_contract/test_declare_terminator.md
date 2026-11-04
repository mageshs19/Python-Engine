# `tests/cursor_contract/test_declare_terminator.py`

Source: [tests/cursor_contract/test_declare_terminator.py](../../../../tests/cursor_contract/test_declare_terminator.py) | 56 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `842b34d15272ffc12ec773020ff885d66e78327cfbd72854e31892b81f440d26`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`BARE` (L3), `CLOSING` (L4)

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_the_default_closes_the_sentence` - L7-L9

```python
test_the_default_closes_the_sentence(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`.

### `test_the_default_preserves_the_previous_bytes` - L12-L15

```python
test_the_default_preserves_the_previous_bytes(declares, spec)
```

Observed calls (lexical order): `declares.build`, `spec`.

### `test_an_explicit_last_closes_the_sentence` - L18-L20

```python
test_an_explicit_last_closes_the_sentence(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`.

### `test_a_non_last_declaration_closes_bare` - L23-L25

```python
test_a_non_last_declaration_closes_bare(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`.

### `test_only_the_last_of_two_declarations_carries_the_period` - L28-L40

```python
test_only_the_last_of_two_declarations_carries_the_period(declares, spec, bodies)
```

Observed calls (lexical order): `spec`, `len`, `bodies`, `declares.build`, `enumerate`.

### `test_queryno_still_precedes_the_close_on_both` - L43-L47

```python
test_queryno_still_precedes_the_close_on_both(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `lines[-2].startswith`.

Control points:

- L44: `for flag in (True, False)`

### `test_a_refusal_is_unaffected_by_is_last` - L50-L56

```python
test_a_refusal_is_unaffected_by_is_last(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `any`, `body.startswith`.

Control points:

- L51: `for flag in (True, False)`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
