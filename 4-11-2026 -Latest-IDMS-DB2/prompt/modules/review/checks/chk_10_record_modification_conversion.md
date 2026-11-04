# `review/checks/chk_10_record_modification_conversion.py`

Source: [review/checks/chk_10_record_modification_conversion.py](../../../../review/checks/chk_10_record_modification_conversion.py) | 156 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `4803dd94469dd4225516a55a7feab9180b87d1e19608a47940d49ad44861a6a2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-10 Record modification conversion.

## Import declarations

```python
from __future__ import annotations
from review.engine import sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `RecordModificationConversionCheck` - L10-L156

```python
class RecordModificationConversionCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-10'
TITLE = 'Record modification conversion'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 100
```

### `RecordModificationConversionCheck.relevant` - L17-L18

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `view.has_code_token`.

### `RecordModificationConversionCheck.not_relevant_reason` - L20-L21

```python
not_relevant_reason(self) -> str
```

### `RecordModificationConversionCheck.review` - L23-L146

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `sql.sql_blocks`, `sql.targets_restart`, `record.expect_none`, `any`, `record.skip`, `record.ok`, `all`, `b.has`, `self._location_set_before`.

Control points:

- L48: `if not writes`
- L60: `if not inserts`
- L75: `if not updates`
- L90: `if not deletes`
- L105: `if not std.ENFORCE_QUERYNO`
- L111: `if not writes`
- L126: `if not std.ENFORCE_SQL_LOCATION_BEFORE_SQL`
- L132: `if not writes`

### `RecordModificationConversionCheck._location_set_before` - L150-L156

```python
_location_set_before(view, block) -> bool
```

Observed calls (lexical order): `sql.lines_before`, `any`, `line.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
