# `converter/composers/db2_date_working_storage_manager.py`

Source: [converter/composers/db2_date_working_storage_manager.py](../../../../converter/composers/db2_date_working_storage_manager.py) | 217 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `c8359b9efd4e60e624dc10133df080df26ccd3c003357aa07907a2ba9e336cc0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date Working-Storage manager.

## Module-level bindings

`WS_DATUMVELDEN_PREFIX` (L23), `LEVEL_01_PREFIX` (L24)

## Import declarations

```python
from converter.composers.db2_date_line_utils import Db2DateLineUtils
from patterns.db2_date_patterns import DATE_WORKING_STORAGE_MARKER_PATTERN, DB2_DATE_WORKING_STORAGE_BASE_PATTERN, LINKAGE_SECTION_PATTERN, PROCEDURE_DIVISION_PATTERN
from rules.db2_date_conversion_rules import DB2_DATE_BASE_WORKING_STORAGE_LINES, DB2_DATE_HELPER_FIELD_TEMPLATE
```

## Local dependency notes

- [converter/composers/db2_date_line_utils.py](db2_date_line_utils.md)
- [patterns/db2_date_patterns.py](../../patterns/db2_date_patterns.md)
- [rules/db2_date_conversion_rules.py](../../rules/db2_date_conversion_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/db2_date_comparison_composer.py](db2_date_comparison_composer.md)
- [converter/composers/schema_date_transfer_composer.py](schema_date_transfer_composer.md)

## Symbol contracts and control points

### `Db2DateWorkingStorageManager` - L27-L217

```python
class Db2DateWorkingStorageManager()
```

### `Db2DateWorkingStorageManager.__init__` - L28-L32

```python
__init__(self, line_utils: Db2DateLineUtils | None=None) -> None
```

Observed calls (lexical order): `Db2DateLineUtils`.

### `Db2DateWorkingStorageManager._logical` - L34-L35

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `Db2DateWorkingStorageManager.ensure_date_working_storage` - L37-L63

```python
ensure_date_working_storage(self, lines: list[str], date_fields: list[str]) -> list[str]
```

Ensure DB2 date Working-Storage exists.

Observed calls (lexical order): `self._has_date_working_storage`, `self._date_working_storage_block`, `self._date_working_storage_insert_index`, `self._ensure_missing_date_helper_fields`.

Control points:

- L51: `if not self._has_date_working_storage(lines)`
- L55: `if insert_index < 0`

### `Db2DateWorkingStorageManager._ensure_missing_date_helper_fields` - L65-L102

```python
_ensure_missing_date_helper_fields(self, lines: list[str], date_fields: list[str]) -> list[str]
```

Add missing HELP-* date fields when WS-DATUMVELDEN already exists.

Observed calls (lexical order): `self.line_utils.helper_name`, `self._helper_declared`, `missing_helpers.append`, `DB2_DATE_HELPER_FIELD_TEMPLATE.format`, `self._date_helper_insert_index`.

Control points:

- L76: `if not date_fields`
- L81: `for field_name in date_fields`
- L84: `if self._helper_declared(lines=lines, helper=helper)`
- L89: `if not missing_helpers`
- L99: `if insert_index < 0`

### `Db2DateWorkingStorageManager._helper_declared` - L104-L128

```python
_helper_declared(self, lines: list[str], helper: str) -> bool
```

Return True only when the HELP-* field is declared before PROCEDURE DIVISION. A PROCEDURE DIVISION usage must not count as a declaration, which avoids false positives on reruns.

Observed calls (lexical order): `str`, `str(helper or '').strip`, `str(helper or '').strip().upper`, `self._logical`, `PROCEDURE_DIVISION_PATTERN.match`, `logical.upper`.

Control points:

- L116: `if not helper_upper`
- L119: `for line in lines`
- L122: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L125: `if helper_upper in logical.upper()`

### `Db2DateWorkingStorageManager._date_helper_insert_index` - L130-L162

```python
_date_helper_insert_index(self, lines: list[str]) -> int
```

Return index where missing HELP-* fields should be inserted.

Observed calls (lexical order): `enumerate`, `self._logical`, `logical.upper`, `upper_logical.startswith`, `LINKAGE_SECTION_PATTERN.match`, `PROCEDURE_DIVISION_PATTERN.match`.

Control points:

- L142: `for (index, line) in enumerate(lines)`
- L146: `if upper_logical.startswith(WS_DATUMVELDEN_PREFIX)`
- L150: `if not ws_datumvelden_seen`
- L153: `if LINKAGE_SECTION_PATTERN.match(logical)`
- L156: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L159: `if upper_logical.startswith(LEVEL_01_PREFIX)`

### `Db2DateWorkingStorageManager._has_date_working_storage` - L164-L187

```python
_has_date_working_storage(self, lines: list[str]) -> bool
```

Observed calls (lexical order): `self._logical`, `DATE_WORKING_STORAGE_MARKER_PATTERN.search`, `PROCEDURE_DIVISION_PATTERN.match`, `logical.upper`, `upper_logical.startswith`, `DB2_DATE_WORKING_STORAGE_BASE_PATTERN.search`.

Control points:

- L167: `for line in lines`
- L170: `if DATE_WORKING_STORAGE_MARKER_PATTERN.search(line)`
- L173: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L176: `if in_procedure_division`
- L181: `if upper_logical.startswith(WS_DATUMVELDEN_PREFIX)`
- L184: `if DB2_DATE_WORKING_STORAGE_BASE_PATTERN.search(upper_logical)`

### `Db2DateWorkingStorageManager._date_working_storage_insert_index` - L189-L202

```python
_date_working_storage_insert_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self._logical`, `LINKAGE_SECTION_PATTERN.match`, `PROCEDURE_DIVISION_PATTERN.match`.

Control points:

- L190: `for (index, line) in enumerate(lines)`
- L193: `if LINKAGE_SECTION_PATTERN.match(logical)`
- L196: `for (index, line) in enumerate(lines)`
- L199: `if PROCEDURE_DIVISION_PATTERN.match(logical)`

### `Db2DateWorkingStorageManager._date_working_storage_block` - L204-L217

```python
_date_working_storage_block(self, date_fields: list[str]) -> list[str]
```

Observed calls (lexical order): `list`, `self.line_utils.helper_name`, `lines.append`, `DB2_DATE_HELPER_FIELD_TEMPLATE.format`.

Control points:

- L210: `for field_name in date_fields`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
