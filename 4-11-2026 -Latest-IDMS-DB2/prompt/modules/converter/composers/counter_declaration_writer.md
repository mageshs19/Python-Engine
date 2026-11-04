# `converter/composers/counter_declaration_writer.py`

Source: [converter/composers/counter_declaration_writer.py](../../../../converter/composers/counter_declaration_writer.py) | 286 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `09fff30e8e0af2b63bfedac764ad91df42be348ca6077540bea47c9b2e11d3ee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Facade over the counter declaration package.

## Module-level bindings

`__all__` (L286)

## Import declarations

```python
from __future__ import annotations
from converter.composers.counter_declaration import CounterAnchorResolver, CounterLineFactory, CounterTotalsWriter
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.counter_declaration_patterns import DATA_ENTRY_PATTERN
from rules.counter_declaration_rules import COUNTER_DECLARATION_MESSAGES, COUNTER_DECLARATION_TEMPLATE, COUNTER_NAME_PREFIX, COUNTER_NAME_SUFFIX, COUNTER_PICTURE, ENFORCE_COUNTER_NAME_SHAPE, ENFORCE_TOTALS_SUBSET_OF_DECLARED
```

## Local dependency notes

- [converter/composers/counter_declaration/__init__.py](counter_declaration/__init__.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/counter_declaration_patterns.py](../../patterns/counter_declaration_patterns.md)
- [rules/counter_declaration_rules.py](../../rules/counter_declaration_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration_composer.py](counter_declaration_composer.md)

## Symbol contracts and control points

### `CounterDeclarationWriter` - L77-L283

```python
class CounterDeclarationWriter()
```

Writes counter declarations and end-of-run totals.

### `CounterDeclarationWriter.__init__` - L80-L100

```python
__init__(self, fixed_format: FixedFormatLineService | None=None, resolver: CounterAnchorResolver | None=None, totals_writer: CounterTotalsWriter | None=None) -> None
```

Observed calls (lexical order): `CounterLineFactory`, `FixedFormatLineService`, `CounterAnchorResolver`, `CounterTotalsWriter`.

### `CounterDeclarationWriter.declare` - L103-L148

```python
declare(self, lines: list[str], missing: list[str]) -> list[str]
```

Observed calls (lexical order): `self._declared_names`, `self._admissible`, `self.resolver.resolve`, `self.messages.extend`, `self.messages.append`, `COUNTER_DECLARATION_MESSAGES['skipped_no_group'].format`, `len`, `COUNTER_DECLARATION_TEMPLATE.format`, `block.append`, `self.line_factory.statement`, `self._declared.append`, `COUNTER_DECLARATION_MESSAGES['declared'].format`.

Control points:

- L107: `if not missing`
- L113: `if not admissible`
- L121: `if anchor is None or not anchor.is_usable`
- L130: `for name in admissible`

### `CounterDeclarationWriter.append_totals` - L150-L163

```python
append_totals(self, lines: list[str], counters: list[str]) -> list[str]
```

Observed calls (lexical order): `self._allowed_for_totals`, `self.totals_writer.append`, `self.messages.extend`.

Control points:

- L158: `if not allowed`

### `CounterDeclarationWriter._admissible` - L166-L213

```python
_admissible(self, candidates: list[str], existing: set[str]) -> list[str]
```

Candidates this class is willing to declare.

Observed calls (lexical order): `set`, `str`, `str(raw or '').strip`, `str(raw or '').strip().upper`, `seen.add`, `self._is_counter`, `self.messages.append`, `COUNTER_DECLARATION_MESSAGES['refused_shape'].format`, `COUNTER_DECLARATION_MESSAGES['refused_duplicate'].format`, `admissible.append`.

Control points:

- L187: `for raw in candidates`
- L189: `if not name or name in seen`
- L193: `if ENFORCE_COUNTER_NAME_SHAPE and (not self._is_counter(name))`
- L203: `if name in existing`

### `CounterDeclarationWriter._allowed_for_totals` - L215-L251

```python
_allowed_for_totals(self, lines: list[str], counters: list[str]) -> list[str]
```

Names the totals pass may display.

Observed calls (lexical order): `list`, `n.upper`, `self._declared_names`, `str`, `str(raw or '').strip`, `str(raw or '').strip().upper`, `allowed.append`, `self.messages.append`, `COUNTER_DECLARATION_MESSAGES['refused_total'].format`.

Control points:

- L231: `if not ENFORCE_TOTALS_SUBSET_OF_DECLARED`
- L238: `for raw in counters`
- L240: `if not name`
- L242: `if name in known`

### `CounterDeclarationWriter._declared_names` - L253-L270

```python
_declared_names(self, lines: list[str]) -> set[str]
```

Every data-name declared in the source, upper-cased.

Observed calls (lexical order): `set`, `self.line_factory.is_skippable`, `DATA_ENTRY_PATTERN.match`, `self.line_factory.logical`, `match.group`, `match.group('name').upper`, `names.add`.

Control points:

- L261: `for line in lines`
- L262: `if self.line_factory.is_skippable(line)`
- L267: `if match`

### `CounterDeclarationWriter._is_counter` - L273-L283

```python
_is_counter(name: str) -> bool
```

WS-NB-<token>-COUNT, with a non-empty token.

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `text.startswith`, `text.endswith`, `text[len(COUNTER_NAME_PREFIX):-len(COUNTER_NAME_SUFFIX)].strip`, `len`, `bool`.

Control points:

- L276: `if not text.startswith(COUNTER_NAME_PREFIX)`
- L278: `if not text.endswith(COUNTER_NAME_SUFFIX)`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
