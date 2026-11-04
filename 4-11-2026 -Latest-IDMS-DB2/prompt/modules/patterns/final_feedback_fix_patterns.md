# `patterns/final_feedback_fix_patterns.py`

Source: [patterns/final_feedback_fix_patterns.py](../../../patterns/final_feedback_fix_patterns.py) | 178 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `66ff5b0148be0f6923d16c8c82921f43f074115293f2512e04cbf8186ce1782a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Final feedback fix regex patterns.

## Module-level bindings

`PROGRAM_ID_PATTERN` (L16), `MOVE_TO_PROGRAM_NAME_PATTERN` (L22), `PROCEDURE_DIVISION_TOKEN_PATTERN` (L29), `DIVISION_SECTION_HEADER_PATTERN` (L34), `PARAGRAPH_HEADER_PATTERN` (L45), `EXEC_SQL_START_PATTERN` (L50), `END_EXEC_PATTERN` (L55), `DECLARE_CURSOR_PATTERN` (L60), `FETCH_CURSOR_PATTERN` (L65), `SELECT_KEYWORD_PATTERN` (L70), `SELECT_ITEM_PATTERN` (L75), `FROM_PATTERN` (L80), `WHERE_PATTERN` (L85), `ORDER_BY_PATTERN` (L90), `FOR_READ_ONLY_PATTERN` (L95), `HOST_REFERENCE_PATTERN` (L100), `ASC_DESC_PATTERN` (L105), `SQL_NAME_TOKEN_PATTERN` (L110), `DATE_HELPER_EUR_PATTERN` (L115), `DATE_LOW_EUR_LITERAL_PATTERN` (L120), `DATE_HIGH_EUR_LITERAL_PATTERN` (L125), `STRING_START_PATTERN` (L132), `STRING_END_PATTERN` (L133), `STRING_INTO_PATTERN` (L134), `PROCEDURE_DIVISION_PATTERN` (L136), `DIVISION_PATTERN` (L139), `SECTION_PATTERN` (L142), `PARAGRAPH_PATTERN` (L145), `EXEC_SQL_END_LINE_PATTERN` (L152), `IF_START_PATTERN` (L154), `ELSE_PATTERN` (L155), `END_IF_PATTERN` (L156), `EVALUATE_START_PATTERN` (L157), `WHEN_PATTERN` (L158), `END_EVALUATE_PATTERN` (L159), `DB2_COLON_COMMENT_BODY_PATTERN` (L161), `DB2_SPACE_COMMENT_BODY_PATTERN` (L162), `COBOL_LITERAL_PATTERN` (L167), `VM_BD_TOKEN_PATTERN` (L175)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (12)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cobol_area_alignment_classifier.py](../converter/services/cobol_area_alignment_classifier.md)
- [converter/services/cobol_area_alignment_service.py](../converter/services/cobol_area_alignment_service.md)
- [converter/services/cursor_select_column_parser.py](../converter/services/cursor_select_column_parser.md)
- [converter/services/cursor_select_fetch_rewriter.py](../converter/services/cursor_select_fetch_rewriter.md)
- [converter/services/cursor_sql_block_scanner.py](../converter/services/cursor_sql_block_scanner.md)
- [converter/services/db2_comment_readability_service.py](../converter/services/db2_comment_readability_service.md)
- [converter/services/db2_date_format_service.py](../converter/services/db2_date_format_service.md)
- [converter/services/procedure_block_indent_service.py](../converter/services/procedure_block_indent_service.md)
- [converter/services/program_name_sync_service.py](../converter/services/program_name_sync_service.md)
- [converter/services/string_block_format_service.py](../converter/services/string_block_format_service.md)
- [converter/transformers/cobol_program_id_transformer.py](../converter/transformers/cobol_program_id_transformer.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
