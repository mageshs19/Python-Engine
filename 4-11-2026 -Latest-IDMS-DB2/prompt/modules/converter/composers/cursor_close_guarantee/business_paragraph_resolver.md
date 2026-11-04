# `converter/composers/cursor_close_guarantee/business_paragraph_resolver.py`

Source: [converter/composers/cursor_close_guarantee/business_paragraph_resolver.py](../../../../../converter/composers/cursor_close_guarantee/business_paragraph_resolver.py) | 218 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `4122074dc99232ea5540c260815bcea7e4e4933de360f9b0c9e1cfab868e319f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Resolves the business paragraph a cursor's row logic lives in.

## Module-level bindings

`GENERATED_PARAGRAPH_TOKENS` (L40), `__all__` (L218)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.line_utils import CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.message_log import MessageLog
from converter.composers.cursor_close_guarantee.models import CursorParagraphSet
from patterns.cursor_close_guarantee_patterns import CURSOR_PARAGRAPH_HEADER_PATTERN, HOST_GROUP_REFERENCE_PATTERN, PARAGRAPH_HEADER_PATTERN, PERFORM_CURSOR_PARAGRAPH_PATTERN, SECTION_HEADER_PATTERN
from rules.cursor_close_guarantee_rules import NON_PARAGRAPH_SINGLE_WORDS
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/line_utils.py](line_utils.md)
- [converter/composers/cursor_close_guarantee/message_log.py](message_log.md)
- [converter/composers/cursor_close_guarantee/models.py](models.md)
- [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Symbol contracts and control points

### `BusinessParagraphResolver` - L50-L215

```python
class BusinessParagraphResolver()
```

Finds and verifies the business paragraph of one cursor.

### `BusinessParagraphResolver.__init__` - L53-L59

```python
__init__(self, line_utils: CursorGuaranteeLineUtils | None=None, log: MessageLog | None=None) -> None
```

Observed calls (lexical order): `CursorGuaranteeLineUtils`, `MessageLog`.

### `BusinessParagraphResolver.resolve` - L65-L92

```python
resolve(self, lines: list[str], cursor_set: CursorParagraphSet) -> str
```

Observed calls (lexical order): `self.paragraph_spans`, `self._index_performing`, `self.dclgen_group`, `self.is_generated`, `self._verifies`, `self.log.log`.

Control points:

- L71: `if not spans`
- L75: `if host < 0`
- L80: `for (name, start, end) in spans[host + 1:]`
- L81: `if self.is_generated(name)`
- L83: `if self._verifies(lines, start, end, cursor_set.cursor, group)`

### `BusinessParagraphResolver.paragraph_name` - L98-L111

```python
paragraph_name(self, line: str) -> str
```

Observed calls (lexical order): `self.lines_utils.logical`, `self.lines_utils.is_comment`, `PARAGRAPH_HEADER_PATTERN.match`, `SECTION_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`.

Control points:

- L100: `if not logical or self.lines_utils.is_comment(logical)`
- L107: `if not match`

### `BusinessParagraphResolver.paragraph_spans` - L113-L129

```python
paragraph_spans(self, lines: list[str]) -> list[tuple]
```

Observed calls (lexical order): `enumerate`, `self.paragraph_name`, `spans.append`, `len`.

Control points:

- L118: `for (index, line) in enumerate(lines)`
- L120: `if not name`
- L122: `if current`
- L126: `if current`

### `BusinessParagraphResolver.is_generated` - L132-L137

```python
is_generated(name: str) -> bool
```

A generated utility or cursor paragraph is never business logic.

Observed calls (lexical order): `str`, `str(name or '').upper`, `CURSOR_PARAGRAPH_HEADER_PATTERN.match`, `any`.

Control points:

- L135: `if CURSOR_PARAGRAPH_HEADER_PATTERN.match(f'{clean}.')`

### `BusinessParagraphResolver.dclgen_group` - L143-L172

```python
dclgen_group(self, lines: list[str], cursor_set: CursorParagraphSet) -> str
```

The group the FETCH reads into, taken from its own INTO list.

Observed calls (lexical order): `str`, `str(cursor_set.fetch_name or '').upper`, `self.lines_utils.logical`, `self.paragraph_name`, `HOST_GROUP_REFERENCE_PATTERN.search`, `match.group`, `match.group('group').upper`, `logical.upper`, `logical.upper().startswith`.

Control points:

- L150: `if not target`
- L154: `for line in lines`
- L156: `if not logical`
- L159: `if self.paragraph_name(line) == target`
- L162: `if not inside`
- L166: `if match`
- L169: `if logical.upper().startswith('END-EXEC')`

### `BusinessParagraphResolver._index_performing` - L178-L192

```python
_index_performing(self, lines: list[str], spans: list[tuple], paragraph: str) -> int
```

Observed calls (lexical order): `f'PERFORM {paragraph}'.upper`, `enumerate`, `range`, `self.lines_utils.logical`, `logical.upper`, `logical.upper().startswith`.

Control points:

- L186: `for (position, (_name, start, end)) in enumerate(spans)`
- L187: `for index in range(start, end + 1)`
- L189: `if logical and logical.upper().startswith(target)`

### `BusinessParagraphResolver._verifies` - L194-L215

```python
_verifies(self, lines: list[str], start: int, end: int, cursor: str, group: str) -> bool
```

Observed calls (lexical order): `range`, `self.lines_utils.logical`, `self.lines_utils.is_comment`, `logical.upper`, `PERFORM_CURSOR_PARAGRAPH_PATTERN.match`, `match.group`, `match.group('cursor').upper`, `str`, `str(cursor).upper`.

Control points:

- L202: `for index in range(start, end + 1)`
- L204: `if not logical or self.lines_utils.is_comment(logical)`
- L208: `if group and group in upper`
- L212: `if match and match.group('cursor').upper() != str(cursor).upper()`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
