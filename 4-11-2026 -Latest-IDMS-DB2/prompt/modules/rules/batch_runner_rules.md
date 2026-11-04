# `rules/batch_runner_rules.py`

Source: [rules/batch_runner_rules.py](../../../rules/batch_runner_rules.py) | 32 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `75822c57f37f3541fbf86bdd1cd3fce326e0fe4f3834896c30c5c5f315a65d09`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`BATCH_RUNNER_RULES` (L8), `BATCH_MODE_UPDATE` (L16), `BATCH_MODE_RETRIEVAL` (L17), `TARGET_PROGRAM_ID_ENV_KEY` (L20), `AUTO_FIX_PIC_LENGTH_MISMATCHES_DEFAULT` (L23), `OUTPUT_TIMESTAMP_FORMAT` (L26), `OUTPUT_FILE_EXTENSION` (L27), `OUTPUT_FILE_NAME_TEMPLATE` (L28), `COBOL_TEXT_ENCODING` (L32)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch/batch_environment.py](../runners/batch/batch_environment.md)
- [runners/batch/batch_validator.py](../runners/batch/batch_validator.md)
- [runners/batch/program_converter.py](../runners/batch/program_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
