# `review/checks/chk_11_sqlcode_commit_conversion.py`

Source: [review/checks/chk_11_sqlcode_commit_conversion.py](../../../../review/checks/chk_11_sqlcode_commit_conversion.py) | 312 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `67511070ce34be6bd9327505b477eb91d74fad1c011f3544aeed3cb463c4f2b9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-11 SQLCODE and COMMIT conversion.

## Module-level bindings

`EVALUATE_ANY` (L11), `PERIOD` (L12), `IDMS_UPDATE_VERBS` (L13)

## Import declarations

```python
from __future__ import annotations
import re
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

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_review_business_semantics.py](../../tests/test_review_business_semantics.md)

## Symbol contracts and control points

### `SqlcodeCommitConversionCheck` - L16-L312

```python
class SqlcodeCommitConversionCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-11'
TITLE = 'SQLCODE and COMMIT conversion'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 110
```

### `SqlcodeCommitConversionCheck.relevant` - L23-L24

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `view.has_code_token`.

### `SqlcodeCommitConversionCheck.not_relevant_reason` - L26-L27

```python
not_relevant_reason(self) -> str
```

### `SqlcodeCommitConversionCheck.review` - L29-L222

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `list`, `sql.norm`, `sql.sql_blocks`, `self._evaluate_spans`, `self._sql_block_indexes`, `record.expect_none`, `any`, `record.skip`, `record.expect`, `bool`, `record.expect_all`, `self._span_has`, `self._checked_after`, `view.has_code_token`, `line.startswith`, `self._source_requires_commit`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L63: `if not std.USE_EVALUATE_SQLCODE`
- L68: `if not executable`
- L86: `if not spans`
- L102: `if not spans`
- L122: `if not spans`
- L141: `if not executable`
- L153: `if not any((b.verb == 'FETCH' for b in blocks))`
- L171: `if not ctx.has_source`
- Another 4 conditions/loops exist in this source span.

### `SqlcodeCommitConversionCheck._source_requires_commit` - L226-L236

```python
_source_requires_commit(source: str) -> bool
```

FINISH is not itself proof that DB2 COMMIT is required.

Observed calls (lexical order): `str`, `str(source or '').upper`, `re.search`, `any`.

Control points:

- L234: `if re.search('\\bCOMMIT\\b', text)`

### `SqlcodeCommitConversionCheck._evaluate_spans` - L240-L263

```python
_evaluate_spans(code: list[str]) -> list[tuple[int, int]]
```

Start and end index of each EVALUATE SQLCODE block.

Observed calls (lexical order): `enumerate`, `line.startswith`, `len`, `range`, `current.startswith`, `spans.append`.

Control points:

- L248: `for (index, line) in enumerate(code)`
- L249: `if not line.startswith(std.SQLCODE_EVALUATE_START)`
- L253: `for cursor in range(index, len(code))`
- L255: `if current.startswith(std.SQLCODE_EVALUATE_END)`
- L257: `if depth <= 0`
- L260: `if current.startswith(EVALUATE_ANY)`

### `SqlcodeCommitConversionCheck._sql_block_indexes` - L266-L275

```python
_sql_block_indexes(blocks) -> set[int]
```

Code indexes occupied by EXEC SQL blocks.

Observed calls (lexical order): `set`, `out.update`, `range`.

Control points:

- L273: `for block in blocks`

### `SqlcodeCommitConversionCheck._interior_periods` - L278-L296

```python
_interior_periods(lines: list, code: list[str], spans: list[tuple[int, int]], sql_indexes: set[int]) -> list
```

Lines inside an EVALUATE that end with a period.

Observed calls (lexical order): `set`, `len`, `range`, `code[index].endswith`, `seen.add`, `out.append`.

Control points:

- L288: `for (start, end) in spans`
- L290: `for index in range(start + 1, stop)`
- L291: `if index in sql_indexes or index in seen`
- L293: `if code[index].endswith(PERIOD)`

### `SqlcodeCommitConversionCheck._span_has` - L299-L302

```python
_span_has(code: list[str], start: int, end: int, token: str) -> bool
```

Observed calls (lexical order): `len`, `sql.norm`, `any`.

### `SqlcodeCommitConversionCheck._checked_after` - L305-L312

```python
_checked_after(view, block) -> bool
```

Observed calls (lexical order): `sql.lines_after`, `any`, `line.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
