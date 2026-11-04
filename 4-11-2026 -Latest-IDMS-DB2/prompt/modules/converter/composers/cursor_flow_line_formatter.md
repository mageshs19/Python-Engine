# `converter/composers/cursor_flow_line_formatter.py`

Source: [converter/composers/cursor_flow_line_formatter.py](../../../../converter/composers/cursor_flow_line_formatter.py) | 71 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `112c8ce981cede977ca146e9f3aacd378977f7100931c6e28df9ddbad93642cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor flow line formatter.

## Import declarations

```python
from patterns.sequence_patterns import strip_sequence_numbers
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/line_utils.py](cursor_close_guarantee/line_utils.md)
- [converter/composers/cursor_flow/legacy_error_status_loop_normalizer.py](cursor_flow/legacy_error_status_loop_normalizer.md)
- [converter/composers/cursor_flow/loop_shape.py](cursor_flow/loop_shape.md)
- [converter/composers/cursor_flow/span_loop_plan.py](cursor_flow/span_loop_plan.md)
- [converter/composers/cursor_flow/span_loop_rewriter.py](cursor_flow/span_loop_rewriter.md)
- [converter/composers/cursor_flow_obtain_next_cleanup.py](cursor_flow_obtain_next_cleanup.md)
- [converter/composers/cursor_flow_plan_discoverer.py](cursor_flow_plan_discoverer.md)
- [converter/composers/cursor_flow_rewriter.py](cursor_flow_rewriter.md)
- [converter/composers/cursor_guarantee/cursor_lines.py](cursor_guarantee/cursor_lines.md)

## Symbol contracts and control points

### `CursorFlowLineFormatter` - L12-L71

```python
class CursorFlowLineFormatter()
```

Declared class/data-model fields:

```python
FIXED_FORMAT_MIN_WIDTH = 80
BODY_WIDTH = 65
```

### `CursorFlowLineFormatter.logical` - L16-L17

```python
logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

### `CursorFlowLineFormatter.normalize_line_endings` - L19-L20

```python
normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `CursorFlowLineFormatter.format_like_line` - L22-L44

```python
format_like_line(self, reference_line: str, replacement_body: str) -> str
```

Observed calls (lexical order): `str`, `str(reference_line or '').rstrip`, `self._is_fixed_format_line`, `self._body_with_reference_indent`, `body[:self.BODY_WIDTH].ljust`, `self.leading_spaces`.

Control points:

- L29: `if self._is_fixed_format_line(line)`

### `CursorFlowLineFormatter._body_with_reference_indent` - L46-L53

```python
_body_with_reference_indent(self, reference_line: str, replacement_body: str) -> str
```

Observed calls (lexical order): `reference_line[7:72].rstrip`, `self.leading_spaces`.

### `CursorFlowLineFormatter._is_fixed_format_line` - L55-L62

```python
_is_fixed_format_line(self, line: str) -> bool
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[72:80].isdigit`.

Control points:

- L56: `if len(line) < self.FIXED_FORMAT_MIN_WIDTH`
- L58: `if not line[:6].isdigit()`
- L60: `if not line[72:80].isdigit()`

### `CursorFlowLineFormatter.leading_spaces` - L64-L71

```python
leading_spaces(self, text: str, default: str='') -> str
```

Observed calls (lexical order): `str`, `len`, `value.lstrip`.

Control points:

- L66: `if not value`
- L69: `if count <= 0`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
