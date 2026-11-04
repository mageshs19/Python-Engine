# `tests/test_review_business_semantics.py`

Source: [tests/test_review_business_semantics.py](../../../tests/test_review_business_semantics.py) | 50 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `4fbee33f7726660bcd0c8692391331e51d5c8835cf38607871b7b99a79bb9c08`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.domain.models import DclgenColumn, SheetMappingRow
from review.checks.chk_11_sqlcode_commit_conversion import SqlcodeCommitConversionCheck
from review.checks.chk_24_picture_and_length import PictureAndLengthCheck
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [review/checks/chk_11_sqlcode_commit_conversion.py](../review/checks/chk_11_sqlcode_commit_conversion.md)
- [review/checks/chk_24_picture_and_length.py](../review/checks/chk_24_picture_and_length.md)

## Symbol contracts and control points

### `test_finish_without_database_update_does_not_imply_commit` - L8-L10

```python
test_finish_without_database_update_does_not_imply_commit()
```

Observed calls (lexical order): `SqlcodeCommitConversionCheck._source_requires_commit`.

### `test_finish_with_modify_requires_commit` - L13-L15

```python
test_finish_with_modify_requires_commit()
```

Observed calls (lexical order): `SqlcodeCommitConversionCheck._source_requires_commit`.

### `test_explicit_source_commit_requires_commit` - L18-L20

```python
test_explicit_source_commit_requires_commit()
```

Observed calls (lexical order): `SqlcodeCommitConversionCheck._source_requires_commit`.

### `test_numeric_legacy_date_to_db2_date_host_is_representation_conversion` - L23-L34

```python
test_numeric_legacy_date_to_db2_date_host_is_representation_conversion()
```

Observed calls (lexical order): `SheetMappingRow`, `DclgenColumn`, `SimpleNamespace`, `PictureAndLengthCheck._category_mismatches`.

### `test_numeric_to_character_non_temporal_still_fails_category_check` - L37-L50

```python
test_numeric_to_character_non_temporal_still_fails_category_check()
```

Observed calls (lexical order): `SheetMappingRow`, `DclgenColumn`, `SimpleNamespace`, `PictureAndLengthCheck._category_mismatches`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
