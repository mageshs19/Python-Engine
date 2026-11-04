# `tests/test_record_mapping_failure_contract.py`

Source: [tests/test_record_mapping_failure_contract.py](../../../tests/test_record_mapping_failure_contract.py) | 29 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e9484af8bb290d050475c14153358ecc6000038eaa779da87af5d2a0b34d99db`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
import pytest
from converter.composers.record_materialisation.record_plan_builder import RecordPlanBuilder, RecordMappingLookupError
```

## Local dependency notes

- [converter/composers/record_materialisation/record_plan_builder.py](../converter/composers/record_materialisation/record_plan_builder.md)

## Symbol contracts and control points

### `FailRepo` - L7-L9

```python
class FailRepo()
```

### `FailRepo.rows_for_record` - L8-L9

```python
rows_for_record(self, record)
```

Observed calls (lexical order): `OSError`.

Explicit raises: `OSError('CSV not readable')`.

### `EmptyRepo` - L12-L14

```python
class EmptyRepo()
```

### `EmptyRepo.rows_for_record` - L13-L14

```python
rows_for_record(self, record)
```

### `builder` - L17-L20

```python
builder(repo)
```

Observed calls (lexical order): `RecordPlanBuilder`.

### `test_io_failure_is_not_silently_interpreted_as_no_fields` - L23-L25

```python
test_io_failure_is_not_silently_interpreted_as_no_fields()
```

Observed calls (lexical order): `pytest.raises`, `FailRepo`, `builder`, `builder(FailRepo())._rows`.

### `test_truly_unmapped_record_is_still_empty` - L28-L29

```python
test_truly_unmapped_record_is_still_empty()
```

Observed calls (lexical order): `EmptyRepo`, `builder`, `builder(EmptyRepo())._rows`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
