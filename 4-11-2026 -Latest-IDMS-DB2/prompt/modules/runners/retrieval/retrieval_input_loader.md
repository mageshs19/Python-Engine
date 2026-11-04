# `runners/retrieval/retrieval_input_loader.py`

Source: [runners/retrieval/retrieval_input_loader.py](../../../../runners/retrieval/retrieval_input_loader.py) | 165 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `1066e3c4fafead44b49bf4f24fae2c8735c823a5b3995071672e5038d2db4f63`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from config.path_settings import DEFAULT_MAPPING_SHEET_DIR
from converter.infrastructure.file_loader import FileLoader
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from rules.retrieval_runner_messages import COPYBOOK_SOURCE_LABEL, DCLGEN_SOURCE_LABEL_TEMPLATE, DIAG_COPYBOOK_FILE_COUNT_TEMPLATE, DIAG_COPYBOOK_FILE_TEMPLATE, DIAG_COPYBOOK_TEXT_LEN_TEMPLATE, DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE, DIAG_DCLGEN_FILE_COUNT_TEMPLATE, DIAG_DCLGEN_FILE_TEMPLATE, DIAG_DCLGEN_TEXT_LEN_TEMPLATE, DIAG_DCLGEN_TOTAL_COLUMNS_TEMPLATE, DIAG_MAPPING_FOLDER_TEMPLATE, DIAG_MAPPING_ROWS_TEMPLATE, DIAG_MAPPING_SELECTED_TEMPLATE, DIAG_START_LOAD_INPUTS, LOG_COPYBOOK_FILE, LOG_COPYBOOK_FILE_COUNT, LOG_COPYBOOK_TEXT_LEN, LOG_COPYBOOK_TOTAL_FIELDS, LOG_DCLGEN_FILE, LOG_DCLGEN_FILE_COUNT, LOG_DCLGEN_TEXT_LEN, LOG_DCLGEN_TOTAL_COLUMNS, LOG_MAPPING_ROWS, LOG_MAPPING_SELECTED
from .retrieval_input_selector import selected_copybook_paths, selected_dclgen_paths, selected_mapping_sheet_path
```

## Local dependency notes

- [config/path_settings.py](../../config/path_settings.md)
- [converter/infrastructure/file_loader.py](../../converter/infrastructure/file_loader.md)
- [converter/infrastructure/local_uploaded_file.py](../../converter/infrastructure/local_uploaded_file.md)
- [converter/parsers/copybook_parser.py](../../converter/parsers/copybook_parser.md)
- [converter/parsers/dclgen_parser.py](../../converter/parsers/dclgen_parser.md)
- [converter/parsers/sheet_mapping_parser.py](../../converter/parsers/sheet_mapping_parser.md)
- [rules/retrieval_runner_messages.py](../../rules/retrieval_runner_messages.md)
- [runners/retrieval/retrieval_input_selector.py](retrieval_input_selector.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/convert_programs.py](../convert_programs.md)
- [tests/test_lrf_vmdz4310_multiline_access_diagnostic.py](../../tests/test_lrf_vmdz4310_multiline_access_diagnostic.md)
- [tests/test_lrf_vmdz4310_production_regression.py](../../tests/test_lrf_vmdz4310_production_regression.md)

## Symbol contracts and control points

### `_load_mapping_rows` - L43-L58

```python
_load_mapping_rows(sheet_parser, diagnostics, logger)
```

Observed calls (lexical order): `selected_mapping_sheet_path`, `LocalUploadedFile`, `sheet_parser.parse_uploaded_file`, `diagnostics.append`, `DIAG_MAPPING_FOLDER_TEMPLATE.format`, `DIAG_MAPPING_SELECTED_TEMPLATE.format`, `DIAG_MAPPING_ROWS_TEMPLATE.format`, `len`, `logger.info`, `hasattr`, `diagnostics.extend`.

Control points:

- L55: `if hasattr(sheet_parser, 'diagnostics')`

### `_load_dclgen_columns` - L61-L100

```python
_load_dclgen_columns(dclgen_parser, file_loader, diagnostics, logger)
```

Observed calls (lexical order): `selected_dclgen_paths`, `diagnostics.append`, `DIAG_DCLGEN_FILE_COUNT_TEMPLATE.format`, `len`, `logger.info`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `dclgen_texts.append`, `DIAG_DCLGEN_FILE_TEMPLATE.format`, `DIAG_DCLGEN_TEXT_LEN_TEMPLATE.format`, `hasattr`, `dclgen_parser.parse_many_texts`, `dclgen_columns.extend`, `dclgen_parser.parse`, `DCLGEN_SOURCE_LABEL_TEMPLATE.format`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L70: `for (index, path) in enumerate(dclgen_files, start=1)`
- L80: `if hasattr(dclgen_parser, 'parse_many_texts')`
- L84: `for (index, text) in enumerate(dclgen_texts, start=1)`
- L97: `if hasattr(dclgen_parser, 'diagnostics')`

### `_load_copybook_fields` - L103-L143

```python
_load_copybook_fields(copybook_parser, file_loader, diagnostics, logger)
```

Observed calls (lexical order): `selected_copybook_paths`, `diagnostics.append`, `DIAG_COPYBOOK_FILE_COUNT_TEMPLATE.format`, `len`, `logger.info`, `enumerate`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `text_parts.append`, `DIAG_COPYBOOK_FILE_TEMPLATE.format`, `DIAG_COPYBOOK_TEXT_LEN_TEMPLATE.format`, `'\n'.join`, `copybook_text.strip`, `copybook_parser.parse`, `DIAG_COPYBOOK_TOTAL_FIELDS_TEMPLATE.format`, `hasattr`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L112: `for (index, path) in enumerate(copybook_files, start=1)`
- L124: `if copybook_text.strip()`
- L140: `if hasattr(copybook_parser, 'diagnostics')`

### `load_shared_inputs` - L146-L165

```python
load_shared_inputs(logger) -> tuple[list, list, list, list[str]]
```

Observed calls (lexical order): `SheetMappingParser`, `DclgenParser`, `CopybookParser`, `FileLoader`, `diagnostics.append`, `logger.info`, `_load_mapping_rows`, `_load_dclgen_columns`, `_load_copybook_fields`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
