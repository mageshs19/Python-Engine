# `mainframe/verification/group_representation_contract.py`

Source: [mainframe/verification/group_representation_contract.py](../../../../mainframe/verification/group_representation_contract.py) | 216 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `ee3f1e852716c785e4fe3e2c78a6051e10e68bea4ae0f9f4de1414a2d0ca0438`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reject unconverted DB2 character-to-packed group transfers.

## Module-level bindings

`_DECL` (L17), `_NONDISPLAY` (L18), `_QUALIFIER` (L19), `_MOVE` (L20), `_CHAR_TYPE` (L24)

## Import declarations

```python
from __future__ import annotations
from bisect import bisect_right
from dataclasses import dataclass, field
import re
from typing import Iterable
from .cobol_storage_layout import group_byte_length
```

## Local dependency notes

- [mainframe/verification/cobol_storage_layout.py](cobol_storage_layout.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_semantic_release_gate.py](../zowe_semantic_release_gate.md)
- [review/checks/chk_35_group_representation.py](../../review/checks/chk_35_group_representation.md)
- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)

## Symbol contracts and control points

### `_body` - L27-L36

```python
_body(raw: str) -> str
```

Observed calls (lexical order): `len`, `raw[:6].isdigit`, `raw[:7].isspace`, `raw.lstrip`, `raw.lstrip().startswith`, `raw.strip`.

Control points:

- L28: `if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace())`
- L29: `if raw[6] in '*/Dd'`
- L32: `if raw.lstrip().startswith(('*', '/'))`

### `_masked` - L39-L41

```python
_masked(text: str) -> str
```

Observed calls (lexical order): `''.join`, `m.group`, `re.sub`.

### `_Node` - L45-L64

```python
class _Node()
```

Declared class/data-model fields:

```python
level: int
name: str
clause: str
line: int
parent: '_Node | None' = None
children: list['_Node'] = field(default_factory=list)
```

### `_Node.descendants` - L53-L56

```python
descendants(self) -> Iterable['_Node']
```

Observed calls (lexical order): `child.descendants`.

Control points:

- L54: `for child in self.children`

### `_Node.ancestors` - L58-L64

```python
ancestors(self) -> tuple[str, ...]
```

Observed calls (lexical order): `values.append`, `tuple`.

Control points:

- L61: `while parent is not None`

### `_nodes` - L67-L105

```python
_nodes(text: str) -> list[_Node]
```

Observed calls (lexical order): `enumerate`, `text.splitlines`, `_body`, `re.match`, `re.search`, `_DECL.match`, `int`, `match.group`, `stack.pop`, `_Node`, `match.group(2).upper`, `match.group(3).strip`, `node.parent.children.append`, `nodes.append`, `stack.append`.

Control points:

- L72: `for (number, raw) in enumerate(text.splitlines(), 1)`
- L74: `if re.match('^DATA\\s+DIVISION\\b', body, re.I)`
- L76: `if re.match('^PROCEDURE\\s+DIVISION\\b', body, re.I)`
- L78: `if not in_data`
- L80: `if re.match('^EXEC\\s+SQL\\b', body, re.I)`
- L82: `if in_sql`
- L83: `if re.search('\\bEND-EXEC\\b', body, re.I)`
- L86: `if re.match('^[A-Z-]+\\s+SECTION\\b|^FD\\s|^SD\\s', body, re.I)`
- Another 5 conditions/loops exist in this source span.

### `_node_size` - L108-L112

```python
_node_size(node: _Node) -> int
```

Observed calls (lexical order): `node.descendants`, `'\n'.join`, `group_byte_length`.

### `_column_key` - L115-L117

```python
_column_key(column) -> tuple[str, str]
```

Observed calls (lexical order): `str`, `str(column.table_name).strip`, `str(column.table_name).strip().upper`, `str(column.table_name).strip().upper().replace`, `str(column.cobol_host_name).strip`, `str(column.cobol_host_name).strip().upper`, `str(column.cobol_host_name).strip().upper().replace`.

### `GroupRepresentationFinding` - L121-L126

```python
class GroupRepresentationFinding()
```

Declared class/data-model fields:

```python
code: str
line: int
source: str
target: str
message: str
```

### `audit_character_group_moves` - L129-L180

```python
audit_character_group_moves(text: str, columns: Iterable) -> tuple[GroupRepresentationFinding, ...]
```

Detect scalar CHAR hosts copied without conversion to packed groups.

Observed calls (lexical order): `_column_key`, `by_host.setdefault`, `by_host.setdefault(_column_key(column), []).append`, `_nodes`, `_body`, `text.splitlines`, `enumerate`, `len`, `next`, `re.match`, `'\n'.join`, `_masked`, `re.finditer`, `match.end`, `offsets.append`, `_MOVE.finditer`.
Another 23 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L137: `for column in columns`
- L145: `for match in re.finditer('\n', code)`
- L148: `for match in _MOVE.finditer(code)`
- L150: `if not candidates`
- L154: `if not host_type`
- L162: `if len(qualified) != 1`
- L164: `if len(qualified) > 1`
- L169: `if not node.children or not any((_NONDISPLAY.search(n.clause) for n in [node, *node.descendants()]))`

### `audit_target_character_widths` - L183-L216

```python
audit_target_character_widths(text: str, rows: Iterable, columns: Iterable) -> tuple[GroupRepresentationFinding, ...]
```

Compare declared target CHAR widths, scoped to hosts used by this member.

Observed calls (lexical order): `'\n'.join`, `_body`, `_masked`, `text.splitlines`, `set`, `_CHAR_TYPE.match`, `str`, `str(column.db2_type).strip`, `_column_key`, `re.escape`, `re.search`, `str(column.column_name).upper`, `str(column.table_name).strip`, `str(column.table_name).strip().upper`, `str(row.new_db2_record).strip`, `str(row.new_db2_record).strip().upper`.
Another 12 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L192: `for column in columns`
- L194: `if not target_type`
- L198: `if not (re.search('\\b' + re.escape(host) + '\\b', code, re.I) or re.search('\\b' + re.escape(str(column.column_name).upper()) + '\\b', code, re.I))`
- L201: `for row in rows`
- L202: `if str(row.new_db2_record).strip().upper() != str(column.table_name).strip().upper()`
- L204: `if str(row.new_db2_field_name).strip().upper() != str(column.column_name).strip().upper()`
- L207: `if not sheet_type or int(sheet_type.group(1)) == int(target_type.group(1))`
- L210: `if identity in seen`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
