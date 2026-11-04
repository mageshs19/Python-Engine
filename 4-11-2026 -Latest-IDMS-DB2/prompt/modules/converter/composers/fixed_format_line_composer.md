# `converter/composers/fixed_format_line_composer.py`

Source: [converter/composers/fixed_format_line_composer.py](../../../../converter/composers/fixed_format_line_composer.py) | 263 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `0219f5c0696314a70aebe9e0b123550ca3cf4eeff1e965aa23af980c845a7d8c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Per-line composition: parse, area-body, wrap, sequence, compose.

## Module-level bindings

`DEFAULT_PROCEDURE_INDENT` (L61), `__all__` (L263)

## Import declarations

```python
from __future__ import annotations
from patterns.fixed_format_patterns import DIVISION_PATTERN, SEQUENCE_ONLY_PATTERN
from rules.fixed_format_rules import BODY_WIDTH, COMMENT_INDICATOR, DEBUG_INDICATOR, DEBUG_INDICATOR_LOWER, FIXED_FORMAT_MESSAGES, LEFT_SEQUENCE_WIDTH, PAGE_INDICATOR, PROCEDURE_DIVISION_NAME, RIGHT_SEQUENCE_WIDTH, SPACE_INDICATOR, TOTAL_WIDTH, VALID_INDICATORS
```

## Local dependency notes

- [patterns/fixed_format_patterns.py](../../patterns/fixed_format_patterns.md)
- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_composer.py](fixed_format_composer.md)

## Symbol contracts and control points

### `FixedFormatLineComposer` - L64-L260

```python
class FixedFormatLineComposer()
```

Per-line composition: parse, area-body, wrap, sequence, compose.

### `FixedFormatLineComposer._compose_body_lines` - L70-L156

```python
_compose_body_lines(self, *, raw_text: str, state, current_division: str, inside_exec_sql: bool, previous_procedure_indent: str, preserve_blank_lines: bool, output_lines: list[str]) -> tuple[str, bool, str]
```

Process one raw line, appending composed records.

Observed calls (lexical order): `SEQUENCE_ONLY_PATTERN.match`, `raw_text.strip`, `self.line_parser.parse_line`, `str`, `body.strip`, `self._append_blank`, `DIVISION_PATTERN.match`, `division_match.group`, `division_match.group(1).upper`, `self.body_formatter.is_exec_sql_start`, `self.body_formatter.area_body`, `self.wrapper.wrap_body`, `self.wrapper.repair_boolean_operator_only_lines`, `enumerate`, `self._continuation_indicator`, `output_lines.append`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L86: `if SEQUENCE_ONLY_PATTERN.match(raw_text.strip())`
- L94: `if not logical and indicator == SPACE_INDICATOR`
- L99: `if division_match`
- L103: `if self.body_formatter.is_exec_sql_start(logical)`
- L126: `for (index, physical_body) in enumerate(physical_bodies)`
- L142: `if current_division == PROCEDURE_DIVISION_NAME and indicator == SPACE_INDICATOR and physical_bodies and (not self.body_formatter.is_area_a_statement(logical))`
- L153: `if self.body_formatter.is_exec_sql_end(logical)`

### `FixedFormatLineComposer._append_blank` - L158-L175

```python
_append_blank(self, state, preserve_blank_lines: bool, output_lines: list[str]) -> None
```

Observed calls (lexical order): `output_lines.append`, `self._compose_line`, `state.current_left`, `state.current_right`, `state.advance`.

Control points:

- L164: `if not preserve_blank_lines`

### `FixedFormatLineComposer._continuation_indicator` - L177-L182

```python
_continuation_indicator(self, indicator: str) -> str
```

Control points:

- L178: `if indicator in {COMMENT_INDICATOR, PAGE_INDICATOR}`
- L180: `if indicator in {DEBUG_INDICATOR, DEBUG_INDICATOR_LOWER}`

### `FixedFormatLineComposer._compose_line` - L187-L223

```python
_compose_line(self, left_seq: str, indicator: str, area_body: str, right_seq: str) -> str
```

Assemble one 80-COLUMN record. Width is counted in CHARACTERS.

Observed calls (lexical order): `str`, `str(left_seq or '').zfill`, `str(right_seq or '').zfill`, `str(area_body or '').rstrip`, `len`, `self._report_truncation`, `safe_body.ljust`, `self._report_geometry_drift`, `line[:TOTAL_WIDTH].ljust`.

Control points:

- L202: `if safe_indicator not in VALID_INDICATORS`
- L204: `if safe_indicator == DEBUG_INDICATOR_LOWER`
- L209: `if len(safe_body) > BODY_WIDTH`
- L219: `if len(line) != TOTAL_WIDTH`

### `FixedFormatLineComposer._report_truncation` - L228-L244

```python
_report_truncation(self, body: str) -> None
```

Record a body that did not fit columns 8-72.

Observed calls (lexical order): `getattr`, `FIXED_FORMAT_MESSAGES.get`, `messages.append`, `template.format`, `len`, `body.strip`.

Control points:

- L231: `if messages is None`
- L235: `if not template`

### `FixedFormatLineComposer._report_geometry_drift` - L246-L260

```python
_report_geometry_drift(self, width: int) -> None
```

Record a record that did not assemble to exactly 80 columns.

Observed calls (lexical order): `getattr`, `FIXED_FORMAT_MESSAGES.get`, `messages.append`, `template.format`.

Control points:

- L249: `if messages is None`
- L253: `if template`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
