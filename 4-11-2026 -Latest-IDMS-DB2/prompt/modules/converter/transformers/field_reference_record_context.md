# `converter/transformers/field_reference_record_context.py`

Source: [converter/transformers/field_reference_record_context.py](../../../../converter/transformers/field_reference_record_context.py) | 128 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `5c2706bfdb994425ef79f2ee1eab508cbecaa7aadfbd74112d7864b22a784efd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from patterns.field_reference_rewriter_patterns import GENERATED_OBTAIN_COMMENT_PATTERN, INITIALIZE_DCL_PATTERN, MOVE_SPACES_TO_RECORD_PATTERN, PARAGRAPH_PATTERN, QUALIFIED_REFERENCE_PATTERN
```

## Local dependency notes

- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/field_reference_rewriter_patterns.py](../../patterns/field_reference_rewriter_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference_rewriter.py](field_reference_rewriter.md)

## Symbol contracts and control points

### `FieldReferenceRecordContext` - L13-L128

```python
class FieldReferenceRecordContext()
```

Detects active record context for safe bare field rewriting.

### `FieldReferenceRecordContext.__init__` - L18-L25

```python
__init__(self, *, record_field_map: dict[str, dict[str, str]], group_record_map: dict[str, str]) -> None
```

### `FieldReferenceRecordContext.detect_active_record_from_line` - L27-L50

```python
detect_active_record_from_line(self, *, logical_line: str, current_active_record: str) -> str
```

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `detector`.

Control points:

- L35: `if not logical`
- L38: `for detector in [self.record_from_paragraph, self.record_from_initialize, self.record_from_generated_comment, self.record_from_move_target, self.record_from_qualified_reference]`
- L47: `if record`

### `FieldReferenceRecordContext.record_from_paragraph` - L52-L67

```python
record_from_paragraph(self, logical_line: str) -> str
```

Observed calls (lexical order): `PARAGRAPH_PATTERN.match`, `NameNormalizer.normalize`, `match.group`.

Control points:

- L58: `if not match`
- L63: `for record in self.record_field_map`
- L64: `if record and record in paragraph`

### `FieldReferenceRecordContext.record_from_initialize` - L69-L80

```python
record_from_initialize(self, logical_line: str) -> str
```

Observed calls (lexical order): `INITIALIZE_DCL_PATTERN.search`, `NameNormalizer.normalize`, `match.group`, `self.group_record_map.get`.

Control points:

- L75: `if not match`

### `FieldReferenceRecordContext.record_from_generated_comment` - L82-L96

```python
record_from_generated_comment(self, logical_line: str) -> str
```

Observed calls (lexical order): `GENERATED_OBTAIN_COMMENT_PATTERN.search`, `NameNormalizer.normalize`, `match.group`.

Control points:

- L88: `if not match`
- L93: `if record in self.record_field_map`

### `FieldReferenceRecordContext.record_from_move_target` - L98-L112

```python
record_from_move_target(self, logical_line: str) -> str
```

Observed calls (lexical order): `MOVE_SPACES_TO_RECORD_PATTERN.search`, `NameNormalizer.normalize`, `match.group`.

Control points:

- L104: `if not match`
- L109: `if record in self.record_field_map`

### `FieldReferenceRecordContext.record_from_qualified_reference` - L114-L128

```python
record_from_qualified_reference(self, logical_line: str) -> str
```

Observed calls (lexical order): `QUALIFIED_REFERENCE_PATTERN.search`, `NameNormalizer.normalize`, `match.group`.

Control points:

- L120: `if not match`
- L125: `if record in self.record_field_map`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
