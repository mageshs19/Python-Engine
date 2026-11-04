# `converter/generators/lrf_host_variable_populator.py`

Source: [converter/generators/lrf_host_variable_populator.py](../../../../converter/generators/lrf_host_variable_populator.py) | 1116 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `7645ea7a5ec14502ffc2ce16823b07256cd1147e07d6455ef8c1b34f9937bc74`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generates host-variable population code for LRF-expanded cursors.

## Module-level bindings

`LRF_EXPANSION_MARKER_PATTERN` (L119), `PERFORM_OPEN_PATTERN` (L125), `CURSOR_DECLARE_TEMPLATE` (L131), `WHERE_COLUMN_PATTERN` (L134), `_NON_COLUMN_WORDS` (L139), `_DECLARE_SCAN_LIMIT` (L143), `_PERFORM_SCAN_LIMIT` (L144), `_CONTINUATION_SCAN_LIMIT` (L145), `__all__` (L1110)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import Optional
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.cursor_spec.lrf_comment_patterns import LRF_CONTINUATION_RECORD_PATTERN, LRF_ACCESS_MARKER_PROBE, LRF_EXPANSION_PATTERN, LRF_EXPANSION_WRAPPED_PATTERN, LRF_CONTINUATION_ARROW_PATTERN, LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN
from rules.lrf_populator_rules import ALLOW_AREA_SWEEP_PATHS, ENABLE_LRF_HOST_POPULATION, ENFORCE_LRF_BODY_WIDTH, LRF_AREA_NAME_PREFIXES, LRF_BLANK_INDICATOR, LRF_BODY_WIDTH, LRF_COMMAND_RECORD_ATTRIBUTES, LRF_COMMAND_WITHIN_ATTRIBUTES, LRF_COMMENT_INDENT, LRF_COMMENT_INDICATOR, LRF_LEFT_SEQUENCE_WIDTH, LRF_PATH_COMMAND_ATTRIBUTES, LRF_POPULATOR_MESSAGES, LRF_RIGHT_SEQUENCE_WIDTH, LRF_STATEMENT_INDENT, REFUSE_ON_UNRESOLVED_PATH, LRF_CURSOR_BY_RECORD_METHODS, LRF_CURSOR_BY_TABLE_METHODS, LRF_TABLE_BY_RECORD_METHODS, LRF_HOST_GROUP_BY_TABLE_METHODS
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/cursor_spec/lrf_comment_patterns.py](../../patterns/cursor_spec/lrf_comment_patterns.md)
- [rules/lrf_populator_rules.py](../../rules/lrf_populator_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/lrf_host_variable_population.py](../pipeline/lrf_host_variable_population.md)

## Symbol contracts and control points

### `LrfPathFacts` - L154-L167

```python
class LrfPathFacts()
```

What the parsed subschema says about one LRF path keyword.

Declared class/data-model fields:

```python
target_record: str = ''
set_name: str = ''
area_name: str = ''
parent_record: str = ''
container: str = ''
resolved: bool = False
source: str = 'marker'
```

### `LrfPathFacts.is_area_sweep` - L166-L167

```python
is_area_sweep(self) -> bool
```

Observed calls (lexical order): `bool`.

### `LrfExpansionMarker` - L171-L191

```python
class LrfExpansionMarker()
```

Metadata extracted from one LRF expansion comment.

Declared class/data-model fields:

```python
mode: str = ''
logical_record: str = ''
keyword: str = ''
parent_record: str = ''
target_record: str = ''
set_name: str = ''
area_name: str = ''
cursor_name: str = ''
line_index: int = 0
```

### `LrfExpansionMarker.is_area_sweep` - L185-L186

```python
is_area_sweep(self) -> bool
```

Observed calls (lexical order): `bool`.

### `LrfExpansionMarker.record_name_display` - L189-L191

```python
record_name_display(self) -> str
```

Target record in COBOL form, for diagnostics.

Observed calls (lexical order): `str`, `str(self.target_record or '').upper`, `str(self.target_record or '').upper().replace`.

### `LrfHostVariableInitSequence` - L195-L200

```python
class LrfHostVariableInitSequence()
```

Generated initialisation code for one LRF cursor.

Declared class/data-model fields:

```python
cursor_name: str = ''
host_group_name: str = ''
initialization_lines: list[str] = field(default_factory=list)
```

