# `converter/composers/update_sql_cleanup/date_move_builder.py`

Source: [converter/composers/update_sql_cleanup/date_move_builder.py](../../../../../converter/composers/update_sql_cleanup/date_move_builder.py) | 86 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `174b2549d46b5599fd95a66edd6eaa4b50a29df188232318bd842ce06df2daee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date move builder (update SQL cleanup).

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.sql_generation_rules import DATE_COLUMN_PREFIXES, DATE_STAGING_FIELDS, DB2_DATE_NULL_SENTINEL
from converter.services.db2_date_sentinel_policy import Db2DateSentinelPolicy
```

## Local dependency notes

- [converter/services/db2_date_sentinel_policy.py](../../services/db2_date_sentinel_policy.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/sql_generation_rules.py](../../../rules/sql_generation_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/bare_move_rewriter.py](bare_move_rewriter.md)
- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)
- [tests/update_sql_cleanup/conftest.py](../../../tests/update_sql_cleanup/conftest.md)

## Symbol contracts and control points

### `DateMoveBuilder` - L22-L86

```python
class DateMoveBuilder()
```

### `DateMoveBuilder.is_db2_date_column` - L24-L28

```python
is_db2_date_column(self, column_name: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `any`, `column.startswith`.

### `DateMoveBuilder._is_staging_field` - L31-L38

```python
_is_staging_field(source: str) -> bool
```

True when the source is already a DB2 date staging field.

Observed calls (lexical order): `str`, `str(source or '').strip`, `str(source or '').strip().upper`.

### `DateMoveBuilder.date_ymd8_to_db2_external_move` - L40-L86

```python
date_ymd8_to_db2_external_move(self, source_value: str, host_key: str, leading: str) -> list[str]
```

Convert CCYYMMDD into DB2 external date format DD.MM.CCYY.

Observed calls (lexical order): `str`, `str(source_value or '').strip`, `self._is_staging_field`, `Db2DateSentinelPolicy`, `sentinel.guard_lines`, `hasattr`, `self.messages.extend`.

Control points:

- L61: `if self._is_staging_field(source)`
- L66: `if not source`
- L76: `if not hasattr(self, 'messages')`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
