# `tests/test_lrf_vmdz4310_multiline_access_diagnostic.py`

Source: [tests/test_lrf_vmdz4310_multiline_access_diagnostic.py](../../../tests/test_lrf_vmdz4310_multiline_access_diagnostic.py) | 76 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `da378e2ecdd8ad69727ac576ecfb30b9bcd3c01e5be77021a4ff4fcb59ffa022`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L8), `SOURCE` (L9)

## Import declarations

```python
from __future__ import annotations
import logging
from pathlib import Path
from runners.retrieval.retrieval_input_loader import load_shared_inputs
from runners.retrieval.retrieval_program_converter import convert_one_program
```

## Local dependency notes

- [runners/retrieval/retrieval_input_loader.py](../runners/retrieval/retrieval_input_loader.md)
- [runners/retrieval/retrieval_program_converter.py](../runners/retrieval/retrieval_program_converter.md)

## Symbol contracts and control points

### `_body` - L12-L15

```python
_body(line: str) -> str
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].strip`, `line.strip`.

Control points:

- L13: `if len(line) >= 7 and line[:6].isdigit()`

### `_convert` - L18-L34

```python
_convert(tmp_path: Path) -> tuple[str, str]
```

Observed calls (lexical order): `logging.getLogger`, `logger.addHandler`, `logging.NullHandler`, `logger.setLevel`, `load_shared_inputs`, `convert_one_program`, `'\n'.join`, `output_path.read_text`.

### `test_lrf_first_marker_is_recovered_even_when_comment_wraps` - L37-L50

```python
test_lrf_first_marker_is_recovered_even_when_comment_wraps(tmp_path: Path) -> None
```

Observed calls (lexical order): `_convert`.

### `test_vmdz4310_until_condition_is_split_across_physical_lines_but_preserved` - L53-L76

```python
test_vmdz4310_until_condition_is_split_across_physical_lines_but_preserved(tmp_path: Path) -> None
```

Observed calls (lexical order): `SOURCE.read_text`, `SOURCE.read_text(encoding='utf-8', errors='replace').splitlines`, `enumerate`, `next`, `_body`, `_convert`, `all`, `generated.splitlines`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
