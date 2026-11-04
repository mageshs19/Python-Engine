# `converter/composers/update/update_audit_repair_composer.py`

Source: [converter/composers/update/update_audit_repair_composer.py](../../../../../converter/composers/update/update_audit_repair_composer.py) | 232 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `76b66a647b28f6d0ca14a83e815a7b81ff2a90fedc05d2851cab724a97a9a9da`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Put the update audit MOVEs back after the restart family rebuilt the business paragraph.

## Module-level bindings

`HOST_REFERENCE_PATTERN` (L66), `COMMENT_INDICATORS` (L71), `UNKNOWN_PARAGRAPH` (L72)

## Import declarations

```python
from __future__ import annotations
import re
from rules.update_audit_repair_rules import AUDIT_TIMESTAMP_COLUMN_PREFIXES, AUDIT_TIMESTAMP_SOURCE_FIELD, AUDIT_USERID_COLUMN_PREFIXES, AUDIT_USERID_SOURCE_FIELD, BLOCK_SCAN_LIMIT, BODY_END_INDEX, BODY_START_INDEX, CONTINUATION_INDENT, CONTINUATION_SPLIT_TOKEN, END_EXEC_TOKEN, ENFORCE_UPDATE_AUDIT_MOVES, EXEC_SQL_TOKEN, INDICATOR_INDEX, LINE_WIDTH, MESSAGES, MOVE_TEMPLATE, PARAGRAPH_SCAN_LIMIT, SEQUENCE_WIDTH, SET_KEYWORD, STATEMENT_INDENT, UPDATE_VERB
```

## Local dependency notes

- [rules/update_audit_repair_rules.py](../../../rules/update_audit_repair_rules.md)

## Symbol contracts and control points

### `UpdateAuditRepairComposer` - L75-L229

```python
class UpdateAuditRepairComposer()
```

Re-asserts the audit MOVEs in front of every business UPDATE.

### `UpdateAuditRepairComposer.__init__` - L78-L82

```python
__init__(self, enabled: bool | None=None) -> None
```

Observed calls (lexical order): `bool`.

### `UpdateAuditRepairComposer.apply` - L87-L163

```python
apply(self, cobol_text: str) -> str
```

Observed calls (lexical order): `self._say`, `cobol_text.splitlines`, `self._targets`, `reversed`, `self._paragraph_start`, `self._paragraph_name`, `self._source_for`, `self._already_moved`, `self._declared`, `self._render`, `len`, `new_lines.extend`, `'\n'.join`.

Control points:

- L90: `if not self.enabled`
- L94: `if not cobol_text`
- L101: `if not targets`
- L109: `for (block_start, hosts) in reversed(targets)`
- L114: `for (host, group) in hosts`
- L116: `if source is None`
- L119: `if self._already_moved(lines, paragraph_start, block_start, host)`
- L130: `if not self._declared(cobol_text, source)`
- Another 2 conditions/loops exist in this source span.

### `UpdateAuditRepairComposer._targets` - L168-L193

```python
_targets(self, lines: list[str]) -> list[tuple[int, list[tuple[str, str]]]]
```

Every EXEC SQL UPDATE block that names at least one audit column.

Observed calls (lexical order): `enumerate`, `self._is_comment`, `self._body`, `self._body(line).upper`, `self._block_end`, `' '.join`, `' '.join((self._body(lines[i]) for i in range(index, end + 1))).upper`, `range`, `self._audit_hosts`, `found.append`.

Control points:

- L172: `for (index, line) in enumerate(lines)`
- L173: `if self._is_comment(line)`
- L175: `if EXEC_SQL_TOKEN not in self._body(line).upper()`
- L179: `if end is None`
- L186: `if UPDATE_VERB not in block or SET_KEYWORD not in block`
- L190: `if hosts`

### `UpdateAuditRepairComposer._block_end` - L195-L202

```python
_block_end(self, lines: list[str], start: int) -> int | None
```

Observed calls (lexical order): `len`, `min`, `range`, `self._is_comment`, `self._body`, `self._body(lines[index]).upper`.

Control points:

- L197: `for index in range(start, limit)`
- L198: `if self._is_comment(lines[index])`
- L200: `if END_EXEC_TOKEN in self._body(lines[index]).upper()`

### `UpdateAuditRepairComposer._audit_hosts` - L204-L219

```python
_audit_hosts(self, block: str) -> list[tuple[str, str]]
```

Audit host variables in SET-clause order, de-duplicated.

Observed calls (lexical order): `set`, `HOST_REFERENCE_PATTERN.finditer`, `match.group`, `match.group('host').upper`, `match.group('group').upper`, `self._source_for`, `seen.add`, `hosts.append`.

Control points:

- L209: `for match in HOST_REFERENCE_PATTERN.finditer(block)`
- L212: `if host in seen`
- L214: `if self._source_for(host) is None`

### `UpdateAuditRepairComposer._source_for` - L222-L229

```python
_source_for(host: str) -> str | None
```

Map a host variable to its audit source field, or None.

Observed calls (lexical order): `host.upper`, `host.upper().replace`, `column.startswith`, `tuple`.

Control points:

- L225: `if column.startswith(tuple(AUDIT_TIMESTAMP_COLUMN_PREFIXES))`
- L227: `if column.startswith(tuple(AUDIT_USERID_COLUMN_PREFIXES))`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
