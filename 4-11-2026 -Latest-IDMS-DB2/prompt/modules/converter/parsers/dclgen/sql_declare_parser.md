# `converter/parsers/dclgen/sql_declare_parser.py`

Source: [converter/parsers/dclgen/sql_declare_parser.py](../../../../../converter/parsers/dclgen/sql_declare_parser.py) | 298 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `6b01f18cd9ed4da865f89897b63e1c12c9e496d2dd84a2c4643351ff29cf846b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Parses EXEC SQL DECLARE TABLE column definitions from DCLGEN text.

## Import declarations

```python
from __future__ import annotations
from catalogs.db2_sql_types import DB2_SQL_SKIP_WORDS, DB2_SQL_TYPE_STARTERS
from patterns.dclgen_patterns import DECLARE_TABLE_ALT_PATTERN, DECLARE_TABLE_PATTERN, DCLGEN_TABLE_COMMENT_PATTERN, VALID_SQL_COLUMN_NAME_PATTERN
```

## Local dependency notes

- [catalogs/db2_sql_types.py](../../../catalogs/db2_sql_types.md)
- [patterns/dclgen_patterns.py](../../../patterns/dclgen_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/dclgen_parser.py](../dclgen_parser.md)

## Symbol contracts and control points

### `SqlDeclareParser` - L17-L298

```python
class SqlDeclareParser()
```

### `SqlDeclareParser.__init__` - L18-L20

```python
__init__(self, name_normalizer, diagnostics: list[str]) -> None
```

### `SqlDeclareParser.find_table_name` - L22-L31

```python
find_table_name(self, text: str) -> str
```

Observed calls (lexical order): `pattern.search`, `match.group`, `self.names.normalize_sql_name`.

Control points:

- L23: `for pattern in [DECLARE_TABLE_PATTERN, DECLARE_TABLE_ALT_PATTERN, DCLGEN_TABLE_COMMENT_PATTERN]`
- L29: `if match`

### `SqlDeclareParser.parse_columns` - L33-L70

```python
parse_columns(self, text: str, table_name: str, source_label: str) -> list[dict[str, object]]
```

Observed calls (lexical order): `self._extract_declare_sections`, `self.diagnostics.append`, `enumerate`, `self.find_table_name`, `self._extract_parenthesized_body`, `self._parse_declare_body`, `len`, `output.extend`.

Control points:

- L41: `if not sections`
- L49: `for (section_index, section) in enumerate(sections, start=1)`
- L53: `if not body`

### `SqlDeclareParser._extract_declare_sections` - L72-L104

```python
_extract_declare_sections(self, text: str) -> list[str]
```

Observed calls (lexical order): `text.splitlines`, `line.upper`, `current.append`, `'\n'.join`, `sections.append`, `upper.strip`, `upper.strip().startswith`.

Control points:

- L78: `for line in lines`
- L81: `if 'DECLARE' in upper and 'TABLE' in upper`
- L86: `if inside`
- L89: `if 'END-EXEC' in upper`
- L95: `if upper.strip() == ')' or upper.strip().startswith(')')`
- L101: `if inside and current`

### `SqlDeclareParser._extract_parenthesized_body` - L106-L130

```python
_extract_parenthesized_body(self, section: str) -> str
```

Observed calls (lexical order): `section.find`, `len`, `range`, `body_chars.append`, `''.join`.

Control points:

- L108: `if start < 0`
- L114: `for index in range(start, len(section))`
- L117: `if char == '('`
- L119: `if depth == 1`
- L122: `if char == ')'`
- L124: `if depth == 0`
- L127: `if depth >= 1`

### `SqlDeclareParser._parse_declare_body` - L132-L181

```python
_parse_declare_body(self, body: str, table_name: str) -> list[dict[str, object]]
```

Observed calls (lexical order): `self._split_sql_items`, `self._normalize_sql_item`, `self._parse_inline_column_definition`, `inline_columns.append`, `self._looks_like_column_name`, `column_names.append`, `self.names.normalize_sql_name`, `self._looks_like_db2_type`, `db2_types.append`, `self._normalize_db2_type`, `enumerate`, `len`, `output.append`, `self._is_nullable_db2_type`.

Control points:

- L143: `for item in logical_items`
- L145: `if not normalized_item`
- L152: `if inline`
- L156: `if self._looks_like_column_name(normalized_item)`
- L162: `if self._looks_like_db2_type(normalized_item)`
- L166: `if inline_columns`
- L170: `for (index, column_name) in enumerate(column_names)`

### `SqlDeclareParser._split_sql_items` - L183-L217

```python
_split_sql_items(self, body: str) -> list[str]
```

Observed calls (lexical order): `body.replace`, `current.append`, `''.join`, `''.join(current).strip`, `items.append`, `expanded.extend`, `self._split_possible_stacked_column_or_type_lines`.

Control points:

- L189: `for char in normalized`
- L190: `if char == '('`
- L194: `if char == ')'`
- L195: `if depth > 0`
- L199: `if char == ',' and depth == 0`
- L201: `if item`
- L208: `if item`
- L212: `for item in items`

### `SqlDeclareParser._split_possible_stacked_column_or_type_lines` - L219-L241

```python
_split_possible_stacked_column_or_type_lines(self, item: str) -> list[str]
```

Observed calls (lexical order): `' '.join`, `str`, `str(item or '').split`, `self._parse_inline_column_definition`, `text.split`, `len`, `self._looks_like_db2_type`, `all`, `self._looks_like_column_name`.

Control points:

- L224: `if not text`
- L228: `if inline`
- L232: `if len(tokens) <= 1`
- L235: `if self._looks_like_db2_type(text)`
- L238: `if all((self._looks_like_column_name(token) for token in tokens))`

### `SqlDeclareParser._parse_inline_column_definition` - L243-L266

```python
_parse_inline_column_definition(self, item: str, table_name: str) -> dict[str, object] | None
```

Observed calls (lexical order): `item.split`, `len`, `self.names.normalize_sql_name`, `self._looks_like_column_name`, `' '.join`, `self._looks_like_db2_type`, `self._normalize_db2_type`, `self._is_nullable_db2_type`.

Control points:

- L249: `if len(tokens) < 2`
- L253: `if not self._looks_like_column_name(first)`
- L257: `if not self._looks_like_db2_type(remaining)`

### `SqlDeclareParser._looks_like_column_name` - L268-L276

```python
_looks_like_column_name(self, value: str) -> bool
```

Observed calls (lexical order): `self.names.normalize_sql_name`, `text.split`, `VALID_SQL_COLUMN_NAME_PATTERN.fullmatch`, `bool`.

Control points:

- L270: `if not text`
- L272: `if text in DB2_SQL_SKIP_WORDS`
- L274: `if text.split(' ')[0] in DB2_SQL_TYPE_STARTERS`

### `SqlDeclareParser._looks_like_db2_type` - L278-L284

```python
_looks_like_db2_type(self, value: str) -> bool
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `text.split`, `first.split`.

Control points:

- L280: `if not text`

### `SqlDeclareParser._normalize_sql_item` - L286-L290

```python
_normalize_sql_item(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `text.strip`, `text.strip(',').strip`, `' '.join`, `text.split`.

### `SqlDeclareParser._normalize_db2_type` - L292-L295

```python
_normalize_db2_type(self, value: str) -> str
```

Observed calls (lexical order): `' '.join`, `str`, `str(value or '').replace`, `str(value or '').replace(', ', ',').split`, `text.rstrip`, `text.upper`.

### `SqlDeclareParser._is_nullable_db2_type` - L297-L298

```python
_is_nullable_db2_type(self, db2_type: str) -> bool
```

Observed calls (lexical order): `str`, `str(db2_type or '').upper`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
