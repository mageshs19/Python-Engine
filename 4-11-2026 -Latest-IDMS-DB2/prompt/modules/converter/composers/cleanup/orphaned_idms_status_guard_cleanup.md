# `converter/composers/cleanup/orphaned_idms_status_guard_cleanup.py`

Source: [converter/composers/cleanup/orphaned_idms_status_guard_cleanup.py](../../../../../converter/composers/cleanup/orphaned_idms_status_guard_cleanup.py) | 75 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `648724b37f5c677bbe5ce95ab7cae5297cbd3e4d3f0b98a9b9843ea55b836348`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Remove status guards whose IDMS BIND/READY operation no longer exists.

## Module-level bindings

`_GUARD` (L15), `_END_IF` (L16), `_CALL_USERABEN` (L17), `_DISPLAY_SETUP` (L18)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [tests/test_orphaned_idms_status_guard_cleanup.py](../../../tests/test_orphaned_idms_status_guard_cleanup.md)

## Symbol contracts and control points

### `OrphanedIdmsStatusGuardCleanup` - L21-L75

```python
class OrphanedIdmsStatusGuardCleanup()
```

### `OrphanedIdmsStatusGuardCleanup.__init__` - L22-L24

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `OrphanedIdmsStatusGuardCleanup.apply` - L26-L64

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `len`, `self.line_utils.logical`, `_GUARD.fullmatch`, `out.append`, `_END_IF.fullmatch`, `'\n'.join`, `re.search`, `_CALL_USERABEN.search`, `_DISPLAY_SETUP.search`, `self._is_obsolete_warning`, `self._blank_comment`, `ref[:6].isdigit`, `note[:65].ljust`, `self.messages.add`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L31: `while i < len(lines)`
- L33: `if not _GUARD.fullmatch(logical)`
- L38: `while end < len(lines) and (not _END_IF.fullmatch(self.line_utils.logical(lines[end])))`
- L40: `if end >= len(lines)`
- L48: `if safe_shape and _CALL_USERABEN.search(block) and _DISPLAY_SETUP.search(block)`
- L49: `while out and self._is_obsolete_warning(out[-1])`
- L53: `if len(ref) >= 80 and ref[:6].isdigit()`
- L62: `if removed`

### `OrphanedIdmsStatusGuardCleanup._is_obsolete_warning` - L66-L68

```python
_is_obsolete_warning(self, line: str) -> bool
```

Observed calls (lexical order): `self.line_utils.logical`, `self.line_utils.logical(line).upper`.

### `OrphanedIdmsStatusGuardCleanup._blank_comment` - L71-L75

```python
_blank_comment(line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `value[:6].isdigit`.

Control points:

- L73: `if len(value) >= 80 and value[:6].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
