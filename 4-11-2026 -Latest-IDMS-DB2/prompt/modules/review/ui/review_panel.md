# `review/ui/review_panel.py`

Source: [review/ui/review_panel.py](../../../../review/ui/review_panel.py) | 236 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `9fea1b48b95e922ddd7fa4f89c74d43e37acc4f28b9714380c4bf67769d663b0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Streamlit panel. Reviews whatever is currently in session state.

## Module-level bindings

`IDMS_WRITE` (L26), `STATE_KEY` (L29), `STATE_STAMP` (L30), `TEXT_ENCODING` (L31)

## Import declarations

```python
from __future__ import annotations
import csv
import hashlib
import io
import re
import streamlit as st
from review.engine.context import KIND_RETRIEVAL, KIND_UPDATE, ReviewContext
from review.engine.models import Outcome
from review.engine.reviewer import Reviewer, blockers, is_accepted
from review.report import csv_writer, text_writer
from review.standards import wording as w
```

## Local dependency notes

- [review/engine/context.py](../engine/context.md)
- [review/engine/models.py](../engine/models.md)
- [review/engine/reviewer.py](../engine/reviewer.md)
- [review/report/__init__.py](../report/__init__.md)
- [review/report/csv_writer.py](../report/csv_writer.md)
- [review/report/text_writer.py](../report/text_writer.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/wording.py](../standards/wording.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_page.py](../../converter/ui/main_page.md)

## Symbol contracts and control points

### `_kind` - L34-L40

```python
_kind(source_text: str) -> str
```

UPDATE when the source contains an IDMS write verb.

Observed calls (lexical order): `IDMS_WRITE.search`, `str`.

### `_fingerprint` - L43-L60

```python
_fingerprint() -> str
```

Identity of the program currently held in session state.

Observed calls (lexical order): `st.session_state.get`, `str`, `hashlib.sha1`, `hashlib.sha1(converted.encode(TEXT_ENCODING, errors='replace')).hexdigest`, `converted.encode`, `'|'.join`, `len`.

### `build_context` - L63-L78

```python
build_context() -> ReviewContext
```

Observed calls (lexical order): `st.session_state.get`, `ReviewContext`, `_kind`.

### `render_review_panel` - L81-L114

```python
render_review_panel() -> None
```

Observed calls (lexical order): `st.markdown`, `st.session_state.get`, `_discard`, `st.info`, `_fingerprint`, `_current_result`, `st.caption`, `w.UI_TARGET.format`, `_kind`, `st.columns`, `st.button`, `Reviewer`, `Reviewer().review`, `build_context`, `_render_verdict`, `_render_totals`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L84: `if not st.session_state.get('converted_cobol')`
- L100: `if st.button(w.UI_RUN, type='primary', key='review_run')`
- L105: `if result is None`

### `_discard` - L118-L120

```python
_discard() -> None
```

Observed calls (lexical order): `st.session_state.pop`.

### `_current_result` - L123-L132

```python
_current_result(current: str)
```

The stored report, but only when it belongs to this program.

Observed calls (lexical order): `st.session_state.get`, `_discard`, `st.warning`.

Control points:

- L126: `if result is None`
- L128: `if st.session_state.get(STATE_STAMP) == current`

### `_render_verdict` - L136-L148

```python
_render_verdict(result) -> None
```

Observed calls (lexical order): `st.markdown`, `w.UI_PROGRAM.format`, `is_accepted`, `st.success`, `st.error`, `w.UI_REJECTED.format`, `', '.join`, `blockers`.

Control points:

- L143: `if is_accepted(result)`

### `_render_totals` - L151-L163

```python
_render_totals(result) -> None
```

Observed calls (lexical order): `st.columns`, `c1.metric`, `c2.metric`, `c3.metric`, `c4.metric`, `st.caption`, `w.UI_CRITERIA.format`.

### `_render_detail` - L166-L188

```python
_render_detail(result) -> None
```

Observed calls (lexical order): `st.columns`, `st.checkbox`, `w.UI_CHECK_LABEL.format`, `st.expander`, `_render_criteria`.

Control points:

- L177: `for check in result.checks`
- L178: `if failures_only and check.outcome is not Outcome.FAIL`

### `_render_criteria` - L191-L209

```python
_render_criteria(check, show_skips: bool) -> None
```

Observed calls (lexical order): `st.markdown`, `w.UI_CRITERION.format`, `st.caption`, `st.code`, `'\n'.join`, `f.render`.

Control points:

- L192: `for crit in check.criteria`
- L193: `if crit.outcome is Outcome.PASS`
- L195: `if crit.outcome is Outcome.SKIPPED and (not show_skips)`
- L203: `if crit.note`
- L205: `if crit.findings`

### `_render_downloads` - L212-L236

```python
_render_downloads(result) -> None
```

Observed calls (lexical order): `st.markdown`, `(result.program_name or w.UI_DEFAULT_STEM).replace`, `st.columns`, `st.download_button`, `text_writer.render`, `w.UI_FILE_TEXT.format`, `io.StringIO`, `csv.writer`, `writer.writerow`, `csv_writer.rows`, `writer.writerows`, `buffer.getvalue`, `w.UI_FILE_CSV.format`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
