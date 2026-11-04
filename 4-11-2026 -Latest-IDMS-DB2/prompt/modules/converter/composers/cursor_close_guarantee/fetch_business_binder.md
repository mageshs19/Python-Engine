# `converter/composers/cursor_close_guarantee/fetch_business_binder.py`

Source: [converter/composers/cursor_close_guarantee/fetch_business_binder.py](../../../../../converter/composers/cursor_close_guarantee/fetch_business_binder.py) | 713 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `ee09041309cdcbbc215340258d482039630c53e738ea442519ef58ef9ddef9af`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Binds a generated FETCH paragraph to its business paragraph.

## Module-level bindings

`LINE_WIDTH` (L106), `BODY_START` (L107), `BODY_END` (L108), `COMMENT_INDICATORS` (L109), `PERFORM_BUSINESS_TEMPLATE` (L111), `EOC_CONDITION_TEMPLATE` (L112), `UNTIL_LOOKAHEAD_LIMIT` (L116), `_LEGACY_EOC_FORMS` (L120), `_NAME` (L132), `WHEN_ZERO_PATTERN` (L134), `ANY_WHEN_PATTERN` (L137), `END_EVALUATE_PATTERN` (L138), `CONTINUE_PATTERN` (L139), `PARAGRAPH_HEADER_PATTERN` (L141), `SECTION_HEADER_PATTERN` (L144), `DIVISION_PATTERN` (L147), `CURSOR_PARAGRAPH_PATTERN` (L149), `PERFORM_CURSOR_OPEN_PATTERN` (L152), `HOST_GROUP_REFERENCE_PATTERN` (L155), `PERFORM_DRIVER_PATTERN` (L164), `UNTIL_LINE_PATTERN` (L172), `NON_PARAGRAPH_WORDS` (L176), `GENERATED_PARAGRAPH_TOKENS` (L182), `MESSAGES` (L191), `__all__` (L713)

## Import declarations

