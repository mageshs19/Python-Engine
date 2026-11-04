# `patterns/output_write_paragraph_patterns.py`

Source: [patterns/output_write_paragraph_patterns.py](../../../patterns/output_write_paragraph_patterns.py) | 56 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `5f3280b845f2264fc7ab09a06786b8f6fdec3cce2b4e0b4f979bb9b8b5f9c47a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Output write paragraph extraction regex patterns.

## Module-level bindings

`PARAGRAPH_HEADER_PATTERN` (L18), `PROCEDURE_DIVISION_PATTERN` (L23), `DIVISION_PATTERN` (L28), `IF_START_PATTERN` (L34), `END_IF_PATTERN` (L39), `WRITE_STATEMENT_PATTERN` (L46), `PERFORM_WRITE_PARAGRAPH_PATTERN` (L53)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/output_write_guard.py](../converter/composers/output_write/output_write_guard.md)
- [converter/composers/output_write/output_write_line_utils.py](../converter/composers/output_write/output_write_line_utils.md)
- [converter/composers/output_write/output_write_scanner.py](../converter/composers/output_write/output_write_scanner.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
