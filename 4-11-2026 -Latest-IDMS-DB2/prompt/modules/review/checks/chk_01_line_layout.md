# `review/checks/chk_01_line_layout.py`

Source: [review/checks/chk_01_line_layout.py](../../../../review/checks/chk_01_line_layout.py) | 63 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `88af4c05d9f3f7896528cbe54342cbdb8d4b0212c4d65cdb9c73a15607b11811`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-01 Fixed format 80-column layout.

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

### `LineLayoutCheck` - L9-L63

```python
class LineLayoutCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-01'
TITLE = 'Fixed format 80-column layout'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 10
```

### `LineLayoutCheck.review` - L16-L63

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `record.expect_none`, `len`, `l.raw[0:6].isdigit`, `l.overflow.strip`, `l.raw[72:80].isdigit`, `view.sequence`, `record.expect`, `view.constant_step`, `bool`, `record.skip`.

Control points:

- L56: `if std.ENFORCE_SEQUENCE_START`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
