# `review/checks/chk_20_into_clause_binding.py`

Source: [review/checks/chk_20_into_clause_binding.py](../../../../review/checks/chk_20_into_clause_binding.py) | 57 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `a725ad812fb62f4425d2b6847cd26dce7e19ccf0f59b7622de7c7db05dd4bdf7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-20 INTO clause - host variables bind SELECT results.

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

### `IntoClauseBindingCheck` - L15-L57

```python
class IntoClauseBindingCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-20'
TITLE = 'INTO clause - host variables bind SELECT results'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 200
```

### `IntoClauseBindingCheck.relevant` - L22-L24

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `sql.sql_blocks`, `any`, `s.has`.

### `IntoClauseBindingCheck.not_relevant_reason` - L26-L27

```python
not_relevant_reason(self) -> str
```

### `IntoClauseBindingCheck.review` - L29-L57

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `s.has`, `record.expect`, `bool`, `len`, `record.ok`, `record.pass_all`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
