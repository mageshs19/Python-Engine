# `converter/parsers/dclgen/sql_name_normalizer.py`

Source: [converter/parsers/dclgen/sql_name_normalizer.py](../../../../../converter/parsers/dclgen/sql_name_normalizer.py) | 46 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `a6fd35539469ab65eeacbd01902399a4889954c6cc480719a835defb044a9597`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DCLGEN SQL / COBOL name normalization helpers.

## Import declarations

```python
from __future__ import annotations
from patterns.dclgen_patterns import MULTIPLE_UNDERSCORE_PATTERN, SQL_NAME_CLEANUP_PATTERN
```

## Local dependency notes

- [patterns/dclgen_patterns.py](../../../patterns/dclgen_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/dclgen_parser.py](../dclgen_parser.md)

## Symbol contracts and control points

### `DclgenNameNormalizer` - L14-L46

```python
class DclgenNameNormalizer()
```

### `DclgenNameNormalizer.normalize_sql_name` - L15-L27

```python
normalize_sql_name(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `text.strip`, `text.strip('"').strip`, `text.strip('>').strip`, `text.strip('>').strip('[').strip`, `text.split`, `text.replace`, `SQL_NAME_CLEANUP_PATTERN.sub`, `text.upper`, `MULTIPLE_UNDERSCORE_PATTERN.sub`.

Control points:

- L20: `if '.' in text`

### `DclgenNameNormalizer.normalize_cobol_name_to_db2` - L29-L35

```python
normalize_cobol_name_to_db2(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `text.replace`, `SQL_NAME_CLEANUP_PATTERN.sub`, `MULTIPLE_UNDERSCORE_PATTERN.sub`, `text.strip`.

### `DclgenNameNormalizer.normalize_compare_name` - L37-L46

```python
normalize_compare_name(self, value: str) -> str
```

Observed calls (lexical order): `self.normalize_cobol_name_to_db2`, `text.startswith`.

Control points:

- L40: `if text.startswith('DCL_')`
- L43: `if text.startswith('DCL')`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
