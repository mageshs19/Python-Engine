# `tests/restart/_checklist.py`

Source: [tests/restart/_checklist.py](../../../../tests/restart/_checklist.py) | 271 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `cfc70a4fd22be60c0cf3558412bce63961b23652e4b0d35dfda38ed51b4f1132`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The VMDZ1567 verification checklist, as executable assertions.

## Module-level bindings

`HEADER` (L57), `DATA_ENTRY` (L58), `SEQUENCE_LEAK` (L62), `QUERYNO` (L63), `DOUBLE_QUALIFIED` (L64), `QUOTED_LOCATION` (L65), `LITERAL_LOOP` (L66), `COMMIT_STATEMENT` (L70), `OPENERS` (L72), `CLOSERS` (L73), `__all__` (L271)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.restart.restart_injection_composer import NON_PARAGRAPH_WORDS
from rules.restart_standard_rules import ROLE_COMMIT, ROLE_CONTROL
```

## Local dependency notes

- [converter/composers/restart/restart_injection_composer.py](../../converter/composers/restart/restart_injection_composer.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/restart/test_m10c_golden_output.py](test_m10c_golden_output.md)

## Symbol contracts and control points

### `RestartChecklist` - L76-L268

```python
class RestartChecklist()
```

Reads generated COBOL. Changes nothing.

### `RestartChecklist.__init__` - L79-L90

```python
__init__(self, line_utils, *, config=None, legacy_tokens=(), banned_texts=()) -> None
```

Observed calls (lexical order): `tuple`.

### `RestartChecklist.inspect` - L95-L101

```python
inspect(self, text: str) -> list[str]
```

Observed calls (lexical order): `self._bodies`, `findings.extend`, `self._compile_blockers`, `self._behaviour`, `self._standards`.

### `RestartChecklist._compile_blockers` - L106-L122

```python
_compile_blockers(self, bodies: list[str]) -> list[str]
```

Observed calls (lexical order): `SEQUENCE_LEAK.search`, `out.append`, `out.extend`, `self._orphan_terminators`, `self._duplicate_declarations`, `self._value_in_file_section`, `any`, `banned.upper`.

Control points:

- L109: `for body in bodies`
- L110: `if SEQUENCE_LEAK.search(body)`
- L112: `if '..' in body`
- L119: `for banned in self.banned_texts`
- L120: `if any((banned.upper() in body for body in bodies))`

### `RestartChecklist._orphan_terminators` - L125-L134

```python
_orphan_terminators(bodies: list[str]) -> list[str]
```

Observed calls (lexical order): `body.startswith`.

Control points:

- L127: `for body in bodies`
- L128: `if body.startswith(OPENERS)`
- L130: `if body.startswith(CLOSERS)`
- L132: `if depth < 0`

### `RestartChecklist._duplicate_declarations` - L137-L161

```python
_duplicate_declarations(bodies: list[str]) -> list[str]
```

A name declared twice where qualification cannot save it.

Observed calls (lexical order): `set`, `DATA_ENTRY.match`, `match.group`, `match.group('level').lstrip`, `match.group('name').upper`, `out.append`, `roots.add`.

Control points:

- L150: `for body in bodies`
- L152: `if not match`
- L155: `if level not in ('1', '77')`
- L158: `if name in roots`

### `RestartChecklist._value_in_file_section` - L164-L176

```python
_value_in_file_section(bodies: list[str]) -> list[str]
```

VALUE is illegal in the FILE SECTION - a hard compile error.

Observed calls (lexical order): `body.startswith`.

Control points:

- L167: `for body in bodies`
- L168: `if body.startswith('FILE SECTION')`
- L171: `if body.startswith(('WORKING-STORAGE', 'LINKAGE', 'PROCEDURE'))`
- L174: `if inside and ' VALUE ' in f' {body} '`

### `RestartChecklist._behaviour` - L181-L203

```python
_behaviour(self, bodies: list[str]) -> list[str]
```

Observed calls (lexical order): `b.startswith`, `len`, `out.append`, `self.config.paragraph`, `self._performs`, `self._paragraphs`, `paragraphs.get`, `self.config.names.process_paragraph.upper`, `COMMIT_STATEMENT.match`, `any`.

Control points:

- L184: `if len(stops) != 1`
- L187: `if self.config is None`
- L192: `if not self._performs(bodies, control)`
- L194: `if not self._performs(bodies, commit)`
- L199: `if any((COMMIT_STATEMENT.match(body) for body in business))`
- L201: `if not paragraphs`

### `RestartChecklist._performs` - L206-L208

```python
_performs(bodies: list[str], paragraph: str) -> bool
```

Observed calls (lexical order): `paragraph.upper`, `any`, `body.startswith`.

### `RestartChecklist._standards` - L213-L232

```python
_standards(self, bodies: list[str]) -> list[str]
```

Observed calls (lexical order): `QUERYNO.search`, `m.group`, `len`, `set`, `out.append`, `sorted`, `QUOTED_LOCATION.search`, `LITERAL_LOOP.search`, `DOUBLE_QUALIFIED.search`, `out.extend`, `self._totals`, `any`, `token.upper`.

Control points:

- L217: `if len(numbers) != len(set(numbers))`
- L220: `for body in bodies`
- L221: `if QUOTED_LOCATION.search(body)`
- L223: `if LITERAL_LOOP.search(body)`
- L225: `if DOUBLE_QUALIFIED.search(body)`
- L229: `for token in self.legacy_tokens`
- L230: `if any((token.upper() in body for body in bodies))`

### `RestartChecklist._totals` - L235-L242

```python
_totals(bodies: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `body.startswith`, `max`, `any`, `b.startswith`.

Control points:

- L236: `for (index, body) in enumerate(bodies)`
- L237: `if not body.startswith('STOP RUN')`
- L240: `if not any((b.startswith('DISPLAY') for b in window))`

### `RestartChecklist._bodies` - L247-L254

```python
_bodies(self, text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `self.line_utils.logical`, `str(self.line_utils.logical(raw) or '').strip`, `self.line_utils.is_comment`, `' '.join`, `body.upper`, `body.upper().split`, `out.append`.

Control points:

- L249: `for raw in str(text or '').splitlines()`
- L251: `if not body or self.line_utils.is_comment(body)`

### `RestartChecklist._paragraphs` - L257-L268

```python
_paragraphs(bodies: list[str]) -> dict[str, list[str]]
```

Observed calls (lexical order): `HEADER.match`, `match.group`, `match.group('name').upper`, `found[current].append`.

Control points:

- L260: `for body in bodies`
- L262: `if match and match.group('name').upper() not in NON_PARAGRAPH_WORDS`
- L266: `if current`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
