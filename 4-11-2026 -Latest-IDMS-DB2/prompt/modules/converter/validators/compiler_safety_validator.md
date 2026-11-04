# `converter/validators/compiler_safety_validator.py`

Source: [converter/validators/compiler_safety_validator.py](../../../../converter/validators/compiler_safety_validator.py) | 265 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `6c9860f657fde3949463c1c34d5815a38e582c1dc6b346aa6041e78bff671814`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Static preflight checks for common COBOL/DB2 compile failures.

## Module-level bindings

`_FIXED_LINE` (L11), `_LEVEL_ENTRY` (L12), `_CURSOR_DECLARE` (L13), `_FETCH` (L14), `_HOST` (L15), `__all__` (L265)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/validators/production_validator.py](production_validator.md)
- [tests/generated_fields/test_compiler_safety_validator.py](../../tests/generated_fields/test_compiler_safety_validator.md)
- [tests/test_compiler_safety_validator.py](../../tests/test_compiler_safety_validator.md)

## Symbol contracts and control points

### `CompilerSafetyValidator` - L18-L262

```python
class CompilerSafetyValidator()
```

Find source-level hazards before submitting a mainframe compile.

### `CompilerSafetyValidator.validate` - L21-L33

```python
validate(self, cobol_text: str) -> list[str]
```

Observed calls (lexical order): `str`, `text.strip`, `self._logical`, `text.splitlines`, `self._mask_executable_lines`, `messages.extend`, `self._redefines_value`, `self._sql_block_balance`, `self._sqlcode_sentence_terminators`, `self._cursor_fetch_parity`.

Control points:

- L23: `if not text.strip()`

### `CompilerSafetyValidator._logical` - L36-L44

```python
_logical(line: str) -> str
```

Return executable-area text, excluding fixed-format metadata/comments.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `raw[:6].isdigit`.

Control points:

- L39: `if len(raw) >= 7 and raw[:6].isdigit()`
- L41: `if indicator in {'*', '/', 'D', 'd'}`

### `CompilerSafetyValidator._mask_executable_lines` - L47-L103

```python
_mask_executable_lines(lines: list[str]) -> list[str]
```

Mask literals, inline comments and SQL comments without shifting columns.

Observed calls (lexical order): `list`, `str`, `len`, `range`, `''.join`, `result.append`.

Control points:

- L56: `for line in lines`
- L60: `while i < len(chars)`
- L61: `if in_block_comment`
- L62: `if i + 1 < len(chars) and chars[i] == '*' and (chars[i + 1] == '/')`
- L72: `if quote is not None`
- L74: `if char == quote`
- L75: `if i + 1 < len(chars) and chars[i + 1] == quote`
- L83: `if char in {"'", '"'}`
- Another 5 conditions/loops exist in this source span.

### `CompilerSafetyValidator._redefines_value` - L105-L133

```python
_redefines_value(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `line.startswith`, `_LEVEL_ENTRY.match`, `check`, `declaration.append`.

Control points:

- L123: `for (number, line) in enumerate(lines, start=1)`
- L124: `if not line or line.startswith('*') or line.startswith('/')`
- L126: `if _LEVEL_ENTRY.match(line)`
- L130: `if declaration`

### `CompilerSafetyValidator._redefines_value.check` - L110-L121

```python
check() -> None
```

Observed calls (lexical order): `' '.join`, `re.search`, `messages.append`.

Control points:

- L111: `if not declaration`
- L114: `if re.search('\\bREDEFINES\\b', joined, re.I) and re.search('\\bVALUE(?:S)?\\b', joined, re.I)`

### `CompilerSafetyValidator._sql_block_balance` - L136-L155

```python
_sql_block_balance(lines: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `line.startswith`, `line.upper`, `len`, `re.findall`, `messages.append`.

Control points:

- L139: `for (number, line) in enumerate(lines, start=1)`
- L140: `if not line or line.startswith('*') or line.startswith('/')`
- L146: `if open_count < 0`
- L151: `if open_count`

### `CompilerSafetyValidator._sqlcode_sentence_terminators` - L158-L188

```python
_sqlcode_sentence_terminators(lines: list[str]) -> list[str]
```

Flag periods that terminate an EVALUATE SQLCODE before END-EVALUATE.

Observed calls (lexical order): `enumerate`, `line.startswith`, `line.upper`, `re.search`, `active.append`, `active.pop`, `re.sub`, `messages.append`.

Control points:

- L167: `for (number, line) in enumerate(lines, start=1)`
- L168: `if not line or line.startswith(('*', '/'))`
- L171: `if re.search('\\bEVALUATE\\s+SQLCODE\\b', upper)`
- L174: `if not active`
- L176: `if re.search('\\bEND-EVALUATE\\b', upper)`
- L182: `if re.search('\\.\\s*$', without_literals)`

### `CompilerSafetyValidator._cursor_fetch_parity` - L190-L235

```python
_cursor_fetch_parity(self, lines: list[str]) -> list[str]
```

Compare each simple cursor SELECT column count with its FETCH host count.

Observed calls (lexical order): `line.startswith`, `line.upper`, `re.search`, `current.append`, `' '.join`, `sql_blocks.append`, `_CURSOR_DECLARE.search`, `declare.group`, `declare.group(1).upper`, `select.group`, `self._top_level_items`, `_FETCH.search`, `fetch.group`, `fetch.group(1).upper`, `_HOST.findall`, `into.group`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L195: `for line in lines`
- L196: `if not line or line.startswith('*') or line.startswith('/')`
- L199: `if not inside and re.search('\\bEXEC\\s+SQL\\b', upper)`
- L202: `if inside`
- L204: `if inside and re.search('\\bEND-EXEC\\b', upper)`
- L211: `for block in sql_blocks`
- L213: `if declare`
- L216: `if select`
- Another 5 conditions/loops exist in this source span.

### `CompilerSafetyValidator._top_level_items` - L238-L262

```python
_top_level_items(select_list: str) -> int
```

Count comma-separated SELECT expressions, ignoring nested commas.

Observed calls (lexical order): `str`, `str(select_list or '').strip`, `len`, `max`.

Control points:

- L241: `if not text`
- L247: `while i < len(text)`
- L249: `if char == "'"`
- L250: `if quoted and i + 1 < len(text) and (text[i + 1] == "'")`
- L254: `if not quoted`
- L255: `if char == '('`
- L257: `if char == ')'`
- L259: `if char == ',' and depth == 0`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
