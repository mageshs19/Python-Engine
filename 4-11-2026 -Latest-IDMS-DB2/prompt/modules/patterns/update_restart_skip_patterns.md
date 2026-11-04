# `patterns/update_restart_skip_patterns.py`

Source: [patterns/update_restart_skip_patterns.py](../../../patterns/update_restart_skip_patterns.py) | 46 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `92361955b075103a35d6011d2cf7e5262902d415b3f730437da6c7ae6ca1ae3c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`CONVERTED_FOR_PATTERN` (L8), `SKIPPED_FOR_PATTERN` (L15), `REMOVED_OBTAIN_CALC_PATTERN` (L22), `SQLCODE_IF_PATTERN` (L28), `END_IF_PATTERN` (L33), `CONTINUE_PATTERN` (L38), `DB2_COMMENT_PATTERN` (L43)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_restart_skip_composer.py](../converter/composers/update_restart_skip_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
