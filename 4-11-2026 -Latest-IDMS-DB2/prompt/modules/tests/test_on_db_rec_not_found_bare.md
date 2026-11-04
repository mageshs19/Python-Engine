# `tests/test_on_db_rec_not_found_bare.py`

Source: [tests/test_on_db_rec_not_found_bare.py](../../../tests/test_on_db_rec_not_found_bare.py) | 52 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `45dbaafe5308dd952e9f5711204ffb48e34fd3a4477939c12f3dbaa4564e85c0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regression test for the bare ON DB-REC-NOT-FOUND conversion.

## Import declarations

```python
from __future__ import annotations
from converter.transformers.idms_statement.data_statement_converter import DataStatementConverterMixin
from rules.idms_transformer_rules import SQLCODE_100_IF_CLOSE, SQLCODE_100_IF_OPEN
```

## Local dependency notes

- [converter/transformers/idms_statement/data_statement_converter.py](../converter/transformers/idms_statement/data_statement_converter.md)
- [rules/idms_transformer_rules.py](../rules/idms_transformer_rules.md)

## Symbol contracts and control points

### `_converter` - L21-L22

```python
_converter() -> DataStatementConverterMixin
```

Observed calls (lexical order): `DataStatementConverterMixin.__new__`.

### `test_bare_on_opens_a_valid_if_guard` - L25-L27

```python
test_bare_on_opens_a_valid_if_guard() -> None
```

Observed calls (lexical order): `_converter`, `_converter()._convert_on_db_rec_not_found`.

### `test_bare_on_with_trailing_period_opens_a_valid_if_guard` - L30-L32

```python
test_bare_on_with_trailing_period_opens_a_valid_if_guard() -> None
```

Observed calls (lexical order): `_converter`, `_converter()._convert_on_db_rec_not_found`.

### `test_bare_on_never_emits_the_invalid_on_sqlcode_statement` - L35-L39

```python
test_bare_on_never_emits_the_invalid_on_sqlcode_statement() -> None
```

Observed calls (lexical order): `_converter`, `_converter()._convert_on_db_rec_not_found`, `line.upper`, `line.upper().lstrip`, `line.upper().lstrip().startswith`.

Control points:

- L38: `for line in result`

### `test_same_line_on_still_builds_the_full_guard_block` - L42-L48

```python
test_same_line_on_still_builds_the_full_guard_block() -> None
```

Observed calls (lexical order): `_converter`, `_converter()._convert_on_db_rec_not_found`, `any`.

### `test_unrelated_line_is_not_claimed` - L51-L52

```python
test_unrelated_line_is_not_claimed() -> None
```

Observed calls (lexical order): `_converter`, `_converter()._convert_on_db_rec_not_found`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
