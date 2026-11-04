# `converter/transformers/lrf_path_expander.py`

Source: [converter/transformers/lrf_path_expander.py](../../../../converter/transformers/lrf_path_expander.py) | 1330 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `eda6fcf8d0eb6cfbdbc7265eba53199559774532273fb6dcafdb580326472337`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Expands LRF syntax into the classic IDMS syntax the converter knows.

## Module-level bindings

`PROCEDURE_DIVISION_TOKEN` (L227), `COMMENT_INDICATORS` (L228), `COMMENT_PREFIX_COLUMNS` (L229), `MODE_NEXT` (L230), `DEFAULT_INDENT` (L231), `__all__` (L1330)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.lrf_program_patterns import BARE_OF_LR_PATTERN, LR_ERASE_WHERE_PATTERN, LR_OBTAIN_WHERE_PATTERN, LR_OBTAIN_WHERE_PREFIX_PATTERN, LR_OBTAIN_START_PATTERN, LR_STATUS_ABBREVIATED_PATTERN, LR_STATUS_CONDITION_PATTERN, LR_STATUS_TOKEN_PATTERN, OF_LR_SUFFIX_PATTERN
from rules.lrf_conversion_rules import ENABLE_LRF_PATH_EXPANSION, END_OF_SET_LITERAL_FRAGMENTS, END_OF_SET_TOKEN, EXPANDED_CALC_PARENT_TEMPLATE, EXPANDED_FILTER_TEMPLATE, EXPANDED_OBTAIN_TEMPLATE, EXPANDED_PARENT_TEMPLATE, FIND_FIRST_TEMPLATE, FOUND_LITERAL_FRAGMENTS, FOUND_NEGATION_FRAGMENTS, LRF_EXPANSION_MESSAGES, LRF_PARENT_NOT_FOUND_TOKEN, MULTILINE_WHERE_SCAN_LIMIT, NEGATION_FRAGMENTS, NOT_FOUND_LITERAL_FRAGMENTS, OBTAIN_CALC_TEMPLATE, OBTAIN_FIRST_TEMPLATE, OBTAIN_NEXT_TEMPLATE, RECORD_FOUND_TOKEN, RECORD_NOT_FOUND_TOKEN, REQUIRE_MAPPED_DRIVING_RECORD, SKIPPED_CALC_PARENT_TEMPLATE, SKIPPED_NO_KEYWORD_TEMPLATE, SKIPPED_NO_PATH_TEMPLATE, SKIPPED_NO_RECORD_TEMPLATE, SKIPPED_UNMAPPED_TEMPLATE, STATEMENT_TERMINATOR, STATUS_END_OF_SET, STATUS_NOT_FOUND, STATUS_SET_EMPTY, UNMAPPED_DIAGNOSTIC_TEMPLATE, UNRENDERABLE_DIAGNOSTIC_TEMPLATE
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/lrf_program_patterns.py](../../patterns/lrf_program_patterns.md)
- [rules/lrf_conversion_rules.py](../../rules/lrf_conversion_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/lrf/test_status_token_classifier.py](../../tests/lrf/test_status_token_classifier.md)
- [tests/test_lrf_keyword_scope_safety.py](../../tests/test_lrf_keyword_scope_safety.md)
- [tests/test_lrf_path_expander.py](../../tests/test_lrf_path_expander.md)

## Symbol contracts and control points

### `cobol_name` - L234-L236

```python
cobol_name(value: str) -> str
```

UPPERCASE COBOL/IDMS form: hyphens, never underscores.

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `str(value or '').strip().upper().replace`.

### `LrfPathExpander` - L239-L1327

```python
class LrfPathExpander()
```

Rewrites LRF program syntax into classic IDMS syntax.

### `LrfPathExpander.__init__` - L242-L260

