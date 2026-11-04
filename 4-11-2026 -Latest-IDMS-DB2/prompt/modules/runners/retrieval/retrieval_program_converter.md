# `runners/retrieval/retrieval_program_converter.py`

Source: [runners/retrieval/retrieval_program_converter.py](../../../../runners/retrieval/retrieval_program_converter.py) | 513 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `89406dc2b06e3d58d846a66d3d7900bcfa4f27f402f807010dedab4a3076378a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Converts one retrieval program and prints its report.

## Module-level bindings

`LRF_TEXT_ENCODING` (L114), `LRF_SOURCE_LABEL` (L115), `__all__` (L509)

## Import declarations

```python
from __future__ import annotations
from converter.services.source_copybook_members_loader import read_source_copybook_members as _read_source_copybook_members
from datetime import datetime
from pathlib import Path
from config.path_settings import DEFAULT_LRF_DIR, lrf_paths
from converter.domain.models import ConversionInput
from converter.infrastructure.file_loader import FileLoader
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.pipeline.conversion_service import ConversionService
from converter.parsers.cobol_parser import CobolParser
from converter.parsers.lrf_parser import LrfParser
from converter.services.name_derivation_resolver import NameDerivationResolver
from patterns.lrf_patterns import COPY_IDMS_LR_PATTERN
from rules.lrf_rules import DIAG_LRF_FILE_COUNT_TEMPLATE, DIAG_LRF_FILE_TEMPLATE, DIAG_LRF_FOLDER_TEMPLATE, DIAG_LRF_NO_RECORDS_IN_SCOPE, DIAG_LRF_PARSED_ZERO, DIAG_LRF_PARSE_FAILED_TEMPLATE, DIAG_LRF_READ_FAILED_TEMPLATE, DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE, DIAG_LRF_TEXT_LEN_TEMPLATE, DIAG_LRF_TOTAL_RECORDS_TEMPLATE, LABEL_LRF, LOG_LRF_FILE_COUNT, LOG_LRF_TOTAL_RECORDS, LRF_VALIDATION_MESSAGES
from rules.retrieval_runner_messages import BULLET_TEMPLATE, DIAG_DERIVED_PROGRAM_ID_TEMPLATE, DIAG_SOURCE_FILE_TEMPLATE, DIAG_SOURCE_LEN_TEMPLATE, HEADER_DIAGNOSTICS, HEADER_INPUT_SUMMARY, HEADER_SELECTED_INPUT_FILES, HEADER_VALIDATION_MESSAGES, LOG_DERIVED_PROGRAM_ID, LOG_GENERATION_COMPLETED, LOG_OUTPUT_CREATED, LOG_SOURCE_FILE, LOG_SOURCE_LEN, NO_VALIDATION_MESSAGES, PRESERVE_SOURCE_LABEL, PRINT_GENERATION_COMPLETED, PRINT_INPUT_PROGRAM_TEMPLATE, PRINT_OUTPUT_CREATED_TEMPLATE, RULE_DIAGNOSTICS, RULE_INPUT_SUMMARY, RULE_SELECTED_INPUT_FILES, RULE_VALIDATION_MESSAGES, SELECTED_COBOL_SOURCE_TEMPLATE, SELECTED_COPYBOOK_HEADER, SELECTED_COPYBOOK_NONE, SELECTED_DCLGEN_HEADER, SELECTED_PATH_BULLET_TEMPLATE, SELECTED_SHEET_MAPPING_TEMPLATE, SUMMARY_COBOL_LEN_TEMPLATE, SUMMARY_COPYBOOK_FIELDS_TEMPLATE, SUMMARY_DCLGEN_COLUMNS_TEMPLATE, SUMMARY_PROJECT_ROOT_TEMPLATE, SUMMARY_SHEET_ROWS_TEMPLATE, SUMMARY_SRC_DIR_TEMPLATE, SUMMARY_TARGET_PROGRAM_ID_TEMPLATE
from rules.retrieval_runner_rules import AUTO_FIX_PIC_LENGTH_MISMATCHES_DEFAULT, COBOL_TEXT_ENCODING, OUTPUT_FILE_EXTENSION, OUTPUT_FILE_NAME_TEMPLATE, OUTPUT_TIMESTAMP_FORMAT
from .retrieval_input_selector import selected_copybook_paths, selected_dclgen_paths, selected_mapping_sheet_path
from converter.postprocess.copybook_reference_renamer import CopybookReferenceRenamer
```

## Local dependency notes

- [config/path_settings.py](../../config/path_settings.md)
- [converter/domain/models.py](../../converter/domain/models.md)
- [converter/infrastructure/file_loader.py](../../converter/infrastructure/file_loader.md)
- [converter/infrastructure/local_uploaded_file.py](../../converter/infrastructure/local_uploaded_file.md)
- [converter/parsers/cobol_parser.py](../../converter/parsers/cobol_parser.md)
- [converter/parsers/lrf_parser.py](../../converter/parsers/lrf_parser.md)
- [converter/pipeline/conversion_service.py](../../converter/pipeline/conversion_service.md)
- [converter/postprocess/copybook_reference_renamer.py](../../converter/postprocess/copybook_reference_renamer.md)
- [converter/services/name_derivation_resolver.py](../../converter/services/name_derivation_resolver.md)
- [converter/services/source_copybook_members_loader.py](../../converter/services/source_copybook_members_loader.md)
- [patterns/lrf_patterns.py](../../patterns/lrf_patterns.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)
- [rules/retrieval_runner_messages.py](../../rules/retrieval_runner_messages.md)
- [rules/retrieval_runner_rules.py](../../rules/retrieval_runner_rules.md)
- [runners/retrieval/retrieval_input_selector.py](retrieval_input_selector.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/convert_programs.py](../convert_programs.md)
- [tests/test_lrf_vmdz4310_multiline_access_diagnostic.py](../../tests/test_lrf_vmdz4310_multiline_access_diagnostic.md)
- [tests/test_lrf_vmdz4310_production_regression.py](../../tests/test_lrf_vmdz4310_production_regression.md)

## Symbol contracts and control points

### `resolve_target_program_id` - L118-L123

```python
resolve_target_program_id(source_text: str) -> str
```

Derive the target PROGRAM-ID from the source (VM...BD... -> VMDZ...).

Observed calls (lexical order): `CobolParser`, `CobolParser().program_id`, `NameDerivationResolver`, `NameDerivationResolver().derive`.

Control points:

- L121: `if not source_id`

### `_build_output_path` - L126-L140

```python
_build_output_path(output_dir: Path, program_path: Path, target_program_id: str='') -> Path
```

Observed calls (lexical order): `str`, `str(target_program_id or '').strip`, `datetime.now`, `datetime.now().strftime`, `OUTPUT_FILE_NAME_TEMPLATE.format`.

### `_read_lrf_text` - L146-L163

```python
_read_lrf_text(path: Path, file_loader: FileLoader) -> str
```

Read one subschema, BOM tolerant.

Observed calls (lexical order): `LocalUploadedFile`, `file_loader.read_uploaded_text`, `str`, `str(text or '').strip`, `str(text).lstrip`, `Path`, `Path(path).read_text`.

Control points:

- L155: `if str(text or '').strip()`

### `_parse_lrf_text` - L166-L171

```python
_parse_lrf_text(parser: LrfParser, text: str) -> list
```

Parse subschema text, tolerating either parse() signature.

Observed calls (lexical order): `list`, `parser.parse`.

### `load_logical_records` - L174-L249

```python
load_logical_records(diagnostics: list[str], logger) -> list
```

Every logical record declared in the configured LRF folder.

Observed calls (lexical order): `DIAG_LRF_FOLDER_TEMPLATE.format`, `diagnostics.append`, `Path`, `lrf_paths`, `DIAG_LRF_READ_FAILED_TEMPLATE.format`, `DIAG_LRF_FILE_COUNT_TEMPLATE.format`, `len`, `logger.info`, `FileLoader`, `LrfParser`, `enumerate`, `DIAG_LRF_FILE_TEMPLATE.format`, `_read_lrf_text`, `DIAG_LRF_TEXT_LEN_TEMPLATE.format`, `text_parts.append`, `'\n'.join`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L197: `if not files`
- L205: `for (index, path) in enumerate(files, start=1)`
- L225: `if not combined.strip()`
- L246: `if parser_diagnostics`

### `_source_uses_logical_records` - L252-L267

```python
_source_uses_logical_records(source_text: str) -> list[str]
```

Logical record names the SOURCE copies via COPY IDMS LR.

Observed calls (lexical order): `str`, `str(source_text or '').splitlines`, `COPY_IDMS_LR_PATTERN.search`, `match.group`, `str(match.group('lr') or '').strip`, `str(match.group('lr') or '').strip().upper`, `names.append`.

Control points:

- L256: `for raw_line in str(source_text or '').splitlines()`
- L259: `if not match`
- L264: `if name and name not in names`

### `_narrate_lrf` - L270-L302

```python
_narrate_lrf(*, source_text: str, logical_records: list, diagnostics: list[str], logger) -> None
```

Record what LRF metadata this program run will actually see.

Observed calls (lexical order): `', '.join`, `getattr`, `str`, `diagnostics.append`, `DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE.format`, `len`, `_source_uses_logical_records`, `logger.warning`.

Control points:

- L283: `if logical_records`
- L299: `if used and (not logical_records)`

### `_print_summary` - L308-L364

```python
_print_summary(*, program_path, sheet_rows, dclgen_columns, copybook_fields, logical_records, idms_len, target_program_id, project_root, src_dir)
```

Observed calls (lexical order): `print`, `SUMMARY_PROJECT_ROOT_TEMPLATE.format`, `SUMMARY_SRC_DIR_TEMPLATE.format`, `SUMMARY_SHEET_ROWS_TEMPLATE.format`, `len`, `SUMMARY_DCLGEN_COLUMNS_TEMPLATE.format`, `SUMMARY_COPYBOOK_FIELDS_TEMPLATE.format`, `SUMMARY_COBOL_LEN_TEMPLATE.format`, `SUMMARY_TARGET_PROGRAM_ID_TEMPLATE.format`, `SELECTED_SHEET_MAPPING_TEMPLATE.format`, `selected_mapping_sheet_path`, `SELECTED_COBOL_SOURCE_TEMPLATE.format`, `selected_dclgen_paths`, `SELECTED_PATH_BULLET_TEMPLATE.format`, `selected_copybook_paths`, `list`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L343: `for path in selected_dclgen_paths()`
- L347: `if copybooks`
- L349: `for path in copybooks`
- L360: `if lrf_files`
- L361: `for path in lrf_files`

### `_print_results` - L367-L385

```python
_print_results(result, diagnostics, logger)
```

Observed calls (lexical order): `print`, `BULLET_TEMPLATE.format`, `logger.warning`, `logger.info`.

Control points:

- L372: `if result.validation_messages`
- L373: `for message in result.validation_messages`
- L383: `for diagnostic in diagnostics`

### `convert_one_program` - L391-L506

```python
convert_one_program(*, program_path: Path, sheet_rows: list, dclgen_columns: list, copybook_fields: list, shared_diagnostics: list[str], output_dir: Path, project_root, src_dir, logger, logical_records: list | None=None) -> Path
```

Convert one retrieval program.

Observed calls (lexical order): `FileLoader`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `resolve_target_program_id`, `list`, `DIAG_SOURCE_FILE_TEMPLATE.format`, `diagnostics.append`, `DIAG_SOURCE_LEN_TEMPLATE.format`, `len`, `DIAG_DERIVED_PROGRAM_ID_TEMPLATE.format`, `logger.info`, `load_logical_records`, `_narrate_lrf`, `ConversionService`, `ConversionService().convert`, `ConversionInput`.
Another 13 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L470: `if getattr(result, 'production_blocked', False)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
