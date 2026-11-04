# `converter/validators/input_validator.py`

Source: [converter/validators/input_validator.py](../../../../converter/validators/input_validator.py) | 34 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `580717c33d9a09cee06bb7a0b630c99c15559e99d81508f44207f0237200b490`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import ConversionInput
from rules.validation_rules import INPUT_VALIDATION_MESSAGES
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [rules/validation_rules.py](../../rules/validation_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion_service.py](../pipeline/conversion_service.md)
- [tests/test_validators.py](../../tests/test_validators.md)

## Symbol contracts and control points

### `InputValidator` - L5-L34

```python
class InputValidator()
```

Validates required conversion inputs.

### `InputValidator.validate` - L13-L34

```python
validate(self, conversion_input: ConversionInput) -> list[str]
```

Observed calls (lexical order): `messages.append`, `conversion_input.idms_cobol_text.strip`.

Control points:

- L19: `if not conversion_input.sheet_mapping_rows`
- L24: `if not conversion_input.dclgen_columns`
- L29: `if not conversion_input.idms_cobol_text.strip()`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
