# `converter/parsers/dclgen/cobol_host_field_parser.py`

Source: [converter/parsers/dclgen/cobol_host_field_parser.py](../../../../../converter/parsers/dclgen/cobol_host_field_parser.py) | 83 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `de7cbc211bb905a785da0932cc2636679a5dc1bf1cea44e1a0bcab002c452179`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Parses COBOL host fields (PIC / USAGE) from DCLGEN text.

## Import declarations

```python
from __future__ import annotations
from patterns.dclgen_patterns import COBOL_FIELD_PATTERN, COBOL_GROUP_PATTERN, DCLGEN_PIC_PATTERN, DCLGEN_USAGE_PATTERN
```

## Local dependency notes

- [patterns/dclgen_patterns.py](../../../patterns/dclgen_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/dclgen_parser.py](../dclgen_parser.md)

## Symbol contracts and control points

### `CobolHostFieldParser` - L16-L83

```python
class CobolHostFieldParser()
```

### `CobolHostFieldParser.__init__` - L17-L18

```python
__init__(self, diagnostics: list[str]) -> None
```

### `CobolHostFieldParser.parse` - L20-L71

```python
parse(self, text: str, source_label: str) -> list[dict[str, str]]
```

Observed calls (lexical order): `text.splitlines`, `raw_line.rstrip`, `COBOL_GROUP_PATTERN.match`, `group_match.group`, `group_match.group(1).upper`, `COBOL_FIELD_PATTERN.match`, `match.group`, `match.group(2).upper`, `name.upper`, `name.upper().endswith`, `self._picture`, `self._usage`, `fields.append`, `self.diagnostics.append`, `len`.

Control points:

- L29: `for raw_line in text.splitlines()`
- L33: `if group_match`
- L38: `if not seen_group`
- L42: `if not match`
- L53: `if not pic and (not usage)`

### `CobolHostFieldParser._picture` - L73-L77

```python
_picture(self, text: str) -> str
```

Observed calls (lexical order): `DCLGEN_PIC_PATTERN.search`, `str`, `match.group`, `match.group('pic').strip`, `match.group('pic').strip().upper`.

Control points:

- L75: `if not match`

### `CobolHostFieldParser._usage` - L79-L83

```python
_usage(self, text: str) -> str
```

Observed calls (lexical order): `DCLGEN_USAGE_PATTERN.search`, `str`, `match.group`, `match.group(1).strip`, `match.group(1).strip().upper`.

Control points:

- L81: `if not match`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
