# `converter/composers/fixed_format_body_formatter.py`

Source: [converter/composers/fixed_format_body_formatter.py](../../../../converter/composers/fixed_format_body_formatter.py) | 166 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `320d00111afc30e7c4ec5505153aa8cd80d43ffe210d71c5402ba83cf24acbef`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL body formatter.

## Import declarations

```python
from __future__ import annotations
from patterns.fixed_format_patterns import AREA_A_PREFIX_PATTERN, DATA_LEVEL_PATTERN, DIVISION_PATTERN, EXEC_SQL_END_PATTERN, EXEC_SQL_START_PATTERN, PARAGRAPH_PATTERN, SECTION_PATTERN
from rules.cobol_statement_rules import NON_PARAGRAPH_WORDS, PROCEDURE_VERBS, SQL_LEVEL_1_KEYWORDS, SQL_LEVEL_2_KEYWORDS
from rules.fixed_format_rules import AREA_A_DATA_LEVELS, AREA_B_INDENT, PRESERVE_VERBATIM_INDICATORS, PROCEDURE_DIVISION_NAME, SQL_INDENT
```

## Local dependency notes

- [patterns/fixed_format_patterns.py](../../patterns/fixed_format_patterns.md)
- [rules/cobol_statement_rules.py](../../rules/cobol_statement_rules.md)
- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_composer.py](fixed_format_composer.md)

## Symbol contracts and control points

### `FixedFormatBodyFormatter` - L41-L166

```python
class FixedFormatBodyFormatter()
```

### `FixedFormatBodyFormatter.area_body` - L42-L78

```python
area_body(self, body: str, logical: str, current_division: str, inside_exec_sql: bool, indicator: str, previous_procedure_indent: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `str(logical or '').strip`, `original.startswith`, `self.is_area_a_statement`, `self.sql_area_body`, `self.procedure_area_b_body`, `DATA_LEVEL_PATTERN.match`, `self.data_area_body`.

Control points:

- L54: `if indicator in PRESERVE_VERBATIM_INDICATORS`
- L57: `if not clean_statement`
- L60: `if original.startswith(' ')`
- L63: `if self.is_area_a_statement(clean_statement)`
- L66: `if inside_exec_sql`
- L69: `if current_division == PROCEDURE_DIVISION_NAME`
- L75: `if DATA_LEVEL_PATTERN.match(clean_statement)`

### `FixedFormatBodyFormatter.procedure_area_b_body` - L80-L96

```python
procedure_area_b_body(self, clean_statement: str, previous_procedure_indent: str) -> str
```

Observed calls (lexical order): `clean_statement.upper`, `self.is_area_a_statement`, `upper.startswith`.

Control points:

- L87: `if self.is_area_a_statement(clean_statement)`
- L90: `if upper.startswith(PROCEDURE_VERBS)`
- L93: `if previous_procedure_indent`

### `FixedFormatBodyFormatter.data_area_body` - L98-L107

```python
data_area_body(self, clean_statement: str) -> str
```

Observed calls (lexical order): `clean_statement.split`.

Control points:

- L100: `if not parts`
- L104: `if level in AREA_A_DATA_LEVELS`

### `FixedFormatBodyFormatter.sql_area_body` - L109-L124

```python
sql_area_body(self, clean_statement: str) -> str
```

Observed calls (lexical order): `clean_statement.upper`, `EXEC_SQL_START_PATTERN.match`, `EXEC_SQL_END_PATTERN.match`, `upper.startswith`.

Control points:

- L112: `if EXEC_SQL_START_PATTERN.match(clean_statement)`
- L115: `if EXEC_SQL_END_PATTERN.match(clean_statement)`
- L118: `if upper.startswith(SQL_LEVEL_1_KEYWORDS)`
- L121: `if upper.startswith(SQL_LEVEL_2_KEYWORDS)`

### `FixedFormatBodyFormatter.is_area_a_statement` - L126-L149

```python
is_area_a_statement(self, statement: str) -> bool
```

Observed calls (lexical order): `str`, `str(statement or '').strip`, `DIVISION_PATTERN.match`, `SECTION_PATTERN.match`, `AREA_A_PREFIX_PATTERN.match`, `DATA_LEVEL_PATTERN.match`, `clean_statement.split`, `PARAGRAPH_PATTERN.match`, `clean_statement.rstrip`, `clean_statement.rstrip('.').strip`, `clean_statement.rstrip('.').strip().upper`.

Control points:

- L128: `if not clean_statement`
- L131: `if DIVISION_PATTERN.match(clean_statement)`
- L133: `if SECTION_PATTERN.match(clean_statement)`
- L135: `if AREA_A_PREFIX_PATTERN.match(clean_statement)`
- L138: `if DATA_LEVEL_PATTERN.match(clean_statement)`
- L142: `if not PARAGRAPH_PATTERN.match(clean_statement)`
- L146: `if paragraph_name in NON_PARAGRAPH_WORDS`

### `FixedFormatBodyFormatter.is_exec_sql_start` - L151-L152

```python
is_exec_sql_start(self, statement: str) -> bool
```

Observed calls (lexical order): `EXEC_SQL_START_PATTERN.match`, `bool`, `str`, `str(statement or '').strip`.

### `FixedFormatBodyFormatter.is_exec_sql_end` - L154-L155

```python
is_exec_sql_end(self, statement: str) -> bool
```

Observed calls (lexical order): `EXEC_SQL_END_PATTERN.match`, `bool`, `str`, `str(statement or '').strip`.

### `FixedFormatBodyFormatter.leading_spaces` - L157-L166

```python
leading_spaces(self, text: str, default: str='') -> str
```

Observed calls (lexical order): `str`, `len`, `value.lstrip`.

Control points:

- L159: `if not value`
- L163: `if count <= 0`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
