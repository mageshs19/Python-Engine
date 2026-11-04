# `converter/composers/retrieval_commit_cleanup_composer.py`

Source: [converter/composers/retrieval_commit_cleanup_composer.py](../../../../converter/composers/retrieval_commit_cleanup_composer.py) | 359 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `c9a5d673b78d996e4fd7fcd6a8379f8f0eed68f3f8f99138505ea955a036c1cb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Removes a COMMIT block from a retrieval program.

## Module-level bindings

`LEFT_SEQUENCE_WIDTH` (L90), `RIGHT_SEQUENCE_START` (L91), `RIGHT_SEQUENCE_END` (L92), `INDICATOR_AND_BODY_WIDTH` (L94), `FIXED_LINE_WIDTH` (L95), `RIGHT_SEQUENCE_DIGIT_FLOOR` (L99), `COMMENT_INDICATORS` (L101), `DIVISION_TOKEN` (L102), `SECTION_TOKEN` (L103), `STATEMENT_TERMINATOR` (L104), `WORD_SEPARATOR` (L105), `__all__` (L359)

## Import declarations

```python
from __future__ import annotations
from patterns.sequence_patterns import strip_sequence_numbers
from rules.retrieval_commit_cleanup_rules import BLOCK_SCAN_LIMIT, COMMIT_LOCATION_TOKEN, COMMIT_REMOVED_COMMENT, COMMIT_SQL_TOKEN, CONTINUE_INDENT, CONTINUE_INDICATOR, CONTINUE_STATEMENT, EMPTINESS_SCAN_LIMIT, END_EXEC_TOKEN, ENFORCE_PARAGRAPH_NOT_EMPTIED, ENFORCE_RETRIEVAL_COMMIT_CLEANUP, EXEC_SQL_TOKEN, NON_PARAGRAPH_SINGLE_WORDS, RETRIEVAL_COMMIT_MESSAGES
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [rules/retrieval_commit_cleanup_rules.py](../../rules/retrieval_commit_cleanup_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_retrieval_commit_continue_guard.py](../../tests/test_retrieval_commit_continue_guard.md)

## Symbol contracts and control points

### `RetrievalCommitCleanupComposer` - L108-L356

```python
class RetrievalCommitCleanupComposer()
```

Strips COMMIT from a read-only program.

### `RetrievalCommitCleanupComposer.__init__` - L111-L113

```python
__init__(self, *, is_update_program: bool=False) -> None
```

Observed calls (lexical order): `bool`.

