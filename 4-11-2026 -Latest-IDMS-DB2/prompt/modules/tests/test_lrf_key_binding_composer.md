# `tests/test_lrf_key_binding_composer.py`

Source: [tests/test_lrf_key_binding_composer.py](../../../tests/test_lrf_key_binding_composer.py) | 45 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b012ec516c461b0d36ae764a98016955eed87e2e76202504ab61fef3467d2c7a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.lrf_key_binding_composer import LrfKeyBindingComposer
```

## Local dependency notes

- [converter/composers/lrf_key_binding_composer.py](../converter/composers/lrf_key_binding_composer.md)

## Symbol contracts and control points

### `test_key_moves_are_inserted_after_initialize_and_before_open` - L4-L14

```python
test_key_moves_are_inserted_after_initialize_and_before_open()
```

Observed calls (lexical order): `LrfKeyBindingComposer`, `composer.compose`, `result.index`, `' '.join`.

### `test_parent_status_block_is_removed_and_post_close_uses_eoc_flag` - L17-L32

```python
test_parent_status_block_is_removed_and_post_close_uses_eoc_flag()
```

Observed calls (lexical order): `LrfKeyBindingComposer`, `composer.compose`.

### `test_loop_uses_cursor_eoc_flag_when_fetch_in_same_perform_block` - L35-L45

```python
test_loop_uses_cursor_eoc_flag_when_fetch_in_same_perform_block()
```

Observed calls (lexical order): `LrfKeyBindingComposer`, `composer.compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
