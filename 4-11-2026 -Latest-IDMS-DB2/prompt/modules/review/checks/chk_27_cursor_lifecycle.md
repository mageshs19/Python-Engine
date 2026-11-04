# `review/checks/chk_27_cursor_lifecycle.py`

Source: [review/checks/chk_27_cursor_lifecycle.py](../../../../review/checks/chk_27_cursor_lifecycle.py) | 99 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `a04ee6c08d0ef74b1caf51f36ee3b5473d2d17ec5b46f859c5ca724486a5619a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-27 Cursor lifecycle - DECLARE, OPEN, FETCH, CLOSE, termination.

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import cursors, sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cursors.py](../engine/cursors.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `CursorLifecycleCheck` - L12-L99

```python
class CursorLifecycleCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-27'
TITLE = 'Cursor lifecycle validation'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 270
```

### `CursorLifecycleCheck.relevant` - L19-L20

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`, `cursors.declare_blocks`.

### `CursorLifecycleCheck.not_relevant_reason` - L22-L23

```python
not_relevant_reason(self) -> str
```

### `CursorLifecycleCheck.review` - L25-L99

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.declare_blocks`, `cursors.declared_cursors`, `cursors.open_statements`, `cursors.close_statements`, `sql.fetch_statements`, `all`, `d.has`, `record.expect_none`, `cursors.cursor_name`, `f.has`, `cursors.cursor_paragraphs`, `'\n'.join`, `'\n'.join(cursors.paragraph_body(view, para)).upper`, `cursors.paragraph_body`, `bool`, `re.search`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L72: `for para in cursors.cursor_paragraphs(view)`
- L78: `if not has_location`
- L80: `if para.operation == 'FETCH'`
- L81: `if not re.search('\\bWHEN\\s+(?:\\+?100|SQLCODE\\s*=\\s*\\+?100)\\b', body)`
- L83: `if not re.search('\\bWHEN\\s+OTHER\\b', body) or not re.search('\\b(?:PERFORM|GO\\s+TO)\\s+SQLERROR\\b|\\bSQLERROR\\b', body)`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
