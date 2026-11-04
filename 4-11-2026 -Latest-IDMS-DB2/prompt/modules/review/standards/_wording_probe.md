# `review/standards/_wording_probe.py`

Source: [review/standards/_wording_probe.py](../../../../review/standards/_wording_probe.py) | 90 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `8cd3265b3197f67fb18a9782e89be153556c5f4dfce1c737f09a8e20e6f4e085`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Developer probe: verify every `from rules.X import (...)` name exists.

## Module-level bindings

`PROJECT_ROOT` (L20), `SRC_DIR` (L21), `SCAN_DIRS` (L27), `WATCHED_PACKAGES` (L28)

## Import declarations

```python
from __future__ import annotations
import ast
import importlib
import sys
from pathlib import Path
```

## Symbol contracts and control points

### `missing_names` - L31-L73

```python
missing_names() -> list[str]
```

Observed calls (lexical order): `base.exists`, `base.rglob`, `sorted`, `ast.parse`, `path.read_text`, `problems.append`, `ast.walk`, `isinstance`, `module.startswith`, `importlib.import_module`, `cache.get`, `hasattr`.

Control points:

- L35: `for folder in SCAN_DIRS`
- L37: `if not base.exists()`
- L40: `for path in sorted(base.rglob('*.py'))`
- L47: `for node in ast.walk(tree)`
- L48: `if not isinstance(node, ast.ImportFrom)`
- L51: `if not module.startswith(WATCHED_PACKAGES)`
- L54: `if module not in cache`
- L62: `if target is None`
- Another 3 conditions/loops exist in this source span.

### `main` - L76-L86

```python
main() -> None
```

Observed calls (lexical order): `missing_names`, `print`, `SystemExit`, `len`.

Control points:

- L79: `if not problems`
- L83: `for problem in problems`

Explicit raises: `SystemExit(0)`; `SystemExit(1)`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
