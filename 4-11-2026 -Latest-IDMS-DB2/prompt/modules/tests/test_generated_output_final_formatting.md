# `tests/test_generated_output_final_formatting.py`

Source: [tests/test_generated_output_final_formatting.py](../../../tests/test_generated_output_final_formatting.py) | 196 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `f136b3c5bf456baa05ecfd7965f6dae38b905ac9ba7b8cd092f6cd6ea557a77c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.unnecessary_comments_cleanup_composer import UnnecessaryCommentsCleanupComposer
from converter.services.final_generated_output_service import FinalGeneratedOutputService
```

## Local dependency notes

- [converter/composers/unnecessary_comments_cleanup_composer.py](../converter/composers/unnecessary_comments_cleanup_composer.md)
- [converter/services/final_generated_output_service.py](../converter/services/final_generated_output_service.md)

## Symbol contracts and control points

### `_fixed` - L9-L12

```python
_fixed(body: str, seq: int=100) -> str
```

Observed calls (lexical order): `body.startswith`, `f'{seq:06d}{indicator}{source_body:<65}'[:72].ljust`.

### `_body` - L15-L16

```python
_body(line: str) -> str
```

Observed calls (lexical order): `line[7:72].rstrip`.

### `test_removes_generated_db2_narration_and_orphaned_continuations` - L19-L40

```python
test_removes_generated_db2_narration_and_orphaned_continuations()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `UnnecessaryCommentsCleanupComposer`, `composer.compose`, `_body`, `result.splitlines`, `any`.

### `test_final_output_pass_cleans_comments_and_resequences_afterward` - L43-L70

```python
test_final_output_pass_cleans_comments_and_resequences_afterward()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `FinalGeneratedOutputService`, `service.apply`, `result.splitlines`, `all`, `len`, `int`, `sorted`, `any`, `_body`.

### `test_final_output_removes_orphaned_record_label_comment_before_sql` - L73-L92

```python
test_final_output_removes_orphaned_record_label_comment_before_sql()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `_body`, `_body(line).strip`, `any`, `result.splitlines`.

### `test_final_output_removes_empty_sqlcode_guard_before_next_paragraph` - L95-L112

```python
test_final_output_removes_empty_sqlcode_guard_before_next_paragraph()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `_body`, `_body(line).strip`, `result.splitlines`.

### `test_final_output_removes_extra_filter_note_only_when_sql_consumed_it` - L115-L138

```python
test_final_output_removes_extra_filter_note_only_when_sql_consumed_it()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `any`, `result.splitlines`.

### `test_final_output_adds_sql_location_for_legacy_runtime_sql_without_one` - L141-L158

```python
test_final_output_adds_sql_location_for_legacy_runtime_sql_without_one()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `_body`, `_body(line).strip`, `result.splitlines`, `enumerate`, `next`.

### `test_final_output_removes_obsolete_conversion_breadcrumb_but_keeps_neighboring_comments` - L162-L178

```python
test_final_output_removes_obsolete_conversion_breadcrumb_but_keeps_neighboring_comments()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `_body`, `_body(line).strip`, `result.splitlines`, `any`.

### `test_lrf_error_condition_keeps_scope_over_following_stop_perform` - L181-L196

```python
test_lrf_error_condition_keeps_scope_over_following_stop_perform()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `_body`, `_body(line).strip`, `result.splitlines`, `bodies.index`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
