# `patterns/sequence_patterns.py`

Source: [patterns/sequence_patterns.py](../../../patterns/sequence_patterns.py) | 529 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `cb7147c2c5aa09795b04b3149587d2963dcdcd9ad26df3e3d23adc57e30b9d1c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL fixed-format sequence handling.

## Module-level bindings

`LEFT_SEQUENCE_START` (L99), `LEFT_SEQUENCE_END` (L100), `INDICATOR_INDEX` (L101), `BODY_START` (L102), `BODY_END` (L103), `RIGHT_SEQUENCE_START` (L104), `RIGHT_SEQUENCE_END` (L105), `LINE_WIDTH` (L107), `BODY_WIDTH` (L108), `INDICATED_BODY_WIDTH` (L109), `MIN_ADDRESSABLE_LENGTH` (L111), `LEFT_SEQUENCE_WIDTH` (L112), `RIGHT_SEQUENCE_WIDTH` (L113), `LINE_ENDINGS` (L115), `VALID_INDICATORS` (L118), `COMMENT_INDICATORS` (L119), `DEBUG_INDICATORS` (L120), `CONTINUATION_INDICATOR` (L121), `BLANK_INDICATOR` (L122), `STRIP_NESTED_SEQUENCE` (L127), `MAX_NESTED_SEQUENCE_PASSES` (L128), `CONTINUATION_REQUIRES_RIGHT_SEQUENCE` (L134), `_INDICATOR_CLASS` (L139), `_NESTED_INDICATOR_CLASS` (L144), `LEFT_SEQUENCE_PATTERN` (L149), `RIGHT_SEQUENCE_PATTERN` (L154), `NESTED_SEQUENCE_PATTERN` (L161), `SEQUENCE_ARTIFACT_PATTERN` (L169), `_ALL_DIGITS_PATTERN` (L174), `__all__` (L485)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (17)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_analyzer.py](../converter/analyzers/field_usage_analyzer.md)
- [converter/analyzers/program_flow/flow_line_reader.py](../converter/analyzers/program_flow/flow_line_reader.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](../converter/composers/cleanup/cobol_cleanup_line_utils.md)
- [converter/composers/cleanup/paragraph_terminator_cleanup.py](../converter/composers/cleanup/paragraph_terminator_cleanup.md)
- [converter/composers/cursor_flow_line_formatter.py](../converter/composers/cursor_flow_line_formatter.md)
- [converter/composers/cursor_order_cleanup_composer.py](../converter/composers/cursor_order_cleanup_composer.md)
- [converter/composers/db2_date_line_utils.py](../converter/composers/db2_date_line_utils.md)
- [converter/composers/retrieval_commit_cleanup_composer.py](../converter/composers/retrieval_commit_cleanup_composer.md)
- [converter/composers/sqlcode_wrapper_line_utils.py](../converter/composers/sqlcode_wrapper_line_utils.md)
- [converter/composers/unnecessary_comments_cleanup_composer.py](../converter/composers/unnecessary_comments_cleanup_composer.md)
- [converter/composers/update_restart_skip_composer.py](../converter/composers/update_restart_skip_composer.md)
- [converter/composers/update_sql_cleanup/scan_mixin.py](../converter/composers/update_sql_cleanup/scan_mixin.md)
- 5 further importers are recorded in [the source manifest](../../source_manifest.json).

## Symbol contracts and control points

### `_clean` - L180-L186

```python
_clean(line: str) -> str
```

The physical line with its line ending removed, nothing else.

Observed calls (lexical order): `str`, `str(line or '').rstrip`.

### `is_paragraph_number_prefix` - L189-L217

```python
is_paragraph_number_prefix(line: str) -> bool
```

True when a six-digit run is the HEAD OF A NAME, not a sequence area.

Observed calls (lexical order): `_clean`, `len`, `text[LEFT_SEQUENCE_START:LEFT_SEQUENCE_END].isdigit`, `text[BODY_START:BODY_START + 1].isalnum`, `has_right_sequence`.

Control points:

- L205: `if len(text) <= BODY_START`
- L208: `if not text[LEFT_SEQUENCE_START:LEFT_SEQUENCE_END].isdigit()`
- L211: `if text[INDICATOR_INDEX] != CONTINUATION_INDICATOR`
- L214: `if not text[BODY_START:BODY_START + 1].isalnum()`

### `is_fixed_format_line` - L220-L244

```python
is_fixed_format_line(line: str) -> bool
```

True when columns 1-6 are numeric and column 7 is a valid indicator.

Observed calls (lexical order): `_clean`, `len`, `text[LEFT_SEQUENCE_START:LEFT_SEQUENCE_END].isdigit`, `is_paragraph_number_prefix`.

Control points:

- L232: `if len(text) < MIN_ADDRESSABLE_LENGTH`
- L235: `if not text[LEFT_SEQUENCE_START:LEFT_SEQUENCE_END].isdigit()`
- L238: `if text[INDICATOR_INDEX] not in VALID_INDICATORS`
- L241: `if CONTINUATION_REQUIRES_RIGHT_SEQUENCE and is_paragraph_number_prefix(text)`

### `has_right_sequence` - L247-L258

```python
has_right_sequence(line: str) -> bool
```

True when columns 73-80 hold an eight-digit sequence.

Observed calls (lexical order): `_clean`, `len`, `bool`, `_ALL_DIGITS_PATTERN.match`.

Control points:

- L251: `if len(text) < RIGHT_SEQUENCE_END`

### `indicator_of` - L261-L277

```python
indicator_of(line: str) -> str
```

Column 7 of a fixed-format line.

Observed calls (lexical order): `_clean`, `is_fixed_format_line`, `text.lstrip`.

Control points:

- L270: `if is_fixed_format_line(text)`
- L274: `if stripped and stripped[0] in COMMENT_INDICATORS`

### `is_comment_or_control` - L280-L292

```python
is_comment_or_control(line: str) -> bool
```

True for comment, page-eject and debug lines.

Observed calls (lexical order): `_clean`, `text.strip`, `indicator_of`.

Control points:

- L289: `if not text.strip()`

### `is_blank` - L295-L297

```python
is_blank(line: str) -> bool
```

True when the line carries no body at all.

Observed calls (lexical order): `logical_body`.

### `has_nested_sequence_area` - L300-L312

```python
has_nested_sequence_area(body: str) -> bool
```

True when a BODY still begins with a leaked sequence area.

Observed calls (lexical order): `str`, `NESTED_SEQUENCE_PATTERN.match`, `bool`, `text.lstrip`.

Control points:

- L309: `if text[:1] in VALID_INDICATORS`

### `is_sequence_artifact` - L315-L334

```python
is_sequence_artifact(line: str) -> bool
```

True when the line carries nothing but a leaked sequence number.

Observed calls (lexical order): `_clean`, `text.strip`, `logical_body`, `SEQUENCE_ARTIFACT_PATTERN.match`, `is_fixed_format_line`, `text[BODY_START:RIGHT_SEQUENCE_START].strip`, `has_right_sequence`, `bool`.

Control points:

- L319: `if not text.strip()`
- L323: `if body and SEQUENCE_ARTIFACT_PATTERN.match(body)`
- L328: `if is_fixed_format_line(text)`
- L330: `if not remainder and (not has_right_sequence(text))`

### `strip_left_sequence` - L340-L367

```python
strip_left_sequence(line: str) -> str
```

Remove columns 1-6, keeping the indicator and the body.

Observed calls (lexical order): `_clean`, `is_paragraph_number_prefix`, `is_fixed_format_line`, `LEFT_SEQUENCE_PATTERN.match`, `match.group`, `body[1:2].isalnum`, `has_right_sequence`.

Control points:

- L349: `if CONTINUATION_REQUIRES_RIGHT_SEQUENCE and is_paragraph_number_prefix(text)`
- L352: `if is_fixed_format_line(text)`
- L356: `if match`
- L358: `if CONTINUATION_REQUIRES_RIGHT_SEQUENCE and body[:1] == CONTINUATION_INDICATOR and body[1:2].isalnum() and (not has_right_sequence(text))`

### `strip_right_sequence` - L370-L387

```python
strip_right_sequence(line: str) -> str
```

Remove columns 73-80, but only when they really are a sequence.

Observed calls (lexical order): `_clean`, `is_fixed_format_line`, `has_right_sequence`, `RIGHT_SEQUENCE_PATTERN.match`, `match.group`.

Control points:

- L378: `if is_fixed_format_line(text)`
- L379: `if has_right_sequence(text)`
- L384: `if match`

### `strip_nested_sequence` - L390-L412

```python
strip_nested_sequence(body: str) -> str
```

Remove a sequence area that has leaked into a body.

Observed calls (lexical order): `str`, `range`, `text.lstrip`, `NESTED_SEQUENCE_PATTERN.match`, `match.group`.

Control points:

- L396: `if not STRIP_NESTED_SEQUENCE`
- L402: `if text[:1] in VALID_INDICATORS`
- L405: `for _ in range(MAX_NESTED_SEQUENCE_PASSES)`
- L408: `if not match`

### `strip_sequence_numbers` - L415-L433

```python
strip_sequence_numbers(line: str) -> str
```

Remove columns 1-6 and 73-80, KEEPING column 7 onwards.

Observed calls (lexical order): `_clean`, `is_paragraph_number_prefix`, `is_fixed_format_line`, `text.ljust`, `padded[INDICATOR_INDEX:RIGHT_SEQUENCE_START].rstrip`, `strip_nested_sequence`, `strip_left_sequence`, `strip_right_sequence`, `strip_right_sequence(strip_left_sequence(text)).rstrip`.

Control points:

- L424: `if CONTINUATION_REQUIRES_RIGHT_SEQUENCE and is_paragraph_number_prefix(text)`
- L427: `if is_fixed_format_line(text)`

### `logical_body` - L436-L448

```python
logical_body(line: str) -> str
```

Columns 8-72 only, stripped. Indicator excluded.

Observed calls (lexical order): `_clean`, `is_paragraph_number_prefix`, `text.strip`, `is_fixed_format_line`, `text.ljust`, `padded[BODY_START:BODY_END].rstrip`, `strip_nested_sequence`, `strip_nested_sequence(body).strip`, `strip_sequence_numbers`, `strip_sequence_numbers(text).strip`.

Control points:

- L440: `if CONTINUATION_REQUIRES_RIGHT_SEQUENCE and is_paragraph_number_prefix(text)`
- L443: `if is_fixed_format_line(text)`

### `replace_body` - L454-L482

```python
replace_body(line: str, new_body: str) -> str
```

Rewrite columns 8-72 and keep both sequence areas in place.

Observed calls (lexical order): `_clean`, `str`, `str(new_body or '').rstrip`, `is_fixed_format_line`, `len`, `text.lstrip`, `has_right_sequence`, `body.ljust`.

Control points:

- L467: `if not is_fixed_format_line(text)`
- L471: `if len(body) > BODY_WIDTH`

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
