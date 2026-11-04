# `patterns/cursor_paragraph_patterns.py`

Source: [patterns/cursor_paragraph_patterns.py](../../../patterns/cursor_paragraph_patterns.py) | 63 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `d98ccfd6413b4716c43ab92dc004bf6c12038f5b7d90259a890bc72283f53161`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor paragraph regex patterns.

## Module-level bindings

`UNNUMBERED_PERFORM_PATTERN_TEMPLATE` (L20), `NUMBERED_PERFORM_PATTERN_TEMPLATE` (L28), `LEGACY_PERFORM_PATTERN_TEMPLATE` (L36), `PERFORM_REPLACEMENT_TEMPLATE` (L44), `LEGACY_SQL_ERROR_PERFORM_PATTERN` (L51), `LEGACY_SQL_ERROR_HEADER_PATTERN` (L58), `LEGACY_SQL_ERROR_HEADER_REPLACEMENT` (L63)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_perform_rewriter.py](../converter/generators/cursor_paragraph/cursor_perform_rewriter.md)
- [converter/generators/sql_error_generator.py](../converter/generators/sql_error_generator.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
