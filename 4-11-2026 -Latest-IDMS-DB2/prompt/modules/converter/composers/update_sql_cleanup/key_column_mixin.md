# `converter/composers/update_sql_cleanup/key_column_mixin.py`

Source: [converter/composers/update_sql_cleanup/key_column_mixin.py](../../../../../converter/composers/update_sql_cleanup/key_column_mixin.py) | 78 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `4a25099d111fd166eabdd82b9b8665274d0ca0c074d3334f59208eece7f24664`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Primary-key column resolution mixin for update-program SQL cleanup.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.update_sql_cleanup_rules import IDENTITY_KEY_PREFIXES
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/update_sql_cleanup_rules.py](../../../rules/update_sql_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_base.py](../update_sql_cleanup_base.md)

## Symbol contracts and control points

### `KeyColumnMixin` - L12-L78

```python
class KeyColumnMixin()
```

### `KeyColumnMixin._db2_primary_key_columns` - L13-L42

```python
_db2_primary_key_columns(self, record: str, table: str) -> list[str]
```

Return DB2 primary-key columns for SQL WHERE.

Observed calls (lexical order): `self._strict_db2_primary_key_columns`, `self._filter_existing_dclgen_columns`, `len`, `column.startswith`.

Control points:

- L30: `if len(strict_keys) <= 1`
- L39: `if identity_keys`

### `KeyColumnMixin._strict_db2_primary_key_columns` - L44-L78

```python
_strict_db2_primary_key_columns(self, record: str) -> list[str]
```

Observed calls (lexical order): `set`, `self.mapping_repository.rows_for_record`, `NameNormalizer.normalize`, `getattr`, `seen.add`, `output.append`, `hasattr`, `self.mapping_repository.key_columns_for_record`.

Control points:

- L51: `for row in self.mapping_repository.rows_for_record(record)`
- L58: `if not column`
- L60: `if 'FOREIGN' in relation`
- L62: `if 'FOREIGN' in db2_key`
- L64: `if 'PRIMARY' not in db2_key and db2_key != 'KEY'`
- L66: `if column in seen`
- L72: `if output`
- L75: `if hasattr(self.mapping_repository, 'key_columns_for_record')`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
