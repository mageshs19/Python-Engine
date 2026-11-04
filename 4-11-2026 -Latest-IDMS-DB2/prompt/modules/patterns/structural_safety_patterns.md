# `patterns/structural_safety_patterns.py`

Source: [patterns/structural_safety_patterns.py](../../../patterns/structural_safety_patterns.py) | 100 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `3fffbe40341ba6cf07cd610de3d587849857f75f51933ae9e044f1ffef0380f5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for the structural safety passes. Regex only.

## Module-level bindings

`_DATA_NAME` (L26), `_PARAGRAPH_NAME` (L29), `IF_START_PATTERN` (L32), `END_IF_PATTERN` (L33), `LEVEL_01_PATTERN` (L36), `SUBORDINATE_LEVEL_PATTERN` (L40), `FD_PATTERN` (L44), `FILE_SECTION_PATTERN` (L45), `WORKING_STORAGE_PATTERN` (L48), `LINKAGE_SECTION_PATTERN` (L51), `PROCEDURE_DIVISION_PATTERN` (L54), `RECORD_VERB_PATTERN` (L59), `WRITE_FROM_PATTERN` (L64), `READ_INTO_PATTERN` (L67), `MOVE_WHOLE_GROUP_PATTERN` (L70), `MOVE_BARE_SOURCE_PATTERN` (L77), `MOVE_BARE_TARGET_PATTERN` (L82), `QUALIFIER_PATTERN` (L87), `PARAGRAPH_HEADER_PATTERN` (L92), `SECTION_HEADER_PATTERN` (L95), `EXIT_STATEMENT_PATTERN` (L98)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/structural_safety_composer.py](../converter/composers/structural_safety_composer.md)
- [converter/services/cobol_condition_scanner.py](../converter/services/cobol_condition_scanner.md)
- [converter/services/working_storage_group_selector.py](../converter/services/working_storage_group_selector.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
