# `review/checks/chk_18_sql_statements.py`

Source: [review/checks/chk_18_sql_statements.py](../../../../review/checks/chk_18_sql_statements.py) | 140 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `e3e0299c434efb2cf7ad8007080a54ca67eeb179f16b69b8e0fe6f13069ccaee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-18 SQL statements & host variable binding.

## Module-level bindings

`RECOGNISED_VERBS` (L46), `OPENER` (L66), `TERMINATOR` (L67)

## Import declarations

```python
from __future__ import annotations
from review.engine import sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)

## Symbol contracts and control points

### `SQLStatementsCheck` - L70-L140

```python
class SQLStatementsCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-18'
TITLE = 'SQL statements & host variable binding'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 180
```

### `SQLStatementsCheck.relevant` - L77-L78

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`, `sql.sql_blocks`.

### `SQLStatementsCheck.not_relevant_reason` - L80-L81

```python
not_relevant_reason(self) -> str
```

### `SQLStatementsCheck.review` - L84-L140

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `sql.norm`, `opener_lines.append`, `record.ok`, `record.fail`, `record.expect_none`, `', '.join`, `record.skip`.

Control points:

- L96: `for line in view.code`
- L98: `if OPENER in logical`
- L100: `if TERMINATOR not in logical`
- L102: `if TERMINATOR in logical`
- L105: `if openers == terminators`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
