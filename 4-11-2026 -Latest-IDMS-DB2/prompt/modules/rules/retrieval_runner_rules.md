# `rules/retrieval_runner_rules.py`

Source: [rules/retrieval_runner_rules.py](../../../rules/retrieval_runner_rules.py) | 29 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `d3c16c6d87d82ac181267ad2d237d9ee1aa29fa2426063b28f71915b22ee0066`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`RETRIEVAL_RUNNER_RULES` (L8), `AUTO_FIX_PIC_LENGTH_MISMATCHES_DEFAULT` (L16), `OUTPUT_TIMESTAMP_FORMAT` (L19), `OUTPUT_FILE_EXTENSION` (L20), `OUTPUT_FILE_NAME_TEMPLATE` (L21), `COBOL_TEXT_ENCODING` (L24), `RETRIEVAL_LOGGER_NAME` (L27)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/convert_programs.py](../runners/convert_programs.md)
- [runners/retrieval/retrieval_program_converter.py](../runners/retrieval/retrieval_program_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
