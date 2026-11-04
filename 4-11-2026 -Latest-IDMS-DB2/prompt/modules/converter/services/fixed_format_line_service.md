# `converter/services/fixed_format_line_service.py`

Source: [converter/services/fixed_format_line_service.py](../../../../converter/services/fixed_format_line_service.py) | 613 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `36bfbc311c2bdc177a8e5d552e544f1e1bdd1bf969aa9fc31278dc8a55b4b422`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL line helper service.

## Module-level bindings

`__all__` (L609)

## Import declarations

```python
from __future__ import annotations
from rules.fixed_format_rules import QUALIFIER_CONNECTOR_WORDS
```

## Local dependency notes

- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (51)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/counter_line_factory.py](../composers/counter_declaration/counter_line_factory.md)
- [converter/composers/counter_declaration_composer.py](../composers/counter_declaration_composer.md)
- [converter/composers/counter_declaration_writer.py](../composers/counter_declaration_writer.md)
- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)
- [converter/composers/fixed_format_wrapper.py](../composers/fixed_format_wrapper.md)
- [converter/composers/lrf_group_move_decomposer.py](../composers/lrf_group_move_decomposer.md)
- [converter/composers/lrf_key_binding_composer.py](../composers/lrf_key_binding_composer.md)
- [converter/composers/move_alignment_composer.py](../composers/move_alignment_composer.md)
- [converter/composers/output_write/output_write_line_utils.py](../composers/output_write/output_write_line_utils.md)
- [converter/composers/output_write_paragraph_composer.py](../composers/output_write_paragraph_composer.md)
- [converter/composers/procedure_indent_normalizer.py](../composers/procedure_indent_normalizer.md)
- [converter/composers/program_identity_initializer.py](../composers/program_identity_initializer.md)
- [tests/test_cobol_area_alignment_reflow.py](../../tests/test_cobol_area_alignment_reflow.md)
- [tests/test_field_reference_geometry.py](../../tests/test_field_reference_geometry.md)
- [tests/test_fixed_format_continuation_indicator.py](../../tests/test_fixed_format_continuation_indicator.md)
- [tests/test_qualifier_connector_wrap.py](../../tests/test_qualifier_connector_wrap.md)
- 35 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `glue_qualifier_connectors` - L118-L139

```python
glue_qualifier_connectors(words: list[str]) -> list[str]
```

Merge each qualifier connector (OF/IN) with the name that follows it.

Observed calls (lexical order): `len`, `word.upper`, `glued.append`.

Control points:

- L129: `while index < total`
- L132: `if is_connector and index + 1 < total`

### `BodyOverflowError` - L142-L143

```python
class BodyOverflowError(ValueError)
```

Raised when a COBOL body would not fit columns 8-72.

### `FixedFormatLineService` - L146-L606

```python
class FixedFormatLineService()
```

Utility for fixed-format COBOL lines.

Declared class/data-model fields:

```python
LEFT_SEQUENCE_START = 0
LEFT_SEQUENCE_END = 6
INDICATOR_INDEX = 6
BODY_START = 7
BODY_END = 72
RIGHT_SEQUENCE_START = 72
RIGHT_SEQUENCE_END = 80
BODY_WIDTH = 65
LEFT_SEQUENCE_WIDTH = 6
RIGHT_SEQUENCE_WIDTH = 8
MIN_ADDRESSABLE_LENGTH = 7
COMMENT_INDICATORS = ('*', '/')
DEBUG_INDICATORS = ('D', 'd')
CONTINUATION_INDICATOR = '-'
BLANK_INDICATOR = ' '
VALID_INDICATORS = (' ', '*', '/', 'D', 'd', '-')
WRAP_CONTINUATION_INDENT = ' '
WRAP_MAX_LINES = 4
```

### `FixedFormatLineService.is_fixed_line` - L189-L206

```python
is_fixed_line(self, line: str) -> bool
```

