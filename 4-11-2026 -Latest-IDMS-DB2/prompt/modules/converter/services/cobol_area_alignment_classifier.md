# `converter/services/cobol_area_alignment_classifier.py`

Source: [converter/services/cobol_area_alignment_classifier.py](../../../../converter/services/cobol_area_alignment_classifier.py) | 86 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `854303662cf4c2ecef96a375d39d6cf9229775e67d2eb7b40572bcafe44c0dd1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL Area A / Area B alignment classification helpers.

## Import declarations

```python
from __future__ import annotations
from patterns.final_feedback_fix_patterns import DIVISION_SECTION_HEADER_PATTERN, PARAGRAPH_HEADER_PATTERN
from rules.cobol_statement_rules import NON_PARAGRAPH_SINGLE_WORDS
```

## Local dependency notes

- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/cobol_statement_rules.py](../../rules/cobol_statement_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cobol_area_alignment_reflow.py](cobol_area_alignment_reflow.md)
- [converter/services/cobol_area_alignment_service.py](cobol_area_alignment_service.md)
- [tests/test_cobol_area_alignment_reflow.py](../../tests/test_cobol_area_alignment_reflow.md)

## Symbol contracts and control points

### `CobolAreaAlignmentClassifier` - L16-L86

```python
class CobolAreaAlignmentClassifier()
```

Classifies Procedure Division logical lines for safe Area A / continuation decisions.

### `CobolAreaAlignmentClassifier.is_area_a` - L22-L43

```python
is_area_a(self, logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `text.upper`, `DIVISION_SECTION_HEADER_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `upper.rstrip`.

Control points:

- L29: `if not text`
- L32: `if DIVISION_SECTION_HEADER_PATTERN.match(text)`
- L35: `if not PARAGRAPH_HEADER_PATTERN.match(text)`
- L40: `if statement_name in NON_PARAGRAPH_SINGLE_WORDS`

### `CobolAreaAlignmentClassifier.looks_like_continuation` - L45-L86

```python
looks_like_continuation(self, *, current_logical: str, next_logical: str) -> bool
```

Detect generic continuation lines.

Observed calls (lexical order): `str`, `str(current_logical or '').strip`, `str(current_logical or '').strip().upper`, `str(next_logical or '').strip`, `next_text.upper`, `current.endswith`, `next_text.startswith`, `next_upper.split`, `DIVISION_SECTION_HEADER_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L66: `if not current or not next_text`
- L69: `if current.endswith(('=', '>', '<', '>=', '<=', 'OR', 'AND', 'NOT'))`
- L72: `if next_text.startswith(("'", '"'))`
- L77: `if first_word in NON_PARAGRAPH_SINGLE_WORDS`
- L80: `if DIVISION_SECTION_HEADER_PATTERN.match(next_text)`
- L83: `if PARAGRAPH_HEADER_PATTERN.match(next_text)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
