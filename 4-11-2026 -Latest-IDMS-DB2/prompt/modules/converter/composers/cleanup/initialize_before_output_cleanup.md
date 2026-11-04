# `converter/composers/cleanup/initialize_before_output_cleanup.py`

Source: [converter/composers/cleanup/initialize_before_output_cleanup.py](../../../../../converter/composers/cleanup/initialize_before_output_cleanup.py) | 288 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `217478a8e8df89e1bfaedaefe01775a03ec313528fe5a4e637e79264dcf70b50`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Initialize-before-output cleanup.

## Module-level bindings

`NOT_FOUND` (L59)

## Import declarations

```python
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.services.name_normalizer import NameNormalizer
from patterns.cobol_cleanup_patterns import INITIALIZE_PATTERN, MOVE_TO_OUTPUT_FIELD_PATTERN, WRITE_PATTERN
from rules.cobol_cleanup_rules import INITIALIZE_LOOKBACK_WINDOW, OUTPUT_MOVE_SCAN_WINDOW, STATEMENT_CONTINUATION_TOKENS
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)
- [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [converter/composers/late_db2_date_composer.py](../late_db2_date_composer.md)

## Symbol contracts and control points

### `InitializeBeforeOutputCleanup` - L62-L288

```python
class InitializeBeforeOutputCleanup()
```

### `InitializeBeforeOutputCleanup.__init__` - L63-L69

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `InitializeBeforeOutputCleanup._logical` - L74-L75

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `InitializeBeforeOutputCleanup._leading_spaces` - L77-L78

```python
_leading_spaces(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.leading_spaces`.

### `InitializeBeforeOutputCleanup._is_comment_or_blank` - L80-L81

```python
_is_comment_or_blank(self, logical: str) -> bool
```

Observed calls (lexical order): `self.line_utils.is_comment_or_blank`.

### `InitializeBeforeOutputCleanup.ensure_initialize_before_output_population` - L86-L129

```python
ensure_initialize_before_output_population(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `list`, `self._output_write_blocks`, `reversed`, `int`, `str`, `self._remove_initialize_for_record_in_range`, `self._has_initialize_immediately_before`, `self._leading_spaces`, `output.insert`, `self.messages.add`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L93: `for block in reversed(write_blocks)`
- L98: `if write_index < 0 or first_move_index < 0`
- L110: `if removed_count`
- L114: `if self._has_initialize_immediately_before(lines=output, index=first_move_index, record=record)`
- L126: `if changed`

### `InitializeBeforeOutputCleanup._output_write_blocks` - L134-L163

```python
_output_write_blocks(self, lines: list[str]) -> list[dict[str, object]]
```

Observed calls (lexical order): `enumerate`, `self._logical`, `WRITE_PATTERN.match`, `match.group`, `self._first_output_move_block_start_before_write`, `output.append`.

Control points:

- L140: `for (index, line) in enumerate(lines)`
- L144: `if not match`

### `InitializeBeforeOutputCleanup._first_output_move_block_start_before_write` - L165-L186

```python
_first_output_move_block_start_before_write(self, lines: list[str], write_index: int) -> int
```

First PHYSICAL line of the first statement targeting output.

Observed calls (lexical order): `max`, `self._logical_statements`, `MOVE_TO_OUTPUT_FIELD_PATTERN.match`.

Control points:

- L178: `for (statement, first_index) in self._logical_statements(lines=lines, start=start, end=write_index)`
- L183: `if MOVE_TO_OUTPUT_FIELD_PATTERN.match(statement)`

### `InitializeBeforeOutputCleanup._logical_statements` - L191-L221

```python
_logical_statements(self, lines: list[str], start: int, end: int)
```

Yield (statement_text, first_physical_index) in source order.

Observed calls (lexical order): `len`, `max`, `min`, `range`, `self._logical`, `self._is_comment_or_blank`, `f'{buffer} {logical}'.strip`, `self._is_complete`.

Control points:

- L205: `for index in range(max(0, start), min(end, len(lines)))`
- L208: `if not logical or self._is_comment_or_blank(logical)`
- L211: `if first < 0`
- L216: `if self._is_complete(buffer)`
- L220: `if first >= 0 and buffer`

### `InitializeBeforeOutputCleanup._is_complete` - L224-L239

```python
_is_complete(buffer: str) -> bool
```

False while the statement ends on a continuation token.

Observed calls (lexical order): `str`, `str(buffer or '').rstrip`, `text.endswith`, `text.split`, `text.split()[-1].upper`, `text.split()[-1].upper().rstrip`.

Control points:

- L232: `if not text`
- L235: `if text.endswith(',')`

### `InitializeBeforeOutputCleanup._remove_initialize_for_record_in_range` - L244-L268

```python
_remove_initialize_for_record_in_range(self, lines: list[str], record: str, start_index: int, end_index: int) -> tuple[list[str], int]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `enumerate`, `INITIALIZE_PATTERN.match`, `self._logical`, `match.group`, `output.append`.

Control points:

- L255: `for (index, line) in enumerate(lines)`
- L256: `if start_index <= index < end_index`
- L259: `if match`
- L262: `if current == target_record`

### `InitializeBeforeOutputCleanup._has_initialize_immediately_before` - L270-L288

```python
_has_initialize_immediately_before(self, lines: list[str], index: int, record: str) -> bool
```

Observed calls (lexical order): `max`, `NameNormalizer.normalize`, `range`, `INITIALIZE_PATTERN.match`, `self._logical`, `match.group`.

Control points:

- L279: `for prior_index in range(lookback_start, index)`
- L282: `if not match`
- L285: `if NameNormalizer.normalize(match.group('record')) == target_record`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
