# `tests/generated_fields/test_anchor_guards.py`

Source: [tests/generated_fields/test_anchor_guards.py](../../../../tests/generated_fields/test_anchor_guards.py) | 74 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ff0fcd599fee1eb9fbda4be8acd42f09155a94621cbd9eee558e9e85f45c2f0a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_a_record_layout_is_never_chosen` - L4-L9

```python
test_a_record_layout_is_never_chosen(program, resolve, with_record_layout)
```

Observed calls (lexical order): `program`, `resolve`.

### `test_a_childless_group_is_never_chosen` - L12-L19

```python
test_a_childless_group_is_never_chosen(program, resolve, with_childless_group)
```

Observed calls (lexical order): `program`, `resolve`, `any`.

### `test_no_working_storage_refuses_rather_than_guesses` - L22-L30

```python
test_no_working_storage_refuses_rather_than_guesses(program, resolve, without_working_storage)
```

Observed calls (lexical order): `program`, `resolve`, `any`.

### `test_cs_program_lands_in_the_preferred_work_group` - L33-L42

```python
test_cs_program_lands_in_the_preferred_work_group(program, declare, bodies, with_work_group)
```

Observed calls (lexical order): `declare`, `program`, `bodies`, `any`, `b.startswith`.

### `test_cs_program_never_lands_under_an_elementary_item` - L45-L55

```python
test_cs_program_never_lands_under_an_elementary_item(program, declare, bodies, with_childless_group)
```

Observed calls (lexical order): `declare`, `program`, `bodies`, `next`, `enumerate`, `b.startswith`, `text[position - 1].startswith`.

### `test_cs_program_is_declared_only_once` - L58-L65

```python
test_cs_program_is_declared_only_once(program, declare, bodies, with_work_group)
```

Observed calls (lexical order): `declare`, `program`, `bodies`, `len`, `any`.

### `test_cs_program_and_counters_would_share_one_group` - L68-L74

```python
test_cs_program_and_counters_would_share_one_group(program, resolve, declare, with_work_group)
```

Observed calls (lexical order): `declare`, `program`, `resolve`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
