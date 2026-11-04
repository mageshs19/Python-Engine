# `patterns/update_final_feedback_patterns.py`

Source: [patterns/update_final_feedback_patterns.py](../../../patterns/update_final_feedback_patterns.py) | 98 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `c9b407c0067b1c1020e128284b83fdc12c4f0b92139614800af77457764d2f26`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Update final feedback regex patterns.

## Module-level bindings

`EXEC_SQL_START_PATTERN` (L17), `EXEC_SQL_END_PATTERN` (L22), `UPDATE_STATEMENT_PATTERN` (L27), `FROM_STATEMENT_PATTERN` (L32), `SET_KEYWORD_PATTERN` (L37), `WHERE_KEYWORD_PATTERN` (L42), `SQL_SET_ASSIGNMENT_PATTERN` (L47), `NON_SQL_DCL_DOT_REFERENCE_PATTERN` (L55), `DCLGEN_OF_REFERENCE_PATTERN` (L61), `MOVE_TO_DCL_OF_REFERENCE_PATTERN` (L67), `MOVE_TO_BARE_RECORD_PATTERN` (L74), `INITIALIZE_DCL_PATTERN` (L80), `SQL_LOCATION_DB_OPERATION_PATTERN` (L85), `CONVERTED_DB2_OPERATION_COMMENT_PATTERN` (L91)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/update_audit_move_inserter.py](../converter/services/update_audit_move_inserter.md)
- [converter/services/update_cobol_reference_cleanup.py](../converter/services/update_cobol_reference_cleanup.md)
- [converter/services/update_diagnostic_label_normalizer.py](../converter/services/update_diagnostic_label_normalizer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
