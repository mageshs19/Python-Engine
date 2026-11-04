# `converter/generators/restart/restart_storage_builder.py`

Source: [converter/generators/restart/restart_storage_builder.py](../../../../../converter/generators/restart/restart_storage_builder.py) | 277 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `1f2c09339e5a92d270a7bb874f570ffa4fd46eccf8f94f1fc2fdc232a017bb60`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the WORKING-STORAGE the restart family depends on.

## Module-level bindings

`REQUIRED_NAMES` (L111), `REQUIRED_SIZES` (L120), `__all__` (L273)

## Import declarations

```python
from __future__ import annotations
from catalogs.restart_storage_catalog import DATE_GROUP, DATE_GROUP_LINES, EOF_CONDITION_SUFFIX, EOF_SWITCH_PREFIX, HELP_GROUP, NOT_EOF_CONDITION_SUFFIX, SWITCH_GROUP
from converter.generators.restart.restart_config import RestartConfig
from converter.services.name_derivation_resolver import NameDerivationResolver
from rules.restart_storage_templates import ENFORCE_RESTART_STORAGE, EOF_FALSE_VALUE, EOF_TRUE_VALUE, HELP_GROUP_TEMPLATE, RESTART_STORAGE_MESSAGES, SWITCH_GROUP_TEMPLATE
```

## Local dependency notes

- [catalogs/restart_storage_catalog.py](../../../catalogs/restart_storage_catalog.md)
- [converter/generators/restart/restart_config.py](restart_config.md)
- [converter/services/name_derivation_resolver.py](../../services/name_derivation_resolver.md)
- [rules/restart_storage_templates.py](../../../rules/restart_storage_templates.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_storage_injector.py](../../composers/restart/restart_storage_injector.md)
- [tests/restart/test_m11_storage_builder.py](../../../tests/restart/test_m11_storage_builder.md)
- [tests/restart/test_m5_storage_builder_derives_record.py](../../../tests/restart/test_m5_storage_builder_derives_record.md)

## Symbol contracts and control points

### `RestartStorageBuilder` - L126-L270

```python
class RestartStorageBuilder()
```

Renders the restart working storage, or refuses and says why.

### `RestartStorageBuilder.__init__` - L129-L140

```python
__init__(self, config: RestartConfig, name_derivation_resolver: NameDerivationResolver | None=None) -> None
```

Observed calls (lexical order): `NameDerivationResolver`.

### `RestartStorageBuilder.build` - L145-L168

```python
build(self) -> tuple[str, ...]
```

Every group, in declaration order. Empty when refused.

Observed calls (lexical order): `self._log`, `self._usable`, `lines.extend`, `self.switch_group`, `lines.append`, `self.help_group`, `self.date_group`, `len`, `line.strip`, `', '.join`, `tuple`.

Control points:

- L149: `if not ENFORCE_RESTART_STORAGE`
- L153: `if not self._usable()`

### `RestartStorageBuilder.switch_group` - L170-L180

```python
switch_group(self) -> tuple[str, ...]
```

The EOF switch and its two condition names.

Observed calls (lexical order): `self.eof_switch`, `self.eof_condition`, `self.not_eof_condition`, `line.format`, `tuple`.

### `RestartStorageBuilder.help_group` - L182-L196

```python
help_group(self) -> tuple[str, ...]
```

Restart record, input save area and the two counters.

Observed calls (lexical order): `line.format`, `tuple`.

### `RestartStorageBuilder.date_group` - L198-L202

```python
date_group(self) -> tuple[str, ...]
```

The date conversion layout, from the catalog.

Observed calls (lexical order): `tuple`, `line.format`.

### `RestartStorageBuilder.eof_switch` - L207-L209

```python
eof_switch(self) -> str
```

Observed calls (lexical order): `self._record`.

### `RestartStorageBuilder.eof_condition` - L211-L213

```python
eof_condition(self) -> str
```

Observed calls (lexical order): `self._record`.

### `RestartStorageBuilder.not_eof_condition` - L215-L217

```python
not_eof_condition(self) -> str
```

Observed calls (lexical order): `self._record`.

### `RestartStorageBuilder._record` - L219-L243

```python
_record(self) -> str
```

The record name every generated identifier in this group is built on - DERIVED to its final DB2 spelling.

Observed calls (lexical order): `str`, `str(self.config.names.record_name or '').strip`, `str(self.config.names.record_name or '').strip().upper`, `self._name_resolver.derive`, `str(derived or source).strip`, `str(derived or source).strip().upper`.

Control points:

- L240: `if not source`

### `RestartStorageBuilder._usable` - L248-L262

```python
_usable(self) -> bool
```

Observed calls (lexical order): `getattr`, `str`, `str(getattr(names, name, '') or '').strip`, `self._log`, `int`.

Control points:

- L252: `for name in REQUIRED_NAMES`
- L253: `if not str(getattr(names, name, '') or '').strip()`
- L257: `for size in REQUIRED_SIZES`
- L258: `if int(getattr(names, size, 0) or 0) <= 0`

### `RestartStorageBuilder._log` - L267-L270

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `RESTART_STORAGE_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L269: `if template`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
