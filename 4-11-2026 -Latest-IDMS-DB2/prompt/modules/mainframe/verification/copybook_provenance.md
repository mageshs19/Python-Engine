# `mainframe/verification/copybook_provenance.py`

Source: [mainframe/verification/copybook_provenance.py](../../../../mainframe/verification/copybook_provenance.py) | 152 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `d505086dbf64324a2c5a9b57dacdecf9024072f20d4ff2d216ded52a6410b437`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Derive and verify COPY members from explicit source/target relationships.

## Module-level bindings

`_COPY` (L20), `_ROOT` (L21)

## Import declarations

```python
from __future__ import annotations
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from converter.services.name_derivation_resolver import NameDerivationResolver
from .cobol_storage_layout import group_byte_length
from .record_write_contract import _code
```

## Local dependency notes

- [converter/services/name_derivation_resolver.py](../../converter/services/name_derivation_resolver.md)
- [mainframe/verification/cobol_storage_layout.py](cobol_storage_layout.md)
- [mainframe/verification/record_write_contract.py](record_write_contract.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_semantic_release_gate.py](../zowe_semantic_release_gate.md)
- [review/runner/workspace_inputs.py](../../review/runner/workspace_inputs.md)
- [tests/test_copybook_provenance_and_occurs.py](../../tests/test_copybook_provenance_and_occurs.md)

## Symbol contracts and control points

### `CopybookResolution` - L25-L29

```python
class CopybookResolution()
```

Declared class/data-model fields:

```python
expanded_text: str
staged_members: tuple[Path, ...]
notes: tuple[str, ...]
errors: tuple[str, ...]
```

### `_copies` - L32-L34

```python
_copies(text: str) -> set[str]
```

Observed calls (lexical order): `match.group`, `match.group(1).upper`, `text.splitlines`, `_COPY.match`, `_code`.

### `_member_path` - L37-L42

```python
_member_path(folder: Path, name: str) -> Path | None
```

Observed calls (lexical order): `candidate.is_file`.

Control points:

- L38: `for suffix in ('.cpy', '.cbl', '.txt')`
- L40: `if candidate.is_file()`

### `_sub_outside_literals` - L45-L69

```python
_sub_outside_literals(code: str, pattern: re.Pattern[str], replacement: str) -> str
```

Never change VALUE literals while renaming COPY data names.

Observed calls (lexical order): `len`, `parts.append`, `pattern.sub`, `''.join`.

Control points:

- L50: `while pos < len(code)`
- L51: `if code[pos] not in ("'", '"')`
- L57: `while end < len(code)`
- L58: `if code[end] == quote`
- L59: `if end + 1 < len(code) and code[end + 1] == quote`

### `_rename_root` - L72-L85

```python
_rename_root(source_text: str, before: str, after: str) -> str
```

Observed calls (lexical order): `re.compile`, `re.escape`, `source_text.splitlines`, `_code`, `body.upper`, `body.upper().startswith`, `result.append`, `len`, `line[:6].isdigit`, `_sub_outside_literals`, `''.join`.

Control points:

- L76: `for line in source_text.splitlines(keepends=True)`
- L78: `if not body or body.upper().startswith('COPY ')`
- L81: `if len(line) >= 7 and line[:6].isdigit()`

### `resolve_copybooks` - L88-L152

```python
resolve_copybooks(source: str, target: str, authoritative: Path, staged: Path) -> CopybookResolution
```

Observed calls (lexical order): `_copies`, `NameDerivationResolver`, `sorted`, `_member_path`, `path.read_text`, `notes.append`, `resolver.derive`, `resolver.is_derivable`, `len`, `errors.append`, `original_path.read_text`, `_code`, `any`, `original.splitlines`, `re.search`, `_rename_root`.
Another 20 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L97: `for target_name in sorted(target_copies)`
- L99: `if path is not None`
- L105: `if len(candidates) != 1`
- L110: `if original_path is None`
- L114: `if any((re.search('\\bCOPY\\b', _code(line), re.I) for line in original.splitlines()))`
- L120: `if len(original_roots) != 1 or not (original_roots[0] == before or original_roots[0].startswith(before + '-'))`
- L133: `if old_size != new_size`
- L145: `for line in expanded.splitlines(keepends=True)`
- Another 1 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
