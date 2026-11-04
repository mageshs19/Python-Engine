# `tests/test_business_parity_review_rules_v128.py`

Source: [tests/test_business_parity_review_rules_v128.py](../../../tests/test_business_parity_review_rules_v128.py) | 133 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `7168cd42a377420dfa68aad0dc258cc1b9652d81ec21f216e012c0f38e77321f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from review.checks.chk_15_nested_cursor_processing import NestedCursorProcessingCheck
from review.checks.chk_25_copybook_and_record_usage import CopybookAndRecordUsageCheck
from review.engine.cobol_view import CobolView
from review.engine.context import ReviewContext
```

## Local dependency notes

- [review/checks/chk_15_nested_cursor_processing.py](../review/checks/chk_15_nested_cursor_processing.md)
- [review/checks/chk_25_copybook_and_record_usage.py](../review/checks/chk_25_copybook_and_record_usage.md)
- [review/engine/cobol_view.py](../review/engine/cobol_view.md)
- [review/engine/context.py](../review/engine/context.md)

## Symbol contracts and control points

### `_mapping` - L9-L16

```python
_mapping(record, source, target)
```

Observed calls (lexical order): `SimpleNamespace`.

### `test_child_early_stop_is_not_inferred_from_unrelated_generated_y_flag` - L19-L25

```python
test_child_early_stop_is_not_inferred_from_unrelated_generated_y_flag()
```

Observed calls (lexical order): `ReviewContext`, `NestedCursorProcessingCheck._source_requires_business_early_stop`.

### `test_compound_source_traversal_requires_business_early_stop` - L28-L37

```python
test_compound_source_traversal_requires_business_early_stop()
```

Observed calls (lexical order): `ReviewContext`, `NestedCursorProcessingCheck._source_requires_business_early_stop`.

### `test_unmaterialised_mapped_legacy_field_is_reported` - L40-L61

```python
test_unmaterialised_mapped_legacy_field_is_reported()
```

Observed calls (lexical order): `ReviewContext`, `_mapping`, `CobolView`, `CopybookAndRecordUsageCheck._unmaterialised_legacy_fields`.

### `test_materialised_or_declared_legacy_name_is_not_reported` - L64-L86

```python
test_materialised_or_declared_legacy_name_is_not_reported()
```

Observed calls (lexical order): `ReviewContext`, `_mapping`, `CobolView`, `CopybookAndRecordUsageCheck._unmaterialised_legacy_fields`.

### `test_ambiguous_legacy_field_is_not_guessed` - L89-L106

```python
test_ambiguous_legacy_field_is_not_guessed()
```

Observed calls (lexical order): `ReviewContext`, `_mapping`, `CobolView`, `CopybookAndRecordUsageCheck._unmaterialised_legacy_fields`, `set`.

### `test_declared_materialised_idms_record_group_is_not_residual_qualifier` - L109-L121

```python
test_declared_materialised_idms_record_group_is_not_residual_qualifier()
```

Observed calls (lexical order): `sorted`.

### `test_undeclared_legacy_record_group_still_counts_as_residual` - L124-L133

```python
test_undeclared_legacy_record_group_still_counts_as_residual()
```

Observed calls (lexical order): `set`, `sorted`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
