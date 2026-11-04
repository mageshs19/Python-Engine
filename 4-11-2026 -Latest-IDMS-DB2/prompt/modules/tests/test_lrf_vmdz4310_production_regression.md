# `tests/test_lrf_vmdz4310_production_regression.py`

Source: [tests/test_lrf_vmdz4310_production_regression.py](../../../tests/test_lrf_vmdz4310_production_regression.py) | 148 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `1389f25e8fc2916d5e5c8d181a5efa94ae6d39d119bf359d39aeddbb330999b3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`PROJECT_ROOT` (L11), `PROGRAM_PATH` (L12)

## Import declarations

```python
from __future__ import annotations
import logging
import re
from pathlib import Path
from runners.retrieval.retrieval_input_loader import load_shared_inputs
from runners.retrieval.retrieval_program_converter import convert_one_program
```

## Local dependency notes

- [runners/retrieval/retrieval_input_loader.py](../runners/retrieval/retrieval_input_loader.md)
- [runners/retrieval/retrieval_program_converter.py](../runners/retrieval/retrieval_program_converter.md)

## Symbol contracts and control points

### `test_vmdz4310_lrf_parent_child_access_is_structurally_safe` - L15-L148

```python
test_vmdz4310_lrf_parent_child_access_is_structurally_safe(tmp_path, capsys)
```

Observed calls (lexical order): `logging.getLogger`, `logger.addHandler`, `logging.NullHandler`, `logger.setLevel`, `load_shared_inputs`, `convert_one_program`, `output_path.read_text`, `capsys.readouterr`, `' '.join`, `len`, `line.strip`, `line[7:72].strip`, `line[:6].isdigit`, `generated.splitlines`, `generated.index`, `generated.rfind`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L117: `for line in generated.splitlines()`
- L118: `if len(line) > 6 and line[6] not in ('*', '/')`
- L126: `for line in generated.splitlines()`
- L127: `if len(line) >= 7 and line[:6].isdigit()`
- L129: `if line[6] == '*'`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
