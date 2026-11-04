# `converter/postprocess/update_restart_dclgen_resolver.py`

Source: [converter/postprocess/update_restart_dclgen_resolver.py](../../../../converter/postprocess/update_restart_dclgen_resolver.py) | 107 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `26d862836d108d1413df25a88913e9b7c15ab615ff6d39caffb14fa11ff08ebf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`RESTART_TABLE_NAME_HINTS` (L23), `__all__` (L104)

## Import declarations

```python
from __future__ import annotations
from typing import Any, Optional
from converter.postprocess.update_metadata_models import DclgenRoleInfo, upper
from converter.postprocess.update_restart_dclgen_matcher import UpdateRestartDclgenMatcher
from converter.postprocess.update_restart_dclgen_role_builder import UpdateRestartDclgenRoleBuilder
from converter.postprocess.update_restart_dclgen_row_mapper import UpdateRestartDclgenRowMapper
```

## Local dependency notes

- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)
- [converter/postprocess/update_restart_dclgen_matcher.py](update_restart_dclgen_matcher.md)
- [converter/postprocess/update_restart_dclgen_role_builder.py](update_restart_dclgen_role_builder.md)
- [converter/postprocess/update_restart_dclgen_row_mapper.py](update_restart_dclgen_row_mapper.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)

## Symbol contracts and control points

### `UpdateRestartDclgenResolver` - L26-L101

```python
class UpdateRestartDclgenResolver()
```

Selects the restart DCLGEN group by TABLE NAME (deterministic) and delegates role-building.

### `UpdateRestartDclgenResolver.__init__` - L40-L52

```python
__init__(self, *, row_mapper: UpdateRestartDclgenRowMapper | None=None, role_builder: UpdateRestartDclgenRoleBuilder | None=None, matcher: UpdateRestartDclgenMatcher | None=None) -> None
```

Observed calls (lexical order): `UpdateRestartDclgenRowMapper`, `UpdateRestartDclgenMatcher`, `UpdateRestartDclgenRoleBuilder`.

### `UpdateRestartDclgenResolver.resolve_restart_dclgen` - L54-L69

```python
resolve_restart_dclgen(self, dclgen_columns: list[Any], mapping_repository: Any | None=None) -> Optional[DclgenRoleInfo]
```

Observed calls (lexical order): `self._group_columns_by_dclgen`, `self._find_restart_group_by_table_name`, `self.role_builder.build_restart_roles`.

Control points:

- L62: `if not restart_group`

### `UpdateRestartDclgenResolver._group_columns_by_dclgen` - L71-L85

```python
_group_columns_by_dclgen(self, dclgen_columns: list[Any]) -> dict[str, list[Any]]
```

Group parsed DCLGEN columns by their resolved DB2 table name.

Observed calls (lexical order): `self.row_mapper.column_row`, `row.get`, `upper`, `groups.setdefault`, `groups.setdefault(group_key, []).append`.

Control points:

- L78: `for item in dclgen_columns`
- L81: `if not group_key`

### `UpdateRestartDclgenResolver._find_restart_group_by_table_name` - L87-L101

```python
_find_restart_group_by_table_name(self, groups: dict[str, list[Any]]) -> Optional[tuple[str, list[Any]]]
```

Deterministically pick the restart DCLGEN group by table name.

Observed calls (lexical order): `groups.items`, `upper`, `any`.

Control points:

- L96: `for (group_key, columns) in groups.items()`
- L98: `if any((hint in table_name for hint in RESTART_TABLE_NAME_HINTS))`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
