# `runners/batch/batch_reporter.py`

Source: [runners/batch/batch_reporter.py](../../../../runners/batch/batch_reporter.py) | 92 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `5c96d94a50e1a7c39a4663c0ce60c9b04a8db210d73d3c9dca857defc5a2598a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from rules.batch_runner_messages import BULLET_TEMPLATE, HEADER_DIAGNOSTICS, HEADER_VALIDATION_MESSAGES, LOG_CONVERSION_COMPLETED_TEMPLATE, LOG_INPUT_PROGRAM_TEMPLATE, LOG_OUTPUT_FILE_TEMPLATE, NO_VALIDATION_MESSAGES, PRESERVE_SOURCE_LABEL, PRINT_GENERATION_COMPLETED_TEMPLATE, PRINT_INPUT_PROGRAM_TEMPLATE, PRINT_OUTPUT_CREATED_TEMPLATE, SUMMARY_MAPPING_FOLDER_TEMPLATE, SUMMARY_MODE_TEMPLATE, SUMMARY_OUTPUT_FOLDER_TEMPLATE, SUMMARY_PROGRAM_COUNT_TEMPLATE, SUMMARY_PROGRAM_FOLDER_TEMPLATE, SUMMARY_PROJECT_ROOT_TEMPLATE, SUMMARY_SRC_DIR_TEMPLATE, SUMMARY_TARGET_PROGRAM_ID_TEMPLATE, HEADER_BATCH_INPUT_SUMMARY
from .batch_models import BatchMode
```

## Local dependency notes

- [rules/batch_runner_messages.py](../../rules/batch_runner_messages.md)
- [runners/batch/batch_models.py](batch_models.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch/program_converter.py](program_converter.md)
- [runners/batch_program_runner.py](../batch_program_runner.md)

## Symbol contracts and control points

### `log_program_result` - L31-L66

```python
log_program_result(*, mode: BatchMode, program_path: Path, output_path: Path, result, diagnostics: list[str], logger) -> None
```

Observed calls (lexical order): `LOG_CONVERSION_COMPLETED_TEMPLATE.format`, `logger.info`, `LOG_INPUT_PROGRAM_TEMPLATE.format`, `LOG_OUTPUT_FILE_TEMPLATE.format`, `print`, `PRINT_GENERATION_COMPLETED_TEMPLATE.format`, `PRINT_INPUT_PROGRAM_TEMPLATE.format`, `PRINT_OUTPUT_CREATED_TEMPLATE.format`, `BULLET_TEMPLATE.format`, `logger.warning`.

Control points:

- L53: `if result.validation_messages`
- L54: `for message in result.validation_messages`
- L64: `for diagnostic in diagnostics`

### `print_batch_summary` - L69-L92

```python
print_batch_summary(*, project_root, src_dir, mode: BatchMode, mapping_folder, program_count: int, target_program_id: str) -> None
```

Observed calls (lexical order): `print`, `SUMMARY_PROJECT_ROOT_TEMPLATE.format`, `SUMMARY_SRC_DIR_TEMPLATE.format`, `SUMMARY_MODE_TEMPLATE.format`, `SUMMARY_MAPPING_FOLDER_TEMPLATE.format`, `SUMMARY_PROGRAM_FOLDER_TEMPLATE.format`, `SUMMARY_PROGRAM_COUNT_TEMPLATE.format`, `SUMMARY_OUTPUT_FOLDER_TEMPLATE.format`, `SUMMARY_TARGET_PROGRAM_ID_TEMPLATE.format`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
