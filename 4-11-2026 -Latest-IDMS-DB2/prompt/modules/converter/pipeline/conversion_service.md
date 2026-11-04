# `converter/pipeline/conversion_service.py`

Source: [converter/pipeline/conversion_service.py](../../../../converter/pipeline/conversion_service.py) | 51 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `487cc263a485ced37634ea76bcd3796e2893d212b03df407ae4ab605213bbd09`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import ConversionInput, ConversionResult
from converter.pipeline.conversion.conversion_component_factory import ConversionComponentFactory
from converter.pipeline.conversion.conversion_message_utils import ConversionMessageUtils
from converter.pipeline.conversion.conversion_pipeline import ConversionPipeline
from converter.validators.input_validator import InputValidator
from converter.validators.production_validator import ProductionValidator
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/pipeline/conversion/conversion_component_factory.py](conversion/conversion_component_factory.md)
- [converter/pipeline/conversion/conversion_message_utils.py](conversion/conversion_message_utils.md)
- [converter/pipeline/conversion/conversion_pipeline.py](conversion/conversion_pipeline.md)
- [converter/validators/input_validator.py](../validators/input_validator.md)
- [converter/validators/production_validator.py](../validators/production_validator.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/program_converter.py](../../runners/batch/program_converter.md)
- [runners/retrieval/retrieval_program_converter.py](../../runners/retrieval/retrieval_program_converter.md)
- [runners/update/update_program_converter.py](../../runners/update/update_program_converter.md)
- [tests/test_imports.py](../../tests/test_imports.md)

## Symbol contracts and control points

### `ConversionService` - L17-L51

```python
class ConversionService(ConversionComponentFactory, ConversionPipeline, ConversionMessageUtils)
```

Main orchestration service for IDMS COBOL to DB2 COBOL conversion.

### `ConversionService.convert` - L24-L51

```python
convert(self, conversion_input: ConversionInput) -> ConversionResult
```

Observed calls (lexical order): `InputValidator`, `InputValidator().validate`, `validation_messages.extend`, `ConversionResult`, `self._unique_messages`, `self._run_pipeline`, `ProductionValidator`, `ProductionValidator(dclgen_repository=dclgen_repository).validate`.

Control points:

- L29: `if input_messages`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
