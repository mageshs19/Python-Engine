# `converter/composers/schema_numeric_key_guard.py`

Source: [converter/composers/schema_numeric_key_guard.py](../../../../converter/composers/schema_numeric_key_guard.py) | 93 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `ea52dfaa72229c16cf20f515837267ec2d4b2660bb5827057718578df63e244b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Guard non-numeric alphanumeric reference-modification input to DB2 numeric hosts.

## Module-level bindings

`PATTERN` (L15), `__all__` (L93)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_schema_driven_4310_generic_rules.py](../../tests/test_schema_driven_4310_generic_rules.md)

## Symbol contracts and control points

### `SchemaNumericKeyGuard` - L19-L91

```python
class SchemaNumericKeyGuard()
```

### `SchemaNumericKeyGuard.__init__` - L20-L23

```python
__init__(self, dclgen_columns=())
```

Observed calls (lexical order): `list`, `FixedFormatLineService`.

### `SchemaNumericKeyGuard._body` - L26-L29

```python
_body(line)
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].strip`, `line.lstrip`, `line.lstrip().startswith`, `line.strip`.

Control points:

- L27: `if len(line) >= 7 and line[:6].isdigit()`

### `SchemaNumericKeyGuard._numeric_host` - L31-L38

```python
_numeric_host(self, host, group)
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.to_cobol`, `len`, `found[0].cobol_picture.strip`, `found[0].cobol_picture.strip().upper`, `bool`, `re.match`.

Control points:

- L35: `if len(found) != 1`

### `SchemaNumericKeyGuard.compose` - L40-L91

```python
compose(self, text)
```

Observed calls (lexical order): `self.messages.clear`, `text.splitlines`, `self._body`, `re.match`, `m.group`, `m.group(1).upper`, `m.group(2).upper`, `text.upper`, `len`, `out.append`, `parts[-1].endswith`, `parts.append`, `' '.join`, `' '.join(parts).upper`, `PATTERN.fullmatch`, `match.groupdict`.
Another 10 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L42: `if not text`
- L46: `for line in lines`
- L48: `if re.match('^PROCEDURE\\s+DIVISION\\b', body, re.I)`
- L50: `if not in_procedure`
- L52: `if m`
- L54: `if 'PERFORM SQLERROR' not in text.upper()`
- L57: `while i < len(lines)`
- L59: `if not re.match('^MOVE\\s+', body, re.I)`
- Another 6 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
