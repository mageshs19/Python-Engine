# `review/checks/chk_13_cursor_paragraph_structure.py`

Source: [review/checks/chk_13_cursor_paragraph_structure.py](../../../../review/checks/chk_13_cursor_paragraph_structure.py) | 143 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `55ada75f4cd01a626e4fb925bcdd1a2057168f7a7acb8192d378654eab1c6735`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-13 Cursor paragraph structure.

## Import declarations

```python
from __future__ import annotations
from review.engine import cursors
from review.engine.check_base import MAJOR, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cursors.py](../engine/cursors.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `CursorParagraphStructureCheck` - L10-L143

```python
class CursorParagraphStructureCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-13'
TITLE = 'Cursor paragraph structure'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 130
```

### `CursorParagraphStructureCheck.relevant` - L17-L18

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`, `cursors.cursor_paragraphs`.

### `CursorParagraphStructureCheck.not_relevant_reason` - L20-L21

```python
not_relevant_reason(self) -> str
```

### `CursorParagraphStructureCheck.review` - L23-L143

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.paragraph_sets`, `cursors.cursor_paragraphs`, `cursors.declared_cursors`, `cursors.performed_names`, `record.skip`, `', '.join`, `sorted`, `sets.get`, `missing.append`, `record.expect_all`, `sets.items`, `group.get`, `expected.items`, `wrong.append`, `set`, `sets.values`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L30: `if not declared`
- L38: `for name in sorted(declared)`
- L40: `for operation in std.CURSOR_OPERATIONS`
- L41: `if operation not in have`
- L51: `for (name, group) in sorted(sets.items())`
- L53: `if open_para is None`
- L65: `for (operation, number) in expected.items()`
- L67: `if para is not None and para.number != number`
- Another 3 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
