# `review/checks/chk_14_end_of_cursor_handling.py`

Source: [review/checks/chk_14_end_of_cursor_handling.py](../../../../review/checks/chk_14_end_of_cursor_handling.py) | 234 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `3bcebb71d9dc78d0e980744f5a0ae365fd7c4bacf050c6f39de6b5448bf3d3a9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-14 End-of-cursor handling in the fetch paragraph.

## Import declarations

```python
from __future__ import annotations
from review.engine import cursors, sql_blocks as sql
from review.engine.check_base import MAJOR, BOTH, Check
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

### `EndOfCursorHandlingCheck` - L78-L234

```python
class EndOfCursorHandlingCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-14'
TITLE = 'End-of-cursor handling'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 140
```

### `EndOfCursorHandlingCheck.relevant` - L85-L86

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`, `cursors.cursor_paragraphs`.

### `EndOfCursorHandlingCheck.not_relevant_reason` - L88-L89

```python
not_relevant_reason(self) -> str
```

### `EndOfCursorHandlingCheck.review` - L91-L225

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.paragraph_sets`, `sets.values`, `record.skip`, `record.expect_none`, `self._body_has`, `any`, `sql.norm`, `missing.append`, `record.expect_all`, `record.expect`, `view.has_token`.

Control points:

- L101: `if not fetches`
- L120: `if not fetches`
- L139: `if not opens`
- L163: `if not std.ENFORCE_EOC_FLAG_LOOP`
- L188: `if not fetches`
- L199: `for para in fetches`
- L203: `if not any((terminator in line for line in code))`
- L218: `if std.ENFORCE_CURSOR_MARKERS`

### `EndOfCursorHandlingCheck._body_has` - L229-L234

```python
_body_has(view, para, token: str) -> bool
```

Observed calls (lexical order): `sql.norm`, `cursors.paragraph_body`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
