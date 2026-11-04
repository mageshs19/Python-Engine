# `converter/infrastructure/logger_factory.py`

Source: [converter/infrastructure/logger_factory.py](../../../../converter/infrastructure/logger_factory.py) | 82 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `5593ddd04dcb2308f98bc4c25f5dac37f8caff4e0e0bbd4a17eea00bb934bde4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`LOG_CONSOLE_ENV_KEY` (L15), `LOG_CONSOLE_LEVEL` (L16)

## Import declarations

```python
import os
import logging
from datetime import datetime
from pathlib import Path
from config.logging_settings import DEFAULT_LOG_LEVEL, LOG_DATE_FORMAT, LOG_DATE_TIME_FORMAT, LOG_FILE_PREFIX, LOG_MESSAGE_FORMAT
from config.path_settings import LOGS_DIR
```

## Local dependency notes

- [config/logging_settings.py](../../config/logging_settings.md)
- [config/path_settings.py](../../config/path_settings.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch_program_runner.py](../../runners/batch_program_runner.md)
- [runners/convert_programs.py](../../runners/convert_programs.md)
- [runners/run_update.py](../../runners/run_update.md)
- [tests/test_vmdz1526_lrf_update_integration.py](../../tests/test_vmdz1526_lrf_update_integration.md)

## Symbol contracts and control points

### `LoggerFactory` - L19-L82

```python
class LoggerFactory()
```

Creates production-style loggers that write to logs folder.

### `LoggerFactory.create_logger` - L28-L72

```python
create_logger(name: str, logs_dir: Path | None=None, level: str=DEFAULT_LOG_LEVEL, console: bool | None=None) -> logging.Logger
```

Observed calls (lexical order): `Path`, `target_logs_dir.mkdir`, `datetime.now`, `datetime.now().strftime`, `logging.getLogger`, `LoggerFactory._level_value`, `logger.setLevel`, `logger.handlers.clear`, `logging.Formatter`, `logging.FileHandler`, `file_handler.setLevel`, `file_handler.setFormatter`, `logger.addHandler`, `os.environ.get`, `os.environ.get(LOG_CONSOLE_ENV_KEY, '').strip`, `logging.StreamHandler`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L55: `if console is None`
- L62: `if console`

### `LoggerFactory._level_value` - L75-L82

```python
_level_value(level: str) -> int
```

Observed calls (lexical order): `getattr`, `str`, `str(level or DEFAULT_LOG_LEVEL).upper`.

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
