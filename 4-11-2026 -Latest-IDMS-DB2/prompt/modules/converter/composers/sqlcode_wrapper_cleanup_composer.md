# `converter/composers/sqlcode_wrapper_cleanup_composer.py`

Source: [converter/composers/sqlcode_wrapper_cleanup_composer.py](../../../../converter/composers/sqlcode_wrapper_cleanup_composer.py) | 195 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `d88b3f2b1f6b8dcad2d42ac81a2abd60264dbb3a139d06b22710e59c5cadf024`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQLCODE wrapper cleanup composer.

## Import declarations

```python
from __future__ import annotations
from converter.composers.sqlcode_wrapper_line_utils import SqlcodeWrapperLineUtils
from rules.sqlcode_wrapper_rules import BASE_INDENT, CHILD_INDENT, CLEANUP_COMMENT_TEXT, COMMENT_PREFIXES, INNER_IF_LOOKAHEAD, INNER_IF_TEXT, MARKER_LOOKAHEAD, OUTER_IF_TEXT, REMOVED_OBTAIN_NEXT_TEXT, TOKEN_END_IF, TOKEN_IF
```

## Local dependency notes

- [converter/composers/sqlcode_wrapper_line_utils.py](sqlcode_wrapper_line_utils.md)
- [rules/sqlcode_wrapper_rules.py](../../rules/sqlcode_wrapper_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `SqlcodeWrapperCleanupComposer` - L42-L195

```python
class SqlcodeWrapperCleanupComposer(SqlcodeWrapperLineUtils)
```

### `SqlcodeWrapperCleanupComposer.compose` - L43-L71

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self._normalize_line_endings`, `self._normalize_line_endings(text).splitlines`, `len`, `self._logical`, `self._logical(lines[index]).upper`, `output.append`, `self._try_extract_redundant_wrapper_block`, `output.extend`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L44: `if not text`
- L51: `while index < len(lines)`
- L54: `if OUTER_IF_TEXT not in logical`
- L62: `if block is None`

### `SqlcodeWrapperCleanupComposer._try_extract_redundant_wrapper_block` - L73-L113

```python
_try_extract_redundant_wrapper_block(self, lines: list[str], start_index: int) -> tuple[list[str], int] | None
```

Observed calls (lexical order): `self._find_marker_after_outer_if`, `self._find_inner_if_sqlcode_100`, `self._find_matching_end_if`, `self._normalize_inner_body`, `self._format_comment_like_line`, `replacement.extend`.

Control points:

- L81: `if marker_index < 0`
- L87: `if inner_if_index < 0`
- L93: `if inner_end_index < 0`
- L99: `if outer_end_index < 0 or outer_end_index <= inner_end_index`

### `SqlcodeWrapperCleanupComposer._find_marker_after_outer_if` - L115-L122

```python
_find_marker_after_outer_if(self, lines: list[str], start_index: int) -> int
```

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `self._logical(lines[index]).upper`.

Control points:

- L119: `for index in range(start_index, end_index)`
- L120: `if REMOVED_OBTAIN_NEXT_TEXT in self._logical(lines[index]).upper()`

### `SqlcodeWrapperCleanupComposer._find_inner_if_sqlcode_100` - L124-L131

```python
_find_inner_if_sqlcode_100(self, lines: list[str], start_index: int) -> int
```

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `self._logical(lines[index]).upper`, `self._logical(lines[index]).upper().startswith`.

Control points:

- L128: `for index in range(start_index, end_index)`
- L129: `if self._logical(lines[index]).upper().startswith(INNER_IF_TEXT)`

### `SqlcodeWrapperCleanupComposer._find_matching_end_if` - L133-L144

```python
_find_matching_end_if(self, lines: list[str], if_index: int) -> int
```

Observed calls (lexical order): `len`, `range`, `self._logical`, `self._logical(lines[index]).upper`, `self._logical(lines[index]).upper().rstrip`, `logical.startswith`.

Control points:

- L135: `for index in range(if_index, len(lines))`
- L137: `if logical.startswith(TOKEN_IF)`
- L140: `if logical == TOKEN_END_IF`
- L142: `if depth == 0`

### `SqlcodeWrapperCleanupComposer._normalize_inner_body` - L146-L186

```python
_normalize_inner_body(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._logical`, `output.append`, `any`, `logical.startswith`, `output.extend`, `self._normalized_lines_for_logical`, `logical.upper`, `logical.upper().rstrip`.

Control points:

- L150: `for line in lines`
- L153: `if not logical`
- L157: `if any((logical.startswith(p) for p in COMMENT_PREFIXES))`
- L161: `if not first_content_seen`
- L170: `if logical.upper().rstrip('.') == TOKEN_END_IF`

### `SqlcodeWrapperCleanupComposer._normalized_lines_for_logical` - L188-L195

```python
_normalized_lines_for_logical(self, original_line: str, logical: str, indent: str) -> list[str]
```

Observed calls (lexical order): `self._wrap_logical_body`, `self._replace_body_part`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
