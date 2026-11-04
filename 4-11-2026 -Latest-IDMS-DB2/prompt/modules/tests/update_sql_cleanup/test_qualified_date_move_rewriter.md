# `tests/update_sql_cleanup/test_qualified_date_move_rewriter.py`

Source: [tests/update_sql_cleanup/test_qualified_date_move_rewriter.py](../../../../tests/update_sql_cleanup/test_qualified_date_move_rewriter.py) | 76 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `76329c14df18d8a529e8ba1e7aaa770109c367732c7bd559396e46434618be8a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The defect: a DATE column that arrived QUALIFIED lost its conversion.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.composers.update_sql_cleanup.qualified_date_move_rewriter import QualifiedDateMoveRewriter
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/qualified_date_move_rewriter.py](../../converter/composers/update_sql_cleanup/qualified_date_move_rewriter.md)

## Symbol contracts and control points

### `_logical` - L20-L21

```python
_logical(lines)
```

Observed calls (lexical order): `' '.join`, `str`, `str(l).strip`, `str(l).upper`, `str(l).upper().split`.

### `test_a_qualified_date_move_gains_the_conversion_block` - L24-L33

```python
test_a_qualified_date_move_gains_the_conversion_block(composer)
```

Observed calls (lexical order): `_logical`, `composer.rewrite`, `composer.rewrite(source).splitlines`.

### `test_the_continuation_form_is_matched` - L36-L43

```python
test_the_continuation_form_is_matched(composer)
```

The column-72 wrapper pushes the qualifier onto the next line.

Observed calls (lexical order): `_logical`, `composer.rewrite`, `composer.rewrite(source).splitlines`.

### `test_a_non_date_column_is_left_alone` - L46-L49

```python
test_a_non_date_column_is_left_alone(composer)
```

Observed calls (lexical order): `_logical`, `composer.rewrite`, `composer.rewrite(source).splitlines`, `' '.join`.

### `test_the_pass_is_idempotent` - L52-L60

```python
test_the_pass_is_idempotent(composer)
```

Observed calls (lexical order): `composer.rewrite`, `_logical`, `_logical(once.splitlines()).count`, `once.splitlines`, `_logical(twice.splitlines()).count`, `twice.splitlines`.

### `test_a_move_inside_exec_sql_is_never_touched` - L63-L69

```python
test_a_move_inside_exec_sql_is_never_touched(composer)
```

Observed calls (lexical order): `composer.rewrite`.

### `test_the_conversion_is_reported` - L72-L76

```python
test_the_conversion_is_reported(composer)
```

Observed calls (lexical order): `composer.rewrite`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
