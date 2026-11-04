# `tests/cursor_where/conftest.py`

Source: [tests/cursor_where/conftest.py](../../../../tests/cursor_where/conftest.py) | 33 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `f9d988bd612f248c01af20324e126a89194dfc5ab7fac0020ebe1d2410d8e771`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixtures for the cursor WHERE suite.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.generators.db2_infrastructure.cursor_declare_builder import CursorDeclareBuilder
from tests.cursor_where._fixtures import ColumnNameResolver, LineUtils
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare_builder.py](../../converter/generators/db2_infrastructure/cursor_declare_builder.md)
- [tests/cursor_where/_fixtures.py](_fixtures.md)

## Symbol contracts and control points

### `declares` - L22-L24

```python
declares() -> CursorDeclareBuilder
```

Builder WITHOUT the ownership guard wired (guard stands down).

Observed calls (lexical order): `CursorDeclareBuilder`, `LineUtils`.

### `guarded_declares` - L28-L33

```python
guarded_declares() -> CursorDeclareBuilder
```

Builder WITH the ownership guard wired.

Observed calls (lexical order): `CursorDeclareBuilder`, `LineUtils`, `ColumnNameResolver`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
