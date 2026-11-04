# `catalogs/restart_paragraph_catalog.py`

Source: [catalogs/restart_paragraph_catalog.py](../../../catalogs/restart_paragraph_catalog.py) | 239 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `328100ac1778b7459d633f46d792e07d4ef6935cd815b5a4bc4aa4435fbec8fe`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Site vocabulary for the restart / checkpoint family.

## Module-level bindings

`PARAGRAPH_SUFFIXES` (L58), `TABLE_SUFFIXED_ROLES` (L71), `PARAGRAPH_NAME_TEMPLATE` (L73), `TABLE_PARAGRAPH_NAME_TEMPLATE` (L74), `QUERYNO_SELECT` (L84), `QUERYNO_UPDATE` (L85), `QUERYNO_INSERT` (L86), `DEFAULT_RESTART_RECORD` (L95), `DEFAULT_READ_COUNT_FIELD` (L96), `DEFAULT_RESTART_KEY_FIELD` (L97), `DEFAULT_INPUT_COUNTER` (L98), `DEFAULT_COMMIT_COUNTER` (L99), `DEFAULT_INPUT_SAVE_AREA` (L100), `DEFAULT_PROGRAM_CONSTANT` (L101), `DEFAULT_RUN_DATE_FIELD` (L102), `DEFAULT_READ_PARAGRAPH` (L104), `DEFAULT_ERROR_PARAGRAPH` (L105), `DEFAULT_ABEND_MODULE` (L106), `DEFAULT_SQL_LOCATION_FIELD` (L110), `__all__` (L218)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from rules.restart_standard_rules import ROLE_ABEND, ROLE_COMMIT, ROLE_CONTROL, ROLE_INSERT, ROLE_RESTART_FOUND, ROLE_SELECT, ROLE_UPDATE, ROLE_WRITE_RESTART
```

## Local dependency notes

- [rules/restart_standard_rules.py](../rules/restart_standard_rules.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/restart/restart_config.py](../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_name_resolver.py](../converter/generators/restart/restart_name_resolver.md)
- [converter/generators/restart/restart_sql_builder.py](../converter/generators/restart/restart_sql_builder.md)
- [converter/resolvers/restart_role_resolver.py](../converter/resolvers/restart_role_resolver.md)
- [tests/restart/conftest.py](../tests/restart/conftest.md)
- [tests/restart/test_m10_role_resolver.py](../tests/restart/test_m10_role_resolver.md)
- [tests/restart/test_m10b_stage_adapter.py](../tests/restart/test_m10b_stage_adapter.md)
- [tests/restart/test_m2_restart_config.py](../tests/restart/test_m2_restart_config.md)
- [tests/restart/test_m4_sql_builder.py](../tests/restart/test_m4_sql_builder.md)

## Symbol contracts and control points

### `RestartDclgenRole` - L118-L182

```python
class RestartDclgenRole()
```

Column, host-field and retention data of the restart table.

Declared class/data-model fields:

```python
table_name: str
include_name: str
host_record: str
program_column: str
program_field: str
phase_column: str
phase_field: str
date_column: str
date_field: str
status_column: str
status_field: str
retention_column: str
retention_field: str
payload_column: str
payload_group: str
payload_len_field: str
payload_text_field: str
retention_days: int = 0
```

### `RestartDclgenRole.columns` - L150-L159

```python
columns(self) -> tuple[str, ...]
```

Column list, in the order the manual reference writes them.

### `RestartDclgenRole.host_fields` - L161-L174

```python
host_fields(self) -> tuple[str, ...]
```

Host fields paired one-for-one with columns().

### `RestartDclgenRole.key_pairs` - L176-L182

```python
key_pairs(self) -> tuple[tuple[str, str], ...]
```

(column, host field) for each predicate of the checkpoint key.

### `production_restart_role` - L185-L215

```python
production_restart_role() -> RestartDclgenRole
```

Standard restart DCLGEN role.

Observed calls (lexical order): `RestartDclgenRole`.

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
