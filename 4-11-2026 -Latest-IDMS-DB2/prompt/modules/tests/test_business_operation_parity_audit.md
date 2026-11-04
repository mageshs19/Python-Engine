# `tests/test_business_operation_parity_audit.py`

Source: [tests/test_business_operation_parity_audit.py](../../../tests/test_business_operation_parity_audit.py) | 610 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `52f9a01059a40bbadfdb1e16fa4c27a8a110d8ae36bbef83903efed7d420c8de`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.program_flow.business_operation_parity_audit import BusinessOperationParityAuditor
import csv
```

## Local dependency notes

- [converter/analyzers/program_flow/business_operation_parity_audit.py](../converter/analyzers/program_flow/business_operation_parity_audit.md)

## Symbol contracts and control points

### `test_all_idms_dml_families_require_db2_counterparts` - L6-L23

```python
test_all_idms_dml_families_require_db2_counterparts()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`, `len`.

### `test_comments_and_literals_do_not_create_source_operations` - L26-L40

```python
test_comments_and_literals_do_not_create_source_operations()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`.

### `test_cursorized_reads_count_as_select_coverage_without_count_matching` - L43-L56

```python
test_cursorized_reads_count_as_select_coverage_without_count_matching()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`, `len`.

### `test_per_operation_audit_checks_the_mapped_db2_table` - L59-L76

```python
test_per_operation_audit_checks_the_mapped_db2_table(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `'Cobol Recrd IDMS,New DB2 Record \\nCUSTOMER,DZCUSTTB \\n'.replace`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`.

### `test_per_operation_audit_accepts_mapping_to_db2_table` - L79-L94

```python
test_per_operation_audit_accepts_mapping_to_db2_table(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`.

### `test_unmapped_lrf_set_operand_is_review_not_false_failure` - L97-L112

```python
test_unmapped_lrf_set_operand_is_review_not_false_failure(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `len`.

### `test_update_must_reference_every_mapped_primary_key` - L115-L138

```python
test_update_must_reference_every_mapped_primary_key(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `len`.

### `test_lrf_where_keyword_resolves_logical_record_for_table_audit` - L141-L162

```python
test_lrf_where_keyword_resolves_logical_record_for_table_audit(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `dclgen.mkdir`, `(dclgen / 'DZEVEFTV.txt').write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping, dclgen_dir=dclgen).audit`.

### `test_update_set_must_include_explicitly_changed_mapped_field` - L165-L190

```python
test_update_set_must_include_explicitly_changed_mapped_field(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`, `next`.

### `test_update_set_accepts_mapped_changed_field_and_additional_audit_columns` - L193-L214

```python
test_update_set_accepts_mapped_changed_field_and_additional_audit_columns(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`.

### `test_update_set_audit_resolves_unqualified_record_field_from_mapping` - L217-L239

```python
test_update_set_audit_resolves_unqualified_record_field_from_mapping(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`.

### `test_obtain_downstream_field_read_requires_select_projection` - L242-L262

```python
test_obtain_downstream_field_read_requires_select_projection(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_obtain_select_projection_must_include_downstream_fields` - L265-L286

```python
test_obtain_select_projection_must_include_downstream_fields(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `next`.

### `test_obtain_projection_passes_when_required_fields_are_selected` - L289-L310

```python
test_obtain_projection_passes_when_required_fields_are_selected(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `issue.code.startswith`.

### `test_transaction_boundaries_require_matching_db2_sql` - L313-L326

```python
test_transaction_boundaries_require_matching_db2_sql()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`.

### `test_transaction_boundary_keywords_in_comments_and_literals_are_ignored` - L329-L340

```python
test_transaction_boundary_keywords_in_comments_and_literals_are_ignored()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`.

### `test_commit_and_rollback_are_recognized_only_inside_embedded_db2_sql` - L343-L355

```python
test_commit_and_rollback_are_recognized_only_inside_embedded_db2_sql()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`.

### `test_idms_not_found_handler_without_db2_sqlcode_100_is_reviewed` - L358-L369

```python
test_idms_not_found_handler_without_db2_sqlcode_100_is_reviewed()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`, `any`.

### `test_idms_not_found_handler_with_local_db2_when_100_is_recognized` - L372-L389

```python
test_idms_not_found_handler_with_local_db2_when_100_is_recognized(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_unrelated_sqlcode_100_does_not_satisfy_not_found_parity` - L392-L414

```python
test_unrelated_sqlcode_100_does_not_satisfy_not_found_parity(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_not_found_branch_in_later_paragraph_does_not_satisfy_select` - L417-L435

```python
test_not_found_branch_in_later_paragraph_does_not_satisfy_select(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_direct_update_replacement_requires_operation_local_affected_row_check` - L438-L458

```python
test_direct_update_replacement_requires_operation_local_affected_row_check(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_direct_update_replacement_recognizes_sqlerrd_three_guard` - L461-L480

```python
test_direct_update_replacement_recognizes_sqlerrd_three_guard(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_direct_update_row_count_mention_without_zero_guard_does_not_pass` - L483-L504

```python
test_direct_update_row_count_mention_without_zero_guard_does_not_pass(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_select_and_update_for_mapped_table_is_not_misclassified_as_direct_update_replacement` - L507-L533

```python
test_select_and_update_for_mapped_table_is_not_misclassified_as_direct_update_replacement(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_direct_update_without_mapped_select_still_requires_zero_row_review` - L536-L556

```python
test_direct_update_without_mapped_select_still_requires_zero_row_review(tmp_path)
```

Observed calls (lexical order): `mapping.write_text`, `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor(mapping_csv=mapping).audit`, `any`.

### `test_physical_write_is_required_independently_of_db2_select` - L559-L572

```python
test_physical_write_is_required_independently_of_db2_select()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`, `any`.

### `test_same_name_business_paragraph_cannot_silently_become_display_only` - L575-L594

```python
test_same_name_business_paragraph_cannot_silently_become_display_only()
```

Observed calls (lexical order): `BusinessOperationParityAuditor`, `BusinessOperationParityAuditor().audit`, `any`, `target.replace`.

### `test_tab_export_populates_all_semantic_mapping_indexes` - L597-L610

```python
test_tab_export_populates_all_semantic_mapping_indexes(tmp_path)
```

Observed calls (lexical order): `mapping.open`, `csv.writer`, `writer.writerow`, `BusinessOperationParityAuditor`, `auditor.audit`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
