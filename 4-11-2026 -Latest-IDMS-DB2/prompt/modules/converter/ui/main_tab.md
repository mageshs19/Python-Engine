# `converter/ui/main_tab.py`

Source: [converter/ui/main_tab.py](../../../../converter/ui/main_tab.py) | 121 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `229487be607beecb58e122b9540652dd491807d2a61104f766644ee9adc49791`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import streamlit as st
from converter.ui.conversion_actions import generate_db2_cobol
from converter.ui.input_loader import load_and_analyze_inputs
from converter.ui.status_panel import render_current_status, render_main_download_section
from rules.lrf_rules import LRF_UPLOAD_HELP, LRF_UPLOAD_LABEL
```

## Local dependency notes

- [converter/ui/conversion_actions.py](conversion_actions.md)
- [converter/ui/input_loader.py](input_loader.md)
- [converter/ui/status_panel.py](status_panel.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_page.py](main_page.md)

## Symbol contracts and control points

### `render_main_tab` - L17-L47

```python
render_main_tab() -> None
```

Observed calls (lexical order): `st.markdown`, `st.info`, `_render_uploaders`, `st.caption`, `_render_action_buttons`, `render_current_status`, `render_main_download_section`.

### `_render_uploaders` - L50-L96

```python
_render_uploaders()
```

Observed calls (lexical order): `st.columns`, `st.file_uploader`.

### `_render_action_buttons` - L99-L121

```python
_render_action_buttons(*, sheet_mapping_file, dclgen_files, copybook_files, lrf_files, idms_cobol_source_file) -> None
```

Observed calls (lexical order): `st.columns`, `st.button`, `load_and_analyze_inputs`, `generate_db2_cobol`.

Control points:

- L110: `if st.button('Load and Analyze Inputs', type='primary')`
- L120: `if st.button('Generate DB2 COBOL')`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
