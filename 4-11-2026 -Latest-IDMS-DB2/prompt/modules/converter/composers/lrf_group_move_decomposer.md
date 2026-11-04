# `converter/composers/lrf_group_move_decomposer.py`

Source: [converter/composers/lrf_group_move_decomposer.py](../../../../converter/composers/lrf_group_move_decomposer.py) | 889 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `4091d105f838508b9a47a3b710ad2c91d522a6b7202ff793435eea69c04d55a8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Safely decompose LRF 1:N group references into DB2 host-field operations.

## Module-level bindings

`__all__` (L889)

## Import declarations

```python
from __future__ import annotations
import re
from converter.generators.initialization.line_geometry import LineGeometry
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.name_normalizer import NameNormalizer
from rules.move_alignment_rules import STATEMENT_OPENERS
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../generators/initialization/line_geometry.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/move_alignment_rules.py](../../rules/move_alignment_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_generic_unused_copybook_and_group_move.py](../../tests/test_generic_unused_copybook_and_group_move.md)
- [tests/test_lrf_move_statement_boundaries.py](../../tests/test_lrf_move_statement_boundaries.md)

## Symbol contracts and control points

### `LrfGroupMoveDecomposer` - L18-L886

```python
class LrfGroupMoveDecomposer()
```

Declared class/data-model fields:

```python
_FIELD_LEVEL = re.compile('^\\s*(?P<level>\\d{1,2})\\s+(?P<name>[A-Z0-9-]+)', re.I)
_MOVE_GROUP_TO_TARGET = re.compile('^MOVE\\s+(?P<field>[A-Z][A-Z0-9-]*)\\s+OF\\s+(?P<record>[A-Z][A-Z0-9-]*)\\s+TO\\s+(?P<target>[A-Z][A-Z0-9-]*)(?:\\s+OF\\s+(?P<target_record>[A-Z][A-Z0-9-]*))?\\s*\\.?$', re.I)
_MOVE_TO_GROUP = re.compile('^MOVE\\s+(?P<source>[A-Z][A-Z0-9-]*|SPACES|SPACE|ZEROES|ZEROS|ZERO)\\s+TO\\s+(?P<field>[A-Z][A-Z0-9-]*)\\s+OF\\s+(?P<record>[A-Z][A-Z0-9-]*)\\s*\\.?$', re.I)
_MOVE_SPACES_TO_RECORD = re.compile('^MOVE\\s+(?:SPACES|SPACE)\\s+TO\\s+(?P<records>[A-Z][A-Z0-9-]*(?:\\s+[A-Z][A-Z0-9-]*)*)\\s*\\.?$', re.I)
_MOVE_SIMPLE_SOURCE_MULTI_TARGET = re.compile("^MOVE\\s+(?P<source>'(?:''|[^'])*'|[A-Z][A-Z0-9-]*|[0-9]+)\\s+TO\\s+(?P<targets>.+?)\\s*\\.?$", re.I)
_MOVE_TARGET = re.compile('(?P<field>[A-Z][A-Z0-9-]*)(?:\\s+OF\\s+(?P<record>[A-Z][A-Z0-9-]*))?', re.I)
_DISPLAY_PREFIX = re.compile('^DISPLAY\\b', re.I)
_PICTURE_WIDTH = re.compile('\\b(?:PIC|PICTURE)\\s+(.+)$', re.I)
_TYPE_WIDTH = re.compile('\\b(?:CHAR|CHARACTER|DECIMAL|NUMERIC|INTEGER)\\s*\\(\\s*(\\d+)', re.I)
```

### `LrfGroupMoveDecomposer.__init__` - L47-L58

```python
__init__(self, *, mapping_repository, dclgen_repository, copybook_repository, table_name_resolver, host_variable_resolver)
```

Observed calls (lexical order): `LineGeometry`, `FixedFormatLineService`, `set`.

### `LrfGroupMoveDecomposer.apply` - L60-L486

