# `converter/postprocess/update_restart_dclgen_role_builder.py`

Source: [converter/postprocess/update_restart_dclgen_role_builder.py](../../../../converter/postprocess/update_restart_dclgen_role_builder.py) | 124 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `39f50dc2ce5a2964fad5824e33a7cd8e37ac87cc100184a54b07f5b066f4b371`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from typing import Any
from catalogs.dclgen_schema import DCLGEN_GROUP_PREFIX
from converter.postprocess.restart_role.restart_role_factory import RestartRoleFactory
from converter.postprocess.restart_role.restart_role_field_resolver import RestartRoleFieldResolver
from converter.postprocess.update_metadata_models import DclgenRoleInfo
from converter.postprocess.update_restart_dclgen_matcher import UpdateRestartDclgenMatcher
from converter.postprocess.update_restart_dclgen_row_mapper import UpdateRestartDclgenRowMapper
from rules.update_restart_rules import RESTART_PAYLOAD_FALLBACK_TOKEN_KEY, RESTART_PAYLOAD_LENGTH_SPEC, RESTART_PAYLOAD_TEXT_SPEC, RESTART_PAYLOAD_TOKEN_KEY, RESTART_ROLE_COLUMN_FIELD_SPEC
```

## Local dependency notes

- [catalogs/dclgen_schema.py](../../catalogs/dclgen_schema.md)
- [converter/postprocess/restart_role/restart_role_factory.py](restart_role/restart_role_factory.md)
- [converter/postprocess/restart_role/restart_role_field_resolver.py](restart_role/restart_role_field_resolver.md)
- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)
- [converter/postprocess/update_restart_dclgen_matcher.py](update_restart_dclgen_matcher.md)
- [converter/postprocess/update_restart_dclgen_row_mapper.py](update_restart_dclgen_row_mapper.md)
- [rules/update_restart_rules.py](../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_restart_dclgen_resolver.py](update_restart_dclgen_resolver.md)

## Symbol contracts and control points

### `UpdateRestartDclgenRoleBuilder` - L28-L124

```python
class UpdateRestartDclgenRoleBuilder(RestartRoleFieldResolver, RestartRoleFactory)
```

Builds DclgenRoleInfo from the selected restart DCLGEN column group.

### `UpdateRestartDclgenRoleBuilder.__init__` - L40-L47

```python
__init__(self, *, row_mapper: UpdateRestartDclgenRowMapper | None=None, matcher: UpdateRestartDclgenMatcher | None=None) -> None
```

Observed calls (lexical order): `UpdateRestartDclgenRowMapper`, `UpdateRestartDclgenMatcher`.

### `UpdateRestartDclgenRoleBuilder.build_restart_roles` - L49-L124

```python
build_restart_roles(self, *, group_key: str, columns: list[Any]) -> DclgenRoleInfo
```

Observed calls (lexical order): `self.row_mapper.column_row`, `self.row_mapper.first_value`, `self._resolve_payload_group`, `self._resolve_payload_child_field`, `RESTART_ROLE_COLUMN_FIELD_SPEC.items`, `self._find_column`, `self._find_field`, `self._make_role`.

Control points:

- L62: `if not host_record and table_name`
- L83: `for (role, (token_key, fallback_key)) in RESTART_ROLE_COLUMN_FIELD_SPEC.items()`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
