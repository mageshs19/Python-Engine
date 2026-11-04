# `tests/test_output_write_placement_cleanup.py`

Source: [tests/test_output_write_placement_cleanup.py](../../../tests/test_output_write_placement_cleanup.py) | 372 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `0826b97aa2edc08de8804fdd4a947d630b04e800183099f6c952abcf9bb38657`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.output_write_placement_cleanup import OutputWritePlacementCleanup
from converter.composers.cleanup.child_fetch_early_stop_cleanup import ChildFetchEarlyStopCleanup
from converter.composers.cleanup.cursor_nesting_analyser import CursorNestingAnalyser
```

## Local dependency notes

- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](../converter/composers/cleanup/child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/cleanup_message_collector.py](../converter/composers/cleanup/cleanup_message_collector.md)
- [converter/composers/cleanup/cursor_nesting_analyser.py](../converter/composers/cleanup/cursor_nesting_analyser.md)
- [converter/composers/cleanup/output_write_placement_cleanup.py](../converter/composers/cleanup/output_write_placement_cleanup.md)

## Symbol contracts and control points

### `_nested_parent_child_program` - L7-L42

```python
_nested_parent_child_program() -> str
```

Use four-digit cursor numbers so numeric thresholds cannot infer depth.

### `test_write_moves_after_child_close_not_after_parent_close` - L45-L70

```python
test_write_moves_after_child_close_not_after_parent_close()
```

Observed calls (lexical order): `CleanupMessageCollector`, `OutputWritePlacementCleanup`, `cleanup.move_output_write_after_child_loop`, `_nested_parent_child_program`, `result.index`, `result.count`, `any`.

### `test_nested_cursor_parent_is_not_reclassified_as_child_row_paragraph` - L73-L87

```python
test_nested_cursor_parent_is_not_reclassified_as_child_row_paragraph()
```

Observed calls (lexical order): `CleanupMessageCollector`, `OutputWritePlacementCleanup`, `cleanup.move_output_write_after_child_loop`, `_nested_parent_child_program`, `result.index`.

### `test_early_stop_targets_nested_cursor_not_paragraph_number` - L90-L112

```python
test_early_stop_targets_nested_cursor_not_paragraph_number()
```

Observed calls (lexical order): `CleanupMessageCollector`, `ChildFetchEarlyStopCleanup`, `_nested_parent_child_program`, `_nested_parent_child_program().replace`, `_nested_parent_child_program().replace("PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'...`, `cleanup.ensure_child_fetch_early_stop`.

### `test_nested_child_without_reachable_yes_assignment_does_not_get_early_stop` - L115-L131

```python
test_nested_child_without_reachable_yes_assignment_does_not_get_early_stop()
```

Observed calls (lexical order): `_nested_parent_child_program`, `_nested_parent_child_program().replace`, `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`.

### `test_single_cursor_never_gets_shared_child_early_stop_condition` - L134-L165

```python
test_single_cursor_never_gets_shared_child_early_stop_condition()
```

Observed calls (lexical order): `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`.

### `test_nested_cursor_classification_is_independent_of_numbering_scheme` - L168-L180

```python
test_nested_cursor_classification_is_independent_of_numbering_scheme()
```

Observed calls (lexical order): `_nested_parent_child_program`, `source.replace`, `source.replace('2100-', '710-').replace`, `source.replace('2100-', '710-').replace('2200-', '720-').replace`, `source.replace('3100-', '810-').replace`, `source.replace('3100-', '810-').replace('3200-', '820-').replace`, `source.splitlines`, `CursorNestingAnalyser`, `analyser.is_nested_fetch`.

### `test_child_flag_reset_is_not_borrowed_from_previous_paragraph` - L183-L209

```python
test_child_flag_reset_is_not_borrowed_from_previous_paragraph()
```

Observed calls (lexical order): `_nested_parent_child_program`, `source.replace`, `source.replace("PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'.", 'PERFORM 3200-FETCH-...`, `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`, `result.split`, `result.split('HOOFDVERWERKING.', 1)[1].split`.

### `test_child_flag_is_reset_again_after_a_previous_child_loop` - L212-L233

```python
test_child_flag_is_reset_again_after_a_previous_child_loop()
```

Observed calls (lexical order): `_nested_parent_child_program`, `_nested_parent_child_program().replace`, `_nested_parent_child_program().replace("PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'...`, `source.replace`, `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`, `result.count`.

### `test_child_flag_reset_is_repeated_after_intervening_perform_call` - L237-L260

```python
test_child_flag_reset_is_repeated_after_intervening_perform_call()
```

Observed calls (lexical order): `_nested_parent_child_program`, `_nested_parent_child_program().replace`, `_nested_parent_child_program().replace("PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'...`, `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`, `result.index`, `preceding.rstrip`, `preceding.rstrip().endswith`, `preceding.count`.

### `_business_paragraph_driven_nested_cursor_program` - L263-L302

```python
_business_paragraph_driven_nested_cursor_program() -> str
```

VMDZ4420-style loop: business paragraph performs the next child FETCH.

### `test_business_paragraph_loop_preserves_sw_status_d_early_stop` - L305-L319

```python
test_business_paragraph_loop_preserves_sw_status_d_early_stop()
```

Observed calls (lexical order): `_business_paragraph_driven_nested_cursor_program`, `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`, `result.index`.

### `test_business_paragraph_loop_does_not_add_flag_without_business_assignment` - L322-L335

```python
test_business_paragraph_loop_does_not_add_flag_without_business_assignment()
```

Observed calls (lexical order): `_business_paragraph_driven_nested_cursor_program`, `_business_paragraph_driven_nested_cursor_program().replace`, `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`.

### `test_business_stop_flag_is_discovered_from_logic_not_its_name` - L338-L360

```python
test_business_stop_flag_is_discovered_from_logic_not_its_name()
```

A differently named business flag gets the same proven loop treatment.

Observed calls (lexical order): `_nested_parent_child_program`, `_nested_parent_child_program().replace`, `_nested_parent_child_program().replace("PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR SW-STATUS-D = 'Y'...`, `ChildFetchEarlyStopCleanup`, `ChildFetchEarlyStopCleanup(CleanupMessageCollector()).ensure_child_fetch_early_stop`, `CleanupMessageCollector`.

### `test_output_guard_uses_the_flag_found_in_the_child_loop` - L363-L372

```python
test_output_guard_uses_the_flag_found_in_the_child_loop()
```

Observed calls (lexical order): `_nested_parent_child_program`, `_nested_parent_child_program().replace`, `OutputWritePlacementCleanup`, `OutputWritePlacementCleanup(CleanupMessageCollector()).move_output_write_after_child_loop`, `CleanupMessageCollector`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
