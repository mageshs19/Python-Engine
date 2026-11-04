# `config/path_settings.py`

Source: [config/path_settings.py](../../../config/path_settings.py) | 385 lines.
Owning logic guide: [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../11_CONFIGURATION_AND_ENTRYPOINTS.md).
Source SHA-256: `41be5cc9fe6789e8fda04feace52cef9faa433037377a9d3b5c380d5d28c8827`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`PROJECT_ROOT` (L12), `SRC_DIR` (L13), `LOGS_DIR` (L14), `INPUT_DIR_ENV_KEY` (L17), `LAYOUT_ENV_KEY` (L18), `LAYOUT_FLAT` (L21), `LAYOUT_KIND` (L22), `WORKSPACE_DIR_NAME` (L34), `DEFAULT_WORKSPACE_DIR` (L35), `FALLBACK_INPUT_DIR` (L37), `DEFAULT_INPUT_DIR` (L45), `DEFAULT_MAPPING_SHEET_DIR` (L49), `DEFAULT_DCLGEN_DIR` (L50), `DEFAULT_COPYBOOK_DIR` (L51), `DEFAULT_PROGRAM_DIR` (L52), `DEFAULT_OUTPUT_DIR` (L53), `DEFAULT_LOCAL_MAPPING_SHEET_DIR` (L60), `KIND_RETRIEVAL_FOLDER` (L63), `KIND_UPDATE_FOLDER` (L64), `INPUT_LAYOUT` (L86), `LAYOUT_IS_FLAT` (L87), `DEFAULT_RETRIEVAL_MAPPING_SHEET_DIR` (L96), `DEFAULT_UPDATE_MAPPING_SHEET_DIR` (L99), `DEFAULT_RETRIEVAL_PROGRAM_DIR` (L104), `DEFAULT_UPDATE_PROGRAM_DIR` (L107), `DEFAULT_RETRIEVAL_OUTPUT_DIR` (L115), `DEFAULT_UPDATE_OUTPUT_DIR` (L118), `SUPPORTED_MAPPING_EXTENSIONS` (L124), `SUPPORTED_TEXT_EXTENSIONS` (L130), `SUPPORTED_LRF_EXTENSIONS` (L138), `DEFAULT_LRF_DIR` (L151), `DEFAULT_SUBSCHEMA_DIR` (L152), `DEFAULT_SHEET_MAPPING_PATH` (L156), `DEFAULT_RETRIEVAL_SOURCE_PATH` (L157), `DEFAULT_UPDATE_SOURCE_PATH` (L158), `DEFAULT_DCLGEN_CANDIDATE_PATHS` (L333), `DEFAULT_COPYBOOK_CANDIDATE_PATHS` (L334), `DEFAULT_LRF_CANDIDATE_PATHS` (L335), `__all__` (L338)

## Import declarations

```python
from __future__ import annotations
import os
from pathlib import Path
```

## Importers (13)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/infrastructure/logger_factory.py](../converter/infrastructure/logger_factory.md)
- [converter/services/source_copybook_members_loader.py](../converter/services/source_copybook_members_loader.md)
- [runners/batch/batch_validator.py](../runners/batch/batch_validator.md)
- [runners/batch/shared_input_loader.py](../runners/batch/shared_input_loader.md)
- [runners/batch_program_runner.py](../runners/batch_program_runner.md)
- [runners/convert_programs.py](../runners/convert_programs.md)
- [runners/retrieval/retrieval_input_loader.py](../runners/retrieval/retrieval_input_loader.md)
- [runners/retrieval/retrieval_input_selector.py](../runners/retrieval/retrieval_input_selector.md)
- [runners/retrieval/retrieval_program_converter.py](../runners/retrieval/retrieval_program_converter.md)
- [runners/run_update.py](../runners/run_update.md)
- [runners/update/update_input_loader.py](../runners/update/update_input_loader.md)
- [runners/update/update_input_selector.py](../runners/update/update_input_selector.md)
- [tests/generated_output/conftest.py](../tests/generated_output/conftest.md)

## Symbol contracts and control points

### `_input_root` - L40-L42

```python
_input_root() -> Path
```

Observed calls (lexical order): `os.environ.get`, `os.environ.get(INPUT_DIR_ENV_KEY, '').strip`, `os.environ.get(INPUT_DIR_ENV_KEY, '').strip().strip`, `Path`.

