# `tests/test_lrf_vmdz4310_latest_artifact.py`

Source: [tests/test_lrf_vmdz4310_latest_artifact.py](../../../tests/test_lrf_vmdz4310_latest_artifact.py) | 40 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `7c0f0d18a36ad17c36b91832d65d2e862bb3c32879e1176cd21d35f9dca2788b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L4), `LATEST` (L6)

## Import declarations

```python
from pathlib import Path
import re
from tests.workspace_fixtures import generated_program
```

## Local dependency notes

- [tests/workspace_fixtures.py](workspace_fixtures.md)

## Symbol contracts and control points

### `test_latest_vmdz4310_artifact_is_singleton_not_cursor_based` - L9-L40

```python
test_latest_vmdz4310_artifact_is_singleton_not_cursor_based()
```

Observed calls (lexical order): `LATEST.read_text`, `text.upper`, `text.splitlines`, `len`, `line[:6].isdigit`, `line[7:72].rstrip`, `upper.index`, `upper.rfind`, `block.split`, `re.findall`, `column.replace`.

Control points:

- L27: `for line in text.splitlines()`
- L28: `if len(line) >= 7 and line[:6].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
