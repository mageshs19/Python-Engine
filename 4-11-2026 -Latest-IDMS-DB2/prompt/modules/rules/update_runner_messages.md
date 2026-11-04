# `rules/update_runner_messages.py`

Source: [rules/update_runner_messages.py](../../../rules/update_runner_messages.py) | 122 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `ed410ba6e3b78ca654103f74e909733dd91761ddbf84f1d3708e149d889d7b3c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`LABEL_MAPPING_SHEET` (L6), `LABEL_DCLGEN_FOLDER` (L7), `LABEL_UPDATE_PROGRAM` (L8), `LABEL_SHEET_MAPPING` (L9), `LABEL_DCLGEN_TEMPLATE` (L10), `LABEL_COPYBOOK_TEMPLATE` (L11), `LABEL_UPDATE_PROGRAM_TEMPLATE` (L12), `FILE_NOT_FOUND_TEMPLATE` (L15), `PATH_NOT_FILE_TEMPLATE` (L16), `FOLDER_NOT_FOUND_TEMPLATE` (L17), `PATH_NOT_FOLDER_TEMPLATE` (L18), `NO_MAPPING_FILE_TEMPLATE` (L19), `NO_PROGRAM_FILE_TEMPLATE` (L20), `MULTIPLE_MAPPING_TEMPLATE` (L21), `NO_DCLGEN_CANDIDATE_TEMPLATE` (L25), `DIAG_START_LOAD_INPUTS` (L31), `DIAG_MAPPING_FOLDER_TEMPLATE` (L32), `DIAG_MAPPING_SELECTED_TEMPLATE` (L33), `DIAG_MAPPING_ROWS_TEMPLATE` (L34), `DIAG_DCLGEN_FOLDER_TEMPLATE` (L35), `DIAG_DCLGEN_FILE_COUNT_TEMPLATE` (L36), `DIAG_DCLGEN_FILE_TEMPLATE` (L37), `DIAG_DCLGEN_TEXT_LEN_TEMPLATE` (L38), `DIAG_DCLGEN_TOTAL_COLUMNS_TEMPLATE` (L39), `DIAG_COPYBOOK_FILE_COUNT_TEMPLATE` (L40), `DIAG_COPYBOOK_FILE_TEMPLATE` (L41), `DIAG_COPYBOOK_TEXT_LEN_TEMPLATE` (L42), `DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE` (L43), `COPYBOOK_SOURCE_LABEL` (L45), `DCLGEN_SOURCE_LABEL_TEMPLATE` (L46), `LOG_MAPPING_SELECTED` (L49), `LOG_MAPPING_ROWS` (L50), `LOG_DCLGEN_FILE_COUNT` (L51), `LOG_DCLGEN_FILE` (L52), `LOG_DCLGEN_TEXT_LEN` (L53), `LOG_DCLGEN_TOTAL_COLUMNS` (L54), `LOG_COPYBOOK_FILE_COUNT` (L55), `LOG_COPYBOOK_FILE` (L56), `LOG_COPYBOOK_TEXT_LEN` (L57), `LOG_COPYBOOK_TOTAL_FIELDS` (L58), `DIAG_SOURCE_FILE_TEMPLATE` (L61), `DIAG_SOURCE_LEN_TEMPLATE` (L62), `DIAG_DERIVED_PROGRAM_ID_TEMPLATE` (L63), `LOG_SOURCE_FILE` (L65), `LOG_SOURCE_LEN` (L66), `LOG_DERIVED_PROGRAM_ID` (L67), `LOG_GENERATION_COMPLETED` (L68), `LOG_OUTPUT_CREATED` (L69), `PRESERVE_SOURCE_LABEL` (L71), `DIAG_UPDATE_ENHANCEMENT_DONE` (L74), `LOG_UPDATE_ENHANCEMENT_DONE` (L75), `DIAG_UPDATE_AUDIT_MOVES` (L76), `DIAG_UPDATE_SKIPPED_TEMPLATE` (L80), `PRINT_GENERATION_COMPLETED` (L86), `PRINT_INPUT_PROGRAM_TEMPLATE` (L87), `PRINT_OUTPUT_CREATED_TEMPLATE` (L88), `HEADER_INPUT_SUMMARY` (L90), `HEADER_SELECTED_INPUT_FILES` (L91), `HEADER_VALIDATION_MESSAGES` (L92), `HEADER_DIAGNOSTICS` (L93), `HEADER_UPDATE_BATCH_SUMMARY` (L94), `RULE_INPUT_SUMMARY` (L96), `RULE_SELECTED_INPUT_FILES` (L97), `RULE_VALIDATION_MESSAGES` (L98), `RULE_DIAGNOSTICS` (L99), `RULE_UPDATE_BATCH_SUMMARY` (L100), `SUMMARY_PROJECT_ROOT_TEMPLATE` (L102), `SUMMARY_SRC_DIR_TEMPLATE` (L103), `SUMMARY_SHEET_ROWS_TEMPLATE` (L104), `SUMMARY_DCLGEN_COLUMNS_TEMPLATE` (L105), `SUMMARY_COPYBOOK_FIELDS_TEMPLATE` (L106), `SUMMARY_COBOL_LEN_TEMPLATE` (L107), `SUMMARY_TARGET_PROGRAM_ID_TEMPLATE` (L108), `SELECTED_SHEET_MAPPING_TEMPLATE` (L110), `SELECTED_COBOL_SOURCE_TEMPLATE` (L111), `SELECTED_DCLGEN_HEADER` (L112), `SELECTED_COPYBOOK_HEADER` (L113), `SELECTED_COPYBOOK_NONE` (L114), `SELECTED_PATH_BULLET_TEMPLATE` (L115), `BATCH_PROGRAM_FOLDER_TEMPLATE` (L117), `BATCH_PROGRAM_COUNT_TEMPLATE` (L118), `BATCH_OUTPUT_FOLDER_TEMPLATE` (L119), `NO_VALIDATION_MESSAGES` (L121), `BULLET_TEMPLATE` (L122)

## Import declarations

```python
from __future__ import annotations
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/run_update.py](../runners/run_update.md)
- [runners/update/update_input_loader.py](../runners/update/update_input_loader.md)
- [runners/update/update_input_selector.py](../runners/update/update_input_selector.md)
- [runners/update/update_postprocess_pipeline.py](../runners/update/update_postprocess_pipeline.md)
- [runners/update/update_program_converter.py](../runners/update/update_program_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
