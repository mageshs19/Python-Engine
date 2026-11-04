# `tests/test_dzecabtv_fix.py`

Source: [tests/test_dzecabtv_fix.py](../../../tests/test_dzecabtv_fix.py) | 116 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `3770bb760d2c42302e003c7c40bece3353deb8e5f7e6c8fd7bd0b4332dc90e2b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Test that FFRECAB (restart table) is filtered from DCLGEN dependency resolution.

## Import declarations

```python
import pytest
from mainframe.zowe_resolver import resolve_dependencies
```

## Local dependency notes

- [mainframe/zowe_resolver.py](../mainframe/zowe_resolver.md)

## Symbol contracts and control points

### `TestFfrecabFiltering` - L26-L113

```python
class TestFfrecabFiltering()
```

FFRECAB should be filtered from DCLGEN dependency resolution.

### `TestFfrecabFiltering.test_ffrecab_not_generates_dclgen_when_sole_record` - L29-L35

```python
test_ffrecab_not_generates_dclgen_when_sole_record(self)
```

OBTAIN FFRECAB alone should produce no DCLGENs.

Observed calls (lexical order): `resolve_dependencies`, `len`.

### `TestFfrecabFiltering.test_ffrecab_filtered_alongside_data_records` - L37-L51

```python
test_ffrecab_filtered_alongside_data_records(self)
```

OBTAIN FFRECAB + data records: only data records generate DCLGENs.

Observed calls (lexical order): `resolve_dependencies`.

### `TestFfrecabFiltering.test_vm1bd526_real_source` - L53-L75

```python
test_vm1bd526_real_source(self)
```

Verify actual VM1BD526 source no longer generates DZECABTV.

Observed calls (lexical order): `resolve_dependencies`, `any`, `set`.

### `TestFfrecabFiltering.test_vm1bd567_real_source` - L77-L98

```python
test_vm1bd567_real_source(self)
```

Verify actual VM1BD567 source no longer generates DZECABTV.

Observed calls (lexical order): `resolve_dependencies`, `any`, `set`.

### `TestFfrecabFiltering.test_manifest_no_longer_lists_dzecabtv` - L100-L113

```python
test_manifest_no_longer_lists_dzecabtv(self)
```

End-to-end: VM1BD526 and VM1BD567 should not reference DZECABTV.

Observed calls (lexical order): `resolve_dependencies`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
