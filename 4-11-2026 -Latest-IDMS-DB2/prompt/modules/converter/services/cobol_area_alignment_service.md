# `converter/services/cobol_area_alignment_service.py`

Source: [converter/services/cobol_area_alignment_service.py](../../../../converter/services/cobol_area_alignment_service.py) | 188 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `aa2973fe6ad367152e8488746e13940b9812938face4025004066ff54dc9ef8c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL Area A / Area B alignment service.

## Import declarations

```python
from __future__ import annotations
from patterns.final_feedback_fix_patterns import END_EXEC_PATTERN, EXEC_SQL_START_PATTERN, PROCEDURE_DIVISION_TOKEN_PATTERN
from rules.final_feedback_fix_rules import AREA_B_BODY_INDENT, SQL_BODY_INDENT
from converter.services.cobol_area_alignment_classifier import CobolAreaAlignmentClassifier
from converter.services.cobol_area_alignment_reflow import CobolAreaAlignmentReflow
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/cobol_area_alignment_classifier.py](cobol_area_alignment_classifier.md)
- [converter/services/cobol_area_alignment_reflow.py](cobol_area_alignment_reflow.md)
- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/final_feedback_fix_rules.py](../../rules/final_feedback_fix_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)
- [converter/generators/boilerplate_generator.py](../generators/boilerplate_generator.md)

## Symbol contracts and control points

### `CobolAreaAlignmentService` - L38-L188

```python
class CobolAreaAlignmentService()
```

Aligns generated Procedure Division executable statements to Area B.

### `CobolAreaAlignmentService.__init__` - L53-L62

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `CobolAreaAlignmentClassifier`, `CobolAreaAlignmentReflow`.

### `CobolAreaAlignmentService.align` - L64-L161

```python
align(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).splitlines`, `len`, `self.fixed_format.logical`, `PROCEDURE_DIVISION_TOKEN_PATTERN.search`, `output.append`, `self.fixed_format.is_comment_or_control_line`, `EXEC_SQL_START_PATTERN.match`, `self._replace_body_when_safe`, `END_EXEC_PATTERN.search`, `self.classifier.is_area_a`, `self._body_fits`, `self.fixed_format.replace_body`, `self.reflow.try_reflow_with_next_line`, `output.extend`, `'\n'.join`.

Control points:

- L65: `if not text`
- L75: `while index < len(lines)`
- L79: `if PROCEDURE_DIVISION_TOKEN_PATTERN.search(logical)`
- L85: `if not in_procedure_division`
- L90: `if self.fixed_format.is_comment_or_control_line(line)`
- L95: `if not logical`
- L100: `if EXEC_SQL_START_PATTERN.match(logical)`
- L111: `if in_exec_sql`
- Another 4 conditions/loops exist in this source span.

### `CobolAreaAlignmentService._replace_body_when_safe` - L163-L182

```python
_replace_body_when_safe(self, *, line: str, new_body: str) -> str
```

Replace fixed-format body only when it will not truncate.

Observed calls (lexical order): `self.fixed_format.is_fixed_line`, `self.fixed_format.replace_body`, `self._body_fits`.

Control points:

- L176: `if not self.fixed_format.is_fixed_line(line)`
- L179: `if not self._body_fits(new_body)`

### `CobolAreaAlignmentService._body_fits` - L184-L188

```python
_body_fits(self, body: str) -> bool
```

Observed calls (lexical order): `len`, `str`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
