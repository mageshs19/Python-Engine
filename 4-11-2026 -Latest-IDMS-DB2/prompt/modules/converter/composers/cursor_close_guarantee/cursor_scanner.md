# `converter/composers/cursor_close_guarantee/cursor_scanner.py`

Source: [converter/composers/cursor_close_guarantee/cursor_scanner.py](../../../../../converter/composers/cursor_close_guarantee/cursor_scanner.py) | 124 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `0998098f0f22ff3fda725d02250209dc3f8c1ab86dfec5082cd21aabef24b315`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Read-only discovery of generated cursor paragraphs and their PERFORMs.

## Module-level bindings

`PARAGRAPH_NAME_TEMPLATE` (L24), `__all__` (L124)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.line_utils import CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.models import CursorParagraphSet, CursorPerform
from patterns.cursor_close_guarantee_patterns import CURSOR_PARAGRAPH_HEADER_PATTERN, PERFORM_CURSOR_PARAGRAPH_PATTERN
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/line_utils.py](line_utils.md)
- [converter/composers/cursor_close_guarantee/models.py](models.md)
- [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)

## Symbol contracts and control points

### `CursorScanner` - L27-L121

```python
class CursorScanner()
```

Finds generated cursor paragraphs and every PERFORM of them.

### `CursorScanner.__init__` - L30-L34

```python
__init__(self, line_utils: CursorGuaranteeLineUtils | None=None) -> None
```

Observed calls (lexical order): `CursorGuaranteeLineUtils`.

### `CursorScanner.paragraph_sets` - L39-L68

```python
paragraph_sets(self, lines: list[str]) -> dict
```

Map every cursor to its generated OPEN / FETCH / CLOSE names.

Observed calls (lexical order): `self.lines_utils.logical`, `CURSOR_PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `match.group('operation').upper`, `PARAGRAPH_NAME_TEMPLATE.format`, `int`, `found.setdefault`, `CursorParagraphSet`, `entry.remember`.

Control points:

- L43: `for line in lines`
- L46: `if not logical`
- L51: `if not match`

### `CursorScanner.performs` - L73-L114

```python
performs(self, lines: list[str], cursor: str) -> list[CursorPerform]
```

Every PERFORM of a generated paragraph belonging to one cursor.

Observed calls (lexical order): `str`, `str(cursor or '').upper`, `enumerate`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `match.group('operation').upper`, `output.append`, `CursorPerform`, `PARAGRAPH_NAME_TEMPLATE.format`, `int`, `str(match.group('tail') or '').strip`.

Control points:

- L82: `if not target`
- L85: `for (index, line) in enumerate(lines)`
- L88: `if not logical or self.lines_utils.is_comment(logical)`
- L93: `if not match`
- L96: `if match.group('cursor').upper() != target`

### `CursorScanner.by_operation` - L117-L121

```python
by_operation(performs: list[CursorPerform], operation: str) -> list[CursorPerform]
```

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
