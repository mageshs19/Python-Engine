# `tests/test_cobol_storage_layout.py`

Source: [tests/test_cobol_storage_layout.py](../../../tests/test_cobol_storage_layout.py) | 31 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `f0782739f185273a7a45f20f4d42587eefdb8f4c17a686ec51662a26421c5a4b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`BASE` (L5), `GENERATED` (L6)

## Import declarations

```python
from pathlib import Path
import pytest
from mainframe.verification.cobol_storage_layout import group_byte_length, child_byte_lengths
```

## Local dependency notes

- [mainframe/verification/cobol_storage_layout.py](../mainframe/verification/cobol_storage_layout.md)

## Symbol contracts and control points

### `test_redefines_preserves_offsets_not_double_count` - L9-L11

```python
test_redefines_preserves_offsets_not_double_count()
```

Observed calls (lexical order): `group_byte_length`.

### `test_unknown_storage_fails_closed` - L14-L17

```python
test_unknown_storage_fails_closed()
```

Observed calls (lexical order): `pytest.raises`, `group_byte_length`.

### `test_vmdz7200_manual_layout_contract` - L20-L23

```python
test_vmdz7200_manual_layout_contract()
```

Observed calls (lexical order): `(BASE / 'VMDZ7200.cbl').read_text`, `group_byte_length`, `child_byte_lengths`.

### `test_vmdz7200_generated_layout_contract` - L26-L31

```python
test_vmdz7200_generated_layout_contract()
```

Observed calls (lexical order): `GENERATED.glob`, `sorted`, `len`, `p[0].read_text`, `group_byte_length`, `child_byte_lengths`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
