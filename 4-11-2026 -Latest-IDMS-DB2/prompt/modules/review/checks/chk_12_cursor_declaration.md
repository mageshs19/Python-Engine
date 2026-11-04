# `review/checks/chk_12_cursor_declaration.py`

Source: [review/checks/chk_12_cursor_declaration.py](../../../../review/checks/chk_12_cursor_declaration.py) | 136 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `078ddb3f4be7ded168076e0ac2bb587a0dabf62d225e72d057480cb960b291a4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-12 Cursor declaration standard.

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import cursors
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cursors.py](../engine/cursors.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `CursorDeclarationCheck` - L12-L136

```python
class CursorDeclarationCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-12'
TITLE = 'Cursor declaration standard'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 120
```

### `CursorDeclarationCheck.relevant` - L19-L20

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`, `cursors.declare_blocks`.

### `CursorDeclarationCheck.not_relevant_reason` - L22-L23

```python
not_relevant_reason(self) -> str
```

### `CursorDeclarationCheck.review` - L25-L128

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.declare_blocks`, `cursors.declared_cursors`, `bool`, `re.search`, `record.skip`, `record.expect_none`, `b.has`, `all`, `cursors.DECLARE.search`, `cursors.DECLARE.search(b.text).group`, `cursors.DECLARE.search(b.text).group('cursor').upper`, `names.count`, `sorted`, `record.expect_all`, `self._procedure_division_line`, `cursors.cursors_used`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L39: `if not std.ENFORCE_CURSOR_WITH_HOLD or not has_transaction_boundary`
- L51: `if not std.ENFORCE_CURSOR_FOR_READ_ONLY`
- L72: `if not std.ENFORCE_CURSOR_EXPLICIT_COLUMNS`
- L96: `if pd_line <= 0`
- L109: `if not opened`
- L121: `if std.ENFORCE_CURSOR_MARKERS`

### `CursorDeclarationCheck._procedure_division_line` - L132-L136

```python
_procedure_division_line(view) -> int
```

Observed calls (lexical order): `line.logical.startswith`.

Control points:

- L133: `for line in view.code`
- L134: `if line.logical.startswith('PROCEDURE DIVISION')`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
