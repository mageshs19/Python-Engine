# `patterns/update_storage_include_patterns.py`

Source: [patterns/update_storage_include_patterns.py](../../../patterns/update_storage_include_patterns.py) | 88 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a9330954413326f1aeb59063f4b12b688229402d7f290493f5f0ecd8bcc918a6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`PROGRAM_NAME_MOVE_PATTERN` (L13), `CS_PROGRAM_01_PATTERN` (L18), `DCL_HOST_REFERENCE_PATTERN` (L24), `EXEC_SQL_INCLUDE_PATTERN` (L29), `LEGACY_77_DECLARATION_PATTERN_TEMPLATE` (L34), `WORKING_STORAGE_SECTION_LINE_PATTERN` (L38), `LINKAGE_SECTION_LINE_PATTERN` (L43), `PROCEDURE_DIVISION_LINE_PATTERN` (L48), `LEGACY_ABEND_MARKER_LITERAL_PREFIX` (L63), `LEGACY_ABEND_MARKER_77_ONELINE_PATTERN` (L67), `LEGACY_ABEND_MARKER_VALUE_LINE_PATTERN` (L72), `LEGACY_ABEND_MARKER_77_HEADER_NO_VALUE_PATTERN` (L76), `LEGACY_ABEND_MARKER_77_HEADER_NAMED_PATTERN` (L80), `CS_PROGRAM_DECLARATION_PATTERN` (L85)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/storage_include/storage_include_injector.py](../converter/postprocess/storage_include/storage_include_injector.md)
- [converter/postprocess/storage_include/storage_ws_injector.py](../converter/postprocess/storage_include/storage_ws_injector.md)
- [converter/postprocess/update_storage_include_manager.py](../converter/postprocess/update_storage_include_manager.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
