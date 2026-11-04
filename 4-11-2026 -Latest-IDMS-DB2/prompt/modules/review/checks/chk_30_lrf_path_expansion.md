# `review/checks/chk_30_lrf_path_expansion.py`

Source: [review/checks/chk_30_lrf_path_expansion.py](../../../../review/checks/chk_30_lrf_path_expansion.py) | 141 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `c9efd973cb5704ede5995d811950e991bc5e238f0164d2de2921e8eef983f57b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-30 LRF subschema path expansion - WHERE clause generation.

## Import declarations

```python
from __future__ import annotations
from review.engine import metadata as meta
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `LrfPathExpansionCheck` - L23-L141

```python
class LrfPathExpansionCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-30'
TITLE = 'LRF subschema path expansion - WHERE clause generation'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 300
```

### `LrfPathExpansionCheck.relevant` - L30-L35

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `l.logical.upper`, `any`.

### `LrfPathExpansionCheck.not_relevant_reason` - L37-L38

```python
not_relevant_reason(self) -> str
```

### `LrfPathExpansionCheck._marker_statements` - L42-L73

```python
_marker_statements(view) -> list[tuple[int, str]]
```

(line number, full marker text) for every LRF marker.

Observed calls (lexical order): `list`, `enumerate`, `line.logical.upper`, `range`, `len`, `nxt.logical.upper`, `out.append`.

Control points:

- L53: `for (index, line) in enumerate(lines)`
- L54: `if not line.is_comment`
- L57: `if std.LRF_EXPANSION_MARKER not in text`
- L61: `for offset in range(1, std.LRF_MARKER_CONTINUATION_LINES + 1)`
- L62: `if index + offset >= len(lines)`
- L65: `if not nxt.is_comment`
- L68: `if std.LRF_WITHIN_KEYWORD in joined`

### `LrfPathExpansionCheck.review` - L75-L141

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `self._marker_statements`, `any`, `record.expect_none`, `record.skip`, `record.expect_all`, `record.ok`, `len`, `l.logical.upper`, `record.expect`, `bool`.

Control points:

- L105: `if not markers`
- L122: `if extra`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
