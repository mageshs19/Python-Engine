# `converter/composers/record_materialisation/record_field_plan.py`

Source: [converter/composers/record_materialisation/record_field_plan.py](../../../../../converter/composers/record_materialisation/record_field_plan.py) | 47 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `7481e2b4d6b5a435c955f31bab34ca8dafaf43216c799220aa5f8babc1c0f738`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Back-compatible import point for the record plan model.

## Module-level bindings

`__all__` (L39)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_field import COMP_3_SYMBOL, DEFAULT_LEVEL, RecordFieldPlan
from converter.composers.record_materialisation.record_host_resolver import RecordHostResolver
from converter.composers.record_materialisation.record_plan import RecordMaterialisationPlan
from converter.composers.record_materialisation.record_plan_builder import RecordPlanBuilder
from converter.composers.record_materialisation.record_row_reader import RecordRowReader
```

## Local dependency notes

- [converter/composers/record_materialisation/record_field.py](record_field.md)
- [converter/composers/record_materialisation/record_host_resolver.py](record_host_resolver.md)
- [converter/composers/record_materialisation/record_plan.py](record_plan.md)
- [converter/composers/record_materialisation/record_plan_builder.py](record_plan_builder.md)
- [converter/composers/record_materialisation/record_row_reader.py](record_row_reader.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/__init__.py](__init__.md)
- [converter/composers/record_materialisation/record_move_generator.py](record_move_generator.md)

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
