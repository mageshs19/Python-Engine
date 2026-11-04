# `converter/composers/record_materialisation/record_plan.py`

Source: [converter/composers/record_materialisation/record_plan.py](../../../../../converter/composers/record_materialisation/record_plan.py) | 98 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `fb4663f8103fe490f742303f7070fd649874652c00e510b7601e786ab3b78657`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Everything needed to materialise one record.

## Module-level bindings

`__all__` (L98)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.composers.record_materialisation.record_field import DEFAULT_LEVEL, RecordFieldPlan
from rules.record_materialisation_rules import REQUIRE_COMPLETE_FIELD_COVERAGE
```

## Local dependency notes

- [converter/composers/record_materialisation/record_field.py](record_field.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_field_plan.py](record_field_plan.md)
- [converter/composers/record_materialisation/record_layout_generator.py](record_layout_generator.md)
- [converter/composers/record_materialisation/record_plan_builder.py](record_plan_builder.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/generated_fields/test_record_comp3_preservation.py](../../../tests/generated_fields/test_record_comp3_preservation.md)
- [tests/test_db2_code_fixes.py](../../../tests/test_db2_code_fixes.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `RecordMaterialisationPlan` - L23-L95

```python
class RecordMaterialisationPlan()
```

Fields, diagnostics and sizes for one materialised record.

Declared class/data-model fields:

```python
record_name: str = ''
table_name: str = ''
group_name: str = ''
fields: list[RecordFieldPlan] = field(default_factory=list)
missing_hosts: list[str] = field(default_factory=list)
skipped_rows: int = 0
```

### `RecordMaterialisationPlan.declarable_fields` - L35-L36

```python
declarable_fields(self) -> list[RecordFieldPlan]
```

### `RecordMaterialisationPlan.movable_fields` - L39-L40

```python
movable_fields(self) -> list[RecordFieldPlan]
```

### `RecordMaterialisationPlan.filler_fields` - L43-L44

```python
filler_fields(self) -> list[RecordFieldPlan]
```

### `RecordMaterialisationPlan.total_bytes` - L48-L53

```python
total_bytes(self) -> int
```

Observed calls (lexical order): `sum`.

### `RecordMaterialisationPlan.min_level` - L56-L63

```python
min_level(self) -> int
```

Shallowest level in the mapping, used to rebase the layout.

Observed calls (lexical order): `int`, `str`, `str(item.level).strip`, `str(item.level).strip().isdigit`, `min`.

### `RecordMaterialisationPlan.is_complete` - L67-L70

```python
is_complete(self) -> bool
```

Control points:

- L68: `if not REQUIRE_COMPLETE_FIELD_COVERAGE`

### `RecordMaterialisationPlan.remainder_bytes` - L72-L86

```python
remainder_bytes(self, declared_bytes: int) -> int
```

Unused trailing bytes of the target field. Never negative.

Observed calls (lexical order): `int`, `max`.

Control points:

- L84: `if not declared_bytes or int(declared_bytes) <= 0`

### `RecordMaterialisationPlan.overflows` - L88-L95

```python
overflows(self, declared_bytes: int, tolerance: int=0) -> bool
```

True ONLY when the layout is LONGER than the target field.

Observed calls (lexical order): `int`.

Control points:

- L93: `if not declared_bytes or int(declared_bytes) <= 0`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
