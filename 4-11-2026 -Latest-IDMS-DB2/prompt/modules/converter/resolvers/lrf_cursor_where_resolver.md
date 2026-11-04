# `converter/resolvers/lrf_cursor_where_resolver.py`

Source: [converter/resolvers/lrf_cursor_where_resolver.py](../../../../converter/resolvers/lrf_cursor_where_resolver.py) | 466 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `cd9cd426bdf70a9b809a3bde51ccd6ee272a360a1a01506489146d91704b77e1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Resolves WHERE clauses for LRF-expanded cursors.

## Module-level bindings

`__all__` (L466)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.name_normalizer import NameNormalizer
from patterns.cursor_spec.lrf_comment_patterns import LRF_ACCESS_MARKER_PROBE, LRF_CONTINUATION_ARROW_PATTERN, LRF_CONTINUATION_RECORD_PATTERN, LRF_EXPANSION_PATTERN as _SHARED_LRF_EXPANSION_PATTERN, LRF_EXPANSION_WRAPPED_PATTERN as _SHARED_LRF_WRAPPED_PATTERN, LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN as _SHARED_LRF_WRAPPED_NO_ARROW_PATTERN
```

## Local dependency notes

- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/cursor_spec/lrf_comment_patterns.py](../../patterns/cursor_spec/lrf_comment_patterns.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](../generators/db2_infrastructure/spec_builder/cursor_spec_builder.md)
- [converter/pipeline/lrf_cursor_fix.py](../pipeline/lrf_cursor_fix.md)
- [tests/test_lrf_first_only_update_path.py](../../tests/test_lrf_first_only_update_path.md)

## Symbol contracts and control points

### `LrfCursorWhereResolver` - L58-L463

```python
class LrfCursorWhereResolver()
```

Generates WHERE conditions for LRF-expanded cursors.

Declared class/data-model fields:

```python
LRF_EXPANSION_PATTERN = _SHARED_LRF_EXPANSION_PATTERN
LRF_EXPANSION_WRAPPED_PATTERN = _SHARED_LRF_WRAPPED_PATTERN
LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN = _SHARED_LRF_WRAPPED_NO_ARROW_PATTERN
LRF_CONTINUATION_RECORD_PATTERN = LRF_CONTINUATION_RECORD_PATTERN
LRF_CONTINUATION_ARROW_PATTERN = LRF_CONTINUATION_ARROW_PATTERN
```

### `LrfCursorWhereResolver.__init__` - L69-L81

```python
__init__(self, *, relationship_resolver=None, cursor_column_resolver=None, host_variable_resolver=None, mapping_repository=None) -> None
```

### `LrfCursorWhereResolver.extract_lrf_cursors_from_cobol` - L87-L232

```python
extract_lrf_cursors_from_cobol(self, cobol_text: str) -> dict[str, dict[str, str]]
```

Extract LRF expansion markers from COBOL source.

Observed calls (lexical order): `str`, `str(cobol_text or '').splitlines`, `enumerate`, `self._logical_body`, `body.lower`, `len`, `min`, `range`, `self._parts`, `combined.lower`, `re.search`, `filter_match.group`, `filter_match.group('keyword').upper`, `re.sub`, `re.sub('\\s+', ' ', filter_match.group('conditions')).strip`, `body.strip`.
Another 31 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L107: `for (index, line) in enumerate(lines)`
- L109: `if 'extra filter:' in body.lower()`
- L111: `for next_index in range(index + 1, min(index + 4, len(lines)))`
- L113: `if indicator not in ('*', '/')`
- L116: `if 'add to the generated cursor where' in combined.lower()`
- L123: `if filter_match`
- L128: `if not body.strip()`
- L134: `if match is not None`
- Another 19 conditions/loops exist in this source span.

### `LrfCursorWhereResolver.where_conditions_for_lrf_cursor` - L238-L276

```python
where_conditions_for_lrf_cursor(self, record_name: str, lrf_cursor_info: dict[str, str]) -> list[str]
```

WHERE predicates for an LRF-expanded cursor.

Observed calls (lexical order): `lrf_cursor_info.get`, `self.relationship_resolver.resolve_for_child_record`, `getattr`, `str`, `where_conditions.append`, `self.extra_filter_conditions_for_lrf_cursor`, `where_conditions.extend`.

Control points:

- L249: `if not lrf_cursor_info.get('is_lrf_expanded')`
- L252: `if self.relationship_resolver is None`
- L258: `if not relationship or not getattr(relationship, 'conditions', None)`
- L262: `for condition in relationship.conditions`
- L267: `if child_col and parent_host_ref`
- L273: `if extra_conditions is None`

### `LrfCursorWhereResolver.extra_filter_conditions_for_lrf_cursor` - L278-L292

```python
extra_filter_conditions_for_lrf_cursor(self, record_name: str, lrf_cursor_info: dict[str, str]) -> list[str] | None
```

