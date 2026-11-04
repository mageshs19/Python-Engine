# `mainframe/zowe_console.py`

Source: [mainframe/zowe_console.py](../../../mainframe/zowe_console.py) | 267 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `4c71dd444f4fe6991290ce20f4d6655600f0a34922181bf9e99edb347a53da3e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Console rendering for the pipeline. Printing and logging only.

## Module-level bindings

`WIDTH` (L43), `INNER` (L44), `HEAVY` (L45), `LIGHT` (L46), `INDENT` (L47), `BAR_WIDTH` (L48), `LABEL_WIDTH` (L49), `ROW_LABEL_WIDTH` (L50), `STATUS_WIDTH` (L51), `VALUE_WIDTH` (L52), `STAMP_FORMAT` (L53), `LOGGER_NAME` (L55), `LOG_FORMAT` (L56), `LOG_DATE_FORMAT` (L57), `BAR_FILLED_UNICODE` (L60), `BAR_EMPTY_UNICODE` (L61), `BAR_FILLED_ASCII` (L62), `BAR_EMPTY_ASCII` (L63), `NO_COLOUR_ENV` (L66), `COMPACT_ENV` (L67), `COLOUR_RESET` (L68), `COLOUR_DIM` (L69), `COLOUR_GREEN` (L70), `COLOUR_RED` (L71), `COLOUR_YELLOW` (L72), `STATUS_COLOURS` (L74), `COLOUR` (L106), `COMPACT` (L108), `__all__` (L252)

## Import declarations

```python
from __future__ import annotations
import logging
import os
import sys
from datetime import datetime
from mainframe.zowe_env import mask, setting_source
from mainframe.zowe_rules import NAME_HOST, NAME_PASSWORD, NAME_USER, STATUS_FAILED, STATUS_NOTHING, STATUS_OK, STATUS_SKIPPED
```

## Local dependency notes

- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_rules.py](zowe_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_commands.py](zowe_commands.md)
- [mainframe/zowe_pipeline.py](zowe_pipeline.md)
- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)
- [mainframe/zowe_steps.py](zowe_steps.md)

## Symbol contracts and control points

### `_detect_colour` - L83-L89

```python
_detect_colour() -> bool
```

Observed calls (lexical order): `os.environ.get`, `bool`, `sys.stdout.isatty`.

Control points:

- L84: `if os.environ.get(NO_COLOUR_ENV)`

### `_detect_glyphs` - L92-L103

```python
_detect_glyphs() -> tuple[str, str]
```

Block glyphs when the code page can encode them, else ASCII.

Observed calls (lexical order): `getattr`, `BAR_FILLED_UNICODE.encode`.

### `_paint` - L115-L118

```python
_paint(text: str, code: str) -> str
```

Observed calls (lexical order): `str`.

Control points:

- L116: `if not COLOUR or not code`

### `_status_cell` - L121-L123

```python
_status_cell(status: str) -> str
```

Pad BEFORE colouring, so escape codes never affect alignment.

Observed calls (lexical order): `STATUS_COLOURS.get`, `_paint`, `str`, `str(status).ljust`.

### `banner` - L127-L133

```python
banner(title: str) -> None
```

Observed calls (lexical order): `print`, `str`, `str(title).upper`, `datetime.now`, `datetime.now().strftime`.

Control points:

- L128: `if not COMPACT`

### `footer` - L136-L140

```python
footer() -> None
```

Observed calls (lexical order): `print`, `datetime.now`, `datetime.now().strftime`.

Control points:

- L137: `if not COMPACT`

### `section` - L143-L147

```python
section(title: str) -> None
```

Observed calls (lexical order): `print`, `str`, `str(title).upper`.

Control points:

- L144: `if not COMPACT`

### `header` - L150-L152

```python
header(title: str) -> None
```

Backward compatible with the earlier plain header.

Observed calls (lexical order): `section`.

### `row` - L155-L157

```python
row(label: str, value) -> None
```

Observed calls (lexical order): `str`, `print`.

### `bullets` - L160-L162

```python
bullets(lines) -> None
```

Observed calls (lexical order): `print`.

Control points:

- L161: `for line in lines or []`

### `warnings` - L165-L167

```python
warnings(lines) -> None
```

Observed calls (lexical order): `print`.

Control points:

- L166: `for line in lines or []`

### `step_start` - L171-L175

```python
step_start(index: int, total: int, label: str) -> None
```

Observed calls (lexical order): `print`, `str`, `str(label).upper`.

Control points:

- L172: `if not COMPACT`

### `step_line` - L178-L184

```python
step_line(index: int, total: int, label: str, status: str, seconds: float) -> None
```

Observed calls (lexical order): `print`, `str`, `_status_cell`.

### `summary` - L187-L207

```python
summary(results) -> None
```

Observed calls (lexical order): `print`, `section`, `_status_cell`.

Control points:

- L188: `if COMPACT`
- L196: `for result in results or []`
- L203: `if result.status == STATUS_FAILED`

### `verdict` - L210-L212

```python
verdict(text: str, failed: bool=False) -> None
```

Observed calls (lexical order): `print`, `_paint`.

### `credentials` - L216-L232

```python
credentials(artifact: str, connection) -> None
```

Report host / user / password source. The password is masked.

Observed calls (lexical order): `getattr`, `row`, `setting_source`, `mask`.

### `configure_logging` - L236-L245

```python
configure_logging(verbose: bool) -> None
```

Quiet by default. Only WARNING and above reach the console.

Observed calls (lexical order): `logging.basicConfig`, `logging.getLogger`, `logging.getLogger('urllib3').setLevel`.

Control points:

- L244: `if not verbose`

### `logger` - L248-L249

```python
logger() -> logging.Logger
```

Observed calls (lexical order): `logging.getLogger`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
