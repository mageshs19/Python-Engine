# `converter/services/db2_date_sentinel_policy.py`

Source: [converter/services/db2_date_sentinel_policy.py](../../../../converter/services/db2_date_sentinel_policy.py) | 133 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `16d3ca98e3846a5d992a755579d07f9d5578449655fd89e76c79f4bcc716e91c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The single owner of the DB2 null-date sentinel decision.

## Module-level bindings

`__all__` (L133)

## Import declarations

```python
from __future__ import annotations
from rules.db2_date_sentinel_rules import DB2_DATE_SENTINEL_MESSAGES, DCLGEN_NAME_PREFIX, DCLGEN_QUALIFIER_TOKENS, ENFORCE_DB2_DATE_NULL_SENTINEL, PARM_DATE_SOURCE_NAMES, PARM_DATE_SOURCE_PREFIXES, PARM_DATE_SOURCE_SUFFIXES, SENTINEL_GUARD_BODY_INDENT, SENTINEL_GUARD_CLOSE, SENTINEL_GUARD_MOVE, SENTINEL_GUARD_OPEN
```

## Local dependency notes

- [rules/db2_date_sentinel_rules.py](../../rules/db2_date_sentinel_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/date_move_builder.py](../composers/update_sql_cleanup/date_move_builder.md)
- [converter/generators/sql/sql_date_move_builder.py](../generators/sql/sql_date_move_builder.md)
- [converter/postprocess/update_date_host_converter.py](../postprocess/update_date_host_converter.md)
- [tests/db2_date_sentinel/test_parm_sourced_date_has_no_sentinel.py](../../tests/db2_date_sentinel/test_parm_sourced_date_has_no_sentinel.md)

## Symbol contracts and control points

### `Db2DateSentinelPolicy` - L55-L130

```python
class Db2DateSentinelPolicy()
```

Decides whether a date move needs the null-date guard.

### `Db2DateSentinelPolicy.__init__` - L58-L60

```python
__init__(self, sentinel: str) -> None
```

Observed calls (lexical order): `str`, `str(sentinel or '').strip`.

### `Db2DateSentinelPolicy.guard_lines` - L65-L82

```python
guard_lines(self, source: str, indent: str='') -> list[str]
```

The guard, indented, or \[\] when the source cannot be unset.

Observed calls (lexical order): `self._normalize`, `self._say`, `self.is_dclgen_qualified`, `self._render`, `self.is_parm_sourced`.

Control points:

- L69: `if not ENFORCE_DB2_DATE_NULL_SENTINEL`
- L73: `if self.is_dclgen_qualified(name)`
- L77: `if self.is_parm_sourced(name)`

### `Db2DateSentinelPolicy.is_parm_sourced` - L84-L97

```python
is_parm_sourced(self, source: str) -> bool
```

True when the value is supplied by the JCL PARM.

Observed calls (lexical order): `self._normalize`, `name.endswith`, `name.startswith`.

Control points:

- L88: `if not name`
- L91: `if name in PARM_DATE_SOURCE_NAMES`
- L94: `if name.endswith(PARM_DATE_SOURCE_SUFFIXES)`

### `Db2DateSentinelPolicy.is_dclgen_qualified` - L99-L109

```python
is_dclgen_qualified(self, source: str) -> bool
```

True when the value is read from a DB2 column.

Observed calls (lexical order): `self._normalize`, `name.startswith`, `any`.

Control points:

- L103: `if not name`
- L106: `if name.startswith(DCLGEN_NAME_PREFIX)`

### `Db2DateSentinelPolicy._render` - L114-L121

```python
_render(self, indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `SENTINEL_GUARD_MOVE.format`.

### `Db2DateSentinelPolicy._normalize` - L124-L125

```python
_normalize(source: str) -> str
```

Observed calls (lexical order): `' '.join`, `' '.join(str(source or '').split()).upper`, `str`, `str(source or '').split`.

### `Db2DateSentinelPolicy._say` - L127-L130

```python
_say(self, key: str, **fields: object) -> None
```

Observed calls (lexical order): `DB2_DATE_SENTINEL_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L129: `if template`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
