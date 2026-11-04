# `runners/batch/batch_validator.py`

Source: [runners/batch/batch_validator.py](../../../../runners/batch/batch_validator.py) | 133 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `26d0c779725c5c6a9642a5233b809ba208d714acef25d6795d21655bffa990d4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Batch input validation.

## Module-level bindings

`__all__` (L124)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from config.path_settings import DEFAULT_COPYBOOK_DIR, DEFAULT_DCLGEN_DIR, DEFAULT_LRF_DIR, DEFAULT_MAPPING_SHEET_DIR, ensure_lrf_dir, ensure_output_dirs, lrf_paths, mapping_sheet_paths, retrieval_program_paths, update_program_paths
from rules.batch_runner_messages import FOLDER_NOT_FOUND_TEMPLATE, LABEL_COPYBOOK, LABEL_DCLGEN, LABEL_MAPPING_SHEET, LABEL_PROGRAM_TEMPLATE, NO_MAPPING_FILES_TEMPLATE, NO_PROGRAM_FILES_TEMPLATE, PATH_NOT_FOLDER_TEMPLATE, UNSUPPORTED_MODE_TEMPLATE
from rules.batch_runner_rules import BATCH_MODE_RETRIEVAL, BATCH_MODE_UPDATE
from rules.lrf_rules import LABEL_LRF
from .batch_models import BatchMode
```

## Local dependency notes

- [config/path_settings.py](../../config/path_settings.md)
- [rules/batch_runner_messages.py](../../rules/batch_runner_messages.md)
- [rules/batch_runner_rules.py](../../rules/batch_runner_rules.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)
- [runners/batch/batch_models.py](batch_models.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch_program_runner.py](../batch_program_runner.md)

## Symbol contracts and control points

### `validate_folder` - L45-L54

```python
validate_folder(folder: Path, label: str) -> None
```

Mandatory folder. Missing or not-a-folder is a hard stop.

Observed calls (lexical order): `folder.exists`, `FileNotFoundError`, `FOLDER_NOT_FOUND_TEMPLATE.format`, `folder.is_dir`, `PATH_NOT_FOLDER_TEMPLATE.format`.

Control points:

- L47: `if not folder.exists()`
- L51: `if not folder.is_dir()`

Explicit raises: `FileNotFoundError(FOLDER_NOT_FOUND_TEMPLATE.format(label=label, folder=folder))`; `FileNotFoundError(PATH_NOT_FOLDER_TEMPLATE.format(label=label, folder=folder))`.

### `optional_folder` - L57-L59

```python
optional_folder(folder: Path) -> bool
```

Optional folder. Returns True only when it exists and is a folder.

Observed calls (lexical order): `folder.exists`, `folder.is_dir`.

### `lrf_folder_status` - L62-L69

```python
lrf_folder_status() -> tuple[bool, int]
```

(folder_present, file_count) for the optional LRF input.

Observed calls (lexical order): `optional_folder`, `len`, `lrf_paths`.

Control points:

- L67: `if not optional_folder(DEFAULT_LRF_DIR)`

### `validate_common_input_folders` - L72-L83

```python
validate_common_input_folders() -> None
```

Observed calls (lexical order): `validate_folder`, `optional_folder`, `ensure_lrf_dir`, `ensure_output_dirs`.

Control points:

- L80: `if not optional_folder(DEFAULT_LRF_DIR)`

### `validate_mapping_files` - L86-L91

```python
validate_mapping_files() -> None
```

At least one mapping sheet must exist in the mapping folder.

Observed calls (lexical order): `mapping_sheet_paths`, `FileNotFoundError`, `NO_MAPPING_FILES_TEMPLATE.format`.

Control points:

- L88: `if not mapping_sheet_paths()`

Explicit raises: `FileNotFoundError(NO_MAPPING_FILES_TEMPLATE.format(folder=DEFAULT_MAPPING_SHEET_DIR))`.

### `program_paths_for_mode` - L95-L104

```python
program_paths_for_mode(mode_name: str) -> list[Path]
```

Observed calls (lexical order): `str`, `str(mode_name or '').strip`, `str(mode_name or '').strip().upper`, `update_program_paths`, `retrieval_program_paths`, `UNSUPPORTED_MODE_TEMPLATE.format`, `ValueError`.

Control points:

- L98: `if normalized == BATCH_MODE_UPDATE`
- L101: `if normalized == BATCH_MODE_RETRIEVAL`

Explicit raises: `ValueError(UNSUPPORTED_MODE_TEMPLATE.format(mode=mode_name))`.

### `validate_mode` - L107-L121

```python
validate_mode(mode: BatchMode) -> None
```

Observed calls (lexical order): `validate_folder`, `LABEL_PROGRAM_TEMPLATE.format`, `mode.output_dir.mkdir`, `program_paths_for_mode`, `FileNotFoundError`, `NO_PROGRAM_FILES_TEMPLATE.format`.

Control points:

- L115: `if not programs`

Explicit raises: `FileNotFoundError(NO_PROGRAM_FILES_TEMPLATE.format(mode=mode.name, folder=mode.program_dir))`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
