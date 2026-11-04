# `converter/composers/cursor_flow/loop_shape.py`

Source: [converter/composers/cursor_flow/loop_shape.py](../../../../../converter/composers/cursor_flow/loop_shape.py) | 210 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `6e202f1401295142d7fbe2e117970951c20d30a178bcdaf4065c8f3437925a3f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Classifies every driving loop in a program, whatever the idiom.

## Module-level bindings

`UNTIL_CONTINUATION_WINDOW` (L29), `COMMENT_PREFIXES` (L30), `__all__` (L210)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from patterns.cursor_loop_patterns import PERFORM_CURSOR_PARAGRAPH_PATTERN, PERFORM_INLINE_WITH_UNTIL_PATTERN, PERFORM_SIMPLE_PATTERN, PERFORM_SPAN_PATTERN, PERFORM_SPAN_WITH_UNTIL_PATTERN, UNTIL_LINE_PATTERN
from rules.cursor_loop_rules import LEGACY_EOC_CONDITIONS, LOOP_KIND_INLINE, LOOP_KIND_SPAN
```

## Local dependency notes

- [converter/composers/cursor_flow_line_formatter.py](../cursor_flow_line_formatter.md)
- [patterns/cursor_loop_patterns.py](../../../patterns/cursor_loop_patterns.md)
- [rules/cursor_loop_rules.py](../../../rules/cursor_loop_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_flow/span_loop_plan.py](span_loop_plan.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../../tests/test_generic_cursor_numbering_and_perform_integrity.md)

## Symbol contracts and control points

### `LoopShape` - L34-L60

```python
class LoopShape()
```

One driving loop, normalised across idioms.

Declared class/data-model fields:

```python
kind: str = ''
paragraph: str = ''
through: str = ''
condition: str = ''
perform_index: int = -1
until_index: int = -1
end_index: int = -1
terminated: bool = False
```

### `LoopShape.is_span` - L47-L48

```python
is_span(self) -> bool
```

### `LoopShape.has_condition` - L51-L52

```python
has_condition(self) -> bool
```

Observed calls (lexical order): `bool`.

### `LoopShape.condition_is_legacy` - L55-L60

```python
condition_is_legacy(self) -> bool
```

Observed calls (lexical order): `self.condition.upper`, `self.condition.upper().replace`, `any`, `legacy.replace`.

### `LoopShapeScanner` - L63-L207

```python
class LoopShapeScanner()
```

Finds every driving loop, in both idioms, anywhere in the program.

### `LoopShapeScanner.__init__` - L66-L70

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `LoopShapeScanner.scan` - L73-L97

```python
scan(self, lines: list[str]) -> list[LoopShape]
```

Observed calls (lexical order): `len`, `self._logical`, `self._is_comment`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `self._shape_at`, `shapes.append`.

Control points:

- L77: `while index < len(lines)`
- L80: `if not logical or self._is_comment(logical)`
- L85: `if PERFORM_CURSOR_PARAGRAPH_PATTERN.match(logical)`
- L90: `if shape is None`

### `LoopShapeScanner.inline_loops` - L100-L101

```python
inline_loops(shapes: list[LoopShape]) -> list[LoopShape]
```

### `LoopShapeScanner.span_loops` - L104-L105

```python
span_loops(shapes: list[LoopShape]) -> list[LoopShape]
```

### `LoopShapeScanner._shape_at` - L108-L176

```python
_shape_at(self, lines: list[str], index: int, logical: str) -> LoopShape | None
```

Observed calls (lexical order): `PERFORM_SPAN_WITH_UNTIL_PATTERN.match`, `LoopShape`, `match.group`, `match.group('paragraph').upper`, `match.group('through').upper`, `match.group('condition').strip`, `logical.rstrip`, `logical.rstrip().endswith`, `PERFORM_SPAN_PATTERN.match`, `self._until_after`, `PERFORM_INLINE_WITH_UNTIL_PATTERN.match`, `PERFORM_SIMPLE_PATTERN.match`.

Control points:

- L116: `if match`
- L130: `if match`
- L147: `if match`
- L160: `if match`
- L164: `if until_index < 0`

### `LoopShapeScanner._until_after` - L178-L199

```python
_until_after(self, lines: list[str], start_index: int) -> tuple[int, str, bool]
```

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `self._is_comment`, `UNTIL_LINE_PATTERN.match`, `match.group`, `match.group('condition').strip`, `bool`.

Control points:

- L185: `for index in range(start_index, end)`
- L187: `if not logical or self._is_comment(logical)`
- L191: `if match`

### `LoopShapeScanner._logical` - L202-L203

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_formatter.logical`.

### `LoopShapeScanner._is_comment` - L206-L207

```python
_is_comment(logical: str) -> bool
```

Observed calls (lexical order): `logical.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
