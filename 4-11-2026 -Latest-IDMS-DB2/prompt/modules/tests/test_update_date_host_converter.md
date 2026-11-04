# `tests/test_update_date_host_converter.py`

Source: [tests/test_update_date_host_converter.py](../../../tests/test_update_date_host_converter.py) | 80 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `65626da77337c9e3d6da4b7e3a1e32e378974924b42718d19871750cee874de3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.postprocess.update_date_host_converter import UpdateDateHostConverter
```

## Local dependency notes

- [converter/postprocess/update_date_host_converter.py](../converter/postprocess/update_date_host_converter.md)

## Symbol contracts and control points

### `_col` - L8-L15

```python
_col(host, db2_type)
```

Observed calls (lexical order): `SimpleNamespace`.

### `_fixed` - L18-L19

```python
_fixed(body: str) -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `_converter` - L22-L29

```python
_converter()
```

Observed calls (lexical order): `_col`, `UpdateDateHostConverter`.

### `test_raw_move_to_date_host_is_converted_one_line` - L32-L41

```python
test_raw_move_to_date_host_is_converted_one_line()
```

Observed calls (lexical order): `_fixed`, `_converter`, `_converter().apply`.

### `test_raw_move_to_date_host_is_converted_wrapped` - L44-L50

```python
test_raw_move_to_date_host_is_converted_wrapped()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `_converter`, `_converter().apply`.

### `test_timestamp_audit_move_is_never_converted` - L55-L61

```python
test_timestamp_audit_move_is_never_converted()
```

Observed calls (lexical order): `_fixed`, `_converter`, `_converter().apply`.

### `test_user_audit_char_move_is_never_converted` - L64-L68

```python
test_user_audit_char_move_is_never_converted()
```

Observed calls (lexical order): `_fixed`, `_converter`, `_converter().apply`.

### `test_exec_sql_host_reference_untouched` - L71-L80

```python
test_exec_sql_host_reference_untouched()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `_converter`, `_converter().apply`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
