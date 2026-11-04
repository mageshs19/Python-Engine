# `tests/test_ai_standardized_reference_audit.py`

Source: [tests/test_ai_standardized_reference_audit.py](../../../tests/test_ai_standardized_reference_audit.py) | 59 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `678ff385555a7b26cff797407d7a45934c21f939dcedf60c1b6f45b3edd2287d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
from runners.audit_ai_standardized_reference import build_report, inspect_program, latest_python_output, normalized_diff_counts
import os
```

## Local dependency notes

- [runners/audit_ai_standardized_reference.py](../runners/audit_ai_standardized_reference.md)

## Symbol contracts and control points

### `test_latest_output_uses_filename_timestamp_not_file_mtime` - L11-L21

```python
test_latest_output_uses_filename_timestamp_not_file_mtime(tmp_path: Path)
```

Observed calls (lexical order): `output.mkdir`, `older.write_text`, `newer.write_text`, `newer.stat`, `os.utime`, `latest_python_output`.

### `test_inspector_reports_sql_infrastructure_and_cursor_operations` - L24-L43

```python
test_inspector_reports_sql_infrastructure_and_cursor_operations(tmp_path: Path)
```

Observed calls (lexical order): `path.write_text`, `'\n'.join`, `enumerate`, `inspect_program`.

### `test_diff_counter_ignores_sequence_number_changes` - L46-L50

```python
test_diff_counter_ignores_sequence_number_changes()
```

Observed calls (lexical order): `normalized_diff_counts`.

### `test_project_report_keeps_v6_as_advisory_not_authoritative` - L53-L59

```python
test_project_report_keeps_v6_as_advisory_not_authoritative()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `build_report`, `len`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
