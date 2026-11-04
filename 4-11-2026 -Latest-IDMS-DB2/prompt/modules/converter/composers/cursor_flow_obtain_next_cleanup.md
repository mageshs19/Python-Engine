# `converter/composers/cursor_flow_obtain_next_cleanup.py`

Source: [converter/composers/cursor_flow_obtain_next_cleanup.py](../../../../converter/composers/cursor_flow_obtain_next_cleanup.py) | 98 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `11edec61682a72487ced04f5fa72e3a3f24e75448500e11636f59e1dddbdfc90`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor flow OBTAIN NEXT cleanup.

## Import declarations

```python
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from patterns.cursor_flow_patterns import CONVERTED_OBTAIN_COMMENT_PATTERN, CONVERTED_OBTAIN_NEXT_COMMENT_PATTERN, PERFORM_CURSOR_PATTERN
from rules.cursor_flow_rules import REMOVED_OBTAIN_NEXT_COMMENT
```

## Local dependency notes

- [converter/composers/cursor_flow_line_formatter.py](cursor_flow_line_formatter.md)
- [patterns/cursor_flow_patterns.py](../../patterns/cursor_flow_patterns.md)
- [rules/cursor_flow_rules.py](../../rules/cursor_flow_rules.md)

## Symbol contracts and control points

### `CursorFlowObtainNextCleanup` - L20-L98

```python
class CursorFlowObtainNextCleanup()
```

### `CursorFlowObtainNextCleanup.__init__` - L21-L25

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `CursorFlowObtainNextCleanup._logical` - L27-L28

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_formatter.logical`.

### `CursorFlowObtainNextCleanup.remove_leftover_obtain_next_cursor_calls` - L30-L65

```python
remove_leftover_obtain_next_cursor_calls(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `len`, `self._logical`, `CONVERTED_OBTAIN_NEXT_COMMENT_PATTERN.match`, `output.append`, `self._skip_obtain_next_block`, `self.line_formatter.format_like_line`.

Control points:

- L37: `while index < len(lines)`
- L40: `if not CONVERTED_OBTAIN_NEXT_COMMENT_PATTERN.match(logical)`

### `CursorFlowObtainNextCleanup._skip_obtain_next_block` - L67-L98

```python
_skip_obtain_next_block(self, lines: list[str], start_index: int, skipped_lines: list[str]) -> int
```

Observed calls (lexical order): `len`, `self._logical`, `skipped_lines.append`, `next_logical.startswith`, `CONVERTED_OBTAIN_COMMENT_PATTERN.match`, `PERFORM_CURSOR_PATTERN.match`.

Control points:

- L75: `while index < len(lines)`
- L78: `if not next_logical`
- L83: `if next_logical.startswith('*') and (not CONVERTED_OBTAIN_COMMENT_PATTERN.match(next_logical))`
- L88: `if CONVERTED_OBTAIN_COMMENT_PATTERN.match(next_logical)`
- L91: `if PERFORM_CURSOR_PATTERN.match(next_logical)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
