# `mainframe/verification/cobol_storage_layout.py`

Source: [mainframe/verification/cobol_storage_layout.py](../../../../mainframe/verification/cobol_storage_layout.py) | 138 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `225c4b685e26a5bbe747498f832729332e0c55c795daf6cbd67225ac76b3ecf5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Strict, independent byte-size verifier for COBOL fixed-record groups.

## Module-level bindings

`_DECL` (L12), `_PIC` (L13), `_REDEF` (L14), `_PIC_ELEMENT` (L15), `_OCCURS` (L16)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
```

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/verification/copybook_provenance.py](copybook_provenance.md)
- [mainframe/verification/group_representation_contract.py](group_representation_contract.md)
- [mainframe/verification/record_population_contract.py](record_population_contract.md)
- [mainframe/verification/record_write_contract.py](record_write_contract.md)
- [tests/test_cobol_storage_layout.py](../../tests/test_cobol_storage_layout.md)
- [tests/test_copybook_provenance_and_occurs.py](../../tests/test_copybook_provenance_and_occurs.md)

## Symbol contracts and control points

### `Field` - L20-L25

```python
class Field()
```

Declared class/data-model fields:

```python
level: int
name: str
source: str
children: list['Field'] = field(default_factory=list)
parent: 'Field | None' = None
```

### `_body` - L28-L33

```python
_body(raw: str) -> str
```

Observed calls (lexical order): `len`, `raw[:6].isdigit`, `raw[7:72].strip`, `raw.lstrip`, `raw.lstrip().startswith`, `raw.strip`.

Control points:

- L29: `if len(raw) >= 7 and raw[:6].isdigit()`
- L30: `if raw[6] in {'*', '/', 'D', 'd'}`

### `extract_group` - L36-L71

```python
extract_group(text: str, group_name: str) -> Field
```

Extract the named level-01 group, preserving hierarchy and PIC continuations.

Observed calls (lexical order): `group_name.upper`, `text.splitlines`, `_body`, `_DECL.match`, `int`, `match.group`, `match.group(2).upper`, `Field`, `match.group(3).strip`, `stack.pop`, `ValueError`, `stack[-1].children.append`, `stack.append`.

Control points:

- L41: `for line in text.splitlines()`
- L43: `if not code`
- L46: `if match`
- L48: `if root is None`
- L49: `if level != 1 or name != target`
- L54: `if level == 88`
- L57: `if level <= root.level`
- L59: `while stack and stack[-1].level >= level`
- Another 3 conditions/loops exist in this source span.

Explicit raises: `ValueError('invalid COBOL level hierarchy')`; `ValueError(f'level-01 group {target} not found')`.

### `_picture_bytes` - L74-L95

```python
_picture_bytes(node: Field) -> int
```

Observed calls (lexical order): `node.source.upper`, `re.search`, `ValueError`, `_PIC.search`, `match.group`, `match.group(1).upper`, `_PIC_ELEMENT.findall`, `int`, `sum`.

Control points:

- L76: `if re.search('\\b(?:DEPENDING|SIGN\\s+IS\\s+|USAGE\\s+(?:IS\\s+)?(?:COMP|BINARY|COMP-1|COMP-2)|SYNCHRONIZED)\\b', src)`
- L79: `if not match`
- L82: `if re.search('[^9XANZVS()0-9]', pic)`
- L85: `if not parts`
- L89: `if 'COMP-3' in src or 'PACKED-DECIMAL' in src`
- L90: `if kind != {'9'}`
- L93: `if re.search('\\bCOMP(?:UTATIONAL)?(?:-[0-9]+)?\\b', src)`

Explicit raises: `ValueError(f'unsupported storage declaration {node.name}: {src}')`; `ValueError(f'leaf without PIC {node.name}: {src}')`; `ValueError(f'unsupported PIC {node.name}: {pic}')`; `ValueError(f'unrecognised PIC {node.name}: {pic}')`; `ValueError(f'packed field is not numeric {node.name}')`; `ValueError(f'unsupported binary storage {node.name}: {src}')`.

### `_field_bytes` - L98-L129

```python
_field_bytes(node: Field) -> int
```

Observed calls (lexical order): `node.source.upper`, `re.search`, `_OCCURS.search`, `ValueError`, `_OCCURS.search(src).group`, `int`, `_picture_bytes`, `_PIC.search`, `_field_bytes`, `_REDEF.search`, `redefine.group`, `redefine.group(1).upper`, `max`.

Control points:

- L100: `if re.search('\\bOCCURS\\b', src) and (not _OCCURS.search(src) or re.search('\\b(?:DEPENDING|TO\\s+\\d+|UNTIL)\\b', src))`
- L105: `if repeat < 1 or repeat > 100000`
- L107: `if not node.children`
- L109: `if _PIC.search(node.source)`
- L113: `for child in node.children`
- L116: `if redefine`
- L118: `if target not in offsets`
- L125: `if child.name != 'FILLER'`
- Another 1 conditions/loops exist in this source span.

Explicit raises: `ValueError(f'unsupported variable or malformed OCCURS {node.name}: {src}')`; `ValueError(f'unsafe OCCURS count for {node.name}: {repeat}')`; `ValueError(f'group has PIC and children: {node.name}')`; `ValueError(f'{child.name} REDEFINES unknown preceding sibling {target}')`; `ValueError(f'nonunique data name {child.name} at same level')`.

### `group_byte_length` - L132-L133

```python
group_byte_length(text: str, group_name: str) -> int
```

Observed calls (lexical order): `_field_bytes`, `extract_group`.

### `child_byte_lengths` - L136-L138

```python
child_byte_lengths(text: str, group_name: str) -> dict[str, int]
```

Observed calls (lexical order): `extract_group`, `_field_bytes`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
