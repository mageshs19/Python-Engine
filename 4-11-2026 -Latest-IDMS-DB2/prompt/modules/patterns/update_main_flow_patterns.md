# `patterns/update_main_flow_patterns.py`

Source: [patterns/update_main_flow_patterns.py](../../../patterns/update_main_flow_patterns.py) | 66 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b03f45d6f42fd9f34136abe85fc758be20c354b99fcb15356307a32d382b93b0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`OPEN_INPUT_LINE_PATTERN` (L13), `STOP_RUN_LINE_PATTERN` (L18), `PROCEDURE_DIVISION_LINE_PATTERN` (L23), `DIVISION_LINE_PATTERN` (L28), `SECTION_LINE_PATTERN` (L33), `PARAGRAPH_HEADER_LINE_PATTERN` (L38), `PERFORM_UNTIL_LINE_PATTERN` (L43), `PERFORM_READ_FLAT_FILE_LINE_PATTERN` (L48), `EXEC_SQL_LINE_PATTERN` (L53), `MOVE_LINE_PATTERN` (L58), `PERFORM_LINE_PATTERN` (L63)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/main_flow/main_flow_locators.py](../converter/postprocess/main_flow/main_flow_locators.md)
- [converter/postprocess/main_flow/main_flow_paragraph_resolver.py](../converter/postprocess/main_flow/main_flow_paragraph_resolver.md)
- [converter/postprocess/update_business_sql_standardizer.py](../converter/postprocess/update_business_sql_standardizer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
