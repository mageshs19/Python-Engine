# `converter/ui/session_state.py`

Source: [converter/ui/session_state.py](../../../../converter/ui/session_state.py) | 44 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `f4a6884a237d73db4ea414eeda7da73be9eed5c61db37ba0dae95d2ff8a2edf5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import streamlit as st
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/input_loader.py](input_loader.md)
- [converter/ui/main_page.py](main_page.md)

## Symbol contracts and control points

### `initialize_session_state` - L9-L36

```python
initialize_session_state() -> None
```

Observed calls (lexical order): `defaults.items`, `isinstance`.

Control points:

- L28: `for (key, value) in defaults.items()`
- L29: `if key in st.session_state`
- L31: `if isinstance(value, list)`
- L33: `if isinstance(value, dict)`

### `reset_generated_output_state` - L39-L44

```python
reset_generated_output_state() -> None
```

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
