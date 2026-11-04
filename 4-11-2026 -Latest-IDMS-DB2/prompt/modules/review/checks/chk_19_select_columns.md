# `review/checks/chk_19_select_columns.py`

Source: [review/checks/chk_19_select_columns.py](../../../../review/checks/chk_19_select_columns.py) | 46 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `89ccfdd80a2235f77bd375946317927948318890dbc751420b2f20fa2fa4a31c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-19 SELECT operations - column names match DCLGEN.

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

### `SelectColumnsCheck` - L9-L46

```python
class SelectColumnsCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-19'
TITLE = 'SELECT operations - column names match DCLGEN'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 190
```

### `SelectColumnsCheck.relevant` - L16-L18

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `sql.sql_blocks`, `bool`.

### `SelectColumnsCheck.not_relevant_reason` - L20-L21

```python
not_relevant_reason(self) -> str
```

### `SelectColumnsCheck.review` - L23-L46

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `s.has`, `record.expect_none`, `record.ok`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
