# `tests/test_lr_access_analyser.py`

Source: [tests/test_lr_access_analyser.py](../../../tests/test_lr_access_analyser.py) | 919 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `c3c6fa5ff11c08ab6c71a5b7ab81545c89cdcb4f2673d95e0d534d82bdff6814`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.lr_access.lr_access_analyser import LrAccessAnalyser
from pathlib import Path
```

## Local dependency notes

- [converter/analyzers/lr_access/lr_access_analyser.py](../converter/analyzers/lr_access/lr_access_analyser.md)

## Symbol contracts and control points

### `test_classifies_inline_bounded_search_without_program_specific_names` - L4-L18

```python
test_classifies_inline_bounded_search_without_program_specific_names()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_does_not_classify_status_only_sweep_as_bounded_search` - L21-L28

```python
test_does_not_classify_status_only_sweep_as_bounded_search()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`.

### `test_ambiguous_multiple_sites_for_same_record_are_omitted` - L31-L45

```python
test_ambiguous_multiple_sites_for_same_record_are_omitted()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_refuses_to_classify_loop_with_business_work` - L48-L57

```python
test_refuses_to_classify_loop_with_business_work()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`.

### `test_real_vm4bd310_source_is_classified_without_hardcoded_program_rule` - L60-L66

```python
test_real_vm4bd310_source_is_classified_without_hardcoded_program_rule()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `LrAccessAnalyser`, `analyser.bounded_searches`, `source_path.read_text`, `result.get`.

### `test_paragraph_and_thru_lrf_loops_are_reported_but_never_classified_for_rewrite` - L69-L76

```python
test_paragraph_and_thru_lrf_loops_are_reported_but_never_classified_for_rewrite()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_nested_inline_loop_is_not_misclassified_from_partial_scope` - L79-L90

```python
test_nested_inline_loop_is_not_misclassified_from_partial_scope()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_numeric_paragraph_loop_with_lrf_access_is_reported_even_when_until_is_eof` - L93-L108

```python
test_numeric_paragraph_loop_with_lrf_access_is_reported_even_when_until_is_eof()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_numeric_paragraph_through_loop_is_reported_without_rewrite` - L111-L121

```python
test_numeric_paragraph_through_loop_is_reported_without_rewrite()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_outer_eof_loop_follows_nested_perform_calls_to_find_lrf_access` - L124-L135

```python
test_outer_eof_loop_follows_nested_perform_calls_to_find_lrf_access()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_refuses_bounded_search_when_store_precedes_next_access` - L138-L147

```python
test_refuses_bounded_search_when_store_precedes_next_access()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`.

### `test_vmdz1526_lrf_intermediate_reports_outer_eof_loop_that_calls_lrf_work` - L150-L162

