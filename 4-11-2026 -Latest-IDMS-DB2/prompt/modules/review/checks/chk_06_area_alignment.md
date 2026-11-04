# `review/checks/chk_06_area_alignment.py`

Source: [review/checks/chk_06_area_alignment.py](../../../../review/checks/chk_06_area_alignment.py) | 281 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `52fdfc82a34e481654790c637457742b05c8ac31ca2866a00d1b235833afa7ad`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-06 Area A and Area B alignment.

## Module-level bindings

`DIVISION` (L10), `SECTION` (L11), `PARAGRAPH` (L12), `LEVEL` (L13), `PROCEDURE_DIVISION` (L14), `SQL_START` (L16), `SQL_END` (L17), `STATUS_START` (L18), `STATUS_END` (L19)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine.check_base import MINOR, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `AreaAlignmentCheck` - L22-L281

```python
class AreaAlignmentCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-06'
TITLE = 'Area A and Area B alignment'
SEVERITY = MINOR
APPLIES_TO = BOTH
ORDER = 60
```

### `AreaAlignmentCheck.relevant` - L29-L30

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `any`.

### `AreaAlignmentCheck.not_relevant_reason` - L32-L33

```python
not_relevant_reason(self) -> str
```

### `AreaAlignmentCheck.review` - L35-L198

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `self._generated_sql_lines`, `DIVISION.match`, `DIVISION.match(line.logical).group`, `record.skip`, `record.expect_none`, `SECTION.match`, `self._paragraph_headers`, `LEVEL.match`, `LEVEL.match(line.logical).group`, `' and '.join`, `self._procedure_statements`.

Control points:

- L55: `if not divisions`
- L72: `if not sections`
- L85: `if not paragraphs`
- L103: `if not top_levels`
- L125: `if not sub_levels`
- L144: `if not std.ENFORCE_AREA_B_STATEMENT_INDENT`
- L151: `if not statements`
- L163: `if not std.ENFORCE_AREA_B_SQL_INDENT`
- Another 2 conditions/loops exist in this source span.

### `AreaAlignmentCheck._paragraph_headers` - L202-L221

```python
_paragraph_headers(lines, generated: set[int]) -> list
```

Real paragraph headers only.

Observed calls (lexical order): `SECTION.match`, `PARAGRAPH.match`, `match.group`, `out.append`.

Control points:

- L210: `for line in lines`
- L211: `if line.number in generated`
- L213: `if SECTION.match(line.logical)`
- L216: `if not match`
- L218: `if match.group('name') in std.NON_PARAGRAPH_WORDS`

### `AreaAlignmentCheck._procedure_statements` - L224-L242

```python
_procedure_statements(lines, generated: set[int]) -> list
```

Hand-written executable lines after PROCEDURE DIVISION.

Observed calls (lexical order): `PROCEDURE_DIVISION.match`, `DIVISION.match`, `SECTION.match`, `PARAGRAPH.match`, `match.group`, `out.append`.

Control points:

- L228: `for line in lines`
- L229: `if PROCEDURE_DIVISION.match(line.logical)`
- L232: `if not started`
- L234: `if line.number in generated`
- L236: `if DIVISION.match(line.logical) or SECTION.match(line.logical)`
- L239: `if match and match.group('name') not in std.NON_PARAGRAPH_WORDS`

### `AreaAlignmentCheck._generated_sql_lines` - L245-L281

```python
_generated_sql_lines(lines) -> list
```

Every line of a generated DB2 block, terminators included.

Observed calls (lexical order): `SQL_START.match`, `out.append`, `SQL_END.search`, `STATUS_START.match`, `STATUS_END.search`.

Control points:

- L257: `for line in lines`
- L260: `if not in_exec and (not in_status)`
- L261: `if SQL_START.match(logical)`
- L264: `if SQL_END.search(logical)`
- L267: `if STATUS_START.match(logical)`
- L270: `if STATUS_END.search(logical)`
- L276: `if in_exec and SQL_END.search(logical)`
- L278: `if in_status and STATUS_END.search(logical)`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
