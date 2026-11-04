# `review/checks/chk_24_picture_and_length.py`

Source: [review/checks/chk_24_picture_and_length.py](../../../../review/checks/chk_24_picture_and_length.py) | 399 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `27a546861af59bea7a0586a0e7bd76c64614e6baec3a1d014dd256098ec884e7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-24 Picture clause and length validation.

## Module-level bindings

`DIGITS` (L11), `DB2_SIZED` (L12), `PIC_KEYWORDS` (L16), `IS_KEYWORD` (L17), `LENGTH_SYMBOLS` (L18), `IGNORED_SYMBOLS` (L19), `FIXED_TYPE_LENGTHS` (L22), `CHARACTER_TYPES` (L27)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import metadata as meta
from review.engine.check_base import MAJOR, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)
- [tests/test_review_business_semantics.py](../../tests/test_review_business_semantics.md)

## Symbol contracts and control points

### `_strip_picture_prefix` - L30-L45

```python
_strip_picture_prefix(text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').strip`, `str(text or '').strip().upper`, `value.startswith`, `len`, `value[len(keyword):].strip`, `value[len(IS_KEYWORD):].strip`, `re.split`, `re.split('\\b(?:USAGE|COMP(?:UTATIONAL)?(?:-[0-9]+)?|PACKED-DECIMAL|BINARY|DISPLAY|VALUE|SIGN|SYNCHRONIZED|...`.

Control points:

- L32: `for keyword in PIC_KEYWORDS`
- L33: `if value.startswith(keyword)`
- L36: `if value.startswith(IS_KEYWORD)`

### `picture_length` - L48-L89

```python
picture_length(picture: str) -> int
```

Character length implied by a COBOL picture clause.

Observed calls (lexical order): `_strip_picture_prefix`, `_strip_picture_prefix(picture).replace`, `_strip_picture_prefix(picture).replace(' ', '').rstrip`, `len`, `text.find`, `digits.isdigit`, `int`.

Control points:

- L58: `if not text`
- L65: `while index < size`
- L68: `if symbol in IGNORED_SYMBOLS`
- L72: `if symbol not in LENGTH_SYMBOLS`
- L79: `if index < size and text[index] == '('`
- L82: `if digits.isdigit()`

### `picture_category` - L92-L101

```python
picture_category(picture: str) -> str
```

ALPHANUMERIC, NUMERIC or empty when undecidable.

Observed calls (lexical order): `_strip_picture_prefix`.

Control points:

- L95: `if not text`
- L97: `if 'X' in text or 'A' in text`
- L99: `if '9' in text`

### `db2_type_length` - L104-L122

```python
db2_type_length(db2_type: str) -> int
```

Host length implied by a DB2 type, 0 when not decidable.

Observed calls (lexical order): `str`, `str(db2_type or '').strip`, `str(db2_type or '').strip().upper`, `sorted`, `text.startswith`, `DB2_SIZED.match`, `match.group`, `match.group('type').startswith`, `int`.

Control points:

- L112: `if not text`
- L115: `for name in sorted(FIXED_TYPE_LENGTHS, key=len, reverse=True)`
- L116: `if text.startswith(name)`
- L120: `if match and match.group('type').startswith(CHARACTER_TYPES)`

### `is_varchar` - L125-L127

```python
is_varchar(db2_type: str) -> bool
```

A group host whose pictures live on its 49-level children.

Observed calls (lexical order): `str`, `str(db2_type or '').strip`, `str(db2_type or '').strip().upper`, `str(db2_type or '').strip().upper().startswith`.

### `has_comparable_length` - L130-L134

```python
has_comparable_length(db2_type: str) -> bool
```

True when stored bytes and picture positions mean the same thing.

Observed calls (lexical order): `str`, `str(db2_type or '').strip`, `str(db2_type or '').strip().upper`, `str(db2_type or '').strip().upper().startswith`.

### `PictureAndLengthCheck` - L137-L399

```python
class PictureAndLengthCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-24'
TITLE = 'Picture clause and length validation'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 240
```

### `PictureAndLengthCheck.relevant` - L144-L145

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `bool`.

### `PictureAndLengthCheck.not_relevant_reason` - L147-L148

```python
not_relevant_reason(self) -> str
```

### `PictureAndLengthCheck.review` - L150-L270

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `list`, `record.expect_all`, `sorted`, `meta.field`, `is_varchar`, `picture_length`, `record.skip`, `self._length_mismatches`, `self._source_picture_mismatches`, `self._category_mismatches`, `view.has_code_token`, `any`, `self._type_mismatches`.

Control points:

- L192: `if not std.ENFORCE_PICTURE_LENGTH_MATCH`
- L198: `if not ctx.sheet_mapping_rows`
- L212: `if not ctx.sheet_mapping_rows`
- L224: `if not ctx.sheet_mapping_rows`
- L242: `if not used`
- L261: `if not any((meta.field(c, 'db2_type') for c in columns))`

### `PictureAndLengthCheck._target` - L274-L281

```python
_target(row) -> tuple[str, str]
```

Observed calls (lexical order): `meta.field`.

### `PictureAndLengthCheck._db2_type_for` - L284-L293

```python
_db2_type_for(ctx, table: str, column: str) -> str
```

Observed calls (lexical order): `meta.norm_name`, `meta.field`.

Control points:

- L287: `for item in ctx.dclgen_columns or []`
- L288: `if meta.field(item, 'table_name') != wanted_table`
- L290: `if meta.field(item, 'column_name') != wanted_column`

### `PictureAndLengthCheck._length_mismatches` - L296-L314

```python
_length_mismatches(cls, ctx) -> list[str]
```

Compared only where bytes and positions mean the same thing.

Observed calls (lexical order): `cls._target`, `meta.field`, `DIGITS.match`, `cls._db2_type_for`, `has_comparable_length`, `meta.picture_for`, `picture_length`, `abs`, `int`, `out.append`, `set`, `sorted`.

Control points:

- L299: `for row in ctx.sheet_mapping_rows or []`
- L302: `if not table or not column or (not DIGITS.match(declared))`
- L304: `if not has_comparable_length(cls._db2_type_for(ctx, table, column))`
- L307: `if not actual`
- L309: `if abs(actual - int(declared)) > std.PICTURE_LENGTH_TOLERANCE`

### `PictureAndLengthCheck._source_picture_mismatches` - L317-L343

```python
_source_picture_mismatches(cls, ctx) -> list[str]
```

Observed calls (lexical order): `cls._target`, `cls._db2_type_for`, `has_comparable_length`, `meta.field`, `picture_length`, `meta.picture_for`, `abs`, `out.append`, `set`, `sorted`.

Control points:

- L319: `for row in ctx.sheet_mapping_rows or []`
- L321: `if not table or not column`
- L323: `if not has_comparable_length(cls._db2_type_for(ctx, table, column))`
- L328: `if not source_pic`
- L334: `if not source_length or not target_length`
- L336: `if abs(source_length - target_length) > std.PICTURE_LENGTH_TOLERANCE`

### `PictureAndLengthCheck._category_mismatches` - L346-L374

```python
_category_mismatches(cls, ctx) -> list[str]
```

Observed calls (lexical order): `cls._target`, `meta.field`, `picture_category`, `meta.picture_for`, `cls._db2_type_for`, `cls._db2_type_for(ctx, table, column).upper`, `db2_type.startswith`, `out.append`, `set`, `sorted`.

Control points:

- L348: `for row in ctx.sheet_mapping_rows or []`
- L350: `if not table or not column`
- L357: `if not source or not target`
- L366: `if source == 'NUMERIC' and target == 'ALPHANUMERIC' and db2_type.startswith(('DATE', 'TIME', 'TIMESTAMP'))`
- L372: `if source != target`

### `PictureAndLengthCheck._type_mismatches` - L377-L399

```python
_type_mismatches(ctx) -> list[str]
```

Observed calls (lexical order): `meta.field`, `is_varchar`, `db2_type_length`, `picture_length`, `abs`, `out.append`, `set`, `sorted`.

Control points:

- L379: `for column in ctx.dclgen_columns or []`
- L382: `if not picture or not db2_type`
- L384: `if is_varchar(db2_type)`
- L387: `if not expected`
- L390: `if not actual`
- L392: `if abs(actual - expected) > std.PICTURE_LENGTH_TOLERANCE`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
