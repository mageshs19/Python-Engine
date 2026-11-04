# `converter/composers/cursor_close_guarantee/paragraph_index.py`

Source: [converter/composers/cursor_close_guarantee/paragraph_index.py](../../../../../converter/composers/cursor_close_guarantee/paragraph_index.py) | 158 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `96165386ebd902aa0af9e5a01ec22479ccf911104fd29064de6ee3f4875903f5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Paragraph discovery and navigation over generated COBOL lines.

## Module-level bindings

`__all__` (L158)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.line_utils import CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.models import ParagraphHeader
from patterns.cursor_close_guarantee_patterns import PARAGRAPH_HEADER_PATTERN, SECTION_HEADER_PATTERN
from rules.cursor_close_guarantee_rules import NON_PARAGRAPH_SINGLE_WORDS
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/line_utils.py](line_utils.md)
- [converter/composers/cursor_close_guarantee/models.py](models.md)
- [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)
- [converter/composers/cursor_close_guarantee/loop_synthesiser.py](loop_synthesiser.md)

## Symbol contracts and control points

### `ParagraphIndex` - L26-L155

```python
class ParagraphIndex()
```

Finds paragraph headers and navigates between statements.

### `ParagraphIndex.__init__` - L29-L33

```python
__init__(self, line_utils: CursorGuaranteeLineUtils | None=None) -> None
```

Observed calls (lexical order): `CursorGuaranteeLineUtils`.

### `ParagraphIndex.headers` - L38-L69

```python
headers(self, lines: list[str]) -> list[ParagraphHeader]
```

Every real paragraph header, cursor paragraphs included.

Observed calls (lexical order): `enumerate`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `SECTION_HEADER_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`, `ParagraphHeader`, `output.append`.

Control points:

- L48: `for (index, line) in enumerate(lines)`
- L51: `if not logical or self.lines_utils.is_comment(logical)`
- L54: `if SECTION_HEADER_PATTERN.match(logical)`
- L59: `if not match`
- L64: `if name in NON_PARAGRAPH_SINGLE_WORDS`

### `ParagraphIndex.owner_paragraph` - L75-L87

```python
owner_paragraph(headers: list[ParagraphHeader], index: int) -> str
```

Name of the paragraph that physically contains a line index.

Control points:

- L82: `for header in headers`
- L83: `if header.index >= index`

### `ParagraphIndex.span` - L90-L113

```python
span(headers: list[ParagraphHeader], name: str, total: int) -> tuple[int, int] | None
```

(first body line, first line after the paragraph).

Observed calls (lexical order): `str`, `str(name or '').upper`, `enumerate`, `len`, `min`.

Control points:

- L98: `if not target`
- L101: `for (position, header) in enumerate(headers)`
- L102: `if header.name != target`

### `ParagraphIndex.exists` - L115-L117

```python
exists(self, headers: list[ParagraphHeader], name: str) -> bool
```

Observed calls (lexical order): `str`, `str(name or '').upper`, `any`.

### `ParagraphIndex.next_executable_index` - L122-L133

```python
next_executable_index(self, lines: list[str], start: int, end: int) -> int
```

Observed calls (lexical order): `len`, `max`, `min`, `range`, `self.lines_utils.is_blank_or_comment`.

Control points:

- L128: `for index in range(max(0, start), min(end, len(lines)))`
- L129: `if self.lines_utils.is_blank_or_comment(lines[index])`

### `ParagraphIndex.previous_executable_index` - L135-L155

```python
previous_executable_index(self, lines: list[str], start: int) -> int
```

Previous statement, refusing to cross a paragraph boundary.

Observed calls (lexical order): `len`, `min`, `range`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L141: `if not lines`
- L144: `for index in range(min(start, len(lines) - 1), -1, -1)`
- L147: `if not logical or self.lines_utils.is_comment(logical)`
- L150: `if PARAGRAPH_HEADER_PATTERN.match(logical)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
