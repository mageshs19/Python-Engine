# `tests/test_sw_status_child_fetch_driven_normalization.py`

Source: [tests/test_sw_status_child_fetch_driven_normalization.py](../../../tests/test_sw_status_child_fetch_driven_normalization.py) | 196 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e2d29dd63c04dc176742f9ac417f07d5b7e03daca3f7f12c7bb5a3e910c8ab0f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
from converter.composers.cleanup.child_fetch_early_stop_cleanup import ChildFetchEarlyStopCleanup
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.fixed_format_composer import FixedFormatComposer
```

## Local dependency notes

- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](../converter/composers/cleanup/child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/cleanup_message_collector.py](../converter/composers/cleanup/cleanup_message_collector.md)
- [converter/composers/fixed_format_composer.py](../converter/composers/fixed_format_composer.md)

## Symbol contracts and control points

### `test_sw_status_child_loop_uses_fetch_driven_business_processing` - L11-L77

```python
test_sw_status_child_loop_uses_fetch_driven_business_processing()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `source_path.read_text`, `ChildFetchEarlyStopCleanup`, `CleanupMessageCollector`, `cleanup.ensure_child_fetch_early_stop`, `cleanup._logical`, `cleanup._logical(line).strip`, `output.splitlines`, `'\n'.join`, `next`, `enumerate`, `len`, `range`, `logical_lines[i].endswith`, `logical_lines[i].upper`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

### `test_fetch_driven_normalization_preserves_program_specific_output_logic` - L80-L112

```python
test_fetch_driven_normalization_preserves_program_specific_output_logic()
```

Generic loop repair must lift the source output block, not synthesize one.

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `source_path.read_text`, `source.replace`, `ChildFetchEarlyStopCleanup`, `CleanupMessageCollector`, `cleanup.ensure_child_fetch_early_stop`, `cleanup._logical`, `cleanup._logical(line).strip`, `output.splitlines`, `'\n'.join`, `enumerate`, `next`.

### `test_fetch_driven_normalization_refuses_to_invent_missing_output_branch` - L115-L129

```python
test_fetch_driven_normalization_refuses_to_invent_missing_output_branch()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `source_path.read_text`, `source.replace`, `ChildFetchEarlyStopCleanup`, `CleanupMessageCollector`, `cleanup._normalize_sw_status_child_loop`.

### `test_fetch_driven_normalization_resequences_inserted_fixed_format_lines` - L132-L171

```python
test_fetch_driven_normalization_resequences_inserted_fixed_format_lines()
```

Inserted COBOL records must not clone the anchor's sequence fields.

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `source_path.read_text`, `ChildFetchEarlyStopCleanup`, `CleanupMessageCollector`, `FixedFormatComposer`, `FixedFormatComposer().format`, `cleanup.ensure_child_fetch_early_stop`, `formatter.validate_fixed_format`, `line.strip`, `output.splitlines`, `int`, `len`, `set`, `all`, `zip`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

### `test_child_fetch_semantic_rewrite_does_not_run_global_formatter` - L174-L196

```python
test_child_fetch_semantic_rewrite_does_not_run_global_formatter(monkeypatch)
```

Semantic cleanup must not own physical layout or resequencing.

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `source_path.read_text`, `monkeypatch.setattr`, `ChildFetchEarlyStopCleanup`, `CleanupMessageCollector`, `cleanup.ensure_child_fetch_early_stop`, `'\n'.join`, `cleanup._logical`, `cleanup._logical(line).strip`, `output.splitlines`.

### `test_child_fetch_semantic_rewrite_does_not_run_global_formatter.forbidden_format` - L187-L188

```python
forbidden_format(*args, **kwargs)
```

Observed calls (lexical order): `AssertionError`.

Explicit raises: `AssertionError('semantic cleanup must not invoke physical formatter')`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
