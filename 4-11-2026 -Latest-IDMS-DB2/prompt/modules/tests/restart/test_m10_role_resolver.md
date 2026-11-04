# `tests/restart/test_m10_role_resolver.py`

Source: [tests/restart/test_m10_role_resolver.py](../../../../tests/restart/test_m10_role_resolver.py) | 206 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `82af7f8f078b6278fe069c3a7a9e42c34b67702c19bc85fedb437520c837a4fc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M10 - RestartRoleResolver.

## Module-level bindings

`RECORD` (L32), `SHEET_TABLE` (L33), `DCLGEN_TABLE` (L34), `RETENTION` (L35)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import types
import pytest
from catalogs.restart_paragraph_catalog import RestartDclgenRole
from converter.resolvers.restart_role_resolver import SHEET_AUTHORITY_FIELD, SITE_AUTHORITY_FIELD, RestartRoleResolver
import converter.resolvers.restart_role_resolver as module
```

## Local dependency notes

- [catalogs/restart_paragraph_catalog.py](../../catalogs/restart_paragraph_catalog.md)
- [converter/resolvers/restart_role_resolver.py](../../converter/resolvers/restart_role_resolver.md)

## Symbol contracts and control points

### `_Mapping` - L38-L48

```python
class _Mapping()
```

Minimal stand-in for MappingRepository.

### `_Mapping.__init__` - L41-L42

```python
__init__(self, table: str=SHEET_TABLE) -> None
```

### `_Mapping.db2_table_for_record` - L44-L45

```python
db2_table_for_record(self, record_name: str) -> str
```

### `_Mapping.has_table` - L47-L48

```python
has_table(self, table_name: str) -> bool
```

Observed calls (lexical order): `bool`, `self.table.upper`, `table_name.upper`.

### `_dclgen` - L51-L64

```python
_dclgen(**overrides)
```

A complete DCLGEN role, generated from the role's own fields.

Observed calls (lexical order): `dataclasses.fields`, `field.name.upper`, `values.pop`, `values.update`, `types.SimpleNamespace`.

Control points:

- L54: `for field in dataclasses.fields(RestartDclgenRole)`
- L55: `if field.name == SITE_AUTHORITY_FIELD`
- L57: `if field.name == SHEET_AUTHORITY_FIELD`

### `resolver` - L68-L69

```python
resolver()
```

Observed calls (lexical order): `RestartRoleResolver`, `_Mapping`.

### `resolved` - L73-L79

```python
resolved(resolver)
```

Observed calls (lexical order): `resolver.resolve`, `_dclgen`.

### `test_a_complete_input_builds_a_role` - L85-L87

```python
test_a_complete_input_builds_a_role(resolved)
```

Observed calls (lexical order): `isinstance`.

### `test_every_declared_field_is_filled` - L90-L94

```python
test_every_declared_field_is_filled(resolved)
```

Observed calls (lexical order): `dataclasses.fields`, `getattr`.

Control points:

- L92: `for field in dataclasses.fields(RestartDclgenRole)`

### `test_the_table_name_comes_from_sheet_mapping` - L97-L101

```python
test_the_table_name_comes_from_sheet_mapping(resolved)
```

The DCLGEN member names something else on purpose.

### `test_the_disagreement_is_reported` - L104-L107

```python
test_the_disagreement_is_reported(resolved)
```

Observed calls (lexical order): `any`.

### `test_the_columns_come_from_the_dclgen` - L110-L113

```python
test_the_columns_come_from_the_dclgen(resolved)
```

### `test_the_host_record_alias_is_translated` - L116-L118

```python
test_the_host_record_alias_is_translated(resolved)
```

### `test_the_retention_comes_from_site_metadata` - L121-L123

```python
test_the_retention_comes_from_site_metadata(resolved)
```

### `test_a_confirmed_hint_is_accepted` - L126-L133

```python
test_a_confirmed_hint_is_accepted(resolver)
```

Observed calls (lexical order): `resolver.resolve`, `_dclgen`, `any`.

### `test_a_missing_dclgen_refuses` - L139-L142

```python
test_a_missing_dclgen_refuses(resolver)
```

Observed calls (lexical order): `resolver.resolve`.

### `test_no_mapping_repository_refuses` - L145-L150

```python
test_no_mapping_repository_refuses()
```

Observed calls (lexical order): `RestartRoleResolver`, `RestartRoleResolver().resolve`, `_dclgen`, `any`.

### `test_an_unmapped_record_refuses` - L153-L158

```python
test_an_unmapped_record_refuses(resolver)
```

Observed calls (lexical order): `resolver.resolve`, `_dclgen`, `any`.

### `test_no_retention_refuses` - L161-L167

```python
test_no_retention_refuses(resolver)
```

Principle C: the generator never picks a number.

Observed calls (lexical order): `resolver.resolve`, `_dclgen`, `any`.

### `test_one_empty_dclgen_entry_refuses_the_whole_role` - L170-L177

```python
test_one_empty_dclgen_entry_refuses_the_whole_role(resolver)
```

Observed calls (lexical order): `resolver.resolve`, `_dclgen`, `any`.

### `test_a_refusal_never_returns_a_partial_role` - L180-L186

```python
test_a_refusal_never_returns_a_partial_role(resolver)
```

Observed calls (lexical order): `resolver.resolve`, `_dclgen`.

### `test_resolving_twice_produces_an_equal_role` - L192-L199

```python
test_resolving_twice_produces_an_equal_role(resolver)
```

Observed calls (lexical order): `resolver.resolve`, `_dclgen`.

### `test_the_catalogued_role_is_never_used` - L202-L206

```python
test_the_catalogued_role_is_never_used()
```

M10 exists to stop a catalogued name reaching generated SQL.

Observed calls (lexical order): `hasattr`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
