# `rules/retrieval_runner_messages.py`

Source: [rules/retrieval_runner_messages.py](../../../rules/retrieval_runner_messages.py) | 108 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `f2aaae5c26eaaf32bd80639c407cbfe08d9029c443ab3f4eea02840b4c804cbb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`LABEL_MAPPING_SHEET` (L9), `LABEL_SHEET_MAPPING` (L10), `LABEL_RETRIEVAL_PROGRAM` (L11), `LABEL_DCLGEN_TEMPLATE` (L12), `LABEL_COPYBOOK_TEMPLATE` (L13), `LABEL_RETRIEVAL_PROGRAM_TEMPLATE` (L14), `FILE_NOT_FOUND_TEMPLATE` (L17), `PATH_NOT_FILE_TEMPLATE` (L18), `FOLDER_NOT_FOUND_TEMPLATE` (L19), `PATH_NOT_FOLDER_TEMPLATE` (L20), `NO_MAPPING_FILE_TEMPLATE` (L21), `NO_PROGRAM_FILE_TEMPLATE` (L22), `NO_DCLGEN_CANDIDATE_TEMPLATE` (L23), `DIAG_START_LOAD_INPUTS` (L29), `DIAG_MAPPING_FOLDER_TEMPLATE` (L30), `DIAG_MAPPING_SELECTED_TEMPLATE` (L31), `DIAG_MAPPING_ROWS_TEMPLATE` (L32), `DIAG_DCLGEN_FILE_COUNT_TEMPLATE` (L33), `DIAG_DCLGEN_FILE_TEMPLATE` (L34), `DIAG_DCLGEN_TEXT_LEN_TEMPLATE` (L35), `DIAG_DCLGEN_TOTAL_COLUMNS_TEMPLATE` (L36), `DIAG_COPYBOOK_FILE_COUNT_TEMPLATE` (L37), `DIAG_COPYBOOK_FILE_TEMPLATE` (L38), `DIAG_COPYBOOK_TEXT_LEN_TEMPLATE` (L39), `DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE` (L40), `COPYBOOK_SOURCE_LABEL` (L43), `DCLGEN_SOURCE_LABEL_TEMPLATE` (L44), `LOG_MAPPING_SELECTED` (L47), `LOG_MAPPING_ROWS` (L48), `LOG_DCLGEN_FILE_COUNT` (L49), `LOG_DCLGEN_FILE` (L50), `LOG_DCLGEN_TEXT_LEN` (L51), `LOG_DCLGEN_TOTAL_COLUMNS` (L52), `LOG_COPYBOOK_FILE_COUNT` (L53), `LOG_COPYBOOK_FILE` (L54), `LOG_COPYBOOK_TEXT_LEN` (L55), `LOG_COPYBOOK_TOTAL_FIELDS` (L56), `DIAG_SOURCE_FILE_TEMPLATE` (L59), `DIAG_SOURCE_LEN_TEMPLATE` (L60), `DIAG_DERIVED_PROGRAM_ID_TEMPLATE` (L61), `LOG_SOURCE_FILE` (L63), `LOG_SOURCE_LEN` (L64), `LOG_DERIVED_PROGRAM_ID` (L65), `LOG_GENERATION_COMPLETED` (L66), `LOG_OUTPUT_CREATED` (L67), `PRESERVE_SOURCE_LABEL` (L69), `PRINT_GENERATION_COMPLETED` (L72), `PRINT_INPUT_PROGRAM_TEMPLATE` (L73), `PRINT_OUTPUT_CREATED_TEMPLATE` (L74), `HEADER_INPUT_SUMMARY` (L76), `HEADER_SELECTED_INPUT_FILES` (L77), `HEADER_VALIDATION_MESSAGES` (L78), `HEADER_DIAGNOSTICS` (L79), `HEADER_RETRIEVAL_BATCH_SUMMARY` (L80), `RULE_INPUT_SUMMARY` (L82), `RULE_SELECTED_INPUT_FILES` (L83), `RULE_VALIDATION_MESSAGES` (L84), `RULE_DIAGNOSTICS` (L85), `RULE_RETRIEVAL_BATCH_SUMMARY` (L86), `SUMMARY_PROJECT_ROOT_TEMPLATE` (L88), `SUMMARY_SRC_DIR_TEMPLATE` (L89), `SUMMARY_SHEET_ROWS_TEMPLATE` (L90), `SUMMARY_DCLGEN_COLUMNS_TEMPLATE` (L91), `SUMMARY_COPYBOOK_FIELDS_TEMPLATE` (L92), `SUMMARY_COBOL_LEN_TEMPLATE` (L93), `SUMMARY_TARGET_PROGRAM_ID_TEMPLATE` (L94), `SELECTED_SHEET_MAPPING_TEMPLATE` (L96), `SELECTED_COBOL_SOURCE_TEMPLATE` (L97), `SELECTED_DCLGEN_HEADER` (L98), `SELECTED_COPYBOOK_HEADER` (L99), `SELECTED_COPYBOOK_NONE` (L100), `SELECTED_PATH_BULLET_TEMPLATE` (L101), `BATCH_PROGRAM_FOLDER_TEMPLATE` (L103), `BATCH_PROGRAM_COUNT_TEMPLATE` (L104), `BATCH_OUTPUT_FOLDER_TEMPLATE` (L105), `NO_VALIDATION_MESSAGES` (L107), `BULLET_TEMPLATE` (L108)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/convert_programs.py](../runners/convert_programs.md)
- [runners/retrieval/retrieval_input_loader.py](../runners/retrieval/retrieval_input_loader.md)
- [runners/retrieval/retrieval_input_selector.py](../runners/retrieval/retrieval_input_selector.md)
- [runners/retrieval/retrieval_program_converter.py](../runners/retrieval/retrieval_program_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
