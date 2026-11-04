# `converter/composers/move_alignment_composer.py`

Source: [converter/composers/move_alignment_composer.py](../../../../converter/composers/move_alignment_composer.py) | 618 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `fc5869f4fa31241a6b17c60506f402b573417f9ea672233c5b8b2ab74221d100`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Aligns the TO keyword across runs of MOVE statements.

## Module-level bindings

`MASK_CHARACTER` (L50), `BLANK_INDICATOR` (L51), `__all__` (L618)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.move_alignment_rules import BLANK_LINE_BREAKS_RUN, ENFORCE_MOVE_ALIGNMENT, MAX_ALIGN_PADDING, MIN_GAP_BEFORE_TO, MIN_RUN_SIZE, MOVE_ALIGNMENT_MESSAGES, MULTI_RECEIVER_STANDS_ALONE, QUOTE_CHARACTERS, RECEIVER_OFFSET, SENTENCE_TERMINATOR, SKIPPABLE_INDICATORS, SQL_BLOCK_END, SQL_BLOCK_START, STATEMENT_OPENERS, TOKEN_TO, VERB_MOVE
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [rules/move_alignment_rules.py](../../rules/move_alignment_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/registry.py](../pipeline/registry.md)
- [tests/layout/test_move_alignment.py](../../tests/layout/test_move_alignment.md)

## Symbol contracts and control points

### `MoveStatement` - L55-L70

```python
class MoveStatement()
```

One MOVE, however many physical lines carried it.

Declared class/data-model fields:

```python
indent: str = ''
source: str = ''
receivers: list[str] = field(default_factory=list)
terminator: str = ''
templates: list[str] = field(default_factory=list)
```

### `MoveStatement.is_single_receiver` - L65-L66

```python
is_single_receiver(self) -> bool
```

Observed calls (lexical order): `len`.

### `MoveStatement.prefix` - L69-L70

```python
prefix(self) -> str
```

### `Passthrough` - L74-L77

```python
class Passthrough()
```

Any line this pass does not own.

Declared class/data-model fields:

```python
line: str = ''
```

### `MoveAlignmentComposer` - L80-L615

```python
class MoveAlignmentComposer()
```

Aligns TO across runs of MOVE statements.

