# `tests/test_copybook_reference_renamer.py`

Source: [tests/test_copybook_reference_renamer.py](../../../tests/test_copybook_reference_renamer.py) | 112 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b7165fb7ba88d5e4df21ab310fe3823d1305ffefd85edc60382b6ea72f009f31`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.postprocess.copybook_reference_renamer import CopybookReferenceRenamer
```

## Local dependency notes

- [converter/postprocess/copybook_reference_renamer.py](../converter/postprocess/copybook_reference_renamer.md)

## Symbol contracts and control points

### `_fixed` - L6-L8

```python
_fixed(body: str, seq: str='000750') -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `_comment` - L11-L13

```python
_comment(body: str, seq: str='000260') -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `test_bd_copybook_and_references_renamed` - L16-L28

```python
test_bd_copybook_and_references_renamed()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`.

### `test_bz_copybook_and_rec_reference_renamed` - L31-L42

```python
test_bz_copybook_and_rec_reference_renamed()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`.

### `test_comment_lines_are_preserved` - L45-L54

```python
test_comment_lines_are_preserved()
```

Observed calls (lexical order): `'\n'.join`, `_comment`, `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`, `out.splitlines`.

### `test_non_derivable_copybooks_untouched` - L57-L64

```python
test_non_derivable_copybooks_untouched()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`.

### `test_line_lengths_are_preserved` - L67-L76

```python
test_line_lengths_are_preserved()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`, `block.split`, `out.split`, `zip`, `len`.

Control points:

- L75: `for (before, after) in zip(block.split('\n'), out.split('\n'))`

### `test_duplicate_copy_is_deduplicated` - L79-L86

```python
test_duplicate_copy_is_deduplicated()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`, `out.upper`, `out.upper().count`.

### `test_no_copybook_returns_text_unchanged` - L89-L91

```python
test_no_copybook_returns_text_unchanged()
```

Observed calls (lexical order): `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`.

### `test_empty_text_is_safe` - L94-L96

```python
test_empty_text_is_safe()
```

Observed calls (lexical order): `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`.

### `test_idms_restart_table_ffrecab_stays_unchanged` - L99-L111

```python
test_idms_restart_table_ffrecab_stays_unchanged()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `CopybookReferenceRenamer`, `CopybookReferenceRenamer().apply`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
