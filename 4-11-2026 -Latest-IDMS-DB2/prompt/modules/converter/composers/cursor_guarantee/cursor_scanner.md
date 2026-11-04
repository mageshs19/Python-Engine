# `converter/composers/cursor_guarantee/cursor_scanner.py`

Source: [converter/composers/cursor_guarantee/cursor_scanner.py](../../../../../converter/composers/cursor_guarantee/cursor_scanner.py) | 237 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `3f7ac7f514ac9485a9f9d86795073a5fab2d3ce16bc1c957fd1427df9ff8093d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Read-only discovery over generated COBOL.

## Module-level bindings

`__all__` (L237)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_guarantee.cursor_lines import CursorLines
from converter.composers.cursor_guarantee.cursor_models import CURSOR_PARAGRAPH_HEADER_PATTERN, PARAGRAPH_NAME_TEMPLATE, PERFORM_CURSOR_PARAGRAPH_PATTERN, PERFORM_INLINE_WITH_UNTIL_PATTERN, PERFORM_PARAGRAPH_PATTERN, PERFORM_SPAN_PATTERN, PERFORM_SPAN_WITH_UNTIL_PATTERN, UNTIL_ONLY_PATTERN, CursorParagraphSet, CursorPerform, LoopShape
from rules.cursor_close_guarantee_rules import STATEMENT_TERMINATOR, UNTIL_LOOKAHEAD_LIMIT
```

## Local dependency notes

- [converter/composers/cursor_guarantee/cursor_lines.py](cursor_lines.md)
- [converter/composers/cursor_guarantee/cursor_models.py](cursor_models.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee_composer.py](../cursor_close_guarantee_composer.md)
- [converter/composers/cursor_guarantee/__init__.py](__init__.md)

## Symbol contracts and control points

### `CursorScanner` - L33-L234

```python
class CursorScanner()
```

Everything this pass needs to KNOW before it changes anything.

### `CursorScanner.__init__` - L36-L37

```python
__init__(self, lines_utils: CursorLines | None=None) -> None
```

Observed calls (lexical order): `CursorLines`.

### `CursorScanner.paragraph_sets` - L42-L72

```python
paragraph_sets(self, lines: list[str]) -> dict
```

Map every cursor to its OPEN / FETCH / CLOSE paragraph names.

Observed calls (lexical order): `self.lines_utils.logical`, `self.lines_utils.is_comment`, `CURSOR_PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `match.group('operation').upper`, `PARAGRAPH_NAME_TEMPLATE.format`, `int`, `found.setdefault`, `CursorParagraphSet`, `entry.names.setdefault`.

Control points:

- L46: `for line in lines`
- L49: `if not logical or self.lines_utils.is_comment(logical)`
- L54: `if not match`

### `CursorScanner.performs` - L77-L118

```python
performs(self, lines: list[str], cursor: str) -> list[CursorPerform]
```

Every PERFORM of a generated paragraph of ONE cursor.

Observed calls (lexical order): `str`, `str(cursor or '').upper`, `enumerate`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `match.group('operation').upper`, `output.append`, `CursorPerform`, `PARAGRAPH_NAME_TEMPLATE.format`, `int`, `str(match.group('tail') or '').strip`.

Control points:

- L86: `if not target`
- L89: `for (index, line) in enumerate(lines)`
- L92: `if not logical or self.lines_utils.is_comment(logical)`
- L97: `if not match`
- L100: `if match.group('cursor').upper() != target`

### `CursorScanner.by_operation` - L121-L125

```python
by_operation(performs: list[CursorPerform], operation: str) -> list[CursorPerform]
```

### `CursorScanner.find_business_loop` - L130-L159

```python
find_business_loop(self, lines: list[str], business: str) -> LoopShape | None
```

The loop that drives the business paragraph, if any.

Observed calls (lexical order): `str`, `str(business or '').upper`, `enumerate`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `self._one_line_loop`, `self._two_line_loop`.

Control points:

- L138: `if not target`
- L141: `for (index, line) in enumerate(lines)`
- L144: `if not logical or self.lines_utils.is_comment(logical)`
- L148: `if PERFORM_CURSOR_PARAGRAPH_PATTERN.match(logical)`
- L152: `if shape is not None`
- L156: `if shape is not None`

### `CursorScanner._one_line_loop` - L161-L185

```python
_one_line_loop(self, logical: str, index: int, target: str) -> LoopShape | None
```

PERFORM ... \[THRU ...\] UNTIL <condition> on a single line.

Observed calls (lexical order): `pattern.match`, `match.group`, `match.group('paragraph').upper`, `LoopShape`, `match.group('condition').strip`, `logical.rstrip`, `logical.rstrip().endswith`.

Control points:

- L168: `for pattern in (PERFORM_SPAN_WITH_UNTIL_PATTERN, PERFORM_INLINE_WITH_UNTIL_PATTERN)`
- L174: `if not match or match.group('paragraph').upper() != target`

### `CursorScanner._two_line_loop` - L187-L203

```python
_two_line_loop(self, lines: list[str], logical: str, index: int, target: str) -> LoopShape | None
```

PERFORM whose UNTIL clause sits on a continuation line.

Observed calls (lexical order): `pattern.match`, `match.group`, `match.group('paragraph').upper`, `self._until_on_following_line`.

Control points:

- L195: `for pattern in (PERFORM_SPAN_PATTERN, PERFORM_PARAGRAPH_PATTERN)`
- L198: `if not match or match.group('paragraph').upper() != target`

### `CursorScanner._until_on_following_line` - L205-L234

```python
_until_on_following_line(self, lines: list[str], perform_index: int) -> LoopShape | None
```

Observed calls (lexical order): `len`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `UNTIL_ONLY_PATTERN.match`, `LoopShape`, `match.group`, `match.group('condition').strip`, `logical.rstrip`, `logical.rstrip().endswith`.

Control points:

- L213: `while index < len(lines) and scanned < UNTIL_LOOKAHEAD_LIMIT`
- L216: `if not logical or self.lines_utils.is_comment(logical)`
- L223: `if match`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
