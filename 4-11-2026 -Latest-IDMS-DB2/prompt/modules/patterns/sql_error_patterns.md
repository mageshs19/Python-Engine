# `patterns/sql_error_patterns.py`

Source: [patterns/sql_error_patterns.py](../../../patterns/sql_error_patterns.py) | 35 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `5af65e4006c441486f355e2bf9c28db84987bbe8ef229dd097f3197eac7c689c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQLERROR regex patterns.

## Module-level bindings

`SQLERROR_PARAGRAPH_PATTERN` (L14), `SQLERROR_HEADER_ONLY_PATTERN` (L20), `PARAGRAPH_HEADER_PATTERN` (L26), `END_PROGRAM_BOUNDARY_PATTERN` (L32)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/sql_error_generator.py](../converter/generators/sql_error_generator.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
