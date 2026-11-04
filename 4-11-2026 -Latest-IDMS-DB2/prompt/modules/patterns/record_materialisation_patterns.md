# `patterns/record_materialisation_patterns.py`

Source: [patterns/record_materialisation_patterns.py](../../../patterns/record_materialisation_patterns.py) | 124 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `65cc2b4c6c1a4a84ae659f81bc4913a9e6813eaf8dca1a126eb910474c457970`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for IDMS record materialisation. Regex only.

## Module-level bindings

`_NAME` (L9), `WHOLE_RECORD_MOVE_PATTERN` (L12), `TARGET_FIELD_PATTERN_TEMPLATE` (L18), `COBOL_ZONE_PATTERN` (L24), `COBOL_ZONE_REDEFINES_PATTERN` (L30), `PICTURE_PATTERN` (L37), `PICTURE_REPEAT_PATTERN` (L45), `WORKING_STORAGE_PATTERN` (L47), `PROCEDURE_DIVISION_PATTERN` (L50), `PICTURE_SYMBOL_PATTERN` (L65), `PICTURE_CLAUSE_PATTERN` (L71), `PICTURE_SYMBOL_REPEAT_PATTERN` (L96), `PICTURE_AFTER_KEYWORD_PATTERN` (L109), `USAGE_CLAUSE_PATTERN` (L119)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_move_scanner.py](../converter/composers/record_materialisation/record_move_scanner.md)
- [converter/composers/record_materialisation/record_row_reader.py](../converter/composers/record_materialisation/record_row_reader.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py](../converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
