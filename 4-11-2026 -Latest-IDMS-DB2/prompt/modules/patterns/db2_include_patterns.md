# `patterns/db2_include_patterns.py`

Source: [patterns/db2_include_patterns.py](../../../patterns/db2_include_patterns.py) | 52 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `732da08427530004673d32a40d92d1d44f9a9a8dce60a43aaec353045b218f0f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 INCLUDE scanning patterns.

## Module-level bindings

`INCLUDE_SINGLE_PATTERN` (L20), `INCLUDE_BODY_PATTERN` (L26), `INCLUDE_NAME_PATTERN` (L32), `EXEC_SQL_OPEN_PATTERN` (L37), `END_EXEC_PATTERN` (L42), `DCLGEN_GROUP_PATTERN` (L49)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/dclgen_include_cleanup.py](../converter/composers/cleanup/dclgen_include_cleanup.md)
- [converter/generators/db2_infrastructure/include_renderer.py](../converter/generators/db2_infrastructure/include_renderer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
