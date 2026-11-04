# `patterns/update_date_host_patterns.py`

Source: [patterns/update_date_host_patterns.py](../../../patterns/update_date_host_patterns.py) | 39 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `7442d531ea46bb18ef226ea022a959215032da46df17258f451f9a5ba8a50ea2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`EXEC_SQL_START_PATTERN` (L10), `END_EXEC_PATTERN` (L15), `MOVE_TO_HOST_OF_GROUP_PATTERN` (L21), `MOVE_SOURCE_ONLY_PATTERN` (L29), `TO_HOST_OF_GROUP_PATTERN` (L35)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_date_host_converter.py](../converter/postprocess/update_date_host_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
