# `converter/resolvers/restart_context_builder.py`

Source: [converter/resolvers/restart_context_builder.py](../../../../converter/resolvers/restart_context_builder.py) | 210 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `0686b6c02c81df72496ced3baef8671c498f90b77a725eec404fce4d3fa5b133`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the run-scoped context the restart pass needs.

## Module-level bindings

`MESSAGE_PREFIX` (L66), `RESOLVER_METHOD` (L67), `__all__` (L210)

## Import declarations

```python
from __future__ import annotations
from typing import Any
from catalogs.restart_site_catalog import RESTART_RETENTION_DAYS
from catalogs.restart_trigger_catalog import CHECKPOINT_VERBS, LEGACY_CHECKPOINT_RECORDS
from converter.composers.restart.restart_stage_adapter import RestartRunContext
from converter.composers.restart.restart_injection_composer import PROGRAM_KIND_RETRIEVAL, PROGRAM_KIND_UPDATE
```

## Local dependency notes

- [catalogs/restart_site_catalog.py](../../catalogs/restart_site_catalog.md)
- [catalogs/restart_trigger_catalog.py](../../catalogs/restart_trigger_catalog.md)
- [converter/composers/restart/restart_injection_composer.py](../composers/restart/restart_injection_composer.md)
- [converter/composers/restart/restart_stage_adapter.py](../composers/restart/restart_stage_adapter.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline_steps.py](../pipeline/conversion/conversion_pipeline_steps.md)

## Symbol contracts and control points

### `RestartContextBuilder` - L70-L207

```python
class RestartContextBuilder()
```

Turns conversion inputs into a RestartRunContext, or refuses.

### `RestartContextBuilder.__init__` - L73-L77

```python
__init__(self, dclgen_resolver: Any=None) -> None
```

Observed calls (lexical order): `self._verify`.

Control points:

- L76: `if dclgen_resolver is not None`

### `RestartContextBuilder.build` - L82-L134

```python
build(self, *, source_text: str, dclgen_columns: Any=(), is_update: bool=False, retention_days: int=RESTART_RETENTION_DAYS, totals: tuple[str, ...]=()) -> tuple[RestartRunContext | None, list[str]]
```

Observed calls (lexical order): `tuple`, `self._say`, `RestartRunContext`, `list`, `self._checkpoint_record`, `self._dclgen_role`, `getattr`, `str`, `str(getattr(role, 'table_name', '') or '').strip`, `int`, `self._report_totals`.

Control points:

- L97: `if not is_update`
- L105: `if not record`
- L115: `if role is None`

### `RestartContextBuilder._checkpoint_record` - L140-L155

```python
_checkpoint_record(source_text: str) -> str
```

The first checkpoint record the source ACTS on.

Observed calls (lexical order): `' '.join`, `str`, `str(source_text or '').upper`, `str(source_text or '').upper().split`, `str(record).upper`, `any`.

Control points:

- L147: `for record in LEGACY_CHECKPOINT_RECORDS`
- L149: `if any((f'{verb} {name}' in text for verb in CHECKPOINT_VERBS))`
- L151: `if any((f'{verb} CURRENT {name}' in text for verb in CHECKPOINT_VERBS))`

### `RestartContextBuilder._dclgen_role` - L160-L175

```python
_dclgen_role(self, dclgen_columns: Any) -> Any
```

Observed calls (lexical order): `self._say`, `getattr`, `list`, `method`.

Control points:

- L161: `if self.dclgen_resolver is None`
- L170: `if role is None`

### `RestartContextBuilder._report_totals` - L180-L193

```python
_report_totals(self, totals: tuple[str, ...]) -> None
```

Say what arrived. Silence is what hid the defect.

Observed calls (lexical order): `self._say`, `len`.

Control points:

- L182: `if totals`

### `RestartContextBuilder._verify` - L199-L204

```python
_verify(resolver: Any) -> None
```

Observed calls (lexical order): `callable`, `getattr`, `TypeError`, `type`.

Control points:

- L200: `if not callable(getattr(resolver, RESOLVER_METHOD, None))`

Explicit raises: `TypeError(f'RestartContextBuilder needs a resolver exposing {RESOLVER_METHOD}(); got {type(resolver).__name__}.')`.

### `RestartContextBuilder._say` - L206-L207

```python
_say(self, message: str) -> None
```

Observed calls (lexical order): `self.messages.append`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
