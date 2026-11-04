# `review/checks/chk_17_restart_logic.py`

Source: [review/checks/chk_17_restart_logic.py](../../../../review/checks/chk_17_restart_logic.py) | 97 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `7b4ef41e1af749cab85a3994379fcacebf5c39ef93c7654752d72bf7cb6d9c75`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-17 Restart table logic - paragraph structure, SQL metadata, safe skip.

## Import declarations

```python
from __future__ import annotations
from review.engine import sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `RestartTableLogicCheck` - L10-L97

```python
class RestartTableLogicCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-17'
TITLE = 'Restart table logic - structure, SQL, safe skip'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 170
```

### `RestartTableLogicCheck.relevant` - L17-L24

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `any`, `sql.sql_blocks`, `sql.targets_restart`.

### `RestartTableLogicCheck.not_relevant_reason` - L26-L27

```python
not_relevant_reason(self) -> str
```

### `RestartTableLogicCheck.review` - L29-L97

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `sql.targets_restart`, `any`, `record.expect`, `record.ok`, `all`, `s.has`, `record.expect_none`, `u.has`, `i.has`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
