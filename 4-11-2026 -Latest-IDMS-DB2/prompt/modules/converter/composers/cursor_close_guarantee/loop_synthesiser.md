# `converter/composers/cursor_close_guarantee/loop_synthesiser.py`

Source: [converter/composers/cursor_close_guarantee/loop_synthesiser.py](../../../../../converter/composers/cursor_close_guarantee/loop_synthesiser.py) | 278 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `48de0baeb63125935345e9cd68cde6e22b9f34490c5bce0cc45117422a8d3687`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the manual OPEN / FETCH-UNTIL / CLOSE shape from scratch.

## Module-level bindings

`__all__` (L278)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.line_utils import CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.message_log import MessageLog
from converter.composers.cursor_close_guarantee.models import CursorParagraphSet, CursorPerform
from converter.composers.cursor_close_guarantee.paragraph_index import ParagraphIndex
from patterns.cursor_close_guarantee_patterns import CONTINUE_PATTERN, WHEN_ZERO_PATTERN
from rules.cursor_close_guarantee_rules import ENFORCE_FETCH_DRIVES_BUSINESS_PARAGRAPH, EXIT_PARAGRAPH_SUFFIX, PERFORM_BUSINESS_TEMPLATE, PERFORM_BUSINESS_THRU_TEMPLATE, PERFORM_CLOSE_TEMPLATE, PERFORM_FETCH_UNTIL_TEMPLATE, PREFER_THRU_EXIT_PARAGRAPH, STATEMENT_TERMINATOR
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/line_utils.py](line_utils.md)
- [converter/composers/cursor_close_guarantee/message_log.py](message_log.md)
- [converter/composers/cursor_close_guarantee/models.py](models.md)
- [converter/composers/cursor_close_guarantee/paragraph_index.py](paragraph_index.md)
- [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)

## Symbol contracts and control points

### `LoopSynthesiser` - L51-L275

```python
class LoopSynthesiser()
```

Creates the manual driving-loop shape for an undriven cursor.

### `LoopSynthesiser.__init__` - L54-L62

```python
__init__(self, line_utils: CursorGuaranteeLineUtils | None=None, paragraph_index: ParagraphIndex | None=None, log: MessageLog | None=None) -> None
```

Observed calls (lexical order): `CursorGuaranteeLineUtils`, `ParagraphIndex`, `MessageLog`.

### `LoopSynthesiser.synthesise` - L70-L120

```python
synthesise(self, lines: list[str], cursor_set: CursorParagraphSet, priming: CursorPerform, repeats: list[CursorPerform], business: str, close_performs: list[CursorPerform], eoc_condition: str) -> list[str]
```

Build OPEN / FETCH-UNTIL / CLOSE for an undriven cursor.

Observed calls (lexical order): `list`, `self.log.log`, `sorted`, `self._remove_statement`, `self._write_driving_loop`.

Control points:

- L100: `if not business`
- L107: `for repeat in sorted(repeats, key=lambda item: item.index, reverse=True)`

### `LoopSynthesiser._bind_fetch_to_business` - L124-L172

```python
_bind_fetch_to_business(self, lines: list[str], fetch_paragraph: str, business: str) -> list[str]
```

Rewrite WHEN ZERO / CONTINUE inside the FETCH paragraph.

Observed calls (lexical order): `self.paragraphs.headers`, `len`, `self.paragraphs.span`, `list`, `self._business_body`, `WHEN_ZERO_PATTERN.match`, `self.lines_utils.logical`, `self.paragraphs.next_executable_index`, `CONTINUE_PATTERN.match`, `self.lines_utils.format_like`, `self.log.log`.

Control points:

- L134: `if span is None`
- L142: `while index < end`
- L143: `if not WHEN_ZERO_PATTERN.match(self.lines_utils.logical(output[index]))`
- L151: `if target < 0`
- L155: `if not CONTINUE_PATTERN.match(self.lines_utils.logical(output[target]))`

### `LoopSynthesiser._business_body` - L174-L185

```python
_business_body(self, headers: list, business: str) -> str
```

PERFORM <para>, or PERFORM <para> THRU <para>-EXIT when it exists.

Observed calls (lexical order): `self.paragraphs.exists`, `PERFORM_BUSINESS_THRU_TEMPLATE.format`, `PERFORM_BUSINESS_TEMPLATE.format`.

Control points:

- L176: `if PREFER_THRU_EXIT_PARAGRAPH`
- L179: `if self.paragraphs.exists(headers, exit_name)`

### `LoopSynthesiser._remove_statement` - L190-L224

```python
_remove_statement(self, lines: list[str], index: int) -> list[str]
```

Delete one statement without orphaning its COBOL sentence.

Observed calls (lexical order): `len`, `self.lines_utils.is_terminated`, `self.lines_utils.logical`, `list`, `self.paragraphs.previous_executable_index`, `self.lines_utils.format_like`, `previous_logical.rstrip`.

Control points:

- L196: `if not 0 <= index < len(lines)`
- L206: `if not carried_period`
- L211: `if previous < 0`
- L216: `if self.lines_utils.is_terminated(previous_logical)`

### `LoopSynthesiser._write_driving_loop` - L229-L275

```python
_write_driving_loop(self, lines: list[str], cursor_set: CursorParagraphSet, priming_index: int, close_performs: list[CursorPerform], eoc_condition: str) -> list[str]
```

Observed calls (lexical order): `len`, `list`, `self.lines_utils.format_like`, `PERFORM_FETCH_UNTIL_TEMPLATE.format`, `self.log.log`, `replacement.append`, `PERFORM_CLOSE_TEMPLATE.format`.

Control points:

- L237: `if not 0 <= priming_index < len(lines)`
- L253: `if close_performs`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