```python
apply(self, text: str, parent_records: set[str] | None=None) -> str
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `self.geometry.split`, `self._child_records_from_comments`, `enumerate`, `self._collect_move`, `self._MOVE_GROUP_TO_TARGET.match`, `explicit.group`, `self._explicit_target_groups.add`, `len`, `self.geometry.body`, `body.upper`, `body.upper().strip`, `self.geometry.is_comment`, `output.append`, `candidate.group`.
Another 76 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L68: `for (candidate_index, _candidate_line) in enumerate(lines)`
- L72: `if not candidate_statement`
- L75: `if not explicit`
- L79: `if explicit_record in lrf_records`
- L87: `while index < len(lines)`
- L91: `if not body or self.geometry.is_comment(line)`
- L97: `if last_assembled is not None`
- L99: `if not candidate or (NameNormalizer.normalize(candidate.group('record')), NameNormalizer.normalize(candidate.group('field'))) != last_assembled[:2]`
- Another 60 conditions/loops exist in this source span.

### `LrfGroupMoveDecomposer._render_generated_statement` - L488-L497

```python
_render_generated_statement(self, source_line: str, statement: str) -> list[str]
```

Emit generated statements in fixed format with correct continuation indicators.

Observed calls (lexical order): `self.fixed.is_fixed_line`, `len`, `self.geometry.indent_of`, `self.fixed.emit`.

Control points:

- L490: `if self.fixed.is_fixed_line(source_line)`

### `LrfGroupMoveDecomposer.filter_resolved_field_diagnostics` - L499-L513

```python
filter_resolved_field_diagnostics(self, messages: list[str]) -> list[str]
```

Drop earlier 1:N warnings for group references this pass proved and expanded.

Observed calls (lexical order): `re.compile`, `pattern.search`, `str`, `NameNormalizer.normalize`, `match.group`, `output.append`.

Control points:

- L503: `for message in messages`
- L505: `if match`
- L510: `if pair in self.resolved_group_references`

### `LrfGroupMoveDecomposer._numeric_picture_digits` - L516-L521

```python
_numeric_picture_digits(picture: str) -> int
```

Observed calls (lexical order): `str`, `str(picture or '').upper`, `str(picture or '').upper().replace`, `re.fullmatch`, `int`, `m.group`, `re.sub`, `expanded.count`.

Control points:

- L518: `if not text or not re.fullmatch('[S9VP()+\\-.,0-9]+', text) or '9' not in text`

### `LrfGroupMoveDecomposer._narrow_numeric_group_source` - L523-L567

```python
_narrow_numeric_group_source(self, statement: str) -> str
```

Narrow a group source only when its GROUP-R numeric view is proven.

Observed calls (lexical order): `re.match`, `str`, `str(statement or '').strip`, `NameNormalizer.normalize`, `match.group`, `self.copybooks.find`, `getattr`, `str(getattr(source_field, 'picture', '') or '').strip`, `self.copybooks.parent_for`, `self._numeric_picture_digits`, `target_group.startswith`, `next`, `self.dclgen.all`, `str(getattr(target_column, 'db2_type', '') or '').upper`, `str(getattr(target_column, 'db2_type', '') or '').upper().strip`, `str(getattr(target_column, 'cobol_picture', '') or '').upper`.
Another 9 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L530: `if not match`
- L536: `if source_field is None or str(getattr(source_field, 'picture', '') or '').strip()`
- L539: `if child is None`
- L542: `if parent is None or NameNormalizer.normalize(parent.name) != source`
- L545: `if not source_digits`
- L554: `if target_column is None`
- L565: `if not numeric_target or target_digits != source_digits`

### `LrfGroupMoveDecomposer._collect_move` - L569-L588

```python
_collect_move(self, lines: list[str], start: int) -> tuple[str, int]
```

Observed calls (lexical order): `self.geometry.body`, `self.geometry.body(lines[start]).strip`, `re.match`, `len`, `self.geometry.body(next_line).strip`, `self.geometry.is_comment`, `next_body.split`, `next_body.split(maxsplit=1)[0].rstrip`, `next_body.split(maxsplit=1)[0].rstrip('.').upper`, `parts.append`, `' '.join`.

Control points:

- L571: `if not re.match('^MOVE\\b', body, re.I)`
- L575: `while '.' not in parts[-1] and start + consumed < len(lines) and (consumed < 4)`
- L578: `if not next_body or self.geometry.is_comment(next_line)`
- L584: `if next_body.split(maxsplit=1)[0].rstrip('.').upper() in STATEMENT_OPENERS`

### `LrfGroupMoveDecomposer._infer_target_record` - L590-L605

```python
_infer_target_record(self, field: str, lrf_records: set[str]) -> str
```

Infer an omitted target qualifier only when one LRF record owns the group.

Observed calls (lexical order): `NameNormalizer.normalize`, `sorted`, `self._group_components`, `len`, `candidates.append`.

Control points:

- L594: `for record in sorted(lrf_records)`
- L600: `if (record, normalized_field) not in self._explicit_target_groups`
- L603: `if len(components) > 1`

### `LrfGroupMoveDecomposer._helper_for_split` - L607-L640

```python
_helper_for_split(self, record: str, field: str, source_width: int, components: list[dict]) -> dict[str, object]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `len`, `range`, `zip`, `int`, `component.get`, `str`, `str(component.get('data_type', '') or '').upper`, `any`, `declarations.append`.

