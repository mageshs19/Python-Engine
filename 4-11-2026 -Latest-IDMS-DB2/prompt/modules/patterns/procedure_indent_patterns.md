# `patterns/procedure_indent_patterns.py`

Source: [patterns/procedure_indent_patterns.py](../../../patterns/procedure_indent_patterns.py) | 104 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `f86d5470592074c85e7dd282590cf90cfcfe15202a01d374a9f5c9753c6f683f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Procedure Division indentation regex patterns.

## Module-level bindings

`PROCEDURE_DIVISION_PATTERN` (L20), `OTHER_DIVISION_PATTERN` (L25), `SECTION_HEADER_PATTERN` (L30), `PARAGRAPH_HEADER_PATTERN` (L35), `IF_START_PATTERN` (L43), `ELSE_PATTERN` (L48), `EVALUATE_START_PATTERN` (L53), `WHEN_PATTERN` (L58), `INLINE_PERFORM_PATTERN` (L65), `SCOPED_OPENER_PATTERN` (L73), `SCOPE_TERMINATOR_PATTERN` (L81), `EXEC_SQL_START_PATTERN` (L89), `END_EXEC_PATTERN` (L94), `LONE_PERIOD_PATTERN` (L102)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/procedure_indent/indent_models.py](../converter/composers/procedure_indent/indent_models.md)
- [converter/composers/procedure_indent/indent_resolver.py](../converter/composers/procedure_indent/indent_resolver.md)
- [converter/composers/procedure_indent_normalizer.py](../converter/composers/procedure_indent_normalizer.md)
- [tests/test_qualifier_connector_wrap.py](../tests/test_qualifier_connector_wrap.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
