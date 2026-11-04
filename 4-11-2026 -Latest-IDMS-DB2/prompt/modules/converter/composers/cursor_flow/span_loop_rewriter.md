# `converter/composers/cursor_flow/span_loop_rewriter.py`

Source: [converter/composers/cursor_flow/span_loop_rewriter.py](../../../../../converter/composers/cursor_flow/span_loop_rewriter.py) | 165 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `cf2890e80fec97720afccafcd07ccd7218a35890ef550ebeb0badf4bbc5a5a45`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Conservative rewrite for a SPAN driving loop.

## Module-level bindings

`__all__` (L165)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_flow.span_loop_plan import SpanLoopPlan
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from patterns.cursor_loop_patterns import PERFORM_CURSOR_PARAGRAPH_PATTERN, UNTIL_LINE_PATTERN
from rules.cursor_loop_rules import CLOSE_PRESENCE_WINDOW, CURSOR_LOOP_MESSAGES, PERFORM_CLOSE_TEMPLATE, STATEMENT_TERMINATOR, UNTIL_TEMPLATE, UNTIL_TERMINATED_TEMPLATE
```

## Local dependency notes

- [converter/composers/cursor_flow/span_loop_plan.py](span_loop_plan.md)
- [converter/composers/cursor_flow_line_formatter.py](../cursor_flow_line_formatter.md)
- [patterns/cursor_loop_patterns.py](../../../patterns/cursor_loop_patterns.md)
- [rules/cursor_loop_rules.py](../../../rules/cursor_loop_rules.md)

## Symbol contracts and control points

### `SpanLoopRewriter` - L35-L162

```python
class SpanLoopRewriter()
```

### `SpanLoopRewriter.__init__` - L36-L41

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `SpanLoopRewriter.rewrite` - L44-L65

```python
rewrite(self, lines: list[str], plans: list[SpanLoopPlan]) -> list[str]
```

Observed calls (lexical order): `list`, `sorted`, `self._rewrite_condition`, `self._ensure_close`.

Control points:

- L51: `if not plans`
- L57: `for plan in sorted(plans, key=lambda item: item.loop.end_index, reverse=True)`

### `SpanLoopRewriter._rewrite_condition` - L68-L104

```python
_rewrite_condition(self, lines: list[str], plan: SpanLoopPlan) -> list[str]
```

Observed calls (lexical order): `len`, `self.line_formatter.logical`, `UNTIL_LINE_PATTERN.match`, `template.format`, `logical.upper`, `logical.upper().partition`, `logical[:len(head)].rstrip`, `UNTIL_TEMPLATE.format`, `self.line_formatter.format_like_line`, `self._log`.

Control points:

- L74: `if loop is None or not loop.condition_is_legacy`
- L78: `if not 0 <= index < len(lines)`
- L83: `if UNTIL_LINE_PATTERN.match(logical)`
- L96: `if loop.terminated`

### `SpanLoopRewriter._ensure_close` - L107-L130

```python
_ensure_close(self, lines: list[str], plan: SpanLoopPlan) -> list[str]
```

Observed calls (lexical order): `self._close_already_performed`, `self._log`, `len`, `self.line_formatter.format_like_line`, `PERFORM_CLOSE_TEMPLATE.format`, `lines.insert`.

Control points:

- L112: `if self._close_already_performed(lines, plan)`
- L117: `if insert_at > len(lines)`

### `SpanLoopRewriter._close_already_performed` - L132-L156

```python
_close_already_performed(self, lines: list[str], plan: SpanLoopPlan) -> bool
```

Observed calls (lexical order): `plan.close_paragraph.upper`, `max`, `len`, `min`, `range`, `self.line_formatter.logical`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `match.group`, `match.group('operation').upper`, `int`, `match.group('cursor').upper`.

Control points:

- L142: `for index in range(start, end)`
- L145: `if not match`
- L147: `if match.group('operation').upper() != 'CLOSE'`
- L153: `if name == wanted`

### `SpanLoopRewriter._log` - L159-L162

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `CURSOR_LOOP_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L161: `if template`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
