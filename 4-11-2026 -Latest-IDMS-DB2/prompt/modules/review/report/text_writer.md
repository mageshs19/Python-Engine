# `review/report/text_writer.py`

Source: [review/report/text_writer.py](../../../../review/report/text_writer.py) | 109 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `5f9c60c0b89222b193ff873328847c61f22061bcab77eb1c6fd6929c1ba55aff`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders a ReviewResult as the human-readable Code Review Report.

## Module-level bindings

`TEXT_ENCODING` (L15), `FILE_SUFFIX` (L16)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from review.engine.models import Outcome, ReviewResult
from review.engine.reviewer import blockers, is_accepted
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

### `render` - L19-L102

```python
render(result: ReviewResult) -> str
```

Observed calls (lexical order): `add`, `w.F_PROGRAM.format`, `w.F_KIND.format`, `w.F_SOURCE.format`, `w.F_WHEN.format`, `result.reviewed_at.strftime`, `w.F_TOTALS.format`, `w.F_CRITERIA.format`, `w.F_RESULT.format`, `is_accepted`, `blockers`, `w.F_BLOCKING.format`, `', '.join`, `w.F_CHECK.format`, `w.F_CRIT.format`, `w.F_NOTE.format`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L49: `if blocking`
- L59: `for check in result.checks`
- L66: `for crit in check.criteria`
- L67: `if crit.outcome is Outcome.PASS`
- L73: `if crit.note`
- L75: `for finding in crit.findings`
- L84: `if not failed`
- L87: `for check in failed`
- Another 2 conditions/loops exist in this source span.

### `write` - L105-L109

```python
write(result: ReviewResult, folder: Path, stem: str) -> Path
```

Observed calls (lexical order): `folder.mkdir`, `Path`, `path.write_text`, `render`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
