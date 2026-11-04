# `converter/composers/record_materialisation/record_move_scanner.py`

Source: [converter/composers/record_materialisation/record_move_scanner.py](../../../../../converter/composers/record_materialisation/record_move_scanner.py) | 138 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `3d85b868f53b583282572f0bb078cd450ecb5de8d7c0f637ece9702c2834753e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Locates whole-record MOVE statements and their target fields.

## Module-level bindings

`__all__` (L138)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.record_materialisation.record_line_utils import RecordLineUtils
from converter.composers.record_materialisation.record_picture_sizer import RecordPictureSizer
from converter.composers.record_materialisation.record_sites import MoveSite, TargetSite
from patterns.record_materialisation_patterns import PROCEDURE_DIVISION_PATTERN, TARGET_FIELD_PATTERN_TEMPLATE, WHOLE_RECORD_MOVE_PATTERN
```

## Local dependency notes

- [converter/composers/record_materialisation/record_line_utils.py](record_line_utils.md)
- [converter/composers/record_materialisation/record_picture_sizer.py](record_picture_sizer.md)
- [converter/composers/record_materialisation/record_sites.py](record_sites.md)
- [patterns/record_materialisation_patterns.py](../../../patterns/record_materialisation_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/__init__.py](__init__.md)
- [converter/composers/record_materialisation_composer.py](../record_materialisation_composer.md)

## Symbol contracts and control points

### `RecordMoveScanner` - L43-L135

```python
class RecordMoveScanner()
```

Finds whole-record MOVEs and the fields they write into.

### `RecordMoveScanner.__init__` - L46-L52

```python
__init__(self, line_utils: RecordLineUtils | None=None, sizer: RecordPictureSizer | None=None) -> None
```

Observed calls (lexical order): `RecordLineUtils`, `RecordPictureSizer`.

### `RecordMoveScanner.find_move` - L55-L92

```python
find_move(self, lines: list[str], handled: set[tuple[str, str]]) -> MoveSite | None
```

Next whole-record MOVE not yet visited. None when exhausted.

Observed calls (lexical order): `enumerate`, `self.lines.is_skippable`, `self.lines.logical`, `PROCEDURE_DIVISION_PATTERN.match`, `WHOLE_RECORD_MOVE_PATTERN.match`, `MoveSite`, `match.group`, `match.group('record').upper`, `match.group('target').upper`.

Control points:

- L63: `for (index, line) in enumerate(lines)`
- L64: `if self.lines.is_skippable(line)`
- L68: `if not body`
- L71: `if PROCEDURE_DIVISION_PATTERN.match(body)`
- L75: `if not in_procedure`
- L79: `if not match`
- L87: `if site.key in handled`

### `RecordMoveScanner.find_target` - L95-L122

```python
find_target(self, lines: list[str], target: str) -> TargetSite
```

The DATA DIVISION entry for `target`, or an empty TargetSite.

Observed calls (lexical order): `self._target_pattern`, `enumerate`, `self.lines.is_skippable`, `self.lines.logical`, `PROCEDURE_DIVISION_PATTERN.match`, `pattern.match`, `TargetSite`, `self.sizer.declared_bytes`, `self.lines.level_of`.

Control points:

- L99: `for (index, line) in enumerate(lines)`
- L100: `if self.lines.is_skippable(line)`
- L104: `if not body`
- L109: `if PROCEDURE_DIVISION_PATTERN.match(body)`
- L113: `if not match`

### `RecordMoveScanner._target_pattern` - L126-L130

```python
_target_pattern(target: str)
```

Observed calls (lexical order): `re.compile`, `TARGET_FIELD_PATTERN_TEMPLATE.format`, `re.escape`.

### `RecordMoveScanner.picture_bytes` - L134-L135

```python
picture_bytes(cls, picture: str) -> int
```

Observed calls (lexical order): `RecordPictureSizer.size_of`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
