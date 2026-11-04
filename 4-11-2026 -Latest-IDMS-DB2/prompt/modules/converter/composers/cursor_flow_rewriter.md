# `converter/composers/cursor_flow_rewriter.py`

Source: [converter/composers/cursor_flow_rewriter.py](../../../../converter/composers/cursor_flow_rewriter.py) | 221 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `1d677e7152908e4f612b06402c92292010c8f906ffe7a70340b43f9b073c589d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor flow rewriter.

## Import declarations

```python
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from converter.composers.cursor_flow_models import CursorFlowPlan
from patterns.cursor_flow_patterns import ANY_PARAGRAPH_HEADER_PATTERN, CONTINUE_PATTERN, CURSOR_PARAGRAPH_HEADER_PATTERN, WHEN_ZERO_PATTERN
from rules.cursor_flow_rules import NON_PARAGRAPH_DOTTED_LINES, NON_PARAGRAPH_HEADER_PREFIXES
```

## Local dependency notes

- [converter/composers/cursor_flow_line_formatter.py](cursor_flow_line_formatter.md)
- [converter/composers/cursor_flow_models.py](cursor_flow_models.md)
- [patterns/cursor_flow_patterns.py](../../patterns/cursor_flow_patterns.md)
- [rules/cursor_flow_rules.py](../../rules/cursor_flow_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_cursor_flow_plan_safety.py](../../tests/test_cursor_flow_plan_safety.md)

## Symbol contracts and control points

### `CursorFlowRewriter` - L25-L221

```python
class CursorFlowRewriter()
```

### `CursorFlowRewriter.__init__` - L26-L30

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `CursorFlowRewriter._logical` - L32-L33

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_formatter.logical`.

### `CursorFlowRewriter.rewrite_main_flow` - L35-L78

```python
rewrite_main_flow(self, lines: list[str], plans: list[CursorFlowPlan]) -> list[str]
```

Observed calls (lexical order): `set`, `indexes_to_skip.add`, `enumerate`, `plan_by_open_index.get`, `output.append`, `self.line_formatter.format_like_line`.

Control points:

- L43: `for plan in plans`
- L47: `if plan.close_index >= 0`
- L52: `for (index, line) in enumerate(lines)`
- L53: `if index in indexes_to_skip`
- L57: `if plan is None`

### `CursorFlowRewriter.rewrite_fetch_paragraphs` - L80-L133

```python
rewrite_fetch_paragraphs(self, lines: list[str], plans: list[CursorFlowPlan]) -> list[str]
```

Observed calls (lexical order): `plan.fetch_paragraph.upper`, `len`, `self._logical`, `CURSOR_PARAGRAPH_HEADER_PATTERN.match`, `output.append`, `header_match.group`, `header_match.group('operation').upper`, `f'{header_match.group('number')}-FETCH-{header_match.group('cursor')}'.upper`, `business_by_fetch_paragraph.get`, `self._collect_paragraph`, `output.extend`, `self._replace_when_zero_continue`.

Control points:

- L93: `while index < len(lines)`
- L97: `if not header_match`
- L102: `if header_match.group('operation').upper() != 'FETCH'`
- L116: `if not business_paragraph`

### `CursorFlowRewriter._collect_paragraph` - L135-L154

```python
_collect_paragraph(self, lines: list[str], start_index: int) -> tuple[list[str], int]
```

Observed calls (lexical order): `len`, `self._logical`, `CURSOR_PARAGRAPH_HEADER_PATTERN.match`, `self._is_non_cursor_paragraph_header`, `output.append`.

Control points:

- L143: `while index < len(lines)`
- L146: `if CURSOR_PARAGRAPH_HEADER_PATTERN.match(logical)`
- L148: `if self._is_non_cursor_paragraph_header(logical)`

### `CursorFlowRewriter._replace_when_zero_continue` - L156-L195

```python
_replace_when_zero_continue(self, paragraph_lines: list[str], business_paragraph: str) -> list[str]
```

Observed calls (lexical order): `len`, `self._logical`, `output.append`, `WHEN_ZERO_PATTERN.match`, `self._next_non_blank_index`, `CONTINUE_PATTERN.match`, `output.extend`, `self.line_formatter.format_like_line`.

Control points:

- L164: `while index < len(paragraph_lines)`
- L169: `if not WHEN_ZERO_PATTERN.match(logical)`
- L177: `if next_index < 0`
- L182: `if not CONTINUE_PATTERN.match(self._logical(next_line))`

### `CursorFlowRewriter._next_non_blank_index` - L197-L205

```python
_next_non_blank_index(self, lines: list[str], start_index: int) -> int
```

Observed calls (lexical order): `len`, `range`, `self._logical`.

Control points:

- L202: `for index in range(start_index, len(lines))`
- L203: `if self._logical(lines[index])`

### `CursorFlowRewriter._is_non_cursor_paragraph_header` - L207-L221

```python
_is_non_cursor_paragraph_header(self, logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `str(logical or '').strip().upper`, `normalized.startswith`, `ANY_PARAGRAPH_HEADER_PATTERN.match`, `CURSOR_PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L210: `if not normalized`
- L212: `if normalized in NON_PARAGRAPH_DOTTED_LINES`
- L214: `if normalized.startswith(NON_PARAGRAPH_HEADER_PREFIXES)`
- L216: `if not ANY_PARAGRAPH_HEADER_PATTERN.match(normalized)`
- L218: `if CURSOR_PARAGRAPH_HEADER_PATTERN.match(normalized)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
