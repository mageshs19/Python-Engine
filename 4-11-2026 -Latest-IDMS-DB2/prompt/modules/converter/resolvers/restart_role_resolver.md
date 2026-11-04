# `converter/resolvers/restart_role_resolver.py`

Source: [converter/resolvers/restart_role_resolver.py](../../../../converter/resolvers/restart_role_resolver.py) | 238 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `d23d49bb86aedeb969d5335cdbac21e8b8e38254c4752fee15511445e2fd69f1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the M2 RestartDclgenRole from the three site authorities.

## Module-level bindings

`MESSAGE_PREFIX` (L52), `SHEET_AUTHORITY_FIELD` (L55), `SITE_AUTHORITY_FIELD` (L58), `DCLGEN_ALIASES` (L62), `__all__` (L232)

## Import declarations

```python
from __future__ import annotations
import dataclasses
from typing import Any
from catalogs.restart_paragraph_catalog import RestartDclgenRole
from rules.restart_standard_rules import NOT_APPLICABLE_REASONS
```

## Local dependency notes

- [catalogs/restart_paragraph_catalog.py](../../catalogs/restart_paragraph_catalog.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_stage_adapter.py](../composers/restart/restart_stage_adapter.md)
- [tests/restart/test_m10_role_resolver.py](../../tests/restart/test_m10_role_resolver.md)
- [tests/restart/test_m10b_stage_adapter.py](../../tests/restart/test_m10b_stage_adapter.md)

## Symbol contracts and control points

### `RestartRoleResolver` - L67-L229

```python
class RestartRoleResolver()
```

Assembles one RestartDclgenRole, or refuses and says why.

### `RestartRoleResolver.__init__` - L70-L77

```python
__init__(self, mapping_repository: Any=None, table_name_resolver: Any=None) -> None
```

### `RestartRoleResolver.resolve` - L82-L111

```python
resolve(self, *, dclgen_role: Any=None, record_name: str='', table_hint: str='', retention_days: int=0) -> tuple[RestartDclgenRole | None, list[str]]
```

Return (role, messages). The role is None when refused.

Observed calls (lexical order): `self._say`, `list`, `self._table_name`, `self._retention`, `self._collect`, `len`, `RestartDclgenRole`.

Control points:

- L93: `if dclgen_role is None`
- L101: `if missing`
- L102: `for name in missing`

### `RestartRoleResolver._table_name` - L116-L149

```python
_table_name(self, record_name: str, table_hint: str, dclgen_role: Any) -> str
```

Observed calls (lexical order): `self._say`, `str`, `str(record_name or '').strip`, `repository.db2_table_for_record`, `str(repository.db2_table_for_record(record) or '').strip`, `str(table_hint or '').strip`, `self._has_table`, `self._resolve_table`, `self._report_disagreement`.

Control points:

- L123: `if repository is None`
- L132: `if record`
- L136: `if not mapped and hint and self._has_table(hint)`
- L140: `if not mapped`

### `RestartRoleResolver._has_table` - L151-L153

```python
_has_table(self, name: str) -> bool
```

Observed calls (lexical order): `getattr`, `bool`, `callable`, `checker`.

### `RestartRoleResolver._resolve_table` - L155-L159

```python
_resolve_table(self, mapped: str) -> str
```

Observed calls (lexical order): `mapped.upper`, `resolver.resolve_table`, `str`, `str(resolver.resolve_table(mapped) or mapped).upper`.

Control points:

- L157: `if resolver is None`

### `RestartRoleResolver._report_disagreement` - L161-L169

```python
_report_disagreement(self, resolved: str, dclgen_role: Any) -> None
```

Observed calls (lexical order): `str`, `str(getattr(dclgen_role, SHEET_AUTHORITY_FIELD, '') or '').strip`, `str(getattr(dclgen_role, SHEET_AUTHORITY_FIELD, '') or '').strip().upper`, `getattr`, `self._say`.

Control points:

- L165: `if declared and resolved and (declared != resolved)`

### `RestartRoleResolver._retention` - L174-L185

```python
_retention(self, retention_days: int) -> int
```

Observed calls (lexical order): `int`, `self._say`.

Control points:

- L179: `if value <= 0`

### `RestartRoleResolver._collect` - L190-L212

```python
_collect(self, dclgen_role: Any, table: str, retention: int) -> tuple[dict[str, Any], list[str]]
```

Observed calls (lexical order): `dataclasses.fields`, `self._from_dclgen`, `self._is_filled`, `missing.append`.

Control points:

- L199: `for field in dataclasses.fields(RestartDclgenRole)`
- L201: `if name == SHEET_AUTHORITY_FIELD`
- L203: `if name == SITE_AUTHORITY_FIELD`
- L209: `if not self._is_filled(value)`

### `RestartRoleResolver._from_dclgen` - L215-L220

```python
_from_dclgen(dclgen_role: Any, name: str) -> str
```

Observed calls (lexical order): `DCLGEN_ALIASES.get`, `getattr`, `str`, `str(getattr(dclgen_role, attribute, '') or '').strip`, `value.upper`.

Control points:

- L216: `for attribute in DCLGEN_ALIASES.get(name, (name,))`
- L218: `if value`

### `RestartRoleResolver._is_filled` - L223-L226

```python
_is_filled(value: Any) -> bool
```

Observed calls (lexical order): `isinstance`, `bool`, `str`, `str(value or '').strip`.

Control points:

- L224: `if isinstance(value, int)`

### `RestartRoleResolver._say` - L228-L229

```python
_say(self, message: str) -> None
```

Observed calls (lexical order): `self.messages.append`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
