# `runners/batch/program_converter.py`

Source: [runners/batch/program_converter.py](../../../../runners/batch/program_converter.py) | 220 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `475ccc9067ba7ea438c5800cab66df901c4d380f498d7acdc0bb1e49d1737c70`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`DIAG_RETRIEVAL_SKIPPED_TEMPLATE` (L38)

## Import declarations

```python
from __future__ import annotations
from converter.services.source_copybook_members_loader import read_source_copybook_members as _read_source_copybook_members
from datetime import datetime
from pathlib import Path
from converter.domain.models import ConversionInput
from converter.infrastructure.file_loader import FileLoader
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.pipeline.conversion_service import ConversionService
from converter.resolvers.program_kind_resolver import ProgramKindResolver
from patterns.lrf_patterns import COPY_IDMS_LR_PATTERN
from rules.batch_runner_messages import DIAG_SOURCE_FILE_TEMPLATE, DIAG_SOURCE_LEN_TEMPLATE
from rules.batch_runner_rules import AUTO_FIX_PIC_LENGTH_MISMATCHES_DEFAULT, COBOL_TEXT_ENCODING, OUTPUT_FILE_EXTENSION, OUTPUT_FILE_NAME_TEMPLATE, OUTPUT_TIMESTAMP_FORMAT
from rules.lrf_rules import DIAG_LRF_NO_RECORDS_IN_SCOPE, DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE, LOG_LRF_TOTAL_RECORDS, LRF_VALIDATION_MESSAGES
from .batch_models import BatchMode, SharedInputs
from .batch_reporter import log_program_result
from .update_postprocess_pipeline import apply_update_postprocess
```

## Local dependency notes

- [converter/domain/models.py](../../converter/domain/models.md)
- [converter/infrastructure/file_loader.py](../../converter/infrastructure/file_loader.md)
- [converter/infrastructure/local_uploaded_file.py](../../converter/infrastructure/local_uploaded_file.md)
- [converter/pipeline/conversion_service.py](../../converter/pipeline/conversion_service.md)
- [converter/resolvers/program_kind_resolver.py](../../converter/resolvers/program_kind_resolver.md)
- [converter/services/source_copybook_members_loader.py](../../converter/services/source_copybook_members_loader.md)
- [patterns/lrf_patterns.py](../../patterns/lrf_patterns.md)
- [rules/batch_runner_messages.py](../../rules/batch_runner_messages.md)
- [rules/batch_runner_rules.py](../../rules/batch_runner_rules.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)
- [runners/batch/batch_models.py](batch_models.md)
- [runners/batch/batch_reporter.py](batch_reporter.md)
- [runners/batch/update_postprocess_pipeline.py](update_postprocess_pipeline.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch_program_runner.py](../batch_program_runner.md)

## Symbol contracts and control points

### `build_output_path` - L44-L76

```python
build_output_path(*, mode: BatchMode, program_path: Path, target_program_id: str='') -> Path
```

The output path for one converted program.

Observed calls (lexical order): `datetime.now`, `datetime.now().strftime`, `str`, `str(target_program_id or '').strip`, `OUTPUT_FILE_NAME_TEMPLATE.format`.

### `_logical_records` - L82-L88

```python
_logical_records(shared_inputs: SharedInputs) -> list
```

LRF logical records from the shared inputs.

Observed calls (lexical order): `getattr`, `list`.

### `_source_uses_logical_records` - L91-L101

```python
_source_uses_logical_records(source_text: str) -> list[str]
```

Logical record names the SOURCE program copies via COPY IDMS LR.

Observed calls (lexical order): `str`, `str(source_text or '').splitlines`, `COPY_IDMS_LR_PATTERN.search`, `match.group`, `str(match.group('lr') or '').strip`, `str(match.group('lr') or '').strip().upper`, `names.append`.

Control points:

- L94: `for raw_line in str(source_text or '').splitlines()`
- L96: `if not match`
- L99: `if name and name not in names`

### `_narrate_lrf` - L104-L137

```python
_narrate_lrf(*, source_text: str, logical_records: list, diagnostics: list[str], logger) -> None
```

Record what LRF metadata this program run will see.

Observed calls (lexical order): `', '.join`, `getattr`, `str`, `diagnostics.append`, `DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE.format`, `len`, `logger.info`, `_source_uses_logical_records`, `logger.warning`.

Control points:

- L117: `if logical_records`
- L134: `if used and (not logical_records)`

### `convert_one_program` - L140-L220

```python
convert_one_program(*, mode: BatchMode, program_path: Path, shared_inputs: SharedInputs, target_program_id: str, logger) -> Path
```

Observed calls (lexical order): `FileLoader`, `LocalUploadedFile`, `file_loader.read_uploaded_text`, `list`, `diagnostics.append`, `DIAG_SOURCE_FILE_TEMPLATE.format`, `DIAG_SOURCE_LEN_TEMPLATE.format`, `len`, `_logical_records`, `_narrate_lrf`, `ConversionService`, `service.convert`, `ConversionInput`, `_read_source_copybook_members`, `ProgramKindResolver`, `ProgramKindResolver().is_update`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L183: `if mode.apply_update_postprocess`
- L187: `if is_update`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