True when columns 1-6 are numeric and column 7 is a valid indicator.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[self.LEFT_SEQUENCE_START:self.LEFT_SEQUENCE_END].isdigit`.

Control points:

- L198: `if len(text) < self.MIN_ADDRESSABLE_LENGTH`
- L201: `if not text[self.LEFT_SEQUENCE_START:self.LEFT_SEQUENCE_END].isdigit()`

### `FixedFormatLineService.is_strict_fixed_line` - L208-L223

```python
is_strict_fixed_line(self, line: str) -> bool
```

The original, stricter test: full 80 columns, both sequences numeric.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[self.LEFT_SEQUENCE_START:self.LEFT_SEQUENCE_END].isdigit`, `text[self.RIGHT_SEQUENCE_START:self.RIGHT_SEQUENCE_END].isdigit`.

### `FixedFormatLineService.split` - L225-L244

```python
split(self, line: str) -> tuple[str, str, str, str]
```

Return (left_sequence, indicator, body, right_sequence).

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.is_fixed_line`, `text.ljust`.

Control points:

- L234: `if self.is_fixed_line(text)`

### `FixedFormatLineService.body` - L246-L247

```python
body(self, line: str) -> str
```

Observed calls (lexical order): `self.split`.

### `FixedFormatLineService.logical` - L249-L250

```python
logical(self, line: str) -> str
```

Observed calls (lexical order): `self.body`, `self.body(line).strip`.

### `FixedFormatLineService.indicator` - L252-L253

```python
indicator(self, line: str) -> str
```

Observed calls (lexical order): `self.split`.

### `FixedFormatLineService.left_sequence` - L255-L256

```python
left_sequence(self, line: str) -> str
```

Observed calls (lexical order): `self.split`.

### `FixedFormatLineService.right_sequence` - L258-L259

```python
right_sequence(self, line: str) -> str
```

Observed calls (lexical order): `self.split`.

### `FixedFormatLineService.leading_spaces` - L261-L266

```python
leading_spaces(self, text: str, default: str='') -> str
```

Observed calls (lexical order): `str`, `len`, `value.lstrip`.

Control points:

- L263: `if not value`

### `FixedFormatLineService.body_indent` - L268-L269

```python
body_indent(self, line: str) -> str
```

Observed calls (lexical order): `self.body`, `self.leading_spaces`.

### `FixedFormatLineService.is_comment_or_control_line` - L274-L289

```python
is_comment_or_control_line(self, line: str) -> bool
```

True for comment, page-eject and debug lines.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `text.strip`, `self.is_fixed_line`, `text.lstrip`, `bool`.

Control points:

- L281: `if not text.strip()`
- L284: `if self.is_fixed_line(text)`

### `FixedFormatLineService.is_comment_line` - L291-L292

```python
is_comment_line(self, line: str) -> bool
```

Observed calls (lexical order): `self.indicator`.

### `FixedFormatLineService.is_debug_line` - L294-L295

```python
is_debug_line(self, line: str) -> bool
```

Observed calls (lexical order): `self.indicator`.

### `FixedFormatLineService.is_continuation_line` - L297-L298

```python
is_continuation_line(self, line: str) -> bool
```

Observed calls (lexical order): `self.indicator`.

### `FixedFormatLineService.is_blank` - L300-L301

```python
is_blank(self, line: str) -> bool
```

Observed calls (lexical order): `self.logical`.

### `FixedFormatLineService.is_sequence_artifact` - L303-L332

```python
is_sequence_artifact(self, line: str) -> bool
```

True when the BODY is nothing but a leaked source sequence number.

Observed calls (lexical order): `self.logical`, `candidate.endswith`, `candidate.strip`, `len`, `candidate.isdigit`.

Control points:

- L318: `if not candidate`
- L321: `if candidate.endswith('.')`
- L324: `if candidate and candidate[-1] in self.COMMENT_INDICATORS`

### `FixedFormatLineService.body_fits` - L337-L338

```python
body_fits(self, body: str) -> bool
```

Observed calls (lexical order): `len`, `str`, `str(body or '').rstrip`.

### `FixedFormatLineService.normalize_indicator` - L343-L352

```python
normalize_indicator(self, indicator: str) -> str
```

One valid column-7 character. Anything unrecognised becomes blank.

Observed calls (lexical order): `str`.

Control points:

- L350: `if marker not in self.VALID_INDICATORS`

### `FixedFormatLineService.build` - L354-L404

```python
build(self, left_sequence: str, indicator: str, body: str, right_sequence: str) -> str
```

Assemble one 80-column line, or a free-form line when unsequenced.

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `self.body_fits`, `BodyOverflowError`, `len`, `self.normalize_indicator`, `left.rjust`, `right.rjust`, `clean_body.ljust`.

Control points:

- L378: `if not self.body_fits(clean_body)`
- L391: `if not left and (not right)`
- L392: `if marker == self.BLANK_INDICATOR`

Explicit raises: `BodyOverflowError(f'COBOL body needs {len(clean_body)} columns, only {self.BODY_WIDTH} are available: {clean_body!r}')`.

### `FixedFormatLineService.build_or_none` - L406-L416

```python
build_or_none(self, left_sequence: str, indicator: str, body: str, right_sequence: str) -> str | None
```

Observed calls (lexical order): `self.build`.

### `FixedFormatLineService.emit` - L418-L457

```python
emit(self, left_sequence: str, indicator: str, body: str, right_sequence: str) -> list[str]
```

Render a logical body as one or more physical lines.

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `self.body_fits`, `self.build`, `self.leading_spaces`, `self.wrap_body_lines`, `BodyOverflowError`, `enumerate`.

Control points:

- L432: `if self.body_fits(clean_body)`
- L443: `if not bodies`

Explicit raises: `BodyOverflowError(f'COBOL body cannot be wrapped within {self.WRAP_MAX_LINES} lines: {clean_body!r}')`.

### `FixedFormatLineService.replace_body` - L462-L474

```python
replace_body(self, line: str, new_body: str) -> str
```

Replace the body, or return the line unchanged when it will not fit.

Observed calls (lexical order): `self.split`, `self.build_or_none`, `str`, `str(line or '').rstrip`.

### `FixedFormatLineService.replace_body_strict` - L476-L479

```python
replace_body_strict(self, line: str, new_body: str) -> str
```

Replace the body, raising BodyOverflowError when it will not fit.

Observed calls (lexical order): `self.split`, `self.build`.

### `FixedFormatLineService.replace_body_wrapped` - L481-L521

```python
replace_body_wrapped(self, line: str, new_body: str) -> list[str]
```

Replace the body, wrapping onto further physical lines if needed.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.split`, `str(new_body or '').rstrip`, `self.body_fits`, `self.replace_body`, `self.is_fixed_line`, `self.leading_spaces`, `self.wrap_body_lines`, `enumerate`, `self.build_or_none`, `rendered.append`.

