# `converter/generators/sql/sql_date_move_builder.py`

Source: [converter/generators/sql/sql_date_move_builder.py](../../../../../converter/generators/sql/sql_date_move_builder.py) | 104 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `c94a798ea8f5c7f6cf93c057e959c08a71b7593ac58990cdad881a36906e7dae`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date column detection and CCYYMMDD -> DD.MM.CCYY move builder.

## Module-level bindings

`__all__` (L104)

## Import declarations

```python
from __future__ import annotations
from converter.services.db2_date_sentinel_policy import Db2DateSentinelPolicy
from converter.services.name_normalizer import NameNormalizer
from rules.sql_generation_rules import DATE_COLUMN_PREFIXES, DATE_STAGING_FIELDS, DB2_DATE_NULL_SENTINEL
```

## Local dependency notes

- [converter/services/db2_date_sentinel_policy.py](../../services/db2_date_sentinel_policy.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/sql_generation_rules.py](../../../rules/sql_generation_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/sql_generator.py](../sql_generator.md)

## Symbol contracts and control points

### `SqlDateMoveBuilder` - L24-L101

```python
class SqlDateMoveBuilder()
```

Builds the manual CCYYMMDD -> DD.MM.CCYY host move.

### `SqlDateMoveBuilder.__init__` - L27-L31

```python
__init__(self) -> None
```

### `SqlDateMoveBuilder.is_db2_date_column` - L36-L40

```python
is_db2_date_column(self, column_name: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `any`, `column.startswith`.

### `SqlDateMoveBuilder._is_staging_field` - L43-L50

```python
_is_staging_field(source: str) -> bool
```

True when the source is already a DB2 date staging field.

Observed calls (lexical order): `str`, `str(source or '').strip`, `str(source or '').strip().upper`.

### `SqlDateMoveBuilder.date_ymd8_to_db2_external_move` - L55-L101

```python
date_ymd8_to_db2_external_move(self, source_value: str, host_key: str) -> list[str]
```

Convert a CCYYMMDD source value into DB2 external date DD.MM.CCYY, then move it into the DB2 date host field.

Observed calls (lexical order): `str`, `str(source_value or '').strip`, `self._is_staging_field`, `Db2DateSentinelPolicy`, `sentinel.guard_lines`, `self.messages.extend`.

Control points:

- L78: `if self._is_staging_field(source)`
- L83: `if not source`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
