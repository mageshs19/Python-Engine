# `tests/postprocess/test_ensure_working_storage_whitespace_tolerant.py`

Source: [tests/postprocess/test_ensure_working_storage_whitespace_tolerant.py](../../../../tests/postprocess/test_ensure_working_storage_whitespace_tolerant.py) | 98 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b3b408ca85082fec08c48f4be236493252ea99fe7f1d089c93ae3cf17e314996`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regression for NEW-2c: a group declared by a DIFFERENT generator, with different internal spacing, must still be recognised as present.

## Module-level bindings

`TWO_SPACE_SOURCE` (L48), `ONE_SPACE_SOURCE` (L59)

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.storage_include.storage_ws_injector import StorageWsInjector
```

## Local dependency notes

- [converter/postprocess/storage_include/storage_ws_injector.py](../../converter/postprocess/storage_include/storage_ws_injector.md)

## Symbol contracts and control points

### `_LineUtils` - L20-L39

```python
class _LineUtils()
```

Minimal stand-in: fixed-format columns 8-72, stripped.

### `_LineUtils.lines` - L23-L24

```python
lines(self, text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`.

### `_LineUtils.logical` - L26-L30

```python
logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[7:72].rstrip`, `text.strip`.

Control points:

- L28: `if len(text) > 7 and text[:6].strip().isdigit()`

### `_LineUtils.logical_contains` - L32-L39

```python
logical_contains(self, cobol_text: str, expected: str) -> bool
```

Observed calls (lexical order): `str`, `str(expected or '').strip`, `str(expected or '').strip().upper`, `self.lines`, `self.logical`, `self.logical(line).upper`.

Control points:

- L34: `if not target`
- L36: `for line in self.lines(cobol_text)`
- L37: `if target in self.logical(line).upper()`

### `_injector` - L42-L45

```python
_injector()
```

Observed calls (lexical order): `StorageWsInjector`, `_LineUtils`.

### `test_a_two_space_aligned_group_is_recognised_as_declared` - L64-L67

```python
test_a_two_space_aligned_group_is_recognised_as_declared()
```

Observed calls (lexical order): `_injector`, `injector._declares_group`.

### `test_a_one_space_aligned_group_is_also_recognised` - L70-L72

```python
test_a_one_space_aligned_group_is_also_recognised()
```

Observed calls (lexical order): `_injector`, `injector._declares_group`.

### `test_a_genuinely_absent_group_is_not_recognised` - L75-L84

```python
test_a_genuinely_absent_group_is_not_recognised()
```

Observed calls (lexical order): `_injector`, `'\n'.join`, `injector._declares_group`.

### `test_ensure_working_storage_does_not_duplicate_a_two_space_group` - L87-L98

```python
test_ensure_working_storage_does_not_duplicate_a_two_space_group(monkeypatch)
```

The exact regression: the metadata-driven system's own spacing convention must be recognised, not just this generator's own.

Observed calls (lexical order): `_injector`, `injector.ensure_working_storage`, `any`, `d.lower`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