Control points:

- L494: `if self.body_fits(clean_body)`
- L497: `if not self.is_fixed_line(original)`
- L506: `if not bodies`
- L510: `for (index, part) in enumerate(bodies)`
- L517: `if built is None`

### `FixedFormatLineService.wrap_body` - L526-L542

```python
wrap_body(self, body: str, continuation_indent: str) -> list[str]
```

Split one logical body into at most TWO fixed-format bodies.

Observed calls (lexical order): `self.wrap_body_lines`, `len`.

### `FixedFormatLineService.wrap_body_lines` - L544-L606

```python
wrap_body_lines(self, body: str, continuation_indent: str, max_lines: int | None=None) -> list[str]
```

Split one logical body into N fixed-format bodies.

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `self.leading_spaces`, `clean_body.split`, `glue_qualifier_connectors`, `len`, `any`, `max`, `list`, `' '.join`, `taken.append`, `bodies.append`.

Control points:

- L567: `if not words or limit < 1`
- L573: `if first_limit <= 0 or next_limit <= 0`
- L577: `if any((len(word) > max(first_limit, next_limit) for word in words))`
- L584: `while remaining`
- L585: `if len(bodies) >= limit`
- L592: `for word in remaining`
- L594: `if len(candidate) <= window`
- L599: `if not taken`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
