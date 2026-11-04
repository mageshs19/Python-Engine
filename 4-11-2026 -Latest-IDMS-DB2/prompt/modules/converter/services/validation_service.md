# `converter/services/validation_service.py`

Source: [converter/services/validation_service.py](../../../../converter/services/validation_service.py) | 33 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `e5bad35d52a58b26f4db219b475c03c7801832c3a2d2112978a2edde1abbb55d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import ConversionInput
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)

## Symbol contracts and control points

### `ValidationService` - L4-L33

```python
class ValidationService()
```

Validates the minimum required conversion inputs.

### `ValidationService.validate` - L12-L33

```python
validate(self, conversion_input: ConversionInput) -> list[str]
```

Observed calls (lexical order): `messages.append`, `conversion_input.idms_cobol_text.strip`.

Control points:

- L18: `if not conversion_input.sheet_mapping_rows`
- L23: `if not conversion_input.dclgen_columns`
- L28: `if not conversion_input.idms_cobol_text.strip()`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
