# `converter/composers/bounded_lrf_singleton_rewriter.py`

Source: [converter/composers/bounded_lrf_singleton_rewriter.py](../../../../converter/composers/bounded_lrf_singleton_rewriter.py) | 1040 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `86566cf1c445eb01ce0c5d78e59bc9a57e63cd4242b09ad743bc07e9807c12e9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Safely rewrite proven LRF cursor access to a singleton DB2 SELECT.

## Module-level bindings

`__all__` (L1040)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_bounded_lrf_singleton_rewriter.py](../../tests/test_bounded_lrf_singleton_rewriter.md)
- [tests/test_lrf_cursor_release_gate.py](../../tests/test_lrf_cursor_release_gate.md)
- [tests/test_lrf_first_only_update_path.py](../../tests/test_lrf_first_only_update_path.md)
- [tests/test_lrf_source_access_comment_safety.py](../../tests/test_lrf_source_access_comment_safety.md)

## Symbol contracts and control points

### `RewriteResult` - L16-L19

```python
class RewriteResult()
```

Declared class/data-model fields:

```python
text: str
changed: bool = False
diagnostic: str = ''
```

### `BoundedLrfSingletonRewriter` - L22-L1037

```python
class BoundedLrfSingletonRewriter()
```

Declared class/data-model fields:

```python
_DECLARE = re.compile('\\bDECLARE\\s+(?P<cursor>[A-Z0-9-]+)\\s+CURSOR\\b', re.I)
_PERFORM_UNTIL = re.compile('\\bPERFORM\\s+UNTIL\\b', re.I)
_END_PERFORM = re.compile('\\bEND-PERFORM\\b', re.I)
_PREDICATE = re.compile('\\b(?P<field>[A-Z][A-Z0-9-]*)\\s+(?:OF\\s+[A-Z][A-Z0-9-]*)?\\s*=\\s*(?P<literal>\'[^\']*\'|\\"[^\\"]*\\"|\\d+)', re.I)
_HOST = re.compile(':(?P<host>[A-Z][A-Z0-9-]*(?:\\.[A-Z][A-Z0-9-]*)?)', re.I)
```

### `BoundedLrfSingletonRewriter._parts` - L33-L36

```python
_parts(line: str) -> tuple[str, str, str]
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].rstrip`, `line.rstrip`.

Control points:

- L34: `if len(line) >= 7 and line[:6].isdigit()`

### `BoundedLrfSingletonRewriter._body` - L39-L40

```python
_body(cls, line: str) -> str
```

Observed calls (lexical order): `cls._parts`, `cls._parts(line)[2].strip`.

### `BoundedLrfSingletonRewriter._fixed` - L43-L46

```python
_fixed(body: str, indicator: str=' ') -> str
```

Observed calls (lexical order): `len`, `ValueError`.

Control points:

- L44: `if len(body) > 65`

Explicit raises: `ValueError(f'fixed-format body exceeds 65 columns: {body}')`.

### `BoundedLrfSingletonRewriter._sql_identifier` - L49-L50

```python
_sql_identifier(field: str) -> str
```

Observed calls (lexical order): `field.strip`, `field.strip().upper`, `re.sub`.

### `BoundedLrfSingletonRewriter.rewrite` - L52-L92

```python
rewrite(self, cobol_text: str, *, original_idms_text: str='') -> RewriteResult
```

Rewrite every independently provable bounded cursor in the program.

Observed calls (lexical order): `str`, `range`, `self._rewrite_one`, `diagnostics.append`, `RewriteResult`, `len`, `' | '.join`.

Control points:

- L64: `for _ in range(32)`
- L66: `if not result.changed`
- L70: `if result.diagnostic and (not (changed and 'No generated WITH HOLD cursor declaration found' in result.diagnostic))`
- L75: `if result.diagnostic`
- L77: `if result.text == current`
- L85: `if changed`

### `BoundedLrfSingletonRewriter._rewrite_one` - L94-L380

```python
_rewrite_one(self, cobol_text: str, *, original_idms_text: str='') -> RewriteResult
```

Observed calls (lexical order): `str`, `original.splitlines`, `self._body`, `'\n'.join`, `'\n'.join(bodies).upper`, `self._source_proves_first_only`, `str(original_idms_text or '').upper`, `self._source_has_next_for_lrf_first`, `RewriteResult`, `enumerate`, `self._DECLARE.search`, `body.upper`, `declarations.append`, `match.group`, `match.group('cursor').upper`, `self._find_end_exec`.
Another 40 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L110: `if not lrf_cursor_provenance`
- L120: `for (idx, body) in enumerate(bodies)`
- L122: `if match and ('WITH HOLD' in body.upper() or lrf_cursor_provenance)`
- L124: `if not declarations`
- L131: `for (candidate_start, candidate_cursor) in declarations`
- L133: `if candidate_end is None`
- L137: `if not re.search('\\bORDER\\s+BY\\b', candidate_sql, re.I) or not re.search('\\bWHERE\\b', candidate_sql, re.I)`
- L145: `if missing_literals`
- Another 32 conditions/loops exist in this source span.

### `BoundedLrfSingletonRewriter._select_columns` - L383-L391

```python
_select_columns(cls, cursor_sql: str) -> list[str]
```

Parse the generated simple-column SELECT projection or fail closed.

Observed calls (lexical order): `re.search`, `match.group`, `match.group(1).split`, `part.strip`, `part.strip().lstrip`, `part.strip().lstrip(',').strip`, `any`, `re.fullmatch`.

Control points:

- L386: `if not match`
- L389: `if not columns or any((not re.fullmatch('[A-Z][A-Z0-9_]*', column, re.I) for column in columns))`

### `BoundedLrfSingletonRewriter._update_where_projection` - L394-L452

```python
_update_where_projection(cls, selected_columns: list[str], hosts: list[str], bodies: list[str], *, after: int, excluded_spans: tuple[tuple[int | None, int | None], ...], source_lines: list[str] | None=None) -> tuple[list[str], list[str]] | None
```

Project only cursor columns used by a following UPDATE's WHERE.

Observed calls (lexical order): `len`, `set`, `excluded.update`, `range`, `re.search`, `cls._find_end_exec`, `' '.join`, `cls._HOST.finditer`, `m.group`, `where_match.group`, `host.upper`, `zip`, `any`, `value.upper`, `ordered_columns.append`, `ordered_hosts.append`.

Control points:

- L411: `if len(selected_columns) != len(hosts) or not selected_columns`
- L414: `for (start, end) in excluded_spans`
- L415: `if start is None or end is None`
- L419: `for start in range(after + 1, len(bodies))`
- L420: `if start in excluded or not re.search('\\bEXEC\\s+SQL\\b', bodies[start], re.I)`
- L427: `if end is None`
- L432: `if not re.search('\\bUPDATE\\s+[A-Z][A-Z0-9_]*\\b', statement, re.I)`
- L436: `if not where_match`
- Another 4 conditions/loops exist in this source span.

### `BoundedLrfSingletonRewriter._business_projection` - L455-L539

```python
_business_projection(cls, selected_columns: list[str], hosts: list[str], bodies: list[str], *, after: int, excluded_spans: tuple[tuple[int | None, int | None], ...]) -> tuple[list[str], list[str]] | None
```

Return SELECT/FETCH pairs actually consumed by downstream logic.

Observed calls (lexical order): `len`, `set`, `excluded.update`, `range`, `enumerate`, `host.split`, `host.split('.', 1)[1].upper`, `host.split('.', 1)[0].upper`, `body.lstrip`, `body.lstrip().startswith`, `re.finditer`, `ref.group`, `ref.group('field').upper`, `ref.group('group').upper`, `body[:ref.start()].upper`, `body[:ref.start()].upper().rstrip`.
Another 13 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L471: `if len(selected_columns) != len(hosts) or not selected_columns`
- L475: `for (start, end) in excluded_spans`
- L476: `if start is None or end is None`
- L489: `for (line_index, body) in tail`
- L490: `if body.lstrip().startswith('*')`
- L492: `for ref in re.finditer('\\b(?P<field>[A-Z][A-Z0-9-]*)\\s+OF\\s+(?P<group>DCL[A-Z0-9-]*)\\b', body, re.I)`
- L499: `if group not in host_groups`
- L504: `if re.search('\\bTO\\s*$', before)`
- Another 9 conditions/loops exist in this source span.

### `BoundedLrfSingletonRewriter._count_calls` - L542-L544

```python
_count_calls(bodies: list[str], paragraph: str) -> int
```

Observed calls (lexical order): `re.compile`, `re.escape`, `bool`, `pattern.search`, `sum`.

### `BoundedLrfSingletonRewriter._sql_terminator_on_line` - L547-L593

```python
_sql_terminator_on_line(body: str, in_block_comment: bool=False, quote: str | None=None) -> tuple[bool, bool, str | None]
```

Return whether END-EXEC occurs outside SQL/COBOL lexical comments.

Observed calls (lexical order): `len`, `body.find`, `body.startswith`, `re.match`, `body[index - 1].isalnum`.

Control points:

- L559: `while index < len(body)`
- L560: `if in_block_comment`
- L562: `if close < 0`
- L569: `if quote`
- L570: `if char == quote`
- L572: `if index + 1 < len(body) and body[index + 1] == quote`
- L579: `if char in {"'", '"'}`
- L583: `if body.startswith('--', index) or body.startswith('*>', index)`
- Another 2 conditions/loops exist in this source span.

### `BoundedLrfSingletonRewriter._find_end_exec` - L596-L646

```python
_find_end_exec(cls, bodies: list[str], start: int, source_lines: list[str] | None=None) -> int | None
```

Find the matching SQL terminator without an arbitrary line limit.

Observed calls (lexical order): `len`, `range`, `cls._parts`, `cls._sql_terminator_on_line`, `re.search`, `source_body.lstrip`, `re.fullmatch`, `re.match`.

Control points:

- L612: `for idx in range(start, len(bodies))`
- L613: `if source_lines is not None and idx < len(source_lines)`
- L615: `if indicator in ('*', '/', 'D', 'd')`
- L621: `if is_terminator`
- L623: `if in_block_comment`
- L625: `if idx == start`
- L627: `if re.search('\\bEXEC\\s+SQL\\b', body, re.I)`
- L635: `if source_lines is not None and idx < len(source_lines)`
- Another 2 conditions/loops exist in this source span.

### `BoundedLrfSingletonRewriter._source_lrf_filter_literals` - L649-L677

```python
_source_lrf_filter_literals(cls, source_text: str) -> list[str]
```

Extract literals from explicit LRF extra-filter comments for a safety check.

Observed calls (lexical order): `source_text.splitlines`, `enumerate`, `cls._parts`, `body.lower`, `len`, `min`, `range`, `combined.lower`, `re.split`, `collected.extend`, `match.group`, `re.finditer`, `dict.fromkeys`, `list`.

Control points:

- L651: `if not source_text`
- L655: `for (index, line) in enumerate(lines)`
- L657: `if 'extra filter:' not in body.lower() and 'add to the generated cursor where' not in body.lower()`
- L660: `for next_index in range(index + 1, min(index + 4, len(lines)))`
- L662: `if indicator2 not in ('*', '/')`
- L665: `if 'add to the generated cursor where' in combined.lower()`
- L667: `if 'add to the generated cursor where' not in combined.lower()`
- L670: `if 'extra filter:' in combined.lower()`

### `BoundedLrfSingletonRewriter._source_accesses` - L680-L708

```python
_source_accesses(cls, source_text: str) -> list[tuple[str, str]]
```

Return active OBTAIN/FIND FIRST/NEXT accesses across wrapped lines.

Observed calls (lexical order): `source_text.splitlines`, `cls._parts`, `executable_lines.append`, `cls._mask_literals_and_inline_comment`, `' '.join`, `re.compile`, `match.group`, `match.group('record').upper`, `match.group('verb').upper`, `pattern.finditer`.

Control points:

- L690: `if not source_text`
- L693: `for line in source_text.splitlines()`
- L695: `if indicator in ('*', '/', 'D', 'd')`

### `BoundedLrfSingletonRewriter._source_proves_first_only` - L711-L718

```python
_source_proves_first_only(cls, source_text: str) -> bool
```

Prove one source OBTAIN/FIND FIRST with no matching NEXT.

Observed calls (lexical order): `cls._source_accesses`, `len`, `any`.

Control points:

- L715: `if len(firsts) != 1`

### `BoundedLrfSingletonRewriter._source_has_next_for_lrf_first` - L721-L741

```python
_source_has_next_for_lrf_first(cls, source_text: str) -> bool
```

Guard marker-only fallback against an explicit NEXT of its target.

Observed calls (lexical order): `source_text.splitlines`, `cls._parts`, `body.upper`, `re.search`, `marker_records.append`, `match.group`, `match.group('record').upper`, `cls._source_accesses`, `any`.

Control points:

- L723: `if not source_text`
- L726: `for line in source_text.splitlines()`
- L728: `if 'EXPANDED LRF FIRST' not in body.upper()`
- L731: `if match`
- L734: `if marker_records`

### `BoundedLrfSingletonRewriter._find_first_only_loop` - L744-L757

```python
_find_first_only_loop(cls, bodies: list[str], cursor: str, source_lines: list[str])
```

Find a generated single-line FETCH UNTIL EOC for source FIRST-only access.

Observed calls (lexical order): `re.compile`, `re.escape`, `enumerate`, `cls._parts`, `body.strip`, `fetch_pattern.match`, `match.group`, `match.group('para').upper`, `matches.append`, `len`.

Control points:

- L751: `for (index, body) in enumerate(bodies)`
- L752: `if cls._parts(source_lines[index])[1] in ('*', '/')`
- L755: `if match`

### `BoundedLrfSingletonRewriter._find_bounded_loop` - L759-L846

```python
_find_bounded_loop(self, bodies: list[str], cursor: str, source_lines: list[str])
```

Observed calls (lexical order): `enumerate`, `self._parts`, `self._PERFORM_UNTIL.search`, `len`, `min`, `range`, `re.findall`, `self._END_PERFORM.findall`, `any`, `re.search`, `re.compile`, `re.escape`, `fetch_pattern.finditer`, `fetch_matches.append`, `match.group`, `line.strip`.
Another 11 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L761: `for (start, body) in enumerate(bodies)`
- L762: `if self._parts(source_lines[start])[1] in ('*', '/')`
- L765: `if not until_match`
- L775: `for index in range(start + 1, search_end)`
- L776: `if self._parts(source_lines[index])[1] in ('*', '/')`
- L782: `if depth <= 0`
- L785: `if end is None`
- L794: `if any((re.search('\\bPERFORM\\s+UNTIL\\b', line, re.I) for line in block_lines[1:]))`
- Another 9 conditions/loops exist in this source span.

### `BoundedLrfSingletonRewriter._matching_end_if` - L849-L873

```python
_matching_end_if(cls, bodies: list[str], *, source_lines: list[str], start: int) -> int | None
```

Find the matching END-IF for a branch, balancing nested IF blocks.

Observed calls (lexical order): `len`, `range`, `cls._parts`, `cls._mask_literals_and_inline_comment`, `re.findall`, `re.sub`.

Control points:

- L862: `for index in range(start, len(bodies))`
- L864: `if indicator in ('*', '/', 'D', 'd')`
- L871: `if depth <= 0 and index >= start`

### `BoundedLrfSingletonRewriter._mask_literals_and_inline_comment` - L876-L899

```python
_mask_literals_and_inline_comment(text: str) -> str
```

Mask COBOL quoted literals and inline comments while retaining code.

Observed calls (lexical order): `list`, `len`, `range`, `''.join`.

Control points:

- L881: `while index < len(chars)`
- L883: `if quote`
- L885: `if char == quote`
- L886: `if index + 1 < len(chars) and chars[index + 1] == quote`
- L891: `if char in ("'", '"')`
- L894: `if char == '*' and index + 1 < len(chars) and (chars[index + 1] == '>')`
- L895: `for rest in range(index, len(chars))`

### `BoundedLrfSingletonRewriter._paragraph_name` - L902-L908

```python
_paragraph_name(bodies: list[str], pattern: str) -> str | None
```

Observed calls (lexical order): `re.compile`, `body.strip`, `regex.match`, `match.group`, `match.group('name').upper`.

Control points:

- L904: `for body in bodies`
- L906: `if match`

### `BoundedLrfSingletonRewriter._paragraph_span` - L911-L921

```python
_paragraph_span(bodies: list[str], paragraph: str) -> tuple[int | None, int | None]
```

Observed calls (lexical order): `enumerate`, `next`, `re.escape`, `re.match`, `re.compile`, `len`, `range`, `bodies[idx].strip`, `header.match`.

Control points:

- L913: `if start is None`
- L917: `for idx in range(start + 1, len(bodies))`
- L918: `if header.match(bodies[idx].strip())`

### `BoundedLrfSingletonRewriter._find_call` - L924-L933

```python
_find_call(bodies: list[str], paragraph: str, *, before: int | None=None, after: int | None=None) -> int | None
```

Observed calls (lexical order): `re.compile`, `re.escape`, `enumerate`, `regex.search`.

Control points:

- L926: `for (idx, body) in enumerate(bodies)`
- L927: `if before is not None and idx >= before`
- L929: `if after is not None and idx <= after`
- L931: `if regex.search(body)`

### `BoundedLrfSingletonRewriter._build_singleton_sql` - L935-L1037

```python
_build_singleton_sql(self, declaration_lines: list[str], *, cursor: str, selected_columns: list[str], hosts: list[str], predicate_field: str, predicate_literal: str) -> list[str]
```

Observed calls (lexical order): `self._body`, `'\n'.join`, `re.escape`, `re.sub`, `re.sub('\\bEND-EXEC\\.?\\s*$', '', sql, flags=re.I).strip`, `re.search`, `len`, `',\n '.join`, `select_match.end`, `select_match.start`, `enumerate`, `from_match.start`, `self._sql_identifier`, `order_match.start`, `queryno_match.start`, `sql.rstrip`.
Another 23 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L947: `if not from_match or not select_match or len(selected_columns) != len(hosts) or (not hosts)`
- L952: `if not from_match`
- L957: `if not order_match`
- L959: `if predicate_field and predicate_literal`
- L963: `if queryno_match`
- L969: `if not logical_lines[0].upper().startswith('EXEC SQL')`
- L971: `if not any(('FETCH FIRST 1 ROW ONLY' in line.upper() for line in logical_lines))`
- L982: `for line in logical_lines`
- Another 12 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
