# `converter/postprocess/storage_include/storage_ws_injector.py`

Source: [converter/postprocess/storage_include/storage_ws_injector.py](../../../../../converter/postprocess/storage_include/storage_ws_injector.py) | 469 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `e96732dbb07bb37f6bc9a06cd92756dc7a6639d04741e597accbd944ff281305`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.dynamic_metadata_resolver import UpdateProgramContext
from patterns.update_restart_patterns import MALFORMED_SQLERROR_END_EVALUATE_PATTERN
from patterns.update_storage_include_patterns import CS_PROGRAM_01_PATTERN, PROGRAM_NAME_MOVE_PATTERN, CS_PROGRAM_DECLARATION_PATTERN
from rules.update_restart_rules import UPDATE_RESTART_DIAGNOSTICS, UPDATE_RESTART_WS_NAMES
from rules.update_storage_include_rules import CS_PROGRAM_77_TEMPLATE, DATE_WS_ANCHORS, DATE_WS_EXISTS_UNDER_OTHER_GROUP, PROGRAM_NAME_MOVE_REPLACEMENT_TEMPLATE, SKIP_DATA_DIVISION_DATE_WS, SKIP_DATA_DIVISION_WS
from patterns.db2_date_patterns import DB2_DATE_WORKING_STORAGE_BASE_PATTERN, PROCEDURE_DIVISION_PATTERN
import re
```

## Local dependency notes

- [converter/postprocess/dynamic_metadata_resolver.py](../dynamic_metadata_resolver.md)
- [patterns/db2_date_patterns.py](../../../patterns/db2_date_patterns.md)
- [patterns/update_restart_patterns.py](../../../patterns/update_restart_patterns.md)
- [patterns/update_storage_include_patterns.py](../../../patterns/update_storage_include_patterns.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)
- [rules/update_storage_include_rules.py](../../../rules/update_storage_include_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_storage_include_manager.py](../update_storage_include_manager.md)
- [tests/postprocess/test_ensure_working_storage_whitespace_tolerant.py](../../../tests/postprocess/test_ensure_working_storage_whitespace_tolerant.md)

## Symbol contracts and control points

### `StorageWsInjector` - L32-L469

```python
class StorageWsInjector()
```

Working-storage, date-WS, program-name and SQLERROR passes.

### `StorageWsInjector.fix_malformed_sqlerror` - L38-L45

```python
fix_malformed_sqlerror(self, cobol_text, diagnostics)
```

Observed calls (lexical order): `MALFORMED_SQLERROR_END_EVALUATE_PATTERN.sub`, `diagnostics.append`.

Control points:

- L43: `if updated != cobol_text`

### `StorageWsInjector.normalize_program_name` - L47-L140

```python
normalize_program_name(self, cobol_text, context, diagnostics)
```

Normalise the PROGRAM-NAME move and the program constant.

Observed calls (lexical order): `str`, `str(context.program_id or '').strip`, `str(context.program_id or '').strip().upper`, `PROGRAM_NAME_MOVE_PATTERN.sub`, `PROGRAM_NAME_MOVE_REPLACEMENT_TEMPLATE.format`, `CS_PROGRAM_01_PATTERN.sub`, `CS_PROGRAM_77_TEMPLATE.format`, `match.group`, `self._program_constant_declared`, `diagnostics.append`, `self.line_utils.lines`, `self._data_division_end_index`, `self._find_77_level_insert_point`, `self.line_utils.join`.

Control points:

- L90: `if not program_id`
- L105: `if self._program_constant_declared(updated)`
- L110: `if updated != cobol_text`
- L120: `if 0 <= insert_index <= boundary`
- L136: `if updated != cobol_text`

### `StorageWsInjector._program_constant_declared` - L142-L156

```python
_program_constant_declared(self, cobol_text) -> bool
```

CS-PROGRAM declared at ANY level, DATA DIVISION only.

Observed calls (lexical order): `self.line_utils.lines`, `self.line_utils.logical`, `str`, `logical.lstrip`, `logical.lstrip().startswith`, `PROCEDURE_DIVISION_PATTERN.match`, `CS_PROGRAM_DECLARATION_PATTERN.match`.

Control points:

- L144: `for line in self.line_utils.lines(cobol_text)`
- L147: `if not logical or logical.lstrip().startswith('*')`
- L150: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L153: `if CS_PROGRAM_DECLARATION_PATTERN.match(logical)`

### `StorageWsInjector._data_division_end_index` - L158-L165

```python
_data_division_end_index(self, lines) -> int
```

Index of the PROCEDURE DIVISION header, or the line count.

Observed calls (lexical order): `enumerate`, `self.line_utils.logical`, `str`, `PROCEDURE_DIVISION_PATTERN.match`, `len`.

Control points:

- L160: `for (index, line) in enumerate(lines)`
- L162: `if PROCEDURE_DIVISION_PATTERN.match(logical)`

### `StorageWsInjector._find_77_level_insert_point` - L167-L215

```python
_find_77_level_insert_point(self, cobol_text: str) -> int
```

Find line index where 77-level declarations should be inserted.

Observed calls (lexical order): `self.line_utils.lines`, `enumerate`, `line.upper`, `re.match`, `len`.

Control points:

- L184: `for (i, line) in enumerate(lines)`
- L188: `if 'WORKING-STORAGE SECTION' in line_upper`
- L193: `if working_storage_idx >= 0`
- L195: `if re.match('^\\s*77\\s+', line, re.IGNORECASE)`
- L199: `if first_01_idx < 0 and re.match('^\\s*01\\s+', line, re.IGNORECASE)`
- L203: `if working_storage_idx < 0`
- L207: `if last_77_idx >= 0`
- L211: `if first_01_idx >= 0`

### `StorageWsInjector.ensure_working_storage` - L217-L274

```python
ensure_working_storage(self, cobol_text, context, diagnostics)
```

Ensure WORKING-STORAGE section has required groups.

Observed calls (lexical order): `self._has_ws_items_in_file_section`, `diagnostics.append`, `self._remove_ws_items_from_file_section`, `self._declares_group`, `self.line_utils.lines`, `self.line_utils.data_division_insert_line_index`, `self.generator.working_storage`, `self.generator.working_storage(context).splitlines`, `self.line_utils.join`.

Control points:

- L249: `if self._has_ws_items_in_file_section(cobol_text)`
- L259: `if self._declares_group(cobol_text, names['switch_group']) and self._declares_group(cobol_text, names['help_group'])`
- L267: `if insert_index < 0`

### `StorageWsInjector._declares_group` - L276-L296

```python
_declares_group(self, cobol_text: str, group_name: str) -> bool
```

True when `01 <group_name>.` is already declared, regardless of how many spaces separate the level number from the name - COBOL permits any amount of Area A/B whitespace there, and a different generator (RestartStorageInjector) may align it differently than this one does. See CORRECTION in ensure_working_storage() above.

Observed calls (lexical order): `str`, `str(group_name or '').strip`, `str(group_name or '').strip().upper`, `re.compile`, `re.escape`, `self.line_utils.lines`, `self.line_utils.logical`, `str(self.line_utils.logical(line) or '').strip`, `pattern.match`.

Control points:

- L286: `if not wanted`
- L292: `for line in self.line_utils.lines(cobol_text)`
- L294: `if pattern.match(logical)`

### `StorageWsInjector._has_ws_items_in_file_section` - L298-L333

```python
_has_ws_items_in_file_section(self, cobol_text: str) -> bool
```

Check if WORKING-STORAGE items exist in FILE SECTION.

Observed calls (lexical order): `cobol_text.split`, `line.upper`, `re.match`.

Control points:

- L310: `for line in lines`
- L314: `if 'FILE SECTION' in line_upper`
- L319: `if 'WORKING-STORAGE SECTION' in line_upper`
- L325: `if in_file_section`
- L327: `if re.match('^\\s*01\\s+WS-', line, re.IGNORECASE)`
- L330: `if re.match('^\\s*0[1-9]\\s+(WS-|SW-|WS\\s+)', line, re.IGNORECASE)`

### `StorageWsInjector._remove_ws_items_from_file_section` - L335-L386

```python
_remove_ws_items_from_file_section(self, cobol_text: str, diagnostics: list) -> str
```

Remove WORKING-STORAGE items from FILE SECTION.

Observed calls (lexical order): `cobol_text.split`, `enumerate`, `line.upper`, `re.match`, `match.group`, `removed_groups.append`, `result.append`, `diagnostics.append`, `', '.join`, `'\n'.join`.

Control points:

- L351: `for (i, line) in enumerate(lines)`
- L355: `if 'FILE SECTION' in line_upper`
- L357: `if 'WORKING-STORAGE SECTION' in line_upper`
- L361: `if in_file_section and re.match('^\\s*01\\s+WS-', line, re.IGNORECASE)`
- L365: `if match`
- L370: `if skip_group`
- L372: `if re.match('^\\s*01\\s+', line, re.IGNORECASE)`
- L374: `if 'PROCEDURE DIVISION' in line_upper`
- Another 1 conditions/loops exist in this source span.

### `StorageWsInjector.ensure_date_working_storage` - L388-L450

```python
ensure_date_working_storage(self, cobol_text, diagnostics)
```

Declare the date layout once, under ANY group name.

Observed calls (lexical order): `any`, `self.line_utils.logical_contains`, `diagnostics.append`, `self._date_layout_declared`, `self.line_utils.lines`, `self.line_utils.data_division_insert_line_index`, `self.generator.date_working_storage`, `self.generator.date_working_storage().splitlines`, `self.line_utils.join`.

Control points:

- L430: `if any((self.line_utils.logical_contains(cobol_text, anchor) for anchor in DATE_WS_ANCHORS))`
- L437: `if self._date_layout_declared(cobol_text)`
- L443: `if insert_index < 0`

### `StorageWsInjector._date_layout_declared` - L452-L469

```python
_date_layout_declared(self, cobol_text) -> bool
```

True when the date fields are DECLARED under any 01 group.

Observed calls (lexical order): `self.line_utils.lines`, `self.line_utils.logical`, `str`, `logical.lstrip`, `logical.lstrip().startswith`, `PROCEDURE_DIVISION_PATTERN.match`, `DB2_DATE_WORKING_STORAGE_BASE_PATTERN.search`.

Control points:

- L457: `for line in self.line_utils.lines(cobol_text)`
- L460: `if not logical or logical.lstrip().startswith('*')`
- L463: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L466: `if DB2_DATE_WORKING_STORAGE_BASE_PATTERN.search(logical)`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
