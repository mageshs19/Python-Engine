# `rules/batch_runner_messages.py`

Source: [rules/batch_runner_messages.py](../../../rules/batch_runner_messages.py) | 86 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `44c11c01c0e19980ef5910eb97677abd863fff26cbbb8e302956a8ec4235982a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`FOLDER_NOT_FOUND_TEMPLATE` (L9), `PATH_NOT_FOLDER_TEMPLATE` (L10), `NO_PROGRAM_FILES_TEMPLATE` (L11), `NO_MAPPING_FILES_TEMPLATE` (L12), `NO_MAPPING_IN_FOLDER_TEMPLATE` (L13), `NO_DCLGEN_FILES_TEMPLATE` (L14), `UNSUPPORTED_MODE_TEMPLATE` (L15), `LABEL_MAPPING_SHEET` (L18), `LABEL_DCLGEN` (L19), `LABEL_COPYBOOK` (L20), `LABEL_PROGRAM_TEMPLATE` (L21), `DIAG_START_LOAD_SHARED_INPUTS` (L24), `DIAG_MULTIPLE_MAPPING_TEMPLATE` (L25), `DIAG_MAPPING_FOLDER_TEMPLATE` (L29), `DIAG_MAPPING_SELECTED_TEMPLATE` (L30), `DIAG_MAPPING_ROWS_TEMPLATE` (L31), `DIAG_DCLGEN_FOLDER_TEMPLATE` (L32), `DIAG_DCLGEN_FILE_COUNT_TEMPLATE` (L33), `DIAG_DCLGEN_FILE_TEMPLATE` (L34), `DIAG_DCLGEN_TEXT_LEN_TEMPLATE` (L35), `DIAG_DCLGEN_TOTAL_COLUMNS_TEMPLATE` (L36), `DIAG_COPYBOOK_FOLDER_TEMPLATE` (L37), `DIAG_COPYBOOK_FILE_COUNT_TEMPLATE` (L38), `DIAG_COPYBOOK_FILE_TEMPLATE` (L39), `DIAG_COPYBOOK_TEXT_LEN_TEMPLATE` (L40), `DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE` (L41), `COPYBOOK_SOURCE_LABEL` (L44), `DCLGEN_SOURCE_LABEL_TEMPLATE` (L45), `DIAG_SOURCE_FILE_TEMPLATE` (L48), `DIAG_SOURCE_LEN_TEMPLATE` (L49), `DIAG_UPDATE_ENHANCEMENT_DONE` (L52), `DIAG_UPDATE_AUDIT_MOVES` (L53), `DIAG_UPDATE_SKIPPED_TEMPLATE` (L57), `LOG_CONVERSION_COMPLETED_TEMPLATE` (L63), `LOG_INPUT_PROGRAM_TEMPLATE` (L64), `LOG_OUTPUT_FILE_TEMPLATE` (L65), `PRINT_GENERATION_COMPLETED_TEMPLATE` (L67), `PRINT_INPUT_PROGRAM_TEMPLATE` (L68), `PRINT_OUTPUT_CREATED_TEMPLATE` (L69), `HEADER_VALIDATION_MESSAGES` (L71), `HEADER_DIAGNOSTICS` (L72), `HEADER_BATCH_INPUT_SUMMARY` (L73), `NO_VALIDATION_MESSAGES` (L74), `BULLET_TEMPLATE` (L75), `SUMMARY_PROJECT_ROOT_TEMPLATE` (L78), `SUMMARY_SRC_DIR_TEMPLATE` (L79), `SUMMARY_MODE_TEMPLATE` (L80), `SUMMARY_MAPPING_FOLDER_TEMPLATE` (L81), `SUMMARY_PROGRAM_FOLDER_TEMPLATE` (L82), `SUMMARY_PROGRAM_COUNT_TEMPLATE` (L83), `SUMMARY_OUTPUT_FOLDER_TEMPLATE` (L84), `SUMMARY_TARGET_PROGRAM_ID_TEMPLATE` (L85), `PRESERVE_SOURCE_LABEL` (L86)

## Import declarations

```python
from __future__ import annotations
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch/batch_reporter.py](../runners/batch/batch_reporter.md)
- [runners/batch/batch_validator.py](../runners/batch/batch_validator.md)
- [runners/batch/program_converter.py](../runners/batch/program_converter.md)
- [runners/batch/shared_input_loader.py](../runners/batch/shared_input_loader.md)
- [runners/batch/update_postprocess_pipeline.py](../runners/batch/update_postprocess_pipeline.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
