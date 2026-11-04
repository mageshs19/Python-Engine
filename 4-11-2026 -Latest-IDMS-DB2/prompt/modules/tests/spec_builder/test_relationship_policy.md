# `tests/spec_builder/test_relationship_policy.py`

Source: [tests/spec_builder/test_relationship_policy.py](../../../../tests/spec_builder/test_relationship_policy.py) | 80 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a73ea5200c0210a685001d3d6ba97839b8c19f795a52eede7928bd94ff33ffdf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Tests for safe cursor relationship predicate generation.

## Import declarations

```python
from __future__ import annotations
from types import SimpleNamespace
```

## Symbol contracts and control points

### `test_parent_not_navigated_returns_no_predicates_and_reports_reason` - L6-L19

```python
test_parent_not_navigated_returns_no_predicates_and_reports_reason(relationship_policy)
```

Observed calls (lexical order): `relationship_policy.where_conditions`, `set`, `any`.

### `test_lrf_marker_does_not_add_duplicate_predicates` - L22-L37

```python
test_lrf_marker_does_not_add_duplicate_predicates(relationship_policy)
```

Observed calls (lexical order): `relationship_policy.where_conditions`, `object`, `any`.

### `test_lrf_area_sweep_does_not_inherit_foreign_key_predicates` - L39-L60

```python
test_lrf_area_sweep_does_not_inherit_foreign_key_predicates(relationship_policy)
```

A root SWEEP must not be narrowed by unrelated mapped FK columns.

Observed calls (lexical order): `relationship_policy.where_conditions`, `SimpleNamespace`, `any`.

### `test_lrf_relationship_path_keeps_relationship_predicates` - L63-L80

```python
test_lrf_relationship_path_keeps_relationship_predicates(relationship_policy)
```

An ALL/path child access must retain its parent-child predicate.

Observed calls (lexical order): `relationship_policy.where_conditions`, `SimpleNamespace`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
