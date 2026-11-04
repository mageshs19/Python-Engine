# `tests/test_update_input_record_renamer.py`

Source: [tests/test_update_input_record_renamer.py](../../../tests/test_update_input_record_renamer.py) | 62 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `28203257e0730e9643c0e305abae807f075a4e8cc1fa752aaffebd8b3e817fdd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.postprocess.update_input_record_renamer import UpdateInputRecordRenamer
```

## Local dependency notes

- [converter/postprocess/update_input_record_renamer.py](../converter/postprocess/update_input_record_renamer.md)

## Symbol contracts and control points

### `_fixed` - L6-L7

```python
_fixed(body: str, seq: str='000750') -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `_comment` - L10-L12

```python
_comment(body: str, seq: str='000260') -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `test_executable_references_renamed` - L15-L28

```python
test_executable_references_renamed()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `UpdateInputRecordRenamer`, `UpdateInputRecordRenamer().apply`.

### `test_comment_line_preserved` - L31-L42

```python
test_comment_line_preserved()
```

Observed calls (lexical order): `'\n'.join`, `_comment`, `_fixed`, `UpdateInputRecordRenamer`, `UpdateInputRecordRenamer().apply`, `out.splitlines`.

### `test_duplicate_copy_deduplicated` - L45-L54

```python
test_duplicate_copy_deduplicated()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `UpdateInputRecordRenamer`, `UpdateInputRecordRenamer().apply`, `out.upper`, `out.upper().count`.

### `test_no_change_when_old_equals_new` - L57-L62

```python
test_no_change_when_old_equals_new()
```

Observed calls (lexical order): `_fixed`, `UpdateInputRecordRenamer`, `UpdateInputRecordRenamer().apply`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
