# `converter/composers/cursor_guarantee/cursor_repair.py`

Source: [converter/composers/cursor_guarantee/cursor_repair.py](../../../../../converter/composers/cursor_guarantee/cursor_repair.py) | 639 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `ce8253d979554e40b7aabd71147b889b3dda2b05bf49306d45d74f95d18a25e2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Every mutation this pass performs.

## Module-level bindings

`NOT_FOUND` (L90), `ALREADY_BOUND` (L91), `CURSOR_PARAGRAPH_OPERATIONS` (L96), `CURSOR_PARAGRAPH_SEPARATOR` (L97), `CURSOR_NAME_PART_INDEX` (L98), `__all__` (L639)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.fetch_business_binder import already_externally_driven
from converter.composers.cursor_guarantee.cursor_lines import CursorLines
from converter.composers.cursor_guarantee.cursor_models import CONTINUE_PATTERN, UNTIL_ONLY_PATTERN, WHEN_ZERO_PATTERN, CursorParagraphSet, CursorPerform, LoopShape, MessageLog
from patterns.cursor_close_guarantee_patterns import ANY_WHEN_PATTERN, END_EVALUATE_PATTERN
from rules.cursor_close_guarantee_rules import ENFORCE_FETCH_DRIVES_BUSINESS_PARAGRAPH, EXIT_PARAGRAPH_SUFFIX, PERFORM_BUSINESS_TEMPLATE, PERFORM_BUSINESS_THRU_TEMPLATE, PERFORM_CLOSE_TEMPLATE, PERFORM_FETCH_UNTIL_TEMPLATE, PREFER_THRU_EXIT_PARAGRAPH, STATEMENT_TERMINATOR, UNTIL_TEMPLATE
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/fetch_business_binder.py](../cursor_close_guarantee/fetch_business_binder.md)
- [converter/composers/cursor_guarantee/cursor_lines.py](cursor_lines.md)
- [converter/composers/cursor_guarantee/cursor_models.py](cursor_models.md)
- [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee_composer.py](../cursor_close_guarantee_composer.md)
- [converter/composers/cursor_guarantee/__init__.py](__init__.md)

## Symbol contracts and control points

### `CursorRepair` - L101-L636

```python
class CursorRepair()
```

Rewrites, inserts and deletes. Owns no path selection.

### `CursorRepair.__init__` - L104-L110

```python
__init__(self, lines_utils: CursorLines | None=None, log: MessageLog | None=None) -> None
```

Observed calls (lexical order): `CursorLines`, `MessageLog`.

### `CursorRepair.normalise_perform_line` - L115-L147

```python
normalise_perform_line(self, lines: list[str], index: int, condition: str, cursor: str) -> list[str]
```

Rewrite the UNTIL tail of a PERFORM <fetch> UNTIL <cond> line.

Observed calls (lexical order): `len`, `self.lines_utils.logical`, `self.lines_utils.partition_until`, `tail.rstrip`, `tail.rstrip(STATEMENT_TERMINATOR).strip`, `self.lines_utils.compress`, `self.lines_utils.is_legacy_condition`, `UNTIL_TEMPLATE.format`, `head.rstrip`, `logical.rstrip`, `logical.rstrip().endswith`, `self._rewrite`.

Control points:

- L123: `if not 0 <= index < len(lines)`
- L129: `if not tail`
- L134: `if self.lines_utils.compress(current) == self.lines_utils.compress(condition)`
- L139: `if not self.lines_utils.is_legacy_condition(current)`
- L144: `if logical.rstrip().endswith(STATEMENT_TERMINATOR)`

### `CursorRepair.normalise_loop` - L149-L184

```python
normalise_loop(self, lines: list[str], loop: LoopShape, condition: str, cursor: str) -> list[str]
```

Rewrite a legacy loop exit condition to the cursor EOC flag.

Observed calls (lexical order): `len`, `self.lines_utils.compress`, `self.lines_utils.is_legacy_condition`, `self.lines_utils.logical`, `UNTIL_ONLY_PATTERN.match`, `UNTIL_TEMPLATE.format`, `self.lines_utils.partition_until`, `head.rstrip`, `self._rewrite`.

Control points:

- L159: `if not 0 <= index < len(lines)`
- L162: `if self.lines_utils.compress(loop.condition) == self.lines_utils.compress(condition)`
- L167: `if not self.lines_utils.is_legacy_condition(loop.condition)`
- L172: `if UNTIL_ONLY_PATTERN.match(logical)`
- L181: `if loop.terminated`

### `CursorRepair._rewrite` - L186-L197

```python
_rewrite(self, lines: list[str], index: int, body: str, cursor: str, condition: str) -> list[str]
```

Observed calls (lexical order): `list`, `self.lines_utils.format_like`, `self.log.log`.

### `CursorRepair.guarantee_close` - L202-L230

```python
guarantee_close(self, lines: list[str], after_index: int, cursor_set: CursorParagraphSet, close_performs: list[CursorPerform]) -> list[str]
```

Observed calls (lexical order): `self.log.log`, `len`, `self.lines_utils.format_like`, `PERFORM_CLOSE_TEMPLATE.format`, `list`, `output.insert`.

Control points:

- L209: `if close_performs`
- L213: `if not 0 <= after_index < len(lines)`

### `CursorRepair.synthesise_loop` - L235-L304

```python
synthesise_loop(self, lines: list[str], cursor_set: CursorParagraphSet, priming: CursorPerform, repeats: list[CursorPerform], business: str, close_performs: list[CursorPerform], eoc_condition: str) -> list[str]
```

Build OPEN / FETCH-UNTIL / CLOSE and drive the business para.

Observed calls (lexical order): `list`, `self.bind_fetch_to_business`, `self.log.log`, `sorted`, `self.remove_statement`, `len`, `self.lines_utils.format_like`, `PERFORM_FETCH_UNTIL_TEMPLATE.format`, `replacement.append`, `PERFORM_CLOSE_TEMPLATE.format`.

Control points:

- L254: `if business and ENFORCE_FETCH_DRIVES_BUSINESS_PARAGRAPH`
- L260: `if not business`
- L264: `for repeat in sorted(repeats, key=lambda item: item.index, reverse=True)`
- L269: `if not 0 <= priming.index < len(output)`
- L284: `if close_performs`

### `CursorRepair.bind_fetch_to_business` - L309-L429

```python
bind_fetch_to_business(self, lines: list[str], fetch_paragraph: str, business: str) -> list[str]
```

Rewrite WHEN ZERO / CONTINUE inside the FETCH paragraph.

Observed calls (lexical order): `self.log.log`, `self.lines_utils.paragraph_headers`, `self.lines_utils.paragraph_span`, `len`, `self._cursor_of`, `already_externally_driven`, `self._business_body`, `self._compress`, `list`, `self.lines_utils.logical`, `WHEN_ZERO_PATTERN.match`, `self._continue_in_branch`, `self.lines_utils.format_like`.

Control points:

- L349: `if not fetch_paragraph or not business`
- L362: `if span is None`
- L370: `if cursor and already_externally_driven(lines, cursor, business, fetch_paragraph)`
- L388: `while index < end`
- L391: `if not WHEN_ZERO_PATTERN.match(logical)`
- L402: `if target == ALREADY_BOUND`
- L410: `if target == NOT_FOUND`
- L425: `if not bound`

### `CursorRepair.remove_fetch_business_binding` - L431-L520

```python
remove_fetch_business_binding(self, lines: list[str], fetch_paragraph: str, business: str) -> list[str]
```

Remove only the duplicate FETCH -> business edge in WHEN ZERO.

Observed calls (lexical order): `self.lines_utils.paragraph_headers`, `self.lines_utils.paragraph_span`, `len`, `self.log.log`, `self._business_body`, `self._compress`, `PERFORM_BUSINESS_TEMPLATE.format`, `list`, `self.lines_utils.logical`, `WHEN_ZERO_PATTERN.match`, `ANY_WHEN_PATTERN.match`, `END_EVALUATE_PATTERN.match`, `range`, `self.lines_utils.is_comment`, `CONTINUE_PATTERN.match`, `self.lines_utils.format_like`.

Control points:

- L444: `if not fetch_paragraph or not business`
- L451: `if span is None`
- L464: `while index < end`
- L466: `if not WHEN_ZERO_PATTERN.match(logical)`
- L471: `while branch_end < end`
- L473: `if candidate and (ANY_WHEN_PATTERN.match(candidate) or END_EVALUATE_PATTERN.match(candidate))`
- L482: `for candidate_index in range(index + 1, branch_end)`
- L484: `if not candidate or self.lines_utils.is_comment(candidate)`
- Another 5 conditions/loops exist in this source span.

### `CursorRepair._continue_in_branch` - L522-L554

```python
_continue_in_branch(self, lines: list[str], start: int, end: int, target_key: str) -> int
```

Index of the CONTINUE inside one WHEN ZERO branch.

Observed calls (lexical order): `len`, `max`, `min`, `range`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `self._compress`, `ANY_WHEN_PATTERN.match`, `END_EVALUATE_PATTERN.match`, `CONTINUE_PATTERN.match`.

Control points:

- L536: `for index in range(max(0, start), min(end, len(lines)))`
- L539: `if not logical or self.lines_utils.is_comment(logical)`
- L542: `if self._compress(logical) == target_key`
- L545: `if ANY_WHEN_PATTERN.match(logical)`
- L548: `if END_EVALUATE_PATTERN.match(logical)`
- L551: `if CONTINUE_PATTERN.match(logical)`

### `CursorRepair._compress` - L557-L559

```python
_compress(text: str) -> str
```

Whitespace-insensitive, case-insensitive comparison key.

Observed calls (lexical order): `' '.join`, `' '.join(str(text or '').split()).upper`, `' '.join(str(text or '').split()).upper().rstrip`, `str`, `str(text or '').split`.

### `CursorRepair._cursor_of` - L562-L581

```python
_cursor_of(fetch_paragraph: str) -> str
```

DZBFASC1 from 720-FETCH-DZBFASC1. Empty when not that shape.

Observed calls (lexical order): `str`, `str(fetch_paragraph or '').upper`, `str(fetch_paragraph or '').upper().split`, `len`, `CURSOR_PARAGRAPH_SEPARATOR.join`.

Control points:

- L573: `if len(parts) <= CURSOR_NAME_PART_INDEX`
- L576: `if parts[1] not in CURSOR_PARAGRAPH_OPERATIONS`

### `CursorRepair._business_body` - L584-L598

```python
_business_body(headers, business: str) -> str
```

Observed calls (lexical order): `PERFORM_BUSINESS_TEMPLATE.format`, `any`, `PERFORM_BUSINESS_THRU_TEMPLATE.format`.

Control points:

- L587: `if not PREFER_THRU_EXIT_PARAGRAPH`
- L592: `if any((header.name == exit_name for header in headers))`

### `CursorRepair.remove_statement` - L603-L636

```python
remove_statement(self, lines: list[str], index: int) -> list[str]
```

Delete one statement without orphaning its COBOL sentence.

Observed calls (lexical order): `len`, `self.lines_utils.logical`, `removed.rstrip`, `removed.rstrip().endswith`, `list`, `self.lines_utils.previous_executable_index`, `previous_logical.rstrip`, `previous_logical.rstrip().endswith`, `self.lines_utils.format_like`.

Control points:

- L609: `if not 0 <= index < len(lines)`
- L618: `if not carried_period`
- L623: `if previous < 0`
- L628: `if previous_logical.rstrip().endswith(STATEMENT_TERMINATOR)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
