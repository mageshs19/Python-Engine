# `review/checks/chk_33_doubly_driven_paragraph.py`

Source: [review/checks/chk_33_doubly_driven_paragraph.py](../../../../review/checks/chk_33_doubly_driven_paragraph.py) | 159 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `cbbf153d89ea70fd9dc66155409d55ab2e7f979b19af7d073f9cc58755e6726b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-33 A business paragraph must have ONE driving edge.

## Module-level bindings

`PERFORM_TARGET` (L40), `PERFORM_UNTIL` (L45), `__all__` (L159)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import cursors
from review.engine import sql_blocks as sql
from review.engine import statements as stmt
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cursors.py](../engine/cursors.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/engine/statements.py](../engine/statements.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `DoublyDrivenParagraphCheck` - L53-L156

```python
class DoublyDrivenParagraphCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-33'
TITLE = 'Business paragraph has exactly one driving edge'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 330
```

### `DoublyDrivenParagraphCheck.relevant` - L60-L62

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `cursors.paragraph_sets`, `any`, `sets.values`.

### `DoublyDrivenParagraphCheck.not_relevant_reason` - L64-L65

```python
not_relevant_reason(self) -> str
```

### `DoublyDrivenParagraphCheck._performed_in` - L69-L79

```python
_performed_in(body: list[str], skip: set[str]) -> set[str]
```

Paragraph names PERFORMed from inside a paragraph body.

Observed calls (lexical order): `set`, `PERFORM_TARGET.match`, `sql.norm`, `match.group`, `match.group('name').upper`, `found.add`.

Control points:

- L72: `for raw in body`
- L74: `if not match`
- L77: `if name not in skip`

### `DoublyDrivenParagraphCheck._driven_by_eoc` - L82-L97

```python
_driven_by_eoc(view) -> dict[str, str]
```

{paragraph: cursor flag} for every PERFORM ... UNTIL <x>-EOC.

Observed calls (lexical order): `stmt.joined_statements`, `PERFORM_UNTIL.match`, `match.group`, `match.group('condition').upper`, `match.group('name').upper`.

Control points:

- L89: `for (_index, text) in stmt.joined_statements(view)`
- L91: `if not match`
- L94: `if std.CURSOR_EOC_SUFFIX not in condition`

### `DoublyDrivenParagraphCheck.review` - L100-L156

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.paragraph_sets`, `self._driven_by_eoc`, `para.name.upper`, `sets.values`, `group.values`, `sets.items`, `sorted`, `group.get`, `cursor_name.upper`, `cursors.paragraph_body`, `self._performed_in`, `driven.get`, `doubly.append`, `driven.items`, `fetch.name.upper`, `undriven.append`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L113: `for (cursor_name, group) in sorted(sets.items())`
- L115: `if fetch is None`
- L125: `for name in sorted(performed)`
- L127: `if condition and flag in condition`
- L139: `if not fetch_loops`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