Control points:

- L615: `if key in self._generated_helpers`
- L628: `for (name, component) in zip(component_names, components)`

### `LrfGroupMoveDecomposer._insert_helper_declarations` - L642-L658

```python
_insert_helper_declarations(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `next`, `enumerate`, `re.search`, `self.geometry.body`, `self.messages.append`, `self._generated_helpers.values`, `declarations.extend`, `self.geometry.join`.

Control points:

- L643: `if not self._generated_helpers`
- L651: `if procedure_index is None`
- L655: `for helper in self._generated_helpers.values()`

### `LrfGroupMoveDecomposer._group_components` - L660-L731

```python
_group_components(self, record: str, group_field: str) -> tuple[list[dict], str]
```

Observed calls (lexical order): `self.mapping.rows_for_record`, `getattr`, `str`, `str(getattr(row, 'cobol_zone', '') or '').strip`, `self._FIELD_LEVEL.match`, `NameNormalizer.normalize`, `match.group`, `self.tables.resolve_table`, `nodes.append`, `int`, `bool`, `re.search`, `enumerate`, `next`, `self.hosts.host_for_column`, `self._row_width`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L663: `for row in rows`
- L666: `if not match`
- L693: `if target_index < 0`
- L696: `if group_node['column']`
- L705: `while index < len(nodes) and nodes[index]['level'] > group_level`
- L707: `if node['redefines'] or node['filler']`
- L710: `if node['column']`
- L714: `if host and width`
- Another 2 conditions/loops exist in this source span.

### `LrfGroupMoveDecomposer._skip_subtree` - L734-L739

```python
_skip_subtree(nodes: list[dict], index: int) -> int
```

Observed calls (lexical order): `len`.

Control points:

- L737: `while index < len(nodes) and nodes[index]['level'] > level`

### `LrfGroupMoveDecomposer._row_width` - L741-L751

```python
_row_width(self, row) -> int
```

Observed calls (lexical order): `getattr`, `str`, `str(getattr(row, 'length_of_field_bytes', '') or '').strip`, `raw.isdigit`, `int`, `self._TYPE_WIDTH.search`, `match.group`.

Control points:

- L743: `if raw.isdigit()`

### `LrfGroupMoveDecomposer._copybook_width` - L753-L764

```python
_copybook_width(self, field: str) -> int
```

Observed calls (lexical order): `self.copybooks.effective_picture_for`, `int`, `self.copybooks.group_width_for`, `picture.upper`, `re.sub`, `re.findall`, `m.group`, `sum`.

Control points:

- L755: `if not picture`
- L759: `for token in re.findall('(?:S?9|X|A|N|Z|\\*|\\$)(?:\\((\\d+)\\))?', picture)`

### `LrfGroupMoveDecomposer._width_matched_children` - L766-L787

```python
_width_matched_children(self, target: str, widths: list[int]) -> list[str]
```

Use source-defined COBOL receiving items when boundaries agree.

Observed calls (lexical order): `hasattr`, `self.copybooks.direct_children_for`, `len`, `zip`, `getattr`, `str`, `str(getattr(child, 'occurs', '') or '').strip`, `str(getattr(child, 'redefines', '') or '').strip`, `self._copybook_width`, `NameNormalizer.to_cobol`, `result.append`.

Control points:

- L773: `if not widths or not hasattr(self.copybooks, 'direct_children_for')`
- L776: `if len(children) != len(widths)`
- L779: `for (child, width) in zip(children, widths)`
- L780: `if str(getattr(child, 'occurs', '') or '').strip()`
- L782: `if str(getattr(child, 'redefines', '') or '').strip()`
- L784: `if self._copybook_width(child.name) != width`

### `LrfGroupMoveDecomposer._reference_modification_base` - L789-L804

```python
_reference_modification_base(self, target: str) -> str
```

Observed calls (lexical order): `self.copybooks.find`, `getattr`, `str`, `str(getattr(field, 'picture', '') or '').strip`, `self.copybooks.parent_for`, `str(getattr(parent, 'picture', '') or '').strip`, `len`, `self.copybooks.direct_children_for`, `NameNormalizer.normalize`, `NameNormalizer.to_cobol`.

Control points:

- L791: `if field is None`
- L793: `if not str(getattr(field, 'picture', '') or '').strip()`
- L796: `if parent and (not str(getattr(parent, 'picture', '') or '').strip()) and (len(self.copybooks.direct_children_for(parent.name)) == 1) and (NameNormalizer.normalize(self.copybooks.d...`

### `LrfGroupMoveDecomposer._has_generated_key_split` - L806-L813

```python
_has_generated_key_split(self, lines: list[str], record: str, source: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `'\n'.join`, `self.geometry.body`, `self.geometry.body(line).upper`, `joined.find`, `marker.upper`, `bool`, `re.escape`, `re.search`, `source.upper`.

Control points:

- L810: `if marker_index < 0`

### `LrfGroupMoveDecomposer._all_components_assigned_before_select` - L815-L825

```python
_all_components_assigned_before_select(self, lines: list[str], record: str, components: list[dict]) -> bool
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `'\n'.join`, `self.geometry.body`, `self.geometry.body(line).upper`, `joined.find`, `marker.upper`, `item['dcl_group'].upper`, `item['host'].upper`, `re.escape`, `re.search`.

Control points:

- L819: `if marker_index < 0`
- L822: `for item in components`
- L823: `if not re.search(f'\\bTO\\s+{re.escape(item['host'].upper())}\\s+OF\\s+{re.escape(item['dcl_group'].upper())}\\b', before, re.I)`

### `LrfGroupMoveDecomposer._group_references_in_display` - L827-L834

```python
_group_references_in_display(self, body: str, lrf_records: set[str]) -> list[tuple[str, str]]
```

Observed calls (lexical order): `re.finditer`, `NameNormalizer.normalize`, `match.group`, `output.append`.

Control points:

- L829: `for match in re.finditer('\\b(?P<field>[A-Z][A-Z0-9-]*)\\s+OF\\s+(?P<record>[A-Z][A-Z0-9-]*)\\b', body, re.I)`
- L832: `if record in lrf_records`

### `LrfGroupMoveDecomposer._child_records_from_comments` - L836-L846

```python
_child_records_from_comments(self, lines: list[str]) -> set[str]
```

Observed calls (lexical order): `set`, `re.compile`, `self.geometry.is_comment`, `pattern.search`, `self.geometry.body`, `NameNormalizer.normalize`, `match.group`, `output.add`.

Control points:

- L839: `for line in lines`
- L840: `if not self.geometry.is_comment(line)`
- L843: `if match`

### `LrfGroupMoveDecomposer._residual_lrf_access_tokens` - L848-L864

```python
_residual_lrf_access_tokens(self, text: str) -> set[str]
```

Observed calls (lexical order): `set`, `re.compile`, `text.splitlines`, `self.geometry.is_comment`, `self.geometry.body`, `patterns.items`, `pattern.search`, `residual.add`.

Control points:

- L857: `for line in text.splitlines()`
- L858: `if self.geometry.is_comment(line)`
- L861: `for (label, pattern) in patterns.items()`
- L862: `if pattern.search(body)`

### `LrfGroupMoveDecomposer._residual_lrf_record_references` - L866-L886

```python
_residual_lrf_record_references(self, text: str, records: set[str]) -> set[str]
```

Observed calls (lexical order): `set`, `text.splitlines`, `self.geometry.is_comment`, `self.geometry.body`, `re.finditer`, `NameNormalizer.normalize`, `match.group`, `NameNormalizer.to_cobol`, `residual.add`, `re.match`, `whole_record.group`.

Control points:

- L868: `for line in text.splitlines()`
- L869: `if self.geometry.is_comment(line)`
- L872: `for match in re.finditer('\\b(?:OF|IN)\\s+(?P<record>[A-Z][A-Z0-9-]*)\\b', body, re.I)`
- L874: `if record in records`
- L882: `if whole_record`
- L884: `if record in records`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
