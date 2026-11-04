# `converter/generators/converter_pipeline_integration.py`

Source: [converter/generators/converter_pipeline_integration.py](../../../../converter/generators/converter_pipeline_integration.py) | 42 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `c6e33e55d5e15be6947c7bad9dde5a025a30ad1f4185afaec6f90f7611973558`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`logger` (L19), `BODY_START` (L21), `BODY_END` (L22), `__all__` (L33)

## Import declarations

```python
from __future__ import annotations
import logging
from converter.generators.enhancement.enhancement_pipeline import ConverterEnhancementPipeline, enhance_converter_output, setup_pipeline_logging
from converter.generators.enhancement.output_validator import OutputValidator, validate_output
from converter.generators.initialization.line_geometry import LineGeometry
from patterns.initialization_scope_patterns import FETCH_PARAGRAPH_HEADER_PATTERN as FETCH_PARAGRAPH_PATTERN
```

## Local dependency notes

- [converter/generators/enhancement/enhancement_pipeline.py](enhancement/enhancement_pipeline.md)
- [converter/generators/enhancement/output_validator.py](enhancement/output_validator.md)
- [converter/generators/initialization/line_geometry.py](initialization/line_geometry.md)
- [patterns/initialization_scope_patterns.py](../../patterns/initialization_scope_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_layout_pipeline.py](../pipeline/conversion/conversion_layout_pipeline.md)

## Symbol contracts and control points

### `_body` - L25-L26

```python
_body(line: str) -> str
```

Observed calls (lexical order): `LineGeometry.body`.

### `_is_comment` - L29-L30

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `LineGeometry.is_comment`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
