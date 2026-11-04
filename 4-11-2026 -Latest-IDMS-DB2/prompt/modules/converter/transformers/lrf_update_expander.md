# `converter/transformers/lrf_update_expander.py`

Source: [converter/transformers/lrf_update_expander.py](../../../../converter/transformers/lrf_update_expander.py) | 802 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `ee926b1c26957503fb6bf1ab5108e7c2aef3c96ebdf67457998d45a1382ebe8e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Expands the UPDATE-side Logical Record Facility syntax into classic IDMS.

## Module-level bindings

`PROCEDURE_DIVISION_TOKEN` (L129), `COMMENT_INDICATORS` (L132), `FREE_FORMAT_COMMENT_PREFIXES` (L136), `COMMENT_PREFIX_COLUMNS` (L138), `DEFAULT_INDENT` (L139), `SEQUENCE_AREA_WIDTH` (L140), `INDICATOR_COLUMN` (L141), `VERB_MODIFY` (L143), `VERB_STORE` (L144), `UPDATE_VERBS` (L145), `NAVIGATION_VERBS` (L146), `WHERE_TOKEN` (L147), `UNMAPPED_DIAGNOSTIC_TEMPLATE` (L149), `UNRENDERABLE_DIAGNOSTIC_TEMPLATE` (L152), `UNTERMINATED_KEEP_TEMPLATE` (L155), `__all__` (L802)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.lrf_program_patterns import LR_MODIFY_WHERE_PATTERN
from rules.lrf_conversion_rules import ENABLE_LRF_PATH_EXPANSION, EXPANDED_UPDATE_TEMPLATE, LRF_UPDATE_MESSAGES, MODIFY_TEMPLATE, REQUIRE_MAPPED_DRIVING_RECORD, SKIPPED_NO_PATH_TEMPLATE, SKIPPED_NO_RECORD_TEMPLATE, SKIPPED_STORE_AMBIGUOUS_TEMPLATE, SKIPPED_UNMAPPED_TEMPLATE, STATEMENT_TERMINATOR, STORE_TEMPLATE
from rules.lrf_conversion_rules import ENABLE_LRF_UPDATE_EXPANSION
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/lrf_program_patterns.py](../../patterns/lrf_program_patterns.md)
- [rules/lrf_conversion_rules.py](../../rules/lrf_conversion_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_lrf_update_expander.py](../../tests/test_lrf_update_expander.md)

## Symbol contracts and control points

### `cobol_name` - L161-L163

```python
cobol_name(value: str) -> str
```

UPPERCASE COBOL/IDMS form: hyphens, never underscores.

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `str(value or '').strip().upper().replace`.

### `LrfUpdateExpander` - L166-L799

```python
class LrfUpdateExpander()
```

Rewrites LRF MODIFY / STORE program syntax into classic IDMS syntax.

### `LrfUpdateExpander.__init__` - L169-L177

```python
__init__(self, *, path_resolver=None, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `LrfUpdateExpander.expand` - L180-L299

```python
expand(self, cobol_text: str) -> str
```

Rewrite update-side LRF syntax. Byte-identical when nothing matches.

Observed calls (lexical order): `str`, `text.strip`, `self._contains_lr_update_syntax`, `self._log`, `self._resolver_is_empty`, `text.endswith`, `text.splitlines`, `set`, `len`, `self._logical`, `output.append`, `logical.upper`, `self._is_comment`, `LR_MODIFY_WHERE_PATTERN.match`, `self._starts_update_verb`, `self._collect_update_statement`.
Another 12 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L186: `if not text.strip()`
- L189: `if not (ENABLE_LRF_PATH_EXPANSION and ENABLE_LRF_UPDATE_EXPANSION)`
- L190: `if self._contains_lr_update_syntax(text)`
- L194: `if self.path_resolver is None or self._resolver_is_empty()`
- L195: `if self._contains_lr_update_syntax(text)`
- L199: `if not self._contains_lr_update_syntax(text)`
- L214: `while index < len(lines)`
- L218: `if not in_procedure`
- Another 11 conditions/loops exist in this source span.

### `LrfUpdateExpander._expand_update` - L302-L443

```python
_expand_update(self, line: str, match, *, source_lines: list[str] | None=None) -> tuple[list[str], bool]
```

Observed calls (lexical order): `list`, `match.group`, `str`, `str(match.group('verb') or '').upper`, `cobol_name`, `self._lookup_path`, `self._log`, `SKIPPED_NO_PATH_TEMPLATE.format`, `keep`, `getattr`, `str(getattr(path, 'path_group_verb', '') or '').upper`, `self._store_target_record`, `self._store_is_ambiguous`, `SKIPPED_STORE_AMBIGUOUS_TEMPLATE.format`, `self._driving_record`, `SKIPPED_NO_RECORD_TEMPLATE.format`.
Another 15 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L315: `if path is None`
- L326: `if expected_lr and expected_lr != lr_name`
- L337: `if path_verb and path_verb != verb`
- L358: `if verb == VERB_STORE and self._store_is_ambiguous(path) and (not store_target)`
- L366: `if not record`
- L378: `if element_records and record not in element_records`
- L389: `if REQUIRE_MAPPED_DRIVING_RECORD and (not self._record_is_mapped(record))`
- L405: `for continuation in source_lines[1:]`
- Another 2 conditions/loops exist in this source span.

### `LrfUpdateExpander._expand_update.keep` - L307-L308

```python
keep(marker: str) -> list[str]
```

Observed calls (lexical order): `self._keep_lines`.

### `LrfUpdateExpander._driving_record` - L446-L461

```python
_driving_record(self, path) -> str
```

The element record the path makes current, in COBOL form.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(command, 'verb', '') or '').upper`, `cobol_name`.

Control points:

- L455: `for command in getattr(path, 'commands', None) or []`
- L457: `if verb in NAVIGATION_VERBS`
- L459: `if name`

### `LrfUpdateExpander._store_is_ambiguous` - L463-L472

```python
_store_is_ambiguous(self, path) -> bool
```

True when a STORE path seeds more than one element record.

Observed calls (lexical order): `self._element_records`, `getattr`, `str`, `str(name or '').strip`, `len`.

### `LrfUpdateExpander._store_target_record` - L474-L495

```python
_store_target_record(self, keyword: str, path) -> str
```

Resolve only an exact ST-<element> keyword to its target record.

Observed calls (lexical order): `cobol_name`, `normalized_keyword.startswith`, `self._element_records`, `getattr`, `str`, `str(name or '').strip`.

Control points:

- L483: `if not normalized_keyword.startswith('ST-')`
- L486: `if not target or '-TO-' in target`

### `LrfUpdateExpander._remove_stale_keep_blocks` - L497-L544

```python
_remove_stale_keep_blocks(self, text: str, *, resolved_lrs: set[str], resolved_keywords: set[str]) -> str
```

Drop stale DB2-KEEP blocks superseded by a successful LRF rewrite.

Observed calls (lexical order): `text.splitlines`, `len`, `self._is_comment`, `result.append`, `' '.join`, `self._logical`, `self._logical(line).upper`, `any`, `result.extend`, `newline.join`, `text.endswith`.

Control points:

- L515: `while index < len(lines)`
- L516: `if not self._is_comment(lines[index])`
- L521: `while end < len(lines) and self._is_comment(lines[end])`
- L529: `if not (has_keep and tied_to_resolved_access)`
- L542: `if text.endswith(('\n', '\r'))`

### `LrfUpdateExpander._resolver_is_empty` - L546-L550

```python
_resolver_is_empty(self) -> bool
```

Observed calls (lexical order): `bool`, `self.path_resolver.is_empty`.

### `LrfUpdateExpander._lookup_path` - L552-L559

```python
_lookup_path(self, keyword: str)
```

Observed calls (lexical order): `getattr`, `repository.path_for_keyword`.

Control points:

- L554: `if repository is None`

### `LrfUpdateExpander._element_records` - L561-L568

```python
_element_records(self, logical_record_name: str) -> list
```

Observed calls (lexical order): `getattr`, `repository.element_records`.

Control points:

- L563: `if repository is None`

### `LrfUpdateExpander._record_is_mapped` - L570-L574

```python
_record_is_mapped(self, record_name: str) -> bool
```

Observed calls (lexical order): `bool`, `self.path_resolver.record_is_mapped`.

### `LrfUpdateExpander._statement` - L577-L599

```python
_statement(self, template_line: str, body: str, terminate: bool=True) -> list[str]
```

Render one generated statement.

Observed calls (lexical order): `body.rstrip`, `text.endswith`, `self._body_indent`, `self._emit`.

Control points:

- L596: `if terminate and (not text.endswith(STATEMENT_TERMINATOR))`

### `LrfUpdateExpander._comment` - L601-L604

```python
_comment(self, template_line: str, body: str) -> list[str]
```

Comment body starts at column 8 - no indent, no leading star.

Observed calls (lexical order): `str`, `str(body or '').lstrip`, `str(body or '').lstrip('*').strip`, `self._emit`.

### `LrfUpdateExpander._keep` - L606-L613

```python
_keep(self, line: str, marker: str) -> list[str]
```

Audit marker, then the ORIGINAL statement, untouched.

Observed calls (lexical order): `self._comment`, `rendered.append`.

### `LrfUpdateExpander._emit` - L615-L625

```python
_emit(self, template_line: str, body: str, indicator: str) -> list[str]
```

Observed calls (lexical order): `self._is_fixed`, `self.fixed_format.split`, `self.fixed_format.emit`.

Control points:

- L616: `if not self._is_fixed(template_line)`
- L617: `if indicator == '*'`

### `LrfUpdateExpander._is_terminated` - L628-L630

```python
_is_terminated(text: str) -> bool
```

True when the SOURCE statement ended in a period.

Observed calls (lexical order): `str`, `str(text or '').rstrip`, `str(text or '').rstrip().endswith`.

### `LrfUpdateExpander._logical` - L632-L637

```python
_logical(self, line: str) -> str
```

Columns 8-72 of a fixed record, or the stripped line.

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `LrfUpdateExpander._is_fixed` - L639-L643

```python
_is_fixed(self, line: str) -> bool
```

Observed calls (lexical order): `bool`, `self.fixed_format.is_fixed_line`.

### `LrfUpdateExpander._body_indent` - L645-L653

```python
_body_indent(self, line: str) -> str
```

Observed calls (lexical order): `self._is_fixed`, `str`, `len`, `text.lstrip`, `self.fixed_format.split`, `body.lstrip`.

Control points:

- L646: `if not self._is_fixed(line)`

### `LrfUpdateExpander._is_comment` - L655-L673

```python
_is_comment(self, line: str) -> bool
```

Column 7 decides in fixed format; only * and / in free format.

Observed calls (lexical order): `str`, `self._is_fixed`, `len`, `text[:SEQUENCE_AREA_WIDTH].strip`, `sequence.isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L659: `if self._is_fixed(text)`
- L667: `if len(text) > INDICATOR_COLUMN`
- L669: `if not sequence or sequence.isdigit()`
- L670: `if text[INDICATOR_COLUMN] in COMMENT_INDICATORS`

