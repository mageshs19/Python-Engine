# `tests/generated_fields/test_anchor_tiers.py`

Source: [tests/generated_fields/test_anchor_tiers.py](../../../../tests/generated_fields/test_anchor_tiers.py) | 68 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `14cade628539203f1a76d3db2395f69f0df80e5cad1885658322b6fae6d827ac`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_tier_one_reuses_the_preferred_work_group` - L4-L12

```python
test_tier_one_reuses_the_preferred_work_group(program, resolve, with_work_group)
```

Observed calls (lexical order): `program`, `resolve`.

### `test_tier_two_reuses_an_existing_generated_group` - L15-L22

```python
test_tier_two_reuses_an_existing_generated_group(program, resolve, with_generated_group)
```

Observed calls (lexical order): `program`, `resolve`.

### `test_tier_two_never_picks_a_business_group` - L25-L29

```python
test_tier_two_never_picks_a_business_group(program, resolve, with_generated_group)
```

Observed calls (lexical order): `program`, `resolve`.

### `test_tier_three_creates_the_generated_group` - L32-L40

```python
test_tier_three_creates_the_generated_group(program, resolve, bodies, without_any_known_group)
```

Observed calls (lexical order): `program`, `resolve`, `bodies`.

### `test_the_created_group_carries_its_marker` - L43-L48

```python
test_the_created_group_carries_its_marker(program, resolve, bodies, without_any_known_group)
```

Observed calls (lexical order): `program`, `resolve`, `' '.join`, `' '.join(bodies(updated)).upper`, `bodies`.

### `test_a_second_resolve_reuses_the_created_group` - L51-L59

```python
test_a_second_resolve_reuses_the_created_group(program, resolve, without_any_known_group)
```

Observed calls (lexical order): `program`, `resolve`.

### `test_the_anchor_sits_after_the_last_child` - L62-L68

```python
test_the_anchor_sits_after_the_last_child(program, resolve, bodies, with_work_group)
```

Observed calls (lexical order): `program`, `resolve`, `updated[anchor.insert_index - 1].strip`, `updated[anchor.insert_index - 1].strip().upper`, `before.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
