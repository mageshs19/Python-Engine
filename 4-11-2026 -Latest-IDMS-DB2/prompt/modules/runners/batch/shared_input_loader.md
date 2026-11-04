# `runners/batch/shared_input_loader.py`

Source: [runners/batch/shared_input_loader.py](../../../../runners/batch/shared_input_loader.py) | 292 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `30387799f97d15592ca3f130b028a0d5ec577a2452489f6c122b8a22e22ea39e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from config.path_settings import DEFAULT_COPYBOOK_DIR, DEFAULT_DCLGEN_DIR, DEFAULT_LRF_DIR, DEFAULT_MAPPING_SHEET_DIR, copybook_paths, dclgen_paths, lrf_paths, mapping_sheet_paths
from converter.infrastructure.file_loader import FileLoader
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.lrf_parser import LrfParser
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from rules.batch_runner_messages import COPYBOOK_SOURCE_LABEL, DCLGEN_SOURCE_LABEL_TEMPLATE, DIAG_COPYBOOK_FILE_COUNT_TEMPLATE, DIAG_COPYBOOK_FILE_TEMPLATE, DIAG_COPYBOOK_FOLDER_TEMPLATE, DIAG_COPYBOOK_TEXT_LEN_TEMPLATE, DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE, DIAG_DCLGEN_FILE_COUNT_TEMPLATE, DIAG_DCLGEN_FILE_TEMPLATE, DIAG_DCLGEN_FOLDER_TEMPLATE, DIAG_DCLGEN_TEXT_LEN_TEMPLATE, DIAG_DCLGEN_TOTAL_COLUMNS_TEMPLATE, DIAG_MAPPING_FOLDER_TEMPLATE, DIAG_MAPPING_ROWS_TEMPLATE, DIAG_MAPPING_SELECTED_TEMPLATE, DIAG_MULTIPLE_MAPPING_TEMPLATE, DIAG_START_LOAD_SHARED_INPUTS, NO_DCLGEN_FILES_TEMPLATE, NO_MAPPING_IN_FOLDER_TEMPLATE
from rules.lrf_rules import DIAG_LRF_FILE_COUNT_TEMPLATE, DIAG_LRF_FILE_TEMPLATE, DIAG_LRF_FOLDER_TEMPLATE, DIAG_LRF_PARSED_ZERO, DIAG_LRF_PARSE_FAILED_TEMPLATE, DIAG_LRF_READ_FAILED_TEMPLATE, DIAG_LRF_TEXT_LEN_TEMPLATE, LOG_LRF_FILE_COUNT, LOG_LRF_TOTAL_RECORDS, LRF_SOURCE_LABEL
from .batch_models import SharedInputs
```

## Local dependency notes

- [config/path_settings.py](../../config/path_settings.md)
- [converter/infrastructure/file_loader.py](../../converter/infrastructure/file_loader.md)
- [converter/infrastructure/local_uploaded_file.py](../../converter/infrastructure/local_uploaded_file.md)
- [converter/parsers/copybook_parser.py](../../converter/parsers/copybook_parser.md)
- [converter/parsers/dclgen_parser.py](../../converter/parsers/dclgen_parser.md)
- [converter/parsers/lrf_parser.py](../../converter/parsers/lrf_parser.md)
- [converter/parsers/sheet_mapping_parser.py](../../converter/parsers/sheet_mapping_parser.md)
- [rules/batch_runner_messages.py](../../rules/batch_runner_messages.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)
- [runners/batch/batch_models.py](batch_models.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch_program_runner.py](../batch_program_runner.md)

## Symbol contracts and control points

### `_load_mapping_rows` - L60-L91

```python
_load_mapping_rows(sheet_parser, diagnostics: list[str])
```

Observed calls (lexical order): `mapping_sheet_paths`, `FileNotFoundError`, `NO_MAPPING_IN_FOLDER_TEMPLATE.format`, `len`, `', '.join`, `diagnostics.append`, `DIAG_MULTIPLE_MAPPING_TEMPLATE.format`, `LocalUploadedFile`, `sheet_parser.parse_uploaded_file`, `DIAG_MAPPING_FOLDER_TEMPLATE.format`, `DIAG_MAPPING_SELECTED_TEMPLATE.format`, `DIAG_MAPPING_ROWS_TEMPLATE.format`, `hasattr`, `diagnostics.extend`.

