# `tests/output_write/test_multiline_guard.py`

Source: [tests/output_write/test_multiline_guard.py](../../../../tests/output_write/test_multiline_guard.py) | 93 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `d69d19c4bdb663f5ef15974285b80aa0c62ef983689c63efec7b7cd8feb51de2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_a_single_line_guard_still_extracts` - L4-L11

```python
test_a_single_line_guard_still_extracts(program, compose, bodies, index_of, single_line_guard)
```

Observed calls (lexical order): `compose`, `program`, `bodies`, `index_of`.

### `test_a_four_line_guard_now_extracts` - L14-L21

```python
test_a_four_line_guard_now_extracts(program, compose, bodies, index_of, four_line_guard)
```

Observed calls (lexical order): `compose`, `program`, `bodies`, `index_of`.

### `test_the_whole_condition_stays_at_the_call_site` - L24-L42

```python
test_the_whole_condition_stays_at_the_call_site(program, compose, bodies, index_of, four_line_guard)
```

Observed calls (lexical order): `compose`, `program`, `bodies`, `index_of`.

Control points:

- L33: `for fragment in ('IF (HELP-DA-A', "HELP-DA-A NOT = '00000000') OR", '(HELP-DA-B', "HELP-DA-A = '00000000')")`

### `test_the_extracted_body_starts_after_the_condition` - L45-L52

```python
test_the_extracted_body_starts_after_the_condition(program, compose, bodies, index_of, four_line_guard)
```

Observed calls (lexical order): `compose`, `program`, `bodies`, `index_of`, `text[paragraph + 1].upper`, `text[paragraph + 1].upper().startswith`.

### `test_no_dangling_boolean_operator_survives` - L55-L62

```python
test_no_dangling_boolean_operator_survives(program, compose, bodies, four_line_guard)
```

Observed calls (lexical order): `compose`, `program`, `bodies`, `body.upper`, `body.upper().startswith`.

Control points:

- L60: `for body in bodies(out)`

### `test_the_counter_increment_lands_at_the_call_site` - L65-L75

```python
test_the_counter_increment_lands_at_the_call_site(program, compose, bodies, index_of, four_line_guard)
```

Observed calls (lexical order): `compose`, `program`, `bodies`, `index_of`.

### `test_the_counter_is_reported` - L78-L80

```python
test_the_counter_is_reported(program, compose, four_line_guard)
```

Observed calls (lexical order): `compose`, `program`, `any`.

### `test_two_writes_are_refused` - L83-L87

```python
test_two_writes_are_refused(program, compose, bodies, index_of, two_writes)
```

Observed calls (lexical order): `compose`, `program`, `bodies`, `index_of`, `any`.

### `test_extraction_is_idempotent` - L90-L93

```python
test_extraction_is_idempotent(program, compose, four_line_guard)
```

Observed calls (lexical order): `compose`, `program`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
