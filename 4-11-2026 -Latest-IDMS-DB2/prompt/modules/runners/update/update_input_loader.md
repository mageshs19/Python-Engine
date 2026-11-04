# `runners/update/update_input_loader.py`

Source: [runners/update/update_input_loader.py](../../../../runners/update/update_input_loader.py) | 261 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `8f5642176fea43c026ecf3f8145a6c2c2c116b030b8f8007e90c02d5e2def723`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`_LOGICAL_RECORDS_CACHE` (L57)

## Import declarations

```python
from __future__ import annotations
from config.path_settings import DEFAULT_DCLGEN_DIR, DEFAULT_MAPPING_SHEET_DIR
from converter.infrastructure.file_loader import FileLoader
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from rules.update_runner_messages import COPYBOOK_SOURCE_LABEL, DCLGEN_SOURCE_LABEL_TEMPLATE, DIAG_COPYBOOK_FILE_COUNT_TEMPLATE, DIAG_COPYBOOK_FILE_TEMPLATE, DIAG_COPYBOOK_TEXT_LEN_TEMPLATE, DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE, DIAG_DCLGEN_FILE_COUNT_TEMPLATE, DIAG_DCLGEN_FILE_TEMPLATE, DIAG_DCLGEN_FOLDER_TEMPLATE, DIAG_DCLGEN_TEXT_LEN_TEMPLATE, DIAG_DCLGEN_TOTAL_COLUMNS_TEMPLATE, DIAG_MAPPING_FOLDER_TEMPLATE, DIAG_MAPPING_ROWS_TEMPLATE, DIAG_MAPPING_SELECTED_TEMPLATE, DIAG_START_LOAD_INPUTS, LOG_COPYBOOK_FILE, LOG_COPYBOOK_FILE_COUNT, LOG_COPYBOOK_TEXT_LEN, LOG_COPYBOOK_TOTAL_FIELDS, LOG_DCLGEN_FILE, LOG_DCLGEN_FILE_COUNT, LOG_DCLGEN_TEXT_LEN, LOG_DCLGEN_TOTAL_COLUMNS, LOG_MAPPING_ROWS, LOG_MAPPING_SELECTED
from .update_input_selector import selected_copybook_paths, selected_dclgen_paths, selected_mapping_sheet_path
from config.path_settings import DEFAULT_LRF_DIR, lrf_paths
from converter.parsers.lrf_parser import LrfParser
from rules.lrf_rules import DIAG_LRF_FILE_COUNT_TEMPLATE, DIAG_LRF_FILE_TEMPLATE, DIAG_LRF_FOLDER_TEMPLATE, DIAG_LRF_PARSE_FAILED_TEMPLATE, DIAG_LRF_PARSED_ZERO, DIAG_LRF_READ_FAILED_TEMPLATE, DIAG_LRF_TEXT_LEN_TEMPLATE, LOG_LRF_FILE_COUNT, LOG_LRF_TOTAL_RECORDS, LRF_SOURCE_LABEL
```

## Local dependency notes

- [config/path_settings.py](../../config/path_settings.md)
- [converter/infrastructure/file_loader.py](../../converter/infrastructure/file_loader.md)
- [converter/infrastructure/local_uploaded_file.py](../../converter/infrastructure/local_uploaded_file.md)
- [converter/parsers/copybook_parser.py](../../converter/parsers/copybook_parser.md)
- [converter/parsers/dclgen_parser.py](../../converter/parsers/dclgen_parser.md)
- [converter/parsers/lrf_parser.py](../../converter/parsers/lrf_parser.md)
- [converter/parsers/sheet_mapping_parser.py](../../converter/parsers/sheet_mapping_parser.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)
- [rules/update_runner_messages.py](../../rules/update_runner_messages.md)
- [runners/update/update_input_selector.py](update_input_selector.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/run_update.py](../run_update.md)
- [runners/update/update_program_converter.py](update_program_converter.md)
- [tests/test_vmdz1526_lrf_update_integration.py](../../tests/test_vmdz1526_lrf_update_integration.md)

## Symbol contracts and control points

