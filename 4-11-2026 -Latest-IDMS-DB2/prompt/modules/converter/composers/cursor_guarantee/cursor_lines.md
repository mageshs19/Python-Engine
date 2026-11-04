# `converter/composers/cursor_guarantee/cursor_lines.py`

Source: [converter/composers/cursor_guarantee/cursor_lines.py](../../../../../converter/composers/cursor_guarantee/cursor_lines.py) | 230 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `4bad8466f352f73b0822a13bb9dd686528ce0cbb3775aa544e981d357c733d33`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Logical-line access and paragraph navigation.

## Module-level bindings

`__all__` (L230)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from converter.composers.cursor_guarantee.cursor_models import COMMENT_INDICATORS, PARAGRAPH_HEADER_PATTERN, SECTION_HEADER_PATTERN, UNTIL_KEYWORD, ParagraphHeader
from rules.cursor_close_guarantee_rules import LEGACY_EOC_CONDITIONS, NON_PARAGRAPH_SINGLE_WORDS
```

## Local dependency notes

- [converter/composers/cursor_flow_line_formatter.py](../cursor_flow_line_formatter.md)
- [converter/composers/cursor_guarantee/cursor_models.py](cursor_models.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee_composer.py](../cursor_close_guarantee_composer.md)
- [converter/composers/cursor_guarantee/__init__.py](__init__.md)
- [converter/composers/cursor_guarantee/cursor_repair.py](cursor_repair.md)
- [converter/composers/cursor_guarantee/cursor_scanner.py](cursor_scanner.md)
- [tests/pipeline/test_single_owner_transformations.py](../../../tests/pipeline/test_single_owner_transformations.md)

## Symbol contracts and control points

### `CursorLines` - L35-L227

```python
class CursorLines()
```

Line inspection, line rewriting and paragraph navigation.

### `CursorLines.__init__` - L38-L42

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `CursorLines.logical` - L47-L55

```python
logical(self, line: str) -> str
```

The COBOL body, sequence area and indicator removed.

Observed calls (lexical order): `self.line_formatter.logical`, `str`, `str(self.line_formatter.logical(line) or '').strip`, `str(line or '').strip`.

### `CursorLines.format_like` - L57-L62

```python
format_like(self, reference_line: str, body: str) -> str
```

Rebuild `body` inside the fixed-format frame of a real line.

Observed calls (lexical order): `self.line_formatter.format_like_line`.

### `CursorLines.is_comment` - L65-L67

```python
is_comment(logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `bool`.

### `CursorLines.compress` - L70-L72

```python
compress(text: str) -> str
```

Whitespace-insensitive, case-insensitive comparison form.

Observed calls (lexical order): `' '.join`, `' '.join(str(text or '').split()).upper`, `str`, `str(text or '').split`.

### `CursorLines.normalize_line_endings` - L75-L76

```python
normalize_line_endings(text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `CursorLines.partition_until` - L82-L93

```python
partition_until(logical: str) -> tuple[str, str, str]
```

Split a logical line on UNTIL, preserving the original case.

Observed calls (lexical order): `str`, `text.upper`, `text.upper().find`, `len`, `text[position + len(UNTIL_KEYWORD):].strip`.

Control points:

- L87: `if position < 0`

### `CursorLines.is_legacy_condition` - L95-L117

```python
is_legacy_condition(self, condition: str) -> bool
```

True for a raw SQLCODE / IDMS end test still in the loop.

Observed calls (lexical order): `self.compress`, `any`, `re.sub`, `re.fullmatch`.

Control points:

- L99: `if not current`
- L102: `if any((current == self.compress(candidate) for candidate in LEGACY_EOC_CONDITIONS))`

### `CursorLines.next_executable_index` - L122-L136

```python
next_executable_index(self, lines: list[str], start: int, end: int) -> int
```

Observed calls (lexical order): `len`, `max`, `min`, `range`, `self.logical`, `self.is_comment`.

Control points:

- L128: `for index in range(max(0, start), min(end, len(lines)))`
- L131: `if not logical or self.is_comment(logical)`

### `CursorLines.previous_executable_index` - L138-L158

```python
previous_executable_index(self, lines: list[str], start: int) -> int
```

Previous statement, refusing to cross a paragraph boundary.

Observed calls (lexical order): `len`, `min`, `range`, `self.logical`, `self.is_comment`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L144: `if not lines`
- L147: `for index in range(min(start, len(lines) - 1), -1, -1)`
- L150: `if not logical or self.is_comment(logical)`
- L153: `if PARAGRAPH_HEADER_PATTERN.match(logical)`

### `CursorLines.paragraph_headers` - L163-L189

```python
paragraph_headers(self, lines: list[str]) -> list[ParagraphHeader]
```

Every real paragraph header, cursor paragraphs included.

Observed calls (lexical order): `enumerate`, `self.logical`, `self.is_comment`, `SECTION_HEADER_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`, `ParagraphHeader`, `headers.append`.

Control points:

- L167: `for (index, line) in enumerate(lines)`
- L170: `if not logical or self.is_comment(logical)`
- L173: `if SECTION_HEADER_PATTERN.match(logical)`
- L178: `if not match`
- L184: `if name in NON_PARAGRAPH_SINGLE_WORDS`

### `CursorLines.owner_paragraph` - L192-L204

```python
owner_paragraph(headers: list[ParagraphHeader], index: int) -> str
```

Name of the paragraph that physically contains a line index.

Control points:

- L199: `for header in headers`
- L200: `if header.index >= index`

### `CursorLines.paragraph_span` - L207-L227

```python
paragraph_span(headers: list[ParagraphHeader], name: str, total: int) -> tuple[int, int] | None
```

(first body line, first line after the paragraph).

Observed calls (lexical order): `str`, `str(name or '').upper`, `enumerate`, `len`, `min`.

Control points:

- L215: `for (position, header) in enumerate(headers)`
- L216: `if header.name != target`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
