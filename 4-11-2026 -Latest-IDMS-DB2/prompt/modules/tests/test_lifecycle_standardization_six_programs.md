# `tests/test_lifecycle_standardization_six_programs.py`

Source: [tests/test_lifecycle_standardization_six_programs.py](../../../tests/test_lifecycle_standardization_six_programs.py) | 135 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `1d33274479d03e6ceb5a5878925fb331bafe1c44a0938c5eef4445805dfea51e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Production regression checks for lifecycle standardization across all six programs.

## Module-level bindings

`ROOT` (L14), `OUTPUTS` (L15)

## Import declarations

```python
from __future__ import annotations
import re
from pathlib import Path
import pytest
from converter.composers.lifecycle_standardization_composer import LifecycleStandardizationComposer
from converter.services.final_generated_output_service import FinalGeneratedOutputService
```

## Local dependency notes

- [converter/composers/lifecycle_standardization_composer.py](../converter/composers/lifecycle_standardization_composer.md)
- [converter/services/final_generated_output_service.py](../converter/services/final_generated_output_service.md)

## Symbol contracts and control points

### `_logical` - L25-L28

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].strip`, `line.strip`.

Control points:

- L26: `if len(line) >= 7 and line[:6].isdigit()`

### `_paragraph_labels` - L31-L37

```python
_paragraph_labels(text: str) -> list[str]
```

Observed calls (lexical order): `text.splitlines`, `_logical`, `re.fullmatch`, `body.upper`, `labels.append`.

Control points:

- L33: `for line in text.splitlines()`
- L35: `if re.fullmatch('[A-Z0-9][A-Z0-9-]*\\.', body, re.I)`

### `_diagnostic_lines` - L40-L46

```python
_diagnostic_lines(text: str) -> list[str]
```

Observed calls (lexical order): `_logical`, `text.splitlines`, `line.lstrip`, `line.lstrip().startswith`, `re.search`.

### `_sql_location_lines` - L49-L59

```python
_sql_location_lines(text: str) -> list[str]
```

Observed calls (lexical order): `text.splitlines`, `_logical`, `body.startswith`, `body.upper`, `re.sub`, `result.append`.

Control points:

- L51: `for line in text.splitlines()`
- L53: `if 'SQL-LOCATION' not in body.upper() or body.startswith(('*', '/'))`

### `test_lifecycle_standardization_preserves_sql_error_behavior` - L63-L115

```python
test_lifecycle_standardization_preserves_sql_error_behavior(program: str, filename: str)
```

Observed calls (lexical order): `path.read_text`, `LifecycleStandardizationComposer`, `composer.compose`, `_paragraph_labels`, `labels.count`, `output.count`, `source.count`, `output.upper`, `output.upper().count`, `source.upper`, `source.upper().count`, `_sql_location_lines`, `_diagnostic_lines`, `list`, `any`.

Control points:

- L71: `for paragraph in ('0000-MAIN-PROCEDURE.', '1000-INITIALIZE-PROGRAM.', '2000-PROCESS-PROGRAM.', '3000-FINALIZE-PROGRAM.')`
- L92: `if program == 'VMDZ1567'`
- L101: `if program in {'VMDZ4302', 'VMDZ4420'}`
- L102: `for label in ('2100-OPEN-DZBEFFC1.', '2200-FETCH-DZBEFFC1.', '2300-CLOSE-DZBEFFC1.', '3100-OPEN-DZEVEFC1.', '3200-FETCH-DZEVEFC1.', '3300-CLOSE-DZEVEFC1.')`
- L107: `if program == 'VMDZ7200'`
- L111: `for label in ('2100-OPEN-DZBFASC1.', '2200-FETCH-DZBFASC1.', '2300-CLOSE-DZBFASC1.')`

### `test_final_output_service_keeps_all_six_programs_fixed_format` - L118-L135

```python
test_final_output_service_keeps_all_six_programs_fixed_format()
```

Observed calls (lexical order): `FinalGeneratedOutputService`, `OUTPUTS.items`, `path.read_text`, `_paragraph_labels`, `service.apply`, `all`, `len`, `output.splitlines`.

Control points:

- L120: `for (program, filename) in OUTPUTS.items()`
- L130: `for label in ('0000-MAIN-PROCEDURE.', '1000-INITIALIZE-PROGRAM.', '2000-PROCESS-PROGRAM.', '3000-FINALIZE-PROGRAM.')`
- L134: `if label not in source_labels`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
