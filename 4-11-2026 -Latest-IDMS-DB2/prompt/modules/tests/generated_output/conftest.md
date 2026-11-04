# `tests/generated_output/conftest.py`

Source: [tests/generated_output/conftest.py](../../../../tests/generated_output/conftest.py) | 111 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `687688067c173fe5d19b12bf562c10aa5714216cb1ddb8e382166728972cb839`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`COBOL_GLOB` (L10), `SOURCE_GLOB` (L11), `WATCHED_SOURCE_DIRS` (L12), `OUTPUT_DIR_NAMES` (L13), `BODY_START` (L18), `BODY_END` (L19), `STAMP_FORMAT` (L20)

## Import declarations

```python
from __future__ import annotations
from datetime import datetime
from pathlib import Path
import pytest
from config import path_settings
```

## Local dependency notes

- [config/__init__.py](../../config/__init__.md)
- [config/path_settings.py](../../config/path_settings.md)

## Symbol contracts and control points

### `_candidate_output_dirs` - L23-L36

```python
_candidate_output_dirs() -> list[Path]
```

Observed calls (lexical order): `set`, `getattr`, `Path`, `str`, `str(path).lower`, `seen.add`, `folders.append`.

Control points:

- L26: `for name in OUTPUT_DIR_NAMES`
- L28: `if folder is None`
- L32: `if key in seen`

### `_newest_generated_cbl` - L39-L52

```python
_newest_generated_cbl() -> Path | None
```

Observed calls (lexical order): `_candidate_output_dirs`, `folder.exists`, `folder.is_dir`, `folder.glob`, `path.is_file`, `newest.stat`, `path.stat`.

Control points:

- L41: `for folder in _candidate_output_dirs()`
- L42: `if not folder.exists() or not folder.is_dir()`
- L44: `for path in folder.glob(COBOL_GLOB)`
- L45: `if not path.is_file()`
- L47: `if newest is None`
- L50: `if path.stat().st_mtime > newest.stat().st_mtime`

### `_newest_source_mtime` - L55-L65

```python
_newest_source_mtime() -> float
```

Observed calls (lexical order): `Path`, `Path.cwd`, `getattr`, `folder.exists`, `folder.rglob`, `path.is_file`, `max`, `path.stat`.

Control points:

- L58: `for name in WATCHED_SOURCE_DIRS`
- L60: `if not folder.exists()`
- L62: `for path in folder.rglob(SOURCE_GLOB)`
- L63: `if path.is_file()`

### `_stamp` - L68-L69

```python
_stamp(mtime: float) -> str
```

Observed calls (lexical order): `datetime.fromtimestamp`, `datetime.fromtimestamp(mtime).strftime`.

### `generated_artifact` - L73-L91

```python
generated_artifact() -> Path
```

Observed calls (lexical order): `_newest_generated_cbl`, `', '.join`, `_candidate_output_dirs`, `str`, `pytest.skip`, `artifact.stat`, `_newest_source_mtime`, `_stamp`.

Control points:

- L75: `if artifact is None`
- L83: `if source_mtime and artifact_mtime < source_mtime`

### `generated_bodies` - L95-L101

```python
generated_bodies(generated_artifact: Path) -> list[str]
```

Observed calls (lexical order): `generated_artifact.read_text`, `line[BODY_START:BODY_END].strip`, `text.splitlines`.

### `previous_body` - L105-L111

```python
previous_body(generated_bodies: list[str])
```

### `previous_body._previous` - L106-L109

```python
_previous(index: int) -> str
```

Control points:

- L107: `if index <= 0`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
