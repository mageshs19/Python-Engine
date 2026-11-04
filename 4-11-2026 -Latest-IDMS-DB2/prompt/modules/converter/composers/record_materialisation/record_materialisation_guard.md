# `converter/composers/record_materialisation/record_materialisation_guard.py`

Source: [converter/composers/record_materialisation/record_materialisation_guard.py](../../../../../converter/composers/record_materialisation/record_materialisation_guard.py) | 131 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `e3ad8555f2b2bd6853a84e5addbeddfa9b9008691f903b6e265ca3049fff59cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Decides whether one record may be materialised.

## Module-level bindings

`MISSING_HOST_SAMPLE` (L36), `__all__` (L131)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from rules.record_materialisation_rules import ALLOW_LAYOUT_SHORTER_THAN_TARGET, ENFORCE_LENGTH_MATCH, LENGTH_TOLERANCE
```

## Local dependency notes

- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/__init__.py](__init__.md)
- [converter/composers/record_materialisation_composer.py](../record_materialisation_composer.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `Refusal` - L40-L44

```python
class Refusal()
```

A named diagnostic plus its template values.

Declared class/data-model fields:

```python
key: str = ''
values: dict = field(default_factory=dict)
```

### `RecordMaterialisationGuard` - L47-L128

```python
class RecordMaterialisationGuard()
```

All refusal decisions for one record, in evaluation order.

### `RecordMaterialisationGuard.__init__` - L50-L51

```python
__init__(self, plan_builder) -> None
```

### `RecordMaterialisationGuard.build_plan` - L54-L81

```python
build_plan(self, record: str)
```

(plan, refusal). plan is None when the record is refused.

Observed calls (lexical order): `self.plan_builder.looks_like_record`, `Refusal`, `self.plan_builder.build`, `len`, `', '.join`.

Control points:

- L56: `if not self.plan_builder.looks_like_record(record)`
- L63: `if not plan.fields`
- L66: `if not plan.group_name`
- L69: `if plan.missing_hosts`

### `RecordMaterialisationGuard.check_length` - L85-L114

```python
check_length(plan, target: str, declared_bytes: int)
```

Refusal when the layout is LONGER than the target field.

Observed calls (lexical order): `Refusal`, `plan.overflows`, `plan.remainder_bytes`.

Control points:

- L87: `if not ENFORCE_LENGTH_MATCH`
- L91: `if not declared_bytes or declared_bytes <= 0`
- L103: `if not (too_long or too_short)`

### `RecordMaterialisationGuard.check_movable` - L118-L128

```python
check_movable(plan)
```

Not a refusal. A visible warning that nothing is populated.

Observed calls (lexical order): `Refusal`, `len`.

Control points:

- L120: `if plan.movable_fields`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
