# `converter/composers/update_sql_cleanup/sql_block_scanner.py`

Source: [converter/composers/update_sql_cleanup/sql_block_scanner.py](../../../../../converter/composers/update_sql_cleanup/sql_block_scanner.py) | 76 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `49202a0148278056e1759d08bc33db53feb045ad7f11c339936ec559461b8c46`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQL block scanner.

## Import declarations

```python
from __future__ import annotations
from converter.composers.update_sql_cleanup.update_sql_cleanup_patterns import SQLCODE_EVALUATE_PATTERN
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/update_sql_cleanup_patterns.py](update_sql_cleanup_patterns.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)

## Symbol contracts and control points

### `SqlBlockScanner` - L19-L76

```python
class SqlBlockScanner()
```

### `SqlBlockScanner.__init__` - L20-L24

```python
__init__(self, owner) -> None
```

### `SqlBlockScanner.next_modify_record` - L26-L38

```python
next_modify_record(self, lines: list[str], start_index: int, max_distance: int) -> str
```

Observed calls (lexical order): `len`, `min`, `range`, `self.owner._logical`, `self.owner.CONVERTED_MODIFY_PATTERN.match`, `NameNormalizer.normalize`, `match.group`.

Control points:

- L33: `for index in range(start_index + 1, end)`
- L36: `if match`

### `SqlBlockScanner.skip_generated_sql_and_sqlcode` - L40-L76

```python
skip_generated_sql_and_sqlcode(self, lines: list[str], start: int) -> int
```

Observed calls (lexical order): `len`, `self.owner._logical`, `logical.upper`, `upper.startswith`, `self.owner.EXEC_SQL_START_PATTERN.match`, `self.owner._skip_exec_sql`, `self.owner.SQLCODE_IF_PATTERN.match`, `self.owner._skip_if_block`, `SQLCODE_EVALUATE_PATTERN.match`, `self.owner._skip_evaluate_block`.

Control points:

- L46: `while index < len(lines)`
- L50: `if not logical`
- L54: `if upper.startswith("MOVE 'SELECT-") or upper.startswith("MOVE 'UPDATE-")`
- L60: `if self.owner.EXEC_SQL_START_PATTERN.match(logical)`
- L65: `if self.owner.SQLCODE_IF_PATTERN.match(logical)`
- L70: `if SQLCODE_EVALUATE_PATTERN.match(logical)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
