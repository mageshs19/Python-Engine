# `converter/composers/unmapped_record_block_composer.py`

Source: [converter/composers/unmapped_record_block_composer.py](../../../../converter/composers/unmapped_record_block_composer.py) | 296 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `fc02283b86fc3cc5cfc0b0f1a768242413dd592122d2dbb78c33c67584ccdc16`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Record-level Option B composer (IDMS-source-seeded, column-confirmed).

## Module-level bindings

`BODY_WIDTH` (L38), `LEFT_WIDTH` (L39), `RIGHT_WIDTH` (L40)

## Import declarations

```python
from __future__ import annotations
import re
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
from patterns.idms_patterns import ERASE_PATTERN, MODIFY_PATTERN, OBTAIN_CALC_PATTERN, OBTAIN_CALC_REVERSED_PATTERN, STORE_PATTERN
```

## Local dependency notes

- [converter/resolvers/column_name_resolver.py](../resolvers/column_name_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/idms_patterns.py](../../patterns/idms_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_layout_steps.py](../pipeline/conversion/conversion_layout_steps.md)

## Symbol contracts and control points

### `UnmappedRecordBlockComposer` - L43-L296

```python
class UnmappedRecordBlockComposer()
```

Declared class/data-model fields:

```python
OF_RECORD_PATTERN = re.compile('\\b(?:OF|IN)\\s+(?P<record>[A-Z][A-Z0-9-]*)\\b', flags=re.IGNORECASE)
STATEMENT_END = re.compile('\\.\\s*$')
LEFT_SEQ = re.compile('^(?P<left>\\d{6})')
RIGHT_SEQ = re.compile('(?P<seq>\\d{8})\\s*$')
FF_FIELD_PATTERN = re.compile('\\bTO\\s+[A-Z0-9-]*-FF(?:-[A-Z0-9-]+)?\\b', flags=re.IGNORECASE)
```

### `UnmappedRecordBlockComposer.__init__` - L60-L69

```python
__init__(self, table_name_resolver: TableNameResolver, column_name_resolver: ColumnNameResolver, original_idms_text: str='') -> None
```

### `UnmappedRecordBlockComposer.compose` - L71-L153

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self._discover_unmapped_records`, `text.replace`, `text.replace('\r\n', '\n').split`, `'|'.join`, `re.escape`, `sorted`, `re.compile`, `set`, `len`, `self._logical`, `logical.startswith`, `output.append`, `self.STATEMENT_END.search`, `list`, `min`, `range`.
Another 15 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L72: `if not text`
- L76: `if not unmapped`
- L93: `while i < n`
- L96: `if not logical or logical.startswith('*')`
- L103: `while span_end < n`
- L105: `if self.STATEMENT_END.search(span_logical)`
- L119: `if (references_record or references_ff_field) and (not touches_dcl)`
- L121: `if not record and references_ff_field`
- Another 4 conditions/loops exist in this source span.

### `UnmappedRecordBlockComposer._discover_unmapped_records` - L157-L195

```python
_discover_unmapped_records(self) -> set[str]
```

Observed calls (lexical order): `set`, `text.replace`, `text.replace('\r\n', '\n').split`, `self._logical`, `logical.upper`, `upper.startswith`, `pattern.search`, `match.groupdict`, `match.group`, `NameNormalizer.normalize`, `self.column_name_resolver.columns_for_record`, `found.add`, `normalized.upper`.

Control points:

- L160: `if not text`
- L171: `for raw in text.replace('\r\n', '\n').split('\n')`
- L174: `if not upper or upper.startswith('*')`
- L176: `for pattern in patterns`
- L178: `if not match`
- L180: `if 'record' not in match.groupdict()`
- L183: `if not token`
- L186: `if not normalized`
- Another 1 conditions/loops exist in this source span.

### `UnmappedRecordBlockComposer._record_of` - L199-L211

```python
_record_of(self, span_logicals: list[str], unmapped: set[str]) -> str
```

Observed calls (lexical order): `self.OF_RECORD_PATTERN.finditer`, `NameNormalizer.normalize`, `NameNormalizer.normalize(match.group('record')).upper`, `match.group`.

Control points:

- L204: `for logical in span_logicals`
- L205: `for match in self.OF_RECORD_PATTERN.finditer(logical)`
- L209: `if token in unmapped`

### `UnmappedRecordBlockComposer._sequences` - L213-L220

```python
_sequences(self, line: str) -> tuple[str, str]
```

Return (left6, right8) sequence numbers from a line, padded.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.LEFT_SEQ.match`, `left_match.group`, `self.RIGHT_SEQ.search`, `right_match.group`.

### `UnmappedRecordBlockComposer._original_body` - L222-L231

```python
_original_body(self, line: str) -> str
```

Return columns 8-72 body of the original fixed-format line.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `re.sub`, `len`, `text[7:72].rstrip`, `text[:6].isdigit`, `text[6:].rstrip`, `text.rstrip`.

Control points:

- L226: `if len(text) >= 8`
- L229: `if len(text) >= 6 and text[:6].isdigit()`

### `UnmappedRecordBlockComposer._build_comment_lines` - L233-L275

```python
_build_comment_lines(self, body: str, left: str, right: str) -> list[str]
```

Build one or more 80-column comment lines for a body, wrapping at the 65-char body window (cols 8-72). Continuation lines repeat the '*' indicator and keep the same left/right sequence numbers.

Observed calls (lexical order): `body.rstrip`, `len`, `chunks.append`, `clean.lstrip`, `min`, `(left or '000000')[:LEFT_WIDTH].zfill`, `(right or '00000000')[:RIGHT_WIDTH].zfill`, `chunk[:BODY_WIDTH].ljust`, `out.append`.

Control points:

- L245: `if not clean`
- L249: `if len(clean) <= BODY_WIDTH`
- L258: `while remaining`
- L259: `if first`
- L272: `for chunk in chunks`

### `UnmappedRecordBlockComposer._comment_line` - L277-L280

```python
_comment_line(self, line: str) -> list[str]
```

Observed calls (lexical order): `self._sequences`, `self._original_body`, `self._build_comment_lines`.

### `UnmappedRecordBlockComposer._comment_marker` - L282-L289

```python
_comment_marker(self, cobol_record: str, left: str, right: str) -> list[str]
```

Observed calls (lexical order): `self._build_comment_lines`.

### `UnmappedRecordBlockComposer._logical` - L292-L296

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `str`, `re.sub`, `text.strip`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
