# `converter/services/working_storage_group_selector.py`

Source: [converter/services/working_storage_group_selector.py](../../../../converter/services/working_storage_group_selector.py) | 216 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `25898653c364d065d2bc9e6b4618c6bf88ae43a3920ea0bde75b8c3cc0eb952e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`COMMENT_PREFIXES` (L22), `PICTURE_TOKENS` (L23), `__all__` (L212)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.structural_safety_patterns import FD_PATTERN, FILE_SECTION_PATTERN, LEVEL_01_PATTERN, LINKAGE_SECTION_PATTERN, MOVE_WHOLE_GROUP_PATTERN, PROCEDURE_DIVISION_PATTERN, READ_INTO_PATTERN, RECORD_VERB_PATTERN, SUBORDINATE_LEVEL_PATTERN, WORKING_STORAGE_PATTERN, WRITE_FROM_PATTERN
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/structural_safety_patterns.py](../../patterns/structural_safety_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/counter_anchor_resolver.py](../composers/counter_declaration/counter_anchor_resolver.md)
- [converter/services/generated_field_anchor.py](generated_field_anchor.md)

## Symbol contracts and control points

### `WorkingStorageGroup` - L27-L52

```python
class WorkingStorageGroup()
```

Declared class/data-model fields:

```python
name: str = ''
header_index: int = -1
first_child_index: int = -1
last_child_index: int = -1
child_level: str = ''
is_record_layout: bool = False
is_elementary: bool = False
```

### `WorkingStorageGroup.has_children` - L37-L38

```python
has_children(self) -> bool
```

Observed calls (lexical order): `bool`.

### `WorkingStorageGroup.is_safe` - L41-L42

```python
is_safe(self) -> bool
```

Observed calls (lexical order): `bool`.

### `WorkingStorageGroup.can_take_child` - L45-L46

```python
can_take_child(self) -> bool
```

### `WorkingStorageGroup.insert_index` - L49-L52

```python
insert_index(self) -> int
```

Control points:

- L50: `if self.last_child_index >= 0`

### `WorkingStorageLayout` - L56-L79

```python
class WorkingStorageLayout()
```

Declared class/data-model fields:

```python
groups: list[WorkingStorageGroup] = field(default_factory=list)
working_storage_index: int = -1
boundary_index: int = -1
```

### `WorkingStorageLayout.safe_groups` - L61-L62

```python
safe_groups(self) -> list[WorkingStorageGroup]
```

### `WorkingStorageLayout.usable_groups` - L64-L65

```python
usable_groups(self) -> list[WorkingStorageGroup]
```

### `WorkingStorageLayout.named` - L67-L73

```python
named(self, names) -> WorkingStorageGroup | None
```

Observed calls (lexical order): `str`, `str(name or '').upper`, `group.name.upper`.

Control points:

- L69: `for name in wanted`
- L70: `for group in self.groups`
- L71: `if group.name.upper() == name and group.can_take_child`

### `WorkingStorageLayout.childless_safe` - L75-L79

```python
childless_safe(self) -> list[WorkingStorageGroup]
```

### `WorkingStorageGroupSelector` - L82-L209

```python
class WorkingStorageGroupSelector()
```

### `WorkingStorageGroupSelector.__init__` - L84-L88

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `WorkingStorageGroupSelector.analyze` - L90-L149

```python
analyze(self, lines: list[str]) -> WorkingStorageLayout
```

Observed calls (lexical order): `WorkingStorageLayout`, `self._record_layout_names`, `enumerate`, `self._logical`, `self._is_comment`, `FILE_SECTION_PATTERN.match`, `WORKING_STORAGE_PATTERN.match`, `LINKAGE_SECTION_PATTERN.match`, `PROCEDURE_DIVISION_PATTERN.match`, `FD_PATTERN.match`, `LEVEL_01_PATTERN.match`, `match.group`, `match.group('name').upper`, `WorkingStorageGroup`, `self._has_picture`, `layout.groups.append`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L98: `for (index, line) in enumerate(lines)`
- L100: `if not body or self._is_comment(body)`
- L103: `if FILE_SECTION_PATTERN.match(body)`
- L108: `if WORKING_STORAGE_PATTERN.match(body)`
- L114: `if LINKAGE_SECTION_PATTERN.match(body) or PROCEDURE_DIVISION_PATTERN.match(body)`
- L120: `if in_file_section or FD_PATTERN.match(body)`
- L123: `if not in_working_storage`
- L127: `if match`
- Another 4 conditions/loops exist in this source span.

### `WorkingStorageGroupSelector.select` - L151-L153

```python
select(self, lines: list[str]) -> WorkingStorageGroup | None
```

Observed calls (lexical order): `self.analyze`, `self.analyze(lines).usable_groups`.

### `WorkingStorageGroupSelector.select_named` - L155-L160

```python
select_named(self, lines: list[str], names) -> WorkingStorageGroup | None
```

Observed calls (lexical order): `self.analyze`, `self.analyze(lines).named`.

### `WorkingStorageGroupSelector._record_layout_names` - L162-L194

```python
_record_layout_names(self, lines: list[str]) -> set[str]
```

Observed calls (lexical order): `set`, `self._logical`, `self._is_comment`, `FILE_SECTION_PATTERN.match`, `WORKING_STORAGE_PATTERN.match`, `LEVEL_01_PATTERN.match`, `match.group`, `match.group('name').upper`, `names.add`, `RECORD_VERB_PATTERN.match`, `pattern.search`, `found.group`, `found.group('name').upper`.

Control points:

- L166: `for line in lines`
- L168: `if not body or self._is_comment(body)`
- L171: `if FILE_SECTION_PATTERN.match(body)`
- L173: `if WORKING_STORAGE_PATTERN.match(body)`
- L176: `if in_file_section`
- L178: `if match`
- L182: `if match`
- L185: `for pattern in (WRITE_FROM_PATTERN, READ_INTO_PATTERN, MOVE_WHOLE_GROUP_PATTERN)`
- Another 1 conditions/loops exist in this source span.

### `WorkingStorageGroupSelector._logical` - L196-L200

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `WorkingStorageGroupSelector._has_picture` - L203-L205

```python
_has_picture(body: str) -> bool
```

Observed calls (lexical order): `str`, `str(body or '').upper`, `any`.

### `WorkingStorageGroupSelector._is_comment` - L208-L209

```python
_is_comment(body: str) -> bool
```

Observed calls (lexical order): `body.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
