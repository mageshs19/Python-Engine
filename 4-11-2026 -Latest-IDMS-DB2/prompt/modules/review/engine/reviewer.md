# `review/engine/reviewer.py`

Source: [review/engine/reviewer.py](../../../../review/engine/reviewer.py) | 75 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `a9b6a98e7492de8a429b9c31bb1946149887e09f4b8bb39a42a95bce80ae02b7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Runs the check pipeline against one ReviewContext.

## Import declarations

```python
from __future__ import annotations
from review.engine.check_base import Check, Recorder
from review.engine.cobol_view import CobolView
from review.engine.context import ReviewContext
from review.engine.models import CheckResult, Criterion, Outcome, ReviewResult
from review.engine.registry import load_checks
from review.standards.pipeline import BLOCKING_SEVERITIES, EVIDENCE_LIMIT
```

## Local dependency notes

- [review/engine/check_base.py](check_base.md)
- [review/engine/cobol_view.py](cobol_view.md)
- [review/engine/context.py](context.md)
- [review/engine/models.py](models.md)
- [review/engine/registry.py](registry.md)
- [review/standards/pipeline.py](../standards/pipeline.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/engine/__init__.py](__init__.md)
- [review/report/csv_writer.py](../report/csv_writer.md)
- [review/report/text_writer.py](../report/text_writer.md)
- [review/runner/review_file.py](../runner/review_file.md)
- [review/ui/review_panel.py](../ui/review_panel.md)
- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)

## Symbol contracts and control points

### `Reviewer` - L17-L62

```python
class Reviewer()
```

### `Reviewer.__init__` - L18-L19

```python
__init__(self, checks: list[Check] | None=None) -> None
```

Observed calls (lexical order): `load_checks`.

### `Reviewer.review` - L21-L30

```python
review(self, ctx: ReviewContext) -> ReviewResult
```

Observed calls (lexical order): `CobolView`, `ReviewResult`, `result.checks.append`, `self._one`.

Control points:

- L28: `for check in self.checks`

### `Reviewer._one` - L32-L62

```python
_one(self, check: Check, ctx: ReviewContext, view: CobolView) -> CheckResult
```

Observed calls (lexical order): `CheckResult`, `check.applies`, `single`, `ctx.missing`, `', '.join`, `check.relevant`, `check.not_relevant_reason`, `Recorder`, `check.review`, `out.criteria.extend`.

Control points:

- L41: `if not check.applies(ctx)`
- L45: `if missing`
- L48: `if view.is_empty`
- L52: `if not check.relevant(ctx, view)`
- L60: `if not out.criteria`

### `Reviewer._one.single` - L35-L39

```python
single(outcome: Outcome, note: str) -> CheckResult
```

Observed calls (lexical order): `out.criteria.append`, `Criterion`.

### `is_accepted` - L65-L67

```python
is_accepted(result: ReviewResult) -> bool
```

Observed calls (lexical order): `blockers`.

### `blockers` - L70-L75

```python
blockers(result: ReviewResult) -> list[CheckResult]
```

Observed calls (lexical order): `s.upper`, `sorted`, `check.severity.upper`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
