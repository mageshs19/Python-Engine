# `review/checks/chk_04_program_header.py`

Source: [review/checks/chk_04_program_header.py](../../../../review/checks/chk_04_program_header.py) | 115 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `d64a2485180998fe27e16295f96035b49b271ac112655949b421bf47ba8d3e4d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-04 Compiler option and PROGRAM-ID.

## Module-level bindings

`CBL` (L10), `PROG` (L11), `ENDP` (L12), `CSPG` (L21), `SITE` (L28)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)

## Symbol contracts and control points

### `derive` - L31-L34

```python
derive(name: str) -> str
```

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `SITE.match`, `m.group`.

### `ProgramHeaderCheck` - L37-L115

```python
class ProgramHeaderCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-04'
TITLE = 'Compiler option and PROGRAM-ID'
SEVERITY = CRITICAL
ORDER = 40
```

### `ProgramHeaderCheck.review` - L43-L106

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `CBL.match`, `record.expect`, `bool`, `std.COMPILER_OPTION_LINE.upper`, `len`, `view.first_group`, `ctx.target_program_id.upper`, `ProgramHeaderCheck._source_id`, `derive`, `record.skip`, `getattr`, `CSPG.match`, `m.group`, `', '.join`, `m.group('v').strip`, `m.group('v').strip().upper`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L60: `if expected`
- L71: `if not getattr(std, 'ENFORCE_END_PROGRAM', True)`
- L76: `if end_name`
- L94: `if not matches`

### `ProgramHeaderCheck._source_id` - L109-L115

```python
_source_id(ctx) -> str
```

Observed calls (lexical order): `str`, `str(ctx.source_cobol or '').splitlines`, `len`, `PROG.match`, `body.strip`, `body.strip().upper`, `m.group`.

Control points:

- L110: `for raw in str(ctx.source_cobol or '').splitlines()`
- L113: `if m`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
