# `rules/update_runner_rules.py`

Source: [rules/update_runner_rules.py](../../../rules/update_runner_rules.py) | 18 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `8a2e4f75425a7b899d358faf654d20fc4870f1737482ae0b24ec6ba928c69caf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`UPDATE_RUNNER_RULES` (L5), `AUTO_FIX_PIC_LENGTH_MISMATCHES_DEFAULT` (L13), `OUTPUT_TIMESTAMP_FORMAT` (L14), `OUTPUT_FILE_EXTENSION` (L15), `OUTPUT_FILE_NAME_TEMPLATE` (L16), `COBOL_TEXT_ENCODING` (L17), `UPDATE_LOGGER_NAME` (L18)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/run_update.py](../runners/run_update.md)
- [runners/update/update_program_converter.py](../runners/update/update_program_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
