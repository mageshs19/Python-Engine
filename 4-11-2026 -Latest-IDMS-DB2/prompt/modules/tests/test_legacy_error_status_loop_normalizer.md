# `tests/test_legacy_error_status_loop_normalizer.py`

Source: [tests/test_legacy_error_status_loop_normalizer.py](../../../tests/test_legacy_error_status_loop_normalizer.py) | 30 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `d88b5bfc3fd1b51b10726198e5929ab6486a4d354f152838255985e5118df3a8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.cursor_flow.legacy_error_status_loop_normalizer import LegacyErrorStatusLoopNormalizer
```

## Local dependency notes

- [converter/composers/cursor_flow/legacy_error_status_loop_normalizer.py](../converter/composers/cursor_flow/legacy_error_status_loop_normalizer.md)

## Symbol contracts and control points

### `test_normalizes_only_proven_cursor_owned_error_status_loops` - L4-L21

```python
test_normalizes_only_proven_cursor_owned_error_status_loops()
```

Observed calls (lexical order): `LegacyErrorStatusLoopNormalizer`, `normalizer.compose`.

### `test_leaves_ambiguous_error_status_loop_unchanged` - L24-L30

```python
test_leaves_ambiguous_error_status_loop_unchanged()
```

Observed calls (lexical order): `LegacyErrorStatusLoopNormalizer`, `LegacyErrorStatusLoopNormalizer().compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