Control points:

- L63: `if not mapping_files`
- L70: `if len(mapping_files) > 1`
- L88: `if hasattr(sheet_parser, 'diagnostics')`

Explicit raises: `FileNotFoundError(NO_MAPPING_IN_FOLDER_TEMPLATE.format(folder=DEFAULT_MAPPING_SHEET_DIR))`.

### `_load_dclgen_columns` - L95-L138

```python
_load_dclgen_columns(dclgen_parser, file_loader, diagnostics: list[str])
```

Observed calls (lexical order): `dclgen_paths`, `diagnostics.append`, `DIAG_DCLGEN_FOLDER_TEMPLATE.format`, `DIAG_DCLGEN_FILE_COUNT_TEMPLATE.format`, `len`, `FileNotFoundError`, `NO_DCLGEN_FILES_TEMPLATE.format`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `DIAG_DCLGEN_FILE_TEMPLATE.format`, `DIAG_DCLGEN_TEXT_LEN_TEMPLATE.format`, `dclgen_parser.parse`, `DCLGEN_SOURCE_LABEL_TEMPLATE.format`, `dclgen_columns.extend`, `DIAG_DCLGEN_TOTAL_COLUMNS_TEMPLATE.format`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L105: `if not dclgen_files`
- L112: `for (index, path) in enumerate(dclgen_files, start=1)`
- L135: `if hasattr(dclgen_parser, 'diagnostics')`

Explicit raises: `FileNotFoundError(NO_DCLGEN_FILES_TEMPLATE.format(folder=DEFAULT_DCLGEN_DIR))`.

### `_load_copybook_fields` - L142-L186

```python
_load_copybook_fields(copybook_parser, file_loader, diagnostics: list[str])
```

Observed calls (lexical order): `copybook_paths`, `diagnostics.append`, `DIAG_COPYBOOK_FOLDER_TEMPLATE.format`, `DIAG_COPYBOOK_FILE_COUNT_TEMPLATE.format`, `len`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `text_parts.append`, `DIAG_COPYBOOK_FILE_TEMPLATE.format`, `DIAG_COPYBOOK_TEXT_LEN_TEMPLATE.format`, `'\n'.join`, `copybook_text.strip`, `copybook_parser.parse`, `DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE.format`, `hasattr`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L153: `for (index, path) in enumerate(copybook_files, start=1)`
- L168: `if copybook_text.strip()`
- L183: `if hasattr(copybook_parser, 'diagnostics')`

### `_load_logical_records` - L190-L256

```python
_load_logical_records(lrf_parser, file_loader, diagnostics: list[str], logger)
```

Load the optional LRF subschema folder.

Observed calls (lexical order): `lrf_paths`, `DIAG_LRF_FOLDER_TEMPLATE.format`, `diagnostics.append`, `DIAG_LRF_FILE_COUNT_TEMPLATE.format`, `len`, `logger.info`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `DIAG_LRF_READ_FAILED_TEMPLATE.format`, `text_parts.append`, `DIAG_LRF_FILE_TEMPLATE.format`, `DIAG_LRF_TEXT_LEN_TEMPLATE.format`, `'\n'.join`, `lrf_text.strip`, `lrf_parser.parse`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L205: `if not lrf_files`
- L211: `for (index, path) in enumerate(lrf_files, start=1)`
- L230: `if not lrf_text.strip()`
- L251: `if hasattr(lrf_parser, 'diagnostics')`

### `load_shared_inputs` - L260-L292

```python
load_shared_inputs(logger) -> SharedInputs
```

Observed calls (lexical order): `SheetMappingParser`, `DclgenParser`, `CopybookParser`, `LrfParser`, `FileLoader`, `diagnostics.append`, `logger.info`, `_load_mapping_rows`, `_load_dclgen_columns`, `_load_copybook_fields`, `_load_logical_records`, `SharedInputs`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
