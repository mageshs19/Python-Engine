# `review/checks/chk_05_sql_error_routing.py`

Source: [review/checks/chk_05_sql_error_routing.py](../../../../review/checks/chk_05_sql_error_routing.py) | 185 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `23b4066d6cab79b4631d4aae1fc00ba9da120bae53bea4cf4d3a2a4f5c372cb4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-05 SQL error paragraph and routing.

## Module-level bindings

`PERFORM_SQL_ERROR` (L13), `PARA_HEADER` (L14), `MOVE_SQL_LOCATION` (L24), `EXEC_SQL` (L28)

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

### `SqlErrorRoutingCheck` - L31-L185

```python
class SqlErrorRoutingCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-05'
TITLE = 'SQL error paragraph and routing'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 50
```

### `SqlErrorRoutingCheck.relevant` - L38-L39

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `view.has_code_token`.

### `SqlErrorRoutingCheck.not_relevant_reason` - L41-L42

```python
not_relevant_reason(self) -> str
```

### `SqlErrorRoutingCheck.review` - L44-L136

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `m.group`, `PARA_HEADER.match`, `getattr`, `bool`, `view.has_code_token`, `record.expect`, `record.skip`, `declared.count`, `record.expect_none`, `view.exact`, `view.searching`, `self._target_of`, `set`, `declared_set.add`, `record.ok`, `view.matching`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L73: `if standard not in declared and included`
- L107: `if included`
- L120: `if not performs`

### `SqlErrorRoutingCheck._review_body` - L142-L170

```python
_review_body(view, record, standard: str) -> None
```

The SQLERROR routine carries the site's agreed body.

Observed calls (lexical order): `getattr`, `token.upper`, `record.skip`, `record.expect_all`.

Control points:

- L160: `if not body`

### `SqlErrorRoutingCheck._target_of` - L176-L185

```python
_target_of(line) -> str
```

Performed paragraph name, or '' when the line does not match.

Observed calls (lexical order): `PERFORM_SQL_ERROR.search`, `match.group`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
