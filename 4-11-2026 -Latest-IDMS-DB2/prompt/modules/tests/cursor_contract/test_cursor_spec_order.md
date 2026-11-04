# `tests/cursor_contract/test_cursor_spec_order.py`

Source: [tests/cursor_contract/test_cursor_spec_order.py](../../../../tests/cursor_contract/test_cursor_spec_order.py) | 24 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `872bfce0b865c7494d273d93df839a37d9a29d3c9a0fc2b1b87f6e1b66b3ab13`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_spec.py](../../converter/generators/db2_infrastructure/cursor_spec.md)

## Symbol contracts and control points

### `test_cursor_order_is_read_from_the_spec_dict` - L6-L10

```python
test_cursor_order_is_read_from_the_spec_dict(names)
```

Observed calls (lexical order): `CursorSpec.read`.

### `test_missing_cursor_order_falls_back_to_list_position` - L13-L17

```python
test_missing_cursor_order_falls_back_to_list_position()
```

Observed calls (lexical order): `CursorSpec.read_all`.

### `test_a_malformed_cursor_order_never_raises` - L20-L24

```python
test_a_malformed_cursor_order_never_raises()
```

Observed calls (lexical order): `CursorSpec.read`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
