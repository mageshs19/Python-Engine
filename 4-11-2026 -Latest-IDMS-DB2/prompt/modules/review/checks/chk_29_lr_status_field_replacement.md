# `review/checks/chk_29_lr_status_field_replacement.py`

Source: [review/checks/chk_29_lr_status_field_replacement.py](../../../../review/checks/chk_29_lr_status_field_replacement.py) | 125 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `a645eeb5f773b8b5b960111e0a6353bf8d7c9d03c388942ce30878088f02fcc2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-29 LR-STATUS field - replaced with cursor end-of-cursor logic.

## Import declarations

```python
from __future__ import annotations
import re
from review.engine.cobol_view import CobolView
from review.engine import metadata as meta
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cobol_view.py](../engine/cobol_view.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)

## Symbol contracts and control points

### `LRStatusFieldReplacementCheck` - L24-L125

```python
class LRStatusFieldReplacementCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-29'
TITLE = 'LR-STATUS field - replaced with cursor end-of-cursor logic'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 290
```

### `LRStatusFieldReplacementCheck.relevant` - L31-L49

```python
relevant(self, ctx, view) -> bool
```

True when this program WAS a logical-record program.

Observed calls (lexical order): `l.logical.upper`, `any`.

### `LRStatusFieldReplacementCheck.not_relevant_reason` - L51-L52

```python
not_relevant_reason(self) -> str
```

### `LRStatusFieldReplacementCheck.review` - L54-L121

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `record.expect_none`, `l.logical.upper`, `any`, `getattr`, `self._requires_end_of_set`, `record.skip`, `record.expect`.

Control points:

- L96: `if source and (not self._requires_end_of_set(source))`

### `LRStatusFieldReplacementCheck._requires_end_of_set` - L123-L125

```python
_requires_end_of_set(source)
```

Observed calls (lexical order): `CobolView`, `bool`, `re.search`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
