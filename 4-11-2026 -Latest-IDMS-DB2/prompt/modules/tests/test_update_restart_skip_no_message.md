# `tests/test_update_restart_skip_no_message.py`

Source: [tests/test_update_restart_skip_no_message.py](../../../tests/test_update_restart_skip_no_message.py) | 49 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `4668af3b2a4bb32b747cf105ef4af0efbbe3080e4424703cdc77afa4e4fabfa8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`EMIT_MANUAL_REDESIGN_MESSAGE` (L44), `MANUAL_REDESIGN_MESSAGE_TEMPLATE` (L46)

## Import declarations

```python
from converter.composers.update_restart_skip_composer import UpdateRestartSkipComposer
```

## Local dependency notes

- [converter/composers/update_restart_skip_composer.py](../converter/composers/update_restart_skip_composer.md)

## Symbol contracts and control points

### `_fixed` - L6-L7

```python
_fixed(body: str) -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `test_manual_redesign_message_suppressed_by_default` - L10-L20

```python
test_manual_redesign_message_suppressed_by_default()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `UpdateRestartSkipComposer`, `composer.compose`, `any`.

### `test_message_flag_is_opt_in` - L23-L25

```python
test_message_flag_is_opt_in()
```

Observed calls (lexical order): `UpdateRestartSkipComposer`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
