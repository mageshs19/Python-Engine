# `converter/postprocess/update_restart_dclgen_row_mapper.py`

Source: [converter/postprocess/update_restart_dclgen_row_mapper.py](../../../../converter/postprocess/update_restart_dclgen_row_mapper.py) | 148 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `b83c758ed7308c6d5feba6c9cefada70dfb4632f13ffdb2bfa9027f66ce874b0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from typing import Any
from catalogs.dclgen_schema import DCLGEN_GROUP_PREFIX
from converter.postprocess.update_metadata_models import include_from_label, upper, value
```

## Local dependency notes

- [catalogs/dclgen_schema.py](../../catalogs/dclgen_schema.md)
- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_restart_dclgen_resolver.py](update_restart_dclgen_resolver.md)
- [converter/postprocess/update_restart_dclgen_role_builder.py](update_restart_dclgen_role_builder.md)

## Symbol contracts and control points

### `UpdateRestartDclgenRowMapper` - L13-L148

```python
class UpdateRestartDclgenRowMapper()
```

Converts parsed DCLGEN column objects into normalized row dictionaries.

### `UpdateRestartDclgenRowMapper.column_row` - L31-L136

```python
column_row(self, item: Any) -> dict[str, str]
```

Observed calls (lexical order): `upper`, `value`, `include_from_label`.

Control points:

- L63: `if not include_name`
- L105: `if not host_record and table_name`

### `UpdateRestartDclgenRowMapper.first_value` - L138-L148

```python
first_value(self, rows: list[dict[str, str]], key: str) -> str
```

Observed calls (lexical order): `row.get`, `str`, `str(row.get(key, '') or '').strip`.

Control points:

- L143: `for row in rows`
- L145: `if text`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
