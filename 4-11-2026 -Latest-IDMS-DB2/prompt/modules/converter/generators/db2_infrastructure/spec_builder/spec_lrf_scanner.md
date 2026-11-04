# `converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py) | 186 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `b28a7d4c7684d9ce93c0c8028f056f98cb09b941128a36bd0d562e3ad6c144a5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reads the generated LRF expansion comments back out of the program.

## Module-level bindings

`MARKER_HEAD` (L68), `JOIN_SEPARATOR` (L78), `__all__` (L186)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from converter.generators.db2_infrastructure.spec_builder.spec_fixed_format import bodies_of
from converter.services.name_normalizer import NameNormalizer
from patterns.cursor_spec import LRF_CONTINUATION_RECORD_PATTERN, LRF_EXPANSION_PATTERN, LRF_EXPANSION_WRAPPED_PATTERN
from rules.lrf_conversion_rules import LRF_MARKER_CONTINUATION_LINES
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/spec_fixed_format.py](spec_fixed_format.md)
- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)
- [patterns/cursor_spec/__init__.py](../../../../patterns/cursor_spec/__init__.md)
- [rules/lrf_conversion_rules.py](../../../../rules/lrf_conversion_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)
- [tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.py](../../../../tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.md)

## Symbol contracts and control points

### `LrfCursor` - L82-L88

```python
class LrfCursor()
```

One record reached through an LRF path.

Declared class/data-model fields:

```python
record: str = ''
mode: str = ''
subschema: str = ''
sweep_condition: str = ''
```

### `SpecLrfScanner` - L91-L183

```python
class SpecLrfScanner()
```

Recovers LRF expansion markers. Read-only.

### `SpecLrfScanner.cursors` - L94-L114

```python
cursors(self, cobol_text: str) -> dict[str, LrfCursor]
```

record name -> LrfCursor. First marker for a record wins.

Observed calls (lexical order): `bodies_of`, `enumerate`, `self._single_line`, `self._joined`, `self._wrapped`.

Control points:

- L99: `for (index, body) in enumerate(bodies)`
- L100: `if not body`
- L108: `if entry is None`
- L111: `if entry.record and entry.record not in output`

### `SpecLrfScanner._single_line` - L118-L128

```python
_single_line(body: str) -> LrfCursor | None
```

The marker fitted on one line: arrow and record together.

Observed calls (lexical order): `LRF_EXPANSION_PATTERN.search`, `LrfCursor`, `NameNormalizer.normalize`, `match.group`, `match.group('mode').upper`, `match.group('subschema').upper`, `match.group('sweep').upper`.

Control points:

- L121: `if not match`

### `SpecLrfScanner._joined` - L131-L163

```python
_joined(cls, bodies: list[str], index: int) -> LrfCursor | None
```

Assemble the marker from its logical bodies, then match.

Observed calls (lexical order): `head.upper`, `len`, `min`, `range`, `nxt.upper`, `parts.append`, `JOIN_SEPARATOR.join`, `LRF_EXPANSION_PATTERN.search`, `LrfCursor`, `NameNormalizer.normalize`, `match.group`, `match.group('mode').upper`, `match.group('subschema').upper`, `match.group('sweep').upper`.

Control points:

- L138: `if MARKER_HEAD not in head.upper()`
- L144: `for following in range(index + 1, limit)`
- L146: `if not nxt`
- L149: `if MARKER_HEAD in nxt.upper()`
- L155: `if match`

### `SpecLrfScanner._wrapped` - L166-L183

```python
_wrapped(bodies: list[str], index: int) -> LrfCursor | None
```

Shape B fallback: arrow ends line 1, record opens line 2.

Observed calls (lexical order): `LRF_EXPANSION_WRAPPED_PATTERN.search`, `len`, `LRF_CONTINUATION_RECORD_PATTERN.match`, `LrfCursor`, `NameNormalizer.normalize`, `continuation.group`, `match.group`, `match.group('mode').upper`, `match.group('subschema').upper`, `match.group('sweep').upper`.

Control points:

- L169: `if not match or index + 1 >= len(bodies)`
- L175: `if not continuation`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
