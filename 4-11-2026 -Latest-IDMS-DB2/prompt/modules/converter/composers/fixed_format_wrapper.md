# `converter/composers/fixed_format_wrapper.py`

Source: [converter/composers/fixed_format_wrapper.py](../../../../converter/composers/fixed_format_wrapper.py) | 263 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `9a45b7fc2f637c65e241ebac71283866e4fc16fcc41f4e930af427e209b556d0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL body wrapper.

## Import declarations

```python
from __future__ import annotations
from patterns.fixed_format_patterns import BOOLEAN_OPERATOR_END_PATTERN, IF_BOOLEAN_SPLIT_PATTERN, MOVE_STATEMENT_PATTERN
from converter.services.fixed_format_line_service import glue_qualifier_connectors
from rules.fixed_format_rules import BODY_WIDTH, BOOLEAN_OPERATOR_WORDS, COMMENT_INDICATOR, PAGE_INDICATOR, PROCEDURE_DIVISION_NAME, WRAP_IF_PREFIX, WRAP_MOVE_PREFIX, WRAP_TO_PREFIX
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/fixed_format_patterns.py](../../patterns/fixed_format_patterns.md)
- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_composer.py](fixed_format_composer.md)
- [tests/test_qualifier_connector_wrap.py](../../tests/test_qualifier_connector_wrap.md)

## Symbol contracts and control points

### `FixedFormatWrapper` - L37-L263

```python
class FixedFormatWrapper()
```

### `FixedFormatWrapper.wrap_body` - L38-L59

```python
wrap_body(self, body: str, indicator: str, inside_exec_sql: bool, current_division: str, previous_procedure_indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `len`, `self.wrap_comment_body`, `self.wrap_cobol_body`.

Control points:

- L48: `if len(text) <= BODY_WIDTH`
- L51: `if indicator in {COMMENT_INDICATOR, PAGE_INDICATOR}`

### `FixedFormatWrapper.wrap_comment_body` - L61-L65

```python
wrap_comment_body(self, text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').strip`, `self.wrap_by_words`.

Control points:

- L63: `if not clean`

### `FixedFormatWrapper.wrap_cobol_body` - L67-L95

```python
wrap_cobol_body(self, text: str, inside_exec_sql: bool, current_division: str, previous_procedure_indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').rstrip`, `raw.strip`, `self.leading_spaces`, `self.wrap_if_statement`, `self.wrap_move_statement`, `self.wrap_by_words`.

Control points:

- L81: `if inside_exec_sql`
- L85: `if if_lines`
- L89: `if move_lines`

### `FixedFormatWrapper.wrap_if_statement` - L97-L117

```python
wrap_if_statement(self, logical: str, indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `text.upper`, `text.upper().startswith`, `self.split_condition_on_boolean_operator`, `self.wrap_by_words`, `left_part.rstrip`, `operator.strip`, `operator.strip().upper`, `right_part.strip`, `self.force_lines_to_body_width`.

Control points:

- L100: `if not text.upper().startswith(WRAP_IF_PREFIX)`
- L104: `if not split_result`

### `FixedFormatWrapper.split_condition_on_boolean_operator` - L119-L135

```python
split_condition_on_boolean_operator(self, logical: str) -> tuple[str, str, str] | None
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `IF_BOOLEAN_SPLIT_PATTERN.split`, `len`, `tokens[0].rstrip`, `tokens[1].strip`, `tokens[1].strip().upper`, `tokens[2].strip`.

Control points:

- L125: `if len(tokens) < 3`
- L132: `if not left_part or not operator or (not right_part)`

### `FixedFormatWrapper.wrap_move_statement` - L137-L154

```python
wrap_move_statement(self, logical: str, indent: str) -> list[str]
```

Observed calls (lexical order): `MOVE_STATEMENT_PATTERN.match`, `str`, `str(logical or '').strip`, `match.group`, `match.group('src').strip`, `match.group('tgt').strip`, `len`, `self.wrap_by_words`.

Control points:

- L139: `if not match`
- L148: `if len(first) <= BODY_WIDTH and len(second) <= BODY_WIDTH`

### `FixedFormatWrapper.wrap_by_words` - L156-L189

```python
wrap_by_words(self, text: str, continuation_indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').rstrip`, `len`, `self.leading_spaces`, `raw.strip`, `content.split`, `glue_qualifier_connectors`, `current.strip`, `current.rstrip`, `lines.append`, `self.force_lines_to_body_width`.

Control points:

- L158: `if len(raw) <= BODY_WIDTH`
- L168: `for word in words`
- L169: `if current.strip()`
- L174: `if len(candidate) <= BODY_WIDTH`
- L178: `if current.strip()`
- L183: `if current.strip()`

### `FixedFormatWrapper.force_lines_to_body_width` - L191-L214

```python
force_lines_to_body_width(self, lines: list[str], continuation_indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `output.append`, `self.leading_spaces`, `max`, `text.strip`, `content[:available_width].rstrip`, `content[len(part):].strip`, `self.repair_boolean_operator_only_lines`.

Control points:

- L196: `for line in lines`
- L199: `if len(text) <= BODY_WIDTH`
- L207: `while content`
- L209: `if not part`

### `FixedFormatWrapper.repair_boolean_operator_only_lines` - L216-L241

```python
repair_boolean_operator_only_lines(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `len`, `str`, `str(lines[index] or '').rstrip`, `current.strip`, `current.strip().upper`, `str(lines[index + 1] or '').rstrip`, `next_line.strip`, `self.leading_spaces`, `output.append`.

Control points:

- L222: `while index < len(lines)`
- L226: `if current_stripped in BOOLEAN_OPERATOR_WORDS and index + 1 < len(lines)`
- L230: `if next_stripped`
- L233: `if len(repaired) <= BODY_WIDTH`

### `FixedFormatWrapper.ends_with_boolean_operator` - L243-L246

```python
ends_with_boolean_operator(self, body: str) -> bool
```

Observed calls (lexical order): `bool`, `BOOLEAN_OPERATOR_END_PATTERN.search`, `str`, `str(body or '').strip`.

### `FixedFormatWrapper.is_comment_or_page_line` - L248-L252

```python
is_comment_or_page_line(self, logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `stripped.startswith`.

### `FixedFormatWrapper.leading_spaces` - L254-L263

```python
leading_spaces(self, text: str, default: str='') -> str
```

Observed calls (lexical order): `str`, `len`, `value.lstrip`.

Control points:

- L256: `if not value`
- L260: `if count <= 0`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
