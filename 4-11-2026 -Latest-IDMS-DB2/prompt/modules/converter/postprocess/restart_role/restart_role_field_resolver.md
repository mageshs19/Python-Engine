# `converter/postprocess/restart_role/restart_role_field_resolver.py`

Source: [converter/postprocess/restart_role/restart_role_field_resolver.py](../../../../../converter/postprocess/restart_role/restart_role_field_resolver.py) | 115 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `f46cb73ea3f05d4d1b7971e4d0f7ee505388c71186df1f05a7f79600eb09eb32`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from rules.update_restart_rules import RESTART_DCLGEN_ROLE_TOKENS, RESTART_PAYLOAD_FALLBACK_TOKEN_KEY, RESTART_PAYLOAD_TOKEN_KEY, RESTART_VARCHAR_SUFFIXES
```

## Local dependency notes

- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_restart_dclgen_role_builder.py](../update_restart_dclgen_role_builder.md)

## Symbol contracts and control points

### `RestartRoleFieldResolver` - L11-L115

```python
class RestartRoleFieldResolver()
```

Resolves restart columns, fields, and payload child fields.

### `RestartRoleFieldResolver._payload_exclude_tokens` - L18-L22

```python
_payload_exclude_tokens(self) -> list[str]
```

### `RestartRoleFieldResolver._resolve_payload_group` - L24-L58

```python
_resolve_payload_group(self, rows: list[dict[str, str]]) -> str
```

Observed calls (lexical order): `self._payload_exclude_tokens`, `self.matcher.find_optional_field`, `self.matcher.find_optional_col`, `hasattr`, `self.row_mapper.column_to_cobol_field`, `payload_column.replace`, `self.matcher.find_field`.

Control points:

- L35: `if payload_group`
- L46: `if payload_column and hasattr(self.row_mapper, 'column_to_cobol_field')`
- L48: `if payload_column`

### `RestartRoleFieldResolver._resolve_payload_child_field` - L60-L89

```python
_resolve_payload_child_field(self, *, rows: list[dict[str, str]], payload_group: str, token_key: str, fallback_token_key: str, suffix_key: str) -> str
```

Observed calls (lexical order): `self.matcher.find_optional_field`, `self._derive_varchar_field`, `explicit_child.endswith`, `explicit_child.startswith`.

Control points:

- L77: `if explicit_child`
- L78: `if explicit_child == payload_group`
- L82: `if explicit_child.endswith(suffix)`
- L84: `if payload_group and explicit_child.startswith(payload_group)`

### `RestartRoleFieldResolver._derive_varchar_field` - L91-L97

```python
_derive_varchar_field(self, *, payload_group: str, suffix_key: str) -> str
```

Observed calls (lexical order): `payload_group.endswith`.

Control points:

- L92: `if not payload_group`
- L95: `if payload_group.endswith(suffix)`

### `RestartRoleFieldResolver._find_column` - L99-L106

```python
_find_column(self, *, rows: list[dict[str, str]], token_key: str, fallback_token_key: str) -> str
```

Observed calls (lexical order): `self.matcher.find_col`.

### `RestartRoleFieldResolver._find_field` - L108-L115

```python
_find_field(self, *, rows: list[dict[str, str]], token_key: str, fallback_token_key: str) -> str
```

Observed calls (lexical order): `self.matcher.find_field`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
