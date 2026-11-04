# `config/config/path_settings.py`

Source: [config/config/path_settings.py](../../../../config/config/path_settings.py) | 180 lines.
Owning logic guide: [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../../11_CONFIGURATION_AND_ENTRYPOINTS.md).
Source SHA-256: `02f25759fb43f036e30ddfe91dd5f3e7eee7427b3625a7acf6f2b0ce3292e526`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Path settings for local command-line runs.

## Module-level bindings

`PROJECT_ROOT` (L31), `SRC_DIR` (L32), `LOGS_DIR` (L33), `DEFAULT_INPUT_DIR` (L35), `DEFAULT_MAPPING_SHEET_DIR` (L37), `DEFAULT_DCLGEN_DIR` (L38), `DEFAULT_COPYBOOK_DIR` (L39), `DEFAULT_PROGRAM_DIR` (L40), `DEFAULT_RETRIEVAL_PROGRAM_DIR` (L42), `DEFAULT_UPDATE_PROGRAM_DIR` (L43), `DEFAULT_OUTPUT_DIR` (L45), `DEFAULT_RETRIEVAL_OUTPUT_DIR` (L46), `DEFAULT_UPDATE_OUTPUT_DIR` (L47), `SUPPORTED_MAPPING_EXTENSIONS` (L49), `SUPPORTED_TEXT_EXTENSIONS` (L54), `DEFAULT_SHEET_MAPPING_PATH` (L61), `DEFAULT_RETRIEVAL_SOURCE_PATH` (L62), `DEFAULT_UPDATE_SOURCE_PATH` (L63), `DEFAULT_DCLGEN_CANDIDATE_PATHS` (L179), `DEFAULT_COPYBOOK_CANDIDATE_PATHS` (L180)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
```

## Symbol contracts and control points

### `existing_files` - L66-L76

```python
existing_files(paths: list[Path]) -> list[Path]
```

Return only paths that exist and are files.

Observed calls (lexical order): `path.exists`, `path.is_file`.

### `files_in_folder` - L79-L102

```python
files_in_folder(folder: Path, extensions: tuple[str, ...]) -> list[Path]
```

Return supported files from a folder in stable name order.

Observed calls (lexical order): `folder.exists`, `folder.is_dir`, `tuple`, `extension.lower`, `sorted`, `folder.iterdir`, `path.is_file`, `path.suffix.lower`, `item.name.lower`.

Control points:

- L86: `if not folder.exists() or not folder.is_dir()`

### `mapping_sheet_paths` - L105-L127

```python
mapping_sheet_paths() -> list[Path]
```

Return mapping sheet files from the single mapping sheet folder.

Observed calls (lexical order): `files_in_folder`, `DEFAULT_SHEET_MAPPING_PATH.exists`, `DEFAULT_SHEET_MAPPING_PATH.is_file`, `path.resolve`, `preferred.resolve`.

Control points:

- L116: `if DEFAULT_SHEET_MAPPING_PATH.exists() and DEFAULT_SHEET_MAPPING_PATH.is_file()`

### `dclgen_paths` - L130-L137

```python
dclgen_paths() -> list[Path]
```

Return all DCLGEN files from the DCLGen folder.

Observed calls (lexical order): `files_in_folder`.

### `copybook_paths` - L140-L147

```python
copybook_paths() -> list[Path]
```

Return all copybook files from the Copybook folder.

Observed calls (lexical order): `files_in_folder`.

### `retrieval_program_paths` - L150-L157

```python
retrieval_program_paths() -> list[Path]
```

Return all retrieval COBOL program files.

Observed calls (lexical order): `files_in_folder`.

### `update_program_paths` - L160-L167

```python
update_program_paths() -> list[Path]
```

Return all update COBOL program files.

Observed calls (lexical order): `files_in_folder`.

### `ensure_output_dirs` - L170-L176

```python
ensure_output_dirs() -> None
```

Ensure output folders exist.

Observed calls (lexical order): `DEFAULT_OUTPUT_DIR.mkdir`, `DEFAULT_RETRIEVAL_OUTPUT_DIR.mkdir`, `DEFAULT_UPDATE_OUTPUT_DIR.mkdir`.

## Change responsibility

After modifying this Python file, review [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../../11_CONFIGURATION_AND_ENTRYPOINTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
