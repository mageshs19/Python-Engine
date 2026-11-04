# `tests/test_update_char_literal_quoter.py`

Source: [tests/test_update_char_literal_quoter.py](../../../tests/test_update_char_literal_quoter.py) | 36 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `95b0ae5c6c3c8319eac3112c4e0371bf660f74c306e2d1395a3c20a1c6510708`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.postprocess.update_final_cleanup import UpdateFinalCleanup
```

## Local dependency notes

- [converter/postprocess/update_final_cleanup.py](../converter/postprocess/update_final_cleanup.md)

## Symbol contracts and control points

### `_fixed` - L4-L6

```python
_fixed(body: str) -> str
```

Build an 80-col fixed-format line: left(6)+space+body(65)+space+right(8).

Observed calls (lexical order): `body[:65].ljust`.

### `test_non_sql_move_dot_reference_is_rewritten_to_of` - L9-L13

```python
test_non_sql_move_dot_reference_is_rewritten_to_of()
```

Observed calls (lexical order): `_fixed`, `UpdateFinalCleanup`, `UpdateFinalCleanup().apply`.

### `test_one_line_exec_sql_include_does_not_wedge_flag` - L16-L23

```python
test_one_line_exec_sql_include_does_not_wedge_flag()
```

Observed calls (lexical order): `_fixed`, `UpdateFinalCleanup`, `UpdateFinalCleanup().apply`.

### `test_sql_host_reference_inside_exec_sql_preserved` - L26-L36

```python
test_sql_host_reference_inside_exec_sql_preserved()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `UpdateFinalCleanup`, `UpdateFinalCleanup().apply`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
