# `tests/restart/test_every_tested_88_is_set.py`

Source: [tests/restart/test_every_tested_88_is_set.py](../../../../tests/restart/test_every_tested_88_is_set.py) | 269 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `de93802916ccab13044cfac9340afa4d2dfc78c1c866d982589eeff68771da9e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Structural guards on generated COBOL switch logic.

## Module-level bindings

`BODY_START` (L59), `BODY_END` (L60), `LEVEL_88` (L62), `DATA_ITEM` (L63), `PROCEDURE_DIVISION` (L64), `CONDITION_REF` (L66), `SET_TRUE` (L67), `MOVE_TO` (L68), `RELATIONAL_HEAD` (L72), `QUALIFIER` (L73), `RESERVED` (L75), `FRESH` (L186), `NEW2_SHAPE` (L223), `RELATIONAL_SHAPE` (L232), `SIBLING_SHAPE` (L239)

## Import declarations

```python
from __future__ import annotations
import re
from pathlib import Path
import pytest
```

## Symbol contracts and control points

### `_is_comment` - L81-L83

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `line.rstrip`, `len`.

### `_body` - L86-L92

```python
_body(line: str) -> str
```

Observed calls (lexical order): `line.rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L88: `if len(text) >= BODY_END and text[:6].strip().isdigit()`
- L90: `if len(text) > BODY_START and text[:6].strip().isdigit()`

### `_logical_lines` - L95-L103

```python
_logical_lines(text: str) -> list[str]
```

Observed calls (lexical order): `text.splitlines`, `_is_comment`, `' '.join`, `_body`, `_body(raw).upper`, `_body(raw).upper().split`, `out.append`.

Control points:

- L97: `for raw in text.splitlines()`
- L98: `if _is_comment(raw)`
- L101: `if body`

### `_declared_conditions` - L106-L121

```python
_declared_conditions(lines: list[str]) -> dict[str, str]
```

88 condition name -> the switch it is subordinate to.

Observed calls (lexical order): `PROCEDURE_DIVISION.match`, `LEVEL_88.match`, `match88.group`, `DATA_ITEM.match`, `item.group`.

Control points:

- L110: `for body in lines`
- L111: `if PROCEDURE_DIVISION.match(body)`
- L114: `if match88`
- L115: `if parent`
- L119: `if item`

### `_condition_references` - L124-L155

```python
_condition_references(lines: list[str]) -> set[str]
```

Names used where a CONDITION NAME is required - IF x / UNTIL x.

Observed calls (lexical order): `set`, `CONDITION_REF.finditer`, `match.group`, `body[match.end():].lstrip`, `match.end`, `QUALIFIER.match`, `QUALIFIER.sub`, `QUALIFIER.sub('', tail, count=1).lstrip`, `tail.startswith`, `RELATIONAL_HEAD.match`, `found.add`.

Control points:

- L139: `for body in lines`
- L140: `for match in CONDITION_REF.finditer(body)`
- L142: `if name in RESERVED`
- L146: `while QUALIFIER.match(tail)`
- L149: `if tail.startswith('(')`
- L151: `if RELATIONAL_HEAD.match(tail)`

### `_written_switches` - L158-L168

```python
_written_switches(lines: list[str], conditions: dict[str, str]) -> set[str]
```

Every switch some statement writes.

Observed calls (lexical order): `set`, `SET_TRUE.finditer`, `conditions.get`, `match.group`, `written.add`, `MOVE_TO.finditer`.

Control points:

- L161: `for body in lines`
- L162: `for match in SET_TRUE.finditer(body)`
- L164: `if parent`
- L166: `for match in MOVE_TO.finditer(body)`

### `_fresh_update_outputs` - L171-L183

```python
_fresh_update_outputs() -> list[Path]
```

Observed calls (lexical order): `Path`, `Path('.').rglob`, `list`, `f.stat`, `max`, `out_dir.glob`.

### `test_a1_every_condition_name_reference_is_declared` - L190-L200

```python
test_a1_every_condition_name_reference_is_declared(cbl: Path)
```

COMPILE: an undefined condition name does not assemble.

Observed calls (lexical order): `_logical_lines`, `cbl.read_text`, `_declared_conditions`, `_condition_references`, `set`, `sorted`.

### `test_a2_every_tested_switch_is_written` - L204-L220

```python
test_a2_every_tested_switch_is_written(cbl: Path)
```

LOGIC: a switch no statement writes cannot end a loop.

Observed calls (lexical order): `_logical_lines`, `cbl.read_text`, `_declared_conditions`, `_written_switches`, `_condition_references`, `set`, `sorted`.

### `test_guard_detects_the_new2_shape` - L250-L254

```python
test_guard_detects_the_new2_shape()
```

A1 must still catch the defect it was created for.

Observed calls (lexical order): `_logical_lines`, `_declared_conditions`, `_condition_references`, `set`.

### `test_a_relational_test_is_not_a_condition_name` - L257-L260

```python
test_a_relational_test_is_not_a_condition_name()
```

VM4BD302: UNTIL SW-EOF = 1 is a comparison, not a condition.

Observed calls (lexical order): `_logical_lines`, `_condition_references`.

### `test_a_sibling_set_writes_the_whole_switch` - L263-L269

```python
test_a_sibling_set_writes_the_whole_switch()
```

VM1BD526: one storage position; setting EOF falsifies NOT-EOF.

Observed calls (lexical order): `_logical_lines`, `_declared_conditions`, `_written_switches`, `_condition_references`, `set`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
