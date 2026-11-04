# `converter/composers/cursor_close_guarantee_composer.py`

Source: [converter/composers/cursor_close_guarantee_composer.py](../../../../converter/composers/cursor_close_guarantee_composer.py) | 490 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `ce04328541a95014927c2e57d5404962fd04525362ce0e8e2f4642dae67ce7ee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Single owner for cursor lifecycle planning and rewriting.

## Module-level bindings

`TOKEN_PERFORM` (L64), `TOKEN_UNTIL` (L65), `TOKEN_END_PERFORM` (L66), `SENTENCE_TERMINATOR` (L67), `UNMAPPED_DIAGNOSTIC_TEMPLATE` (L69), `__all__` (L490)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.fetch_business_binder import already_externally_driven
from converter.composers.cursor_guarantee.business_paragraph_resolver import BusinessParagraphResolver
from converter.composers.cursor_guarantee.cursor_lines import CursorLines
from converter.composers.cursor_guarantee.cursor_models import CursorParagraphSet, CursorPerform, MessageLog
from converter.composers.cursor_guarantee.cursor_repair import CursorRepair
from converter.composers.cursor_guarantee.cursor_scanner import CursorScanner
from rules.cursor_close_guarantee_rules import ENFORCE_CURSOR_CLOSE_GUARANTEE, ENFORCE_FETCH_DRIVES_BUSINESS_PARAGRAPH, EOC_CONDITION_TEMPLATE, OPERATION_CLOSE, OPERATION_FETCH, OPERATION_OPEN, SYNTHESISE_MISSING_DRIVING_LOOP
from rules.cursor_close_guarantee_rules import RECOGNISE_INLINE_BLOCK_DRIVEN_CURSOR
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/fetch_business_binder.py](cursor_close_guarantee/fetch_business_binder.md)
- [converter/composers/cursor_guarantee/business_paragraph_resolver.py](cursor_guarantee/business_paragraph_resolver.md)
- [converter/composers/cursor_guarantee/cursor_lines.py](cursor_guarantee/cursor_lines.md)
- [converter/composers/cursor_guarantee/cursor_models.py](cursor_guarantee/cursor_models.md)
- [converter/composers/cursor_guarantee/cursor_repair.py](cursor_guarantee/cursor_repair.md)
- [converter/composers/cursor_guarantee/cursor_scanner.py](cursor_guarantee/cursor_scanner.md)
- [rules/cursor_close_guarantee_rules.py](../../rules/cursor_close_guarantee_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/pipeline/registry.py](../pipeline/registry.md)
- [runners/audit_cursor_control_ownership.py](../../runners/audit_cursor_control_ownership.md)
- [tests/pipeline/test_single_owner_transformations.py](../../tests/pipeline/test_single_owner_transformations.md)

## Symbol contracts and control points

### `CursorCloseGuaranteeComposer` - L74-L487

```python
class CursorCloseGuaranteeComposer()
```

Last-resort guarantee that a generated cursor loops and closes.

### `CursorCloseGuaranteeComposer.__init__` - L77-L91

```python
__init__(self, line_formatter=None) -> None
```

Observed calls (lexical order): `MessageLog`, `CursorLines`, `CursorScanner`, `CursorRepair`, `BusinessParagraphResolver`.

### `CursorCloseGuaranteeComposer.messages` - L97-L98

```python
messages(self) -> list[str]
```

### `CursorCloseGuaranteeComposer.compose` - L103-L134

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self.log.reset`, `str`, `self.lines_utils.normalize_line_endings`, `self.lines_utils.normalize_line_endings(text).splitlines`, `self.scanner.paragraph_sets`, `self._report`, `'\n'.join`, `'\n'.join(lines).rstrip`, `sorted`, `self._repair_cursor`.

Control points:

- L106: `if not text`
- L109: `if not ENFORCE_CURSOR_CLOSE_GUARANTEE`
- L114: `if not lines`
- L121: `if not cursor_sets`
- L125: `for cursor in sorted(cursor_sets)`
- L128: `if not cursor_set.is_complete`

### `CursorCloseGuaranteeComposer._repair_cursor` - L139-L229

```python
_repair_cursor(self, lines: list[str], cursor_set: CursorParagraphSet) -> list[str]
```

Observed calls (lexical order): `EOC_CONDITION_TEMPLATE.format`, `self.scanner.performs`, `self.scanner.by_operation`, `self._report`, `self._inline_block_span`, `self.repair.guarantee_close`, `self._bind_business_paragraph`, `self._driving_fetch`, `self._repair_inline`, `self.scanner.find_business_loop`, `self._repair_span`, `self.repair.synthesise_loop`, `self._repeat_fetches`.

Control points:

- L149: `if not opens`
- L163: `if span is not None`
- L190: `if driving is not None`
- L206: `if loop is not None`
- L217: `if not SYNTHESISE_MISSING_DRIVING_LOOP`

