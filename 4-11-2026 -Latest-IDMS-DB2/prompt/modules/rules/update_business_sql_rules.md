# `rules/update_business_sql_rules.py`

Source: [rules/update_business_sql_rules.py](../../../rules/update_business_sql_rules.py) | 91 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `6230a1f8d06a47f007154a7f54869b12b50b5ea71f920c3a1a3d04a23fbc7ef2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`FIXED_BODY_WIDTH` (L7), `UPDATE_SQL_SEQUENCE_AREA_WIDTH` (L8), `UPDATE_SQL_INDICATOR_COLUMN` (L9), `UPDATE_SQL_BODY_START_COLUMN` (L10), `UPDATE_SQL_BODY_END_COLUMN` (L11), `UPDATE_SQL_FULL_LINE_WIDTH` (L12), `UPDATE_SQL_TOTAL_LINE_WIDTH` (L13), `UPDATE_SQL_RIGHT_SEQUENCE_WIDTH` (L14), `UPDATE_SQL_AREA_B_INDENT` (L17), `UPDATE_SQL_SQL_BODY_INDENT` (L18), `NESTED_INDENT` (L19), `WHEN_INDENT` (L20), `COMMENT_INDICATORS` (L23), `ACTIVE_INDICATOR` (L24), `TOKEN_IF` (L27), `TOKEN_PERFORM` (L28), `TOKEN_WHEN` (L29), `TOKEN_END_IF` (L30), `TOKEN_INITIALIZE_DCL` (L31), `TOKEN_INITIALIZE` (L32), `TOKEN_EXEC_SQL` (L33), `TOKEN_END_EXEC` (L34), `TOKEN_EVALUATE_SQLCODE` (L35), `TOKEN_END_EVALUATE` (L36), `TOKEN_STAR` (L37), `READ_FLAT_FILE_PARAGRAPH` (L40), `SQL_ERROR_PARAGRAPH_NAMES` (L41), `SQL_ERROR_ROUTINE_MARKER` (L42), `PERFORM_TEMPLATE` (L45), `COMMIT_CHECK_IF_TEMPLATE` (L46), `COMMIT_CHECK_PERFORM_TEMPLATE` (L47), `END_IF_STATEMENT` (L48), `ADD_UPDATE_COUNTER_TEMPLATE` (L49), `INITIALIZE_DCL_GROUP_TEMPLATE` (L50), `FINAL_PERIOD_LINE` (L51), `LONE_PERIOD` (L52), `DIAG_PROCESS_PARAGRAPH_UNRESOLVED` (L55), `DIAG_PROCESS_PARAGRAPH_NOT_FOUND_TEMPLATE` (L59), `ENABLE_STRUCTURAL_UPDATE_DETECTION` (L64), `UPDATE_VERB_LOOKAHEAD` (L67), `DCLGEN_GROUP_PREFIX` (L71), `DCLGEN_GROUP_SUFFIXES` (L72), `ENSURE_UPDATE_COUNTER_DECLARED` (L74), `UPDATE_COUNTER_PICTURE` (L78), `UPDATE_COUNTER_DIAGNOSTICS` (L80)

## Import declarations

```python
from __future__ import annotations
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_business_sql/update_business_sql_line_renderer.py](../converter/postprocess/update_business_sql/update_business_sql_line_renderer.md)
- [converter/postprocess/update_business_sql/update_counter_declarer.py](../converter/postprocess/update_business_sql/update_counter_declarer.md)
- [converter/postprocess/update_business_sql/update_paragraph_normalizer.py](../converter/postprocess/update_business_sql/update_paragraph_normalizer.md)
- [converter/postprocess/update_business_sql/update_sql_block_extractor.py](../converter/postprocess/update_business_sql/update_sql_block_extractor.md)
- [converter/postprocess/update_business_sql_standardizer.py](../converter/postprocess/update_business_sql_standardizer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