```python
from __future__ import annotations
import re
from typing import List, Optional, Tuple
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee_composer.py](../cursor_close_guarantee_composer.md)
- [converter/composers/cursor_guarantee/cursor_repair.py](../cursor_guarantee/cursor_repair.md)
- [tests/cursor_close_guarantee/test_fetch_business_binder_span_conflict.py](../../../tests/cursor_close_guarantee/test_fetch_business_binder_span_conflict.md)

## Symbol contracts and control points

### `FetchBusinessBinder` - L226-L690

```python
class FetchBusinessBinder()
```

Replaces CONTINUE under WHEN ZERO with PERFORM <business>.

### `FetchBusinessBinder.__init__` - L229-L231

```python
__init__(self, log=None) -> None
```

### `FetchBusinessBinder.bind` - L237-L270

```python
bind(self, lines: List[str], cursor: str, fetch_paragraph: str, open_paragraph: str) -> Tuple[List[str], str]
```

Bind one cursor. Returns (lines, business_paragraph_or_empty).

Observed calls (lexical order): `self.business_paragraph`, `self._note`, `self.already_externally_driven`, `self._bind_when_zero`.

Control points:

- L245: `if not fetch_paragraph or not open_paragraph`
- L251: `if not business`
- L256: `if self.already_externally_driven(lines, cursor, business, fetch_paragraph)`

### `FetchBusinessBinder.already_externally_driven` - L272-L349

```python
already_externally_driven(self, lines: List[str], cursor: str, business: str, fetch_paragraph: str='') -> bool
```

True when binding WHEN ZERO would create a mutual PERFORM.

Observed calls (lexical order): `str`, `str(business or '').strip`, `str(business or '').strip().upper`, `self._squash`, `EOC_CONDITION_TEMPLATE.format`, `str(cursor or '').upper`, `self.paragraph_spans`, `self.is_generated`, `enumerate`, `self._is_code`, `any`, `self._body`, `self._body(line).upper`, `PERFORM_DRIVER_PATTERN.match`, `match.group`, `match.group('paragraph').upper`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L298: `if not target`
- L304: `if not eoc_token`
- L313: `for (index, line) in enumerate(lines)`
- L314: `if not self._is_code(line)`
- L316: `if any((start <= index <= end for start, end in generated))`
- L321: `if not match`
- L323: `if match.group('paragraph').upper() != target`
- L327: `if not condition`
- Another 3 conditions/loops exist in this source span.

### `FetchBusinessBinder._is_legacy_error_status_end_test` - L356-L365

```python
_is_legacy_error_status_end_test(condition: str) -> bool
```

Recognise a legacy IDMS non-success loop test conservatively.

Observed calls (lexical order): `''.join`, `str`, `str(condition or '').upper`, `str(condition or '').upper().split`, `bool`, `any`.

### `FetchBusinessBinder._business_fetches` - L367-L384

```python
_business_fetches(self, lines: List[str], business: str, fetch_paragraph: str) -> bool
```

True when <business> performs <fetch> inside its own span.

Observed calls (lexical order): `self.span_of`, `str`, `str(fetch_paragraph or '').upper`, `range`, `self._is_code`, `self._body`, `self._body(lines[index]).upper`, `self._body(lines[index]).upper().startswith`.

Control points:

- L372: `if span is None`
- L378: `for index in range(start, end + 1)`
- L379: `if not self._is_code(lines[index])`
- L381: `if self._body(lines[index]).upper().startswith(target)`

### `FetchBusinessBinder._until_lookahead` - L386-L401

```python
_until_lookahead(self, lines: List[str], start_index: int) -> str
```

The condition of an UNTIL clause on a continuation line.

Observed calls (lexical order): `int`, `max`, `len`, `min`, `range`, `self._is_code`, `UNTIL_LINE_PATTERN.match`, `self._body`, `self._body(lines[index]).upper`, `match.group`.

Control points:

- L395: `for index in range(start, end)`
- L396: `if not self._is_code(lines[index])`

### `FetchBusinessBinder._body` - L408-L414

```python
_body(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `text[BODY_START:BODY_END].strip`, `text.strip`.

Control points:

- L410: `if not text`
- L412: `if len(text) > BODY_START and text[:6].isdigit()`

### `FetchBusinessBinder._indicator` - L417-L422

```python
_indicator(line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`, `text.lstrip`.

Control points:

- L419: `if len(text) > 6 and text[:6].isdigit()`

### `FetchBusinessBinder._is_code` - L424-L427

```python
_is_code(self, line: str) -> bool
```

Observed calls (lexical order): `self._indicator`, `bool`, `self._body`.

Control points:

- L425: `if self._indicator(line) in COMMENT_INDICATORS`

### `FetchBusinessBinder._replace_body` - L429-L444

```python
_replace_body(self, line: str, body: str) -> str
```

Rewrite columns 8-72 only. Sequence areas are never displaced.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `window.lstrip`, `(' ' * indent + body)[:width].ljust`, `text.lstrip`.

Control points:

- L433: `if len(text) > BODY_START and text[:6].isdigit()`

### `FetchBusinessBinder.paragraph_name` - L450-L466

```python
paragraph_name(self, line: str) -> str
```

Observed calls (lexical order): `self._is_code`, `self._body`, `DIVISION_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `SECTION_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`.

Control points:

- L451: `if not self._is_code(line)`
- L455: `if DIVISION_PATTERN.match(body)`
- L462: `if not match`

### `FetchBusinessBinder.paragraph_spans` - L468-L484

```python
paragraph_spans(self, lines: List[str]) -> List[tuple]
```

Observed calls (lexical order): `enumerate`, `self.paragraph_name`, `spans.append`, `len`.

Control points:

- L473: `for (index, line) in enumerate(lines)`
- L475: `if not name`
- L477: `if current`
- L481: `if current`

### `FetchBusinessBinder.is_generated` - L487-L491

```python
is_generated(name: str) -> bool
```

Observed calls (lexical order): `str`, `str(name or '').upper`, `CURSOR_PARAGRAPH_PATTERN.match`, `any`.

Control points:

- L489: `if CURSOR_PARAGRAPH_PATTERN.match(clean)`

### `FetchBusinessBinder.span_of` - L493-L500

```python
span_of(self, lines: List[str], paragraph: str) -> Optional[Tuple[int, int]]
```

Observed calls (lexical order): `str`, `str(paragraph or '').upper`, `self.paragraph_spans`.

Control points:

- L497: `for (name, start, end) in self.paragraph_spans(lines)`
- L498: `if name == target`

### `FetchBusinessBinder.business_paragraph` - L506-L536

```python
business_paragraph(self, lines: List[str], cursor: str, fetch_paragraph: str, open_paragraph: str) -> str
```

First non-generated paragraph after the one that OPENs.

Observed calls (lexical order): `self.paragraph_spans`, `self._index_performing`, `self.dclgen_group`, `self.is_generated`, `self._verifies`, `self._note`.

Control points:

- L519: `if not spans`
- L523: `if host < 0`
- L528: `for (name, start, end) in spans[host + 1:]`
- L529: `if self.is_generated(name)`
- L531: `if self._verifies(lines, start, end, cursor, group)`

### `FetchBusinessBinder.dclgen_group` - L538-L557

```python
dclgen_group(self, lines: List[str], fetch_paragraph: str) -> str
```

The group the FETCH reads into, taken from its own INTO list.

Observed calls (lexical order): `self.span_of`, `range`, `self._is_code`, `self._body`, `HOST_GROUP_REFERENCE_PATTERN.search`, `match.group`, `match.group('group').upper`, `body.upper`, `body.upper().startswith`.

Control points:

- L541: `if span is None`
- L545: `for index in range(start, end + 1)`
- L546: `if not self._is_code(lines[index])`
- L551: `if match`
- L554: `if body.upper().startswith('END-EXEC')`

### `FetchBusinessBinder._index_performing` - L559-L571

```python
_index_performing(self, lines: List[str], spans: List[tuple], paragraph: str) -> int
```

Observed calls (lexical order): `f'PERFORM {paragraph}'.upper`, `enumerate`, `range`, `self._is_code`, `self._body`, `self._body(lines[index]).upper`, `self._body(lines[index]).upper().startswith`.

Control points:

- L564: `for (position, (_name, start, end)) in enumerate(spans)`
- L565: `for index in range(start, end + 1)`
- L566: `if not self._is_code(lines[index])`
- L568: `if self._body(lines[index]).upper().startswith(target)`

### `FetchBusinessBinder._verifies` - L573-L593

```python
_verifies(self, lines: List[str], start: int, end: int, cursor: str, group: str) -> bool
```

Observed calls (lexical order): `range`, `self._is_code`, `self._body`, `self._body(lines[index]).upper`, `PERFORM_CURSOR_OPEN_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `str`, `str(cursor).upper`.

Control points:

- L581: `for index in range(start, end + 1)`
- L582: `if not self._is_code(lines[index])`
- L586: `if group and group in body`
- L590: `if match and match.group('cursor').upper() != str(cursor).upper()`

### `FetchBusinessBinder._bind_when_zero` - L599-L657

```python
_bind_when_zero(self, lines: List[str], fetch_paragraph: str, business: str) -> List[str]
```

Replace the CONTINUE in the WHEN ZERO branch. Idempotent.

Observed calls (lexical order): `self.span_of`, `self._note`, `PERFORM_BUSINESS_TEMPLATE.format`, `self._compress`, `list`, `range`, `self._is_code`, `self._body`, `WHEN_ZERO_PATTERN.match`, `ANY_WHEN_PATTERN.match`, `END_EVALUATE_PATTERN.match`, `CONTINUE_PATTERN.match`, `self._replace_body`.

Control points:

- L612: `if span is None`
- L623: `for index in range(start, end + 1)`
- L624: `if not self._is_code(output[index])`
- L629: `if WHEN_ZERO_PATTERN.match(body)`
- L633: `if not in_when_zero`
- L636: `if self._compress(body) == target`
- L644: `if ANY_WHEN_PATTERN.match(body) or END_EVALUATE_PATTERN.match(body)`
- L649: `if CONTINUE_PATTERN.match(body)`

### `FetchBusinessBinder._compress` - L664-L665

```python
_compress(text: str) -> str
```

Observed calls (lexical order): `' '.join`, `' '.join(str(text or '').split()).upper`, `' '.join(str(text or '').split()).upper().rstrip`, `str`, `str(text or '').split`.

### `FetchBusinessBinder._squash` - L668-L670

```python
_squash(text: str) -> str
```

Upper case with every space removed - for condition matching.

Observed calls (lexical order): `''.join`, `''.join(str(text or '').split()).upper`, `''.join(str(text or '').split()).upper().rstrip`, `str`, `str(text or '').split`.

### `FetchBusinessBinder._note` - L672-L690

```python
_note(self, key: str, **values) -> None
```

Observed calls (lexical order): `MESSAGES.get`, `template.format`, `self.messages.append`, `self.log.messages.append`.

Control points:

- L674: `if not template`
- L685: `if self.log is None`

### `already_externally_driven` - L696-L710

```python
already_externally_driven(lines: List[str], cursor: str, business: str, fetch_paragraph: str='') -> bool
```

Stateless form of FetchBusinessBinder.already_externally_driven.

Observed calls (lexical order): `FetchBusinessBinder`, `FetchBusinessBinder().already_externally_driven`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
