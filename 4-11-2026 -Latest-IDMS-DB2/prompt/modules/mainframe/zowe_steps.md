# `mainframe/zowe_steps.py`

Source: [mainframe/zowe_steps.py](../../../mainframe/zowe_steps.py) | 184 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `107e1fd7d9468b70c9944472f270e8897f72a32987fe1b9538dbfef11f1ae284`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Launches the convert and review runners as subprocesses.

## Module-level bindings

`PROJECT_ROOT` (L36), `RUNNER_MISSING_TEMPLATE` (L38), `TRANSCRIPT_TEMPLATE` (L39), `TRANSCRIPT_STAMP` (L40), `CHILD_INDENT` (L41), `WARNINGS_KEY` (L45), `WARNINGS_VALUE` (L46), `EXIT_RUNNER_MISSING` (L48), `__all__` (L184)

## Import declarations

```python
from __future__ import annotations
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from mainframe.zowe_console import row, warnings
from mainframe.zowe_rules import CONVERT_RUNNER, IDMS_INPUT_DIR_KEY, PYTHONPATH_ENTRIES, PYTHONPATH_KEY, REVIEW_KIND, REVIEW_RUNNER, UNBUFFERED_KEY
from mainframe.zowe_step_output import digest
from mainframe.zowe_workspace import output_dir, review_dir, workspace_root
```

## Local dependency notes

- [mainframe/zowe_console.py](zowe_console.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_step_output.py](zowe_step_output.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)

## Symbol contracts and control points

### `subprocess_environment` - L52-L66

```python
subprocess_environment() -> dict[str, str]
```

The ONLY contract between the pipeline and a runner.

Observed calls (lexical order): `dict`, `str`, `workspace_root`, `os.pathsep.join`, `env.setdefault`.

### `_logs_dir` - L70-L72

```python
_logs_dir() -> Path
```

Workspace Logs folder. Derived, so zowe_workspace need not export it.

Observed calls (lexical order): `workspace_root`.

### `_write_transcript` - L75-L82

```python
_write_transcript(step: str, lines: list[str]) -> Path
```

Observed calls (lexical order): `_logs_dir`, `folder.mkdir`, `TRANSCRIPT_TEMPLATE.format`, `datetime.now`, `datetime.now().strftime`, `'\n'.join`, `path.write_text`.

### `_render_digest` - L86-L112

```python
_render_digest(text: str, _transcript: Path) -> None
```

Observed calls (lexical order): `digest`, `row`, `len`, `warnings`.

Control points:

- L89: `if facts['mapping_rows']`
- L91: `if facts['dclgen_columns']`
- L93: `if facts['copybook_fields']`
- L95: `if facts['lrf_records']`
- L98: `if facts['outputs']`
- L102: `if review`
- L109: `if facts['errors']`
- L111: `if facts['crashed']`

### `_run` - L116-L148

```python
_run(command: list[str], step: str='step', verbose: bool=False) -> tuple[int, float]
```

Observed calls (lexical order): `time.perf_counter`, `subprocess.Popen`, `str`, `subprocess_environment`, `line.rstrip`, `captured.append`, `print`, `process.wait`, `_write_transcript`, `'\n'.join`, `_render_digest`.

Control points:

- L135: `for line in process.stdout`
- L138: `if verbose and stripped`
- L145: `if not verbose`

### `run_convert` - L151-L157

```python
run_convert(verbose: bool=False) -> tuple[int, float]
```

Observed calls (lexical order): `runner.is_file`, `RUNNER_MISSING_TEMPLATE.format`, `print`, `_run`, `str`.

Control points:

- L153: `if not runner.is_file()`

### `run_review` - L160-L181

```python
run_review(quiet: bool=False, verbose: bool=False) -> tuple[int, float]
```

Observed calls (lexical order): `runner.is_file`, `RUNNER_MISSING_TEMPLATE.format`, `print`, `str`, `output_dir`, `review_dir`, `workspace_root`, `command.append`, `_run`.

Control points:

- L162: `if not runner.is_file()`
- L178: `if quiet`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