### `RetrievalCommitCleanupComposer.compose` - L118-L162

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self._log`, `self._split`, `len`, `self._commit_span`, `output.append`, `self._comment_like`, `self._paragraph_emptied`, `self._continue_like`, `'\n'.join`.

Control points:

- L121: `if not text or not ENFORCE_RETRIEVAL_COMMIT_CLEANUP`
- L124: `if self.is_update_program`
- L133: `while index < len(lines)`
- L136: `if span < 0`
- L147: `if ENFORCE_PARAGRAPH_NOT_EMPTIED and self._paragraph_emptied(lines, span)`
- L157: `if removed`

### `RetrievalCommitCleanupComposer._commit_span` - L167-L182

```python
_commit_span(self, lines: list[str], start: int) -> int
```

Index AFTER the COMMIT block starting at `start`, or -1.

Observed calls (lexical order): `self._logical`, `self._exec_block_end`, `body.startswith`, `self._block_is_commit`.

Control points:

- L172: `if COMMIT_SQL_TOKEN in body and COMMIT_LOCATION_TOKEN in body`
- L177: `if body.startswith(EXEC_SQL_TOKEN)`
- L179: `if end > 0 and self._block_is_commit(lines, start, end)`

### `RetrievalCommitCleanupComposer._exec_block_end` - L184-L195

```python
_exec_block_end(self, lines: list[str], start: int) -> int
```

Index AFTER END-EXEC, or -1 when the block does not close.

Observed calls (lexical order): `len`, `self._logical`, `self._logical(lines[start]).startswith`, `min`, `range`.

Control points:

- L186: `if start >= len(lines)`
- L188: `if not self._logical(lines[start]).startswith(EXEC_SQL_TOKEN)`
- L192: `for index in range(start, limit)`
- L193: `if END_EXEC_TOKEN in self._logical(lines[index])`

### `RetrievalCommitCleanupComposer._block_is_commit` - L197-L201

```python
_block_is_commit(self, lines: list[str], start: int, end: int) -> bool
```

Observed calls (lexical order): `any`, `self._logical`, `self._logical(lines[index]).startswith`, `range`.

### `RetrievalCommitCleanupComposer._paragraph_emptied` - L206-L242

```python
_paragraph_emptied(self, lines: list[str], start: int) -> bool
```

True when no executable statement follows before the next paragraph, section or division boundary.

Observed calls (lexical order): `len`, `range`, `self._logical`, `body.startswith`, `self._is_boundary`.

Control points:

- L218: `for index in range(start, len(lines))`
- L219: `if scanned >= EMPTINESS_SCAN_LIMIT`
- L227: `if not body`
- L230: `if body.startswith(COMMENT_INDICATORS)`
- L233: `if self._is_boundary(body)`

### `RetrievalCommitCleanupComposer._is_boundary` - L245-L263

```python
_is_boundary(body: str) -> bool
```

A paragraph header, section header or division boundary.

Observed calls (lexical order): `str`, `str(body or '').strip`, `str(body or '').strip().upper`, `text.endswith`, `text.rstrip`, `bool`.

Control points:

- L248: `if not text`
- L251: `if DIVISION_TOKEN in text and text.endswith(STATEMENT_TERMINATOR)`
- L254: `if text.endswith(SECTION_TOKEN)`
- L259: `if WORD_SEPARATOR not in text and text.endswith(STATEMENT_TERMINATOR)`

### `RetrievalCommitCleanupComposer._comment_like` - L268-L270

```python
_comment_like(self, line: str) -> str
```

The removal comment, carrying the sequence area of `line`.

Observed calls (lexical order): `self._render`.

### `RetrievalCommitCleanupComposer._continue_like` - L272-L281

```python
_continue_like(self, line: str) -> str
```

CONTINUE. carrying the sequence area of `line`.

Observed calls (lexical order): `self._render`.

### `RetrievalCommitCleanupComposer._render` - L284-L311

```python
_render(line: str, body: str) -> str
```

One fixed-format record carrying `body`.

Observed calls (lexical order): `str`, `len`, `text[:LEFT_SEQUENCE_WIDTH].strip`, `text[:LEFT_SEQUENCE_WIDTH].strip().isdigit`, `body[:INDICATOR_AND_BODY_WIDTH].ljust`.

Control points:

- L298: `if not is_fixed`

### `RetrievalCommitCleanupComposer._split` - L317-L324

```python
_split(text: str) -> list[str]
```

Line list, tolerant of CRLF and lone-CR line endings.

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `str(text or '').replace('\r\n', '\n').replace('\r', '\n').split`.

### `RetrievalCommitCleanupComposer._logical` - L327-L351

```python
_logical(line: str) -> str
```

Uppercased logical line, sequence areas removed.

Observed calls (lexical order): `str`, `str(strip_sequence_numbers(str(line or '')) or '').strip`, `str(strip_sequence_numbers(str(line or '')) or '').strip().upper`, `strip_sequence_numbers`, `text.rsplit`, `len`, `parts[1].isdigit`, `parts[0].rstrip`.

Control points:

- L344: `if len(parts) == 2 and parts[1].isdigit() and (len(parts[1]) >= RIGHT_SEQUENCE_DIGIT_FLOOR)`

### `RetrievalCommitCleanupComposer._log` - L353-L356

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `RETRIEVAL_COMMIT_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L355: `if template`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
