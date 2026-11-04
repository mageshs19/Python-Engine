# `converter/ui/test_panel.py`

Source: [converter/ui/test_panel.py](../../../../converter/ui/test_panel.py) | 314 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `3711cae17eb369edf6603dff84c9c53a742ee809af0bd3e7c3edb455ba7f4356`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Streamlit panel for running the Python test suite.

## Module-level bindings

`STATE_RESULT` (L68), `STATE_STAMP` (L69)

## Import declarations

```python
from __future__ import annotations
import csv
import io
from datetime import datetime
import streamlit as st
from runners.pytest_runner import PytestRunner, TestRunResult
from rules.test_runner_rules import ALL_TESTS_LABEL, COLUMN_DURATION, COLUMN_MESSAGE, COLUMN_MODULE, COLUMN_OUTCOME, COLUMN_TEST, FILE_TIMESTAMP_FORMAT, MESSAGE_PREVIEW_LENGTH, OUTCOME_ICONS, RUN_TIMEOUT_SECONDS, TABLE_COLUMNS, UI_ALL_PASSED, UI_COMMAND_HEADER, UI_DETAIL_HEADER, UI_DOWNLOAD_CSV, UI_DOWNLOAD_LOG, UI_FAILURES_ONLY_LABEL, UI_FILE_CSV, UI_FILE_LOG, UI_HEADER, UI_INTRO, UI_KEYWORD_LABEL, UI_KEYWORD_PLACEHOLDER, UI_METRIC_DURATION, UI_METRIC_FAILED, UI_METRIC_PASSED, UI_METRIC_SKIPPED, UI_METRIC_TOTAL, UI_MIME_CSV, UI_MIME_TEXT, UI_NO_RESULT, UI_NO_TESTS_FOUND, UI_OUTPUT_HEADER, UI_RUN_BUTTON, UI_RUN_ERROR, UI_RUNNING, UI_SOME_FAILED, UI_TABLE_HEADER, UI_TARGET_LABEL, UI_TIMED_OUT, UI_VERBOSE_LABEL
```

## Local dependency notes

- [rules/test_runner_rules.py](../../rules/test_runner_rules.md)
- [runners/pytest_runner.py](../../runners/pytest_runner.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_page.py](main_page.md)

## Symbol contracts and control points

### `render_test_panel` - L72-L104

```python
render_test_panel() -> None
```

Render the Tests tab.

Observed calls (lexical order): `st.markdown`, `st.caption`, `PytestRunner`, `runner.has_tests`, `st.info`, `_render_controls`, `st.button`, `st.spinner`, `runner.run`, `datetime.now`, `datetime.now().strftime`, `st.session_state.get`, `_render_result`.

Control points:

- L79: `if not runner.has_tests()`
- L86: `if st.button(UI_RUN_BUTTON, type='primary', key='test_panel_run')`
- L100: `if result is None`

### `_render_controls` - L110-L136

```python
_render_controls(runner: PytestRunner) -> tuple[str, str, bool]
```

Observed calls (lexical order): `st.columns`, `st.selectbox`, `runner.available_targets`, `st.text_input`, `st.checkbox`.

### `_render_result` - L142-L155

```python
_render_result(result: TestRunResult) -> None
```

Observed calls (lexical order): `UI_RUN_ERROR.format`, `st.error`, `UI_TIMED_OUT.format`, `_render_metrics`, `_render_verdict`, `_render_table`, `_render_failures`, `_render_downloads`, `_render_raw_output`.

Control points:

- L143: `if result.error`
- L147: `if result.timed_out`

### `_render_metrics` - L158-L167

```python
_render_metrics(result: TestRunResult) -> None
```

Observed calls (lexical order): `st.columns`, `columns[0].metric`, `columns[1].metric`, `columns[2].metric`, `columns[3].metric`, `columns[4].metric`.

### `_render_verdict` - L170-L180

```python
_render_verdict(result: TestRunResult) -> None
```

Observed calls (lexical order): `st.success`, `st.error`, `UI_SOME_FAILED.format`.

Control points:

- L171: `if result.timed_out`
- L174: `if result.is_green`

### `_render_table` - L183-L213

```python
_render_table(result: TestRunResult) -> None
```

Observed calls (lexical order): `st.markdown`, `st.checkbox`, `st.info`, `OUTCOME_ICONS.get`, `_preview`, `st.dataframe`, `list`.

Control points:

- L193: `if not cases`

### `_render_failures` - L216-L228

```python
_render_failures(result: TestRunResult) -> None
```

Observed calls (lexical order): `st.markdown`, `enumerate`, `OUTCOME_ICONS.get`, `st.expander`, `st.code`.

Control points:

- L217: `if not result.failing`
- L222: `for (index, case) in enumerate(result.failing)`
- L225: `if case.message`
- L227: `if case.detail`

### `_render_downloads` - L231-L252

```python
_render_downloads(result: TestRunResult) -> None
```

Observed calls (lexical order): `st.session_state.get`, `st.columns`, `st.download_button`, `_as_csv`, `UI_FILE_CSV.format`, `_as_log`, `UI_FILE_LOG.format`.

### `_render_raw_output` - L255-L264

```python
_render_raw_output(result: TestRunResult) -> None
```

Observed calls (lexical order): `UI_OUTPUT_HEADER.replace`, `st.expander`, `st.markdown`, `st.code`, `result.stdout.strip`, `result.stderr.strip`.

Control points:

- L260: `if result.stdout.strip()`
- L263: `if result.stderr.strip()`

### `_as_csv` - L270-L286

```python
_as_csv(result: TestRunResult) -> str
```

Observed calls (lexical order): `io.StringIO`, `csv.writer`, `list`, `writer.writerow`, `case.message.replace`, `case.message.replace('\n', ' ').strip`, `buffer.getvalue`.

Control points:

- L275: `for case in result.cases`

### `_as_log` - L289-L307

```python
_as_log(result: TestRunResult) -> str
```

Observed calls (lexical order): `'\n'.join`.

### `_preview` - L310-L314

```python
_preview(text: str) -> str
```

Observed calls (lexical order): `' '.join`, `str`, `str(text or '').split`, `len`.

Control points:

- L312: `if len(clean) <= MESSAGE_PREVIEW_LENGTH`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
