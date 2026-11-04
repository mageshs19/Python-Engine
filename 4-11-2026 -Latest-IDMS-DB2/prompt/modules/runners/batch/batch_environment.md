# `runners/batch/batch_environment.py`

Source: [runners/batch/batch_environment.py](../../../../runners/batch/batch_environment.py) | 28 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `1a2bd575653ca7d116b27e69847c0cc8d5f925194a6575dd5587d3ae978071b9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import os
import sys
from pathlib import Path
from rules.batch_runner_rules import TARGET_PROGRAM_ID_ENV_KEY
```

## Local dependency notes

- [rules/batch_runner_rules.py](../../rules/batch_runner_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch_program_runner.py](../batch_program_runner.md)

## Symbol contracts and control points

### `bootstrap_sys_path` - L10-L23

```python
bootstrap_sys_path(current_file: Path) -> tuple[Path, Path]
```

Ensure PROJECT_ROOT and SRC_DIR are importable.

Observed calls (lexical order): `current_file.resolve`, `str`, `sys.path.insert`.

Control points:

- L19: `for path in (project_root, src_dir)`
- L20: `if str(path) not in sys.path`

### `env_target_program_id` - L26-L28

```python
env_target_program_id() -> str
```

Read the target PROGRAM-ID override from the environment.

Observed calls (lexical order): `os.getenv`, `str`, `str(os.getenv(TARGET_PROGRAM_ID_ENV_KEY, '') or '').strip`, `str(os.getenv(TARGET_PROGRAM_ID_ENV_KEY, '') or '').strip().upper`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
