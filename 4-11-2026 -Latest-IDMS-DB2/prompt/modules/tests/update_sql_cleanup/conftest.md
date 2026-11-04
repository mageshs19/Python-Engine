# `tests/update_sql_cleanup/conftest.py`

Source: [tests/update_sql_cleanup/conftest.py](../../../../tests/update_sql_cleanup/conftest.py) | 93 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `2d20692a32786e09457142a7d40a30dbe7305c37ec589f4b74b68ee67d55eeae`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Minimal DCLGEN stub for the qualified-date-move pass.

## Module-level bindings

`TABLE` (L29), `GROUP` (L30)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.composers.update_sql_cleanup.date_move_builder import DateMoveBuilder
from converter.composers.update_sql_cleanup.qualified_date_move_rewriter import QualifiedDateMoveRewriter
from converter.composers.update_sql_cleanup_base import UpdateSqlCleanupBase
from converter.domain.models import DclgenColumn
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/date_move_builder.py](../../converter/composers/update_sql_cleanup/date_move_builder.md)
- [converter/composers/update_sql_cleanup/qualified_date_move_rewriter.py](../../converter/composers/update_sql_cleanup/qualified_date_move_rewriter.md)
- [converter/composers/update_sql_cleanup_base.py](../../converter/composers/update_sql_cleanup_base.md)
- [converter/domain/models.py](../../converter/domain/models.md)

## Symbol contracts and control points

### `_StubDclgenRepository` - L33-L63

```python
class _StubDclgenRepository()
```

Answers tables(), group_for_table() and columns_for_table().

Declared class/data-model fields:

```python
COLUMNS = [DclgenColumn(table_name=TABLE, column_name='DA_CRFMAS_479BFAR', cobol_host_name='DA-CRFMAS-479BFAR'), DclgenColumn(table_name=TABLE, column_name='DA_INFSDGD_479BFAR', cobol_host_name='DA-INFSDGD-479BFAR'), DclgenColumn(table_name=TABLE, column_name='NR_CIOFMAS_479BFAR', cobol_host_name...
```

### `_StubDclgenRepository.tables` - L54-L55

```python
tables(self) -> list[str]
```

### `_StubDclgenRepository.group_for_table` - L57-L58

```python
group_for_table(self, table_name: str) -> str
```

Observed calls (lexical order): `str`, `str(table_name).upper`.

### `_StubDclgenRepository.columns_for_table` - L60-L63

```python
columns_for_table(self, table_name: str) -> list[DclgenColumn]
```

Observed calls (lexical order): `str`, `str(table_name).upper`, `list`.

Control points:

- L61: `if str(table_name).upper() != TABLE`

### `_StubOwner` - L66-L85

```python
class _StubOwner()
```

Supplies only what QualifiedDateMoveRewriter reads from its owner.

Declared class/data-model fields:

```python
EXEC_SQL_START_PATTERN = UpdateSqlCleanupBase.EXEC_SQL_START_PATTERN
EXEC_SQL_END_PATTERN = UpdateSqlCleanupBase.EXEC_SQL_END_PATTERN
MOVE_TO_DCL_HOST_PATTERN = UpdateSqlCleanupBase.MOVE_TO_DCL_HOST_PATTERN
```

### `_StubOwner.__init__` - L73-L74

```python
__init__(self) -> None
```

Observed calls (lexical order): `_StubDclgenRepository`.

### `_StubOwner._logical` - L77-L80

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`, `' '.join`, `body.split`.

### `_StubOwner._leading_spaces` - L83-L85

```python
_leading_spaces(line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `text.lstrip`.

### `composer` - L89-L93

```python
composer() -> QualifiedDateMoveRewriter
```

Observed calls (lexical order): `QualifiedDateMoveRewriter`, `_StubOwner`, `DateMoveBuilder`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
