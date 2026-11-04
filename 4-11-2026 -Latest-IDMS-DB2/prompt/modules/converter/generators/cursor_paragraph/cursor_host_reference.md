# `converter/generators/cursor_paragraph/cursor_host_reference.py`

Source: [converter/generators/cursor_paragraph/cursor_host_reference.py](../../../../../converter/generators/cursor_paragraph/cursor_host_reference.py) | 113 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `e8fafc8c8c32b459aa233e076ab365f5c373c6d2518e6aa0b96269c08104b552`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Parses a DB2 host reference into its DCLGEN group and field.

## Module-level bindings

`OF_KEYWORD` (L31), `PREDICATE_SEPARATOR` (L32), `__all__` (L107)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from rules.cursor_paragraph_rules import HOST_GROUP_SEPARATOR, HOST_REFERENCE_PREFIX
```

## Local dependency notes

- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_fetch_paragraph.py](cursor_fetch_paragraph.md)

## Symbol contracts and control points

### `HostReference` - L36-L44

```python
class HostReference()
```

One DCLGEN host field and the group that owns it.

Declared class/data-model fields:

```python
field: str = ''
group: str = ''
```

### `HostReference.is_qualified` - L43-L44

```python
is_qualified(self) -> bool
```

Observed calls (lexical order): `bool`.

### `parse` - L47-L71

```python
parse(reference: str) -> HostReference
```

Split any accepted host spelling. Unqualified yields group "".

Observed calls (lexical order): `str`, `str(reference or '').strip`, `text.startswith`, `len`, `text[len(HOST_REFERENCE_PREFIX):].strip`, `HostReference`, `text.upper`, `upper.rindex`, `text[:cut].strip`, `text[:cut].strip().upper`, `text[cut + len(OF_KEYWORD):].strip`, `text[cut + len(OF_KEYWORD):].strip().upper`, `text.partition`, `field.strip`, `field.strip().upper`, `group.strip`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L50: `if text.startswith(HOST_REFERENCE_PREFIX)`
- L52: `if not text`
- L57: `if OF_KEYWORD in upper`
- L64: `if HOST_GROUP_SEPARATOR in text`

### `from_where_condition` - L74-L86

```python
from_where_condition(condition: str) -> HostReference
```

The host named on the RIGHT of one WHERE predicate.

Observed calls (lexical order): `str`, `str(condition or '').strip`, `HostReference`, `parse`, `text.split`.

Control points:

- L84: `if PREDICATE_SEPARATOR not in text`

### `group_of` - L89-L95

```python
group_of(host_variables: list[str] | None) -> str
```

The DCLGEN group owning a FETCH INTO list, or "".

Observed calls (lexical order): `parse`.

Control points:

- L91: `for host in host_variables or []`
- L93: `if reference.group`

### `qualified_pairs` - L98-L104

```python
qualified_pairs(host_variables: list[str] | None) -> list[HostReference]
```

Every QUALIFIED host in a list. Unqualified entries are skipped.

Observed calls (lexical order): `parse`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
