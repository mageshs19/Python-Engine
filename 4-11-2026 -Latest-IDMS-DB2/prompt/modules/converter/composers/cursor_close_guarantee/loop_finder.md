# `converter/composers/cursor_close_guarantee/loop_finder.py`

Source: [converter/composers/cursor_close_guarantee/loop_finder.py](../../../../../converter/composers/cursor_close_guarantee/loop_finder.py) | 171 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `6853053b25ab76744329da795fc555dd7e0d9178c2c9486dd474a9437e271e7d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Finds the business loop that drives a given paragraph.

## Module-level bindings

`SAME_LINE_PATTERNS` (L34), `LOOKAHEAD_PATTERNS` (L39), `__all__` (L171)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.line_utils import CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.models import LoopShape
from patterns.cursor_close_guarantee_patterns import PERFORM_CURSOR_PARAGRAPH_PATTERN, PERFORM_INLINE_WITH_UNTIL_PATTERN, PERFORM_PARAGRAPH_PATTERN, PERFORM_SPAN_PATTERN, PERFORM_SPAN_WITH_UNTIL_PATTERN, UNTIL_ONLY_PATTERN
from rules.cursor_close_guarantee_rules import UNTIL_LOOKAHEAD_LIMIT
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/line_utils.py](line_utils.md)
- [converter/composers/cursor_close_guarantee/models.py](models.md)
- [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)

## Symbol contracts and control points

### `BusinessLoopFinder` - L45-L168

```python
class BusinessLoopFinder()
```

Locates the driving loop of a business paragraph, if one exists.

### `BusinessLoopFinder.__init__` - L48-L52

```python
__init__(self, line_utils: CursorGuaranteeLineUtils | None=None) -> None
```

Observed calls (lexical order): `CursorGuaranteeLineUtils`.

### `BusinessLoopFinder.find` - L57-L87

```python
find(self, lines: list[str], business: str) -> LoopShape | None
```

Observed calls (lexical order): `str`, `str(business or '').upper`, `enumerate`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `self._same_line_loop`, `self._lookahead_loop`.

Control points:

- L64: `if not target`
- L67: `for (index, line) in enumerate(lines)`
- L70: `if not logical or self.lines_utils.is_comment(logical)`
- L74: `if PERFORM_CURSOR_PARAGRAPH_PATTERN.match(logical)`
- L79: `if shape is not None`
- L84: `if shape is not None`

### `BusinessLoopFinder._same_line_loop` - L92-L116

```python
_same_line_loop(self, logical: str, index: int, target: str) -> LoopShape | None
```

PERFORM ... UNTIL <cond> all on one line.

Observed calls (lexical order): `pattern.match`, `match.group`, `match.group('paragraph').upper`, `LoopShape`, `match.group('condition').strip`, `self.lines_utils.is_terminated`.

Control points:

- L99: `for pattern in SAME_LINE_PATTERNS`
- L102: `if not match`
- L105: `if match.group('paragraph').upper() != target`

### `BusinessLoopFinder._lookahead_loop` - L118-L137

```python
_lookahead_loop(self, lines: list[str], logical: str, index: int, target: str) -> LoopShape | None
```

PERFORM ... with the UNTIL clause on a continuation line.

Observed calls (lexical order): `pattern.match`, `match.group`, `match.group('paragraph').upper`, `self._until_on_following_line`.

Control points:

- L126: `for pattern in LOOKAHEAD_PATTERNS`
- L129: `if not match`
- L132: `if match.group('paragraph').upper() != target`

### `BusinessLoopFinder._until_on_following_line` - L139-L168

```python
_until_on_following_line(self, lines: list[str], perform_index: int) -> LoopShape | None
```

Observed calls (lexical order): `len`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `UNTIL_ONLY_PATTERN.match`, `LoopShape`, `match.group`, `match.group('condition').strip`, `self.lines_utils.is_terminated`.

Control points:

- L147: `while index < len(lines) and scanned < UNTIL_LOOKAHEAD_LIMIT`
- L150: `if not logical or self.lines_utils.is_comment(logical)`
- L157: `if match`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
