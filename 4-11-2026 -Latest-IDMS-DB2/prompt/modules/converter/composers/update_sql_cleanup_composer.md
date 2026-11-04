# `converter/composers/update_sql_cleanup_composer.py`

Source: [converter/composers/update_sql_cleanup_composer.py](../../../../converter/composers/update_sql_cleanup_composer.py) | 187 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `7883daf9b1b713225b84ccc175325cac3c46b6c7aac9c69bbb94797ddc7e1412`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Update SQL cleanup composer.

## Module-level bindings

`__all__` (L187)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.update_sql_cleanup.bare_move_rewriter import BareMoveRewriter
from converter.composers.update_sql_cleanup.composer_patterns import ANY_DCL_DOT_REFERENCE_PATTERN, ANY_DCL_OF_REFERENCE_PATTERN, DATE_COLUMN_PREFIXES, MOVE_TO_DCL_DOT_HOST_PATTERN, STRING_INTO_DCL_DOT_HOST_PATTERN, STRING_INTO_DCL_HOST_PATTERN
from converter.composers.update_sql_cleanup.date_move_builder import DateMoveBuilder
from converter.composers.update_sql_cleanup.modify_update_rewriter import ModifyUpdateRewriter
from converter.composers.update_sql_cleanup.obtain_calc_remover import ObtainCalcRemover
from converter.composers.update_sql_cleanup.qualified_date_move_rewriter import QualifiedDateMoveRewriter
from converter.composers.update_sql_cleanup.sql_block_scanner import SqlBlockScanner
from converter.composers.update_sql_cleanup.sqlerror_normalizer import SqlerrorNormalizer
from converter.composers.update_sql_cleanup_base import UpdateSqlCleanupBase
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/bare_move_rewriter.py](update_sql_cleanup/bare_move_rewriter.md)
- [converter/composers/update_sql_cleanup/composer_patterns.py](update_sql_cleanup/composer_patterns.md)
- [converter/composers/update_sql_cleanup/date_move_builder.py](update_sql_cleanup/date_move_builder.md)
- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](update_sql_cleanup/modify_update_rewriter.md)
- [converter/composers/update_sql_cleanup/obtain_calc_remover.py](update_sql_cleanup/obtain_calc_remover.md)
- [converter/composers/update_sql_cleanup/qualified_date_move_rewriter.py](update_sql_cleanup/qualified_date_move_rewriter.md)
- [converter/composers/update_sql_cleanup/sql_block_scanner.py](update_sql_cleanup/sql_block_scanner.md)
- [converter/composers/update_sql_cleanup/sqlerror_normalizer.py](update_sql_cleanup/sqlerror_normalizer.md)
- [converter/composers/update_sql_cleanup_base.py](update_sql_cleanup_base.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_program_feedback_composer.py](update_program_feedback_composer.md)

## Symbol contracts and control points

### `UpdateSqlCleanupComposer` - L85-L184

```python
class UpdateSqlCleanupComposer(UpdateSqlCleanupBase)
```

Declared class/data-model fields:

```python
MOVE_TO_DCL_DOT_HOST_PATTERN = MOVE_TO_DCL_DOT_HOST_PATTERN
STRING_INTO_DCL_HOST_PATTERN = STRING_INTO_DCL_HOST_PATTERN
STRING_INTO_DCL_DOT_HOST_PATTERN = STRING_INTO_DCL_DOT_HOST_PATTERN
ANY_DCL_OF_REFERENCE_PATTERN = ANY_DCL_OF_REFERENCE_PATTERN
ANY_DCL_DOT_REFERENCE_PATTERN = ANY_DCL_DOT_REFERENCE_PATTERN
DATE_COLUMN_PREFIXES = DATE_COLUMN_PREFIXES
```

### `UpdateSqlCleanupComposer.__init__` - L94-L113

```python
__init__(self, *args, **kwargs) -> None
```

Observed calls (lexical order): `super`, `super().__init__`, `SqlBlockScanner`, `DateMoveBuilder`, `SqlerrorNormalizer`, `BareMoveRewriter`, `QualifiedDateMoveRewriter`, `ObtainCalcRemover`, `ModifyUpdateRewriter`.

### `UpdateSqlCleanupComposer.compose` - L115-L132

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `output.strip`, `self._sqlerror.normalize`, `self._bare_move.rewrite`, `self._qualified_date_move.rewrite`, `self.messages.extend`, `self._obtain_calc.rewrite`, `self._modify_update.rewrite`, `output.rstrip`.

Control points:

- L119: `if not output.strip()`

### `UpdateSqlCleanupComposer._db2_primary_key_columns` - L134-L184

```python
_db2_primary_key_columns(self, record: str, table: str) -> list[str]
```

Composite PK / CALC key columns for WHERE.

Observed calls (lexical order): `set`, `self.mapping_repository.rows_for_record`, `NameNormalizer.normalize`, `getattr`, `' '.join`, `seen.add`, `output.append`, `self._filter_existing_dclgen_columns`.

Control points:

- L150: `for row in self.mapping_repository.rows_for_record(record)`
- L158: `if not column`
- L164: `if 'FOREIGN' in combined_text`
- L166: `if ' FK ' in padded_text`
- L176: `if not is_key_column`
- L178: `if column in seen`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
