# `patterns/fixed_format_wrap_patterns.py`

Source: [patterns/fixed_format_wrap_patterns.py](../../../patterns/fixed_format_wrap_patterns.py) | 26 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `057d7d0e9738b88dc6308448b33df62a88c3d966f0f34d70513a803ba2f37951`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format wrapping regex. Patterns only.

## Module-level bindings

`MOVE_TO_PATTERN` (L11), `PARAGRAPH_HEADER_PATTERN` (L17), `DIVISION_OR_SECTION_PATTERN` (L23)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/fixed_format_statement_wrapper.py](../converter/services/fixed_format_statement_wrapper.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
