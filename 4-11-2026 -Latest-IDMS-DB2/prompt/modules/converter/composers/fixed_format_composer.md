# `converter/composers/fixed_format_composer.py`

Source: [converter/composers/fixed_format_composer.py](../../../../converter/composers/fixed_format_composer.py) | 257 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `bb3ef9c72dbc068d9e7d3fcd1f125e92f9152176590f0c80393a377ed89de70d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL composer.

## Import declarations

```python
from converter.composers.fixed_format_body_formatter import FixedFormatBodyFormatter
from converter.composers.fixed_format_line_composer import FixedFormatLineComposer
from converter.composers.fixed_format_line_parser import FixedFormatLineParser
from converter.composers.fixed_format_sequence_manager import FixedFormatSequenceManager
from converter.composers.fixed_format_wrapper import FixedFormatWrapper
from rules.fixed_format_rules import BODY_WIDTH, FIXED_FORMAT_MESSAGES, TOTAL_WIDTH, VALID_INDICATORS
```

## Local dependency notes

- [converter/composers/fixed_format_body_formatter.py](fixed_format_body_formatter.md)
- [converter/composers/fixed_format_line_composer.py](fixed_format_line_composer.md)
- [converter/composers/fixed_format_line_parser.py](fixed_format_line_parser.md)
- [converter/composers/fixed_format_sequence_manager.py](fixed_format_sequence_manager.md)
- [converter/composers/fixed_format_wrapper.py](fixed_format_wrapper.md)
- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](cobol_cleanup_composer.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)
- [tests/layout/test_fixed_format_body_bounds.py](../../tests/layout/test_fixed_format_body_bounds.md)
- [tests/test_sw_status_child_fetch_driven_normalization.py](../../tests/test_sw_status_child_fetch_driven_normalization.md)

## Symbol contracts and control points

### `FixedFormatComposer` - L43-L257

```python
class FixedFormatComposer(FixedFormatLineComposer)
```

Final fixed-format COBOL composer.

### `FixedFormatComposer.__init__` - L56-L62

```python
__init__(self) -> None
```

Observed calls (lexical order): `FixedFormatLineParser`, `FixedFormatBodyFormatter`, `FixedFormatWrapper`, `FixedFormatSequenceManager`.

### `FixedFormatComposer.format` - L64-L115

```python
format(self, text: str, left_start: int | None=None, left_step: int | None=None, right_start: int | None=None, right_step: int | None=None, preserve_blank_lines: bool=True) -> str
```

Observed calls (lexical order): `self._normalize_line_endings`, `self._normalize_line_endings(text).splitlines`, `self._merge_dangling_boolean_lines`, `self.sequence_manager.create_state`, `str`, `str(raw_line or '').rstrip`, `raw_text.strip`, `self._append_blank`, `self._compose_body_lines`, `'\n'.join`, `'\n'.join(output_lines).rstrip`.

Control points:

- L73: `if not text`
- L94: `for raw_line in lines`
- L97: `if not raw_text.strip()`

### `FixedFormatComposer.validate_fixed_format` - L117-L172

```python
validate_fixed_format(self, text: str) -> list[str]
```

Observed calls (lexical order): `enumerate`, `str`, `str(text or '').splitlines`, `len`, `messages.append`, `left_seq.isdigit`, `int`, `right_seq.isdigit`.

Control points:

- L123: `for (line_number, line) in enumerate(str(text or '').splitlines(), start=1)`
- L126: `if not line`
- L129: `if len(line) != TOTAL_WIDTH`
- L139: `if not left_seq.isdigit()`
- L146: `if previous_left is not None and left_value - previous_left != 10`
- L153: `if indicator not in VALID_INDICATORS`
- L158: `if not right_seq.isdigit()`
- L165: `if previous_right is not None and right_value - previous_right != 10000`

### `FixedFormatComposer._normalize_line_endings` - L174-L175

```python
_normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `FixedFormatComposer._merge_dangling_boolean_lines` - L177-L252

```python
_merge_dangling_boolean_lines(self, lines: list[str]) -> list[str]
```

Join a line ending in AND / OR / NOT to its continuation.

Observed calls (lexical order): `len`, `str`, `str(lines[index] or '').rstrip`, `output.append`, `str(lines[index + 1] or '').rstrip`, `self.line_parser.body_for_boolean_merge`, `current_body.strip`, `next_body.strip`, `self.wrapper.is_comment_or_page_line`, `self.wrapper.ends_with_boolean_operator`, `current_body.rstrip`, `self.line_parser.replace_body_preserving_sequence`, `self._log`.

Control points:

- L203: `while index < len(lines)`
- L206: `if index + 1 >= len(lines)`
- L215: `if not current_body.strip() or not next_body.strip()`
- L219: `if self.wrapper.is_comment_or_page_line(current_body)`
- L223: `if self.wrapper.is_comment_or_page_line(next_body)`
- L228: `if self.wrapper.ends_with_boolean_operator(current_body)`
- L231: `if len(merged_body) <= BODY_WIDTH`

### `FixedFormatComposer._log` - L254-L257

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `FIXED_FORMAT_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L256: `if template`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
