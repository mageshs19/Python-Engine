# `patterns/update_restart_patterns.py`

Source: [patterns/update_restart_patterns.py](../../../patterns/update_restart_patterns.py) | 101 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `d4dd4814368222140693387377ee6a0ea06ddf5844d7114166e015ead140bc08`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`WORKING_STORAGE_SECTION_PATTERN` (L6), `LINKAGE_SECTION_PATTERN` (L11), `PROCEDURE_DIVISION_PATTERN` (L16), `END_PROGRAM_PATTERN` (L21), `READ_FLAT_FILE_HEADER_PATTERN` (L26), `PARAGRAPH_HEADER_PATTERN` (L31), `COPY_INCLUDE_TOKEN_PATTERN_TEMPLATE` (L36), `EXEC_SQL_INCLUDE_TOKEN_PATTERN_TEMPLATE` (L38), `MALFORMED_SQLERROR_END_EVALUATE_PATTERN` (L42), `RESTART_COMMENT_PATTERN` (L47), `OLD_RESTART_IF_PATTERN` (L52), `OLD_PREREAD_IF_EOF_PATTERN` (L57), `OLD_PERFORM_UNTIL_EOF_PATTERN` (L62), `MOVE_TO_RESTART_FAMILY_PATTERN` (L68), `FFRECAB_REFERENCE_PATTERN` (L73), `EXEC_SQL_START_PATTERN` (L78), `END_EXEC_PATTERN` (L83), `EVALUATE_SQLCODE_PATTERN` (L88), `END_EVALUATE_PATTERN` (L93), `STOP_RUN_PATTERN` (L98)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/storage_include/storage_ws_injector.py](../converter/postprocess/storage_include/storage_ws_injector.md)
- [converter/postprocess/update_postprocess_line_utils.py](../converter/postprocess/update_postprocess_line_utils.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
