# `converter/postprocess/main_flow/main_flow_paragraph_resolver.py`

Source: [converter/postprocess/main_flow/main_flow_paragraph_resolver.py](../../../../../converter/postprocess/main_flow/main_flow_paragraph_resolver.py) | 114 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `78e19d48c570c90985e5cc2362769542be946667d29557ffb25a6486b40dcc6f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.update_main_flow_patterns import DIVISION_LINE_PATTERN, EXEC_SQL_LINE_PATTERN, MOVE_LINE_PATTERN, PARAGRAPH_HEADER_LINE_PATTERN, PERFORM_LINE_PATTERN, PERFORM_READ_FLAT_FILE_LINE_PATTERN, PERFORM_UNTIL_LINE_PATTERN, PROCEDURE_DIVISION_LINE_PATTERN, SECTION_LINE_PATTERN
from rules.update_restart_rules import MAIN_FLOW_READ_FLAT_FILE_PARAGRAPH, MAIN_FLOW_RESTART_PARAGRAPH_PREFIXES
```

## Local dependency notes

- [patterns/update_main_flow_patterns.py](../../../patterns/update_main_flow_patterns.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_main_flow_rewriter.py](../update_main_flow_rewriter.md)

## Symbol contracts and control points

### `MainFlowParagraphResolver` - L20-L114

```python
class MainFlowParagraphResolver()
```

Resolves and classifies the business processing paragraph.

### `MainFlowParagraphResolver._resolve_process_paragraph_from_main_flow` - L23-L39

```python
_resolve_process_paragraph_from_main_flow(self, *, lines, start_index, end_index)
```

Observed calls (lexical order): `range`, `self._logical`, `self._logical(lines[index]).upper`, `self._logical(lines[index]).upper().rstrip`, `PERFORM_UNTIL_LINE_PATTERN.search`, `match.group`, `str`, `str(match.group('paragraph') or '').strip`, `str(match.group('paragraph') or '').strip().upper`, `self._is_restart_or_utility_paragraph`.

Control points:

- L26: `for index in range(start_index, end_index)`
- L29: `if not match`
- L33: `if not paragraph or paragraph == MAIN_FLOW_READ_FLAT_FILE_PARAGRAPH`
- L35: `if self._is_restart_or_utility_paragraph(paragraph)`

### `MainFlowParagraphResolver._resolve_first_business_paragraph` - L41-L64

```python
_resolve_first_business_paragraph(self, *, lines)
```

Observed calls (lexical order): `enumerate`, `self._logical`, `self._logical(line).strip`, `logical.upper`, `logical.upper().rstrip`, `PROCEDURE_DIVISION_LINE_PATTERN.match`, `DIVISION_LINE_PATTERN.match`, `self._is_paragraph_header`, `self._is_restart_or_utility_paragraph`, `self._paragraph_has_business_sql_or_moves`.

Control points:

- L44: `for (index, line) in enumerate(lines)`
- L48: `if PROCEDURE_DIVISION_LINE_PATTERN.match(logical)`
- L51: `if not inside_procedure`
- L53: `if DIVISION_LINE_PATTERN.match(logical)`
- L55: `if not self._is_paragraph_header(logical)`
- L59: `if self._is_restart_or_utility_paragraph(paragraph_name)`
- L61: `if self._paragraph_has_business_sql_or_moves(lines=lines, start_index=index)`

### `MainFlowParagraphResolver._paragraph_has_business_sql_or_moves` - L66-L82

```python
_paragraph_has_business_sql_or_moves(self, *, lines, start_index)
```

Observed calls (lexical order): `len`, `range`, `self._logical`, `self._logical(lines[index]).strip`, `logical.upper`, `self._is_paragraph_header`, `DIVISION_LINE_PATTERN.match`, `EXEC_SQL_LINE_PATTERN.search`, `MOVE_LINE_PATTERN.match`, `PERFORM_LINE_PATTERN.match`.

Control points:

- L67: `for index in range(start_index + 1, len(lines))`
- L71: `if index > start_index + 1 and self._is_paragraph_header(logical)`
- L73: `if DIVISION_LINE_PATTERN.match(logical)`
- L75: `if EXEC_SQL_LINE_PATTERN.search(upper)`
- L77: `if MOVE_LINE_PATTERN.match(upper)`
- L79: `if PERFORM_LINE_PATTERN.match(upper)`

### `MainFlowParagraphResolver._paragraph_contains_perform_read_flat_file` - L84-L89

```python
_paragraph_contains_perform_read_flat_file(self, paragraph_lines)
```

Observed calls (lexical order): `self._logical`, `self._logical(line).upper`, `self._logical(line).upper().rstrip`, `PERFORM_READ_FLAT_FILE_LINE_PATTERN.match`.

Control points:

- L85: `for line in paragraph_lines`
- L87: `if PERFORM_READ_FLAT_FILE_LINE_PATTERN.match(logical)`

### `MainFlowParagraphResolver._is_paragraph_header` - L91-L103

```python
_is_paragraph_header(self, logical)
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `PARAGRAPH_HEADER_LINE_PATTERN.match`, `text.upper`, `text.upper().rstrip`, `SECTION_LINE_PATTERN.match`, `DIVISION_LINE_PATTERN.match`, `self._is_restart_or_utility_paragraph`.

Control points:

- L93: `if not PARAGRAPH_HEADER_LINE_PATTERN.match(text)`
- L97: `if SECTION_LINE_PATTERN.match(text)`
- L99: `if DIVISION_LINE_PATTERN.match(text)`
- L101: `if self._is_restart_or_utility_paragraph(upper)`

### `MainFlowParagraphResolver._is_restart_or_utility_paragraph` - L105-L114

```python
_is_restart_or_utility_paragraph(self, paragraph_name)
```

Observed calls (lexical order): `str`, `str(paragraph_name or '').strip`, `str(paragraph_name or '').strip().upper`, `str(paragraph_name or '').strip().upper().rstrip`, `any`, `name.startswith`.

Control points:

- L107: `if not name`
- L109: `if name == MAIN_FLOW_READ_FLAT_FILE_PARAGRAPH`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
