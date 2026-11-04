# `converter/composers/cleanup/output_write_placement_cleanup.py`

Source: [converter/composers/cleanup/output_write_placement_cleanup.py](../../../../../converter/composers/cleanup/output_write_placement_cleanup.py) | 632 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `859e0eae37fb5c32908f9f9cbaa6117529f8556c984c3f1e2441e09aa45da9b8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Output write placement cleanup.

## Module-level bindings

`NOT_FOUND` (L91), `__all__` (L632)

## Import declarations

```python
import re
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.composers.cleanup.cursor_nesting_analyser import CursorNestingAnalyser
from patterns.cobol_cleanup_patterns import END_IF_PATTERN, FETCH_PARAGRAPH_NUMBER_PATTERN, IF_START_PATTERN, PARAGRAPH_HEADER_PATTERN, PERFORM_CLOSE_CURSOR_PATTERN, PERFORM_CURSOR_PARAGRAPH_PATTERN, PERFORM_PARAGRAPH_PATTERN, WHEN_ZERO_PATTERN, WRITE_STATEMENT_PATTERN
from rules.cobol_cleanup_rules import EARLY_STOP_GUARD_CLOSE, EARLY_STOP_GUARD_OPEN, EARLY_STOP_VALUE, ENFORCE_OUTPUT_WRITE_AFTER_CHILD_LOOP, FETCH_PARAGRAPH_CURSOR_SEPARATOR, NESTED_INDENT_STEP, NON_PARAGRAPH_SINGLE_WORDS, OUTPUT_WRITE_MOVE_PASS_LIMIT, WHEN_ZERO_PERFORM_SCAN_LIMIT
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [converter/composers/cleanup/cursor_nesting_analyser.py](cursor_nesting_analyser.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)
- [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [tests/test_output_write_placement_cleanup.py](../../../tests/test_output_write_placement_cleanup.md)

## Symbol contracts and control points

### `OutputWritePlacementCleanup` - L94-L629

```python
class OutputWritePlacementCleanup()
```

Moves a guarded output write out of a child-row paragraph.

### `OutputWritePlacementCleanup.__init__` - L97-L109

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`, `CursorNestingAnalyser`, `set`.

### `OutputWritePlacementCleanup._logical` - L111-L112

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `OutputWritePlacementCleanup._leading_spaces` - L114-L115

```python
_leading_spaces(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.leading_spaces`.

### `OutputWritePlacementCleanup._is_comment_or_blank` - L117-L118

```python
_is_comment_or_blank(self, logical: str) -> bool
```

Observed calls (lexical order): `self.line_utils.is_comment_or_blank`.

### `OutputWritePlacementCleanup.move_output_write_after_child_loop` - L123-L142

```python
move_output_write_after_child_loop(self, text: str) -> str
```

Relocate every misplaced guarded output write block.

Observed calls (lexical order): `set`, `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `range`, `self._move_one_block`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L127: `if not text or not ENFORCE_OUTPUT_WRITE_AFTER_CHILD_LOOP`
- L137: `for _pass in range(OUTPUT_WRITE_MOVE_PASS_LIMIT)`
- L139: `if not moved`

### `OutputWritePlacementCleanup._move_one_block` - L147-L225

```python
_move_one_block(self, lines: list[str]) -> bool
```

Move at most one block. Returns True when the list was changed.

Observed calls (lexical order): `self._paragraph_spans`, `spans.items`, `self._is_child_fetch`, `self._row_paragraph`, `self._report_once`, `self._contains_cursor_lifecycle`, `self._cursor_of`, `self._close_perform_index`, `self._trailing_write_block`, `self._index_in_span`, `self._relocate`, `self.messages.add`, `self._owner_paragraph`.

Control points:

- L150: `if not spans`
- L153: `for (fetch_paragraph, fetch_span) in spans.items()`
- L154: `if not self._is_child_fetch(lines, fetch_paragraph)`
- L158: `if not row_paragraph or row_paragraph not in spans`
- L178: `if self._contains_cursor_lifecycle(lines, spans[row_paragraph])`
- L182: `if not cursor`
- L190: `if close_index < 0`
- L198: `if not block`
- Another 1 conditions/loops exist in this source span.

### `OutputWritePlacementCleanup._relocate` - L227-L249

```python
_relocate(self, lines: list[str], start: int, end: int, close_index: int) -> None
```

Observed calls (lexical order): `self._leading_spaces`, `self._uses_early_stop`, `self._render`.

### `OutputWritePlacementCleanup._render` - L254-L279

```python
_render(self, block: list[str], base_indent: str, guarded: str | None) -> list[str]
```

Re-indent the block and guard it with the discovered business flag.

Observed calls (lexical order): `self._shift_indent`, `EARLY_STOP_GUARD_OPEN.format`.

Control points:

- L266: `if not guarded`

### `OutputWritePlacementCleanup._shift_indent` - L281-L305

```python
_shift_indent(self, block: list[str], target_indent: str) -> list[str]
```

Re-indent a block, preserving its internal nesting.

Observed calls (lexical order): `self._minimum_indent`, `self._logical`, `output.append`, `self._body_of`, `self._leading_spaces`, `len`.

Control points:

- L290: `for line in block`
- L293: `if not logical`

### `OutputWritePlacementCleanup._minimum_indent` - L307-L319

```python
_minimum_indent(self, block: list[str]) -> str
```

The shallowest indent in the block. Nesting is measured from it.

Observed calls (lexical order): `self._logical`, `self._body_of`, `self._leading_spaces`, `len`.

Control points:

- L311: `for line in block`
- L313: `if not logical`
- L316: `if narrowest is None or len(indent) < len(narrowest)`

### `OutputWritePlacementCleanup._body_of` - L321-L343

```python
_body_of(self, line: str) -> str
```

The logical body with its own indentation, sequence area removed.

Observed calls (lexical order): `self._logical`, `str`, `str(line or '').rstrip`, `text.rfind`, `text[:position].replace`, `len`, `prefix.rstrip`.

Control points:

- L331: `if not logical`
- L337: `if position <= 0`

### `OutputWritePlacementCleanup._paragraph_spans` - L348-L372

```python
_paragraph_spans(self, lines: list[str]) -> dict[str, tuple[int, int]]
```

Paragraph name -> (first line index, last line index).

Observed calls (lexical order): `enumerate`, `self._logical`, `self._is_comment_or_blank`, `self._is_paragraph_header`, `logical.rstrip`, `logical.rstrip('.').upper`, `len`.

Control points:

- L354: `for (index, line) in enumerate(lines)`
- L357: `if self._is_comment_or_blank(logical)`
- L360: `if not self._is_paragraph_header(logical)`
- L363: `if current`
- L369: `if current and start >= 0`

### `OutputWritePlacementCleanup._is_paragraph_header` - L374-L384

```python
_is_paragraph_header(self, logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `text.endswith`, `PARAGRAPH_HEADER_PATTERN.match`, `text.rstrip`, `text.rstrip('.').upper`, `bool`.

Control points:

- L377: `if not text.endswith('.')`
- L380: `if not PARAGRAPH_HEADER_PATTERN.match(text)`

### `OutputWritePlacementCleanup._owner_paragraph` - L386-L394

```python
_owner_paragraph(self, spans: dict[str, tuple[int, int]], index: int) -> str
```

Observed calls (lexical order): `spans.items`, `self._index_in_span`.

Control points:

- L391: `for (name, span) in spans.items()`
- L392: `if self._index_in_span(index, span)`

### `OutputWritePlacementCleanup._index_in_span` - L397-L399

```python
_index_in_span(index: int, span: tuple[int, int]) -> bool
```

### `OutputWritePlacementCleanup._is_child_fetch` - L404-L410

```python
_is_child_fetch(self, lines: list[str], paragraph: str) -> bool
```

Classify nesting from PERFORM relationships, never numbering.

Observed calls (lexical order): `FETCH_PARAGRAPH_NUMBER_PATTERN.match`, `str`, `str(paragraph or '').upper`, `self.cursor_nesting.is_nested_fetch`.

Control points:

- L406: `if not FETCH_PARAGRAPH_NUMBER_PATTERN.match(str(paragraph or '').upper())`

### `OutputWritePlacementCleanup._cursor_of` - L413-L420

```python
_cursor_of(paragraph: str) -> str
```

Observed calls (lexical order): `str`, `str(paragraph or '').upper`, `text.split`, `text.split(separator, 1)[1].strip`.

Control points:

- L417: `if separator not in text`

### `OutputWritePlacementCleanup._contains_cursor_lifecycle` - L422-L442

```python
_contains_cursor_lifecycle(self, lines: list[str], span: tuple[int, int]) -> bool
```

Whether a candidate business paragraph owns a nested cursor.

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `self._is_comment_or_blank`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`.

Control points:

- L436: `for index in range(start + 1, min(end + 1, len(lines)))`
- L438: `if self._is_comment_or_blank(logical)`
- L440: `if PERFORM_CURSOR_PARAGRAPH_PATTERN.match(logical)`

### `OutputWritePlacementCleanup._row_paragraph` - L444-L479

```python
_row_paragraph(self, lines: list[str], fetch_span: tuple[int, int]) -> str
```

The business paragraph performed under WHEN ZERO of a FETCH.

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `self._is_comment_or_blank`, `WHEN_ZERO_PATTERN.match`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `PERFORM_PARAGRAPH_PATTERN.match`, `match.group`, `match.group('paragraph').upper`.

Control points:

- L454: `for index in range(start + 1, min(end + 1, len(lines)))`
- L457: `if self._is_comment_or_blank(logical)`
- L460: `if WHEN_ZERO_PATTERN.match(logical)`
- L465: `if not seen_when_zero`
- L469: `if scanned > WHEN_ZERO_PERFORM_SCAN_LIMIT`
- L472: `if PERFORM_CURSOR_PARAGRAPH_PATTERN.match(logical)`
- L476: `if match`

### `OutputWritePlacementCleanup._close_perform_index` - L481-L504

```python
_close_perform_index(self, lines: list[str], spans: dict[str, tuple[int, int]], cursor: str) -> int
```

Index of PERFORM <nnn>-CLOSE-<cursor> in a non-cursor paragraph.

Observed calls (lexical order): `enumerate`, `self._logical`, `PERFORM_CLOSE_CURSOR_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `self._owner_paragraph`, `self._is_generated_cursor_paragraph`.

Control points:

- L488: `for (index, line) in enumerate(lines)`
- L492: `if not match`
- L495: `if match.group('cursor').upper() != cursor`
- L499: `if self._is_generated_cursor_paragraph(owner)`

### `OutputWritePlacementCleanup._is_generated_cursor_paragraph` - L506-L509

```python
_is_generated_cursor_paragraph(self, paragraph: str) -> bool
```

Observed calls (lexical order): `bool`, `FETCH_PARAGRAPH_NUMBER_PATTERN.match`, `str`, `str(paragraph or '').upper`.

### `OutputWritePlacementCleanup._uses_early_stop` - L511-L533

```python
_uses_early_stop(self, lines: list[str], close_index: int) -> str | None
```

Return the flag used by this child loop, inferred from its condition.

Observed calls (lexical order): `range`, `self._logical`, `self._logical(lines[index]).strip`, `self._is_comment_or_blank`, `re.search`, `match.group`, `match.group('flag').upper`, `self._is_paragraph_header`.

Control points:

- L513: `for index in range(close_index - 1, -1, -1)`
- L515: `if self._is_comment_or_blank(logical)`
- L525: `if match`
- L527: `if index > 0 and re.search('\\bOR\\s*$', self._logical(lines[index - 1]), re.I)`
- L529: `if re.search('\\bUNTIL\\b.*\\bOR\\b', logical, re.I)`
- L531: `if self._is_paragraph_header(logical)`

### `OutputWritePlacementCleanup._trailing_write_block` - L538-L571

```python
_trailing_write_block(self, lines: list[str], span: tuple[int, int]) -> tuple[int, int] | None
```

The last IF ... WRITE ... END-IF construct of a paragraph.

Observed calls (lexical order): `self._last_code_index`, `END_IF_PATTERN.match`, `self._logical`, `self._matching_if_index`, `any`, `WRITE_STATEMENT_PATTERN.match`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`.

Control points:

- L547: `if last < 0`
- L550: `if not END_IF_PATTERN.match(self._logical(lines[last]))`
- L554: `if opener < 0`
- L559: `if not any((WRITE_STATEMENT_PATTERN.match(self._logical(line)) for line in block))`
- L565: `if any((PERFORM_CURSOR_PARAGRAPH_PATTERN.match(self._logical(line)) for line in block))`

### `OutputWritePlacementCleanup._last_code_index` - L573-L584

```python
_last_code_index(self, lines: list[str], start: int, end: int) -> int
```

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `self._is_comment_or_blank`.

Control points:

- L579: `for index in range(min(end, len(lines) - 1), start, -1)`
- L581: `if self._is_comment_or_blank(logical)`

### `OutputWritePlacementCleanup._matching_if_index` - L586-L610

```python
_matching_if_index(self, lines: list[str], start: int, end_if_index: int) -> int
```

Walk back from an END-IF to its own IF, honouring nesting.

Observed calls (lexical order): `range`, `self._logical`, `self._is_comment_or_blank`, `END_IF_PATTERN.match`, `IF_START_PATTERN.match`.

Control points:

- L595: `for index in range(end_if_index, start, -1)`
- L598: `if self._is_comment_or_blank(logical)`
- L601: `if END_IF_PATTERN.match(logical)`
- L605: `if IF_START_PATTERN.match(logical)`
- L607: `if depth == 0`

### `OutputWritePlacementCleanup._report_once` - L615-L629

```python
_report_once(self, key: str, **fields: str) -> None
```

Report a refusal at most once per program.

Observed calls (lexical order): `fields.items`, `sorted`, `tuple`, `self._reported.add`, `self.messages.add`.

Control points:

- L625: `if signature in self._reported`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
