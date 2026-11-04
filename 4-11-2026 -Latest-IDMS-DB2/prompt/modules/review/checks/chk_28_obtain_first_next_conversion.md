# `review/checks/chk_28_obtain_first_next_conversion.py`

Source: [review/checks/chk_28_obtain_first_next_conversion.py](../../../../review/checks/chk_28_obtain_first_next_conversion.py) | 75 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `a0c102beea0a47dc2fe843a7854358f22f12b82a2abcc530aaab19d914768dd4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-28 OBTAIN FIRST/NEXT conversion - classic IDMS to DB2 cursor.

## Import declarations

```python
from __future__ import annotations
from review.engine import metadata as meta
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `ObtainFirstNextConversionCheck` - L21-L75

```python
class ObtainFirstNextConversionCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-28'
TITLE = 'OBTAIN FIRST/NEXT conversion - classic IDMS to DB2 cursor'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 280
```

### `ObtainFirstNextConversionCheck.relevant` - L28-L30

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `view.has_code_token`, `view.has_comment`.

### `ObtainFirstNextConversionCheck.not_relevant_reason` - L32-L33

```python
not_relevant_reason(self) -> str
```

### `ObtainFirstNextConversionCheck.review` - L35-L75

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `record.ok`, `l.logical.strip`, `l.logical.strip().startswith`, `record.expect_none`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
