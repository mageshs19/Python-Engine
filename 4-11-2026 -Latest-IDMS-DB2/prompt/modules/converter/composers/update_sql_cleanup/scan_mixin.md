# `converter/composers/update_sql_cleanup/scan_mixin.py`

Source: [converter/composers/update_sql_cleanup/scan_mixin.py](../../../../../converter/composers/update_sql_cleanup/scan_mixin.py) | 105 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `b3aed1b0cd3c5498a7e39b887c3ab5f564693063d941c721fbbda137c5d4b355`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Line/text helpers, block-scan helpers, and predicates.

## Import declarations

```python
from __future__ import annotations
from converter.composers.update_sql_cleanup.update_sql_cleanup_patterns import END_IF_PATTERN, EXEC_SQL_END_PATTERN
from converter.services.name_normalizer import NameNormalizer
from patterns.sequence_patterns import strip_sequence_numbers
from rules.update_sql_cleanup_rules import PROTECTED_BARE_TARGET_PREFIXES
from converter.composers.update_sql_cleanup.update_sql_cleanup_patterns import END_EVALUATE_PATTERN, END_IF_PATTERN, EXEC_SQL_END_PATTERN, LONE_PERIOD_PATTERN
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/update_sql_cleanup_patterns.py](update_sql_cleanup_patterns.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/sequence_patterns.py](../../../patterns/sequence_patterns.md)
- [rules/update_sql_cleanup_rules.py](../../../rules/update_sql_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_base.py](../update_sql_cleanup_base.md)

## Symbol contracts and control points

### `ScanMixin` - L24-L105

```python
class ScanMixin()
```

### `ScanMixin._logical` - L25-L29

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

### `ScanMixin._leading_spaces` - L31-L36

```python
_leading_spaces(self, line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `value.lstrip`.

### `ScanMixin._table_for_record` - L38-L45

```python
_table_for_record(self, record: str) -> str
```

Observed calls (lexical order): `self.mapping_repository.db2_table_for_record`, `self.table_name_resolver.resolve_table`.

Control points:

- L43: `if not mapped_table`

### `ScanMixin._is_protected_bare_target` - L47-L52

```python
_is_protected_bare_target(self, target: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `NameNormalizer.to_cobol(target).upper`, `clean.startswith`.

### `ScanMixin._skip_exec_sql` - L54-L64

```python
_skip_exec_sql(self, lines: list[str], index: int) -> int
```

Observed calls (lexical order): `len`, `self._logical`, `EXEC_SQL_END_PATTERN.match`.

Control points:

- L59: `while index < len(lines)`
- L62: `if EXEC_SQL_END_PATTERN.match(logical)`

### `ScanMixin._skip_if_block` - L66-L76

```python
_skip_if_block(self, lines: list[str], index: int) -> int
```

Observed calls (lexical order): `len`, `self._logical`, `END_IF_PATTERN.match`.

Control points:

- L71: `while index < len(lines)`
- L74: `if END_IF_PATTERN.match(logical)`

### `ScanMixin._skip_evaluate_block` - L79-L105

```python
_skip_evaluate_block(self, lines: list[str], index: int) -> int
```

Skip an EVALUATE SQLCODE ... END-EVALUATE block, including a trailing lone period line (the COBOL scope terminator emitted after END-EVALUATE).

Observed calls (lexical order): `len`, `self._logical`, `END_EVALUATE_PATTERN.match`, `LONE_PERIOD_PATTERN.match`.

Control points:

- L89: `while index < len(lines)`
- L92: `if END_EVALUATE_PATTERN.match(logical)`
- L96: `while index < len(lines)`
- L98: `if not logical`
- L101: `if LONE_PERIOD_PATTERN.match(logical)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
