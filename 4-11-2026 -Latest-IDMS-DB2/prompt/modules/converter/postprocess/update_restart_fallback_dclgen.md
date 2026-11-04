# `converter/postprocess/update_restart_fallback_dclgen.py`

Source: [converter/postprocess/update_restart_fallback_dclgen.py](../../../../converter/postprocess/update_restart_fallback_dclgen.py) | 72 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `524f10c3783940b9008e48cbf5a10f209f09808cd1c79e2e72668a551ae0d435`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fallback DZ01RSTV DCLGEN role when restart-table metadata is unavailable.

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.update_metadata_models import DclgenRoleInfo
```

## Local dependency notes

- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_restart_fallback_dclgen.py](../../tests/test_restart_fallback_dclgen.md)

## Symbol contracts and control points

### `create_fallback_restart_dclgen_role` - L28-L72

```python
create_fallback_restart_dclgen_role() -> DclgenRoleInfo
```

Create a standard DZ01RSTV DCLGEN role from production definitions.

Observed calls (lexical order): `DclgenRoleInfo`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
