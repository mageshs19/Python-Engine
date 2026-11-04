# `converter/composers/cleanup/residual_idms_comment_cleanup.py`

Source: [converter/composers/cleanup/residual_idms_comment_cleanup.py](../../../../../converter/composers/cleanup/residual_idms_comment_cleanup.py) | 178 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `a4a2f728763c3b089342525248aaced07e2ca041d24a5522225de04c307e8ae5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Residual IDMS comment cleanup.

## Import declarations

```python
from __future__ import annotations
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from patterns.cobol_cleanup_patterns import BLOCK_OPENER_PATTERN, LONE_CONTINUE_PATTERN, RESIDUAL_IDMS_COMMENT_CONTINUATION_PATTERN, RESIDUAL_IDMS_COMMENT_PATTERN
from patterns.cobol_cleanup_patterns import BLOCK_OPENER_PATTERN, LONE_CONTINUE_PATTERN, REMOVED_OBTAIN_CALC_COMMENT_PATTERN, RESIDUAL_IDMS_COMMENT_CONTINUATION_PATTERN, RESIDUAL_IDMS_COMMENT_PATTERN
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)

## Symbol contracts and control points

### `ResidualIdmsCommentCleanup` - L46-L178

```python
class ResidualIdmsCommentCleanup()
```

### `ResidualIdmsCommentCleanup.__init__` - L47-L53

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `ResidualIdmsCommentCleanup._logical` - L55-L56

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `ResidualIdmsCommentCleanup.remove_residual_idms_comments` - L58-L87

```python
remove_residual_idms_comments(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `len`, `self._logical`, `RESIDUAL_IDMS_COMMENT_PATTERN.match`, `REMOVED_OBTAIN_CALC_COMMENT_PATTERN.match`, `self._skip_comment_group`, `self._maybe_skip_redundant_continue`, `output.append`, `self.messages.add`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L64: `while index < len(lines)`
- L68: `if RESIDUAL_IDMS_COMMENT_PATTERN.match(logical) or REMOVED_OBTAIN_CALC_COMMENT_PATTERN.match(logical)`
- L84: `if removed_comment`

### `ResidualIdmsCommentCleanup._skip_comment_group` - L89-L111

```python
_skip_comment_group(self, lines: list[str], index: int) -> int
```

Skip the residual DB2 comment line plus any immediate continuation or related DB2 comment lines (residual, OBTAIN CALC removal, or wrapped).

Observed calls (lexical order): `len`, `self._logical`, `RESIDUAL_IDMS_COMMENT_PATTERN.match`, `REMOVED_OBTAIN_CALC_COMMENT_PATTERN.match`, `RESIDUAL_IDMS_COMMENT_CONTINUATION_PATTERN.match`.

Control points:

- L99: `while index < len(lines)`
- L101: `if RESIDUAL_IDMS_COMMENT_PATTERN.match(logical)`
- L104: `if REMOVED_OBTAIN_CALC_COMMENT_PATTERN.match(logical)`
- L107: `if RESIDUAL_IDMS_COMMENT_CONTINUATION_PATTERN.match(logical)`

### `ResidualIdmsCommentCleanup._maybe_skip_redundant_continue` - L113-L154

```python
_maybe_skip_redundant_continue(self, lines: list[str], index: int, output: list[str]) -> int
```

If the next executable line is a lone CONTINUE., remove it only when it is safe: it must NOT be the sole statement of an IF/ELSE/WHEN/ EVALUATE branch, and another executable statement (or END-IF/END- EVALUATE/period) must not depend on it.

Observed calls (lexical order): `len`, `self._logical`, `LONE_CONTINUE_PATTERN.match`, `self._previous_is_block_opener`, `self._next_executable_logical`, `next_logical.upper`, `next_upper.startswith`, `self.messages.add`.

Control points:

- L125: `if index >= len(lines)`
- L129: `if not LONE_CONTINUE_PATTERN.match(logical)`
- L149: `if prev_opener and closes_block`

### `ResidualIdmsCommentCleanup._previous_is_block_opener` - L156-L164

```python
_previous_is_block_opener(self, output: list[str]) -> bool
```

Observed calls (lexical order): `reversed`, `self._logical`, `logical.startswith`, `BLOCK_OPENER_PATTERN.match`, `bool`.

Control points:

- L157: `for line in reversed(output)`
- L159: `if not logical`
- L161: `if logical.startswith('*')`

### `ResidualIdmsCommentCleanup._next_executable_logical` - L166-L178

```python
_next_executable_logical(self, lines: list[str], start_index: int) -> str
```

Observed calls (lexical order): `len`, `range`, `self._logical`, `logical.startswith`.

Control points:

- L171: `for index in range(start_index, len(lines))`
- L173: `if not logical`
- L175: `if logical.startswith('*')`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
