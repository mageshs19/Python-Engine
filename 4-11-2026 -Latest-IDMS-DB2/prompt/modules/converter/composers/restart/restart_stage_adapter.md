# `converter/composers/restart/restart_stage_adapter.py`

Source: [converter/composers/restart/restart_stage_adapter.py](../../../../../converter/composers/restart/restart_stage_adapter.py) | 236 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `dfee793b195308a61b27a7f89e874dd9c90901f2806dedfc3331cf1b709842d0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Pipeline-shaped front door for the restart injection.

## Module-level bindings

`MESSAGE_PREFIX` (L60), `__all__` (L232)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Iterable
from converter.composers.restart.restart_injection_composer import PROGRAM_KIND_UPDATE, RestartInjectionComposer
from converter.resolvers.restart_role_resolver import RestartRoleResolver
from converter.generators.restart.restart_totals_resolver import RestartTotalsResolver
from catalogs.restart_storage_catalog import GENERATED_STORAGE_FIELDS
from rules.counter_rules import COUNTER_TOTAL_GUARANTEED_ROLES, COUNTER_TOTAL_MESSAGES
```

## Local dependency notes

- [catalogs/restart_storage_catalog.py](../../../catalogs/restart_storage_catalog.md)
- [converter/composers/restart/restart_injection_composer.py](restart_injection_composer.md)
- [converter/generators/restart/restart_totals_resolver.py](../../generators/restart/restart_totals_resolver.md)
- [converter/resolvers/restart_role_resolver.py](../../resolvers/restart_role_resolver.md)
- [rules/counter_rules.py](../../../rules/counter_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../../pipeline/conversion/conversion_component_factory.md)
- [converter/resolvers/restart_context_builder.py](../../resolvers/restart_context_builder.md)
- [tests/restart/test_m10b_stage_adapter.py](../../../tests/restart/test_m10b_stage_adapter.md)

## Symbol contracts and control points

### `RestartRunContext` - L64-L76

```python
class RestartRunContext()
```

Everything the pass needs that the TEXT cannot supply.

Declared class/data-model fields:

```python
program_kind: str = PROGRAM_KIND_UPDATE
record_name: str = ''
table_hint: str = ''
retention_days: int = 0
dclgen_role: Any = None
totals: tuple[str, ...] = field(default_factory=tuple)
```

### `RestartRunContext.is_update` - L75-L76

```python
is_update(self) -> bool
```

Observed calls (lexical order): `str`, `str(self.program_kind or '').strip`, `str(self.program_kind or '').strip().lower`.

### `RestartStageAdapter` - L79-L230

```python
class RestartStageAdapter()
```

Resolves the role, then runs the restart injection.

### `RestartStageAdapter.__init__` - L82-L98

```python
__init__(self, line_utils, *, context: RestartRunContext | None=None, mapping_repository: Any=None, table_name_resolver: Any=None, shared_cleanups: Iterable[Any]=(), scheme: str | None=None) -> None
```

Observed calls (lexical order): `tuple`.

### `RestartStageAdapter.compose` - L103-L121

```python
compose(self, text: str) -> str
```

Return the converted text. Diagnostics land on .messages.

Observed calls (lexical order): `str`, `self._say`, `self._role`, `self._inject`.

Control points:

- L109: `if context is None`
- L117: `if context.is_update and role is None`

### `RestartStageAdapter._role` - L126-L146

```python
_role(self, context: RestartRunContext) -> Any
```

Resolve the role, or None.

Observed calls (lexical order): `RestartRoleResolver`, `resolver.resolve`, `self.messages.extend`.

Control points:

- L132: `if not context.is_update`

### `RestartStageAdapter._inject` - L151-L169

```python
_inject(self, source: str, context: RestartRunContext, role: Any) -> str
```

Observed calls (lexical order): `RestartInjectionComposer`, `composer.compose`, `self._totals`, `self.messages.extend`.

### `RestartStageAdapter._say` - L171-L172

```python
_say(self, message: str) -> None
```

Observed calls (lexical order): `self.messages.append`.

### `RestartStageAdapter._totals` - L174-L193

```python
_totals(self, source: str, context) -> tuple[str, ...]
```

The end-of-run DISPLAY lines for this program.

Observed calls (lexical order): `tuple`, `RestartTotalsResolver`, `resolver.resolve`, `str`, `str(source or '').splitlines`, `self._guaranteed_counters`, `self.messages.extend`.

Control points:

- L184: `if supplied`

### `RestartStageAdapter._guaranteed_counters` - L195-L215

```python
_guaranteed_counters(self) -> tuple[str, ...]
```

Counter names the restart family will certainly increment.

Observed calls (lexical order): `self._catalogue_name`, `found.append`, `self._say`, `COUNTER_TOTAL_MESSAGES['guarantee_unresolved'].format`, `tuple`.

Control points:

- L204: `for role in COUNTER_TOTAL_GUARANTEED_ROLES`
- L206: `if name`

### `RestartStageAdapter._catalogue_name` - L218-L230

```python
_catalogue_name(role: str) -> str
```

Observed calls (lexical order): `isinstance`, `fields.get`, `str`, `str(fields.get(role) or '').strip`, `str(fields.get(role) or '').strip().upper`, `entry.get`, `str(entry.get('name') or '').strip`, `str(entry.get('name') or '').strip().upper`, `getattr`, `str(getattr(entry, 'name', '') or '').strip`, `str(getattr(entry, 'name', '') or '').strip().upper`.

Control points:

- L221: `if isinstance(fields, dict)`
- L224: `for entry in fields or ()`
- L225: `if isinstance(entry, dict) and str(entry.get('role')) == role`
- L227: `if getattr(entry, 'role', None) == role`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
