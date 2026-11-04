# `converter/composers/record_materialisation/__init__.py`

Source: [converter/composers/record_materialisation/__init__.py](../../../../../converter/composers/record_materialisation/__init__.py) | 54 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `3c2101e60950d379bdaa92280c0e8fd17ed575fae879239832381407a5a8d838`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Whole-record MOVE materialisation.

## Module-level bindings

`__all__` (L41)

## Import declarations

```python
from converter.composers.record_materialisation.record_field_plan import RecordFieldPlan, RecordMaterialisationPlan, RecordPlanBuilder
from converter.composers.record_materialisation.record_layout_generator import RecordLayoutGenerator
from converter.composers.record_materialisation.record_move_generator import RecordMoveGenerator
from converter.composers.record_materialisation.record_line_utils import RecordLineUtils
from converter.composers.record_materialisation.record_move_scanner import MoveSite, RecordMoveScanner, TargetSite
from converter.composers.record_materialisation.record_materialisation_guard import RecordMaterialisationGuard, Refusal
from converter.composers.record_materialisation.record_block_writer import RecordBlockWriter
```

## Local dependency notes

- [converter/composers/record_materialisation/record_block_writer.py](record_block_writer.md)
- [converter/composers/record_materialisation/record_field_plan.py](record_field_plan.md)
- [converter/composers/record_materialisation/record_layout_generator.py](record_layout_generator.md)
- [converter/composers/record_materialisation/record_line_utils.py](record_line_utils.md)
- [converter/composers/record_materialisation/record_materialisation_guard.py](record_materialisation_guard.md)
- [converter/composers/record_materialisation/record_move_generator.py](record_move_generator.md)
- [converter/composers/record_materialisation/record_move_scanner.py](record_move_scanner.md)

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
