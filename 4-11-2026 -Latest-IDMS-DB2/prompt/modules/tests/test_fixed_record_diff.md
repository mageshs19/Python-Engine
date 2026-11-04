# `tests/test_fixed_record_diff.py`

Source: [tests/test_fixed_record_diff.py](../../../tests/test_fixed_record_diff.py) | 63 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `fbbda858e67ba85dcb9657bf9e7183c411381e2f0928e76df6f9571d7e063efc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
import pytest
from mainframe.verification.fixed_record_diff import compare, main
```

## Local dependency notes

- [mainframe/verification/fixed_record_diff.py](../mainframe/verification/fixed_record_diff.md)

## Symbol contracts and control points

### `_files` - L6-L10

```python
_files(tmp_path: Path, a: bytes, b: bytes)
```

Observed calls (lexical order): `m.write_bytes`, `g.write_bytes`.

### `test_equal_bytes_and_order` - L13-L16

```python
test_equal_bytes_and_order(tmp_path)
```

Observed calls (lexical order): `_files`, `compare`.

### `test_changed_content_reports_byte_and_record` - L19-L23

```python
test_changed_content_reports_byte_and_record(tmp_path)
```

Observed calls (lexical order): `_files`, `compare`.

### `test_order_is_a_semantic_difference` - L26-L28

```python
test_order_is_a_semantic_difference(tmp_path)
```

Observed calls (lexical order): `_files`, `compare`.

### `test_record_count_mismatch` - L31-L33

```python
test_record_count_mismatch(tmp_path)
```

Observed calls (lexical order): `_files`, `compare`.

### `test_reject_vb_or_text_newlines` - L36-L38

```python
test_reject_vb_or_text_newlines(tmp_path)
```

Observed calls (lexical order): `_files`, `compare`.

### `test_empty_both_is_equal_but_requires_external_selection_proof` - L41-L43

```python
test_empty_both_is_equal_but_requires_external_selection_proof(tmp_path)
```

Observed calls (lexical order): `_files`, `compare`.

### `test_filler_byte_changes_are_reported` - L46-L50

```python
test_filler_byte_changes_are_reported(tmp_path)
```

Observed calls (lexical order): `_files`, `compare`.

### `test_same_file_is_rejected` - L53-L56

```python
test_same_file_is_rejected(tmp_path)
```

Observed calls (lexical order): `_files`, `pytest.raises`, `compare`.

### `test_cli_nonzero_on_mismatch` - L59-L63

```python
test_cli_nonzero_on_mismatch(tmp_path)
```

Observed calls (lexical order): `_files`, `main`, `str`, `out.read_text`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
