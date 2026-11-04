# `runners/convert_programs.py`

Source: [runners/convert_programs.py](../../../runners/convert_programs.py) | 202 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `12eb25e893682ccd45f6e6e045dfb9703d81155d68cdabb33315b00bb694ba74`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Converts every program in the configured folder, routed by PROGRAM KIND.

## Module-level bindings

`OUTPUT_DIR` (L106), `ROUTE_TEMPLATE` (L110), `ROUTE_FAILED_TEMPLATE` (L111), `KIND_UPDATE` (L117), `KIND_RETRIEVAL` (L118), `__all__` (L120)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from runners.retrieval.retrieval_environment import bootstrap_sys_path
from config.path_settings import DEFAULT_RETRIEVAL_OUTPUT_DIR, DEFAULT_RETRIEVAL_PROGRAM_DIR, LOGS_DIR
from converter.infrastructure.logger_factory import LoggerFactory
from converter.resolvers.program_kind_resolver import ProgramKindResolver
from runners.retrieval.retrieval_input_loader import load_shared_inputs
from runners.retrieval.retrieval_input_selector import selected_program_paths, validate_inputs
from runners.retrieval.retrieval_program_converter import convert_one_program, resolve_target_program_id
from runners.update.update_program_converter import convert_one_program as convert_one_update_program
from rules.retrieval_runner_messages import BATCH_OUTPUT_FOLDER_TEMPLATE, BATCH_PROGRAM_COUNT_TEMPLATE, BATCH_PROGRAM_FOLDER_TEMPLATE, HEADER_RETRIEVAL_BATCH_SUMMARY, RULE_RETRIEVAL_BATCH_SUMMARY
from rules.retrieval_runner_rules import RETRIEVAL_LOGGER_NAME
```

## Local dependency notes

- [config/path_settings.py](../config/path_settings.md)
- [converter/infrastructure/logger_factory.py](../converter/infrastructure/logger_factory.md)
- [converter/resolvers/program_kind_resolver.py](../converter/resolvers/program_kind_resolver.md)
- [rules/retrieval_runner_messages.py](../rules/retrieval_runner_messages.md)
- [rules/retrieval_runner_rules.py](../rules/retrieval_runner_rules.md)
- [runners/retrieval/retrieval_environment.py](retrieval/retrieval_environment.md)
- [runners/retrieval/retrieval_input_loader.py](retrieval/retrieval_input_loader.md)
- [runners/retrieval/retrieval_input_selector.py](retrieval/retrieval_input_selector.md)
- [runners/retrieval/retrieval_program_converter.py](retrieval/retrieval_program_converter.md)
- [runners/update/update_program_converter.py](update/update_program_converter.md)

## Symbol contracts and control points

### `measure_program_kind` - L130-L150

```python
measure_program_kind(program_path: Path) -> str
```

KIND_UPDATE or KIND_RETRIEVAL, measured from the SOURCE text.

Observed calls (lexical order): `Path`, `Path(program_path).read_text`, `print`, `ROUTE_FAILED_TEMPLATE.format`, `ProgramKindResolver`, `ProgramKindResolver().is_update`.

### `run_conversion` - L153-L198

```python
run_conversion() -> None
```

Observed calls (lexical order): `validate_inputs`, `LoggerFactory.create_logger`, `load_shared_inputs`, `selected_program_paths`, `print`, `BATCH_PROGRAM_FOLDER_TEMPLATE.format`, `BATCH_PROGRAM_COUNT_TEMPLATE.format`, `len`, `BATCH_OUTPUT_FOLDER_TEMPLATE.format`, `measure_program_kind`, `Path`, `ROUTE_TEMPLATE.format`, `logger.info`, `converter`.

Control points:

- L174: `for program_path in program_files`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
