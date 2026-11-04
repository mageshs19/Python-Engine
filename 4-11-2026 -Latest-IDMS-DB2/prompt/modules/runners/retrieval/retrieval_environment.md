# `runners/retrieval/retrieval_environment.py`

Source: [runners/retrieval/retrieval_environment.py](../../../../runners/retrieval/retrieval_environment.py) | 20 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `3ec26a0dfd4bfe7738da347a32db10c8276ea09557cb3b404c4d1eb8e6e7b406`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import sys
from pathlib import Path
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/convert_programs.py](../convert_programs.md)

## Symbol contracts and control points

### `bootstrap_sys_path` - L7-L20

```python
bootstrap_sys_path(current_file: Path) -> tuple[Path, Path]
```

Ensure PROJECT_ROOT and SRC_DIR are importable.

Observed calls (lexical order): `current_file.resolve`, `str`, `sys.path.insert`.

Control points:

- L16: `for path in (project_root, src_dir)`
- L17: `if str(path) not in sys.path`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
