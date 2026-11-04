# `converter/postprocess/restart_role/restart_role_factory.py`

Source: [converter/postprocess/restart_role/restart_role_factory.py](../../../../../converter/postprocess/restart_role/restart_role_factory.py) | 32 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `e59ba008f57d3a010834449e8bb6ee55575ebdc40c2719c040f829b99a5f721a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from dataclasses import fields, is_dataclass
from converter.postprocess.update_metadata_models import DclgenRoleInfo
```

## Local dependency notes

- [converter/postprocess/update_metadata_models.py](../update_metadata_models.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_restart_dclgen_role_builder.py](../update_restart_dclgen_role_builder.md)

## Symbol contracts and control points

### `RestartRoleFactory` - L8-L32

```python
class RestartRoleFactory()
```

Constructs DclgenRoleInfo while staying compatible with the model.

### `RestartRoleFactory._make_role` - L15-L32

```python
_make_role(self, **values: str) -> DclgenRoleInfo
```

Observed calls (lexical order): `is_dataclass`, `fields`, `values.items`, `DclgenRoleInfo`, `hasattr`, `setattr`.

Control points:

- L16: `if is_dataclass(DclgenRoleInfo)`
- L25: `for (key, value) in values.items()`
- L26: `if not hasattr(role, key)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
