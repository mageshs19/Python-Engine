# `mainframe/zowe_pipeline.py`

Source: [mainframe/zowe_pipeline.py](../../../mainframe/zowe_pipeline.py) | 172 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `9bc1c3223293bab5675320a76c0db7d434dad27c927f078441c761aed986e431`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> One entry point for the whole Zowe flow.

## Module-level bindings

`SKIP_REASON` (L63)

## Import declarations

```python
from __future__ import annotations
import argparse
import sys
from mainframe.zowe_commands import command_clean, command_init, command_plan, command_show
from mainframe.zowe_console import banner, configure_logging, footer, logger, row, step_line, step_start, summary, verdict, warnings
from mainframe.zowe_pipeline_steps import STEP_FUNCTIONS, StepResult
from mainframe.zowe_rules import EXIT_ERROR, EXIT_NOTHING, EXIT_OK, PIPELINE_COMMANDS, PIPELINE_STEPS, STATUS_FAILED, STATUS_NOTHING, STATUS_OK, STATUS_SKIPPED, STEP_ALL, STEP_CLEAN, STEP_INIT, STEP_PLAN, STEP_SHOW, VERDICT_FAILED_TEMPLATE, VERDICT_OK
from mainframe.zowe_workspace import ensure_workspace
```

## Local dependency notes

- [mainframe/zowe_commands.py](zowe_commands.md)
- [mainframe/zowe_console.py](zowe_console.md)
- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)

## Symbol contracts and control points

### `step_range` - L66-L77

```python
step_range(from_step: str, to_step: str) -> tuple[str, ...]
```

A contiguous slice of PIPELINE_STEPS. Blank means open-ended.

Observed calls (lexical order): `list`, `steps.index`, `len`, `ValueError`, `tuple`.

Control points:

- L72: `if start >= end`

Explicit raises: `ValueError(f'--from {from_step or steps[0]} comes after --to {to_step or steps[-1]}')`.

### `_report` - L80-L86

```python
_report(result: StepResult) -> None
```

Observed calls (lexical order): `warnings`, `row`.

Control points:

- L81: `if result.status == STATUS_FAILED`
- L83: `if result.status == STATUS_SKIPPED`
- L85: `if result.status == STATUS_NOTHING`

### `run_steps` - L89-L112

```python
run_steps(steps: tuple[str, ...], quiet: bool) -> int
```

Observed calls (lexical order): `ensure_workspace`, `len`, `banner`, `enumerate`, `step_start`, `STEP_FUNCTIONS[step]`, `results.append`, `step_line`, `_report`, `summary`, `VERDICT_FAILED_TEMPLATE.format`, `verdict`, `footer`, `any`.

Control points:

- L95: `for (index, step) in enumerate(steps, start=1)`
- L102: `if result.status == STATUS_FAILED`

### `parse_arguments` - L115-L137

```python
parse_arguments() -> argparse.Namespace
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`.

### `run` - L140-L154

```python
run() -> int
```

Observed calls (lexical order): `parse_arguments`, `configure_logging`, `command_init`, `command_show`, `command_plan`, `command_clean`, `run_steps`, `step_range`.

Control points:

- L144: `if args.command == STEP_INIT`
- L146: `if args.command == STEP_SHOW`
- L148: `if args.command == STEP_PLAN`
- L150: `if args.command == STEP_CLEAN`
- L152: `if args.command == STEP_ALL`

### `main` - L157-L168

```python
main() -> None
```

Observed calls (lexical order): `run`, `sys.exit`, `print`, `logger`, `logger().error`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
