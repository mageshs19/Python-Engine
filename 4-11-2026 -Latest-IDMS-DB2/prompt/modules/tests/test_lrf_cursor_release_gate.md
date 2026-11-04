# `tests/test_lrf_cursor_release_gate.py`

Source: [tests/test_lrf_cursor_release_gate.py](../../../tests/test_lrf_cursor_release_gate.py) | 50 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e19ac8e9881e016465c59a843d316926a1ffafe81d57feeacf91184a1a93c243`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L6), `STALE` (L7)

## Import declarations

```python
from pathlib import Path
from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
```

## Local dependency notes

- [converter/composers/bounded_lrf_singleton_rewriter.py](../converter/composers/bounded_lrf_singleton_rewriter.md)
- [converter/validators/generated_cobol_release_validator.py](../converter/validators/generated_cobol_release_validator.md)

## Symbol contracts and control points

### `test_release_gate_rejects_stale_bounded_lrf_cursor_artifact` - L10-L13

```python
test_release_gate_rejects_stale_bounded_lrf_cursor_artifact()
```

Observed calls (lexical order): `STALE.read_text`, `validate_generated_cobol`, `any`.

### `test_singleton_rewrite_removes_cursor_and_matches_manual_projection` - L16-L40

```python
test_singleton_rewrite_removes_cursor_and_matches_manual_projection()
```

Observed calls (lexical order): `STALE.read_text`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`, `map`, `max`, `result.text.splitlines`, `validate_generated_cobol`, `any`.

Control points:

- L31: `for column in ('NR_IDGOOD_479EVEF', 'NR_CI1POS_479EVEF', 'NR_CI26POS_479EVEF', 'DA_CREVTPD_479EVEF')`

### `test_rewriter_refuses_stale_cursor_when_downstream_child_fields_were_not_fetched` - L43-L50

```python
test_rewriter_refuses_stale_cursor_when_downstream_child_fields_were_not_fetched()
```

Observed calls (lexical order): `stale_projection.read_text`, `BoundedLrfSingletonRewriter`, `BoundedLrfSingletonRewriter().rewrite`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
