# `review/engine/sql_location.py`

Source: [review/engine/sql_location.py](../../../../review/engine/sql_location.py) | 51 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `1af5a47c968f2064db6d1479b1e4f1f99cc4b360925aa8fec923428b87ebfe2c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared SQL-LOCATION detection for CHK-05, CHK-09, CHK-10 and CHK-20.

## Module-level bindings

`MOVE_SQL_LOCATION` (L32)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import sql_blocks as sql
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](__init__.md)
- [review/engine/sql_blocks.py](sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `is_location_move` - L39-L41

```python
is_location_move(line: str) -> bool
```

True when the logical line sets SQL-LOCATION in an accepted form.

Observed calls (lexical order): `MOVE_SQL_LOCATION.match`, `bool`, `sql.norm`.

### `set_before` - L44-L51

```python
set_before(view, block, lookback: int | None=None) -> bool
```

True when SQL-LOCATION is set within the look-back window of a block.

Observed calls (lexical order): `sql.lines_before`, `any`, `is_location_move`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