### `LrfUpdateExpander._starts_update_verb` - L676-L678

```python
_starts_update_verb(logical: str) -> str
```

Observed calls (lexical order): `str`, `str(logical or '').upper`, `str(logical or '').upper().split`.

### `LrfUpdateExpander._collect_update_statement` - L680-L735

```python
_collect_update_statement(self, lines: list[str], start: int) -> tuple[int, str, object | None, bool]
```

Collect a bounded physical span for a wrapped MODIFY/STORE.

Observed calls (lexical order): `self._logical`, `LR_MODIFY_WHERE_PATTERN.match`, `range`, `len`, `self._is_comment`, `re.match`, `re.search`, `joined_parts.append`, `' '.join`, `part.strip`, `logical.rstrip`, `logical.rstrip().endswith`, `bool`.

Control points:

- L695: `if match`
- L699: `for offset in range(1, max_lines)`
- L701: `if position >= len(lines)`
- L705: `if not logical or self._is_comment(raw)`
- L709: `if re.match('^[A-Z0-9-]+(?:\\s+SECTION)?\\.$', logical, re.I) and (not re.search('\\bWHERE\\s*$', joined_parts[-1], re.I))`
- L714: `if re.match('^(?:MOVE|IF|ELSE|END-IF|EVALUATE|WHEN|PERFORM|CALL|DISPLAY|ADD|SUBTRACT|COMPUTE|WRITE|READ|OPEN|CLOSE|OBTAIN|FIND|STORE|MODIFY)\\b', logical, re.I) and (not re.match('...`
- L726: `if match`
- L730: `if logical.rstrip().endswith('.')`

