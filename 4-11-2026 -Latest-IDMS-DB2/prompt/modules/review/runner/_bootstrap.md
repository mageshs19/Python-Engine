# `review/runner/_bootstrap.py`

Source: [review/runner/_bootstrap.py](../../../../review/runner/_bootstrap.py) | 42 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `4432a2eb99185defee3340c1cabd03bb7204b1b754559a4acfd211e4e5095a70`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared constants and small file helpers for the code review runners.

## Module-level bindings

`PROJECT_ROOT` (L20), `SRC_DIR` (L21), `REPORT_DIR` (L22), `TIMESTAMP_FORMAT` (L25), `COBOL_GLOB` (L26), `TEXT_ENCODING` (L27), `EXIT_ACCEPTED` (L30), `EXIT_REJECTED` (L31), `EXIT_ERROR` (L32)

## Import declarations

```python
from __future__ import annotations
from datetime import datetime
from pathlib import Path
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/runner/review_file.py](review_file.md)

## Symbol contracts and control points

### `stamp` - L35-L37

```python
stamp() -> str
```

Timestamp used in report file names.

Observed calls (lexical order): `datetime.now`, `datetime.now().strftime`.

### `read_text` - L40-L42

```python
read_text(path: Path) -> str
```

Read a COBOL or text file without ever raising on bad bytes.

Observed calls (lexical order): `Path`, `Path(path).read_text`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
