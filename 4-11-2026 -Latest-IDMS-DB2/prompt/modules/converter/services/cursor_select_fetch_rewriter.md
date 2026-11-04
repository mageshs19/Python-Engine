# `converter/services/cursor_select_fetch_rewriter.py`

Source: [converter/services/cursor_select_fetch_rewriter.py](../../../../converter/services/cursor_select_fetch_rewriter.py) | 182 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `78434cc07949aa261b44711131bad69f05d9f68aacd5ca256e9a23c144122201`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.cursor_select_column_parser import CursorSelectColumnParser
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.final_feedback_fix_patterns import END_EXEC_PATTERN, FROM_PATTERN, HOST_REFERENCE_PATTERN, SELECT_KEYWORD_PATTERN
from rules.cursor_select_minimizer_rules import FETCH_HOST_BODY_PREFIX, SELECT_FIRST_ITEM_BODY_PREFIX, SELECT_NEXT_ITEM_BODY_PREFIX
```

## Local dependency notes

- [converter/services/cursor_select_column_parser.py](cursor_select_column_parser.md)
- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/cursor_select_minimizer_rules.py](../../rules/cursor_select_minimizer_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cursor_select_minimizer_service.py](cursor_select_minimizer_service.md)

## Symbol contracts and control points

### `CursorSelectFetchRewriter` - L22-L182

```python
class CursorSelectFetchRewriter()
```

Removes SELECT and FETCH INTO items by position and normalizes commas only within their respective scopes.

### `CursorSelectFetchRewriter.__init__` - L28-L35

```python
__init__(self, *, fixed_format: FixedFormatLineService, column_parser: CursorSelectColumnParser) -> None
```

### `CursorSelectFetchRewriter.remove_select_positions` - L37-L71

```python
remove_select_positions(self, block: list[str], positions: set[int]) -> list[str]
```

Observed calls (lexical order): `self.fixed_format.logical`, `SELECT_KEYWORD_PATTERN.match`, `output.append`, `FROM_PATTERN.search`, `self.normalize_select_commas`, `self.column_parser.select_column_from_logical`.

Control points:

- L46: `for line in block`
- L49: `if SELECT_KEYWORD_PATTERN.match(logical)`
- L54: `if in_select and FROM_PATTERN.search(logical)`
- L60: `if in_select`
- L63: `if column`
- L66: `if position in positions`

### `CursorSelectFetchRewriter.remove_fetch_positions` - L73-L104

```python
remove_fetch_positions(self, block: list[str], positions: set[int]) -> list[str]
```

Observed calls (lexical order): `self.fixed_format.logical`, `logical.upper`, `output.append`, `END_EXEC_PATTERN.search`, `self.normalize_fetch_commas`, `HOST_REFERENCE_PATTERN.search`.

Control points:

- L82: `for line in block`
- L85: `if logical.upper() == 'INTO'`
- L90: `if in_into and END_EXEC_PATTERN.search(logical)`
- L96: `if in_into and HOST_REFERENCE_PATTERN.search(logical)`
- L99: `if position in positions`

### `CursorSelectFetchRewriter.normalize_select_commas` - L106-L144

```python
normalize_select_commas(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `list`, `enumerate`, `self.fixed_format.logical`, `SELECT_KEYWORD_PATTERN.match`, `FROM_PATTERN.search`, `self.column_parser.select_column_from_logical`, `indexes.append`, `logical.lstrip`, `logical.lstrip(',').strip`, `self.fixed_format.replace_body`.

Control points:

- L114: `for (index, line) in enumerate(result)`
- L117: `if SELECT_KEYWORD_PATTERN.match(logical)`
- L121: `if in_select and FROM_PATTERN.search(logical)`
- L124: `if not in_select`
- L129: `if column`
- L132: `for (item_number, line_index) in enumerate(indexes)`
- L137: `if item_number == 0`

### `CursorSelectFetchRewriter.normalize_fetch_commas` - L146-L182

```python
normalize_fetch_commas(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `list`, `enumerate`, `self.fixed_format.logical`, `logical.upper`, `END_EXEC_PATTERN.search`, `HOST_REFERENCE_PATTERN.search`, `indexes.append`, `self.fixed_format.logical(line).rstrip`, `len`, `self.fixed_format.replace_body`.

Control points:

- L154: `for (index, line) in enumerate(result)`
- L157: `if logical.upper() == 'INTO'`
- L161: `if in_into and END_EXEC_PATTERN.search(logical)`
- L164: `if not in_into`
- L167: `if HOST_REFERENCE_PATTERN.search(logical)`
- L170: `for (item_number, line_index) in enumerate(indexes)`
- L174: `if item_number < len(indexes) - 1`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