### `LrfUpdateExpander._keep_lines` - L737-L741

```python
_keep_lines(self, source_lines: list[str], marker: str) -> list[str]
```

Emit one audit marker and retain all physical source lines intact.

Observed calls (lexical order): `list`, `self._keep`.

Control points:

- L739: `if not source_lines`

### `LrfUpdateExpander._contains_lr_update_syntax` - L743-L763

```python
_contains_lr_update_syntax(self, text: str) -> bool
```

True when any LOGICAL line carries update-side LRF syntax.

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `enumerate`, `self._is_comment`, `self._logical`, `LR_MODIFY_WHERE_PATTERN.match`, `self._unhandled_update_verb`, `self._starts_update_verb`, `self._collect_update_statement`.

Control points:

- L749: `for (index, raw_line) in enumerate(lines)`
- L750: `if self._is_comment(raw_line)`
- L753: `if not logical`
- L755: `if LR_MODIFY_WHERE_PATTERN.match(logical)`
- L757: `if self._unhandled_update_verb(logical)`
- L759: `if self._starts_update_verb(logical)`
- L761: `if match is not None or has_where`

### `LrfUpdateExpander._unhandled_update_verb` - L766-L779

```python
_unhandled_update_verb(logical: str) -> str
```

The verb of an update-side LR line the single-line pattern missed.

Observed calls (lexical order): `str`, `str(logical or '').upper`, `str(logical or '').upper().split`, `len`.

Control points:

- L773: `if len(tokens) < 3`
- L775: `if tokens[0] not in UPDATE_VERBS`
- L777: `if WHERE_TOKEN not in tokens[1:]`

### `LrfUpdateExpander._log` - L781-L799

```python
_log(self, key: str, **values) -> None
```

Record one diagnostic. An unmapped key is REPORTED, not dropped.

Observed calls (lexical order): `LRF_UPDATE_MESSAGES.get`, `' '.join`, `sorted`, `values.items`, `self.messages.append`, `UNMAPPED_DIAGNOSTIC_TEMPLATE.format`, `template.format`, `UNRENDERABLE_DIAGNOSTIC_TEMPLATE.format`.

Control points:

- L785: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
