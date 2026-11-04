# `review/report/csv_writer.py`

Source: [review/report/csv_writer.py](../../../../review/report/csv_writer.py) | 87 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `2cb97c436a453c6844f4a4e53012d29275427085b1c837c2a73b3acc08a4a19a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Writes a ReviewResult as CSV.

## Module-level bindings

`TEXT_ENCODING` (L18), `FILE_SUFFIX` (L19)

## Import declarations

```python
from __future__ import annotations
import csv
from pathlib import Path
from review.engine.models import ReviewResult
from review.engine.reviewer import is_accepted
from review.standards import wording as w
```

## Local dependency notes

- [review/engine/models.py](../engine/models.md)
- [review/engine/reviewer.py](../engine/reviewer.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/wording.py](../standards/wording.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/report/__init__.py](__init__.md)
- [review/runner/review_file.py](../runner/review_file.md)
- [review/ui/review_panel.py](../ui/review_panel.md)

## Symbol contracts and control points

### `rows` - L22-L45

```python
rows(result: ReviewResult) -> list[list[str]]
```

One row per criterion.

Observed calls (lexical order): `result.reviewed_at.strftime`, `out.append`, `w.CSV_LINE_SEPARATOR.join`, `str`.

Control points:

- L26: `for check in result.checks`
- L27: `for crit in check.criteria`

### `summary_rows` - L48-L63

```python
summary_rows(results: list[ReviewResult]) -> list[list[str]]
```

One row per reviewed program.

Observed calls (lexical order): `out.append`, `result.reviewed_at.strftime`, `is_accepted`.

Control points:

- L51: `for result in results`

### `write` - L66-L73

```python
write(result: ReviewResult, folder: Path, stem: str) -> Path
```

Observed calls (lexical order): `folder.mkdir`, `Path`, `path.open`, `csv.writer`, `writer.writerow`, `rows`, `writer.writerows`.

### `write_summary` - L76-L87

```python
write_summary(results: list[ReviewResult], folder: Path, stem: str) -> Path
```

Observed calls (lexical order): `folder.mkdir`, `Path`, `path.open`, `csv.writer`, `writer.writerow`, `summary_rows`, `writer.writerows`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
