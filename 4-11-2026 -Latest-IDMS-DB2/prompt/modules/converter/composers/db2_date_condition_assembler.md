# `converter/composers/db2_date_condition_assembler.py`

Source: [converter/composers/db2_date_condition_assembler.py](../../../../converter/composers/db2_date_condition_assembler.py) | 213 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `c34f1df07a1c44029258ae3dd9aafc8cfd507893143f26aa71500e8105fee8f5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Assembles one COBOL IF condition out of its physical lines.

## Module-level bindings

`OPEN_PAREN` (L50), `CLOSE_PAREN` (L51), `__all__` (L213)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.composers.db2_date_line_utils import Db2DateLineUtils
from patterns.db2_date_patterns import CONDITION_CONTINUATION_PATTERN, END_EXEC_PATTERN, EXEC_SQL_START_PATTERN, IF_START_PATTERN, STATEMENT_START_PATTERN, TRAILING_BOOLEAN_PATTERN
from rules.db2_date_conversion_rules import CONDITION_SCAN_LIMIT
```

## Local dependency notes

- [converter/composers/db2_date_line_utils.py](db2_date_line_utils.md)
- [patterns/db2_date_patterns.py](../../patterns/db2_date_patterns.md)
- [rules/db2_date_conversion_rules.py](../../rules/db2_date_conversion_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/db2_date_comparison_composer.py](db2_date_comparison_composer.md)
- [converter/composers/db2_date_comparison_rewriter.py](db2_date_comparison_rewriter.md)
- [converter/composers/db2_date_field_detector.py](db2_date_field_detector.md)
- [converter/transformers/field_reference_rewriter.py](../transformers/field_reference_rewriter.md)
- [tests/test_db2_date_comparison.py](../../tests/test_db2_date_comparison.md)

## Symbol contracts and control points

### `ConditionSpan` - L55-L67

```python
class ConditionSpan()
```

One IF condition and the physical lines that carry it.

Declared class/data-model fields:

```python
start_index: int = -1
end_index: int = -1
indent: str = ''
text: str = ''
line_indexes: list[int] = field(default_factory=list)
complete: bool = True
```

### `ConditionSpan.line_count` - L66-L67

```python
line_count(self) -> int
```

Observed calls (lexical order): `len`.

### `Db2DateConditionAssembler` - L70-L210

```python
class Db2DateConditionAssembler()
```

Finds IF conditions and joins their physical lines.

### `Db2DateConditionAssembler.__init__` - L73-L77

```python
__init__(self, line_utils: Db2DateLineUtils | None=None) -> None
```

Observed calls (lexical order): `Db2DateLineUtils`.

### `Db2DateConditionAssembler.span_at` - L82-L139

```python
span_at(self, lines: list[str], index: int) -> ConditionSpan | None
```

The condition starting at `index`, or None when it is not an IF.

Observed calls (lexical order): `len`, `self.line_utils.logical`, `self.line_utils.is_comment_or_blank`, `IF_START_PATTERN.match`, `match.group`, `str`, `str(match.group('rest') or '').strip`, `self._depth`, `self._is_complete`, `body.strip`, `parts.append`, `used.append`, `ConditionSpan`, `' '.join`, `' '.join((part for part in parts if part)).strip`.

Control points:

- L88: `if not 0 <= index < len(lines)`
- L93: `if self.line_utils.is_comment_or_blank(logical)`
- L98: `if not match`
- L113: `while not complete and scanned < CONDITION_SCAN_LIMIT`
- L114: `if cursor >= len(lines)`
- L119: `if self.line_utils.is_comment_or_blank(body)`

### `Db2DateConditionAssembler.spans` - L141-L170

```python
spans(self, lines: list[str]) -> list[ConditionSpan]
```

Every IF condition in the program, EXEC SQL blocks excluded.

Observed calls (lexical order): `len`, `self.line_utils.logical`, `EXEC_SQL_START_PATTERN.match`, `END_EXEC_PATTERN.search`, `self.span_at`, `output.append`.

Control points:

- L147: `while index < len(lines)`
- L150: `if EXEC_SQL_START_PATTERN.match(logical)`
- L155: `if in_exec_sql`
- L156: `if END_EXEC_PATTERN.search(logical)`
- L163: `if span is None`

### `Db2DateConditionAssembler._is_complete` - L175-L188

```python
_is_complete(self, previous: str, depth: int, lines: list[str], cursor: int) -> bool
```

Observed calls (lexical order): `TRAILING_BOOLEAN_PATTERN.search`, `self._next_continues`.

Control points:

- L182: `if depth > 0`
- L185: `if TRAILING_BOOLEAN_PATTERN.search(previous or '')`

### `Db2DateConditionAssembler._next_continues` - L190-L205

```python
_next_continues(self, lines: list[str], cursor: int) -> bool
```

Observed calls (lexical order): `len`, `self.line_utils.logical`, `self.line_utils.is_comment_or_blank`, `STATEMENT_START_PATTERN.match`, `CONDITION_CONTINUATION_PATTERN.match`, `bool`.

Control points:

- L193: `while index < len(lines)`
- L196: `if self.line_utils.is_comment_or_blank(body)`
- L200: `if STATEMENT_START_PATTERN.match(body)`

### `Db2DateConditionAssembler._depth` - L208-L210

```python
_depth(text: str) -> int
```

Observed calls (lexical order): `str`, `body.count`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
