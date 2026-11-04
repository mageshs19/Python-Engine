# `mainframe/zowe_pipeline_steps.py`

Source: [mainframe/zowe_pipeline_steps.py](../../../mainframe/zowe_pipeline_steps.py) | 157 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `cea37c3afc883c8f4dc8e3efe82bad9bef9bec6d99bd1547bff1045b1db605d6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The four executable pipeline steps.

## Module-level bindings

`COBOL_GLOB` (L40), `STEP_FUNCTIONS` (L152)

## Import declarations

```python
from __future__ import annotations
import time
from dataclasses import dataclass
from mainframe.zowe_console import bullets, row, warnings
from mainframe.zowe_fetcher import ZoweFetcher
from mainframe.zowe_rules import MAPPING_MISSING_TEMPLATE, STATUS_FAILED, STATUS_NOTHING, STATUS_OK, STATUS_SKIPPED, STEP_CONVERT, STEP_FETCH, STEP_REVIEW, STEP_UPLOAD
from mainframe.zowe_steps import run_convert, run_review
from mainframe.zowe_workspace import count_files, clean_generated, mapping_dir, output_dir, program_dir
from mainframe.zowe_writer import upload_converted_folder
from mainframe.zowe_copybook_upload import require_copybook_upload_configuration, upload_generated_copybooks
from mainframe.zowe_semantic_release_gate import audit_generated_batch
```

## Local dependency notes

- [mainframe/zowe_console.py](zowe_console.md)
- [mainframe/zowe_copybook_upload.py](zowe_copybook_upload.md)
- [mainframe/zowe_fetcher.py](zowe_fetcher.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_semantic_release_gate.py](zowe_semantic_release_gate.md)
- [mainframe/zowe_steps.py](zowe_steps.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)
- [mainframe/zowe_writer.py](zowe_writer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_pipeline.py](zowe_pipeline.md)

## Symbol contracts and control points

### `StepResult` - L44-L52

```python
class StepResult()
```

Declared class/data-model fields:

```python
step: str
status: str
seconds: float = 0.0
code: int = 0
```

### `StepResult.failed` - L51-L52

```python
failed(self) -> bool
```

### `step_fetch` - L55-L79

```python
step_fetch(quiet: bool) -> StepResult
```

Observed calls (lexical order): `time.perf_counter`, `ZoweFetcher`, `ZoweFetcher().fetch_all`, `result.get`, `next`, `line.startswith`, `programs.replace`, `row`, `fetched.replace`, `warnings`, `StepResult`.

Control points:

- L59: `if not quiet`
- L70: `if programs`
- L72: `if fetched`

### `step_convert` - L82-L97

```python
step_convert(quiet: bool) -> StepResult
```

Observed calls (lexical order): `count_files`, `mapping_dir`, `MAPPING_MISSING_TEMPLATE.format`, `print`, `StepResult`, `program_dir`, `clean_generated`, `run_convert`.

Control points:

- L83: `if count_files(mapping_dir()) == 0`
- L87: `if count_files(program_dir()) == 0`

### `step_review` - L100-L115

```python
step_review(quiet: bool) -> StepResult
```

Observed calls (lexical order): `count_files`, `output_dir`, `StepResult`, `run_review`, `audit_generated_batch`, `warnings`, `bullets`.

Control points:

- L101: `if count_files(output_dir(), COBOL_GLOB) == 0`
- L106: `if not semantic_passed`
- L108: `if not quiet`
- L112: `if code == 0 and (not semantic_passed)`

### `step_upload` - L118-L149

```python
step_upload(quiet: bool) -> StepResult
```

Observed calls (lexical order): `time.perf_counter`, `count_files`, `output_dir`, `StepResult`, `run_review`, `audit_generated_batch`, `warnings`, `require_copybook_upload_configuration`, `upload_generated_copybooks`, `upload_converted_folder`, `bullets`.

Control points:

- L121: `if count_files(output_dir(), COBOL_GLOB) == 0`
- L129: `if code != 0 or not semantic_passed`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
