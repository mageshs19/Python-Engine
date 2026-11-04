# `converter/composers/counter_declaration_composer.py`

Source: [converter/composers/counter_declaration_composer.py](../../../../converter/composers/counter_declaration_composer.py) | 603 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `c22b5dace38102b29ba5c9a90bf311c5ac67b03a0ed81350f6883d14e9ef5747`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Counter declaration composer.

## Module-level bindings

`NOT_FOUND` (L82), `PROCEDURE_DIVISION_TOKEN` (L86), `__all__` (L603)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.counter_declaration_writer import CounterDeclarationWriter
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.counter_declaration_patterns import COUNTER_INCREMENT_PATTERN, DATA_ENTRY_PATTERN
from rules.counter_declaration_rules import COUNTER_DECLARATION_MESSAGES, EMIT_COUNTER_TOTALS, ENFORCE_COUNTER_DECLARATION
```

## Local dependency notes

- [converter/composers/counter_declaration_writer.py](counter_declaration_writer.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/counter_declaration_patterns.py](../../patterns/counter_declaration_patterns.md)
- [rules/counter_declaration_rules.py](../../rules/counter_declaration_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/registry.py](../pipeline/registry.md)
- [tests/test_input_record_totals_preservation.py](../../tests/test_input_record_totals_preservation.md)

## Symbol contracts and control points

### `CounterDeclarationComposer` - L89-L600

```python
class CounterDeclarationComposer()
```

Declares referenced row counters and emits end-of-run totals.

### `CounterDeclarationComposer.__init__` - L92-L101

```python
__init__(self, fixed_format: FixedFormatLineService | None=None, writer: CounterDeclarationWriter | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `CounterDeclarationWriter`.

### `CounterDeclarationComposer.compose` - L106-L155

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._preserve_input_and_treated_totals`, `self._referenced_counters`, `self.messages.append`, `COUNTER_DECLARATION_MESSAGES['no_references'].format`, `len`, `'\n'.join`, `'\n'.join(lines).rstrip`, `self._declared_names`, `self.writer.declare`, `self.messages.extend`, `self.writer.append_totals`.

Control points:

- L109: `if not text or not ENFORCE_COUNTER_DECLARATION`
- L126: `if not referenced`
- L140: `if missing`
- L144: `if EMIT_COUNTER_TOTALS`

### `CounterDeclarationComposer._preserve_input_and_treated_totals` - L160-L197

```python
_preserve_input_and_treated_totals(self, lines: list[str]) -> list[str]
```

Keep the two business totals used by file-processing programs.

Observed calls (lexical order): `self._normalize_treated_counter_name`, `self._normalize_treated_display_label`, `self._has_treated_counter`, `self._add_input_read_increments`, `self._declared_names`, `self._insert_before_section`, `self.messages.append`, `self._ensure_total_input_display`.

Control points:

- L178: `if not self._has_treated_counter(lines)`
- L182: `if read_count == 0`
- L186: `if 'WS-TOTAL-INPUT' not in declared`

### `CounterDeclarationComposer._normalize_treated_counter_name` - L199-L277

```python
_normalize_treated_counter_name(self, lines: list[str]) -> list[str]
```

Normalize a counted variable displayed as TREATED to WS-*.

Observed calls (lexical order): `set`, `self._is_skippable`, `self._logical`, `self._logical(line).upper`, `re.search`, `increments.add`, `match.group`, `treated_lines.append`, `self._declared_names`, `name.startswith`, `any`, `re.escape`, `re.compile`, `'|'.join`, `sorted`, `updated.append`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L212: `for line in lines`
- L213: `if self._is_skippable(line)`
- L219: `if match`
- L221: `if 'DISPLAY' in logical and 'TREATED' in logical`
- L224: `if not increments or not treated_lines`
- L229: `for name in increments`
- L230: `if name.startswith('WS-')`
- L232: `if name not in declared or f'WS-{name}' in declared`
- Another 6 conditions/loops exist in this source span.

### `CounterDeclarationComposer._normalize_treated_display_label` - L279-L303

```python
_normalize_treated_display_label(self, lines: list[str]) -> list[str]
```

Align the treated-count label to the reference convention.

Observed calls (lexical order): `re.compile`, `self._is_skippable`, `updated.append`, `self.fixed_format.body`, `label_pattern.sub`, `self.fixed_format.is_fixed_line`, `self.fixed_format.replace_body_wrapped`, `updated.extend`, `self.messages.append`.

Control points:

- L287: `for line in lines`
- L288: `if self._is_skippable(line)`
- L293: `if rewritten == body`
- L297: `if self.fixed_format.is_fixed_line(line)`
- L301: `if changed`

### `CounterDeclarationComposer._has_treated_counter` - L305-L330

```python
_has_treated_counter(self, lines: list[str]) -> bool
```

Require a real incremented/displayed treated counter before adding totals.

Observed calls (lexical order): `set`, `self._is_skippable`, `self._logical`, `self._logical(line).upper`, `re.search`, `increments.add`, `match.group`, `displays.append`, `self._declared_names`, `any`, `re.escape`.

Control points:

- L309: `for line in lines`
- L310: `if self._is_skippable(line)`
- L314: `if match`
- L316: `if 'DISPLAY' in logical and 'TREATED' in logical`

### `CounterDeclarationComposer._add_input_read_increments` - L332-L404

```python
_add_input_read_increments(self, lines: list[str]) -> tuple[list[str], int]
```

Increment WS-TOTAL-INPUT only on successful READ operations.

Observed calls (lexical order): `len`, `self._is_skippable`, `self._logical`, `self._logical(lines[index]).upper`, `re.match`, `self._logical(lines[end]).upper`, `body.startswith`, `self._logical(lines[end]).upper().startswith`, `'\n'.join`, `self._logical(line).upper`, `bool`, `re.search`, `next`, `range`, `self._logical(lines[pos]).upper`, `read_blocks.append`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L339: `while index < len(lines)`
- L340: `if self._is_skippable(lines[index])`
- L344: `if not re.match('^READ\\s+[A-Z0-9-]+\\b', logical)`
- L349: `while end < len(lines)`
- L351: `if body.startswith('END-READ') or body == 'END-READ.'`
- L354: `if end > index and re.match('^[A-Z0-9-]+\\.\\s*$', body)`
- L360: `if end >= len(lines) or not self._logical(lines[end]).upper().startswith('END-READ')`
- L379: `for (start, end, not_at_end, already_counted) in read_blocks`
- Another 4 conditions/loops exist in this source span.

### `CounterDeclarationComposer._ensure_total_input_display` - L406-L440

```python
_ensure_total_input_display(self, lines: list[str]) -> list[str]
```

Display input totals beside the existing treated total when possible.

Observed calls (lexical order): `self._is_skippable`, `self._logical`, `self._logical(line).upper`, `self.fixed_format.build`, `enumerate`, `lines.insert`, `self.messages.append`, `re.match`.

Control points:

- L408: `for line in lines`
- L409: `if self._is_skippable(line)`
- L412: `if 'DISPLAY' in logical and 'TOTAL INPUTS' in logical and ('WS-TOTAL-INPUT' in logical)`
- L418: `for (index, line) in enumerate(lines)`
- L419: `if self._is_skippable(line)`
- L422: `if 'DISPLAY' in logical and 'TREATED' in logical and ('WS-COUNT-TREATED' in logical)`
- L428: `for (index, line) in enumerate(lines)`
- L429: `if self._is_skippable(line)`
- Another 1 conditions/loops exist in this source span.

### `CounterDeclarationComposer._insert_before_section` - L442-L493

```python
_insert_before_section(self, lines: list[str], body: str, anchors: tuple[str, ...]) -> list[str]
```

Declare the counter inside WORKING-STORAGE, never inside FILE SECTION.

Observed calls (lexical order): `next`, `enumerate`, `self._is_skippable`, `self._logical`, `self._logical(line).upper`, `self._logical(line).upper().startswith`, `len`, `range`, `self._logical(lines[index]).upper`, `re.match`, `lines.insert`, `self.fixed_format.build`, `lines.append`, `any`, `logical.startswith`, `self.messages.append`.

Control points:

- L458: `if ws_index >= 0`
- L462: `for index in range(ws_index + 1, len(lines))`
- L463: `if self._is_skippable(lines[index])`
- L466: `if re.match('^[A-Z0-9-]+\\s+SECTION\\b', logical) or re.match('^[A-Z]+\\s+DIVISION\\b', logical)`
- L478: `for (index, line) in enumerate(lines)`
- L479: `if self._is_skippable(line)`
- L482: `if any((logical.startswith(anchor) for anchor in anchors))`

### `CounterDeclarationComposer._procedure_division_index` - L498-L514

```python
_procedure_division_index(self, lines: list[str]) -> int
```

Index of the PROCEDURE DIVISION header, or NOT_FOUND.

Observed calls (lexical order): `enumerate`, `self._is_skippable`, `self._logical`, `self._logical(line).upper`, `logical.startswith`.

Control points:

- L508: `for (index, line) in enumerate(lines)`
- L509: `if self._is_skippable(line)`
- L512: `if logical.startswith(PROCEDURE_DIVISION_TOKEN)`

### `CounterDeclarationComposer._referenced_counters` - L516-L546

```python
_referenced_counters(self, lines: list[str]) -> list[str]
```

Counter names the PROCEDURE DIVISION actually increments.

Observed calls (lexical order): `set`, `self._procedure_division_index`, `self._is_skippable`, `COUNTER_INCREMENT_PATTERN.match`, `self._logical`, `self._matched_name`, `self._matched_name(match).upper`, `seen.add`, `found.append`.

Control points:

- L530: `if start == NOT_FOUND`
- L533: `for line in lines[start:]`
- L534: `if self._is_skippable(line)`
- L538: `if not match`
- L542: `if name and name not in seen`

### `CounterDeclarationComposer._declared_names` - L548-L567

```python
_declared_names(self, lines: list[str]) -> set[str]
```

Every data-name declared in the source, upper-cased.

Observed calls (lexical order): `set`, `self._is_skippable`, `DATA_ENTRY_PATTERN.match`, `self._logical`, `self._matched_name`, `name.upper`, `names.add`.

Control points:

- L557: `for line in lines`
- L558: `if self._is_skippable(line)`
- L562: `if match`
- L564: `if name`

### `CounterDeclarationComposer._logical` - L572-L577

```python
_logical(self, line: str) -> str
```

Columns 8-72, stripped. Never raises on a malformed line.

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `CounterDeclarationComposer._is_skippable` - L579-L586

```python
_is_skippable(self, line: str) -> bool
```

Comment, page-eject, debug or continuation line.

Observed calls (lexical order): `bool`, `self.fixed_format.is_comment_or_control_line`, `str`, `str(line or '').lstrip`, `str(line or '').lstrip().startswith`.

### `CounterDeclarationComposer._matched_name` - L589-L600

```python
_matched_name(match) -> str
```

The 'name' group, or the last group the pattern exposes.

Observed calls (lexical order): `match.group`, `str`, `str(match.group('name') or '').strip`, `match.groups`, `str(groups[-1]).strip`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
