# `review/checks/chk_25_copybook_and_record_usage.py`

Source: [review/checks/chk_25_copybook_and_record_usage.py](../../../../review/checks/chk_25_copybook_and_record_usage.py) | 315 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `46546838ae4520c7c33e559565096d1fbaebae76f7d1ce337b0395472e809607`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-25 Copybook and record usage validation.

## Module-level bindings

`QUALIFIED` (L11), `COPY` (L14), `DATA_ITEM` (L15), `LITERAL` (L18)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import metadata as meta, sql_blocks as sql
from review.engine.check_base import MAJOR, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_business_parity_review_rules_v128.py](../../tests/test_business_parity_review_rules_v128.md)

## Symbol contracts and control points

### `without_literals` - L21-L28

```python
without_literals(text: str) -> str
```

Blank out quoted literals.

Observed calls (lexical order): `LITERAL.sub`, `str`.

### `CopybookAndRecordUsageCheck` - L31-L314

```python
class CopybookAndRecordUsageCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-25'
TITLE = 'Copybook and record usage validation'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 250
```

### `CopybookAndRecordUsageCheck.relevant` - L38-L39

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`.

### `CopybookAndRecordUsageCheck.not_relevant_reason` - L41-L42

```python
not_relevant_reason(self) -> str
```

### `CopybookAndRecordUsageCheck.review` - L44-L198

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `std.DCLGEN_GROUP_PREFIX.upper`, `meta.mapped_records`, `self._qualifiers`, `self._copies`, `self._copybook_fields`, `self._declared_names`, `record.skip`, `record.expect_all`, `sorted`, `meta.dclgen_tables`, `set`, `self._undocumented`, `record.expect_none`, `any`, `group.startswith`, `view.has_code_token`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L53: `if not std.ENFORCE_NO_IDMS_QUALIFIER`
- L58: `if not records`
- L74: `if not qualifiers`
- L98: `if not records`
- L104: `if not ctx.has_source`
- L131: `if not copybook`
- L136: `if not qualifiers`
- L155: `if not copies`
- Another 2 conditions/loops exist in this source span.

### `CopybookAndRecordUsageCheck._qualifiers` - L202-L208

```python
_qualifiers(view) -> set[tuple[str, str]]
```

Observed calls (lexical order): `set`, `sql.norm`, `without_literals`, `QUALIFIED.finditer`, `match.group`, `out.add`.

Control points:

- L204: `for line in view.code`
- L206: `for match in QUALIFIED.finditer(body)`

### `CopybookAndRecordUsageCheck._copies` - L211-L217

```python
_copies(view) -> set[str]
```

Observed calls (lexical order): `set`, `COPY.match`, `sql.norm`, `match.group`, `out.add`.

Control points:

- L213: `for line in view.code`
- L215: `if match`

### `CopybookAndRecordUsageCheck._copybook_fields` - L220-L225

```python
_copybook_fields(ctx) -> set[str]
```

Observed calls (lexical order): `meta.field`.

### `CopybookAndRecordUsageCheck._declared_names` - L228-L235

```python
_declared_names(view) -> set[str]
```

Every data name the program declares in its own DATA DIVISION.

Observed calls (lexical order): `set`, `DATA_ITEM.match`, `sql.norm`, `match.group`, `out.add`.

Control points:

- L231: `for line in view.code`
- L233: `if match`

### `CopybookAndRecordUsageCheck._table_variants` - L238-L247

```python
_table_variants(table: str) -> set[str]
```

Every equivalent DB2 table spelling, TB and TV included.

Observed calls (lexical order): `str`, `str(table or '').strip`, `str(table or '').strip().upper`, `set`, `text.endswith`, `len`, `out.add`.

Control points:

- L241: `if not text`
- L244: `for (source, target) in std.DB2_TABLE_SUFFIX_EQUIVALENTS`
- L245: `if text.endswith(source)`

### `CopybookAndRecordUsageCheck._undocumented` - L250-L265

```python
_undocumented(cls, ctx, view, records: set[str]) -> list[str]
```

Observed calls (lexical order): `sql.norm`, `' '.join`, `sorted`, `meta.table_for_record`, `any`, `view.has_code_token`, `cls._table_variants`, `out.append`.

Control points:

- L255: `for name in sorted((name for name in records if name in source))`
- L257: `if any((view.has_code_token(item) for item in cls._table_variants(table)))`
- L262: `if name in comments`

### `CopybookAndRecordUsageCheck._zone_name` - L267-L274

```python
_zone_name(value: str) -> str
```

Observed calls (lexical order): `' '.join`, `' '.join(str(value or '').replace('.', ' ').split()).upper`, `str`, `str(value or '').replace`, `str(value or '').replace('.', ' ').split`, `text.split`, `parts[0].isdigit`.

Control points:

- L269: `if not text`
- L272: `if parts and parts[0].isdigit()`

### `CopybookAndRecordUsageCheck._mapped_source_fields` - L277-L289

```python
_mapped_source_fields(cls, ctx) -> dict[str, set[str]]
```

Observed calls (lexical order): `meta.field`, `cls._zone_name`, `owners.setdefault`, `owners.setdefault(name, set()).add`, `set`.

Control points:

- L279: `for row in ctx.sheet_mapping_rows or []`
- L287: `if target and record and name`

### `CopybookAndRecordUsageCheck._procedure_text` - L292-L296

```python
_procedure_text(text: str) -> str
```

Observed calls (lexical order): `sql.norm`, `logical.find`.

### `CopybookAndRecordUsageCheck._unmaterialised_legacy_fields` - L299-L314

```python
_unmaterialised_legacy_fields(cls, ctx, view, known_names: set[str]) -> list[str]
```

Observed calls (lexical order): `cls._procedure_text`, `cls._mapped_source_fields`, `cls._mapped_source_fields(ctx).items`, `sorted`, `len`, `re.compile`, `re.escape`, `token.search`, `iter`, `next`, `out.append`.

Control points:

- L302: `if not source_proc or not generated_proc`
- L306: `for (name, owners) in sorted(cls._mapped_source_fields(ctx).items())`
- L309: `if len(owners) != 1 or name in known_names`
- L312: `if token.search(source_proc) and token.search(generated_proc)`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
