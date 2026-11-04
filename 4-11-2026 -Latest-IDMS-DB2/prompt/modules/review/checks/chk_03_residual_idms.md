# `review/checks/chk_03_residual_idms.py`

Source: [review/checks/chk_03_residual_idms.py](../../../../review/checks/chk_03_residual_idms.py) | 36 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `664e03f1098fb9f00fe93d7bff85aad0e13df12f1b235f0bb4d0c201068f46d6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-03 No residual IDMS statements.

## Import declarations

```python
from __future__ import annotations
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `ResidualIdmsCheck` - L9-L36

```python
class ResidualIdmsCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-03'
TITLE = 'No residual IDMS statements'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 30
```

### `ResidualIdmsCheck.review` - L16-L36

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `record.expect_none`, `l.logical.startswith`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