### `_load_mapping_rows` - L60-L75

```python
_load_mapping_rows(sheet_parser, diagnostics, logger)
```

Observed calls (lexical order): `selected_mapping_sheet_path`, `LocalUploadedFile`, `sheet_parser.parse_uploaded_file`, `diagnostics.append`, `DIAG_MAPPING_FOLDER_TEMPLATE.format`, `DIAG_MAPPING_SELECTED_TEMPLATE.format`, `DIAG_MAPPING_ROWS_TEMPLATE.format`, `len`, `logger.info`, `hasattr`, `diagnostics.extend`.

Control points:

- L72: `if hasattr(sheet_parser, 'diagnostics')`

### `_load_dclgen_columns` - L78-L118

```python
_load_dclgen_columns(dclgen_parser, file_loader, diagnostics, logger)
```

Observed calls (lexical order): `selected_dclgen_paths`, `DIAG_DCLGEN_FOLDER_TEMPLATE.format`, `diagnostics.append`, `DIAG_DCLGEN_FILE_COUNT_TEMPLATE.format`, `len`, `logger.info`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `dclgen_texts.append`, `DIAG_DCLGEN_FILE_TEMPLATE.format`, `DIAG_DCLGEN_TEXT_LEN_TEMPLATE.format`, `hasattr`, `dclgen_parser.parse_many_texts`, `dclgen_columns.extend`, `dclgen_parser.parse`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L88: `for (index, path) in enumerate(dclgen_files, start=1)`
- L98: `if hasattr(dclgen_parser, 'parse_many_texts')`
- L102: `for (index, text) in enumerate(dclgen_texts, start=1)`
- L115: `if hasattr(dclgen_parser, 'diagnostics')`

### `_load_copybook_fields` - L121-L161

```python
_load_copybook_fields(copybook_parser, file_loader, diagnostics, logger)
```

Observed calls (lexical order): `selected_copybook_paths`, `diagnostics.append`, `DIAG_COPYBOOK_FILE_COUNT_TEMPLATE.format`, `len`, `logger.info`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `text_parts.append`, `DIAG_COPYBOOK_FILE_TEMPLATE.format`, `DIAG_COPYBOOK_TEXT_LEN_TEMPLATE.format`, `'\n'.join`, `copybook_text.strip`, `copybook_parser.parse`, `DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE.format`, `hasattr`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L130: `for (index, path) in enumerate(copybook_files, start=1)`
- L142: `if copybook_text.strip()`
- L158: `if hasattr(copybook_parser, 'diagnostics')`

### `load_shared_inputs` - L164-L183

```python
load_shared_inputs(logger) -> tuple[list, list, list, list[str]]
```

Observed calls (lexical order): `SheetMappingParser`, `DclgenParser`, `CopybookParser`, `FileLoader`, `diagnostics.append`, `logger.info`, `_load_mapping_rows`, `_load_dclgen_columns`, `_load_copybook_fields`.

### `reset_logical_records_cache` - L185-L188

```python
reset_logical_records_cache() -> None
```

Drop the memoised subschema. One process, many runs.

### `load_logical_records` - L191-L261

```python
load_logical_records(logger, diagnostics: list[str]) -> list
```

The optional LRF subschema, parsed once per process.

Observed calls (lexical order): `diagnostics.append`, `DIAG_LRF_FILE_COUNT_TEMPLATE.format`, `len`, `list`, `FileLoader`, `lrf_paths`, `DIAG_LRF_FOLDER_TEMPLATE.format`, `logger.info`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `DIAG_LRF_READ_FAILED_TEMPLATE.format`, `text_parts.append`, `DIAG_LRF_FILE_TEMPLATE.format`, `DIAG_LRF_TEXT_LEN_TEMPLATE.format`, `'\n'.join`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L200: `if _LOGICAL_RECORDS_CACHE is not None`
- L215: `if not lrf_files`
- L221: `for (index, path) in enumerate(lrf_files, start=1)`
- L236: `if not lrf_text.strip()`
- L256: `if hasattr(parser, 'diagnostics')`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