```python
test_vmdz1526_lrf_intermediate_reports_outer_eof_loop_that_calls_lrf_work()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `LrAccessAnalyser`, `analyser.bounded_searches`, `source_path.read_text`, `any`.

### `test_paragraph_scanner_keeps_same_line_statement_after_paragraph_label` - L165-L175

```python
test_paragraph_scanner_keeps_same_line_statement_after_paragraph_label()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_paragraph_scanner_does_not_treat_program_id_as_a_paragraph` - L178-L190

```python
test_paragraph_scanner_does_not_treat_program_id_as_a_paragraph()
```

Observed calls (lexical order): `LrAccessAnalyser._paragraph_bodies`, `LrAccessAnalyser._logical_text`.

### `test_paragraph_scanner_does_not_split_on_end_exec_terminator` - L193-L204

```python
test_paragraph_scanner_does_not_split_on_end_exec_terminator()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_paragraph_scanner_ignores_lrf_and_perform_words_inside_literals` - L207-L216

```python
test_paragraph_scanner_ignores_lrf_and_perform_words_inside_literals()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_inline_comment_words_do_not_create_lrf_access_or_paragraph_calls` - L219-L228

```python
test_inline_comment_words_do_not_create_lrf_access_or_paragraph_calls()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_inline_comment_marker_inside_quoted_literal_is_preserved` - L231-L240

```python
test_inline_comment_marker_inside_quoted_literal_is_preserved()
```

Observed calls (lexical order): `LrAccessAnalyser._logical_text`, `LrAccessAnalyser`, `analyser.bounded_searches`.

### `test_inline_comment_after_real_lrf_statement_preserves_statement` - L243-L252

```python
test_inline_comment_after_real_lrf_statement_preserves_statement()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_finite_perform_through_with_lrf_access_is_reported_for_review` - L255-L270

```python
test_finite_perform_through_with_lrf_access_is_reported_for_review()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_through_in_comment_does_not_trigger_paragraph_diagnostic` - L273-L283

```python
test_through_in_comment_does_not_trigger_paragraph_diagnostic()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_paragraph_modify_without_obtain_is_still_reported_for_review` - L286-L298

```python
test_paragraph_modify_without_obtain_is_still_reported_for_review()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_inline_perform_varying_is_not_misread_as_paragraph_call` - L301-L315

```python
test_inline_perform_varying_is_not_misread_as_paragraph_call()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_unresolved_thru_endpoint_is_explicitly_flagged_when_lrf_is_present` - L318-L332

```python
test_unresolved_thru_endpoint_is_explicitly_flagged_when_lrf_is_present()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_reversed_thru_range_is_explicitly_flagged` - L335-L350

```python
test_reversed_thru_range_is_explicitly_flagged()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_inline_perform_times_is_not_misread_as_paragraph_call` - L353-L365

```python
test_inline_perform_times_is_not_misread_as_paragraph_call()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_paragraph_erase_without_obtain_is_reported_for_review` - L368-L381

```python
test_paragraph_erase_without_obtain_is_reported_for_review()
```

ERASE-only paragraph flows are LRF work even without OBTAIN/NEXT.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_erase_in_literal_does_not_trigger_paragraph_diagnostic` - L384-L393

```python
test_erase_in_literal_does_not_trigger_paragraph_diagnostic()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_fixed_format_continuation_does_not_merge_perform_and_paragraph_tokens` - L396-L408

```python
test_fixed_format_continuation_does_not_merge_perform_and_paragraph_tokens()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_nested_unresolved_thru_range_keeps_enclosing_lrf_flow_for_review` - L411-L432

```python
test_nested_unresolved_thru_range_keeps_enclosing_lrf_flow_for_review()
```

An unresolved nested THRU must not be reduced to its first paragraph.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_nested_unresolved_paragraph_call_is_not_silently_ignored` - L435-L452

```python
test_nested_unresolved_paragraph_call_is_not_silently_ignored()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_inline_varying_loop_following_paragraph_call_detects_indirect_lrf_access` - L455-L469

```python
test_inline_varying_loop_following_paragraph_call_detects_indirect_lrf_access()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_inline_times_loop_with_nested_perform_calls_and_lrf_is_detected` - L472-L485

```python
test_inline_times_loop_with_nested_perform_calls_and_lrf_is_detected()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_inline_loop_nested_scope_does_not_hide_outer_paragraph_call` - L488-L504

```python
test_inline_loop_nested_scope_does_not_hide_outer_paragraph_call()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_paragraph_call_detects_obtain_owner_form` - L507-L520

```python
test_paragraph_call_detects_obtain_owner_form()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_paragraph_call_detects_direct_obtain_and_set_membership_side_effects` - L523-L537

```python
test_paragraph_call_detects_direct_obtain_and_set_membership_side_effects()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_obtain_owner_inside_literal_does_not_create_false_paragraph_access` - L540-L549

```python
test_obtain_owner_inside_literal_does_not_create_false_paragraph_access()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_paragraph_find_access_is_reported_for_review` - L552-L565

```python
test_paragraph_find_access_is_reported_for_review()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_find_words_inside_literal_do_not_trigger_paragraph_review` - L568-L577

```python
test_find_words_inside_literal_do_not_trigger_paragraph_review()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_duplicate_paragraph_names_union_bodies_for_conservative_lrf_detection` - L580-L599

```python
test_duplicate_paragraph_names_union_bodies_for_conservative_lrf_detection()
```

A later duplicate label must not overwrite an earlier LRF-bearing body.

Observed calls (lexical order): `LrAccessAnalyser._logical_text`, `LrAccessAnalyser._paragraph_bodies`, `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_thru_range_keeps_duplicate_named_paragraphs_in_physical_order` - L602-L621

```python
test_thru_range_keeps_duplicate_named_paragraphs_in_physical_order()
```

A duplicate label inside a THRU range must not disappear from the range.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_thru_range_with_duplicate_endpoint_is_flagged_as_ambiguous` - L624-L641

