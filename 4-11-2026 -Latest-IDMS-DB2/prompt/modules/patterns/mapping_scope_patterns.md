# `patterns/mapping_scope_patterns.py`

Source: [patterns/mapping_scope_patterns.py](../../../patterns/mapping_scope_patterns.py) | 21 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `589bc5b3bbdd2115fb514cf06a6042ea4520cfc9cf19c994c53457da50e5e9b5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Mapping scope regex patterns. Patterns only.

## Module-level bindings

`MESSAGE_TABLE_PATTERN` (L12), `SOURCE_TOKEN_PATTERN` (L18)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/validators/mapping_scope_filter.py](../converter/validators/mapping_scope_filter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
