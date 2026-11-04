# `review/checks/chk_21_where_clause_child_cursor.py`

Source: [review/checks/chk_21_where_clause_child_cursor.py](../../../../review/checks/chk_21_where_clause_child_cursor.py) | 77 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `52b7bb5d985b7949f85b1de667d5e49f011e81dc071a55546480012465206ceb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-21 WHERE clause - child cursor join predicates.

## Import declarations

```python
from __future__ import annotations
from review.engine import cursors, sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cursors.py](../engine/cursors.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)

## Symbol contracts and control points

### `ChildCursorWhereCheck` - L21-L77

```python
class ChildCursorWhereCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-21'
TITLE = 'WHERE clause - child cursor join predicates'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 210
```

### `ChildCursorWhereCheck.relevant` - L28-L30

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `cursors.declare_blocks`, `any`, `d.has`.

### `ChildCursorWhereCheck.not_relevant_reason` - L32-L33

```python
not_relevant_reason(self) -> str
```

### `ChildCursorWhereCheck.review` - L35-L77

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.declare_blocks`, `d.has`, `record.ok`, `record.expect_none`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
