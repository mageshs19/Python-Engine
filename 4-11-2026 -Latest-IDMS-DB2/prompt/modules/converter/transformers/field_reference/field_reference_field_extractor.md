# `converter/transformers/field_reference/field_reference_field_extractor.py`

Source: [converter/transformers/field_reference/field_reference_field_extractor.py](../../../../../converter/transformers/field_reference/field_reference_field_extractor.py) | 55 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `a1ea6875103c2daa8d879d59635b7b6d417e726466ea6f0331f0e35dad23859d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from patterns.field_reference_rewriter_patterns import COBOL_IDENTIFIER_PATTERN, LEVEL_NUMBER_FIELD_PATTERN, REDEFINES_BASE_PATTERN, REDEFINES_FIELD_PATTERN
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/field_reference_rewriter_patterns.py](../../../patterns/field_reference_rewriter_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference_context_builder.py](../field_reference_context_builder.md)

## Symbol contracts and control points

### `FieldReferenceFieldExtractor` - L12-L55

```python
class FieldReferenceFieldExtractor()
```

Pure text helpers for extracting COBOL field names and keys.

### `FieldReferenceFieldExtractor.extract_field_name` - L19-L38

```python
extract_field_name(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `text.replace`, `LEVEL_NUMBER_FIELD_PATTERN.match`, `level_match.group`, `REDEFINES_FIELD_PATTERN.match`, `redefines_match.group`, `COBOL_IDENTIFIER_PATTERN.findall`.

Control points:

- L21: `if not text`
- L27: `if level_match`
- L31: `if redefines_match`
- L35: `if not tokens`

### `FieldReferenceFieldExtractor.extract_redefines_base` - L40-L45

```python
extract_redefines_base(self, value: str) -> str
```

Observed calls (lexical order): `str`, `REDEFINES_BASE_PATTERN.search`, `match.group`.

Control points:

- L43: `if not match`

### `FieldReferenceFieldExtractor.field_key` - L47-L48

```python
field_key(self, value: str) -> str
```

Observed calls (lexical order): `NameNormalizer.to_cobol`.

### `FieldReferenceFieldExtractor.first_non_empty` - L50-L55

```python
first_non_empty(self, *values: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`.

Control points:

- L51: `for value in values`
- L53: `if text`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
