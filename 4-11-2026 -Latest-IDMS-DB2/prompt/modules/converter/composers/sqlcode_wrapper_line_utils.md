# `converter/composers/sqlcode_wrapper_line_utils.py`

Source: [converter/composers/sqlcode_wrapper_line_utils.py](../../../../converter/composers/sqlcode_wrapper_line_utils.py) | 180 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `53ae7ebbac023324fdfb03ab26c4defb7800b33cc789918560b6aa314de6c153`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.sqlcode_wrapper_patterns import MOVE_TO_PATTERN
from patterns.sequence_patterns import strip_sequence_numbers
from rules.sqlcode_wrapper_rules import BASE_INDENT, BODY_END_COLUMN, BODY_START_COLUMN, BODY_WIDTH, CONTINUATION_INDENT, DB2_COMMENT_PREFIX, FULL_LINE_WIDTH, INDICATOR_COLUMN, RIGHT_SEQUENCE_END, RIGHT_SEQUENCE_START, SEQUENCE_AREA_WIDTH, TOKEN_MOVE, TOKEN_OF_DCL, TOKEN_TO
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [patterns/sqlcode_wrapper_patterns.py](../../patterns/sqlcode_wrapper_patterns.md)
- [rules/sqlcode_wrapper_rules.py](../../rules/sqlcode_wrapper_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/sqlcode_wrapper_cleanup_composer.py](sqlcode_wrapper_cleanup_composer.md)

## Symbol contracts and control points

### `SqlcodeWrapperLineUtils` - L23-L180

```python
class SqlcodeWrapperLineUtils()
```

Line normalization, MOVE/word wrapping, and fixed-format helpers.

### `SqlcodeWrapperLineUtils._normalize_line_endings` - L29-L30

```python
_normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `SqlcodeWrapperLineUtils._logical` - L32-L33

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

### `SqlcodeWrapperLineUtils._wrap_logical_body` - L35-L51

```python
_wrap_logical_body(self, logical: str, indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `indent.rstrip`, `self._wrap_move_statement`, `len`, `self._wrap_by_words`.

Control points:

- L37: `if not text`
- L41: `if move_lines`
- L45: `if len(body) <= BODY_WIDTH`

### `SqlcodeWrapperLineUtils._wrap_move_statement` - L53-L93

```python
_wrap_move_statement(self, logical: str, indent: str) -> list[str]
```

Observed calls (lexical order): `MOVE_TO_PATTERN.match`, `str`, `str(logical or '').strip`, `match.group`, `str(match.group('source') or '').strip`, `str(match.group('target') or '').strip`, `source.upper`, `len`, `output.append`, `output.extend`, `self._wrap_by_words`.

Control points:

- L55: `if not match`
- L60: `if not source or not target`
- L66: `if len(one_line) <= BODY_WIDTH and (not force_split)`
- L73: `if len(first_line) <= BODY_WIDTH`
- L83: `if len(second_line) <= BODY_WIDTH`

### `SqlcodeWrapperLineUtils._wrap_by_words` - L95-L137

```python
_wrap_by_words(self, body: str, continuation_indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `len`, `text.strip`, `text.strip().split`, `current.rstrip`, `current.strip`, `output.append`, `enumerate`, `normalized.append`, `line.startswith`, `line.strip`.

Control points:

- L97: `if len(text) <= BODY_WIDTH`
- L104: `for word in words`
- L106: `if len(candidate) <= BODY_WIDTH`
- L109: `if current`
- L110: `if output`
- L116: `if current`
- L117: `if output`
- L122: `if not output`
- Another 3 conditions/loops exist in this source span.

### `SqlcodeWrapperLineUtils._replace_body_part` - L139-L151

```python
_replace_body_part(self, original_line: str, new_body: str) -> str
```

Observed calls (lexical order): `str`, `str(original_line or '').rstrip`, `self._is_fixed_format_line`, `str(new_body or '').rstrip`, `str(new_body or '').rstrip()[:BODY_WIDTH].ljust`.

Control points:

- L142: `if self._is_fixed_format_line(line)`

### `SqlcodeWrapperLineUtils._format_comment_like_line` - L153-L170

```python
_format_comment_like_line(self, reference_line: str, comment_text: str) -> str
```

Observed calls (lexical order): `str`, `str(reference_line or '').rstrip`, `str(comment_text or '').strip`, `clean_comment.upper`, `clean_comment.upper().startswith`, `self._is_fixed_format_line`, `body[:BODY_WIDTH].ljust`.

Control points:

- L159: `if not clean_comment.upper().startswith(DB2_COMMENT_PREFIX)`
- L164: `if self._is_fixed_format_line(line)`

### `SqlcodeWrapperLineUtils._is_fixed_format_line` - L172-L180

```python
_is_fixed_format_line(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:SEQUENCE_AREA_WIDTH].isdigit`, `text[RIGHT_SEQUENCE_START:RIGHT_SEQUENCE_END].isdigit`.

Control points:

- L174: `if len(text) < FULL_LINE_WIDTH`
- L176: `if not text[:SEQUENCE_AREA_WIDTH].isdigit()`
- L178: `if not text[RIGHT_SEQUENCE_START:RIGHT_SEQUENCE_END].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
