# `tests/test_generic_scope_and_reference_v129.py`

Source: [tests/test_generic_scope_and_reference_v129.py](../../../tests/test_generic_scope_and_reference_v129.py) | 110 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `15e8d3598895db0f561be61a1eeb078de7de2d3d612306657a98ed8b7eedfb53`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.domain.models import SheetMappingRow, DclgenColumn
from converter.repositories.mapping_repository import MappingRepository
from converter.repositories.dclgen_repository import DclgenRepository
from converter.transformers.field_reference_rewriter import FieldReferenceRewriter
from converter.services.name_normalizer import NameNormalizer
from review.checks.chk_32_scope_balance import ScopeBalanceCheck
from review.engine.cobol_view import CobolView
from review.checks.chk_29_lr_status_field_replacement import LRStatusFieldReplacementCheck
from converter.services.final_generated_output_service import FinalGeneratedOutputService
from converter.composers.db2_date_comparison_composer import Db2DateComparisonComposer
```

## Local dependency notes

- [converter/composers/db2_date_comparison_composer.py](../converter/composers/db2_date_comparison_composer.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/services/final_generated_output_service.py](../converter/services/final_generated_output_service.md)
- [converter/services/name_normalizer.py](../converter/services/name_normalizer.md)
- [converter/transformers/field_reference_rewriter.py](../converter/transformers/field_reference_rewriter.md)
- [review/checks/chk_29_lr_status_field_replacement.py](../review/checks/chk_29_lr_status_field_replacement.md)
- [review/checks/chk_32_scope_balance.py](../review/checks/chk_32_scope_balance.md)
- [review/engine/cobol_view.py](../review/engine/cobol_view.md)

## Symbol contracts and control points

### `rewriter` - L11-L19

```python
rewriter(rows)
```

Observed calls (lexical order): `NameNormalizer.normalize`, `maps.setdefault`, `row.cobol_zone.split`, `row.new_db2_field_name.replace`, `DclgenRepository`, `SimpleNamespace`, `DclgenColumn`, `FieldReferenceRewriter`, `MappingRepository`.

Control points:

- L13: `for row in rows`

### `row` - L22-L24

```python
row(record='ACCOUNT', field='BALANCE', target='AMOUNT', pic='PIC S9(7)V99 COMP-3', kind='DECIMAL(9,2)')
```

Observed calls (lexical order): `SheetMappingRow`.

### `test_unique_scalar_without_active_record_and_literal_safety` - L27-L33

```python
test_unique_scalar_without_active_record_and_literal_safety()
```

Observed calls (lexical order): `rewriter`, `row`, `obj.rewrite`.

### `test_ambiguous_or_local_scalar_is_not_guessed` - L36-L40

```python
test_ambiguous_or_local_scalar_is_not_guessed()
```

Observed calls (lexical order): `rewriter`, `rewriter([row(), row(record='OTHER', target='OTHER_AMT')]).rewrite`, `row`, `rewriter([row()]).rewrite`.

### `test_date_only_qualifies_comparisons_with_proven_date_host` - L43-L48

```python
test_date_only_qualifies_comparisons_with_proven_date_host()
```

Observed calls (lexical order): `rewriter`, `row`, `obj.rewrite`.

### `test_period_closes_implicit_if_but_later_end_if_is_orphan` - L51-L56

```python
test_period_closes_implicit_if_but_later_end_if_is_orphan()
```

Observed calls (lexical order): `ScopeBalanceCheck`, `CobolView`, `check._walk`, `len`.

### `test_inline_scopes_comments_sql_and_decimal_points` - L59-L69

```python
test_inline_scopes_comments_sql_and_decimal_points()
```

Observed calls (lexical order): `ScopeBalanceCheck`, `CobolView`, `check._walk`.

### `test_missing_scope_is_still_reported` - L72-L74

```python
test_missing_scope_is_still_reported()
```

Observed calls (lexical order): `CobolView`, `ScopeBalanceCheck`, `ScopeBalanceCheck()._walk`.

### `test_end_of_set_review_does_not_require_eoc_for_singleton_failure_test` - L77-L81

```python
test_end_of_set_review_does_not_require_eoc_for_singleton_failure_test()
```

Observed calls (lexical order): `LRStatusFieldReplacementCheck`, `check._requires_end_of_set`.

### `test_stale_status_warning_removed_only_after_last_executable_reference` - L84-L89

```python
test_stale_status_warning_removed_only_after_last_executable_reference()
```

Observed calls (lexical order): `clean`, `clean(warning + ' DISPLAY ERROR-STATUS.\n').startswith`.

### `test_conflicting_columns_for_same_owner_are_not_guessed` - L92-L94

```python
test_conflicting_columns_for_same_owner_are_not_guessed()
```

Observed calls (lexical order): `rewriter`, `row`, `obj.rewrite`.

### `test_date_comparison_pass_runs_again_after_host_qualification` - L97-L110

```python
test_date_comparison_pass_runs_again_after_host_qualification()
```

Observed calls (lexical order): `Db2DateComparisonComposer`, `composer.compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
