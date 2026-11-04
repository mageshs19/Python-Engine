# `tests/test_lrf_update_changed_column_scope.py`

Source: [tests/test_lrf_update_changed_column_scope.py](../../../tests/test_lrf_update_changed_column_scope.py) | 81 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `78e7babf29a424c9d0736dcc41bd93560fd2115b1bed3b431f2e2f817a844d98`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from types import SimpleNamespace
from converter.composers.update_sql_cleanup.modify_update_rewriter import ModifyUpdateRewriter
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](../converter/composers/update_sql_cleanup/modify_update_rewriter.md)

## Symbol contracts and control points

### `_rewriter` - L11-L20

```python
_rewriter()
```

Observed calls (lexical order): `SimpleNamespace`, `line[7:72].strip`, `len`, `line[:6].strip`, `line[:6].strip().isdigit`, `str`, `str(line or '').strip`, `re.compile`, `ModifyUpdateRewriter`, `object`.

### `test_lrf_modify_marker_is_detected_without_program_name_hardcoding` - L23-L31

```python
test_lrf_modify_marker_is_detected_without_program_name_hardcoding()
```

Observed calls (lexical order): `_rewriter`, `rewriter._is_lrf_expanded_modify`.

### `test_lrf_update_scan_uses_full_paragraph_instead_of_last_20_lines` - L34-L51

```python
test_lrf_update_scan_uses_full_paragraph_instead_of_last_20_lines()
```

Observed calls (lexical order): `_rewriter`, `lines.extend`, `range`, `lines.append`, `len`, `rewriter._is_lrf_expanded_modify`, `rewriter._post_select_scan_start`, `max`.

### `test_lrf_update_scan_stops_at_latest_sql_boundary_in_paragraph` - L54-L69

```python
test_lrf_update_scan_stops_at_latest_sql_boundary_in_paragraph()
```

Observed calls (lexical order): `_rewriter`, `rewriter._post_select_scan_start`, `len`.

### `test_lrf_provenance_detection_supports_fixed_format_comment_indicators` - L72-L81

```python
test_lrf_provenance_detection_supports_fixed_format_comment_indicators()
```

Observed calls (lexical order): `_rewriter`, `rewriter._is_lrf_expanded_modify`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
