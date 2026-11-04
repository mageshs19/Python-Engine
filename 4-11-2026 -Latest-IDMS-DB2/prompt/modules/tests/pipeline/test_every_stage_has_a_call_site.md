# `tests/pipeline/test_every_stage_has_a_call_site.py`

Source: [tests/pipeline/test_every_stage_has_a_call_site.py](../../../../tests/pipeline/test_every_stage_has_a_call_site.py) | 51 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `78286effecb12af3cc3527cb26302d5490429101e5d2ae1025def83e929c57fc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> A registered stage with no caller is dead code that reads as live.

## Module-level bindings

`PROJECT_ROOT` (L25), `SOURCE_DIR` (L26), `ENCODING` (L27), `SOURCE` (L39)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
import pytest
from converter.pipeline.registry import PIPELINE
```

## Local dependency notes

- [converter/pipeline/registry.py](../../converter/pipeline/registry.md)

## Symbol contracts and control points

### `_all_source` - L30-L36

```python
_all_source() -> str
```

Observed calls (lexical order): `SOURCE_DIR.rglob`, `sorted`, `parts.append`, `path.read_text`, `'\n'.join`.

Control points:

- L32: `for path in sorted(SOURCE_DIR.rglob('*.py'))`
- L33: `if path.name == 'registry.py'`

### `test_every_stage_is_actually_invoked` - L43-L51

```python
test_every_stage_is_actually_invoked(stage)
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
