# `tests/test_db2_date_comparison.py`

Source: [tests/test_db2_date_comparison.py](../../../tests/test_db2_date_comparison.py) | 391 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `58e925ecc01ec395218f995a6ff5c1b86df52007c73d3aeb0a375b4c59b9d423`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 DATE comparison conversion.

## Module-level bindings

`VMDZ7200_CONDITION` (L64), `FIXED_CONDITION` (L276), `FIXED_PROGRAM` (L341)

## Import declarations

```python
import pytest
from converter.composers.db2_date_comparison_composer import Db2DateComparisonComposer
from converter.composers.db2_date_condition_assembler import Db2DateConditionAssembler
from converter.composers.db2_date_field_detector import Db2DateFieldDetector
from converter.composers.db2_date_comparison_rewriter import Db2DateComparisonRewriter
```

## Local dependency notes

- [converter/composers/db2_date_comparison_composer.py](../converter/composers/db2_date_comparison_composer.md)
- [converter/composers/db2_date_comparison_rewriter.py](../converter/composers/db2_date_comparison_rewriter.md)
- [converter/composers/db2_date_condition_assembler.py](../converter/composers/db2_date_condition_assembler.md)
- [converter/composers/db2_date_field_detector.py](../converter/composers/db2_date_field_detector.md)

## Symbol contracts and control points

### `composer` - L38-L39

```python
composer() -> Db2DateComparisonComposer
```

Observed calls (lexical order): `Db2DateComparisonComposer`.

### `detector` - L43-L44

```python
detector() -> Db2DateFieldDetector
```

Observed calls (lexical order): `Db2DateFieldDetector`.

### `assembler` - L48-L49

```python
assembler() -> Db2DateConditionAssembler
```

Observed calls (lexical order): `Db2DateConditionAssembler`.

### `_program` - L52-L58

```python
_program(body: str) -> str
```

### `test_assembler_joins_a_four_line_parenthesised_condition` - L77-L91

```python
test_assembler_joins_a_four_line_parenthesised_condition(assembler)
```

Observed calls (lexical order): `_program`, `_program(VMDZ7200_CONDITION).splitlines`, `next`, `enumerate`, `line.strip`, `line.strip().startswith`, `assembler.span_at`.

### `test_assembler_stops_before_the_statement_body` - L94-L104

```python
test_assembler_stops_before_the_statement_body(assembler)
```

Observed calls (lexical order): `_program`, `_program(VMDZ7200_CONDITION).splitlines`, `next`, `enumerate`, `line.strip`, `line.strip().startswith`, `assembler.span_at`.

### `test_detector_finds_both_hosts_in_a_compound_condition` - L110-L116

```python
test_detector_finds_both_hosts_in_a_compound_condition(detector)
```

Observed calls (lexical order): `_program`, `_program(VMDZ7200_CONDITION).splitlines`, `detector.date_fields_used_in_comparisons`.

### `test_detector_no_longer_requires_the_token_parmdate` - L119-L129

```python
test_detector_no_longer_requires_the_token_parmdate(detector)
```

Observed calls (lexical order): `_program`, `_program(body).splitlines`, `detector.date_fields_used_in_comparisons`.

### `test_detector_ignores_a_reference_with_no_comparison` - L132-L140

```python
test_detector_ignores_a_reference_with_no_comparison(detector)
```

Observed calls (lexical order): `_program`, `_program(body).splitlines`, `detector.date_fields_used_in_comparisons`.

### `test_detector_never_touches_an_exec_sql_host` - L143-L152

```python
test_detector_never_touches_an_exec_sql_host(detector)
```

Observed calls (lexical order): `_program`, `_program(body).splitlines`, `detector.date_fields_used_in_comparisons`.

### `test_compound_condition_is_rewritten_onto_helpers` - L158-L163

```python
test_compound_condition_is_rewritten_onto_helpers(composer)
```

Observed calls (lexical order): `_program`, `composer.compose`.

### `test_realignment_block_is_emitted_before_the_if` - L166-L177

```python
test_realignment_block_is_emitted_before_the_if(composer)
```

Observed calls (lexical order): `_program`, `composer.compose`, `output.splitlines`, `next`, `enumerate`, `line.strip`, `line.strip().startswith`.

