# `rules/update_program_postprocess_rules.py`

Source: [rules/update_program_postprocess_rules.py](../../../rules/update_program_postprocess_rules.py) | 70 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `58d5532e127e6fbe6a09dbaa8d3cd883520a5b322e9533f873803c87fa756ed1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Rules for update-program COBOL postprocess.

## Module-level bindings

`UPDATE_POSTPROCESS_RULES` (L11), `RESTART_PARAGRAPH_NAMES` (L21), `RESTART_DEFAULTS` (L32), `UPDATE_WORKING_STORAGE_NAMES` (L39), `RESTART_DCLGEN_ROLE_TOKENS` (L52), `RESTART_DCLGEN_MIN_SCORE` (L66), `GENERATED_UPDATE_COMMENT` (L70)

## Import declarations

```python
from __future__ import annotations
```

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
