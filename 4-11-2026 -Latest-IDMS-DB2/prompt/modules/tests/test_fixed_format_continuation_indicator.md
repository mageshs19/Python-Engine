# `tests/test_fixed_format_continuation_indicator.py`

Source: [tests/test_fixed_format_continuation_indicator.py](../../../tests/test_fixed_format_continuation_indicator.py) | 29 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a5e67a7f33b49d562a97777a08341dee56c83c8963fd2f7912e05947d2adbf56`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../converter/services/fixed_format_line_service.md)

## Symbol contracts and control points

### `test_emit_uses_blank_indicator_for_word_boundary_wraps` - L4-L10

```python
test_emit_uses_blank_indicator_for_word_boundary_wraps()
```

Observed calls (lexical order): `FixedFormatLineService`, `service.emit`, `len`.

### `test_replace_body_wrapped_uses_blank_indicator_for_word_boundary_wraps` - L13-L22

```python
test_replace_body_wrapped_uses_blank_indicator_for_word_boundary_wraps()
```

Observed calls (lexical order): `FixedFormatLineService`, `service.build`, `service.replace_body_wrapped`, `len`.

### `test_wrapped_comments_remain_comments_not_executable_continuations` - L25-L29

```python
test_wrapped_comments_remain_comments_not_executable_continuations()
```

Observed calls (lexical order): `FixedFormatLineService`, `service.emit`, `len`, `all`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