### `MoveAlignmentComposer.__init__` - L83-L88

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `MoveAlignmentComposer.compose` - L93-L114

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._parse`, `self._render`, `self.messages.append`, `MOVE_ALIGNMENT_MESSAGES['joined'].format`, `'\n'.join`, `'\n'.join(rendered).rstrip`.

Control points:

- L96: `if not text or not ENFORCE_MOVE_ALIGNMENT`
- L109: `if joined`

### `MoveAlignmentComposer._parse` - L119-L152

```python
_parse(self, lines: list[str]) -> tuple[list, int]
```

Observed calls (lexical order): `len`, `self._track_sql`, `self._is_skippable`, `Passthrough`, `items.append`, `self._body`, `self._opens_move`, `self._collect`.

Control points:

- L125: `while index < len(lines)`
- L129: `if in_sql or self._is_skippable(line)`
- L135: `if not self._opens_move(body)`
- L141: `if statement is None`
- L146: `if consumed > 1 and statement.is_single_receiver`

### `MoveAlignmentComposer._collect` - L154-L205

```python
_collect(self, lines: list[str], start: int) -> tuple[MoveStatement | None, int]
```

Gather one MOVE, following its continuation lines.

Observed calls (lexical order): `self._body`, `self._indent`, `body.strip`, `len`, `self._is_skippable`, `self.fixed_format.is_fixed_line`, `follower.strip`, `self._opens_statement`, `templates.append`, `collected.rstrip`, `collected.rstrip().endswith`, `self._split_move`, `MoveStatement`.

Control points:

- L168: `while start + consumed < len(lines)`
- L170: `if self._is_skippable(nxt)`
- L172: `if not self.fixed_format.is_fixed_line(nxt)`
- L176: `if not follower.strip()`
- L178: `if self._opens_statement(follower)`
- L180: `if not self._indent(follower)`
- L187: `if collected.rstrip().endswith(SENTENCE_TERMINATOR)`
- L191: `if parsed is None`

### `MoveAlignmentComposer._split_move` - L207-L245

```python
_split_move(self, text: str) -> tuple[str, list[str], str] | None
```

'MOVE a TO b c' -> ('a', \['b', 'c'\], '').

Observed calls (lexical order): `str`, `str(text or '').strip`, `body.endswith`, `body[:-len(SENTENCE_TERMINATOR)].rstrip`, `len`, `self._mask_literals`, `self._tokens`, `tokens[0][0].upper`, `enumerate`, `word.upper`, `body[source_start:source_end].strip`, `body[tokens[to_index + 1][1]:].strip`, `self._receivers`.

Control points:

- L212: `if body.endswith(SENTENCE_TERMINATOR)`
- L219: `if len(tokens) < 4`
- L221: `if tokens[0][0].upper() != VERB_MOVE`
- L225: `for (position, (word, _start, _end)) in enumerate(tokens)`
- L226: `if position == 0`
- L228: `if word.upper() == TOKEN_TO`
- L232: `if to_index < 2 or to_index == len(tokens) - 1`
- L242: `if not source or not receivers`

### `MoveAlignmentComposer._receivers` - L248-L279

```python
_receivers(text: str) -> list[str]
```

Split a receiver list on qualification boundaries.

Observed calls (lexical order): `str`, `str(text or '').split`, `len`, `word.upper`, `current.extend`, `' '.join`, `receivers.append`.

Control points:

- L255: `if not words`
- L262: `while index < len(words)`
- L266: `if upper in ('OF', 'IN') and current and (index + 1 < len(words))`
- L271: `if current`
- L276: `if current`

### `MoveAlignmentComposer._render` - L284-L327

```python
_render(self, items: list) -> list[str]
```

Observed calls (lexical order): `len`, `isinstance`, `output.append`, `self._run_from`, `sum`, `self._render_run`, `output.extend`, `self._render_unaligned`, `self.messages.append`, `MOVE_ALIGNMENT_MESSAGES['aligned'].format`.

Control points:

- L290: `while index < len(items)`
- L293: `if not isinstance(item, MoveStatement)`
- L308: `if movable >= MIN_RUN_SIZE`
- L310: `if lines is not None`
- L320: `if runs`

### `MoveAlignmentComposer._run_from` - L329-L367

```python
_run_from(self, items: list, start: int) -> tuple[list, int]
```

The longest alignable run beginning at `start`.

Observed calls (lexical order): `len`, `isinstance`, `self._body`, `self._body(candidate.line).strip`, `self._interrupts`, `run.append`, `run.pop`.

Control points:

- L333: `if MULTI_RECEIVER_STANDS_ALONE and (not first.is_single_receiver)`
- L339: `while start + consumed < len(items)`
- L342: `if isinstance(candidate, Passthrough)`
- L343: `if BLANK_LINE_BREAKS_RUN and (not self._body(candidate.line).strip())`
- L349: `if self._interrupts(candidate.line, first.indent)`
- L355: `if candidate.indent != first.indent`
- L357: `if not candidate.is_single_receiver`
- L363: `while run and isinstance(run[-1], Passthrough)`

### `MoveAlignmentComposer._interrupts` - L369-L378

```python
_interrupts(self, line: str, indent: str) -> bool
```

True when `line` is an executable statement at `indent`.

Observed calls (lexical order): `self._is_skippable`, `self._body`, `body.strip`, `self._indent`, `self._opens_statement`.

Control points:

- L371: `if self._is_skippable(line)`
- L374: `if not body.strip()`
- L376: `if self._indent(body) != indent`

### `MoveAlignmentComposer._render_run` - L380-L416

```python
_render_run(self, run: list) -> list[str] | None
```

Observed calls (lexical order): `isinstance`, `len`, `max`, `min`, `self.messages.append`, `MOVE_ALIGNMENT_MESSAGES['refused_padding'].format`, `rendered.append`, `self._aligned_body`, `self._fits`, `self._clone`.

Control points:

- L382: `if len(moves) < MIN_RUN_SIZE`
- L389: `if padding > MAX_ALIGN_PADDING`
- L399: `for item in run`
- L400: `if isinstance(item, Passthrough)`
- L405: `if not self._fits(body)`
- L412: `if line is None`

### `MoveAlignmentComposer._aligned_body` - L419-L424

```python
_aligned_body(move: MoveStatement, to_column: int) -> str
```

Observed calls (lexical order): `move.prefix.ljust`.

### `MoveAlignmentComposer._render_unaligned` - L425-L458

```python
_render_unaligned(self, run: list) -> list[str]
```

A run the aligner refused, or one too short to align.

Observed calls (lexical order): `isinstance`, `out.append`, `out.extend`, `self._render_plain`.

Control points:

- L453: `for entry in run`
- L454: `if isinstance(entry, Passthrough)`

### `MoveAlignmentComposer._render_plain` - L460-L516

```python
_render_plain(self, move) -> list[str]
```

One MOVE, unaligned. Multi-receiver spills to further lines.

Observed calls (lexical order): `isinstance`, `self.messages.append`, `getattr`, `self._fits`, `self._clone`, `lines.append`, `len`, `enumerate`.

Control points:

- L474: `if not isinstance(move, MoveStatement)`
- L485: `if not self._fits(head)`
- L490: `if first is None`
- L496: `for (position, receiver) in enumerate(move.receivers[1:], start=1)`
- L503: `if not self._fits(body)`
- L512: `if built is None`

### `MoveAlignmentComposer._mask_literals` - L521-L540

```python
_mask_literals(text: str) -> str
```

Blank out quoted literals, preserving length and offsets.

Observed calls (lexical order): `str`, `out.append`, `''.join`.

Control points:

- L526: `for character in str(text or '')`
- L527: `if quote`
- L529: `if character == quote`
- L533: `if character in QUOTE_CHARACTERS`

### `MoveAlignmentComposer._tokens` - L543-L560

```python
_tokens(text: str) -> list[tuple[str, int, int]]
```

(word, start, end) for every whitespace-delimited token.

Observed calls (lexical order): `enumerate`, `str`, `character.isspace`, `tokens.append`, `len`.

Control points:

- L548: `for (position, character) in enumerate(str(text or ''))`
- L549: `if character.isspace()`
- L550: `if start >= 0`
- L554: `if start < 0`
- L557: `if start >= 0`

### `MoveAlignmentComposer._opens_move` - L562-L564

```python
_opens_move(self, body: str) -> bool
```

Observed calls (lexical order): `str`, `str(body or '').split`, `bool`, `words[0].upper`.

### `MoveAlignmentComposer._opens_statement` - L566-L570

```python
_opens_statement(self, body: str) -> bool
```

Observed calls (lexical order): `str`, `str(body or '').split`, `words[0].upper`, `words[0].upper().rstrip`.

Control points:

- L568: `if not words`

### `MoveAlignmentComposer._body` - L572-L577

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.split`, `str`, `str(body or '').rstrip`.

### `MoveAlignmentComposer._clone` - L579-L586

```python
_clone(self, template: str, body: str) -> str | None
```

Observed calls (lexical order): `self.fixed_format.split`, `self.fixed_format.build_or_none`.

### `MoveAlignmentComposer._fits` - L588-L592

```python
_fits(self, body: str) -> bool
```

Observed calls (lexical order): `bool`, `self.fixed_format.body_fits`, `len`, `str`.

### `MoveAlignmentComposer._indent` - L595-L597

```python
_indent(body: str) -> str
```

Observed calls (lexical order): `str`, `len`, `text.lstrip`.

### `MoveAlignmentComposer._is_skippable` - L599-L606

```python
_is_skippable(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `text.strip`, `self.fixed_format.is_fixed_line`, `len`.

Control points:

- L601: `if not text.strip()`
- L603: `if not self.fixed_format.is_fixed_line(text)`

### `MoveAlignmentComposer._track_sql` - L609-L615

```python
_track_sql(line: str, in_sql: bool) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').upper`.

Control points:

- L611: `if SQL_BLOCK_START in upper`
- L613: `if in_sql and SQL_BLOCK_END in upper`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
