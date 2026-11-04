# `review/checks/chk_02_db2_infrastructure.py`

Source: [review/checks/chk_02_db2_infrastructure.py](../../../../review/checks/chk_02_db2_infrastructure.py) | 193 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `3877600bb3fe61f1023ea3ac1261b5e088a4c7113d0f3a82ed665d03385ed354`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-02 DB2 infrastructure declarations.

## Module-level bindings

`WS` (L13), `PD` (L14), `SQL_LOC` (L15), `WS_RUN` (L17), `EXEC_SQL_START` (L18), `EXEC_SQL_END` (L19), `DEFAULT_SOURCE_COPYBOOK` (L21)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `norm` - L24-L26

```python
norm(text: str) -> str
```

Uppercase, trimmed, with every internal whitespace run collapsed.

Observed calls (lexical order): `WS_RUN.sub`, `str`, `str(text or '').strip`, `str(text or '').strip().upper`.

### `statements` - L29-L62

```python
statements(lines: list[str]) -> list[str]
```

Logical statements, with EXEC SQL ... END-EXEC. joined into one entry.

Observed calls (lexical order): `norm`, `line.startswith`, `' '.join`, `out.append`, `buffer.append`.

Control points:

- L39: `for raw in lines`
- L42: `if not inside and line.startswith(EXEC_SQL_START)`
- L45: `if EXEC_SQL_END in line`
- L50: `if inside`
- L52: `if EXEC_SQL_END in line`
- L59: `if buffer`

### `Db2InfrastructureCheck` - L65-L193

```python
class Db2InfrastructureCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-02'
TITLE = 'DB2 infrastructure declarations'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 20
```

### `Db2InfrastructureCheck.review` - L72-L133

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `record.expect_all`, `view.has_code_token`, `statements`, `code.count`, `norm`, `self._review_sql_location`, `WS.match`, `enumerate`, `next`, `PD.match`, `record.expect`, `code.index`, `late.append`, `record.skip`, `record.expect_none`, `view.count_of`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L103: `if ws_at >= 0 and pd_at >= 0`
- L105: `for required in std.REQUIRED_LINES`
- L108: `if at >= 0 and (not ws_at < at < pd_at)`

### `Db2InfrastructureCheck._review_sql_location` - L138-L193

```python
_review_sql_location(self, code: list[str], record) -> None
```

SQL-LOCATION is declared, or deliberately supplied elsewhere.

Observed calls (lexical order): `m.group`, `m.group('pic').strip`, `SQL_LOC.match`, `getattr`, `record.ok`, `record.fail`, `', '.join`, `record.skip`.

Control points:

- L165: `if enforce`
- L166: `if pics`
- L176: `if pics`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
