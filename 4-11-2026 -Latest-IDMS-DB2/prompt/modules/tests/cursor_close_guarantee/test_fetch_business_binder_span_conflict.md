# `tests/cursor_close_guarantee/test_fetch_business_binder_span_conflict.py`

Source: [tests/cursor_close_guarantee/test_fetch_business_binder_span_conflict.py](../../../../tests/cursor_close_guarantee/test_fetch_business_binder_span_conflict.py) | 399 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `490c1038e932031b354123d8f7e78e18dd5b5b46f82d3825eca8b7f824ae8c7a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> FetchBusinessBinder - SPAN-loop double-drive regression.

## Module-level bindings

`_DRIVEN_AND_FETCHES` (L53), `_DRIVEN_BUT_NEVER_FETCHES` (L67)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.composers.cursor_close_guarantee.fetch_business_binder import FetchBusinessBinder
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/fetch_business_binder.py](../../converter/composers/cursor_close_guarantee/fetch_business_binder.md)

## Symbol contracts and control points

### `binder` - L81-L82

```python
binder() -> FetchBusinessBinder
```

Observed calls (lexical order): `FetchBusinessBinder`.

### `span_conflict_lines` - L86-L145

```python
span_conflict_lines() -> list[str]
```

VMDZ7200-shaped SPAN idiom: BEHANDELING already drives itself.

### `inline_control_lines` - L149-L193

```python
inline_control_lines() -> list[str]
```

Classic INLINE idiom: the external loop drives the FETCH paragraph itself, with no SPAN loop anywhere. This is the exact shape FetchBusinessBinder was built to fix, and must keep working.

### `test_detects_span_loop_on_one_physical_line` - L200-L206

```python
test_detects_span_loop_on_one_physical_line(binder)
```

Observed calls (lexical order): `binder.already_externally_driven`.

### `test_detects_span_loop_split_across_continuation_line` - L209-L214

```python
test_detects_span_loop_split_across_continuation_line(binder, span_conflict_lines)
```

Observed calls (lexical order): `binder.already_externally_driven`.

### `test_does_not_match_a_different_business_paragraph` - L217-L222

```python
test_does_not_match_a_different_business_paragraph(binder)
```

Observed calls (lexical order): `binder.already_externally_driven`.

### `test_does_not_match_a_different_cursors_eoc_condition` - L225-L230

```python
test_does_not_match_a_different_cursors_eoc_condition(binder)
```

Observed calls (lexical order): `binder.already_externally_driven`.

### `test_recognises_a_legacy_eoc_condition` - L233-L238

```python
test_recognises_a_legacy_eoc_condition(binder)
```

Observed calls (lexical order): `binder.already_externally_driven`.

### `test_no_span_perform_anywhere_returns_false` - L241-L244

```python
test_no_span_perform_anywhere_returns_false(binder, inline_control_lines)
```

Observed calls (lexical order): `binder.already_externally_driven`.

### `test_bind_refuses_when_business_paragraph_is_already_driven` - L251-L269

```python
test_bind_refuses_when_business_paragraph_is_already_driven(binder, span_conflict_lines)
```

Observed calls (lexical order): `binder.bind`, `binder.span_of`, `binder._body`.

### `test_bind_logs_the_refusal_reason` - L271-L283

```python
test_bind_logs_the_refusal_reason(binder, span_conflict_lines)
```

Observed calls (lexical order): `binder.bind`, `any`.

### `test_bind_never_injects_a_second_fetch_call_path` - L286-L301

```python
test_bind_never_injects_a_second_fetch_call_path(binder, span_conflict_lines)
```

Observed calls (lexical order): `binder.bind`, `binder.span_of`, `' '.join`, `' '.join((binder._body(line) for line in output[fetch_start:fetch_end + 1])).upper`, `binder._body`.

### `test_bind_still_binds_when_no_span_loop_exists` - L308-L327

```python
test_bind_still_binds_when_no_span_loop_exists(binder, inline_control_lines)
```

Observed calls (lexical order): `binder.bind`, `binder.span_of`, `' '.join`, `' '.join((binder._body(line) for line in output[fetch_start:fetch_end + 1])).upper`, `binder._body`, `any`.

### `test_bind_is_idempotent_on_the_inline_case` - L330-L348

```python
test_bind_is_idempotent_on_the_inline_case(binder, inline_control_lines)
```

Observed calls (lexical order): `binder.bind`, `any`.

### `test_bind_is_idempotent_on_the_span_conflict_case` - L351-L373

```python
test_bind_is_idempotent_on_the_span_conflict_case(binder, span_conflict_lines)
```

Observed calls (lexical order): `binder.bind`, `any`.

### `test_refuses_when_business_is_driven_and_refetches` - L374-L381

```python
test_refuses_when_business_is_driven_and_refetches()
```

The VMDZ7200 shape. Binding here creates a mutual PERFORM.

Observed calls (lexical order): `FetchBusinessBinder`, `FetchBusinessBinder().already_externally_driven`.

### `test_does_not_refuse_when_nothing_refetches` - L384-L395

```python
test_does_not_refuse_when_nothing_refetches()
```

An external driver with no tail fetch still needs the bind.

Observed calls (lexical order): `FetchBusinessBinder`, `FetchBusinessBinder().already_externally_driven`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
