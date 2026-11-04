# `runners/batch_program_runner.py`

Source: [runners/batch_program_runner.py](../../../runners/batch_program_runner.py) | 142 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `b5e4abc260fcf874e68b4a387a361e76b73af1ceed3e6c8376aa31fab9f4dfb0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CORRECTION (NEW-4): target_program_id was resolved ONCE, before the loop, from env_target_program_id() falling back to mode.default_target_program_id - the SAME name for every program in the batch. VMDZ7200/4310/4420 all received whichever single name that produced.

## Module-level bindings

`__all__` (L56)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from runners.batch.batch_environment import bootstrap_sys_path, env_target_program_id
from config.path_settings import DEFAULT_MAPPING_SHEET_DIR, LOGS_DIR
from converter.infrastructure.logger_factory import LoggerFactory
from converter.parsers.cobol_parser import CobolParser
from converter.services.name_derivation_resolver import NameDerivationResolver
from runners.batch.batch_models import BatchMode, SharedInputs
from runners.batch.batch_reporter import print_batch_summary
from runners.batch.batch_validator import program_paths_for_mode, validate_common_input_folders, validate_mode
from runners.batch.program_converter import convert_one_program
from runners.batch.shared_input_loader import load_shared_inputs
from config.path_settings import DEFAULT_UPDATE_OUTPUT_DIR, DEFAULT_UPDATE_PROGRAM_DIR
```

## Local dependency notes

- [config/path_settings.py](../config/path_settings.md)
- [converter/infrastructure/logger_factory.py](../converter/infrastructure/logger_factory.md)
- [converter/parsers/cobol_parser.py](../converter/parsers/cobol_parser.md)
- [converter/services/name_derivation_resolver.py](../converter/services/name_derivation_resolver.md)
- [runners/batch/batch_environment.py](batch/batch_environment.md)
- [runners/batch/batch_models.py](batch/batch_models.md)
- [runners/batch/batch_reporter.py](batch/batch_reporter.md)
- [runners/batch/batch_validator.py](batch/batch_validator.md)
- [runners/batch/program_converter.py](batch/program_converter.md)
- [runners/batch/shared_input_loader.py](batch/shared_input_loader.md)

## Symbol contracts and control points

### `resolve_target_program_id_for` - L68-L81

```python
resolve_target_program_id_for(program_path: Path) -> str
```

Derive the target PROGRAM-ID from ONE program's own source text (VM...BD... -> VMDZ...). Returns "" when the source carries no PROGRAM-ID or the name does not match the derivable shape - the caller falls back to the mode default in that case, same as before.

Observed calls (lexical order): `program_path.read_text`, `CobolParser`, `CobolParser().program_id`, `NameDerivationResolver`, `NameDerivationResolver().derive`.

Control points:

- L79: `if not source_id`

### `run_batch` - L84-L125

```python
run_batch(mode: BatchMode) -> None
```

Observed calls (lexical order): `validate_common_input_folders`, `validate_mode`, `LoggerFactory.create_logger`, `mode.name.lower`, `load_shared_inputs`, `program_paths_for_mode`, `env_target_program_id`, `print_batch_summary`, `len`, `resolve_target_program_id_for`, `convert_one_program`.

Control points:

- L113: `for program_path in programs`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