### `_configured_layout` - L68-L70

```python
_configured_layout() -> str
```

Observed calls (lexical order): `os.environ.get`, `os.environ.get(LAYOUT_ENV_KEY, '').strip`, `os.environ.get(LAYOUT_ENV_KEY, '').strip().upper`.

### `_detect_layout` - L73-L83

```python
_detect_layout() -> str
```

FLAT unless the legacy kind sub-folders actually exist.

Observed calls (lexical order): `_configured_layout`, `(DEFAULT_PROGRAM_DIR / KIND_RETRIEVAL_FOLDER).is_dir`, `(DEFAULT_PROGRAM_DIR / KIND_UPDATE_FOLDER).is_dir`.

Control points:

- L76: `if configured`

### `_kind_dir` - L90-L92

```python
_kind_dir(parent: Path, kind: str) -> Path
```

<parent> when flat, <parent>/<kind> when the split layout is in use.

### `existing_files` - L162-L168

```python
existing_files(paths: list[Path]) -> list[Path]
```

Return only paths that exist and are files.

Observed calls (lexical order): `path.exists`, `path.is_file`.

### `files_in_folder` - L171-L192

```python
files_in_folder(folder: Path, extensions: tuple[str, ...]) -> list[Path]
```

Return supported files from a folder in stable name order.

Observed calls (lexical order): `folder.exists`, `folder.is_dir`, `tuple`, `extension.lower`, `sorted`, `folder.iterdir`, `path.is_file`, `path.suffix.lower`, `item.name.lower`.

Control points:

- L176: `if not folder.exists() or not folder.is_dir()`

### `mapping_sheet_paths` - L196-L216

```python
mapping_sheet_paths() -> list[Path]
```

Sheet Mapping workbooks: input root first, then the project copy.

Observed calls (lexical order): `files_in_folder`.

Control points:

- L210: `if paths`

### `retrieval_mapping_sheet_paths` - L219-L228

```python
retrieval_mapping_sheet_paths() -> list[Path]
```

Observed calls (lexical order): `files_in_folder`, `mapping_sheet_paths`.

Control points:

- L225: `if mode_paths`

### `update_mapping_sheet_paths` - L231-L240

```python
update_mapping_sheet_paths() -> list[Path]
```

Observed calls (lexical order): `files_in_folder`, `mapping_sheet_paths`.

Control points:

- L237: `if mode_paths`

### `dclgen_paths` - L244-L248

```python
dclgen_paths() -> list[Path]
```

Observed calls (lexical order): `files_in_folder`.

### `copybook_paths` - L251-L255

```python
copybook_paths() -> list[Path]
```

Observed calls (lexical order): `files_in_folder`.

### `lrf_paths` - L259-L265

```python
lrf_paths() -> list[Path]
```

LRF subschema files: the LRF folder first, then Subschema.

Observed calls (lexical order): `files_in_folder`.

Control points:

- L262: `if paths`

### `ensure_lrf_dir` - L268-L270

```python
ensure_lrf_dir() -> None
```

Create the optional LRF folder when it does not exist.

Observed calls (lexical order): `DEFAULT_LRF_DIR.mkdir`.

### `retrieval_program_paths` - L274-L278

```python
retrieval_program_paths() -> list[Path]
```

Observed calls (lexical order): `files_in_folder`.

### `update_program_paths` - L281-L285

```python
update_program_paths() -> list[Path]
```

Observed calls (lexical order): `files_in_folder`.

### `ensure_output_dirs` - L289-L302

```python
ensure_output_dirs() -> None
```

Create only the folders the ACTIVE layout uses.

Observed calls (lexical order): `DEFAULT_OUTPUT_DIR.mkdir`, `DEFAULT_RETRIEVAL_OUTPUT_DIR.mkdir`, `DEFAULT_UPDATE_OUTPUT_DIR.mkdir`.

Control points:

- L298: `if LAYOUT_IS_FLAT`

### `describe` - L306-L326

```python
describe() -> str
```

One block showing where every input actually resolved.

Observed calls (lexical order): `os.environ.get`, `'\n'.join`.

## Change responsibility

After modifying this Python file, review [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../11_CONFIGURATION_AND_ENTRYPOINTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