Resolve only source-proven extra predicates from an LRF marker.

Observed calls (lexical order): `lrf_cursor_info.get`, `str`, `self._mapped_extra_filter_conditions`, `self.messages.append`.

Control points:

- L283: `if not extra_text`
- L286: `if extra_conditions is None`

### `LrfCursorWhereResolver._mapped_extra_filter_conditions` - L294-L354

```python
_mapped_extra_filter_conditions(self, record_name: str, text: str) -> list[str] | None
```

Map source LRF equality filters to target DB2 columns safely.

Observed calls (lexical order): `getattr`, `callable`, `rows_for_record`, `re.split`, `text.strip`, `re.fullmatch`, `match.group`, `match.group('field').upper`, `re.sub`, `set`, `str`, `str(getattr(row, 'cobol_zone', '') or '').strip`, `str(getattr(row, 'reference_field_name_copybook', '') or '').strip`, `str(getattr(row, 'new_db2_field_name', '') or getattr(row, 'cross_application_db2_field_name', '') or '').s...`, `any`, `normalized_source_name`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L298: `if self.mapping_repository is None`
- L301: `if not callable(rows_for_record)`
- L312: `for part in parts`
- L318: `if not match`
- L322: `for row in rows`
- L332: `if not target_column`
- L342: `if any((source_name and (normalized_source_name(source_name) == source_field or normalized_source_name(source_name).startswith(source_field)) for source_name in row_sources))`
- L351: `if len(candidates) != 1`

### `LrfCursorWhereResolver.augment_select_for_lrf_keys` - L356-L390

```python
augment_select_for_lrf_keys(self, cursor_spec: dict[str, object], lrf_cursor_info: dict[str, str]) -> None
```

Ensure WHERE-referenced key columns appear in the SELECT.

Observed calls (lexical order): `lrf_cursor_info.get`, `cursor_spec.get`, `list`, `NameNormalizer.normalize`, `str`, `text.split`, `text.split(':', 1)[1].strip`, `host_part.split`, `host_field.strip`, `host_field.strip().replace`, `select_columns.append`, `existing.add`.

Control points:

- L366: `if not lrf_cursor_info.get('is_lrf_expanded')`
- L373: `for condition in where_conditions`
- L375: `if ':' not in text or '.' not in text`
- L379: `if '.' not in host_part`
- L386: `if parent_col and parent_col not in existing`

### `LrfCursorWhereResolver.resolve_order_by_direction_for_lrf` - L392-L420

```python
resolve_order_by_direction_for_lrf(self, record_name: str, lrf_cursor_info: dict[str, str], order_by_columns: list[str]) -> list[str]
```

Correct ORDER BY direction from the LRF access mode.

Observed calls (lexical order): `lrf_cursor_info.get`, `str`, `str(lrf_cursor_info.get('mode', 'FIRST')).upper`, `str(expr).strip`, `expr_str.upper`, `corrected.append`, `expr_str.replace`, `expr_str.replace('DESC', 'ASC').strip`.

Control points:

- L399: `if not lrf_cursor_info.get('is_lrf_expanded')`
- L401: `if not order_by_columns`
- L407: `for expr in order_by_columns`
- L413: `if mode == 'NEXT' and (not has_asc) and (not has_desc)`
- L415: `if mode == 'FIRST' and has_desc and (not has_asc)`

### `LrfCursorWhereResolver._parts` - L427-L431

```python
_parts(line: str) -> tuple[str, str, str]
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[7:72].strip`, `text.strip`.

Control points:

- L429: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `LrfCursorWhereResolver._logical_body` - L434-L439

```python
_logical_body(line: str) -> str
```

Columns 8-72 of a fixed-format record, indicator removed.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L437: `if len(text) >= 72 and text[:6].strip().isdigit()`

### `LrfCursorWhereResolver._continuation_arrow_record` - L441-L451

```python
_continuation_arrow_record(self, lines: list[str], index: int) -> str
```

Read the target record from a wrapped marker whose arrow is on line 2.

Observed calls (lexical order): `len`, `min`, `range`, `self._logical_body`, `self._logical_body(lines[offset]).strip`, `self.LRF_CONTINUATION_ARROW_PATTERN.match`, `match.group`.

Control points:

- L443: `for offset in range(index + 1, min(index + 3, len(lines)))`
- L445: `if not body`
- L448: `if match`

### `LrfCursorWhereResolver._continuation_record` - L453-L463

```python
_continuation_record(self, lines: list[str], index: int) -> str
```

Record name opening the body after a wrapped marker.

Observed calls (lexical order): `len`, `min`, `range`, `self._logical_body`, `self._logical_body(lines[offset]).strip`, `self.LRF_CONTINUATION_RECORD_PATTERN.match`, `match.group`.

Control points:

- L455: `for offset in range(index + 1, min(index + 3, len(lines)))`
- L457: `if not body`
- L460: `if match`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
