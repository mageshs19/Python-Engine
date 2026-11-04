# `patterns/lrf_program_patterns.py`

Source: [patterns/lrf_program_patterns.py](../../../patterns/lrf_program_patterns.py) | 107 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `f8a3f46c2516ab94826ff6a4e69604552b365fdce356f6e12aea97d114f71dff`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for LRF syntax appearing in the COBOL PROGRAM (not the subschema).

## Module-level bindings

`LR_OBTAIN_WHERE_PATTERN` (L15), `LR_OBTAIN_WHERE_PREFIX_PATTERN` (L26), `LR_OBTAIN_START_PATTERN` (L37), `LR_ERASE_WHERE_PATTERN` (L44), `LR_MODIFY_WHERE_PATTERN` (L51), `LR_STATUS_CONDITION_PATTERN` (L58), `LR_STATUS_TOKEN_PATTERN` (L65), `OF_LR_SUFFIX_PATTERN` (L71), `BARE_OF_LR_PATTERN` (L77), `COPY_SUBSCHEMA_LR_CTRL_PATTERN` (L83), `LR_STATUS_TOKEN_REPLACEMENT_PATTERN` (L97), `LR_STATUS_ABBREVIATED_PATTERN` (L103)

## Import declarations

```python
from __future__ import annotations
import re
from rules.lrf_conversion_rules import LR_STATUS_TOKEN_REPLACEMENT_ORDER
```

## Local dependency notes

- [rules/lrf_conversion_rules.py](../rules/lrf_conversion_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/lr_status_token_replacer.py](../converter/transformers/lr_status_token_replacer.md)
- [converter/transformers/lrf_path_expander.py](../converter/transformers/lrf_path_expander.md)
- [converter/transformers/lrf_update_expander.py](../converter/transformers/lrf_update_expander.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
