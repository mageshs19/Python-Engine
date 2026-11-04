# `tests/test_record_picture_sizer.py`

Source: [tests/test_record_picture_sizer.py](../../../tests/test_record_picture_sizer.py) | 85 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `9ea345eb4c108077ce8498661520cfa6a3b6a99e9ccbf2ff9cf57e2cae4e507e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> PICTURE sizing.

## Import declarations

```python
import pytest
from converter.composers.record_materialisation.record_picture_sizer import RecordPictureSizer
```

## Local dependency notes

- [converter/composers/record_materialisation/record_picture_sizer.py](../converter/composers/record_materialisation/record_picture_sizer.md)

## Symbol contracts and control points

### `test_declared_bytes_reads_the_full_clause` - L35-L36

```python
test_declared_bytes_reads_the_full_clause(body, expected)
```

Observed calls (lexical order): `RecordPictureSizer.declared_bytes`.

### `test_a_truncated_caller_capture_cannot_win` - L39-L48

```python
test_a_truncated_caller_capture_cannot_win()
```

The caller's group says 'X'; the line says 'X(478)'.

Observed calls (lexical order): `RecordPictureSizer.declared_bytes`, `_Match`.

### `test_a_truncated_caller_capture_cannot_win._Match` - L42-L44

```python
class _Match()
```

### `test_a_truncated_caller_capture_cannot_win._Match.group` - L43-L44

```python
group(self, name)
```

### `test_the_data_name_is_never_measured` - L51-L55

```python
test_the_data_name_is_never_measured()
```

F-TARGET contains an A, which the symbol class matches.

Observed calls (lexical order): `RecordPictureSizer.declared_bytes`.

### `test_comp_3_is_halved` - L58-L60

```python
test_comp_3_is_halved()
```

Observed calls (lexical order): `RecordPictureSizer.size_of`.

### `test_empty_and_unreadable_are_zero` - L63-L66

```python
test_empty_and_unreadable_are_zero()
```

Observed calls (lexical order): `RecordPictureSizer.declared_bytes`, `RecordPictureSizer.size_of`.

### `test_repeat_counts_are_honoured` - L68-L74

```python
test_repeat_counts_are_honoured()
```

The defect: (n) was ignored and every clause measured 1.

Observed calls (lexical order): `RecordPictureSizer.size_of`.

### `test_whitespace_inside_the_repeat_is_tolerated` - L77-L79

```python
test_whitespace_inside_the_repeat_is_tolerated()
```

The mapping workbook contains 'PIC X(4 )'.

Observed calls (lexical order): `RecordPictureSizer.declared_bytes`.

### `test_a_value_clause_is_not_measured` - L82-L85

```python
test_a_value_clause_is_not_measured()
```

Observed calls (lexical order): `RecordPictureSizer.declared_bytes`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
