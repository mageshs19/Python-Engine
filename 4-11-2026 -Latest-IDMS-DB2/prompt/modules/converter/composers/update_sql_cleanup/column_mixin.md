# `converter/composers/update_sql_cleanup/column_mixin.py`

Source: [converter/composers/update_sql_cleanup/column_mixin.py](../../../../../converter/composers/update_sql_cleanup/column_mixin.py) | 97 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `2edca421c4030e67dbd284d8a17a19eaaf01be033899b9d2ac0684740c41a88a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Column resolution mixin for update-program SQL cleanup.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.update_sql_cleanup_rules import INSERT_ONLY_AUDIT_PREFIXES, UPDATE_AUDIT_PREFIXES
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/update_sql_cleanup_rules.py](../../../rules/update_sql_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_base.py](../update_sql_cleanup_base.md)

## Symbol contracts and control points

### `ColumnMixin` - L20-L97

```python
class ColumnMixin()
```

### `ColumnMixin._column_for_source_field` - L21-L43

```python
_column_for_source_field(self, record: str, source_field: str) -> str
```

Resolve source field to DB2 column via the Sheet Mapping repository (deterministic authority). On no match, fail loud so a human corrects the mapping instead of the tool guessing.

Observed calls (lexical order): `self.mapping_repository.column_for_source_field`, `NameNormalizer.normalize`, `self.messages.append`.

Control points:

- L36: `if column`

### `ColumnMixin._update_audit_columns` - L45-L68

```python
_update_audit_columns(self, record: str, table: str) -> list[str]
```

Observed calls (lexical order): `set`, `self.mapping_repository.rows_for_record`, `NameNormalizer.normalize`, `getattr`, `column.startswith`, `seen.add`, `output.append`, `self._filter_existing_dclgen_columns`.

Control points:

- L53: `for row in self.mapping_repository.rows_for_record(record)`
- L57: `if not column`
- L59: `if column.startswith(INSERT_ONLY_AUDIT_PREFIXES)`
- L61: `if not column.startswith(UPDATE_AUDIT_PREFIXES)`
- L63: `if column in seen`

### `ColumnMixin._filter_existing_dclgen_columns` - L70-L97

```python
_filter_existing_dclgen_columns(self, table: str, columns: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self.dclgen_repository.column_names_for_table`, `NameNormalizer.normalize`, `self.host_variable_resolver.has_host_for_column`, `seen.add`, `output.append`.

Control points:

- L81: `for column in columns`
- L83: `if not normalized`
- L85: `if normalized not in valid_columns`
- L87: `if normalized in seen`
- L89: `if not self.host_variable_resolver.has_host_for_column(table_name=table, column_name=normalized)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
