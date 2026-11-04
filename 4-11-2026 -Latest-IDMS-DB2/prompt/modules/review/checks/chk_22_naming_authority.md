# `review/checks/chk_22_naming_authority.py`

Source: [review/checks/chk_22_naming_authority.py](../../../../review/checks/chk_22_naming_authority.py) | 138 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `594244a63fe877c4700fb4128a8e60c1befa73ea7e16ba872faa264bff39cae0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-22 DB2 table and column naming authority.

## Module-level bindings

`TABLE` (L11), `HOST_DOT` (L14)

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

### `NamingAuthorityCheck` - L17-L138

```python
class NamingAuthorityCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-22'
TITLE = 'DB2 table and column naming authority'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 220
```

### `NamingAuthorityCheck.relevant` - L24-L25

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `view.has_code_token`.

### `NamingAuthorityCheck.not_relevant_reason` - L27-L28

```python
not_relevant_reason(self) -> str
```

### `NamingAuthorityCheck.review` - L30-L138

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `match.group`, `TABLE.finditer`, `meta.mapped_tables`, `meta.dclgen_tables`, `record.skip`, `record.expect_all`, `sorted`, `TABLE.search`, `meta.columns_for_table`, `found.group`, `found.group('field').replace`, `HOST_DOT.finditer`, `', '.join`, `offenders.append`, `std.DCLGEN_GROUP_PREFIX.upper`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L43: `if not std.ENFORCE_TABLE_AUTHORITY`
- L48: `if not authority`
- L60: `if not declared`
- L72: `if not std.ENFORCE_COLUMN_AUTHORITY`
- L77: `if not declared`
- L84: `for block in blocks`
- L86: `if not match`
- L90: `if not available`
- Another 3 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
