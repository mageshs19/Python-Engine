# `converter/ui/status_panel.py`

Source: [converter/ui/status_panel.py](../../../../converter/ui/status_panel.py) | 68 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `1e8736a15580bd48be7b1b17bc24dd48ea9fa77be7a483b25a607914e50e1127`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import streamlit as st
from rules.lrf_rules import LRF_METRIC_LABEL
```

## Local dependency notes

- [rules/lrf_rules.py](../../rules/lrf_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_tab.py](main_tab.md)

## Symbol contracts and control points

### `render_current_status` - L11-L37

```python
render_current_status() -> None
```

Observed calls (lexical order): `st.markdown`, `st.columns`, `len`, `st.metric`, `st.session_state.get`, `st.success`.

Control points:

- L33: `if st.session_state.loaded`
- L36: `if st.session_state.generated`

### `render_main_download_section` - L40-L68

```python
render_main_download_section() -> None
```

Observed calls (lexical order): `st.markdown`, `st.info`, `st.success`, `st.caption`, `st.download_button`, `st.expander`, `st.text_area`.

Control points:

- L43: `if not st.session_state.generated or not st.session_state.converted_cobol`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
