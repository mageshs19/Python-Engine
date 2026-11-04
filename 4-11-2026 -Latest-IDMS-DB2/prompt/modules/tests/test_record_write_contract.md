# `tests/test_record_write_contract.py`

Source: [tests/test_record_write_contract.py](../../../tests/test_record_write_contract.py) | 41 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `cc33e072800ad180d03da0f1b15f88f21fe0b10d3fce3866266f619279480f08`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`BASE` (L4)

## Import declarations

```python
from pathlib import Path
from mainframe.verification.record_write_contract import audit_fixed_record_writes
import re
```

## Local dependency notes

- [mainframe/verification/record_write_contract.py](../mainframe/verification/record_write_contract.md)

## Symbol contracts and control points

### `_text` - L7-L8

```python
_text(name)
```

Observed calls (lexical order): `BASE.glob`, `next`, `next(BASE.glob(f'{name}_*.cbl')).read_text`.

### `test_physical_write_contracts_hold_for_retrieval_programs` - L11-L14

```python
test_physical_write_contracts_hold_for_retrieval_programs()
```

Observed calls (lexical order): `_text`, `audit_fixed_record_writes`.

Control points:

- L12: `for name in ('VMDZ4302', 'VMDZ7200')`

### `test_missing_filler_is_a_release_failure` - L17-L23

```python
test_missing_filler_is_a_release_failure()
```

Observed calls (lexical order): `_text`, `re.sub`, `audit_fixed_record_writes`, `any`.

### `test_unsupported_layout_does_not_fake_success` - L26-L29

```python
test_unsupported_layout_does_not_fake_success()
```

Observed calls (lexical order): `audit_fixed_record_writes`, `any`.

### `test_write_literal_is_not_a_file_operation` - L32-L41

```python
test_write_literal_is_not_a_file_operation()
```

Observed calls (lexical order): `audit_fixed_record_writes`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
