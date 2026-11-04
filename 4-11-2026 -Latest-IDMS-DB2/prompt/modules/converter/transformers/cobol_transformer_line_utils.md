# `converter/transformers/cobol_transformer_line_utils.py`

Source: [converter/transformers/cobol_transformer_line_utils.py](../../../../converter/transformers/cobol_transformer_line_utils.py) | 95 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `59a5b16725499867cd68d94ae35d8ec19e704358a820146cfee055976dbe30b6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L93)

## Import declarations

```python
from __future__ import annotations
from patterns.cobol_transformer_patterns import LEFT_SEQUENCE_PATTERN, RIGHT_SEQUENCE_PATTERN, RIGHT_SEQUENCE_WITH_SPACES_PATTERN
```

## Local dependency notes

- [patterns/cobol_transformer_patterns.py](../../patterns/cobol_transformer_patterns.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_identification_transformer.py](cobol_identification_transformer.md)
- [converter/transformers/cobol_program_id_transformer.py](cobol_program_id_transformer.md)
- [converter/transformers/cobol_transformed_line_merger.py](cobol_transformed_line_merger.md)
- [converter/transformers/cobol_transformer.py](cobol_transformer.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/test_db2_code_fixes.py](../../tests/test_db2_code_fixes.md)

## Symbol contracts and control points

### `CobolTransformerLineUtils` - L10-L90

```python
class CobolTransformerLineUtils()
```

Handles COBOL logical line extraction and fixed-format body replacement.

### `CobolTransformerLineUtils.logical_line` - L18-L27

```python
logical_line(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.remove_right_sequence`, `self.remove_left_sequence`, `text.strip`.

### `CobolTransformerLineUtils.remove_left_sequence` - L29-L38

```python
remove_left_sequence(self, line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[6:].strip`.

Control points:

- L35: `if len(text) >= 6 and text[:6].strip().isdigit()`

### `CobolTransformerLineUtils.remove_right_sequence` - L40-L50

```python
remove_right_sequence(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `RIGHT_SEQUENCE_PATTERN.match`, `match.group`, `match.group('body').rstrip`.

Control points:

- L47: `if match`

### `CobolTransformerLineUtils.replace_logical_body` - L52-L90

```python
replace_logical_body(self, original_line: str, replacement_body: str) -> str
```

Observed calls (lexical order): `str`, `str(original_line or '').rstrip`, `LEFT_SEQUENCE_PATTERN.match`, `left_match.group`, `RIGHT_SEQUENCE_WITH_SPACES_PATTERN.match`, `right_match.group`, `len`, `replacement.ljust`.

Control points:

- L64: `if left_match`
- L72: `if right_match`
- L80: `if len(replacement) >= original_body_area_width`
- L87: `if left_sequence`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
