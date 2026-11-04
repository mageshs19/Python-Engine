# `converter/generators/enhancement/enhancement_pipeline.py`

Source: [converter/generators/enhancement/enhancement_pipeline.py](../../../../../converter/generators/enhancement/enhancement_pipeline.py) | 116 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `24b9627331e008aaf9549d388ead2461665b13f72764b04d6f273ee63e90ae4c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`logger` (L16), `STEP_START` (L18), `STEP_DONE` (L19), `STEP_SCOPE` (L20), `STEP_MESSAGE` (L21), `STEP_GROUPS` (L22), `STEP_NO_CHANGE` (L23), `STEP_FAILED` (L24), `PIPELINE_FAILED` (L25), `__all__` (L112)

## Import declarations

```python
from __future__ import annotations
import logging
from typing import Dict
from converter.generators.enhancement.output_validator import OutputValidator
from converter.generators.initialization.scope_initializer import CursorScopedInitializer
from converter.pipeline.conversion.conversion_layout_steps import FinalSequenceResequencerService
```

## Local dependency notes

- [converter/generators/enhancement/output_validator.py](output_validator.md)
- [converter/generators/initialization/scope_initializer.py](../initialization/scope_initializer.md)
- [converter/pipeline/conversion/conversion_layout_steps.py](../../pipeline/conversion/conversion_layout_steps.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/converter_pipeline_integration.py](../converter_pipeline_integration.md)
- [converter/generators/enhancement/__init__.py](__init__.md)

## Symbol contracts and control points

### `ConverterEnhancementPipeline` - L28-L90

```python
class ConverterEnhancementPipeline()
```

### `ConverterEnhancementPipeline.__init__` - L30-L33

```python
__init__(self, program_text: str, program_id: str='UNKNOWN') -> None
```

Observed calls (lexical order): `logging.getLogger`.

### `ConverterEnhancementPipeline.execute` - L35-L51

```python
execute(self) -> str
```

Observed calls (lexical order): `STEP_START.format`, `self.logger.info`, `self._step_scope_initialization`, `FinalSequenceResequencerService`, `FinalSequenceResequencerService().resequence`, `STEP_DONE.format`, `self.logger.error`, `PIPELINE_FAILED.format`.

### `ConverterEnhancementPipeline._step_scope_initialization` - L53-L86

```python
_step_scope_initialization(self, program_text: str) -> str
```

Observed calls (lexical order): `STEP_SCOPE.format`, `self.logger.info`, `CursorScopedInitializer`, `initializer.process`, `STEP_MESSAGE.format`, `self.logger.debug`, `STEP_GROUPS.format`, `len`, `self.logger.warning`, `STEP_NO_CHANGE.format`, `STEP_FAILED.format`.

Control points:

- L59: `for message in initializer.messages`
- L74: `if result == program_text and initializer.messages`

### `ConverterEnhancementPipeline.validate_output` - L89-L90

```python
validate_output(program_text: str) -> Dict[str, object]
```

Observed calls (lexical order): `OutputValidator`, `OutputValidator().validate`.

### `enhance_converter_output` - L93-L97

```python
enhance_converter_output(program_text: str, program_id: str='UNKNOWN') -> str
```

Observed calls (lexical order): `ConverterEnhancementPipeline`, `ConverterEnhancementPipeline(program_text, program_id).execute`.

### `setup_pipeline_logging` - L100-L109

```python
setup_pipeline_logging(log_level: int=logging.INFO) -> None
```

Observed calls (lexical order): `logging.getLogger`, `pipeline_logger.setLevel`, `logging.StreamHandler`, `handler.setFormatter`, `logging.Formatter`, `pipeline_logger.addHandler`.

Control points:

- L103: `if pipeline_logger.handlers`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
