# `converter/postprocess/final_cleanup/final_cleanup_line_utils.py`

Source: [converter/postprocess/final_cleanup/final_cleanup_line_utils.py](../../../../../converter/postprocess/final_cleanup/final_cleanup_line_utils.py) | 123 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `755b02ae7c8cb720a4ea45373dabc0c46882c86cfdd287f3f84b13edbdf083a8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.update_final_cleanup_patterns import PARAGRAPH_HEADER_PATTERN
from rules.update_cobol_final_cleanup_rules import FINAL_CLEANUP_BODY_END, FINAL_CLEANUP_BODY_START, FINAL_CLEANUP_BODY_WIDTH, FINAL_CLEANUP_COMMENT_CHARS, FINAL_CLEANUP_COMMENT_INDICATORS, FINAL_CLEANUP_DEBUG_PREFIX, FINAL_CLEANUP_FULL_WIDTH, FINAL_CLEANUP_INDICATOR_COLUMN, FINAL_CLEANUP_RIGHT_SEQUENCE_WIDTH, FINAL_CLEANUP_SEQUENCE_WIDTH, FINAL_CLEANUP_TOTAL_WIDTH
```

## Local dependency notes

- [patterns/update_final_cleanup_patterns.py](../../../patterns/update_final_cleanup_patterns.md)
- [rules/update_cobol_final_cleanup_rules.py](../../../rules/update_cobol_final_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_final_cleanup.py](../update_final_cleanup.md)

## Symbol contracts and control points

### `FinalCleanupLineUtils` - L19-L123

```python
class FinalCleanupLineUtils()
```

Fixed-format line helpers + paragraph range detection.

### `FinalCleanupLineUtils._replace_body` - L26-L51

```python
_replace_body(self, line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(body or '')[:FINAL_CLEANUP_BODY_WIDTH].ljust`, `len`, `text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip`, `text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit`, `clean_body.rstrip`.

Control points:

- L32: `if len(text) >= FINAL_CLEANUP_FULL_WIDTH and text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit()`
- L44: `if len(text) > FINAL_CLEANUP_SEQUENCE_WIDTH and text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit()`

### `FinalCleanupLineUtils._body` - L53-L78

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip`, `text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit`, `text[FINAL_CLEANUP_BODY_START:FINAL_CLEANUP_BODY_END].rstrip`, `body[-FINAL_CLEANUP_RIGHT_SEQUENCE_WIDTH:].strip`, `body[-FINAL_CLEANUP_RIGHT_SEQUENCE_WIDTH:].strip().isdigit`, `body.rstrip`, `text.rstrip`.

Control points:

- L56: `if len(text) >= FINAL_CLEANUP_FULL_WIDTH and text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit()`
- L62: `if len(text) > FINAL_CLEANUP_SEQUENCE_WIDTH and text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit()`
- L71: `if len(body) >= FINAL_CLEANUP_RIGHT_SEQUENCE_WIDTH and body[-FINAL_CLEANUP_RIGHT_SEQUENCE_WIDTH:].strip().isdigit()`

### `FinalCleanupLineUtils._logical` - L80-L81

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self._body`, `self._body(line).strip`.

### `FinalCleanupLineUtils._is_comment_or_debug` - L83-L98

```python
_is_comment_or_debug(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip`, `text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit`, `text.strip`, `any`, `stripped.startswith`, `stripped.upper`, `stripped.upper().startswith`.

Control points:

- L85: `if len(text) >= FINAL_CLEANUP_INDICATOR_COLUMN and text[:FINAL_CLEANUP_SEQUENCE_WIDTH].strip().isdigit()`

### `FinalCleanupLineUtils._paragraph_ranges` - L100-L114

```python
_paragraph_ranges(self, lines: list[str]) -> list[tuple[int, int]]
```

Observed calls (lexical order): `enumerate`, `PARAGRAPH_HEADER_PATTERN.match`, `self._logical`, `output.append`, `len`.

Control points:

- L104: `for (index, line) in enumerate(lines)`
- L105: `if not PARAGRAPH_HEADER_PATTERN.match(self._logical(line))`
- L107: `if current_start >= 0`
- L111: `if current_start >= 0`

### `FinalCleanupLineUtils._paragraph_end_index` - L116-L123

```python
_paragraph_end_index(self, lines: list[str], start: int) -> int
```

Observed calls (lexical order): `len`, `self._logical`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L118: `while index < len(lines)`
- L120: `if index > start + 1 and PARAGRAPH_HEADER_PATTERN.match(logical)`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
