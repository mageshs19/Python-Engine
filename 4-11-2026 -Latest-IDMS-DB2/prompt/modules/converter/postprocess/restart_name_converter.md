# `converter/postprocess/restart_name_converter.py`

Source: [converter/postprocess/restart_name_converter.py](../../../../converter/postprocess/restart_name_converter.py) | 269 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `2ba5346543e8149ce7107f65b5c170fd3f8436e627f1cffb2f4eece7ed262094`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sheet mapping to COBOL name converter for restart logic.

## Import declarations

```python
from __future__ import annotations
import re
from typing import Optional
```

## Symbol contracts and control points

### `RestartNameConverter` - L22-L202

```python
class RestartNameConverter()
```

Convert between sheet mapping names and COBOL DCL names.

Declared class/data-model fields:

```python
STANDARD_RESTART_TABLES = {'DZ01RSTV', 'FFRECAB'}
DCL_PREFIX = 'DCL'
```

### `RestartNameConverter.is_restart_table` - L48-L50

```python
is_restart_table(name: str) -> bool
```

Check if name refers to a restart/checkpoint table.

### `RestartNameConverter.sheet_to_dclgen` - L53-L90

```python
sheet_to_dclgen(sheet_name: str) -> str
```

Convert sheet mapping name (with _TB suffix) to COBOL DCLGEN name (with TV suffix).

Observed calls (lexical order): `RestartNameConverter.is_restart_table`, `sheet_name.startswith`, `sheet_name.endswith`, `cobol_name.startswith`.

Control points:

- L69: `if not sheet_name`
- L73: `if RestartNameConverter.is_restart_table(sheet_name)`
- L74: `if not sheet_name.startswith(RestartNameConverter.DCL_PREFIX)`
- L79: `if sheet_name.endswith('_TB')`
- L87: `if not cobol_name.startswith(RestartNameConverter.DCL_PREFIX)`

### `RestartNameConverter.dclgen_to_sheet` - L93-L126

```python
dclgen_to_sheet(dclgen_name: str) -> str
```

Reverse conversion: COBOL DCLGEN name → sheet mapping name.

Observed calls (lexical order): `dclgen_name.startswith`, `len`, `RestartNameConverter.is_restart_table`, `name.endswith`.

Control points:

- L108: `if not dclgen_name`
- L112: `if dclgen_name.startswith(RestartNameConverter.DCL_PREFIX)`
- L118: `if RestartNameConverter.is_restart_table(name)`
- L122: `if name.endswith('TV')`

### `RestartNameConverter.extract_base_name` - L129-L152

```python
extract_base_name(dclgen_or_sheet: str) -> str
```

Extract base name regardless of DCL prefix or suffix.

Observed calls (lexical order): `name.startswith`, `len`, `name.endswith`.

Control points:

- L141: `if name.startswith(RestartNameConverter.DCL_PREFIX)`
- L145: `if name.endswith('TV')`
- L149: `if name.endswith('_TB')`

### `RestartNameConverter.is_business_table_with_restart` - L155-L171

```python
is_business_table_with_restart(sheet_name: str) -> bool
```

Check if this is a business table (not restart, not retrieval-only).

Observed calls (lexical order): `sheet_name.endswith`, `RestartNameConverter.is_restart_table`, `RestartNameConverter.extract_base_name`.

### `RestartNameConverter.validate_conversion` - L174-L183

```python
validate_conversion(sheet_name: str, dclgen_name: str) -> bool
```

Validate that sheet name and DCLGEN name are consistent conversions.

Observed calls (lexical order): `RestartNameConverter.sheet_to_dclgen`.

### `RestartNameConverter.suggest_conversion` - L186-L202

```python
suggest_conversion(partial_name: str) -> tuple[str, str]
```

Given a partial name, suggest both sheet and DCLGEN names.

Observed calls (lexical order): `RestartNameConverter.is_restart_table`, `RestartNameConverter.sheet_to_dclgen`.

### `RestartFieldConverter` - L205-L269

```python
class RestartFieldConverter()
```

Convert between sheet mapping column names and COBOL DCL field names for restart checkpoint fields.

Declared class/data-model fields:

```python
ROLE_TOKEN_PATTERNS = {'program': ['NM', 'ID', 'RS', 'PROGRAM'], 'program_fallback': ['PROGRAM'], 'phase': ['NB', 'ID', 'RS', 'PHASE'], 'phase_fallback': ['PHASE'], 'date': ['DA', 'CR', 'RS'], 'date_fallback': ['DATE'], 'status': ['CO', 'ID', 'RS'], 'status_fallback': ['STATUS'], 'retention': ['N...
```

### `RestartFieldConverter.sql_to_cobol_field` - L236-L244

```python
sql_to_cobol_field(sql_column: str) -> str
```

Convert SQL column name to COBOL field name (replace _ with -).

Observed calls (lexical order): `sql_column.replace`.

### `RestartFieldConverter.cobol_to_sql_field` - L247-L255

```python
cobol_to_sql_field(cobol_field: str) -> str
```

Convert COBOL field name to SQL column name (replace - with _).

Observed calls (lexical order): `cobol_field.replace`.

### `RestartFieldConverter.get_role_for_tokens` - L258-L269

```python
get_role_for_tokens(tokens: list[str]) -> Optional[str]
```

Given a list of tokens, find matching role.

Observed calls (lexical order): `RestartFieldConverter.ROLE_TOKEN_PATTERNS.items`, `all`, `t.upper`, `token.upper`.

Control points:

- L266: `for (role, pattern) in RestartFieldConverter.ROLE_TOKEN_PATTERNS.items()`
- L267: `if all((token.upper() in [t.upper() for t in pattern] for token in tokens))`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
