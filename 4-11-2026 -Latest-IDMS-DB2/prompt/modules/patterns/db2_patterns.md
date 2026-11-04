# `patterns/db2_patterns.py`

Source: [patterns/db2_patterns.py](../../../patterns/db2_patterns.py) | 163 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `38e067e2fee32c16aa901babc72479152a78d58bd6c0a30df8bd7aa7736a3741`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 infrastructure and generated block regex patterns.

## Module-level bindings

`SQLCA_TOKEN_PATTERN` (L15), `SQLERRWS_TOKEN_PATTERN` (L20), `SQL_LOCATION_PATTERN` (L25), `SQL_ERROR_PARAGRAPH_PATTERN` (L30), `SQL_ERROR_PERFORM_PATTERN` (L35), `DB2_CURSOR_BLOCK_MARKER_PATTERN` (L40), `DB2_INFRASTRUCTURE_MARKER_PATTERN` (L45), `DB2_CURSOR_DECLARATIONS_MARKER_PATTERN` (L50), `DB2_CURSOR_FLAGS_MARKER_PATTERN` (L55), `DB2_SQL_ERROR_LOCATION_MARKER_PATTERN` (L60), `PROCEDURE_DIVISION_PATTERN` (L65), `LINKAGE_SECTION_PATTERN` (L70), `WORKING_STORAGE_PATTERN` (L75), `DATA_DIVISION_PATTERN` (L80), `END_PROGRAM_PATTERN` (L85), `EXEC_SQL_START_PATTERN` (L90), `EXEC_SQL_END_PATTERN` (L95), `SQL_INCLUDE_PATTERN` (L100), `SQLCA_INCLUDE_PATTERN` (L105), `SQLERRWS_INCLUDE_PATTERN` (L110), `DECLARE_CURSOR_PATTERN` (L115), `OPEN_CURSOR_PATTERN` (L120), `FETCH_CURSOR_PATTERN` (L125), `CLOSE_CURSOR_PATTERN` (L130), `SQLCODE_PATTERN` (L135), `SQLCODE_SUCCESS_PATTERN` (L140), `SQLCODE_NOT_FOUND_PATTERN` (L145), `SQLCODE_ERROR_PATTERN` (L150), `COMMIT_PATTERN` (L155), `ROLLBACK_PATTERN` (L160)

## Import declarations

```python
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/manual_layout_composer.py](../converter/composers/manual_layout_composer.md)
- [converter/generators/cursor_paragraph_generator.py](../converter/generators/cursor_paragraph_generator.md)
- [converter/generators/sql_error_generator.py](../converter/generators/sql_error_generator.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
