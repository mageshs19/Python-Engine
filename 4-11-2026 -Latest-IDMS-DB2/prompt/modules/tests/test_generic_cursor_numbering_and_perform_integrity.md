# `tests/test_generic_cursor_numbering_and_perform_integrity.py`

Source: [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../../tests/test_generic_cursor_numbering_and_perform_integrity.py) | 341 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `d40b5a1a476556c41a0c6f68f6f06e929914d0d9cc182ce4400a2966d0242824`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
from rules.cursor_rules import cursor_paragraph_number
from converter.composers.cursor_flow.span_loop_plan import SpanLoopPlanBuilder
from converter.composers.cursor_flow.loop_shape import LoopShapeScanner
from converter.generators.cursor_paragraph_generator import CursorParagraphGenerator
from converter.generators.sql_error_generator import SqlErrorGenerator
from converter.analyzers.access_error_policy import AccessPattern, classify_access, policy_for
```

## Local dependency notes

- [converter/analyzers/access_error_policy.py](../converter/analyzers/access_error_policy.md)
- [converter/composers/cursor_flow/loop_shape.py](../converter/composers/cursor_flow/loop_shape.md)
- [converter/composers/cursor_flow/span_loop_plan.py](../converter/composers/cursor_flow/span_loop_plan.md)
- [converter/generators/cursor_paragraph_generator.py](../converter/generators/cursor_paragraph_generator.md)
- [converter/generators/sql_error_generator.py](../converter/generators/sql_error_generator.md)
- [converter/resolvers/cursor_name_resolver.py](../converter/resolvers/cursor_name_resolver.md)
- [converter/validators/generated_cobol_release_validator.py](../converter/validators/generated_cobol_release_validator.md)
- [rules/cursor_rules.py](../rules/cursor_rules.md)

## Symbol contracts and control points

### `test_cursor_numbering_is_central_and_scales_beyond_three_cursors` - L6-L10

```python
test_cursor_numbering_is_central_and_scales_beyond_three_cursors()
```

Observed calls (lexical order): `cursor_paragraph_number`.

### `test_cursor_name_resolver_uses_same_numbers_for_all_paragraph_names` - L13-L22

```python
test_cursor_name_resolver_uses_same_numbers_for_all_paragraph_names()
```

Observed calls (lexical order): `CursorNameResolver`, `resolver.cursor_spec`.

### `test_release_validator_catches_stale_perform_after_renumbering` - L25-L47

```python
test_release_validator_catches_stale_perform_after_renumbering()
```

Observed calls (lexical order): `validate_generated_cobol`, `text.replace`, `any`.

### `test_release_validator_catches_mismatched_sql_location` - L50-L61

```python
test_release_validator_catches_mismatched_sql_location()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_span_loop_planner_uses_four_digit_cursor_offsets_and_keeps_legacy_compatibility` - L64-L93

```python
test_span_loop_planner_uses_four_digit_cursor_offsets_and_keeps_legacy_compatibility()
```

Observed calls (lexical order): `LoopShapeScanner`, `scanner.scan`, `SpanLoopPlanBuilder`, `SpanLoopPlanBuilder(scanner=scanner).build`, `len`.

### `test_release_validator_rejects_reversed_perform_thru_range` - L96-L106

```python
test_release_validator_rejects_reversed_perform_thru_range()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_release_validator_rejects_business_thru_range_crossing_cursor_paragraphs` - L109-L125

```python
test_release_validator_rejects_business_thru_range_crossing_cursor_paragraphs()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_release_validator_ignores_terminators_when_indexing_paragraphs` - L128-L140

```python
test_release_validator_ignores_terminators_when_indexing_paragraphs()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_release_validator_checks_multiline_perform_thru_ranges` - L143-L155

```python
test_release_validator_checks_multiline_perform_thru_ranges()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_release_validator_rejects_duplicate_business_paragraph_labels` - L158-L168

```python
test_release_validator_rejects_duplicate_business_paragraph_labels()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_release_validator_enforces_global_cursor_identity_numbering` - L171-L209

```python
test_release_validator_enforces_global_cursor_identity_numbering()
```

Observed calls (lexical order): `validate_generated_cobol`, `text.replace`, `incorrect.replace`, `any`.

### `test_cursor_four_and_later_continue_in_three_hundred_number_blocks` - L212-L214

```python
test_cursor_four_and_later_continue_in_three_hundred_number_blocks()
```

Observed calls (lexical order): `cursor_paragraph_number`.

### `test_cursor_paragraph_generator_emits_standard_multi_cursor_output` - L217-L258

```python
test_cursor_paragraph_generator_emits_standard_multi_cursor_output()
```

Observed calls (lexical order): `CursorNameResolver`, `enumerate`, `resolver.cursor_spec`, `spec.update`, `specs.append`, `CursorParagraphGenerator`, `SqlErrorGenerator`, `generator.paragraph_block`, `validate_generated_cobol`.

Control points:

- L223: `for (order, table) in enumerate(('DZEVEFTV', 'DZBEFFTV', 'DZBFASTV'), start=1)`
- L245: `for label in expected`
- L247: `for number in (2100, 2200, 2300, 3100, 3200, 3300, 4100, 4200, 4300)`

### `test_release_validator_requires_shared_sqlerror_routing_at_every_cursor_level` - L261-L327

```python
test_release_validator_requires_shared_sqlerror_routing_at_every_cursor_level()
```

Observed calls (lexical order): `issue.code.startswith`, `validate_generated_cobol`, `source.replace`, `source.replace('WHEN OTHER PERFORM SQLERROR\n END-EVALUATE.\n 3300-CLOSE-C2.', 'WHEN OTHER CONTINUE\n END-E...`.

### `test_access_error_policy_distinguishes_cursor_singleton_and_lr_outcomes` - L330-L341

```python
test_access_error_policy_distinguishes_cursor_singleton_and_lr_outcomes()
```

Observed calls (lexical order): `classify_access`, `policy_for`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
