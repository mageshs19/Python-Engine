# `converter/composers/cursor_guarantee/business_paragraph_resolver.py`

Source: [converter/composers/cursor_guarantee/business_paragraph_resolver.py](../../../../../converter/composers/cursor_guarantee/business_paragraph_resolver.py) | 348 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `3f724634d3a0cc468a99c85b7784fd83959913b42f6a4162478272b8e75c0a41`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Resolves the business paragraph a cursor's row logic lives in.

## Module-level bindings

`BODY_START` (L59), `BODY_END` (L60), `COMMENT_INDICATORS` (L61), `_NAME` (L66), `PARAGRAPH_HEADER_PATTERN` (L68), `SECTION_HEADER_PATTERN` (L71), `DIVISION_PATTERN` (L74), `CURSOR_PARAGRAPH_PATTERN` (L77), `PERFORM_CURSOR_OPEN_PATTERN` (L80), `HOST_GROUP_REFERENCE_PATTERN` (L85), `END_EXEC_PATTERN` (L89), `NON_PARAGRAPH_WORDS` (L92), `GENERATED_PARAGRAPH_TOKENS` (L99), `__all__` (L348)

## Import declarations

```python
from __future__ import annotations
import re
from rules.cursor_close_guarantee_rules import EXIT_PARAGRAPH_SUFFIX
```

## Local dependency notes

- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee_composer.py](../cursor_close_guarantee_composer.md)
- [tests/pipeline/test_single_owner_transformations.py](../../../tests/pipeline/test_single_owner_transformations.md)

## Symbol contracts and control points

### `BusinessParagraphResolver` - L109-L345

```python
class BusinessParagraphResolver()
```

Finds and verifies the business paragraph of one cursor.

### `BusinessParagraphResolver.__init__` - L112-L114

```python
__init__(self, lines_utils=None, log=None) -> None
```

### `BusinessParagraphResolver.resolve` - L119-L155

```python
resolve(self, lines: list[str], cursor_set) -> str
```

The verified business paragraph, or '' when unresolved.

Observed calls (lexical order): `getattr`, `str`, `self.paragraph_spans`, `self._index_performing`, `self.dclgen_group`, `self.is_generated`, `self._verifies`, `self._log`.

Control points:

- L121: `if not lines or cursor_set is None`
- L128: `if not open_name`
- L132: `if not spans`
- L136: `if host < 0`
- L141: `for (name, start, end) in spans[host + 1:]`
- L142: `if self.is_generated(name)`
- L145: `if self._verifies(lines, start, end, cursor, group)`

### `BusinessParagraphResolver.paragraph_name` - L160-L177

```python
paragraph_name(self, line: str) -> str
```

The paragraph or section name on this line, or ''.

Observed calls (lexical order): `self._logical`, `self._is_comment`, `DIVISION_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `SECTION_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`.

Control points:

- L163: `if not logical or self._is_comment(logical)`
- L166: `if DIVISION_PATTERN.match(logical)`
- L173: `if not match`

### `BusinessParagraphResolver.paragraph_spans` - L179-L196

```python
paragraph_spans(self, lines: list[str]) -> list[tuple]
```

(name, first_index, last_index) for every paragraph, in order.

Observed calls (lexical order): `enumerate`, `self.paragraph_name`, `spans.append`, `len`.

Control points:

- L185: `for (index, line) in enumerate(lines)`
- L187: `if not name`
- L189: `if current`
- L193: `if current`

### `BusinessParagraphResolver.is_generated` - L199-L212

```python
is_generated(name: str) -> bool
```

A generated cursor or utility paragraph is never business logic.

Observed calls (lexical order): `str`, `str(name or '').upper`, `CURSOR_PARAGRAPH_PATTERN.match`, `clean.endswith`, `any`.

Control points:

- L202: `if not clean`
- L204: `if CURSOR_PARAGRAPH_PATTERN.match(clean)`
- L210: `if clean.endswith(EXIT_PARAGRAPH_SUFFIX)`

### `BusinessParagraphResolver.dclgen_group` - L217-L243

```python
dclgen_group(self, lines: list[str], fetch_paragraph: str) -> str
```

The group the FETCH reads into, taken from its own INTO list.

Observed calls (lexical order): `self._span_of`, `range`, `self._logical`, `self._is_comment`, `HOST_GROUP_REFERENCE_PATTERN.search`, `match.group`, `match.group('group').upper`, `END_EXEC_PATTERN.match`.

Control points:

- L223: `if not fetch_paragraph`
- L227: `if span is None`
- L231: `for index in range(start, end + 1)`
- L233: `if not logical or self._is_comment(logical)`
- L237: `if match`
- L240: `if END_EXEC_PATTERN.match(logical)`

### `BusinessParagraphResolver._span_of` - L248-L253

```python
_span_of(self, lines: list[str], paragraph: str)
```

Observed calls (lexical order): `str`, `str(paragraph or '').upper`, `self.paragraph_spans`.

Control points:

- L250: `for (name, start, end) in self.paragraph_spans(lines)`
- L251: `if name == target`

### `BusinessParagraphResolver._index_performing` - L255-L272

```python
_index_performing(self, lines: list[str], spans: list[tuple], paragraph: str) -> int
```

Position in `spans` of the paragraph that performs `paragraph`.

Observed calls (lexical order): `f'PERFORM {paragraph}'.upper`, `enumerate`, `range`, `self._logical`, `self._is_comment`, `logical.upper`, `logical.upper().startswith`.

Control points:

- L264: `for (position, (_name, start, end)) in enumerate(spans)`
- L265: `for index in range(start, end + 1)`
- L267: `if not logical or self._is_comment(logical)`
- L269: `if logical.upper().startswith(target)`

### `BusinessParagraphResolver._verifies` - L274-L300

```python
_verifies(self, lines: list[str], start: int, end: int, cursor: str, group: str) -> bool
```

True when the candidate really is this cursor's row logic.

Observed calls (lexical order): `range`, `self._logical`, `self._is_comment`, `logical.upper`, `PERFORM_CURSOR_OPEN_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `str`, `str(cursor).upper`.

Control points:

- L283: `for index in range(start, end + 1)`
- L285: `if not logical or self._is_comment(logical)`
- L291: `if group and group in upper`
- L297: `if match and match.group('cursor').upper() != str(cursor).upper()`

### `BusinessParagraphResolver._logical` - L305-L312

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `getattr`, `callable`, `getter`, `str`, `str(getter(line) or '').strip`, `self._fallback_logical`.

Control points:

- L307: `if callable(getter)`

### `BusinessParagraphResolver._is_comment` - L314-L322

```python
_is_comment(self, logical: str) -> bool
```

Observed calls (lexical order): `getattr`, `callable`, `bool`, `checker`, `str`, `str(logical or '').lstrip`.

Control points:

- L316: `if callable(checker)`

### `BusinessParagraphResolver._fallback_logical` - L325-L334

```python
_fallback_logical(line: str) -> str
```

Columns 8-72 of a fixed-format record, else the stripped line.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `text[BODY_START:BODY_END].strip`, `text.strip`.

Control points:

- L328: `if not text`
- L330: `if len(text) > BODY_START and text[:6].isdigit()`
- L331: `if text[6:7] in COMMENT_INDICATORS`

### `BusinessParagraphResolver._log` - L336-L345

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `getattr`, `callable`, `logger`.

Control points:

- L337: `if self.log is None`
- L340: `if not callable(logger)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
