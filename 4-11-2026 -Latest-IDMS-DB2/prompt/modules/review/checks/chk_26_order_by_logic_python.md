# `review/checks/chk_26_order_by_logic_python.py`

Source: [review/checks/chk_26_order_by_logic_python.py](../../../../review/checks/chk_26_order_by_logic_python.py) | 74 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `343e72997bd1c30d757d41c03f97ee72399809200ee156289362b529df3d90c7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-26 ORDER BY logic - CursorOrderByResolver validation.

## Import declarations

```python
from __future__ import annotations
from review.engine import cursors
from review.engine.check_base import MINOR, BOTH, Check
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cursors.py](../engine/cursors.md)

## Symbol contracts and control points

### `OrderByLogicPythonCheck` - L21-L74

```python
class OrderByLogicPythonCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-26'
TITLE = 'ORDER BY logic - CursorOrderByResolver validation'
SEVERITY = MINOR
APPLIES_TO = BOTH
ORDER = 260
```

### `OrderByLogicPythonCheck.relevant` - L28-L29

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`, `cursors.declare_blocks`.

### `OrderByLogicPythonCheck.not_relevant_reason` - L31-L32

```python
not_relevant_reason(self) -> str
```

### `OrderByLogicPythonCheck.review` - L34-L74

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.declare_blocks`, `d.has`, `record.pass_all`, `len`, `record.expect_none`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
