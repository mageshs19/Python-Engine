# `patterns/db2_date_patterns.py`

Source: [patterns/db2_date_patterns.py](../../../patterns/db2_date_patterns.py) | 197 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b70843750c589b8051dc19f3621cfd00b4da9dd39e978cd0a2cabb924b5935c0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date comparison regex patterns.

## Module-level bindings

`WORKING_STORAGE_SECTION_PATTERN` (L52), `LINKAGE_SECTION_PATTERN` (L57), `PROCEDURE_DIVISION_PATTERN` (L62), `IF_START_PATTERN` (L72), `CONDITION_CONTINUATION_PATTERN` (L79), `STATEMENT_START_PATTERN` (L85), `TRAILING_BOOLEAN_PATTERN` (L95), `DB2_DATE_HOST_OPERAND_PATTERN` (L108), `SQL_HOST_OPERAND_PATTERN` (L116), `COMPARISON_OPERATOR_PATTERN` (L123), `EXEC_SQL_START_PATTERN` (L131), `END_EXEC_PATTERN` (L136), `DATE_HELPER_FIELD_PATTERN` (L144), `DATE_WORKING_STORAGE_MARKER_PATTERN` (L149), `DB2_SHARED_DATE_HELPER_USAGE_PATTERN` (L154), `DB2_DATE_WORKING_STORAGE_BASE_PATTERN` (L159), `DB2_DATE_COMPARISON_PATTERN` (L169), `__all__` (L179)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/db2_date_condition_assembler.py](../converter/composers/db2_date_condition_assembler.md)
- [converter/composers/db2_date_field_detector.py](../converter/composers/db2_date_field_detector.md)
- [converter/composers/db2_date_working_storage_manager.py](../converter/composers/db2_date_working_storage_manager.md)
- [converter/postprocess/storage_include/storage_ws_injector.py](../converter/postprocess/storage_include/storage_ws_injector.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
