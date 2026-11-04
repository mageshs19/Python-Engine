# `converter/composers/cleanup/cursor_nesting_analyser.py`

Source: [converter/composers/cleanup/cursor_nesting_analyser.py](../../../../../converter/composers/cleanup/cursor_nesting_analyser.py) | 116 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `b1419f5f21a8cd644c5ffed4c57f8b1eb176ee5b89b5c50b54089359fb706788`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Structural parent/child cursor classification for generated COBOL.

## Module-level bindings

`__all__` (L116)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from patterns.cobol_cleanup_patterns import PARAGRAPH_HEADER_PATTERN, PERFORM_CURSOR_PARAGRAPH_PATTERN, PERFORM_PARAGRAPH_PATTERN, WHEN_ZERO_PATTERN
from rules.cobol_cleanup_rules import NON_PARAGRAPH_SINGLE_WORDS
```

## Local dependency notes

- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)
- [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/business_control_flag_analyzer.py](business_control_flag_analyzer.md)
- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/output_write_placement_cleanup.py](output_write_placement_cleanup.md)
- [tests/test_output_write_placement_cleanup.py](../../../tests/test_output_write_placement_cleanup.md)

## Symbol contracts and control points

### `CursorNestingAnalyser` - L27-L113

```python
class CursorNestingAnalyser()
```

### `CursorNestingAnalyser.__init__` - L28-L29

```python
__init__(self, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `CursorNestingAnalyser.is_nested_fetch` - L31-L86

```python
is_nested_fetch(self, lines: list[str], fetch_paragraph: str) -> bool
```

Return true only when the cursor is structurally nested in a parent row.

Observed calls (lexical order): `str`, `str(fetch_paragraph or '').strip`, `str(fetch_paragraph or '').strip().upper`, `candidate.split`, `candidate.split(marker, 1)[1].strip`, `self._paragraph_spans`, `set`, `spans.items`, `len`, `min`, `range`, `self.lines.logical`, `self.lines.logical(lines[index]).upper`, `self.lines.logical(lines[index]).upper().rstrip`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `logical.endswith`.
Another 8 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L35: `if marker not in candidate`
- L38: `if not cursor`
- L42: `if not spans`
- L49: `for (owner, (start, end)) in spans.items()`
- L50: `for index in range(start + 1, min(end + 1, len(lines)))`
- L53: `if match and logical.endswith(cursor_suffix)`
- L57: `if not owners`
- L64: `for (fetch_name, (start, end)) in spans.items()`
- Another 8 conditions/loops exist in this source span.

### `CursorNestingAnalyser.paragraph_spans` - L88-L90

```python
paragraph_spans(self, lines: list[str]) -> dict[str, tuple[int, int]]
```

Expose paragraph spans for cooperating cleanup passes.

Observed calls (lexical order): `self._paragraph_spans`.

### `CursorNestingAnalyser._paragraph_spans` - L92-L113

```python
_paragraph_spans(self, lines: list[str]) -> dict[str, tuple[int, int]]
```

Observed calls (lexical order): `enumerate`, `self.lines.logical`, `logical.startswith`, `PARAGRAPH_HEADER_PATTERN.match`, `logical.endswith`, `logical.rstrip`, `logical.rstrip('.').upper`, `len`.

Control points:

- L97: `for (index, line) in enumerate(lines)`
- L99: `if not logical or logical.startswith(('*', '/'))`
- L101: `if not logical.endswith('.') or not PARAGRAPH_HEADER_PATTERN.match(logical)`
- L104: `if name in NON_PARAGRAPH_SINGLE_WORDS`
- L106: `if current`
- L111: `if current and start >= 0`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
