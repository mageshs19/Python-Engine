# `tests/test_review_kind_wiring.py`

Source: [tests/test_review_kind_wiring.py](../../../tests/test_review_kind_wiring.py) | 85 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `3074e21eb50eceb7f7d54c35880f501918246345cd59ad555827dfc95828e933`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The batch review path must resolve kind PER PROGRAM.

## Module-level bindings

`UPDATE_CBL` (L16), `RETRIEVAL_CBL` (L22), `AUDIT_HOST_CBL` (L28)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from review.engine.context import KIND_RETRIEVAL, KIND_UNKNOWN, KIND_UPDATE
from review.runner.review_file import build_context, describe_kinds
```

## Local dependency notes

- [review/engine/context.py](../review/engine/context.md)
- [review/runner/review_file.py](../review/runner/review_file.md)

## Symbol contracts and control points

### `_write` - L37-L40

```python
_write(tmp_path: Path, name: str, text: str) -> Path
```

Observed calls (lexical order): `path.write_text`.

### `test_unknown_kind_is_detected_per_program` - L43-L46

```python
test_unknown_kind_is_detected_per_program(tmp_path: Path) -> None
```

Observed calls (lexical order): `_write`, `build_context`.

### `test_two_files_in_one_run_get_different_kinds` - L49-L54

```python
test_two_files_in_one_run_get_different_kinds(tmp_path: Path) -> None
```

The defect: one global kind was applied to a whole folder.

Observed calls (lexical order): `_write`, `build_context`.

### `test_explicit_kind_overrides_detection` - L57-L59

```python
test_explicit_kind_overrides_detection(tmp_path: Path) -> None
```

Observed calls (lexical order): `_write`, `build_context`.

### `test_audit_host_variable_does_not_look_like_a_write` - L62-L65

```python
test_audit_host_variable_does_not_look_like_a_write(tmp_path: Path) -> None
```

TS-UPDATE-479BFAR must not promote a cursor to UPDATE.

Observed calls (lexical order): `_write`, `build_context`.

### `test_no_evidence_stays_unknown` - L68-L70

```python
test_no_evidence_stays_unknown(tmp_path: Path) -> None
```

Observed calls (lexical order): `_write`, `build_context`.

### `test_banner_summary_reports_each_kind` - L73-L80

```python
test_banner_summary_reports_each_kind(tmp_path: Path) -> None
```

Observed calls (lexical order): `_write`, `build_context`, `describe_kinds`.

### `test_banner_summary_for_one_file_is_just_the_kind` - L83-L85

```python
test_banner_summary_for_one_file_is_just_the_kind(tmp_path: Path) -> None
```

Observed calls (lexical order): `_write`, `build_context`, `describe_kinds`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
