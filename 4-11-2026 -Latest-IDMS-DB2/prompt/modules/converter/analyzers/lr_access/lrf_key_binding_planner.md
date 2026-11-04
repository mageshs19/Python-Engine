# `converter/analyzers/lr_access/lrf_key_binding_planner.py`

Source: [converter/analyzers/lr_access/lrf_key_binding_planner.py](../../../../../converter/analyzers/lr_access/lrf_key_binding_planner.py) | 204 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `61346841cf1dc3a86598ea195242a876e7e2865e34ece0e27d292fb765191ba1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Plan safe DB2 host-variable bindings for LRF keyed parent traversals.

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from converter.generators.initialization.line_geometry import LineGeometry
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../../generators/initialization/line_geometry.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline_steps.py](../../pipeline/conversion/conversion_pipeline_steps.md)
- [tests/test_lrf_key_binding_planner.py](../../../tests/test_lrf_key_binding_planner.md)

## Symbol contracts and control points

### `LrfKeyBindingPlan` - L18-L25

```python
class LrfKeyBindingPlan()
```

Declared class/data-model fields:

```python
parent_record: str
parent_input_moves: list[str] = field(default_factory=list)
child_record: str = ''
child_dcl_group: str = ''
child_key_moves: list[str] = field(default_factory=list)
diagnostics: list[str] = field(default_factory=list)
safe: bool = True
```

### `LrfKeyBindingPlanner` - L28-L204

```python
class LrfKeyBindingPlanner()
```

Build source-to-key and parent-to-child key bindings from metadata.

Declared class/data-model fields:

```python
_FIELD_LEVEL = re.compile('^\\s*(?P<level>\\d{1,2})\\s+(?P<name>[A-Z0-9-]+)', re.I)
_PIC_WIDTH = re.compile('\\bPIC(?:TURE)?\\s+(?:X|9)\\s*\\(\\s*(\\d+)\\s*\\)', re.I)
_MOVE_TO_GROUP = re.compile('\\bMOVE\\s+(?P<src>[A-Z][A-Z0-9-]*)(?:\\s+OF\\s+[A-Z][A-Z0-9-]*)?\\s+TO\\s+(?P<group>[A-Z][A-Z0-9-]*)\\s+OF\\s+(?P<record>[A-Z][A-Z0-9-]*)\\b', re.I)
_DB2_WIDTH = re.compile('\\b(?:CHAR|CHARACTER|DECIMAL|NUMERIC|INTEGER)\\s*\\(\\s*(\\d+)', re.I)
```

### `LrfKeyBindingPlanner.__init__` - L41-L47

```python
__init__(self, mapping_repository, dclgen_repository, table_name_resolver, host_variable_resolver, copybook_repository=None)
```

Observed calls (lexical order): `LineGeometry`.

### `LrfKeyBindingPlanner.plan_parent_input` - L49-L140

```python
plan_parent_input(self, source_text: str, parent_record: str) -> tuple[list[str], list[str], bool]
```

Return moves that split a mapped composite CALC group into DCLGEN keys.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping.rows_for_record`, `getattr`, `self._field_identity`, `group_rows.append`, `self._logical_source`, `list`, `self._MOVE_TO_GROUP.finditer`, `re.escape`, `re.search`, `access_match.start`, `len`, `match.start`, `m.group`, `candidate.group`, `str`.
Another 17 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L59: `for row in rows`
- L61: `if not field`
- L66: `if 'CALC' in key_kind and 'GROUP' in pic`
- L69: `if not group_rows`
- L83: `for (level, group_name, group_row) in group_rows`
- L86: `if not found`
- L97: `if candidate_width and candidate_children and all((w > 0 for w in candidate_widths)) and (sum(candidate_widths) == candidate_width)`
- L100: `if not candidates`
- Another 5 conditions/loops exist in this source span.

### `LrfKeyBindingPlanner._direct_key_children` - L142-L157

```python
_direct_key_children(self, rows, parent_level: int) -> list[object]
```

Observed calls (lexical order): `getattr`, `self._field_identity`, `NameNormalizer.normalize`, `output.append`.

Control points:

- L144: `for row in rows`
- L146: `if not field or field[0] != parent_level + 1`
- L152: `if 'FOREIGN' in text or not ('PRIMARY_KEY' in text or ('PRIMARY' in text and 'KEY' in text))`
- L155: `if column`

### `LrfKeyBindingPlanner._mapped_width` - L159-L165

```python
_mapped_width(self, row) -> int
```

Observed calls (lexical order): `getattr`, `str`, `str(getattr(row, 'length_of_field_bytes', '') or '').strip`, `direct.isdigit`, `int`, `self._DB2_WIDTH.search`, `match.group`.

Control points:

- L161: `if direct.isdigit()`

### `LrfKeyBindingPlanner._declared_width` - L167-L186

```python
_declared_width(self, logical: str, source: str) -> int
```

Observed calls (lexical order): `logical.splitlines`, `re.escape`, `re.search`, `self._PIC_WIDTH.search`, `int`, `match.group`, `self.copybooks.effective_picture_for`, `str`, `str(self.copybooks.effective_picture_for(source) or '').upper`.

Control points:

- L173: `for line in logical.splitlines()`
- L174: `if re.search(f'\\b{re.escape(source)}\\b', line, re.I) and re.search('\\bPIC(?:TURE)?\\b', line, re.I)`
- L176: `if match`
- L178: `if self.copybooks is not None`
- L184: `if match`

### `LrfKeyBindingPlanner._field_identity` - L188-L193

```python
_field_identity(self, raw: str) -> tuple[int, str] | None
```

Observed calls (lexical order): `' '.join`, `str`, `str(raw or '').split`, `self._FIELD_LEVEL.match`, `NameNormalizer.normalize`, `int`, `match.group`.

Control points:

- L191: `if not match`

### `LrfKeyBindingPlanner._logical_source` - L195-L204

```python
_logical_source(self, source_text: str) -> str
```

Observed calls (lexical order): `str`, `str(source_text or '').splitlines`, `self.geometry.body`, `self.geometry.is_comment`, `body.upper`, `lines.append`, `'\n'.join`.

Control points:

- L197: `for raw in str(source_text or '').splitlines()`
- L199: `if not body or self.geometry.is_comment(raw)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
