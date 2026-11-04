# `tool/trace_obtain_calc.py`

Source: [tool/trace_obtain_calc.py](../../../tool/trace_obtain_calc.py) | 85 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../15_UI_AND_LOGGING.md).
Source SHA-256: `4e3cd22f63aa1061b8640ab78b874b14aacf1bf8cb4fd652a0b05a3ee4f1521f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reports the FIRST pipeline boundary at which a token disappears.

## Module-level bindings

`TOKEN` (L20), `TARGETS` (L22)

## Import declarations

```python
from __future__ import annotations
import importlib
import inspect
import os
import runpy
```

## Symbol contracts and control points

### `_carries` - L45-L50

```python
_carries(value) -> bool
```

Observed calls (lexical order): `isinstance`, `value.upper`, `_carries`, `any`.

Control points:

- L46: `if isinstance(value, str)`
- L48: `if isinstance(value, (list, tuple))`

### `_wrap` - L53-L73

```python
_wrap(module_name: str, class_name: str, method_name: str) -> str
```

Observed calls (lexical order): `importlib.import_module`, `getattr`, `isinstance`, `inspect.getattr_static`, `setattr`, `staticmethod`.

### `_wrap.traced` - L62-L70

```python
traced(*args, **kwargs)
```

Observed calls (lexical order): `_carries`, `kwargs.values`, `list`, `original`, `print`.

Control points:

- L66: `if before and (not after)`
- L68: `if before`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
