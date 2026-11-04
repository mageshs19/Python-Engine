# `tests/test_no_pass_loses_characters.py`

Source: [tests/test_no_pass_loses_characters.py](../../../tests/test_no_pass_loses_characters.py) | 253 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `9b144f8cac715a151bdb4712340bd04791e52b057a00e667fcf4f9747551175e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> No pass may lose characters from a PROCEDURE DIVISION statement.

## Module-level bindings

`QUOTE` (L30), `ZERO8` (L31), `SOURCE` (L41), `CANDIDATES` (L56)

## Import declarations

```python
import importlib
import pytest
```

## Symbol contracts and control points

### `fixed` - L34-L36

```python
fixed(seq: str, body: str, right: str) -> str
```

Observed calls (lexical order): `len`, `body.ljust`.

### `_tokens` - L153-L161

```python
_tokens(text: str) -> str
```

Every non-blank character of every body, order preserved.

Observed calls (lexical order): `text.splitlines`, `len`, `''.join`, `body.split`, `out.append`.

Control points:

- L157: `for line in text.splitlines()`

### `_entry_point` - L164-L169

```python
_entry_point(instance, names)
```

Observed calls (lexical order): `getattr`, `callable`.

Control points:

- L165: `for name in names`
- L167: `if callable(method)`

### `test_pass_preserves_every_character` - L177-L211

```python
test_pass_preserves_every_character(module_name, class_name, entry_names)
```

The failing parametrisation names the pass that eats characters.

Observed calls (lexical order): `importlib.import_module`, `pytest.skip`, `getattr`, `cls`, `_entry_point`, `dir`, `m.startswith`, `entry`, `isinstance`, `_tokens`, `len`.

Control points:

- L185: `if cls is None`
- L194: `if entry is None`

### `test_pass_never_merges_physical_lines` - L219-L253

```python
test_pass_never_merges_physical_lines(module_name, class_name, entry_names)
```

A four-line condition must not come back as two.

Observed calls (lexical order): `importlib.import_module`, `pytest.skip`, `getattr`, `cls`, `_entry_point`, `entry`, `SOURCE.splitlines`, `len`, `line.strip`, `str`, `str(result).splitlines`.

Control points:

- L231: `if cls is None`
- L240: `if entry is None`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
