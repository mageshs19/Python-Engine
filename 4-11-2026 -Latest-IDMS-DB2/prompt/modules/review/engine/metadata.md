# `review/engine/metadata.py`

Source: [review/engine/metadata.py](../../../../review/engine/metadata.py) | 186 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `5461ff5514d8adaf8780c26eeb6a33c2ca2b1f9e9edff5812ccab9bc63cb8dc5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Read-only classification of the metadata carried on a ReviewContext.

## Module-level bindings

`WS_RUN` (L15), `KEY_FOREIGN` (L16), `KEY_FK` (L17)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_16_update_validation.py](../checks/chk_16_update_validation.md)
- [review/checks/chk_22_naming_authority.py](../checks/chk_22_naming_authority.md)
- [review/checks/chk_23_host_variable_exactness.py](../checks/chk_23_host_variable_exactness.md)
- [review/checks/chk_24_picture_and_length.py](../checks/chk_24_picture_and_length.md)
- [review/checks/chk_25_copybook_and_record_usage.py](../checks/chk_25_copybook_and_record_usage.md)
- [review/checks/chk_28_obtain_first_next_conversion.py](../checks/chk_28_obtain_first_next_conversion.md)
- [review/checks/chk_29_lr_status_field_replacement.py](../checks/chk_29_lr_status_field_replacement.md)
- [review/checks/chk_30_lrf_path_expansion.py](../checks/chk_30_lrf_path_expansion.md)
- [review/checks/chk_31_store_modify_erase_removal.py](../checks/chk_31_store_modify_erase_removal.md)

## Symbol contracts and control points

### `norm_name` - L20-L22

```python
norm_name(value) -> str
```

Uppercase, trimmed, whitespace collapsed.

Observed calls (lexical order): `WS_RUN.sub`, `str`, `str(value or '').strip`, `str(value or '').strip().upper`.

### `field` - L25-L31

```python
field(row, *names, default: str='') -> str
```

First populated attribute from a metadata row.

Observed calls (lexical order): `getattr`, `norm_name`.

Control points:

- L27: `for name in names`
- L29: `if value`

### `dclgen_tables` - L35-L40

```python
dclgen_tables(ctx) -> set[str]
```

Observed calls (lexical order): `field`.

### `columns_for_table` - L43-L50

```python
columns_for_table(ctx, table: str) -> set[str]
```

Observed calls (lexical order): `norm_name`, `field`.

### `hosts_for_table` - L53-L64

```python
hosts_for_table(ctx, table: str) -> dict[str, str]
```

DB2 column -> COBOL host variable, for one table.

Observed calls (lexical order): `norm_name`, `field`.

Control points:

- L57: `for column in ctx.dclgen_columns or []`
- L58: `if field(column, 'table_name') != wanted`
- L62: `if name and host`

### `columns_with_prefix` - L67-L75

```python
columns_with_prefix(ctx, table: str, prefixes) -> set[str]
```

DCLGEN columns of a table whose name starts with any prefix.

Observed calls (lexical order): `norm_name`, `tuple`, `set`, `columns_for_table`, `name.startswith`.

Control points:

- L70: `if not wanted`

### `picture_for` - L78-L87

```python
picture_for(ctx, table: str, column: str) -> str
```

Observed calls (lexical order): `norm_name`, `field`.

Control points:

- L81: `for item in ctx.dclgen_columns or []`
- L82: `if field(item, 'table_name') != wanted_table`
- L84: `if field(item, 'column_name') != wanted_column`

### `rows_for_record` - L91-L96

```python
rows_for_record(ctx, record: str) -> list
```

Observed calls (lexical order): `norm_name`, `field`.

### `mapped_records` - L99-L104

```python
mapped_records(ctx) -> set[str]
```

Observed calls (lexical order): `field`.

### `table_for_record` - L107-L112

```python
table_for_record(ctx, record: str) -> str
```

Observed calls (lexical order): `rows_for_record`, `field`.

Control points:

- L108: `for row in rows_for_record(ctx, record)`
- L110: `if table`

### `mapped_tables` - L115-L120

```python
mapped_tables(ctx) -> set[str]
```

Observed calls (lexical order): `field`.

### `mapped_columns` - L123-L128

```python
mapped_columns(ctx) -> set[str]
```

Observed calls (lexical order): `field`.

### `_column_of` - L131-L134

```python
_column_of(row) -> str
```

Observed calls (lexical order): `field`.

### `_is_foreign` - L137-L139

```python
_is_foreign(row) -> bool
```

Observed calls (lexical order): `' '.join`, `field`.

### `primary_key_columns` - L142-L159

```python
primary_key_columns(ctx, record: str, key_markers) -> list[str]
```

Composite PK and CALC key columns. FOREIGN columns are excluded.

Observed calls (lexical order): `norm_name`, `tuple`, `set`, `rows_for_record`, `_column_of`, `_is_foreign`, `' '.join`, `field`, `any`, `seen.add`, `out.append`.

Control points:

- L148: `for row in rows_for_record(ctx, record)`
- L150: `if not column or column in seen`
- L152: `if _is_foreign(row)`
- L155: `if not any((marker in text for marker in markers))`

### `foreign_key_columns` - L162-L172

```python
foreign_key_columns(ctx, record: str) -> list[str]
```

Observed calls (lexical order): `set`, `rows_for_record`, `_is_foreign`, `_column_of`, `seen.add`, `out.append`.

Control points:

- L165: `for row in rows_for_record(ctx, record)`
- L166: `if not _is_foreign(row)`
- L169: `if column and column not in seen`

### `all_primary_key_columns` - L175-L179

```python
all_primary_key_columns(ctx, key_markers) -> set[str]
```

Observed calls (lexical order): `set`, `mapped_records`, `out.update`, `primary_key_columns`.

Control points:

- L177: `for record in mapped_records(ctx)`

### `all_foreign_key_columns` - L182-L186

```python
all_foreign_key_columns(ctx) -> set[str]
```

Observed calls (lexical order): `set`, `mapped_records`, `foreign_key_columns`, `out.update`.

Control points:

- L184: `for record in mapped_records(ctx)`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
