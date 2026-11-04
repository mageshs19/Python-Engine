# `converter/composers/counter_declaration/counter_totals_writer.py`

Source: [converter/composers/counter_declaration/counter_totals_writer.py](../../../../../converter/composers/counter_declaration/counter_totals_writer.py) | 158 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `36596ee1290d8bc6c6066a1d4f514e1a5b1e9a179c56308bcebd3ec14d8486a6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> End-of-run counter totals.

## Module-level bindings

`__all__` (L158)

## Import declarations

```python
from __future__ import annotations
from converter.composers.counter_declaration.counter_line_factory import CounterLineFactory
from patterns.cobol_patterns import GOBACK_PATTERN, STOP_RUN_PATTERN
from rules.counter_declaration_rules import COUNTER_DECLARATION_MESSAGES, COUNTER_DISPLAY_TEMPLATE, COUNTER_LABEL_TEMPLATE, COUNTER_LABEL_WIDTH, COUNTER_NAME_PREFIX, COUNTER_NAME_SUFFIX, COUNTER_OUTPUT_TOKEN, TOTALS_ANCHOR_STATEMENT, TOTALS_DISPLAY_VERB, TOTALS_INDENT, TOTALS_LABEL_TOKEN
```

## Local dependency notes

- [converter/composers/counter_declaration/counter_line_factory.py](counter_line_factory.md)
- [patterns/cobol_patterns.py](../../../patterns/cobol_patterns.md)
- [rules/counter_declaration_rules.py](../../../rules/counter_declaration_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/__init__.py](__init__.md)

## Symbol contracts and control points

### `CounterTotalsWriter` - L40-L155

```python
class CounterTotalsWriter()
```

Appends one DISPLAY per counter immediately before STOP RUN.

### `CounterTotalsWriter.__init__` - L43-L48

```python
__init__(self, line_factory: CounterLineFactory | None=None) -> None
```

Observed calls (lexical order): `CounterLineFactory`.

### `CounterTotalsWriter.append` - L51-L81

```python
append(self, lines: list[str], counters: list[str]) -> list[str]
```

Observed calls (lexical order): `self._stop_run_index`, `self.messages.append`, `COUNTER_DECLARATION_MESSAGES['skipped_no_anchor'].format`, `self._already_present`, `self._display_body`, `self.lines.statement`, `self._ordered`, `block.append`, `self.lines.blank`, `COUNTER_DECLARATION_MESSAGES['totals_added'].format`, `len`.

Control points:

- L54: `if not counters`
- L58: `if anchor < 0`
- L66: `if self._already_present(lines, counters)`

### `CounterTotalsWriter._display_body` - L84-L91

```python
_display_body(self, name: str) -> str
```

Observed calls (lexical order): `COUNTER_LABEL_TEMPLATE.format`, `COUNTER_LABEL_TEMPLATE.format(token=self.token_of(name)).ljust`, `self.token_of`, `COUNTER_DISPLAY_TEMPLATE.format`.

### `CounterTotalsWriter._stop_run_index` - L93-L111

```python
_stop_run_index(self, lines: list[str]) -> int
```

First program-termination statement: STOP RUN or GOBACK.

Observed calls (lexical order): `enumerate`, `self.lines.is_skippable`, `self.lines.logical`, `STOP_RUN_PATTERN.match`, `GOBACK_PATTERN.match`.

Control points:

- L101: `for (index, line) in enumerate(lines)`
- L102: `if self.lines.is_skippable(line)`
- L106: `if STOP_RUN_PATTERN.match(logical)`
- L108: `if GOBACK_PATTERN.match(logical)`

### `CounterTotalsWriter._already_present` - L113-L134

```python
_already_present(self, lines: list[str], counters: list[str]) -> bool
```

Observed calls (lexical order): `set`, `self.lines.is_skippable`, `self.lines.logical`, `self.lines.logical(line).upper`, `name.upper`, `displayed.add`, `all`.

Control points:

- L120: `for line in lines`
- L121: `if self.lines.is_skippable(line)`
- L125: `if TOTALS_DISPLAY_VERB not in logical`
- L127: `if TOTALS_LABEL_TOKEN not in logical`
- L130: `for name in counters`
- L131: `if name.upper() in logical`

### `CounterTotalsWriter._ordered` - L137-L145

```python
_ordered(counters: list[str]) -> list[str]
```

Fetch counters first, the output counter last.

Observed calls (lexical order): `f'{COUNTER_NAME_PREFIX}{COUNTER_OUTPUT_TOKEN}{COUNTER_NAME_SUFFIX}'.upper`, `c.upper`.

### `CounterTotalsWriter.token_of` - L148-L155

```python
token_of(name: str) -> str
```

WS-NB-OUTPUT-COUNT -> OUTPUT.

Observed calls (lexical order): `str`, `str(name or '').upper`, `token.startswith`, `len`, `token.endswith`.

Control points:

- L151: `if token.startswith(COUNTER_NAME_PREFIX)`
- L153: `if token.endswith(COUNTER_NAME_SUFFIX)`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
