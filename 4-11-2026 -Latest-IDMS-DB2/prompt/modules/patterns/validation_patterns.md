# `patterns/validation_patterns.py`

Source: [patterns/validation_patterns.py](../../../patterns/validation_patterns.py) | 103 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `49d46f07784e77bcd6270e4fd27ea3efad4b3e4f989f67adbe1a48b94638542c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Validation regex patterns.

## Module-level bindings

`TODO_HOST_VARIABLE_PATTERN` (L10), `TODO_DB2_PATTERN` (L16), `ERROR_DB2_PATTERN` (L22), `UNABLE_TO_DECLARE_CURSOR_PATTERN` (L28), `NO_FETCH_HOST_VARIABLES_PATTERN` (L34), `FORBIDDEN_EXECUTABLE_IDMS_PATTERNS` (L40), `FORBIDDEN_IDMS_DECLARATIVE_PATTERNS` (L70)

## Import declarations

```python
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/validators/production_validator.py](../converter/validators/production_validator.md)
- [tests/test_patterns.py](../tests/test_patterns.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