```python
__init__(self, *, path_resolver=None, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `set`.

### `LrfPathExpander.expand` - L263-L424

```python
expand(self, cobol_text: str) -> str
```

Observed calls (lexical order): `set`, `self._collect_status_literal_semantics`, `str`, `text.strip`, `self.path_resolver.is_empty`, `self._contains_lrf_syntax`, `self._log`, `text.replace`, `text.replace('\r\n', '\n').replace`, `text.replace('\r\n', '\n').replace('\r', '\n').split`, `enumerate`, `self._logical`, `logical.upper`, `output.append`, `self._is_comment`, `LR_OBTAIN_WHERE_PATTERN.match`.
Another 21 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L269: `if not text.strip() or not ENABLE_LRF_PATH_EXPANSION`
- L272: `if self.path_resolver is None or self.path_resolver.is_empty()`
- L273: `if self._contains_lrf_syntax(text)`
- L277: `if not self._contains_lrf_syntax(text)`
- L297: `for (index, line) in enumerate(lines)`
- L298: `if index in pending_consumed`
- L304: `if PROCEDURE_DIVISION_TOKEN in upper`
- L309: `if not in_procedure or self._is_comment(line) or (not logical)`
- Another 16 conditions/loops exist in this source span.

### `LrfPathExpander._expand_obtain` - L427-L444

```python
_expand_obtain(self, line: str, match) -> tuple[list[str], bool]
```

Observed calls (lexical order): `match.group`, `str`, `str(match.group('mode') or '').upper`, `cobol_name`, `self._is_terminated`, `self._render_obtain`.

### `LrfPathExpander._expand_obtain_multiline` - L446-L563

```python
_expand_obtain_multiline(self, *, lines: list[str], start_index: int, first_logical: str, prefix) -> tuple[int, list[str], bool, bool]
```

Expand an OBTAIN ... WHERE that spans more than one line.

Observed calls (lexical order): `prefix.group`, `str`, `str(prefix.group('mode') or '').upper`, `cobol_name`, `self._is_terminated`, `self._log`, `self._keep_span`, `SKIPPED_NO_KEYWORD_TEMPLATE.format`, `len`, `self._logical`, `self._is_comment`, `self._starts_new_statement`, `rendered.extend`, `carried_comments.append`, `f'{assembled} {nxt}'.strip`, `self._split_where`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L476: `while not self._is_terminated(assembled)`
- L477: `if consumed >= MULTILINE_WHERE_SCAN_LIMIT`
- L497: `if nxt_index >= len(lines)`
- L507: `if next_logical and (not self._is_comment(raw)) and self._starts_new_statement(next_logical)`
- L525: `if self._is_comment(raw)`
- L532: `if not nxt`
- L540: `if not keyword`

### `LrfPathExpander._where_begins_on_following_line` - L565-L595

```python
_where_begins_on_following_line(self, lines: list[str], start_index: int, first_logical: str) -> bool
```

Return True only when a wrapped OBTAIN visibly contains WHERE.

Observed calls (lexical order): `re.search`, `range`, `len`, `self._is_comment`, `self._logical`, `self._starts_new_statement`, `f'{assembled} {logical}'.strip`, `self._is_terminated`.

Control points:

- L576: `if re.search('\\bWHERE\\b', assembled, flags=re.IGNORECASE)`
- L578: `for offset in range(1, MULTILINE_WHERE_SCAN_LIMIT)`
- L580: `if position >= len(lines)`
- L583: `if self._is_comment(raw)`
- L586: `if not logical`
- L588: `if self._starts_new_statement(logical)`
- L591: `if re.search('\\bWHERE\\b', assembled, flags=re.IGNORECASE)`
- L593: `if self._is_terminated(assembled)`

### `LrfPathExpander._starts_new_statement` - L598-L621

```python
_starts_new_statement(logical: str) -> bool
```

Recognize a conservative statement boundary during continuation.

Observed calls (lexical order): `str`, `str(logical or '').strip`, `str(logical or '').strip().upper`, `text.split`, `text.split(None, 1)[0].rstrip`, `first.startswith`, `bool`, `re.match`.

Control points:

- L605: `if not text`
- L608: `if first.startswith(('END-',))`
- L610: `if first in {'IF', 'ELSE', 'EVALUATE', 'WHEN', 'PERFORM', 'MOVE', 'DISPLAY', 'ADD', 'SUBTRACT', 'COMPUTE', 'READ', 'WRITE', 'OPEN', 'CLOSE', 'CALL', 'GOBACK', 'STOP', 'EXEC', 'OBTA...`

### `LrfPathExpander._split_where` - L624-L651

```python
_split_where(assembled: str) -> tuple[str, str]
```

Split 'OBTAIN <mode> <lr> WHERE <keyword> \[AND <rest>\].' into (keyword, extra_conditions). extra_conditions keeps the original text after the keyword, without the leading connector or the trailing period.

Observed calls (lexical order): `assembled.upper`, `upper.find`, `assembled[where_at + len(' WHERE '):].strip`, `len`, `clause.rstrip`, `clause.rstrip().rstrip`, `clause.rstrip().rstrip(STATEMENT_TERMINATOR).strip`, `clause.split`, `parts[1].strip`, `rest.upper`, `rest.upper().startswith`, `rest[len(connector):].strip`.

Control points:

- L632: `if where_at < 0`
- L639: `if not parts`
- L646: `for connector in ('AND ', 'OR ')`
- L647: `if rest.upper().startswith(connector)`

### `LrfPathExpander._render_obtain` - L653-L744

```python
_render_obtain(self, *, line: str, mode: str, lr_name: str, keyword: str, extra_conditions: str, terminated: bool, keep_span: tuple | None=None) -> tuple[list[str], bool]
```

Render one expanded access, or keep and comment the source.

Observed calls (lexical order): `self.path_resolver.plan_for_keyword`, `self._log`, `self._refuse`, `SKIPPED_NO_PATH_TEMPLATE.format`, `SKIPPED_NO_RECORD_TEMPLATE.format`, `self._record_is_mapped`, `SKIPPED_UNMAPPED_TEMPLATE.format`, `rendered.extend`, `EXPANDED_OBTAIN_TEMPLATE.format`, `self._comment`, `EXPANDED_FILTER_TEMPLATE.format`, `self._render_parent`, `self._statement`, `template.format`.

Control points:

- L673: `if plan is None`
- L680: `if not plan.is_usable`
- L690: `if REQUIRE_MAPPED_DRIVING_RECORD and (not self._record_is_mapped(record))`
- L708: `if extra_conditions`
- L717: `if mode != MODE_NEXT`

### `LrfPathExpander._render_parent` - L746-L843

```python
_render_parent(self, *, line: str, plan, keyword: str, terminated: bool) -> list[str]
```

Render the parent access that precedes the driving step.

Observed calls (lexical order): `self._comment`, `EXPANDED_PARENT_TEMPLATE.format`, `rendered.extend`, `self._statement`, `FIND_FIRST_TEMPLATE.format`, `self._log`, `getattr`, `str`, `str(getattr(calc, 'record_name', '') or '').strip`, `self._record_is_mapped`, `SKIPPED_CALC_PARENT_TEMPLATE.format`, `EXPANDED_CALC_PARENT_TEMPLATE.format`, `OBTAIN_CALC_TEMPLATE.format`, `cobol_name`, `self.calc_parent_records.add`.

Control points:

- L775: `if plan.parent is not None`
- L802: `if calc is None`
- L806: `if not record`
- L809: `if REQUIRE_MAPPED_DRIVING_RECORD and (not self._record_is_mapped(record))`

### `LrfPathExpander._expand_erase` - L845-L874

```python
_expand_erase(self, line: str, match) -> tuple[list[str], bool]
```

Observed calls (lexical order): `cobol_name`, `match.group`, `self._is_terminated`, `self.path_resolver.plan_for_keyword`, `self._log`, `self._keep`, `SKIPPED_NO_PATH_TEMPLATE.format`, `self._record_is_mapped`, `SKIPPED_UNMAPPED_TEMPLATE.format`, `EXPANDED_OBTAIN_TEMPLATE.format`, `self._comment`, `rendered.extend`, `self._statement`.

Control points:

- L851: `if plan is None or not plan.is_usable`
- L859: `if REQUIRE_MAPPED_DRIVING_RECORD and (not self._record_is_mapped(record))`

### `LrfPathExpander._collect_status_literal_semantics` - L877-L919

```python
_collect_status_literal_semantics(self) -> dict[str, set[str]]
```

Collect authoritative status meanings from the supplied subschema.

Observed calls (lexical order): `getattr`, `callable`, `str`, `names`, `getter`, `actions.items`, `status_meanings.get`, `str(status_code).strip`, `str(action or '').strip`, `str(action or '').strip().upper`, `action_text.startswith`, `cobol_name`, `len`, `result.setdefault`, `result.setdefault(literal, set()).add`, `set`.

Control points:

- L890: `if not callable(names) or not callable(getter)`
- L903: `for logical_record_name in logical_record_names or []`
- L908: `for path in getattr(logical_record, 'paths', []) or []`
- L909: `for command in getattr(path, 'commands', []) or []`
- L911: `for (status_code, action) in actions.items()`
- L914: `if meaning is None or not action_text.startswith('RETURN ')`
- L917: `if literal`

### `LrfPathExpander._status_token` - L922-L1040

```python
_status_token(literal: str, parent_records: set[str] | None=None, status_semantics: dict[str, set[str]] | None=None) -> str | None
```

The DB2 status token for an IDMS LR-STATUS literal, or None.

Observed calls (lexical order): `cobol_name`, `len`, `iter`, `next`, `set`, `sorted`, `text.startswith`, `any`.

Control points:

- L995: `if not text`
- L1003: `if text in semantics`
- L1005: `if len(meanings) != 1`
- L1008: `if meaning == 'end_of_set'`
- L1010: `if meaning in {'not_found', 'set_empty'}`
- L1011: `for parent in sorted(parent_records or set(), key=len, reverse=True)`
- L1012: `if text.startswith(f'{cobol_name(parent)}-')`
- L1020: `if any((f in text for f in NOT_FOUND_LITERAL_FRAGMENTS))`
- Another 6 conditions/loops exist in this source span.

### `LrfPathExpander._rewrite_lr_status` - L1043-L1092

```python
_rewrite_lr_status(logical: str, parent_records: set[str] | None=None, status_semantics: dict[str, set[str]] | None=None) -> tuple[str, int]
```

Rewrite 'LR-STATUS <op> <literal>' to an IDMS status token.

Observed calls (lexical order): `LR_STATUS_ABBREVIATED_PATTERN.search`, `LR_STATUS_CONDITION_PATTERN.sub`.

Control points:

- L1073: `if LR_STATUS_ABBREVIATED_PATTERN.search(logical)`

### `LrfPathExpander._rewrite_lr_status._replace` - L1076-L1090

```python
_replace(match) -> str
```

Observed calls (lexical order): `match.group`, `str`, `str(match.group('operator') or '').upper`, `LrfPathExpander._status_token`, `operator.startswith`.

Control points:

- L1086: `if token is None`

### `LrfPathExpander._strip_of_lr` - L1095-L1098

```python
_strip_of_lr(logical: str) -> tuple[str, int]
```

Observed calls (lexical order): `OF_LR_SUFFIX_PATTERN.subn`, `BARE_OF_LR_PATTERN.subn`.

### `LrfPathExpander._statement` - L1101-L1122

```python
_statement(self, template_line: str, body: str, terminate: bool=True) -> list[str]
```

Render one generated statement.

Observed calls (lexical order): `body.rstrip`, `text.endswith`, `self._body_indent`, `self._emit`.

Control points:

- L1119: `if terminate and (not text.endswith(STATEMENT_TERMINATOR))`

### `LrfPathExpander._comment` - L1124-L1127

```python
_comment(self, template_line: str, body: str) -> list[str]
```

Comment body starts at column 8 - no indent, no leading star.

Observed calls (lexical order): `str`, `str(body or '').lstrip`, `str(body or '').lstrip('*').strip`, `self._emit`.

### `LrfPathExpander._keep` - L1129-L1133

```python
_keep(self, line: str, marker: str) -> list[str]
```

Comment ONE source line out, behind its refusal marker.

Observed calls (lexical order): `self._comment`, `rendered.extend`, `self._logical`.

### `LrfPathExpander._keep_span` - L1135-L1159

```python
_keep_span(self, lines: list[str], start_index: int, consumed: int, marker: str) -> list[str]
```

Comment a WHOLE multi-line statement out, behind its marker.

Observed calls (lexical order): `self._comment`, `len`, `max`, `min`, `range`, `self._logical`, `rendered.extend`.

Control points:

- L1154: `for index in range(start_index, end)`
- L1156: `if not body`

### `LrfPathExpander._refuse` - L1161-L1171

```python
_refuse(self, line: str, keep_span: tuple | None, marker: str) -> list[str]
```

Keep the source behind a refusal marker, span-aware.

Observed calls (lexical order): `self._keep`, `self._keep_span`.

Control points:

- L1168: `if keep_span is None`

### `LrfPathExpander._emit` - L1173-L1183

```python
_emit(self, template_line: str, body: str, indicator: str) -> list[str]
```

Observed calls (lexical order): `self._is_fixed`, `self.fixed_format.split`, `self.fixed_format.emit`.

Control points:

- L1174: `if not self._is_fixed(template_line)`
- L1175: `if indicator == '*'`

### `LrfPathExpander._replace_body` - L1185-L1190

```python
_replace_body(self, line: str, new_body: str) -> str
```

Observed calls (lexical order): `self._body_indent`, `new_body.strip`, `self._is_fixed`, `self.fixed_format.replace_body`.

Control points:

- L1188: `if not self._is_fixed(line)`

### `LrfPathExpander._is_terminated` - L1194-L1201

```python
_is_terminated(text: str) -> bool
```

True when the SOURCE statement ended in a period.

Observed calls (lexical order): `str`, `str(text or '').rstrip`, `str(text or '').rstrip().endswith`.

### `LrfPathExpander._logical` - L1203-L1207

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `LrfPathExpander._is_fixed` - L1209-L1213

```python
_is_fixed(self, line: str) -> bool
```

Observed calls (lexical order): `bool`, `self.fixed_format.is_fixed_line`.

### `LrfPathExpander._body_indent` - L1215-L1223

```python
_body_indent(self, line: str) -> str
```

Observed calls (lexical order): `self._is_fixed`, `str`, `len`, `text.lstrip`, `self.fixed_format.split`, `body.lstrip`.

Control points:

- L1216: `if not self._is_fixed(line)`

### `LrfPathExpander._record_is_mapped` - L1225-L1241

```python
_record_is_mapped(self, record_name: str) -> bool
```

Sheet Mapping probe, tolerant of a resolver that lacks it.

Observed calls (lexical order): `getattr`, `bool`, `probe`.

Control points:

- L1236: `if probe is None`

### `LrfPathExpander._is_comment` - L1244-L1254

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L1252: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `LrfPathExpander._contains_lrf_syntax` - L1256-L1295

```python
_contains_lrf_syntax(self, text: str) -> bool
```

Detect LRF syntax from logical COBOL bodies, not sequence columns.

Observed calls (lexical order): `str`, `str(text or '').upper`, `LR_STATUS_TOKEN_PATTERN.search`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `str(text or '').replace('\r\n', '\n').replace('\r', '\n').split`, `self._logical`, `line.strip`, `self._is_comment`, `enumerate`, `LR_OBTAIN_WHERE_PATTERN.match`, `LR_OBTAIN_WHERE_PREFIX_PATTERN.match`, `LR_ERASE_WHERE_PATTERN.match`, `LR_OBTAIN_START_PATTERN.match`, `self._starts_new_statement`, `re.search`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L1265: `if LR_STATUS_TOKEN_PATTERN.search(upper)`
- L1267: `if ' OF LR' in upper`
- L1276: `for (index, logical) in enumerate(logical_lines)`
- L1277: `if LR_OBTAIN_WHERE_PATTERN.match(logical) or LR_OBTAIN_WHERE_PREFIX_PATTERN.match(logical) or LR_ERASE_WHERE_PATTERN.match(logical)`
- L1284: `if start_match`
- L1288: `for following in logical_lines[index + 1:index + MULTILINE_WHERE_SCAN_LIMIT]`
- L1289: `if self._starts_new_statement(following)`
- L1291: `if re.search('\\bWHERE\\b', following, flags=re.IGNORECASE)`
- Another 1 conditions/loops exist in this source span.

### `LrfPathExpander._log` - L1297-L1327

```python
_log(self, key: str, **values) -> None
```

Record one diagnostic, or record that it could not be recorded.

Observed calls (lexical order): `LRF_EXPANSION_MESSAGES.get`, `' '.join`, `sorted`, `values.items`, `self.messages.append`, `UNMAPPED_DIAGNOSTIC_TEMPLATE.format`, `template.format`, `UNRENDERABLE_DIAGNOSTIC_TEMPLATE.format`.

Control points:

- L1313: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
