# `patterns/program_kind_patterns.py`

Source: [patterns/program_kind_patterns.py](../../../patterns/program_kind_patterns.py) | 67 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a989f3c8eff89825f58261d6020d1d381a87a70707b8728fedb9a291cf75283e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for program-kind detection. PATTERNS ONLY.

## Module-level bindings

`IDMS_WRITE_VERB_PATTERN` (L30), `IDMS_WRITE_LRF_PATTERN` (L37), `SQL_WRITE_VERB_PATTERN` (L44), `CONVERTED_WRITE_MARKER_PATTERN` (L51), `KEEP_WRITE_MARKER_PATTERN` (L56), `__all__` (L61)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/program_kind_resolver.py](../converter/resolvers/program_kind_resolver.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
