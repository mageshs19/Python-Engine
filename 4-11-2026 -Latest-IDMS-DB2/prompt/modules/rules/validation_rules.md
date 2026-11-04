# `rules/validation_rules.py`

Source: [rules/validation_rules.py](../../../rules/validation_rules.py) | 24 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `1b068b11454b187809f02e20293c3b1f57c0aec3435e897d097fa0f073c2a00c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Validation rule messages. Validators import these constants so validation message text stays centralized.

## Module-level bindings

`INPUT_VALIDATION_MESSAGES` (L5), `MAPPING_VALIDATION_MESSAGES` (L11), `PRODUCTION_VALIDATION_MESSAGES` (L17)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/validators/input_validator.py](../converter/validators/input_validator.md)
- [converter/validators/mapping_validator.py](../converter/validators/mapping_validator.md)
- [converter/validators/production_validator.py](../converter/validators/production_validator.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
