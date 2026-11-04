# `runners/update/update_program_converter.py`

Source: [runners/update/update_program_converter.py](../../../../runners/update/update_program_converter.py) | 290 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `d2deeeeeec74b173530d099b7994a8ec3f40753e4969a219a5bd98ea5a0aa333`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from datetime import datetime
from pathlib import Path
from converter.domain.models import ConversionInput
from converter.infrastructure.file_loader import FileLoader
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.pipeline.conversion_service import ConversionService
from converter.parsers.cobol_parser import CobolParser
from converter.services.name_derivation_resolver import NameDerivationResolver
from rules.update_runner_messages import BULLET_TEMPLATE, DIAG_DERIVED_PROGRAM_ID_TEMPLATE, DIAG_SOURCE_FILE_TEMPLATE, DIAG_SOURCE_LEN_TEMPLATE, HEADER_DIAGNOSTICS, HEADER_INPUT_SUMMARY, HEADER_SELECTED_INPUT_FILES, HEADER_VALIDATION_MESSAGES, LOG_DERIVED_PROGRAM_ID, LOG_GENERATION_COMPLETED, LOG_OUTPUT_CREATED, LOG_SOURCE_FILE, LOG_SOURCE_LEN, NO_VALIDATION_MESSAGES, PRESERVE_SOURCE_LABEL, PRINT_GENERATION_COMPLETED, PRINT_INPUT_PROGRAM_TEMPLATE, PRINT_OUTPUT_CREATED_TEMPLATE, RULE_DIAGNOSTICS, RULE_INPUT_SUMMARY, RULE_SELECTED_INPUT_FILES, RULE_VALIDATION_MESSAGES, SELECTED_COBOL_SOURCE_TEMPLATE, SELECTED_COPYBOOK_HEADER, SELECTED_COPYBOOK_NONE, SELECTED_DCLGEN_HEADER, SELECTED_PATH_BULLET_TEMPLATE, SELECTED_SHEET_MAPPING_TEMPLATE, SUMMARY_COBOL_LEN_TEMPLATE, SUMMARY_COPYBOOK_FIELDS_TEMPLATE, SUMMARY_DCLGEN_COLUMNS_TEMPLATE, SUMMARY_PROJECT_ROOT_TEMPLATE, SUMMARY_SHEET_ROWS_TEMPLATE, SUMMARY_SRC_DIR_TEMPLATE, SUMMARY_TARGET_PROGRAM_ID_TEMPLATE
from rules.update_runner_rules import AUTO_FIX_PIC_LENGTH_MISMATCHES_DEFAULT, COBOL_TEXT_ENCODING, OUTPUT_FILE_EXTENSION, OUTPUT_FILE_NAME_TEMPLATE, OUTPUT_TIMESTAMP_FORMAT
from .update_input_selector import selected_copybook_paths, selected_dclgen_paths, selected_mapping_sheet_path
from .update_postprocess_pipeline import enhance_update_program
from patterns.lrf_patterns import COPY_IDMS_LR_PATTERN
from rules.lrf_rules import DIAG_LRF_NO_RECORDS_IN_SCOPE, DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE, LRF_VALIDATION_MESSAGES
from .update_input_loader import load_logical_records
```

## Local dependency notes

- [converter/domain/models.py](../../converter/domain/models.md)
- [converter/infrastructure/file_loader.py](../../converter/infrastructure/file_loader.md)
- [converter/infrastructure/local_uploaded_file.py](../../converter/infrastructure/local_uploaded_file.md)
- [converter/parsers/cobol_parser.py](../../converter/parsers/cobol_parser.md)
- [converter/pipeline/conversion_service.py](../../converter/pipeline/conversion_service.md)
- [converter/services/name_derivation_resolver.py](../../converter/services/name_derivation_resolver.md)
- [patterns/lrf_patterns.py](../../patterns/lrf_patterns.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)
- [rules/update_runner_messages.py](../../rules/update_runner_messages.md)
- [rules/update_runner_rules.py](../../rules/update_runner_rules.md)
- [runners/update/update_input_loader.py](update_input_loader.md)
- [runners/update/update_input_selector.py](update_input_selector.md)
- [runners/update/update_postprocess_pipeline.py](update_postprocess_pipeline.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/convert_programs.py](../convert_programs.md)
- [runners/run_update.py](../run_update.md)
- [tests/test_vmdz1526_lrf_update_integration.py](../../tests/test_vmdz1526_lrf_update_integration.md)

## Symbol contracts and control points

### `resolve_target_program_id` - L73-L78

```python
resolve_target_program_id(source_text: str) -> str
```

Derive the target PROGRAM-ID from the source (VM...BD... -> VMDZ...).

Observed calls (lexical order): `CobolParser`, `CobolParser().program_id`, `NameDerivationResolver`, `NameDerivationResolver().derive`.

Control points:

- L76: `if not source_id`

### `_build_output_path` - L81-L110

```python
_build_output_path(output_dir: Path, program_path: Path, target_program_id: str='') -> Path
```

Name the artefact after the DERIVED PROGRAM-ID when one resolves.

Observed calls (lexical order): `str`, `str(target_program_id or '').strip`, `datetime.now`, `datetime.now().strftime`, `OUTPUT_FILE_NAME_TEMPLATE.format`.

### `_print_summary` - L112-L145

```python
_print_summary(*, program_path, sheet_rows, dclgen_columns, copybook_fields, idms_len, target_program_id, project_root, src_dir)
```

Observed calls (lexical order): `print`, `SUMMARY_PROJECT_ROOT_TEMPLATE.format`, `SUMMARY_SRC_DIR_TEMPLATE.format`, `SUMMARY_SHEET_ROWS_TEMPLATE.format`, `len`, `SUMMARY_DCLGEN_COLUMNS_TEMPLATE.format`, `SUMMARY_COPYBOOK_FIELDS_TEMPLATE.format`, `SUMMARY_COBOL_LEN_TEMPLATE.format`, `SUMMARY_TARGET_PROGRAM_ID_TEMPLATE.format`, `SELECTED_SHEET_MAPPING_TEMPLATE.format`, `selected_mapping_sheet_path`, `SELECTED_COBOL_SOURCE_TEMPLATE.format`, `selected_dclgen_paths`, `SELECTED_PATH_BULLET_TEMPLATE.format`, `selected_copybook_paths`.

Control points:

- L136: `for path in selected_dclgen_paths()`
- L140: `if copybooks`
- L142: `for path in copybooks`

### `_print_results` - L148-L166

```python
_print_results(result, diagnostics, logger)
```

Observed calls (lexical order): `print`, `BULLET_TEMPLATE.format`, `logger.warning`, `logger.info`.

Control points:

- L153: `if result.validation_messages`
- L154: `for message in result.validation_messages`
- L164: `for diagnostic in diagnostics`

### `_narrate_lrf` - L168-L206

```python
_narrate_lrf(*, source_text: str, logical_records: list, diagnostics: list[str], logger) -> None
```

Record what LRF metadata this program run will see.

Observed calls (lexical order): `', '.join`, `getattr`, `str`, `diagnostics.append`, `DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE.format`, `len`, `str(source_text or '').splitlines`, `COPY_IDMS_LR_PATTERN.search`, `match.group`, `str(match.group('lr') or '').strip`, `str(match.group('lr') or '').strip().upper`, `used.append`, `logger.warning`.

Control points:

- L181: `if logical_records`
- L195: `for raw_line in str(source_text or '').splitlines()`
- L197: `if not match`
- L200: `if name and name not in used`
- L203: `if used and (not logical_records)`

### `convert_one_program` - L208-L290

```python
convert_one_program(*, program_path: Path, sheet_rows: list, dclgen_columns: list, copybook_fields: list, shared_diagnostics: list[str], output_dir: Path, project_root, src_dir, logger) -> Path
```

Observed calls (lexical order): `FileLoader`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `resolve_target_program_id`, `list`, `DIAG_SOURCE_FILE_TEMPLATE.format`, `diagnostics.append`, `DIAG_SOURCE_LEN_TEMPLATE.format`, `len`, `DIAG_DERIVED_PROGRAM_ID_TEMPLATE.format`, `logger.info`, `load_logical_records`, `_narrate_lrf`, `ConversionService`, `ConversionService().convert`, `ConversionInput`.
Another 8 call expressions are in this source span; the list is intentionally bounded.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