### `LrfHostVariablePopulator` - L208-L1107

```python
class LrfHostVariablePopulator()
```

Injects host-variable population code ahead of an LRF cursor OPEN.

### `LrfHostVariablePopulator.__init__` - L212-L237

```python
__init__(self, host_variable_resolver=None, relationship_resolver=None, name_normalizer=None, cursor_name_resolver=None, table_name_resolver=None, lrf_path_resolver=None, lrf_repository=None, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `LrfHostVariablePopulator.augment_procedure_division` - L242-L324

```python
augment_procedure_division(self, cobol_text: str) -> tuple[str, list[str]]
```

Scan the program for LRF markers and inject host population.

Observed calls (lexical order): `str`, `self._log`, `text.split`, `self._extract_lrf_markers`, `self._find_perform_open_after`, `self._build_init_sequence`, `injection_points.setdefault`, `injection_points.setdefault(perform_index, []).extend`, `len`, `self._inject_code`, `'\n'.join`.

Control points:

- L255: `if not ENABLE_LRF_HOST_POPULATION`
- L259: `if not text`
- L267: `if not markers`
- L274: `for marker in markers`
- L279: `if marker.mode != 'FIRST'`
- L288: `if perform_index is None`
- L298: `if sequence is None or not sequence.initialization_lines`
- L313: `if not injection_points`

### `LrfHostVariablePopulator._logical_body` - L330-L347

```python
_logical_body(self, line: str) -> str
```

Columns 8-72 of a fixed-format record, indicator removed.

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L339: `if body`
- L345: `if len(text) >= 72 and text[:6].strip().isdigit()`

### `LrfHostVariablePopulator._sequence_areas` - L349-L368

```python
_sequence_areas(self, template: str) -> tuple[str, str]
```

(left, right) sequence areas borrowed from a template line.

Observed calls (lexical order): `self.fixed_format.parse_line`, `parsed.get`, `str`, `str(template or '').rstrip`, `len`, `text[:6].isdigit`.

Control points:

- L357: `if parsed and parsed.get('is_fixed_format')`

### `LrfHostVariablePopulator._render` - L370-L391

```python
_render(self, body: str, indicator: str, template: str) -> Optional[str]
```

Build one 80-column record, or None when the body will not fit.

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `len`, `self._sequence_areas`, `left.ljust`, `right.ljust`, `clean.ljust`.

Control points:

- L381: `if ENFORCE_LRF_BODY_WIDTH and len(clean) > LRF_BODY_WIDTH`

### `LrfHostVariablePopulator._first_attribute` - L398-L403

```python
_first_attribute(obj, names) -> str
```

Observed calls (lexical order): `getattr`, `str`, `str(value).strip`.

Control points:

- L399: `for name in names`
- L401: `if value`

### `LrfHostVariablePopulator._path_commands` - L405-L410

```python
_path_commands(self, path) -> list
```

Observed calls (lexical order): `getattr`, `list`.

Control points:

- L406: `for name in LRF_PATH_COMMAND_ATTRIBUTES`
- L408: `if commands`

### `LrfHostVariablePopulator._lookup_path` - L412-L447

```python
_lookup_path(self, logical_record: str, keyword: str)
```

Call the repository, probing its arity.

Observed calls (lexical order): `getattr`, `self._log`, `finder`, `type`.

Control points:

- L420: `if repository is None`
- L428: `if finder is None`
- L429: `if not self._repository_reported`

### `LrfHostVariablePopulator._path_facts` - L449-L511

```python
_path_facts(self, logical_record: str, keyword: str, fallback_record: str) -> LrfPathFacts
```

Resolve a path keyword against the parsed subschema.

Observed calls (lexical order): `self._lookup_path`, `LrfPathFacts`, `self._path_commands`, `self._log`, `self._first_attribute`, `len`, `container.upper`, `any`, `upper.startswith`.

Control points:

- L461: `if path is None`
- L469: `if not commands`
- L484: `if len(commands) > 1`
- L489: `if not target and (not container)`

### `LrfHostVariablePopulator._continuation_record` - L517-L532

```python
_continuation_record(self, lines: list[str], index: int) -> str
```

Record name opening the body after a wrapped marker.

Observed calls (lexical order): `len`, `min`, `range`, `self._logical_body`, `self._logical_body(lines[offset]).strip`, `LRF_CONTINUATION_ARROW_PATTERN.match`, `match.group`, `LRF_CONTINUATION_RECORD_PATTERN.match`.

Control points:

- L520: `for offset in range(index + 1, limit)`
- L522: `if not body`
- L525: `if match`
- L529: `if match`

### `LrfHostVariablePopulator._extract_lrf_markers` - L534-L646

```python
_extract_lrf_markers(self, lines: list[str]) -> list[LrfExpansionMarker]
```

Find every LRF expansion marker and bind it to a cursor.

Observed calls (lexical order): `enumerate`, `self._logical_body`, `body.strip`, `LRF_EXPANSION_PATTERN.search`, `match.group`, `LRF_EXPANSION_WRAPPED_PATTERN.search`, `LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN.search`, `LRF_ACCESS_MARKER_PROBE.search`, `self._log`, `self._continuation_record`, `str`, `self._path_facts`, `self._cursor_name_for_record`, `markers.append`, `LrfExpansionMarker`, `str(match.group('mode')).upper`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L547: `for (index, line) in enumerate(lines)`
- L549: `if not body.strip()`
- L555: `if match is not None`
- L559: `if match is None`
- L564: `if match is None`
- L565: `if LRF_ACCESS_MARKER_PROBE.search(body)`
- L570: `if not marker_record`
- L581: `if not facts.resolved and REFUSE_ON_UNRESOLVED_PATH`
- Another 6 conditions/loops exist in this source span.

### `LrfHostVariablePopulator._build_init_sequence` - L653-L801

```python
_build_init_sequence(self, marker: LrfExpansionMarker, lines: list[str], template: str) -> Optional[LrfHostVariableInitSequence]
```

Build host-variable initialization for one LRF cursor.

Observed calls (lexical order): `self._log`, `self._host_group_for_marker`, `self._predicate_columns`, `str`, `str(marker.parent_record or '').strip`, `str(marker.parent_record or '').strip().upper`, `len`, `self._find_cursor_declare`, `self._assemble_declare`, `declaration.upper`, `upper_declaration.find`, `group.upper`, `re.findall`, `self._try_resolver`, `parent_group.upper`, `self._record_is_declared`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L665: `if not self.host_variable_resolver`
- L670: `if not host_group`
- L675: `if key_columns is None`
- L678: `if not key_columns`
- L687: `if not parent_record`
- L701: `if declare_index is not None`
- L727: `if parent_group and predicate_groups == {parent_group.upper()}`
- L734: `if parent_group and parent_group.upper() in predicate_groups`
- Another 4 conditions/loops exist in this source span.

### `LrfHostVariablePopulator._host_group_for_marker` - L803-L822

```python
_host_group_for_marker(self, marker: LrfExpansionMarker) -> str
```

DCLGEN host group for the cursor's table.

Observed calls (lexical order): `self._try_resolver`.

Control points:

- L815: `if not table`

### `LrfHostVariablePopulator._record_is_declared` - L824-L840

```python
_record_is_declared(self, record: str, lines: list[str]) -> bool
```

True when the converted program still declares this record.

Observed calls (lexical order): `str`, `str(record or '').strip`, `str(record or '').strip().upper`, `re.compile`, `re.escape`, `pattern.match`, `self._logical_body`, `self._logical_body(line).strip`.

Control points:

- L833: `if not target`
- L837: `for line in lines`
- L838: `if pattern.match(self._logical_body(line).strip())`

### `LrfHostVariablePopulator._predicate_columns` - L842-L878

```python
_predicate_columns(self, marker: LrfExpansionMarker, lines: list[str]) -> Optional[list[str]]
```

Column names in the cursor's own WHERE clause, in order.

Observed calls (lexical order): `self._find_cursor_declare`, `self._log`, `self._assemble_declare`, `assembled.upper`, `upper.find`, `len`, `set`, `WHERE_COLUMN_PATTERN.finditer`, `match.group`, `column.upper`, `seen.add`, `ordered.append`.

Control points:

- L853: `if declare_index is None`
- L863: `if position < 0`
- L870: `for match in WHERE_COLUMN_PATTERN.finditer(where_clause)`
- L873: `if key in _NON_COLUMN_WORDS or key in seen`

### `LrfHostVariablePopulator._find_cursor_declare` - L880-L893

```python
_find_cursor_declare(self, cursor_name: str, lines: list[str]) -> Optional[int]
```

Line index of the DECLARE statement for this cursor.

Observed calls (lexical order): `re.compile`, `CURSOR_DECLARE_TEMPLATE.format`, `re.escape`, `enumerate`, `pattern.search`, `self._logical_body`.

Control points:

- L890: `for (index, line) in enumerate(lines)`
- L891: `if pattern.search(self._logical_body(line))`

### `LrfHostVariablePopulator._assemble_declare` - L895-L912

```python
_assemble_declare(self, start_index: int, lines: list[str]) -> str
```

Join the DECLARE statement from its logical bodies.

Observed calls (lexical order): `len`, `min`, `range`, `self._logical_body`, `self._logical_body(lines[index]).strip`, `parts.append`, `body.endswith`, `body.upper`, `body.upper().endswith`, `' '.join`.

Control points:

- L904: `for index in range(start_index, limit)`
- L906: `if not body`
- L909: `if body.upper().endswith('END-EXEC') or body.endswith('.')`

### `LrfHostVariablePopulator._find_perform_open_after` - L918-L958

```python
_find_perform_open_after(self, marker: LrfExpansionMarker, lines: list[str]) -> Optional[int]
```

Index of 'PERFORM <nnn>-OPEN-<cursor>.' for this marker.

Observed calls (lexical order): `str`, `str(marker.cursor_name or '').strip`, `str(marker.cursor_name or '').strip().upper`, `enumerate`, `self._logical_body`, `self._logical_body(line).strip`, `PERFORM_OPEN_PATTERN.match`, `match.group`, `match.group('cursor').strip`, `match.group('cursor').strip().upper`, `matches.append`, `self._log`.

Control points:

- L932: `if not wanted`
- L936: `for (index, line) in enumerate(lines)`
- L938: `if not body`
- L941: `if match is None`
- L943: `if match.group('cursor').strip().upper() == wanted`
- L946: `if not matches`
- L950: `if after`

### `LrfHostVariablePopulator._inject_code` - L964-L981

```python
_inject_code(lines: list[str], injection_points: dict[int, list[str]]) -> list[str]
```

Insert generated records before each PERFORM OPEN line.

Observed calls (lexical order): `list`, `injection_points.keys`, `sorted`.

Control points:

- L975: `for index in sorted(injection_points.keys(), reverse=True)`
- L977: `if not block`

### `LrfHostVariablePopulator._try_resolver` - L987-L1002

```python
_try_resolver(self, resolver, method_names, argument: str) -> str
```

First method that answers wins. A missing name is not an error.

Observed calls (lexical order): `getattr`, `finder`, `str`, `str(value or '').strip`.

Control points:

- L989: `if resolver is None or not argument`
- L991: `for name in method_names`
- L993: `if finder is None`
- L1000: `if text`

### `LrfHostVariablePopulator._cursor_name_for_record` - L1004-L1055

```python
_cursor_name_for_record(self, record_name: str, line_index: int) -> str
```

Generated cursor name for an IDMS record, or "".

Observed calls (lexical order): `str`, `str(record_name or '').strip`, `self._log`, `self._try_resolver`.

Control points:

- L1017: `if not record`
- L1023: `if self.cursor_name_resolver is None and self.table_name_resolver is None`
- L1035: `if cursor`
- L1041: `if table`
- L1045: `if cursor`
- L1051: `if cursor`

### `LrfHostVariablePopulator._normalize_host_field` - L1057-L1079

```python
_normalize_host_field(self, field_name: str) -> str
```

COBOL form of a DB2 column name.

Observed calls (lexical order): `str`, `str(field_name or '').strip`, `getattr`, `converter`, `str(converter(text) or '').strip`, `converted.upper`, `text.upper`, `text.upper().replace`.

Control points:

- L1065: `if not text`
- L1069: `if normalizer is not None`
- L1071: `if converter is not None`
- L1074: `if converted`

### `LrfHostVariablePopulator._log` - L1085-L1107

```python
_log(self, key: str, **values) -> None
```

Append one diagnostic sentence.

Observed calls (lexical order): `str`, `str(key or '').strip`, `LRF_POPULATOR_MESSAGES.get`, `' '.join`, `sorted`, `values.items`, `self.messages.append`, `f"LRF populator: unmapped diagnostic '{name}' {detail}".rstrip`, `template.format`, `f'{template} [{detail}]'.rstrip`.

Control points:

- L1096: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
