# `tests/layout/test_fixed_format_body_bounds.py`

Source: [tests/layout/test_fixed_format_body_bounds.py](../../../../tests/layout/test_fixed_format_body_bounds.py) | 105 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `cd36d15bb831d0525a9851b4d2d442e6b21f73ac92b034604cf6ab16c030c0e8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The body never extends past column 72.

## Module-level bindings

`STATEMENT` (L20), `SEQUENCE` (L21), `STRANDED` (L22)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.fixed_format_composer import FixedFormatComposer
from converter.composers.fixed_format_line_parser import FixedFormatLineParser
```

## Local dependency notes

- [converter/composers/fixed_format_composer.py](../../converter/composers/fixed_format_composer.md)
- [converter/composers/fixed_format_line_parser.py](../../converter/composers/fixed_format_line_parser.md)

## Symbol contracts and control points

### `_record` - L25-L26

```python
_record(body: str=STATEMENT, right: str=SEQUENCE) -> str
```

Observed calls (lexical order): `body.ljust`.

### `_bodies` - L29-L30

```python
_bodies(text: str) -> list[str]
```

Observed calls (lexical order): `len`, `text.splitlines`.

### `test_a_full_record_separates_the_sequence` - L36-L39

```python
test_a_full_record_separates_the_sequence()
```

Observed calls (lexical order): `FixedFormatLineParser`, `FixedFormatLineParser().parse_line`, `_record`.

### `test_a_record_one_character_short_still_stops_at_column_72` - L42-L46

```python
test_a_record_one_character_short_still_stops_at_column_72()
```

CORRECTION 4. This returned a 72-character body carrying 0235000.

Observed calls (lexical order): `FixedFormatLineParser`, `FixedFormatLineParser().parse_line`, `_record`, `str`.

### `test_a_record_longer_than_80_still_stops_at_column_72` - L49-L51

```python
test_a_record_longer_than_80_still_stops_at_column_72()
```

Observed calls (lexical order): `FixedFormatLineParser`, `FixedFormatLineParser().parse_line`, `_record`.

### `test_a_blank_sequence_area_yields_no_right_sequence` - L54-L57

```python
test_a_blank_sequence_area_yields_no_right_sequence()
```

Observed calls (lexical order): `FixedFormatLineParser`, `FixedFormatLineParser().parse_line`, `_record`.

### `test_no_body_carries_a_stranded_sequence` - L63-L68

```python
test_no_body_carries_a_stranded_sequence()
```

Observed calls (lexical order): `'\n'.join`, `_record`, `FixedFormatComposer`, `FixedFormatComposer().format`, `STRANDED.search`, `_bodies`.

### `test_formatting_twice_is_idempotent` - L71-L77

```python
test_formatting_twice_is_idempotent()
```

The pass runs more than once per program. The second run must be a no-op; while the body ran past column 72 it was not.

Observed calls (lexical order): `FixedFormatComposer`, `'\n'.join`, `_record`, `composer.format`, `FixedFormatComposer().format`.

### `test_every_emitted_record_is_80_columns` - L80-L84

```python
test_every_emitted_record_is_80_columns()
```

Observed calls (lexical order): `FixedFormatComposer`, `FixedFormatComposer().format`, `_record`, `out.splitlines`, `len`, `repr`.

Control points:

- L82: `for line in out.splitlines()`
- L83: `if line`

### `test_sequence_manager_normalizes_source_steps_to_required_output_steps` - L86-L95

```python
test_sequence_manager_normalizes_source_steps_to_required_output_steps()
```

Observed calls (lexical order): `'\n'.join`, `"000100 DISPLAY 'A'.".ljust`, `"000120 DISPLAY 'B'.".ljust`, `FixedFormatComposer`, `FixedFormatComposer().format`, `out.splitlines`, `int`, `FixedFormatComposer().validate_fixed_format`.

### `test_fixed_format_validator_reports_sequence_gaps` - L98-L105

```python
test_fixed_format_validator_reports_sequence_gaps()
```

Observed calls (lexical order): `"DISPLAY 'A'.".ljust`, `"DISPLAY 'B'.".ljust`, `'\n'.join`, `FixedFormatComposer`, `FixedFormatComposer().validate_fixed_format`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
