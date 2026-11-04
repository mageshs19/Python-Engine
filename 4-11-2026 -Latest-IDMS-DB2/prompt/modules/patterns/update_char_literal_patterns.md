# `patterns/update_char_literal_patterns.py`

Source: [patterns/update_char_literal_patterns.py](../../../patterns/update_char_literal_patterns.py) | 41 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `55bf130206eda9f4aeedf10b1f1c7e77588cb5b8dbf547401092f1989c6fffe7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`EXEC_SQL_START_PATTERN` (L10), `END_EXEC_PATTERN` (L15), `MOVE_NUMLIT_TO_HOST_OF_GROUP_PATTERN` (L22), `TO_HOST_OF_GROUP_PATTERN` (L31), `MOVE_NUMLIT_ONLY_PATTERN` (L38)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_char_literal_quoter.py](../converter/postprocess/update_char_literal_quoter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