### `test_shared_date_working_storage_is_declared` - L180-L184

```python
test_shared_date_working_storage_is_declared(composer)
```

Observed calls (lexical order): `_program`, `composer.compose`.

### `test_original_line_breaks_are_preserved` - L187-L214

```python
test_original_line_breaks_are_preserved(composer)
```

The four physical lines of the condition stay four lines.

Observed calls (lexical order): `_program`, `composer.compose`, `output.splitlines`, `next`, `enumerate`, `line.strip`, `line.strip().startswith`, `len`, `all`.

### `test_one_helper_field_is_declared_per_converted_host` - L217-L228

```python
test_one_helper_field_is_declared_per_converted_host(composer)
```

The realignment target must exist in Working-Storage.

Observed calls (lexical order): `_program`, `composer.compose`, `output.splitlines`, `len`, `any`.

### `test_literals_and_business_operands_are_untouched` - L230-L235

```python
test_literals_and_business_operands_are_untouched(composer)
```

Observed calls (lexical order): `_program`, `composer.compose`.

### `test_conversion_is_reported` - L241-L246

```python
test_conversion_is_reported(composer)
```

Observed calls (lexical order): `_program`, `composer.compose`, `' '.join`.

### `test_a_program_with_no_dates_says_so` - L249-L261

```python
test_a_program_with_no_dates_says_so(composer)
```

Observed calls (lexical order): `_program`, `composer.compose`, `any`.

### `test_empty_text_is_safe` - L264-L266

```python
test_empty_text_is_safe(composer)
```

Observed calls (lexical order): `composer.compose`.

### `_fixed` - L271-L273

```python
_fixed(seq: str, body: str, right: str) -> str
```

An 80-column line: 6 seq, 1 indicator, 65 body, 8 right seq.

Observed calls (lexical order): `body[:65].ljust`.

### `test_substitution_keeps_every_line_at_eighty_columns` - L286-L312

```python
test_substitution_keeps_every_line_at_eighty_columns()
```

The right sequence area must stay at column 73.

Observed calls (lexical order): `_fixed`, `Db2DateComparisonRewriter`, `Db2DateComparisonRewriter().rewrite_date_comparisons`, `len`, `line[:6].isdigit`, `line[72:80].isdigit`.

Control points:

- L309: `for line in rewritten`

### `test_a_four_line_condition_stays_four_lines_when_fixed_format` - L315-L330

```python
test_a_four_line_condition_stays_four_lines_when_fixed_format()
```

Observed calls (lexical order): `_fixed`, `Db2DateComparisonRewriter`, `Db2DateComparisonRewriter().rewrite_date_comparisons`, `len`.

### `_fixed` - L335-L338

```python
_fixed(seq: str, body: str, right: str) -> str
```

An exact 80-column record: 6 seq + 1 indicator + 65 body + 8 seq.

Observed calls (lexical order): `len`, `body.ljust`.

### `_rewrite_fixed` - L353-L361

```python
_rewrite_fixed()
```

Observed calls (lexical order): `Db2DateComparisonRewriter`, `Db2DateComparisonRewriter().rewrite_date_comparisons`, `list`.

### `test_every_rewritten_record_is_exactly_eighty_columns` - L364-L368

```python
test_every_rewritten_record_is_exactly_eighty_columns()
```

Observed calls (lexical order): `_rewrite_fixed`, `len`, `line[0:6].isdigit`, `line[72:80].isdigit`.

Control points:

- L365: `for line in _rewrite_fixed()`

### `test_a_four_line_condition_stays_four_lines` - L371-L372

```python
test_a_four_line_condition_stays_four_lines()
```

Observed calls (lexical order): `_rewrite_fixed`, `len`.

### `test_no_stray_token_is_appended_to_the_body` - L375-L381

```python
test_no_stray_token_is_appended_to_the_body()
```

A wrapped pseudo-body once split the right sequence off as '0'.

Observed calls (lexical order): `_rewrite_fixed`, `line[7:72].rstrip`, `body.endswith`.

Control points:

- L377: `for line in _rewrite_fixed()`

### `test_the_condition_text_is_intact` - L384-L391

```python
test_the_condition_text_is_intact()
```

Observed calls (lexical order): `_rewrite_fixed`, `line[7:72].rstrip`, `' '.join`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
