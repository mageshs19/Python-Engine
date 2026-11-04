# `converter/generators/restart/restart_name_resolver.py`

Source: [converter/generators/restart/restart_name_resolver.py](../../../../../converter/generators/restart/restart_name_resolver.py) | 820 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `5266a6553a8ee9be00450c7472f636bf806f5c5af87c0511e5110e411764ab68`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Resolves the program-side names the restart templates need.

## Module-level bindings

`EOF_SUFFIX` (L195), `NOT_EOF_INFIX` (L196), `EOF_TRUE_VALUE` (L197), `EOF_FALSE_VALUE` (L198), `PICTURE_PREFIX` (L199), `LEVEL_88` (L200), `AT_END_MOVE_PATTERN` (L203), `AT_END_SET_PATTERN` (L207), `READ_PATTERN` (L215), `DATA_RECORD_PATTERN` (L221), `FD_BLOCK_TERMINATORS` (L226), `__all__` (L820)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from catalogs.restart_paragraph_catalog import DEFAULT_ABEND_MODULE, DEFAULT_COMMIT_COUNTER, DEFAULT_ERROR_PARAGRAPH, DEFAULT_INPUT_COUNTER, DEFAULT_INPUT_SAVE_AREA, DEFAULT_PROGRAM_CONSTANT, DEFAULT_READ_COUNT_FIELD, DEFAULT_READ_PARAGRAPH, DEFAULT_RESTART_KEY_FIELD, DEFAULT_RESTART_RECORD, DEFAULT_RUN_DATE_FIELD
from catalogs.restart_storage_catalog import DEFAULT_READ_COUNT_SIZE, DEFAULT_RESTART_KEY_SIZE, EOF_CONDITION_SUFFIX, GENERATED_STORAGE_FIELDS, NOT_EOF_CONDITION_SUFFIX
from converter.generators.restart.restart_config import RestartProgramNames
from converter.services.name_derivation_resolver import NameDerivationResolver
from patterns.restart_patterns import ELEMENTARY_ITEM_PATTERN, FD_PATTERN, LEVEL_88_PATTERN, OPEN_INPUT_PATTERN, PARAGRAPH_HEADER_PATTERN, PERFORM_UNTIL_PATTERN, PICTURE_SIZE_PATTERN, PROCEDURE_DIVISION_PATTERN, READ_INTO_PATTERN, SQL_INCLUDE_PATTERN
from rules.restart_standard_rules import RESTART_PARAGRAPH_PREFIXES
```

## Local dependency notes

- [catalogs/restart_paragraph_catalog.py](../../../catalogs/restart_paragraph_catalog.md)
- [catalogs/restart_storage_catalog.py](../../../catalogs/restart_storage_catalog.md)
- [converter/generators/restart/restart_config.py](restart_config.md)
- [converter/services/name_derivation_resolver.py](../../services/name_derivation_resolver.md)
- [patterns/restart_patterns.py](../../../patterns/restart_patterns.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](../../composers/restart/restart_injection_composer.md)
- [tests/restart/test_m10c_golden_output.py](../../../tests/restart/test_m10c_golden_output.md)
- [tests/restart/test_m3_name_resolver.py](../../../tests/restart/test_m3_name_resolver.md)
- [tests/restart/test_m9b_injection_composer.py](../../../tests/restart/test_m9b_injection_composer.md)

## Symbol contracts and control points

### `ResolutionReport` - L230-L236

```python
class ResolutionReport()
```

What was found, what was defaulted, what was refused.

Declared class/data-model fields:

```python
resolved: dict[str, object]
defaulted: list[str]
refused: list[str]
messages: list[str]
```

### `RestartNameResolver` - L239-L817

```python
class RestartNameResolver()
```

Turns COBOL source lines into RestartProgramNames.

### `RestartNameResolver.__init__` - L242-L245

```python
__init__(self, line_utils) -> None
```

`line_utils` is the SHARED retrieval utility.

### `RestartNameResolver.resolve` - L251-L330

```python
resolve(self, lines: list[str]) -> tuple[RestartProgramNames, ResolutionReport]
```

Observed calls (lexical order): `self._logical_lines`, `self._procedure_index`, `self._declared_items`, `self._file_and_record`, `self._eof_measured`, `self._eof_conditions`, `self._read_paragraph`, `self._process_paragraph`, `self._declared_or_blank`, `self._error_paragraph`, `self._declared_or_generated`, `self._measured_or_catalogued`, `RestartProgramNames`, `found.items`, `self._report`.

### `RestartNameResolver._logical_lines` - L336-L343

```python
_logical_lines(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self.line_utils.logical`, `str`, `str(self.line_utils.logical(raw) or '').strip`, `self.line_utils.is_comment`, `' '.join`, `logical.upper`, `logical.upper().split`, `out.append`.

Control points:

- L338: `for raw in lines or []`
- L340: `if not logical or self.line_utils.is_comment(logical)`

### `RestartNameResolver._procedure_index` - L346-L350

```python
_procedure_index(logical: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `PROCEDURE_DIVISION_PATTERN.match`, `len`.

Control points:

- L347: `for (index, line) in enumerate(logical)`
- L348: `if PROCEDURE_DIVISION_PATTERN.match(line)`

### `RestartNameResolver._declared_items` - L357-L373

```python
_declared_items(data: list[str]) -> dict[str, int]
```

Declared name -> PICTURE size, 0 when the item is a group.

Observed calls (lexical order): `ELEMENTARY_ITEM_PATTERN.match`, `PICTURE_SIZE_PATTERN.match`, `match.group`, `int`, `size.group`, `line.split`, `len`, `parts[0].isdigit`, `items.setdefault`, `parts[1].rstrip`.

Control points:

- L360: `for line in data`
- L362: `if match`
- L371: `if len(parts) >= 2 and parts[0].isdigit()`

### `RestartNameResolver._declared_or_blank` - L376-L378

```python
_declared_or_blank(declared: dict[str, int], candidate: str) -> str
```

A PROGRAM-owned name. Absent means absent.

### `RestartNameResolver._declared_or_generated` - L380-L397

```python
_declared_or_generated(self, declared: dict[str, int], candidate: str, role: str) -> str
```

A GENERATOR-owned name.

Observed calls (lexical order): `self._defaulted.append`.

Control points:

- L392: `if candidate in declared`
- L394: `if role in GENERATED_STORAGE_FIELDS`

### `RestartNameResolver._measured_or_catalogued` - L399-L411

```python
_measured_or_catalogued(self, declared: dict[str, int], field: str, fallback: int, role: str) -> int
```

A PICTURE size. Measured when present, catalogued when not.

Observed calls (lexical order): `declared.get`, `int`, `self._defaulted.append`.

Control points:

- L408: `if size > 0`

### `RestartNameResolver._file_and_record` - L418-L453

```python
_file_and_record(cls, data: list[str], procedure: list[str]) -> tuple[str, str]
```

The input file and the record the reader populates.

Observed calls (lexical order): `READ_INTO_PATTERN.match`, `match.group`, `READ_PATTERN.match`, `OPEN_INPUT_PATTERN.match`, `FD_PATTERN.match`, `cls._fd_record`.

Control points:

- L427: `for line in procedure`
- L429: `if match`
- L433: `for line in procedure`
- L435: `if match`
- L439: `if not file_name`
- L440: `for line in procedure`
- L442: `if match`
- L446: `if not file_name`
- Another 2 conditions/loops exist in this source span.

### `RestartNameResolver._fd_record` - L456-L491

```python
_fd_record(data: list[str], file_name: str) -> str
```

The record declared under FD <file_name>.

Observed calls (lexical order): `str`, `str(file_name or '').strip`, `str(file_name or '').strip().upper`, `line.split`, `FD_PATTERN.match`, `fd.group`, `fd.group('file').upper`, `DATA_RECORD_PATTERN.match`, `stated.group`, `stated.group('record').upper`, `stated.group('record').upper().rstrip`, `len`, `parts[1].rstrip`, `parts[1].rstrip('.').upper`.

Control points:

- L464: `if not wanted`
- L468: `for line in data`
- L470: `if not parts`
- L474: `if fd`
- L478: `if not inside`
- L482: `if stated`
- L485: `if parts[0] == '01' and len(parts) >= 2`
- L488: `if parts[0] in FD_BLOCK_TERMINATORS`

### `RestartNameResolver._eof_measured` - L497-L514

```python
_eof_measured(self, data: list[str], procedure: list[str]) -> tuple[str, str]
```

The pair the SOURCE declares. Empty when it declares none.

Observed calls (lexical order): `self._eof_by_convention`, `self._eof_by_value`.

Control points:

- L510: `if eof and not_eof`

### `RestartNameResolver._eof_conditions` - L516-L534

```python
_eof_conditions(self, measured: tuple[str, str], record_name: str) -> tuple[str, str]
```

The pair the GENERATED family will use.

Observed calls (lexical order): `self._eof_by_record`, `self._defaulted.append`.

Control points:

- L523: `if eof and not_eof`
- L527: `if not eof and built_eof`
- L530: `if not not_eof and built_not_eof`

### `RestartNameResolver._eof_by_record` - L537-L611

```python
_eof_by_record(record_name: str) -> tuple[str, str]
```

<record>-EOF / <record>-NOT-EOF, the catalogued convention, composed on the DERIVED record name.

Observed calls (lexical order): `str`, `str(record_name or '').strip`, `str(record_name or '').strip().upper`, `str(NameDerivationResolver().derive(record) or record).strip`, `str(NameDerivationResolver().derive(record) or record).strip().upper`, `NameDerivationResolver`, `NameDerivationResolver().derive`.

Control points:

- L601: `if not record`

### `RestartNameResolver._eof_by_convention` - L613-L626

```python
_eof_by_convention(data: list[str]) -> tuple[str, str]
```

The documented <record>-EOF / <record>-NOT-EOF naming.

Observed calls (lexical order): `LEVEL_88_PATTERN.match`, `match.group`, `name.endswith`.

Control points:

- L617: `for line in data`
- L619: `if not match`
- L622: `if NOT_EOF_INFIX in name`
- L624: `if name.endswith(EOF_SUFFIX) and value == EOF_TRUE_VALUE`

### `RestartNameResolver._eof_by_value` - L629-L650

```python
_eof_by_value(cls, data: list[str], procedure: list[str]) -> tuple[str, str]
```

The 88-levels of the switch the reader sets at end of file.

Observed calls (lexical order): `cls._at_end_condition`, `cls._sibling_of`, `cls._at_end_switch`, `cls._conditions_under`.

Control points:

- L636: `if condition`
- L640: `if not switch`
- L645: `for (name, value) in cls._conditions_under(data, switch)`
- L646: `if value == EOF_TRUE_VALUE`
- L648: `if value == EOF_FALSE_VALUE`

### `RestartNameResolver._at_end_switch` - L653-L659

```python
_at_end_switch(procedure: list[str]) -> str
```

The field a reader MOVEs its end-of-file value into.

Observed calls (lexical order): `AT_END_MOVE_PATTERN.search`, `match.group`, `match.group('switch').upper`, `match.group('switch').upper().rstrip`.

Control points:

- L655: `for line in procedure`
- L657: `if match`

### `RestartNameResolver._at_end_condition` - L662-L668

```python
_at_end_condition(procedure: list[str]) -> str
```

The 88 a reader SETs TO TRUE at end of file.

Observed calls (lexical order): `AT_END_SET_PATTERN.search`, `match.group`, `match.group('condition').upper`, `match.group('condition').upper().rstrip`.

Control points:

- L664: `for line in procedure`
- L666: `if match`

### `RestartNameResolver._conditions_under` - L671-L697

```python
_conditions_under(data: list[str], switch: str) -> list[tuple[str, str]]
```

(name, value) of every 88 subordinate to `switch`.

Observed calls (lexical order): `line.split`, `LEVEL_88_PATTERN.match`, `out.append`, `match.group`, `parts[0].isdigit`, `len`, `parts[1].rstrip`, `parts[1].rstrip('.').upper`.

Control points:

- L678: `for line in data`
- L680: `if not parts`
- L683: `if parts[0] == LEVEL_88`
- L684: `if inside`
- L686: `if match`
- L692: `if parts[0].isdigit()`

### `RestartNameResolver._sibling_of` - L700-L720

```python
_sibling_of(cls, data: list[str], condition: str) -> str
```

The other 88 declared beside `condition`.

Observed calls (lexical order): `line.split`, `LEVEL_88_PATTERN.match`, `group.append`, `match.group`, `parts[0].isdigit`.

Control points:

- L703: `for line in data`
- L705: `if not parts`
- L707: `if parts[0] == LEVEL_88`
- L709: `if match`
- L712: `if parts[0].isdigit()`
- L713: `if condition in group`
- L717: `for name in group`
- L718: `if name != condition`

### `RestartNameResolver._read_paragraph` - L727-L739

```python
_read_paragraph(procedure: list[str]) -> str
```

The paragraph that owns the READ - either READ form.

Observed calls (lexical order): `match.group`, `PARAGRAPH_HEADER_PATTERN.match`, `enumerate`, `READ_INTO_PATTERN.match`, `READ_PATTERN.match`, `RestartNameResolver._owner`.

Control points:

- L734: `if DEFAULT_READ_PARAGRAPH in headers`
- L736: `for (index, line) in enumerate(procedure)`
- L737: `if READ_INTO_PATTERN.match(line) or READ_PATTERN.match(line)`

### `RestartNameResolver._owner` - L742-L748

```python
_owner(procedure: list[str], index: int) -> str
```

Observed calls (lexical order): `range`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`.

Control points:

- L744: `for position in range(index)`
- L746: `if match`

### `RestartNameResolver._process_paragraph` - L751-L767

```python
_process_paragraph(procedure: list[str], measured_eof: str) -> str
```

The business loop.

Observed calls (lexical order): `PERFORM_UNTIL_PATTERN.match`, `match.group`, `RestartNameResolver._is_infrastructure`.

Control points:

- L757: `for line in procedure`
- L759: `if not match`
- L762: `if RestartNameResolver._is_infrastructure(name)`
- L764: `if measured_eof and measured_eof not in match.group('condition')`

### `RestartNameResolver._is_infrastructure` - L770-L773

```python
_is_infrastructure(name: str) -> bool
```

Observed calls (lexical order): `any`, `name.startswith`.

### `RestartNameResolver._error_paragraph` - L776-L782

```python
_error_paragraph(logical: list[str]) -> str
```

The SQL error paragraph, only when its include is present.

Observed calls (lexical order): `SQL_INCLUDE_PATTERN.match`, `match.group`.

Control points:

- L778: `for line in logical`
- L780: `if match and match.group('name') == DEFAULT_ERROR_PARAGRAPH`

### `RestartNameResolver._report` - L789-L817

```python
_report(found: dict[str, object], names: RestartProgramNames, defaulted: list[str]) -> ResolutionReport
```

Observed calls (lexical order): `list`, `names.missing`, `set`, `sorted`, `messages.extend`, `found.get`, `found.items`, `ResolutionReport`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