### `CursorCloseGuaranteeComposer._inline_block_span` - L234-L281

```python
_inline_block_span(self, lines: list[str], fetches: list[CursorPerform]) -> tuple[int, int] | None
```

The inline PERFORM block that already drives a fetch, or None.

Observed calls (lexical order): `enumerate`, `self._is_comment`, `self._logical`, `self._logical(line).upper`, `self._logical(line).upper().strip`, `body.startswith`, `stack.pop`, `any`, `body.endswith`, `stack.append`.

Control points:

- L249: `if not RECOGNISE_INLINE_BLOCK_DRIVEN_CURSOR or not fetches`
- L255: `for (index, line) in enumerate(lines)`
- L256: `if self._is_comment(line)`
- L260: `if not body`
- L263: `if body.startswith(TOKEN_END_PERFORM)`
- L264: `if not stack`
- L267: `if any((start < hit < index for hit in indexes))`
- L271: `if not body.startswith(TOKEN_PERFORM)`
- Another 2 conditions/loops exist in this source span.

### `CursorCloseGuaranteeComposer._bind_business_paragraph` - L286-L331

```python
_bind_business_paragraph(self, lines: list[str], cursor_set: CursorParagraphSet, fetches: list[CursorPerform]) -> tuple[list[str], str]
```

Make the FETCH drive its business paragraph.

Observed calls (lexical order): `self.business_resolver.resolve`, `self._business_paragraph`, `self._repeat_fetches`, `self._report`, `self.repair.bind_fetch_to_business`.

Control points:

- L311: `if not business`
- L316: `if not ENFORCE_FETCH_DRIVES_BUSINESS_PARAGRAPH`
- L319: `if not business`

### `CursorCloseGuaranteeComposer._repair_inline` - L336-L356

```python
_repair_inline(self, lines: list[str], cursor_set: CursorParagraphSet, driving: CursorPerform, closes: list[CursorPerform], eoc_condition: str) -> list[str]
```

INLINE already ran: only the condition and the CLOSE remain.

Observed calls (lexical order): `self.repair.normalise_perform_line`, `self.repair.guarantee_close`.

### `CursorCloseGuaranteeComposer._repair_span` - L361-L398

```python
_repair_span(self, lines: list[str], cursor_set: CursorParagraphSet, loop, business: str, closes: list[CursorPerform], eoc_condition: str) -> list[str]
```

SPAN shape: the business paragraph owns row processing.

Observed calls (lexical order): `already_externally_driven`, `self.repair.remove_fetch_business_binding`, `self.repair.normalise_loop`, `self.repair.guarantee_close`.

Control points:

- L378: `if business and already_externally_driven(lines, cursor_set.cursor, business, cursor_set.fetch_name)`

### `CursorCloseGuaranteeComposer._driving_fetch` - L404-L416

```python
_driving_fetch(fetches: list[CursorPerform]) -> CursorPerform | None
```

The fetch PERFORM that already carries an UNTIL clause.

Control points:

- L413: `for perform in fetches`
- L414: `if perform.has_until`

### `CursorCloseGuaranteeComposer._repeat_fetches` - L419-L431

```python
_repeat_fetches(fetches: list[CursorPerform]) -> list[CursorPerform]
```

Every fetch PERFORM after the priming one, none with UNTIL.

Observed calls (lexical order): `len`.

### `CursorCloseGuaranteeComposer._business_paragraph` - L433-L443

```python
_business_paragraph(self, lines: list[str], repeats: list[CursorPerform]) -> str
```

The paragraph that used to carry the converted OBTAIN NEXT.

Observed calls (lexical order): `self.lines_utils.paragraph_headers`, `self.lines_utils.owner_paragraph`.

Control points:

- L439: `if not repeats`

### `CursorCloseGuaranteeComposer._logical` - L445-L453

```python
_logical(self, line: str) -> str
```

Columns 8-72 of a fixed record, or the stripped line.

Observed calls (lexical order): `getattr`, `callable`, `reader`, `str`, `str(reader(line) or '').strip`, `str(line or '').strip`.

Control points:

- L448: `if callable(reader)`

### `CursorCloseGuaranteeComposer._is_comment` - L455-L465

```python
_is_comment(self, line: str) -> bool
```

Observed calls (lexical order): `getattr`, `callable`, `bool`, `reader`, `str`, `len`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L457: `if callable(reader)`
- L463: `if len(text) > 6`

### `CursorCloseGuaranteeComposer._report` - L467-L487

```python
_report(self, key: str, **fields) -> None
```

Log one diagnostic. An unmapped key is REPORTED, not dropped.

Observed calls (lexical order): `len`, `self.log.log`, `' '.join`, `fields.items`, `sorted`, `self.log.messages.append`, `UNMAPPED_DIAGNOSTIC_TEMPLATE.format`.

Control points:

- L481: `if len(self.log.messages) == before`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