```python
test_thru_range_with_duplicate_endpoint_is_flagged_as_ambiguous()
```

A name-only THRU endpoint repeated in the source cannot be resolved safely.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_unmatched_nested_inline_perform_does_not_hide_lrf_access` - L644-L658

```python
test_unmatched_nested_inline_perform_does_not_hide_lrf_access()
```

A single END-PERFORM closes the inner scope, not the outer scope.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_unresolved_perform_target_is_not_assumed_free_of_lrf_access` - L661-L675

```python
test_unresolved_perform_target_is_not_assumed_free_of_lrf_access()
```

A missing paragraph/section target cannot be proven side-effect free.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_nested_unresolved_perform_target_keeps_outer_lrf_control_flow_for_review` - L678-L696

```python
test_nested_unresolved_perform_target_keeps_outer_lrf_control_flow_for_review()
```

An unresolved nested PERFORM must conservatively taint its caller.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_perform_section_with_direct_lrf_access_is_resolved_and_flagged` - L699-L717

```python
test_perform_section_with_direct_lrf_access_is_resolved_and_flagged()
```

A section target is a real callable scope, not an unresolved paragraph.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_perform_section_follows_nested_paragraph_call_to_lrf_access` - L720-L739

```python
test_perform_section_follows_nested_paragraph_call_to_lrf_access()
```

Section call-graph traversal must include paragraphs called by that section.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_duplicate_performed_section_name_is_ambiguous_and_kept_for_review` - L742-L761

```python
test_duplicate_performed_section_name_is_ambiguous_and_kept_for_review()
```

Repeated section names must not resolve to an arbitrary section body.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_name_only_perform_to_duplicate_paragraph_is_explicitly_ambiguous` - L764-L782

```python
test_name_only_perform_to_duplicate_paragraph_is_explicitly_ambiguous()
```

Unioning duplicate bodies prevents missed access but cannot resolve a call target.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_duplicate_paragraph_target_without_visible_access_is_still_reviewed` - L785-L803

```python
test_duplicate_paragraph_target_without_visible_access_is_still_reviewed()
```

A duplicate call target is ambiguous even when neither body exposes an LRF verb.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_procedure_copybook_keeps_unresolved_perform_target_on_review_path` - L806-L823

```python
test_procedure_copybook_keeps_unresolved_perform_target_on_review_path()
```

An access hidden in a procedure copybook must not be assumed absent.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_data_division_copybook_alone_does_not_enable_procedure_unknown_target_diagnostics` - L826-L838

```python
test_data_division_copybook_alone_does_not_enable_procedure_unknown_target_diagnostics()
```

A data declaration COPY should not create a false procedure-flow warning.

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`.

### `test_copy_text_inside_procedure_literal_is_not_treated_as_copy_statement` - L841-L851

```python
test_copy_text_inside_procedure_literal_is_not_treated_as_copy_statement()
```

Observed calls (lexical order): `LrAccessAnalyser._has_procedure_copy`, `LrAccessAnalyser._logical_text`, `LrAccessAnalyser`, `analyser.bounded_searches`.

### `test_supplied_procedure_copybook_is_expanded_for_control_flow_analysis_only` - L854-L873

```python
test_supplied_procedure_copybook_is_expanded_for_control_flow_analysis_only()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_nested_procedure_copybooks_are_expanded_recursively` - L876-L890

```python
test_nested_procedure_copybooks_are_expanded_recursively()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_unresolved_procedure_copybook_is_reported_explicitly` - L893-L905

```python
test_unresolved_procedure_copybook_is_reported_explicitly()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

### `test_procedure_copy_replacing_is_not_expanded_with_unmodified_text` - L908-L919

```python
test_procedure_copy_replacing_is_not_expanded_with_unmodified_text()
```

Observed calls (lexical order): `LrAccessAnalyser`, `analyser.bounded_searches`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
