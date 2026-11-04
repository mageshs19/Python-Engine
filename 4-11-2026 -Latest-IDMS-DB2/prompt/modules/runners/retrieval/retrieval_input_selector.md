# `runners/retrieval/retrieval_input_selector.py`

Source: [runners/retrieval/retrieval_input_selector.py](../../../../runners/retrieval/retrieval_input_selector.py) | 142 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `f0d69e96e8068929364b674acc59204fc7e99c3bd68792f6898d8fbd4f18f7f3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from config.path_settings import DEFAULT_COPYBOOK_CANDIDATE_PATHS, DEFAULT_DCLGEN_CANDIDATE_PATHS, DEFAULT_MAPPING_SHEET_DIR, DEFAULT_RETRIEVAL_PROGRAM_DIR, DEFAULT_RETRIEVAL_SOURCE_PATH, DEFAULT_SHEET_MAPPING_PATH, copybook_paths, dclgen_paths, ensure_output_dirs, mapping_sheet_paths, retrieval_program_paths
from rules.retrieval_runner_messages import FILE_NOT_FOUND_TEMPLATE, FOLDER_NOT_FOUND_TEMPLATE, LABEL_MAPPING_SHEET, LABEL_RETRIEVAL_PROGRAM, LABEL_RETRIEVAL_PROGRAM_TEMPLATE, LABEL_SHEET_MAPPING, LABEL_COPYBOOK_TEMPLATE, LABEL_DCLGEN_TEMPLATE, NO_DCLGEN_CANDIDATE_TEMPLATE, NO_MAPPING_FILE_TEMPLATE, NO_PROGRAM_FILE_TEMPLATE, PATH_NOT_FILE_TEMPLATE, PATH_NOT_FOLDER_TEMPLATE
```

## Local dependency notes

- [config/path_settings.py](../../config/path_settings.md)
- [rules/retrieval_runner_messages.py](../../rules/retrieval_runner_messages.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/convert_programs.py](../convert_programs.md)
- [runners/retrieval/retrieval_input_loader.py](retrieval_input_loader.md)
- [runners/retrieval/retrieval_program_converter.py](retrieval_program_converter.md)

## Symbol contracts and control points

### `validate_file_exists` - L35-L43

```python
validate_file_exists(file_path: Path, label: str) -> None
```

Observed calls (lexical order): `file_path.exists`, `FileNotFoundError`, `FILE_NOT_FOUND_TEMPLATE.format`, `file_path.is_file`, `PATH_NOT_FILE_TEMPLATE.format`.

Control points:

- L36: `if not file_path.exists()`
- L40: `if not file_path.is_file()`

Explicit raises: `FileNotFoundError(FILE_NOT_FOUND_TEMPLATE.format(label=label, path=file_path))`; `FileNotFoundError(PATH_NOT_FILE_TEMPLATE.format(label=label, path=file_path))`.

### `validate_folder_exists` - L46-L54

```python
validate_folder_exists(folder_path: Path, label: str) -> None
```

Observed calls (lexical order): `folder_path.exists`, `FileNotFoundError`, `FOLDER_NOT_FOUND_TEMPLATE.format`, `folder_path.is_dir`, `PATH_NOT_FOLDER_TEMPLATE.format`.

Control points:

- L47: `if not folder_path.exists()`
- L51: `if not folder_path.is_dir()`

Explicit raises: `FileNotFoundError(FOLDER_NOT_FOUND_TEMPLATE.format(label=label, path=folder_path))`; `FileNotFoundError(PATH_NOT_FOLDER_TEMPLATE.format(label=label, path=folder_path))`.

### `selected_mapping_sheet_path` - L57-L68

```python
selected_mapping_sheet_path() -> Path
```

Observed calls (lexical order): `mapping_sheet_paths`, `DEFAULT_SHEET_MAPPING_PATH.exists`, `FileNotFoundError`, `NO_MAPPING_FILE_TEMPLATE.format`.

Control points:

- L60: `if not mapping_paths and DEFAULT_SHEET_MAPPING_PATH.exists()`
- L63: `if not mapping_paths`

Explicit raises: `FileNotFoundError(NO_MAPPING_FILE_TEMPLATE.format(folder=DEFAULT_MAPPING_SHEET_DIR))`.

### `selected_dclgen_paths` - L71-L79

```python
selected_dclgen_paths() -> list[Path]
```

Observed calls (lexical order): `dclgen_paths`, `path.exists`, `path.is_file`.

Control points:

- L73: `if paths`

### `selected_copybook_paths` - L82-L90

```python
selected_copybook_paths() -> list[Path]
```

Observed calls (lexical order): `copybook_paths`, `path.exists`, `path.is_file`.

Control points:

- L84: `if paths`

### `selected_program_paths` - L93-L104

```python
selected_program_paths() -> list[Path]
```

Observed calls (lexical order): `retrieval_program_paths`, `DEFAULT_RETRIEVAL_SOURCE_PATH.exists`, `DEFAULT_RETRIEVAL_SOURCE_PATH.is_file`.

Control points:

- L95: `if paths`
- L98: `if DEFAULT_RETRIEVAL_SOURCE_PATH.exists() and DEFAULT_RETRIEVAL_SOURCE_PATH.is_file()`

### `validate_inputs` - L107-L142

```python
validate_inputs() -> None
```

Observed calls (lexical order): `validate_folder_exists`, `selected_mapping_sheet_path`, `validate_file_exists`, `selected_dclgen_paths`, `'\n'.join`, `str`, `NO_DCLGEN_CANDIDATE_TEMPLATE.format`, `ValueError`, `enumerate`, `LABEL_DCLGEN_TEMPLATE.format`, `selected_copybook_paths`, `LABEL_COPYBOOK_TEMPLATE.format`, `selected_program_paths`, `FileNotFoundError`, `NO_PROGRAM_FILE_TEMPLATE.format`, `LABEL_RETRIEVAL_PROGRAM_TEMPLATE.format`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L114: `if not dclgen_files`
- L118: `for (index, dclgen_path) in enumerate(dclgen_files, start=1)`
- L124: `for (index, copybook_path) in enumerate(selected_copybook_paths(), start=1)`
- L131: `if not program_files`
- L136: `for (index, program_path) in enumerate(program_files, start=1)`

Explicit raises: `ValueError(NO_DCLGEN_CANDIDATE_TEMPLATE.format(searched=searched))`; `FileNotFoundError(NO_PROGRAM_FILE_TEMPLATE.format(folder=DEFAULT_RETRIEVAL_PROGRAM_DIR))`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
