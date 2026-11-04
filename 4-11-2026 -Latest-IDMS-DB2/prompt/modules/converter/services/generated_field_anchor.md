# `converter/services/generated_field_anchor.py`

Source: [converter/services/generated_field_anchor.py](../../../../converter/services/generated_field_anchor.py) | 161 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `ae1ffc8921b5fa0f90a2a1a658f4f07ce3567b3903796a6a77c2b64fda6b329d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`CREATED_GROUP_OFFSET` (L20), `__all__` (L161)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from converter.services.working_storage_group_selector import WorkingStorageGroupSelector
from rules.structural_safety_rules import GENERATED_FIELD_CHILD_INDENT, GENERATED_FIELD_CHILD_LEVEL, GENERATED_FIELD_GROUP_ALIASES, GENERATED_FIELD_GROUP_MARKER, GENERATED_FIELD_GROUP_NAME, GENERATED_FIELD_GROUP_TEMPLATE, PREFERRED_WORK_GROUP_NAMES, STRUCTURAL_SAFETY_MESSAGES, UNIFY_GENERATED_FIELD_GROUP
from converter.composers.counter_declaration.counter_line_factory import CounterLineFactory
```

## Local dependency notes

- [converter/composers/counter_declaration/counter_line_factory.py](../composers/counter_declaration/counter_line_factory.md)
- [converter/services/working_storage_group_selector.py](working_storage_group_selector.md)
- [rules/structural_safety_rules.py](../../rules/structural_safety_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/counter_anchor_resolver.py](../composers/counter_declaration/counter_anchor_resolver.md)
- [converter/generators/timestamp/cs_program_declarator.py](../generators/timestamp/cs_program_declarator.md)
- [tests/generated_fields/conftest.py](../../tests/generated_fields/conftest.md)

## Symbol contracts and control points

### `FieldAnchor` - L24-L34

```python
class FieldAnchor()
```

Declared class/data-model fields:

```python
insert_index: int = -1
template_line: str = ''
level: str = ''
indent: str = ''
group: str = ''
created: bool = False
```

### `FieldAnchor.is_usable` - L33-L34

```python
is_usable(self) -> bool
```

Observed calls (lexical order): `bool`.

### `GeneratedFieldAnchorResolver` - L37-L158

```python
class GeneratedFieldAnchorResolver()
```

### `GeneratedFieldAnchorResolver.__init__` - L39-L54

```python
__init__(self, line_factory=None, selector: WorkingStorageGroupSelector | None=None) -> None
```

Observed calls (lexical order): `CounterLineFactory`, `WorkingStorageGroupSelector`, `getattr`.

Control points:

- L44: `if line_factory is None`

### `GeneratedFieldAnchorResolver.resolve` - L56-L80

```python
resolve(self, lines: list[str]) -> tuple[list[str], FieldAnchor]
```

Observed calls (lexical order): `FieldAnchor`, `list`, `self.selector.analyze`, `self._from_names`, `self._log`, `self._report_refusals`, `self._create_group`.

Control points:

- L59: `if not UNIFY_GENERATED_FIELD_GROUP`
- L65: `if anchor is not None`
- L70: `if anchor is not None`
- L76: `if layout.working_storage_index < 0`

### `GeneratedFieldAnchorResolver._from_names` - L82-L86

```python
_from_names(self, lines, layout, names) -> FieldAnchor | None
```

Observed calls (lexical order): `layout.named`, `self._anchor_for`.

Control points:

- L84: `if group is None`

### `GeneratedFieldAnchorResolver._anchor_for` - L88-L112

```python
_anchor_for(self, lines, group) -> FieldAnchor | None
```

Observed calls (lexical order): `len`, `FieldAnchor`, `self.lines.body_indent`.

Control points:

- L89: `if not group.can_take_child`
- L93: `if index < 0 or index > len(lines)`
- L96: `if group.has_children`

### `GeneratedFieldAnchorResolver._create_group` - L114-L142

```python
_create_group(self, lines: list[str], boundary_index: int) -> tuple[list[str], FieldAnchor]
```

Observed calls (lexical order): `len`, `max`, `self.lines.comment`, `self.lines.statement`, `GENERATED_FIELD_GROUP_TEMPLATE.format`, `self._log`, `FieldAnchor`.

Control points:

- L120: `if insert_at < 0 or insert_at > len(lines)`

### `GeneratedFieldAnchorResolver._report_refusals` - L144-L149

```python
_report_refusals(self, layout) -> None
```

Observed calls (lexical order): `self._log`, `layout.childless_safe`.

Control points:

- L145: `for group in layout.groups`
- L146: `if group.is_record_layout`
- L148: `for group in layout.childless_safe()`

### `GeneratedFieldAnchorResolver._log` - L151-L158

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `STRUCTURAL_SAFETY_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L153: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
