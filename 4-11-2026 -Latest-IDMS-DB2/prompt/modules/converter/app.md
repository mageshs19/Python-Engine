# `converter/app.py`

Source: [converter/app.py](../../../converter/app.py) | 35 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../15_UI_AND_LOGGING.md).
Source SHA-256: `8756d9eebc3e79103f9423cf6978ead171e68fda7c2cdda301bdc7e149a7d5f6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`CURRENT_FILE` (L7), `SRC_DIR` (L8), `PROJECT_ROOT` (L9)

## Import declarations

```python
from pathlib import Path
import sys
import streamlit as st
from converter.ui.main_page import render_main_page
```

## Local dependency notes

- [converter/ui/main_page.py](ui/main_page.md)

## Symbol contracts and control points

### `main` - L18-L31

```python
main() -> None
```

Observed calls (lexical order): `st.set_page_config`, `st.title`, `st.caption`, `render_main_page`.

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
