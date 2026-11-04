# `patterns/cobol_cleanup_patterns.py`

Source: [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.py) | 368 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `044d57e7eb79e95687dfe23f084e45fb41cf46022c60c20fc5418766408fd698`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL cleanup regex patterns.

## Module-level bindings

`EXEC_SQL_INCLUDE_PATTERN` (L10), `DCL_GROUP_PATTERN` (L15), `WORKING_STORAGE_PATTERN` (L20), `LINKAGE_SECTION_PATTERN` (L25), `ERROR_STATUS_MOVE_PATTERN` (L30), `WS_STATUS_PATTERN` (L35), `SW_STATUS_D_PIC_PATTERN` (L40), `SW_STATUS_D_MOVE_N_PATTERN` (L45), `FETCH_UNTIL_EOC_PATTERN` (L50), `FETCH_UNTIL_EOC_OR_SW_PATTERN` (L57), `FETCH_UNTIL_EOC_FULL_SW_PATTERN` (L64), `SW_STATUS_Y_CONTINUATION_PATTERN` (L72), `WRITE_PATTERN` (L77), `INITIALIZE_PATTERN` (L82), `MOVE_START_PATTERN` (L87), `MOVE_TO_OUTPUT_FIELD_PATTERN` (L92), `TO_OUTPUT_FIELD_PATTERN` (L97), `DB2_DATE_MOVE_START_PATTERN` (L102), `DB2_DATE_MOVE_ONE_LINE_PATTERN` (L108), `TO_UIT_DATE_FIELD_PATTERN` (L115), `FETCH_PARAGRAPH_NUMBER_PATTERN` (L120), `LONE_CONTINUE_PATTERN` (L133), `BLOCK_OPENER_PATTERN` (L139), `REMOVED_OBTAIN_CALC_COMMENT_PATTERN` (L149), `RESIDUAL_IDMS_COMMENT_CONTINUATION_PATTERN` (L165), `PARAGRAPH_HEADER_PATTERN` (L192), `SECTION_HEADER_PATTERN` (L197), `PROCEDURE_DIVISION_LINE_PATTERN` (L202), `IF_START_PATTERN` (L209), `END_IF_PATTERN` (L214), `WRITE_STATEMENT_PATTERN` (L219), `WHEN_ZERO_PATTERN` (L224), `PERFORM_CURSOR_PARAGRAPH_PATTERN` (L230), `PERFORM_CLOSE_CURSOR_PATTERN` (L236), `PERFORM_PARAGRAPH_PATTERN` (L243), `_NOISE_FRAGMENTS` (L258), `_TRACE_FRAGMENTS` (L276), `RESIDUAL_IDMS_COMMENT_PATTERN` (L282), `TRACE_MARKER_COMMENT_PATTERN` (L287), `GENERATED_DB2_NARRATION_COMMENT_PATTERN` (L296), `GENERATED_DB2_NARRATION_CONTINUATION_PATTERN` (L319), `__all__` (L328)

## Import declarations

```python
import re
```

## Importers (11)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](../converter/composers/cleanup/child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/cursor_nesting_analyser.py](../converter/composers/cleanup/cursor_nesting_analyser.md)
- [converter/composers/cleanup/db2_date_output_cleanup.py](../converter/composers/cleanup/db2_date_output_cleanup.md)
- [converter/composers/cleanup/error_status_flag_cleanup.py](../converter/composers/cleanup/error_status_flag_cleanup.md)
- [converter/composers/cleanup/initialize_before_output_cleanup.py](../converter/composers/cleanup/initialize_before_output_cleanup.md)
- [converter/composers/cleanup/output_write_placement_cleanup.py](../converter/composers/cleanup/output_write_placement_cleanup.md)
- [converter/composers/cleanup/paragraph_terminator_cleanup.py](../converter/composers/cleanup/paragraph_terminator_cleanup.md)
- [converter/composers/cleanup/residual_idms_comment_cleanup.py](../converter/composers/cleanup/residual_idms_comment_cleanup.md)
- [converter/composers/unnecessary_comments_cleanup_composer.py](../converter/composers/unnecessary_comments_cleanup_composer.md)
- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](../converter/composers/update_sql_cleanup/modify_update_rewriter.md)
- [converter/transformers/idms_residual_cleanup.py](../converter/transformers/idms_residual_cleanup.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
