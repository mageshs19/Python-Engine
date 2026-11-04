# `review/checks/chk_09_record_retrieval_conversion.py`

Source: [review/checks/chk_09_record_retrieval_conversion.py](../../../../review/checks/chk_09_record_retrieval_conversion.py) | 161 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `663d65d6184f46fefeb1af05aa2572be650fe113640794ecfd532d23284e6ea1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-09 Record retrieval conversion.

## Import declarations

```python
from __future__ import annotations
from review.engine import sql_blocks as sql
from review.engine.check_base import MAJOR, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `RecordRetrievalConversionCheck` - L10-L161

```python
class RecordRetrievalConversionCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-09'
TITLE = 'Record retrieval conversion'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 90
```

### `RecordRetrievalConversionCheck.relevant` - L17-L18

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `view.has_code_token`.

### `RecordRetrievalConversionCheck.not_relevant_reason` - L20-L21

```python
not_relevant_reason(self) -> str
```

### `RecordRetrievalConversionCheck.review` - L23-L116

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `sql.targets_restart`, `record.expect_none`, `any`, `record.skip`, `b.has`, `self._location_set_before`, `self._empty_paragraphs`, `record.ok`.

Control points:

- L46: `if not selects`
- L58: `if not selects`
- L70: `if not std.ENFORCE_SELECT_WHERE`
- L75: `if not selects`
- L87: `if not std.ENFORCE_SQL_LOCATION_BEFORE_SQL`
- L93: `if not retrieval`
- L111: `if not empty`

### `RecordRetrievalConversionCheck._location_set_before` - L120-L143

```python
_location_set_before(view, block) -> bool
```

True when SQL-LOCATION is set within the look-back window.

Observed calls (lexical order): `getattr`, `sql.lines_before`, `any`, `line.startswith`, `tuple`.

### `RecordRetrievalConversionCheck._empty_paragraphs` - L145-L161

```python
_empty_paragraphs(view) -> list
```

Paragraph headers immediately followed by another header.

Observed calls (lexical order): `enumerate`, `logical.endswith`, `nxt.endswith`, `out.append`.

Control points:

- L149: `for (index, line) in enumerate(code[:-1])`
- L151: `if not logical.endswith('.') or ' ' in logical`
- L154: `if not name or name in std.NON_PARAGRAPH_WORDS`
- L157: `if nxt.endswith('.') and ' ' not in nxt`
- L159: `if following and following not in std.NON_PARAGRAPH_WORDS`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
