# `runners/batch/batch_models.py`

Source: [runners/batch/batch_models.py](../../../../runners/batch/batch_models.py) | 29 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `93b02d6fc32e0cede3fd010c5f0699ccd7d1cb30458d1b6aa68e654fea38e60f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch/batch_reporter.py](batch_reporter.md)
- [runners/batch/batch_validator.py](batch_validator.md)
- [runners/batch/program_converter.py](program_converter.md)
- [runners/batch/shared_input_loader.py](shared_input_loader.md)
- [runners/batch_program_runner.py](../batch_program_runner.md)

## Symbol contracts and control points

### `BatchMode` - L11-L18

```python
class BatchMode()
```

Describes one conversion mode (Retrieval or Update).

Declared class/data-model fields:

```python
name: str
program_dir: Path
output_dir: Path
apply_update_postprocess: bool
default_target_program_id: str = ''
```

### `SharedInputs` - L22-L29

```python
class SharedInputs()
```

Inputs loaded once and shared across every program in a batch.

Declared class/data-model fields:

```python
sheet_rows: list
dclgen_columns: list
copybook_fields: list
diagnostics: list[str] = field(default_factory=list)
logical_records: list = field(default_factory=list)
```

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
