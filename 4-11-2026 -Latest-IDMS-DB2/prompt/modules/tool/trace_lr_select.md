# `tool/trace_lr_select.py`

Source: [tool/trace_lr_select.py](../../../tool/trace_lr_select.py) | 78 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../15_UI_AND_LOGGING.md).
Source SHA-256: `39e8d522aeffe6c0d662660ffda69e5d262bf28b83862d696c98de6fd720bab1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reports the FIRST pipeline boundary at which the generated LR keyed SELECT disappears - or proves it was never produced.

## Module-level bindings

`TOKEN` (L18), `TARGETS` (L20)

## Import declarations

```python
from __future__ import annotations
import importlib
import inspect
import runpy
```

## Symbol contracts and control points

### `_carries` - L40-L45

```python
_carries(value) -> bool
```

Observed calls (lexical order): `isinstance`, `value.upper`, `_carries`, `any`.

Control points:

- L41: `if isinstance(value, str)`
- L43: `if isinstance(value, (list, tuple))`

### `_wrap` - L48-L68

```python
_wrap(module_name: str, class_name: str, method_name: str) -> str
```

Observed calls (lexical order): `importlib.import_module`, `getattr`, `isinstance`, `inspect.getattr_static`, `setattr`, `staticmethod`.

### `_wrap.traced` - L57-L65

```python
traced(*args, **kwargs)
```

Observed calls (lexical order): `_carries`, `kwargs.values`, `list`, `original`, `print`.

Control points:

- L61: `if before and (not after)`
- L63: `if before or after`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
