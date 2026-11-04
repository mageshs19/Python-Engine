# `converter/composers/restart/legacy_restart_cleanup.py`

Source: [converter/composers/restart/legacy_restart_cleanup.py](../../../../../converter/composers/restart/legacy_restart_cleanup.py) | 275 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `4eb4bbecf279e90c3aad242f47966e8c86b3326d766a2125958444920de58a30`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Removes legacy restart residue so the family can be regenerated.

## Module-level bindings

`__all__` (L275)

## Import declarations

```python
from __future__ import annotations
from converter.generators.restart.restart_config import RestartConfig
from patterns.restart_patterns import LEVEL_77_HEADER_PATTERN, LEVEL_77_WITH_VALUE_PATTERN, PARAGRAPH_HEADER_PATTERN, PROCEDURE_DIVISION_PATTERN, VALUE_LINE_PATTERN
from rules.restart_cleanup_rules import CLEANUP_MESSAGES, DIVISION_SUFFIX, LEGACY_ABEND_MARKER_PREFIX, LEGACY_DECLARATION_NAMES, LEGACY_RESTART_DETECTION_TOKENS, NON_PARAGRAPH_DOTTED_LINES, PARAGRAPH_SPAN_LIMIT, SECTION_SUFFIX, VALUE_CONTINUATION_SCAN_LIMIT
from rules.restart_standard_rules import RESTART_PARAGRAPH_ROLES
```

## Local dependency notes

- [converter/generators/restart/restart_config.py](../../generators/restart/restart_config.md)
- [patterns/restart_patterns.py](../../../patterns/restart_patterns.md)
- [rules/restart_cleanup_rules.py](../../../rules/restart_cleanup_rules.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](restart_injection_composer.md)
- [tests/restart/test_m9a_legacy_cleanup.py](../../../tests/restart/test_m9a_legacy_cleanup.md)

## Symbol contracts and control points

### `LegacyRestartCleanup` - L61-L272

```python
class LegacyRestartCleanup()
```

Detects and removes the previous restart mechanism.

### `LegacyRestartCleanup.__init__` - L64-L67

```python
__init__(self, config: RestartConfig, line_utils) -> None
```

### `LegacyRestartCleanup.clean` - L73-L77

```python
clean(self, lines: list[str]) -> list[str]
```

Remove the restart family and unreferenced legacy storage.

Observed calls (lexical order): `list`, `self.remove_paragraphs`, `self.remove_declarations`.

### `LegacyRestartCleanup.detect` - L79-L91

```python
detect(self, lines: list[str]) -> bool
```

True when any legacy restart token is present.

Observed calls (lexical order): `' '.join`, `self._logical`, `self._log`, `bool`.

Control points:

- L87: `for token in found`
- L89: `if not found`

### `LegacyRestartCleanup.remove_paragraphs` - L97-L108

```python
remove_paragraphs(self, lines: list[str], reset: bool=True) -> list[str]
```

Observed calls (lexical order): `list`, `self._remove_one`, `self.config.paragraph`.

Control points:

- L102: `if reset`
- L106: `for role in RESTART_PARAGRAPH_ROLES`

### `LegacyRestartCleanup._remove_one` - L110-L128

```python
_remove_one(self, lines: list[str], paragraph: str) -> list[str]
```

Observed calls (lexical order): `self._header_index`, `self._log`, `self._span_end`.

Control points:

- L112: `if start < 0`
- L117: `if end - start > PARAGRAPH_SPAN_LIMIT`

### `LegacyRestartCleanup._header_index` - L130-L135

```python
_header_index(self, lines: list[str], paragraph: str) -> int
```

Observed calls (lexical order): `paragraph.upper`, `enumerate`, `self._header_name`, `self._logical`.

Control points:

- L132: `for (index, line) in enumerate(lines)`
- L133: `if self._header_name(self._logical(line)) == wanted`

### `LegacyRestartCleanup._span_end` - L137-L146

```python
_span_end(self, lines: list[str], start: int) -> int
```

Observed calls (lexical order): `len`, `range`, `self._logical`, `self._header_name`, `logical.endswith`.

Control points:

- L138: `for index in range(start + 1, len(lines))`
- L140: `if not logical`
- L142: `if self._header_name(logical)`
- L144: `if logical.endswith((SECTION_SUFFIX, DIVISION_SUFFIX))`

### `LegacyRestartCleanup.remove_declarations` - L152-L182

```python
remove_declarations(self, lines: list[str], reset: bool=True) -> list[str]
```

Observed calls (lexical order): `list`, `self._procedure_index`, `len`, `self._log`, `' '.join`, `self._logical`, `out.extend`, `self._legacy_span`, `out.append`.

Control points:

- L157: `if reset`
- L162: `if split >= len(body)`
- L170: `while index < len(body)`
- L171: `if index >= split`
- L176: `if span is None`

### `LegacyRestartCleanup._legacy_span` - L184-L215

```python
_legacy_span(self, lines: list[str], start: int, referenced: str) -> int | None
```

Observed calls (lexical order): `self._logical`, `LEVEL_77_WITH_VALUE_PATTERN.match`, `self._decide`, `inline.group`, `LEVEL_77_HEADER_PATTERN.match`, `len`, `min`, `range`, `VALUE_LINE_PATTERN.match`, `header.group`, `value.group`.

Control points:

- L193: `if inline`
- L200: `if not header`
- L204: `for cursor in range(start + 1, limit)`
- L206: `if not following`
- L209: `if not value`

### `LegacyRestartCleanup._decide` - L217-L239

```python
_decide(self, name: str, value: str, referenced: str, span_end: int) -> int | None
```

Observed calls (lexical order): `name.upper`, `str`, `str(value or '').startswith`, `self._log`.

Control points:

- L228: `if not is_marker and (not is_legacy)`
- L231: `if upper in referenced`

### `LegacyRestartCleanup._procedure_index` - L245-L249

```python
_procedure_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `PROCEDURE_DIVISION_PATTERN.match`, `self._logical`, `len`.

Control points:

- L246: `for (index, line) in enumerate(lines)`
- L247: `if PROCEDURE_DIVISION_PATTERN.match(self._logical(line))`

### `LegacyRestartCleanup._logical` - L251-L255

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`, `str`, `self.line_utils.is_comment`, `' '.join`, `text.upper`, `text.upper().split`.

Control points:

- L253: `if self.line_utils.is_comment(text)`

### `LegacyRestartCleanup._header_name` - L257-L267

```python
_header_name(self, logical: str) -> str
```

Paragraph name when the line is a header, else an empty string.

Observed calls (lexical order): `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`.

Control points:

- L264: `if logical in NON_PARAGRAPH_DOTTED_LINES`

### `LegacyRestartCleanup._log` - L269-L272

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `CLEANUP_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L271: `if template`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
