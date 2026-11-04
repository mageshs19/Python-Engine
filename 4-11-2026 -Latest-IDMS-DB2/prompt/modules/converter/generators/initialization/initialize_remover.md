# `converter/generators/initialization/initialize_remover.py`

Source: [converter/generators/initialization/initialize_remover.py](../../../../../converter/generators/initialization/initialize_remover.py) | 87 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `62f41f2c51d5fdb8e187686771ae48204e23cfa4f0d885a3720a5513af39faa4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L87)

## Import declarations

```python
from __future__ import annotations
from typing import List, Set, Tuple
from converter.generators.initialization.line_geometry import LineGeometry
from patterns.initialization_scope_patterns import INITIALIZE_PATTERN
from rules.initialization_placement_rules import STATEMENT_TERMINATOR
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)

## Symbol contracts and control points

### `InitializeRemover` - L10-L84

```python
class InitializeRemover()
```

### `InitializeRemover.__init__` - L12-L13

```python
__init__(self, geometry: LineGeometry | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`.

### `InitializeRemover.remove` - L15-L35

```python
remove(self, lines: List[str], groups: Set[str]) -> Tuple[List[str], int]
```

Observed calls (lexical order): `set`, `str`, `str(group or '').upper`, `list`, `self._doomed_indexes`, `enumerate`, `output.append`, `self._carries_terminator`, `self._restore_terminator`, `len`.

Control points:

- L21: `if not targets`
- L25: `if not doomed`
- L29: `for (index, line) in enumerate(lines)`
- L30: `if index not in doomed`
- L33: `if self._carries_terminator(line)`

### `InitializeRemover.groups_present` - L37-L45

```python
groups_present(self, lines: List[str]) -> Set[str]
```

Observed calls (lexical order): `set`, `self.geometry.is_comment_or_blank`, `INITIALIZE_PATTERN.match`, `self.geometry.body`, `found.add`, `match.group`, `match.group('group').upper`.

Control points:

- L39: `for line in lines`
- L40: `if self.geometry.is_comment_or_blank(line)`
- L43: `if match`

### `InitializeRemover._doomed_indexes` - L47-L61

```python
_doomed_indexes(self, lines: List[str], targets: Set[str]) -> Set[int]
```

Observed calls (lexical order): `set`, `enumerate`, `self.geometry.is_comment_or_blank`, `INITIALIZE_PATTERN.match`, `self.geometry.body`, `match.group`, `match.group('group').upper`, `doomed.add`.

Control points:

- L53: `for (index, line) in enumerate(lines)`
- L54: `if self.geometry.is_comment_or_blank(line)`
- L57: `if not match`
- L59: `if match.group('group').upper() in targets`

### `InitializeRemover._carries_terminator` - L63-L66

```python
_carries_terminator(self, line: str) -> bool
```

Observed calls (lexical order): `self.geometry.body`, `self.geometry.body(line).rstrip`, `self.geometry.body(line).rstrip().endswith`.

### `InitializeRemover._restore_terminator` - L68-L78

```python
_restore_terminator(self, output: List[str]) -> None
```

Observed calls (lexical order): `self._last_executable`, `self.geometry.body`, `self.geometry.body(output[position]).rstrip`, `body.endswith`, `self.geometry.replace_body`.

Control points:

- L70: `if position < 0`
- L73: `if not body or body.endswith(STATEMENT_TERMINATOR)`

### `InitializeRemover._last_executable` - L80-L84

```python
_last_executable(self, output: List[str]) -> int
```

Observed calls (lexical order): `len`, `range`, `self.geometry.is_comment_or_blank`.

Control points:

- L81: `for position in range(len(output) - 1, -1, -1)`
- L82: `if not self.geometry.is_comment_or_blank(output[position])`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
