# `converter/composers/fixed_format_line_parser.py`

Source: [converter/composers/fixed_format_line_parser.py](../../../../converter/composers/fixed_format_line_parser.py) | 300 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `b0d9a32ff0ce4c814c6e73b3450502356edd11e4e7c767fae1997906102b9f81`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL line parser.

## Module-level bindings

`__all__` (L300)

## Import declarations

```python
from __future__ import annotations
from converter.composers.fixed_format_sequence_stripper import FixedFormatSequenceStripper
from patterns.fixed_format_patterns import DEBUG_LINE_PATTERN, TRUE_LEFT_SEQUENCE_PATTERN
from rules.fixed_format_rules import BODY_END, BODY_START, BODY_WIDTH, COMMENT_INDICATOR, DEBUG_INDICATOR, INDICATOR_INDEX, LEFT_SEQUENCE_END, LEFT_SEQUENCE_START, LEFT_SEQUENCE_WIDTH, LINE_ENDINGS, MIN_ADDRESSABLE_LENGTH, PAGE_INDICATOR, RIGHT_SEQUENCE_END, RIGHT_SEQUENCE_START, RIGHT_SEQUENCE_WIDTH, SPACE_INDICATOR, TOTAL_WIDTH, VALID_INDICATORS
```

## Local dependency notes

- [converter/composers/fixed_format_sequence_stripper.py](fixed_format_sequence_stripper.md)
- [patterns/fixed_format_patterns.py](../../patterns/fixed_format_patterns.md)
- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_composer.py](fixed_format_composer.md)
- [tests/layout/test_fixed_format_body_bounds.py](../../tests/layout/test_fixed_format_body_bounds.md)

## Symbol contracts and control points

### `FixedFormatLineParser` - L81-L297

```python
class FixedFormatLineParser(FixedFormatSequenceStripper)
```

Parses fixed-format and loose COBOL lines safely.

### `FixedFormatLineParser.parse_line` - L87-L109

```python
parse_line(self, line: str) -> dict[str, str | bool]
```

Split one raw record into its four fixed-format areas.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.parse_fixed_80_line`, `self.remove_loose_sequence_numbers`, `self.indicator_for_body`, `self.strip_inline_indicator`.

Control points:

- L96: `if fixed is not None`

### `FixedFormatLineParser.parse_fixed_80_line` - L111-L173

```python
parse_fixed_80_line(self, line: str) -> dict[str, str | bool] | None
```

Parse a sequenced record, whatever its physical length.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self._is_fixed_format_line`, `text[BODY_START:BODY_END].rstrip`, `self._has_right_sequence`.

Control points:

- L153: `if not self._is_fixed_format_line(text)`
- L157: `if indicator not in VALID_INDICATORS`

### `FixedFormatLineParser.body_for_boolean_merge` - L175-L176

```python
body_for_boolean_merge(self, line: str) -> str
```

Observed calls (lexical order): `self.parse_line`, `self.parse_line(line).get`, `str`.

### `FixedFormatLineParser.indicator_for_body` - L181-L193

```python
indicator_for_body(self, body: str) -> str
```

Observed calls (lexical order): `str`, `text.lstrip`, `stripped.startswith`, `DEBUG_LINE_PATTERN.match`.

Control points:

- L183: `if not text`
- L187: `if stripped.startswith(COMMENT_INDICATOR)`
- L189: `if stripped.startswith(PAGE_INDICATOR)`
- L191: `if DEBUG_LINE_PATTERN.match(text)`

### `FixedFormatLineParser.strip_inline_indicator` - L195-L208

```python
strip_inline_indicator(self, body: str, indicator: str) -> str
```

Observed calls (lexical order): `str`, `text.lstrip`, `stripped.startswith`, `stripped[1:].lstrip`, `DEBUG_LINE_PATTERN.match`, `stripped[:1].upper`, `text.rstrip`.

Control points:

- L198: `if indicator in {COMMENT_INDICATOR, PAGE_INDICATOR}`
- L200: `if stripped.startswith(indicator)`
- L203: `if indicator == DEBUG_INDICATOR and DEBUG_LINE_PATTERN.match(text)`
- L205: `if stripped[:1].upper() == DEBUG_INDICATOR`

### `FixedFormatLineParser.is_debug_line` - L210-L211

```python
is_debug_line(self, stripped: str) -> bool
```

Observed calls (lexical order): `DEBUG_LINE_PATTERN.match`, `bool`, `str`.

### `FixedFormatLineParser.replace_body_preserving_sequence` - L216-L255

```python
replace_body_preserving_sequence(self, original_line: str, new_body: str) -> str
```

Rewrite columns 8-72 and keep both sequence areas in place.

Observed calls (lexical order): `str`, `str(original_line or '').rstrip`, `self.parse_line`, `str(new_body or '').rstrip`, `bool`, `parsed.get`, `left.zfill`, `raw_right.zfill`, `body[:BODY_WIDTH].ljust`, `TRUE_LEFT_SEQUENCE_PATTERN.match`, `match.group`.

Control points:

- L231: `if bool(parsed.get('is_fixed_format'))`
- L236: `if indicator not in VALID_INDICATORS`
- L250: `if match`

### `FixedFormatLineParser._is_fixed_format_line` - L260-L275

```python
_is_fixed_format_line(self, line: str) -> bool
```

True when columns 1-6 are numeric and column 7 is an indicator.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[LEFT_SEQUENCE_START:LEFT_SEQUENCE_END].isdigit`.

Control points:

- L269: `if len(text) < MIN_ADDRESSABLE_LENGTH`
- L272: `if not text[LEFT_SEQUENCE_START:LEFT_SEQUENCE_END].isdigit()`

### `FixedFormatLineParser._has_right_sequence` - L277-L284

```python
_has_right_sequence(self, line: str) -> bool
```

True only when columns 73-80 really hold eight digits.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[RIGHT_SEQUENCE_START:RIGHT_SEQUENCE_END].isdigit`.

Control points:

- L281: `if len(text) < RIGHT_SEQUENCE_END`

### `FixedFormatLineParser.is_strict_fixed_line` - L286-L297

```python
is_strict_fixed_line(self, line: str) -> bool
```

A complete 80-column record: sequenced AND right-sequenced.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `self._is_fixed_format_line`, `self._has_right_sequence`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
