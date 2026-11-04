# `review/checks/chk_23_host_variable_exactness.py`

Source: [review/checks/chk_23_host_variable_exactness.py](../../../../review/checks/chk_23_host_variable_exactness.py) | 182 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `95357bf0ef426d3f3fccc92d8cddd971183d6ed3f1ffebbcabea6337471d2586`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-23 DCLGEN host variable name exactness.

## Module-level bindings

`HOST_DOT` (L11), `QUALIFIED` (L12)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import metadata as meta, sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `HostVariableExactnessCheck` - L17-L182

```python
class HostVariableExactnessCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-23'
TITLE = 'DCLGEN host variable name exactness'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 230
```

### `HostVariableExactnessCheck.relevant` - L24-L25

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`, `meta.dclgen_tables`.

### `HostVariableExactnessCheck.not_relevant_reason` - L27-L28

```python
not_relevant_reason(self) -> str
```

### `HostVariableExactnessCheck.review` - L30-L130

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `std.DCLGEN_GROUP_PREFIX.upper`, `self._all_hosts`, `self._hosts_by_group`, `self._sql_references`, `self._cobol_references`, `record.skip`, `record.expect_all`, `sorted`, `self._resolves`, `group_hosts.get`, `set`, `meta.dclgen_tables`, `group.startswith`, `len`.

Control points:

- L39: `if not std.ENFORCE_HOST_NAME_EXACTNESS`
- L44: `if not sql_refs`
- L60: `if not sql_refs`
- L79: `if not cobol_refs`
- L97: `if not cobol_refs`

### `HostVariableExactnessCheck._resolves` - L134-L148

```python
_resolves(field: str, hosts: set[str]) -> bool
```

True when a name is a DCLGEN host or a VARCHAR subfield of one.

Observed calls (lexical order): `field.endswith`, `len`.

Control points:

- L143: `if field in hosts`
- L145: `for suffix in std.VARCHAR_SUBFIELD_SUFFIXES`
- L146: `if field.endswith(suffix) and field[:-len(suffix)] in hosts`

### `HostVariableExactnessCheck._all_hosts` - L151-L155

```python
_all_hosts(ctx) -> set[str]
```

Observed calls (lexical order): `set`, `meta.dclgen_tables`, `meta.hosts_for_table`, `meta.hosts_for_table(ctx, table).values`, `out.update`.

Control points:

- L153: `for table in meta.dclgen_tables(ctx)`

### `HostVariableExactnessCheck._hosts_by_group` - L158-L165

```python
_hosts_by_group(ctx) -> dict[str, set[str]]
```

Observed calls (lexical order): `std.DCLGEN_GROUP_PREFIX.upper`, `meta.dclgen_tables`, `set`, `meta.hosts_for_table`, `meta.hosts_for_table(ctx, table).values`.

Control points:

- L161: `for table in meta.dclgen_tables(ctx)`

### `HostVariableExactnessCheck._sql_references` - L168-L173

```python
_sql_references(view) -> set[tuple[str, str]]
```

Observed calls (lexical order): `match.group`, `sql.sql_blocks`, `HOST_DOT.finditer`.

### `HostVariableExactnessCheck._cobol_references` - L176-L182

```python
_cobol_references(view, prefix: str) -> set[tuple[str, str]]
```

Observed calls (lexical order): `set`, `QUALIFIED.finditer`, `sql.norm`, `match.group`, `match.group('group').startswith`, `out.add`.

Control points:

- L178: `for line in view.code`
- L179: `for match in QUALIFIED.finditer(sql.norm(line.logical))`
- L180: `if match.group('group').startswith(prefix)`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
