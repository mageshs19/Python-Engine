# `rules/lrf_rules.py`

Source: [rules/lrf_rules.py](../../../rules/lrf_rules.py) | 87 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `231f145759b341f5ff2e4f587bfe5b893987c84d048f90f1d315caa0f68831c0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`LRF_RULES` (L6), `PATH_GROUP_OBTAIN` (L15), `PATH_GROUP_ERASE` (L16), `PATH_GROUP_STORE` (L17), `PATH_GROUP_MODIFY` (L18), `SUPPORTED_PATH_GROUPS` (L19), `STATUS_OK` (L27), `STATUS_END_OF_AREA` (L28), `STATUS_RECORD_NOT_FOUND` (L29), `STATUS_SET_NOT_EMPTY` (L30), `STATUS_SET_EMPTY` (L31), `LABEL_LRF` (L34), `LABEL_LOGICAL_RECORDS` (L35), `LRF_SOURCE_LABEL` (L36), `DIAG_LRF_NOT_UPLOADED` (L38), `DIAG_LRF_FOLDER_TEMPLATE` (L39), `DIAG_LRF_FILE_COUNT_TEMPLATE` (L40), `DIAG_LRF_FILE_TEMPLATE` (L41), `DIAG_LRF_TEXT_LEN_TEMPLATE` (L42), `DIAG_LRF_TOTAL_RECORDS_TEMPLATE` (L43), `DIAG_LRF_PATHS_TEMPLATE` (L44), `DIAG_LRF_PARSE_FAILED_TEMPLATE` (L45), `LOG_LRF_FILE_COUNT` (L47), `LOG_LRF_TOTAL_RECORDS` (L48), `LRF_VALIDATION_MESSAGES` (L51), `DIAG_LRF_READ_FAILED_TEMPLATE` (L65), `DIAG_LRF_PARSED_ZERO` (L66), `LRF_UPLOAD_LABEL` (L67), `LRF_UPLOAD_HELP` (L68), `LRF_METRIC_LABEL` (L73), `DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE` (L78), `DIAG_LRF_NO_RECORDS_IN_SCOPE` (L81), `STATEMENT_TERMINATOR` (L86)

## Import declarations

```python
from __future__ import annotations
```

## Importers (12)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/lrf_parser.py](../converter/parsers/lrf_parser.md)
- [converter/repositories/lrf_repository.py](../converter/repositories/lrf_repository.md)
- [converter/ui/conversion_actions.py](../converter/ui/conversion_actions.md)
- [converter/ui/input_loader.py](../converter/ui/input_loader.md)
- [converter/ui/main_tab.py](../converter/ui/main_tab.md)
- [converter/ui/status_panel.py](../converter/ui/status_panel.md)
- [runners/batch/batch_validator.py](../runners/batch/batch_validator.md)
- [runners/batch/program_converter.py](../runners/batch/program_converter.md)
- [runners/batch/shared_input_loader.py](../runners/batch/shared_input_loader.md)
- [runners/retrieval/retrieval_program_converter.py](../runners/retrieval/retrieval_program_converter.md)
- [runners/update/update_input_loader.py](../runners/update/update_input_loader.md)
- [runners/update/update_program_converter.py](../runners/update/update_program_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
