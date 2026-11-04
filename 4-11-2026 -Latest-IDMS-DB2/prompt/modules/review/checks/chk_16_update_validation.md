# `review/checks/chk_16_update_validation.py`

Source: [review/checks/chk_16_update_validation.py](../../../../review/checks/chk_16_update_validation.py) | 122 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `8d7b021918e6c8c42f9b99757acac037b980d6264dd5c88c8f786510f0b05d94`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-16 UPDATE statement validation - SET, WHERE, audit fields.

## Module-level bindings

`SET_CLAUSE` (L23), `WHERE_CLAUSE` (L24), `ASSIGNMENT` (L25)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import metadata as meta, sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `UpdateStatementValidationCheck` - L28-L122

```python
class UpdateStatementValidationCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-16'
TITLE = 'UPDATE statement validation - columns, WHERE, audit fields'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 160
```

### `UpdateStatementValidationCheck.relevant` - L35-L40

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `any`, `sql.targets_restart`, `sql.sql_blocks`.

### `UpdateStatementValidationCheck.not_relevant_reason` - L42-L43

```python
not_relevant_reason(self) -> str
```

### `UpdateStatementValidationCheck.review` - L45-L122

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `sql.targets_restart`, `SET_CLAUSE.search`, `record.expect_none`, `match.group`, `ASSIGNMENT.findall`, `any`, `c.startswith`, `', '.join`, `offenders_audit.append`, `record.expect_all`, `WHERE_CLAUSE.search`, `record.pass_all`.

Control points:

- L65: `for b in updates_only`
- L67: `if match`
- L74: `if bad`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
