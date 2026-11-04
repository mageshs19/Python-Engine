# `converter/pipeline/conversion/conversion_layout_steps.py`

Source: [converter/pipeline/conversion/conversion_layout_steps.py](../../../../../converter/pipeline/conversion/conversion_layout_steps.py) | 491 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `ad0519f15e9c66fb0fc26fa7e9702f3a4bfaa6ad603e15c481257c4ac68ffbd0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Individual finishing passes of the IDMS->DB2 conversion.

## Module-level bindings

`RESTART_COMPOSER_ABSENT` (L123), `__all__` (L491)

## Import declarations

```python
from __future__ import annotations
from collections.abc import Callable
from converter.composers.late_db2_date_composer import LateDb2DateComposer
from converter.composers.structural_safety_composer import StructuralSafetyComposer
from converter.composers.unmapped_record_block_composer import UnmappedRecordBlockComposer
from converter.services.final_sequence_resequencer_service import FinalSequenceResequencerService
from rules.record_materialisation_rules import RECORD_MATERIALISATION_MESSAGES
from converter.pipeline.run import run_stage
from converter.pipeline.stage import Document
```

## Local dependency notes

- [converter/composers/late_db2_date_composer.py](../../composers/late_db2_date_composer.md)
- [converter/composers/structural_safety_composer.py](../../composers/structural_safety_composer.md)
- [converter/composers/unmapped_record_block_composer.py](../../composers/unmapped_record_block_composer.md)
- [converter/pipeline/run.py](../run.md)
- [converter/pipeline/stage.py](../stage.md)
- [converter/services/final_sequence_resequencer_service.py](../../services/final_sequence_resequencer_service.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/enhancement/enhancement_pipeline.py](../../generators/enhancement/enhancement_pipeline.md)
- [converter/pipeline/conversion/conversion_layout_pipeline.py](conversion_layout_pipeline.md)

## Symbol contracts and control points

### `ConversionLayoutSteps` - L129-L470

```python
class ConversionLayoutSteps()
```

The finishing passes, each independently runnable.

### `ConversionLayoutSteps.__init__` - L132-L141

```python
__init__(self, *, composers: dict, resolvers: dict, component_messages: Callable[[object], list[str]]) -> None
```

### `ConversionLayoutSteps.apply_layout` - L146-L163

```python
apply_layout(self, *, converted_cobol: str, original_idms_text: str) -> str
```

Observed calls (lexical order): `self.composers['formatter'].format`, `self.composers['manual_layout'].compose`, `self.composers['style_preserver'].preserve`, `self.composers['fixed_format'].format`.

### `ConversionLayoutSteps.extract_output_write_paragraph` - L168-L193

```python
extract_output_write_paragraph(self, *, converted_cobol: str, validation_messages: list[str]) -> str
```

Lift the record-population body into its own WRITE paragraph.

Observed calls (lexical order): `run_stage`, `Document`, `validation_messages.extend`.

### `ConversionLayoutSteps.apply_late_date_conversion` - L198-L218

```python
apply_late_date_conversion(self, *, converted_cobol: str, validation_messages: list[str]) -> str
```

Re-run the date and INITIALIZE passes on the relocated block.

Observed calls (lexical order): `LateDb2DateComposer`, `composer.compose`, `self._component_messages`, `validation_messages.extend`.

### `ConversionLayoutSteps.materialise_records` - L223-L253

```python
materialise_records(self, *, converted_cobol: str, validation_messages: list[str]) -> str
```

Expand every whole-record MOVE into layout + field moves.

Observed calls (lexical order): `self.composers.get`, `validation_messages.append`, `composer.compose`, `self._component_messages`, `validation_messages.extend`.

Control points:

- L245: `if composer is None`

### `ConversionLayoutSteps.declare_counters` - L258-L276

```python
declare_counters(self, *, converted_cobol: str, validation_messages: list[str]) -> str
```

Declare referenced counters and append end-of-run totals.

Observed calls (lexical order): `Document`, `run_stage`, `validation_messages.extend`.

### `ConversionLayoutSteps.inject_restart_control` - L281-L317

```python
inject_restart_control(self, *, converted_cobol: str, validation_messages: list[str], restart_context=None) -> str
```

Apply the restart family to an UPDATE program.

Observed calls (lexical order): `self.composers.get`, `validation_messages.append`, `composer.compose`, `self._component_messages`, `validation_messages.extend`.

Control points:

- L306: `if composer is None`

### `ConversionLayoutSteps.comment_unmapped_blocks` - L322-L336

```python
comment_unmapped_blocks(self, *, converted_cobol: str, original_idms_text: str, validation_messages: list[str]) -> str
```

Observed calls (lexical order): `UnmappedRecordBlockComposer`, `composer.compose`, `self._component_messages`, `validation_messages.extend`.

### `ConversionLayoutSteps.apply_structural_safety` - L341-L365

```python
apply_structural_safety(self, *, converted_cobol: str, original_idms_text: str, validation_messages: list[str]) -> str
```

Comment references the compiler would reject.

Observed calls (lexical order): `StructuralSafetyComposer`, `composer.compose`, `self._component_messages`, `validation_messages.extend`.

### `ConversionLayoutSteps.normalize_indentation` - L370-L387

```python
normalize_indentation(self, *, converted_cobol: str, validation_messages: list[str]) -> str
```

Align every PROCEDURE DIVISION statement line to Area B.

Observed calls (lexical order): `run_stage`, `Document`, `validation_messages.extend`.

### `ConversionLayoutSteps.align_moves` - L392-L411

```python
align_moves(self, *, converted_cobol: str, validation_messages: list[str]) -> str
```

Align TO across runs of MOVE statements.

Observed calls (lexical order): `Document`, `run_stage`, `validation_messages.extend`.

### `ConversionLayoutSteps.separate_paragraphs` - L416-L434

```python
separate_paragraphs(self, *, converted_cobol: str, validation_messages: list[str]) -> str
```

Insert a blank line before a paragraph header.

Observed calls (lexical order): `Document`, `run_stage`, `validation_messages.extend`.

### `ConversionLayoutSteps.resequence` - L440-L446

```python
resequence(converted_cobol: str) -> str
```

Re-sequence ONLY columns 1-6 and 73-80.

Observed calls (lexical order): `FinalSequenceResequencerService`, `FinalSequenceResequencerService().resequence`.

### `ConversionLayoutSteps.cleanup_final_comments` - L451-L470

```python
cleanup_final_comments(self, converted_cobol: str, validation_messages: list[str]) -> str
```

Remove unnecessary comment blocks from fixed-format output.

Observed calls (lexical order): `Document`, `run_stage`, `validation_messages.extend`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
