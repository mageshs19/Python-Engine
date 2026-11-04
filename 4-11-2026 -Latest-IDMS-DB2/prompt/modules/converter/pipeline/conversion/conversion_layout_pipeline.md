# `converter/pipeline/conversion/conversion_layout_pipeline.py`

Source: [converter/pipeline/conversion/conversion_layout_pipeline.py](../../../../../converter/pipeline/conversion/conversion_layout_pipeline.py) | 215 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `9b4b188bba11847ec8a7d18aaf25df2fc6881478a3dc902d7e30a746a4b8bf69`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Finishing phase of the IDMS->DB2 conversion.

## Module-level bindings

`__all__` (L215)

## Import declarations

```python
from __future__ import annotations
from collections.abc import Callable
from converter.pipeline.conversion.conversion_layout_steps import ConversionLayoutSteps
from converter.generators.converter_pipeline_integration import ConverterEnhancementPipeline
```

## Local dependency notes

- [converter/generators/converter_pipeline_integration.py](../../generators/converter_pipeline_integration.md)
- [converter/pipeline/conversion/conversion_layout_steps.py](conversion_layout_steps.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](conversion_pipeline.md)

## Symbol contracts and control points

### `ConversionLayoutPipeline` - L38-L212

```python
class ConversionLayoutPipeline()
```

Runs the layout and finishing passes, in a fixed, load-bearing order.

### `ConversionLayoutPipeline.__init__` - L109-L126

```python
__init__(self, *, composers: dict, resolvers: dict, component_messages: Callable[[object], list[str]], steps: ConversionLayoutSteps | None=None, restart_context=None) -> None
```

Observed calls (lexical order): `ConversionLayoutSteps`.

### `ConversionLayoutPipeline.finish` - L131-L212

```python
finish(self, *, converted_cobol: str, original_idms_text: str, validation_messages: list[str]) -> str
```

Observed calls (lexical order): `steps.apply_layout`, `steps.extract_output_write_paragraph`, `steps.apply_late_date_conversion`, `steps.materialise_records`, `steps.declare_counters`, `steps.inject_restart_control`, `steps.comment_unmapped_blocks`, `steps.apply_structural_safety`, `steps.normalize_indentation`, `steps.align_moves`, `steps.separate_paragraphs`, `steps.resequence`, `steps.cleanup_final_comments`, `ConverterEnhancementPipeline`, `enhancement_pipeline.execute`, `validation_messages.append`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
