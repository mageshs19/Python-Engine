# `patterns/update_program_postprocess_patterns.py`

Source: [patterns/update_program_postprocess_patterns.py](../../../patterns/update_program_postprocess_patterns.py) | 84 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `35398603e3c3267a514171177c2447ea25cd9cecd970fbd60ba784c2da963d82`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex patterns for update-program postprocess conversion.

## Module-level bindings

`WORKING_STORAGE_SECTION_PATTERN` (L14), `LINKAGE_SECTION_PATTERN` (L19), `PROCEDURE_DIVISION_PATTERN` (L24), `END_PROGRAM_PATTERN` (L29), `READ_FLAT_FILE_HEADER_PATTERN` (L34), `PARAGRAPH_HEADER_PATTERN` (L39), `COPY_INCLUDE_TOKEN_PATTERN_TEMPLATE` (L44), `EXEC_SQL_INCLUDE_TOKEN_PATTERN_TEMPLATE` (L46), `MALFORMED_SQLERROR_END_EVALUATE_PATTERN` (L50), `OLD_EOF_EQUALS_Y_PATTERN` (L55), `MOVE_Y_TO_EOF_PATTERN` (L60), `MOVE_N_TO_EOF_PATTERN` (L65), `OPEN_INPUT_PATTERN` (L70), `PERFORM_UNTIL_EOF_PATTERN` (L75), `OLD_RESTART_RECORD_REFERENCE_PATTERN` (L81)

## Import declarations

```python
from __future__ import annotations
import re
```

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
