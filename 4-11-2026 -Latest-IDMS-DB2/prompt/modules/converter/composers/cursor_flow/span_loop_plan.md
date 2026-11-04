# `converter/composers/cursor_flow/span_loop_plan.py`

Source: [converter/composers/cursor_flow/span_loop_plan.py](../../../../../converter/composers/cursor_flow/span_loop_plan.py) | 190 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `8aebe6a76283c86fe9862e302111e2883656abccca1b0c8c34e109d07c85d948`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Correlates a generated cursor with a SPAN driving loop.

## Module-level bindings

`LEGACY_FETCH_OFFSET` (L27), `LEGACY_CLOSE_OFFSET` (L28), `FOUR_DIGIT_FETCH_OFFSET` (L29), `FOUR_DIGIT_CLOSE_OFFSET` (L30), `__all__` (L190)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from converter.composers.cursor_flow.loop_shape import LoopShape, LoopShapeScanner
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from patterns.cursor_loop_patterns import PERFORM_CURSOR_PARAGRAPH_PATTERN
from rules.cursor_loop_rules import CURSOR_LOOP_MESSAGES, EOC_CONDITION_TEMPLATE, MAX_CORRELATION_DISTANCE
```

## Local dependency notes

- [converter/composers/cursor_flow/loop_shape.py](loop_shape.md)
- [converter/composers/cursor_flow_line_formatter.py](../cursor_flow_line_formatter.md)
- [patterns/cursor_loop_patterns.py](../../../patterns/cursor_loop_patterns.md)
- [rules/cursor_loop_rules.py](../../../rules/cursor_loop_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_flow/span_loop_rewriter.py](span_loop_rewriter.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../../tests/test_generic_cursor_numbering_and_perform_integrity.md)

## Symbol contracts and control points

### `SpanLoopPlan` - L34-L52

```python
class SpanLoopPlan()
```

A cursor whose driving loop is a paragraph span.

Declared class/data-model fields:

```python
cursor_name: str = ''
open_index: int = -1
open_number: int = 0
fetch_paragraph: str = ''
close_paragraph: str = ''
eoc_condition: str = ''
loop: LoopShape | None = None
```

### `SpanLoopPlan.is_usable` - L46-L52

```python
is_usable(self) -> bool
```

Observed calls (lexical order): `bool`.

### `SpanLoopPlanBuilder` - L55-L187

```python
class SpanLoopPlanBuilder()
```

Builds SpanLoopPlan values from scanned loop shapes.

### `SpanLoopPlanBuilder.__init__` - L58-L65

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None, scanner: LoopShapeScanner | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`, `LoopShapeScanner`.

### `SpanLoopPlanBuilder.build` - L68-L129

```python
build(self, lines: list[str], shapes: list[LoopShape], claimed_cursors: set[str] | None=None) -> list[SpanLoopPlan]
```

Plans for cursors NOT already handled by the inline strategy.

Observed calls (lexical order): `self.scanner.span_loops`, `set`, `str`, `str(name).upper`, `self._cursor_opens`, `self._nearest_loop`, `self._log`, `used_loops.add`, `SpanLoopPlan`, `EOC_CONDITION_TEMPLATE.format`, `plans.append`.

Control points:

- L78: `if not span_loops`
- L85: `for (cursor, open_index, open_number) in self._cursor_opens(lines)`
- L86: `if cursor in already`
- L90: `if loop is None`
- L118: `if not plan.is_usable`

### `SpanLoopPlanBuilder._cursor_opens` - L132-L150

```python
_cursor_opens(self, lines: list[str])
```

(cursor, index, number) for every PERFORM nnn-OPEN-<cursor>.

Observed calls (lexical order): `set`, `enumerate`, `self.line_formatter.logical`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `match.group`, `match.group('operation').upper`, `match.group('cursor').upper`, `seen.add`, `int`.

Control points:

- L136: `for (index, line) in enumerate(lines)`
- L140: `if not match`
- L142: `if match.group('operation').upper() != 'OPEN'`
- L146: `if cursor in seen`

### `SpanLoopPlanBuilder._nearest_loop` - L153-L182

```python
_nearest_loop(span_loops: list[LoopShape], open_index: int, used_loops: set[int]) -> LoopShape | None
```

Closest unused span loop, searched in BOTH directions.

Observed calls (lexical order): `abs`, `min`.

Control points:

- L167: `if not candidates`
- L173: `if MAX_CORRELATION_DISTANCE > 0`
- L179: `if not pool`

### `SpanLoopPlanBuilder._log` - L184-L187

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `CURSOR_LOOP_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L186: `if template`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
