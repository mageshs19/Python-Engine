# `review/checks/chk_08_dclgen_include_integrity.py`

Source: [review/checks/chk_08_dclgen_include_integrity.py](../../../../review/checks/chk_08_dclgen_include_integrity.py) | 334 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `0c885fb8a6d71f808a572ca5c135c1d74e15d9ca5c5a9468ba92c16107bf9541`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-08 DCLGEN include and copybook integrity.

## Module-level bindings

`INCLUDE` (L11), `COPY` (L14), `WS_SECTION` (L15), `PROCEDURE_DIVISION` (L16), `WS_RUN` (L17)

## Import declarations

```python
from __future__ import annotations
import re
from collections import Counter
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `norm` - L20-L22

```python
norm(text: str) -> str
```

Uppercase, trimmed, internal whitespace runs collapsed.

Observed calls (lexical order): `WS_RUN.sub`, `str`, `str(text or '').strip`, `str(text or '').strip().upper`.

### `statements` - L25-L56

```python
statements(lines: list[str]) -> list[str]
```

Logical statements, with EXEC SQL ... END-EXEC. joined into one entry.

Observed calls (lexical order): `norm`, `line.startswith`, `' '.join`, `out.append`, `buffer.append`.

Control points:

- L34: `for raw in lines`
- L37: `if not inside and line.startswith(std.SQL_BLOCK_START)`
- L40: `if std.SQL_BLOCK_END in line`
- L45: `if inside`
- L47: `if std.SQL_BLOCK_END in line`
- L54: `if buffer`

### `is_infrastructure` - L59-L61

```python
is_infrastructure(name: str) -> bool
```

SQLCA, SQLERRWS, SQLERROR and GEN are not DCLGEN table includes.

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`.

### `DclgenIncludeIntegrityCheck` - L64-L334

```python
class DclgenIncludeIntegrityCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-08'
TITLE = 'DCLGEN include and copybook integrity'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 80
```

### `DclgenIncludeIntegrityCheck.relevant` - L71-L72

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `view.has_code_token`.

### `DclgenIncludeIntegrityCheck.not_relevant_reason` - L74-L75

```python
not_relevant_reason(self) -> str
```

### `DclgenIncludeIntegrityCheck.review` - L77-L287

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `statements`, `INCLUDE.match`, `INCLUDE.match(line).group`, `INCLUDE.match(line).group('name').upper`, `is_infrastructure`, `set`, `self._referenced_groups`, `self._table_of`, `COPY.match`, `COPY.match(line).group`, `COPY.match(line).group('name').upper`, `record.skip`, `record.expect_all`, `sorted`, `Counter`, `Counter(included).items`.
Another 14 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L100: `if not dclgen_includes`
- L131: `if not std.ENFORCE_INCLUDE_IN_WORKING_STORAGE`
- L136: `if not dclgen_includes`
- L153: `if ws_at < 0 or pd_at < 0`
- L161: `for (index, line) in enumerate(code)`
- L163: `if not match`
- L165: `if is_infrastructure(match.group('name'))`
- L167: `if not ws_at < index < pd_at`
- Another 8 conditions/loops exist in this source span.

### `DclgenIncludeIntegrityCheck._table_of` - L291-L295

```python
_table_of(group: str) -> str
```

DCLDZBEFFTV -> DZBEFFTV.

Observed calls (lexical order): `str`, `str(group or '').strip`, `str(group or '').strip().upper`, `std.DCLGEN_GROUP_PREFIX.upper`, `len`, `text.startswith`.

### `DclgenIncludeIntegrityCheck._referenced_groups` - L298-L301

```python
_referenced_groups(view) -> set[str]
```

Observed calls (lexical order): `std.DCLGEN_GROUP_PREFIX.upper`, `re.compile`, `pattern.findall`, `set`.

### `DclgenIncludeIntegrityCheck._dclgen_tables` - L304-L309

```python
_dclgen_tables(ctx) -> set[str]
```

Observed calls (lexical order): `getattr`, `str`, `str(getattr(column, 'table_name', '') or '').strip`, `str(getattr(column, 'table_name', '') or '').strip().upper`.

### `DclgenIncludeIntegrityCheck._dclgen_hosts` - L312-L323

```python
_dclgen_hosts(ctx) -> dict[str, str]
```

Observed calls (lexical order): `str`, `str(getattr(column, 'cobol_host_name', '') or '').strip`, `str(getattr(column, 'cobol_host_name', '') or '').strip().upper`, `getattr`, `str(getattr(column, 'table_name', '') or '').strip`, `str(getattr(column, 'table_name', '') or '').strip().upper`.

Control points:

- L314: `for column in ctx.dclgen_columns or []`
- L321: `if host and table`

### `DclgenIncludeIntegrityCheck._copybook_records` - L326-L334

```python
_copybook_records(ctx) -> set[str]
```

01-level record names from the supplied copybook fields.

Observed calls (lexical order): `set`, `getattr`, `str`, `str(getattr(field, 'level', '') or '').strip`, `str(getattr(field, 'name', '') or '').strip`, `str(getattr(field, 'name', '') or '').strip().upper`, `out.add`.

Control points:

- L329: `for field in ctx.copybook_fields or []`
- L332: `if name and level == std.COPYBOOK_RECORD_LEVEL`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
