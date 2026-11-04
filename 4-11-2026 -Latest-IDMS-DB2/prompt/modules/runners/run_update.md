# `runners/run_update.py`

Source: [runners/run_update.py](../../../runners/run_update.py) | 86 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `81820cb8b5b1a43d75d6a9cfc47378f2d5705840a1185aed71b161207c3faa3f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`OUTPUT_DIR` (L38), `__all__` (L40)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from runners.update.update_environment import bootstrap_sys_path
from config.path_settings import DEFAULT_UPDATE_OUTPUT_DIR, DEFAULT_UPDATE_PROGRAM_DIR, LOGS_DIR
from converter.infrastructure.logger_factory import LoggerFactory
from runners.update.update_input_loader import load_shared_inputs
from runners.update.update_input_selector import selected_program_paths, validate_inputs
from runners.update.update_postprocess_pipeline import enhance_update_program
from runners.update.update_program_converter import convert_one_program, resolve_target_program_id
from rules.update_runner_messages import BATCH_OUTPUT_FOLDER_TEMPLATE, BATCH_PROGRAM_COUNT_TEMPLATE, BATCH_PROGRAM_FOLDER_TEMPLATE, HEADER_UPDATE_BATCH_SUMMARY, RULE_UPDATE_BATCH_SUMMARY
from rules.update_runner_rules import UPDATE_LOGGER_NAME
```

## Local dependency notes

- [config/path_settings.py](../config/path_settings.md)
- [converter/infrastructure/logger_factory.py](../converter/infrastructure/logger_factory.md)
- [rules/update_runner_messages.py](../rules/update_runner_messages.md)
- [rules/update_runner_rules.py](../rules/update_runner_rules.md)
- [runners/update/update_environment.py](update/update_environment.md)
- [runners/update/update_input_loader.py](update/update_input_loader.md)
- [runners/update/update_input_selector.py](update/update_input_selector.md)
- [runners/update/update_postprocess_pipeline.py](update/update_postprocess_pipeline.md)
- [runners/update/update_program_converter.py](update/update_program_converter.md)

## Symbol contracts and control points

### `run_conversion` - L50-L82

```python
run_conversion() -> None
```

Observed calls (lexical order): `validate_inputs`, `LoggerFactory.create_logger`, `load_shared_inputs`, `selected_program_paths`, `print`, `BATCH_PROGRAM_FOLDER_TEMPLATE.format`, `BATCH_PROGRAM_COUNT_TEMPLATE.format`, `len`, `BATCH_OUTPUT_FOLDER_TEMPLATE.format`, `convert_one_program`.

Control points:

- L71: `for program_path in program_files`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
