# `converter/services/cobol_condition_scanner.py`

Source: [converter/services/cobol_condition_scanner.py](../../../../converter/services/cobol_condition_scanner.py) | 181 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `13a9c5b73c08e824e7ca17d1e6cd08c8660f995dad56a40f7d412bf9f5c9a11c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Finds where a COBOL conditional expression ends.

## Module-level bindings

`COMMENT_PREFIXES` (L30), `__all__` (L181)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.structural_safety_patterns import IF_START_PATTERN
from rules.structural_safety_rules import CONDITION_CONTINUATION_TOKENS, CONDITION_SCAN_LIMIT, CONDITION_TERMINATING_VERBS
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/structural_safety_patterns.py](../../patterns/structural_safety_patterns.md)
- [rules/structural_safety_rules.py](../../rules/structural_safety_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/output_write_block_finder.py](../composers/output_write/output_write_block_finder.md)
- [converter/composers/output_write/output_write_guard.py](../composers/output_write/output_write_guard.md)
- [tests/test_condition_scanner_measures_multiline.py](../../tests/test_condition_scanner_measures_multiline.md)

## Symbol contracts and control points

### `CobolConditionScanner` - L33-L178

```python
class CobolConditionScanner()
```

Locates the last line of a conditional expression.

### `CobolConditionScanner.__init__` - L36-L40

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `CobolConditionScanner.is_condition_start` - L43-L44

```python
is_condition_start(self, line: str) -> bool
```

Observed calls (lexical order): `IF_START_PATTERN.match`, `bool`, `self._logical`.

### `CobolConditionScanner.condition_end_index` - L46-L118

```python
condition_end_index(self, lines: list[str], if_index: int) -> int
```

Index of the LAST line belonging to the IF condition.

Observed calls (lexical order): `len`, `self._logical`, `IF_START_PATTERN.match`, `logical[2:].strip`, `self._holds_statement`, `self._balanced`, `self._ends_on_boolean`, `self._depth`, `min`, `range`, `self._is_comment`, `self._starts_statement`, `self._continues_condition`.

Control points:

- L75: `if not 0 <= if_index < len(lines)`
- L79: `if not IF_START_PATTERN.match(logical)`
- L83: `if self._holds_statement(remainder) and self._balanced(remainder) and (not self._ends_on_boolean(remainder))`
- L94: `for index in range(if_index + 1, end)`
- L97: `if not body or self._is_comment(body)`
- L103: `if self._ends_on_boolean(previous)`
- L110: `if depth <= 0 and self._starts_statement(body)`
- L113: `if depth <= 0 and (not self._continues_condition(body))`

### `CobolConditionScanner._ends_on_boolean` - L121-L128

```python
_ends_on_boolean(body: str) -> bool
```

True when the line's last token is AND / OR / NOT.

Observed calls (lexical order): `str`, `str(body or '').strip`, `str(body or '').strip().rstrip`, `str(body or '').strip().rstrip('.').split`, `bool`, `parts[-1].upper`.

### `CobolConditionScanner.spans_multiple_lines` - L130-L132

```python
spans_multiple_lines(self, lines: list[str], if_index: int) -> bool
```

Observed calls (lexical order): `self.condition_end_index`.

### `CobolConditionScanner.condition_line_count` - L134-L138

```python
condition_line_count(self, lines: list[str], if_index: int) -> int
```

Observed calls (lexical order): `self.condition_end_index`.

Control points:

- L136: `if end < 0`

### `CobolConditionScanner._logical` - L141-L145

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `CobolConditionScanner._is_comment` - L148-L149

```python
_is_comment(body: str) -> bool
```

Observed calls (lexical order): `body.startswith`.

### `CobolConditionScanner._depth` - L152-L153

```python
_depth(body: str) -> int
```

Observed calls (lexical order): `body.count`.

### `CobolConditionScanner._balanced` - L156-L157

```python
_balanced(body: str) -> bool
```

Observed calls (lexical order): `body.count`.

### `CobolConditionScanner._first_word` - L160-L162

```python
_first_word(body: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').strip`, `str(body or '').strip().split`, `parts[0].upper`.

### `CobolConditionScanner._starts_statement` - L164-L165

```python
_starts_statement(self, body: str) -> bool
```

Observed calls (lexical order): `self._first_word`.

### `CobolConditionScanner._continues_condition` - L167-L171

```python
_continues_condition(self, body: str) -> bool
```

Observed calls (lexical order): `self._first_word`, `body.startswith`.

Control points:

- L169: `if word in CONDITION_CONTINUATION_TOKENS`

### `CobolConditionScanner._holds_statement` - L173-L178

```python
_holds_statement(self, remainder: str) -> bool
```

True when the IF line already carries its first statement.

Observed calls (lexical order): `remainder.upper`.

Control points:

- L175: `for verb in CONDITION_TERMINATING_VERBS`
- L176: `if f' {verb} ' in f' {remainder.upper()} '`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
