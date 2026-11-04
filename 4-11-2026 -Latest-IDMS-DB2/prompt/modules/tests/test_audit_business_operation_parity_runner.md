# `tests/test_audit_business_operation_parity_runner.py`

Source: [tests/test_audit_business_operation_parity_runner.py](../../../tests/test_audit_business_operation_parity_runner.py) | 17 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `de5d61ec00b9a5fadd3cddccd937eb75b5d3db66934311aae643cb1c30ac3365`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
from runners.audit_business_operation_parity import latest_candidate
```

## Local dependency notes

- [runners/audit_business_operation_parity.py](../runners/audit_business_operation_parity.md)

## Symbol contracts and control points

### `test_latest_candidate_includes_stable_names_and_uses_modification_time` - L6-L13

```python
test_latest_candidate_includes_stable_names_and_uses_modification_time(tmp_path)
```

Observed calls (lexical order): `old.write_text`, `newest.write_text`, `old.touch`, `newest.touch`, `latest_candidate`.

### `test_latest_candidate_returns_none_when_no_candidate_exists` - L16-L17

```python
test_latest_candidate_returns_none_when_no_candidate_exists(tmp_path)
```

Observed calls (lexical order): `latest_candidate`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
