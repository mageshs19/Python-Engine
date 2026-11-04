# `patterns/counter_declaration_patterns.py`

Source: [patterns/counter_declaration_patterns.py](../../../patterns/counter_declaration_patterns.py) | 54 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `d66ef3bc50058894620efb86e8e242d8b7ea2610d774498c3416c8cc670d6371`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Counter declaration regex patterns.

## Module-level bindings

`COUNTER_INCREMENT_PATTERN` (L18), `DATA_ENTRY_PATTERN` (L24), `GROUP_HEADER_PATTERN` (L30), `SUBORDINATE_ENTRY_PATTERN` (L36), `WORKING_STORAGE_PATTERN` (L41), `SECTION_OR_DIVISION_PATTERN` (L46), `STOP_RUN_PATTERN` (L51)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/counter_anchor.py](../converter/composers/counter_declaration/counter_anchor.md)
- [converter/composers/counter_declaration_composer.py](../converter/composers/counter_declaration_composer.md)
- [converter/composers/counter_declaration_writer.py](../converter/composers/counter_declaration_writer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
