# `tests/test_condition_scanner_measures_multiline.py`

Source: [tests/test_condition_scanner_measures_multiline.py](../../../tests/test_condition_scanner_measures_multiline.py) | 337 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `0ddc72a038715916a5c584419d245d2d44f8cefcfeae3eba7ad9306f02e49ab5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Condition measurement, and what the measurement is used for.

## Module-level bindings

`QUOTE` (L49), `ZERO8` (L50), `C_FLAG` (L51), `D_FLAG` (L52), `Y_FLAG` (L53), `HEADER` (L70), `FOUR_LINE` (L75), `UNRELATED_MULTILINE_THEN_SAFE_WRITE` (L144), `OWN_GUARD_SPANS_LINES` (L184), `CONDITION_LINES` (L197)

## Import declarations

```python
import pytest
from converter.composers.output_write.output_write_block_finder import CandidateBlock
from converter.composers.output_write.output_write_guard import OutputWriteGuard
from converter.composers.output_write_paragraph_composer import OutputWriteParagraphComposer
from converter.services.cobol_condition_scanner import CobolConditionScanner
```

## Local dependency notes

- [converter/composers/output_write/output_write_block_finder.py](../converter/composers/output_write/output_write_block_finder.md)
- [converter/composers/output_write/output_write_guard.py](../converter/composers/output_write/output_write_guard.md)
- [converter/composers/output_write_paragraph_composer.py](../converter/composers/output_write_paragraph_composer.md)
- [converter/services/cobol_condition_scanner.py](../converter/services/cobol_condition_scanner.md)

## Symbol contracts and control points

### `fixed` - L56-L59

```python
fixed(seq: str, body: str, right: str) -> str
```

One 80-column fixed-format record.

Observed calls (lexical order): `len`, `body.ljust`.

### `bodies_of` - L62-L67

```python
bodies_of(text: str) -> list[str]
```

Observed calls (lexical order): `line[7:72].strip`, `text.splitlines`, `len`.

### `scanner` - L86-L87

```python
scanner()
```

Observed calls (lexical order): `CobolConditionScanner`.

### `test_a_four_line_condition_measures_four` - L93-L97

```python
test_a_four_line_condition_measures_four(scanner)
```

Observed calls (lexical order): `len`, `scanner.condition_line_count`.

### `test_a_line_ending_on_and_never_closes_the_condition` - L100-L104

```python
test_a_line_ending_on_and_never_closes_the_condition(scanner)
```

Observed calls (lexical order): `len`, `scanner.condition_end_index`.

### `test_a_single_line_condition_still_measures_one` - L107-L114

```python
test_a_single_line_condition_still_measures_one(scanner)
```

Observed calls (lexical order): `fixed`, `len`, `scanner.condition_line_count`.

### `test_the_guard_measures_a_multi_line_condition` - L120-L124

```python
test_the_guard_measures_a_multi_line_condition()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteGuard`, `OutputWriteGuard().blocks_extraction`, `OutputWriteGuard().widest_condition`.

### `test_the_guard_measures_a_single_line_condition` - L127-L138

```python
test_the_guard_measures_a_single_line_condition()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `OutputWriteGuard`, `OutputWriteGuard().blocks_extraction`, `OutputWriteGuard().widest_condition`.

### `test_an_unrelated_multi_line_condition_does_not_block_a_candidate` - L161-L168

```python
test_an_unrelated_multi_line_condition_does_not_block_a_candidate()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `out.count`.

### `test_the_unrelated_condition_is_left_exactly_as_written` - L171-L178

```python
test_the_unrelated_condition_is_left_exactly_as_written()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `bodies_of`.

### `test_a_candidate_whose_own_guard_spans_lines_is_now_extracted` - L203-L211

```python
test_a_candidate_whose_own_guard_spans_lines_is_now_extracted()
```

The cut moved past the condition, so nothing has to be refused.

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `out.count`.

### `test_every_condition_line_stays_at_the_call_site` - L214-L224

```python
test_every_condition_line_stays_at_the_call_site()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `bodies_of`, `bodies.index`.

Control points:

- L221: `for fragment in CONDITION_LINES`

### `test_the_extracted_body_starts_after_the_condition` - L227-L233

```python
test_the_extracted_body_starts_after_the_condition()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `bodies_of`, `bodies.index`.

### `test_no_dangling_boolean_operator_survives` - L236-L241

```python
test_no_dangling_boolean_operator_survives()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `bodies_of`, `body.upper`, `body.upper().startswith`.

Control points:

- L239: `for body in bodies_of(OutputWriteParagraphComposer().compose(text))`

### `test_the_counter_increment_lands_at_the_call_site` - L244-L252

```python
test_the_counter_increment_lands_at_the_call_site()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `bodies_of`, `bodies.index`.

### `test_the_extraction_is_reported_with_the_source_paragraph` - L255-L263

```python
test_the_extraction_is_reported_with_the_source_paragraph()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `composer.compose`, `' '.join`.

### `test_extraction_is_idempotent` - L266-L272

```python
test_extraction_is_idempotent()
```

Observed calls (lexical order): `'\n'.join`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`.

### `_unresolvable_program` - L278-L298

```python
_unresolvable_program() -> list[str]
```

A condition longer than CONDITION_SCAN_LIMIT never resolves.

Observed calls (lexical order): `fixed`, `range`, `lines.append`, `'0024{0:02d}'.format`, `'0024{0:02d}00'.format`.

Control points:

- L285: `for step in range(30)`

### `test_an_unresolvable_condition_is_still_refused` - L301-L308

```python
test_an_unresolvable_condition_is_still_refused()
```

Observed calls (lexical order): `'\n'.join`, `_unresolvable_program`, `OutputWriteParagraphComposer`, `composer.compose`, `out.count`.

### `test_the_refusal_is_reported_with_the_source_paragraph` - L311-L320

```python
test_the_refusal_is_reported_with_the_source_paragraph()
```

A refusal with no diagnostic is worse than no guard at all.

Observed calls (lexical order): `'\n'.join`, `_unresolvable_program`, `OutputWriteParagraphComposer`, `composer.compose`, `' '.join`.

### `test_an_unresolved_block_falls_back_to_the_safe_body_start` - L323-L329

```python
test_an_unresolved_block_falls_back_to_the_safe_body_start()
```

body_start must never be nonsense when the condition is unknown.

Observed calls (lexical order): `CandidateBlock`.

### `test_a_resolved_block_cuts_after_the_condition` - L332-L337

```python
test_a_resolved_block_cuts_after_the_condition()
```

Observed calls (lexical order): `CandidateBlock`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
