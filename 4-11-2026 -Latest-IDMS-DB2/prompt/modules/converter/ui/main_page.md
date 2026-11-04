# `converter/ui/main_page.py`

Source: [converter/ui/main_page.py](../../../../converter/ui/main_page.py) | 62 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `f69e759c1ccda2480baf3660a85e91c6211a8bee1b668971d4b1169368b39dbe`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`TAB_MAIN` (L20), `TAB_SHEET_MAPPING` (L21), `TAB_GENERATED` (L22), `TAB_VALIDATION` (L23), `TAB_CODE_REVIEW` (L24), `TAB_DIAGNOSTICS` (L25)

## Import declarations

```python
from __future__ import annotations
import streamlit as st
from review.ui.review_panel import render_review_panel
from converter.ui.main_tab import render_main_tab
from converter.ui.output_tabs import render_diagnostics_tab, render_generated_cobol_tab, render_sheet_mapping_rows_tab, render_validation_tab
from converter.ui.session_state import initialize_session_state
from converter.ui.test_panel import render_test_panel
from rules.test_runner_rules import UI_TAB_TITLE as TESTS_TAB_TITLE
```

## Local dependency notes

- [converter/ui/main_tab.py](main_tab.md)
- [converter/ui/output_tabs.py](output_tabs.md)
- [converter/ui/session_state.py](session_state.md)
- [converter/ui/test_panel.py](test_panel.md)
- [review/ui/review_panel.py](../../review/ui/review_panel.md)
- [rules/test_runner_rules.py](../../rules/test_runner_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/app.py](../app.md)

## Symbol contracts and control points

### `render_main_page` - L28-L62

```python
render_main_page() -> None
```

Observed calls (lexical order): `initialize_session_state`, `st.tabs`, `render_main_tab`, `render_sheet_mapping_rows_tab`, `render_generated_cobol_tab`, `render_validation_tab`, `render_review_panel`, `render_diagnostics_tab`, `render_test_panel`.

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
