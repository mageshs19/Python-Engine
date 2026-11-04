# `converter/services/cobol_area_alignment_reflow.py`

Source: [converter/services/cobol_area_alignment_reflow.py](../../../../converter/services/cobol_area_alignment_reflow.py) | 235 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `8539b18fab3e5114ee8e4af86a176148d4cdda2f5c6a1ae9d8b2c41fb292bfd3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL Area B safe two-line reflow helper.

## Module-level bindings

`STATEMENT_KEYWORDS` (L65), `DIVISION_TOKENS` (L74)

## Import declarations

```python
from __future__ import annotations
from converter.services.cobol_area_alignment_classifier import CobolAreaAlignmentClassifier
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.final_feedback_fix_rules import AREA_B_CONTINUATION_BODY_INDENT
```

## Local dependency notes

- [converter/services/cobol_area_alignment_classifier.py](cobol_area_alignment_classifier.md)
- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [rules/final_feedback_fix_rules.py](../../rules/final_feedback_fix_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cobol_area_alignment_service.py](cobol_area_alignment_service.md)
- [tests/test_cobol_area_alignment_reflow.py](../../tests/test_cobol_area_alignment_reflow.md)

## Symbol contracts and control points

### `CobolAreaAlignmentReflow` - L77-L235

```python
class CobolAreaAlignmentReflow()
```

Re-indents a two-line statement without ever truncating it.

### `CobolAreaAlignmentReflow.__init__` - L80-L87

```python
__init__(self, *, fixed_format: FixedFormatLineService, classifier: CobolAreaAlignmentClassifier) -> None
```

### `CobolAreaAlignmentReflow.try_reflow_with_next_line` - L92-L153

```python
try_reflow_with_next_line(self, *, current_line: str, next_line: str, first_indent: str) -> list[str]
```

Re-indent a statement that spans the current and next lines.

Observed calls (lexical order): `self.fixed_format.is_fixed_line`, `self._is_continuation_fragment`, `self.fixed_format.logical`, `str`, `self.fixed_format.body_fits`, `self._render`, `f'{current_logical} {next_logical}'.strip`, `self.fixed_format.wrap_body_lines`, `len`.

Control points:

- L105: `if not current_line or not next_line`
- L108: `if not self.fixed_format.is_fixed_line(current_line)`
- L111: `if not self.fixed_format.is_fixed_line(next_line)`
- L114: `if not self._is_continuation_fragment(next_line)`
- L120: `if not current_logical or not next_logical`
- L133: `if self.fixed_format.body_fits(first_body) and self.fixed_format.body_fits(second_body)`
- L149: `if len(bodies) != 2`

### `CobolAreaAlignmentReflow._render` - L158-L189

```python
_render(self, current_line: str, next_line: str, first_body: str, second_body: str) -> list[str]
```

Rebuild both lines, or refuse if either will not assemble.

Observed calls (lexical order): `self.fixed_format.split`, `self.fixed_format.build_or_none`.

Control points:

- L186: `if first is None or second is None`

### `CobolAreaAlignmentReflow._is_continuation_fragment` - L194-L235

```python
_is_continuation_fragment(self, line: str) -> bool
```

True when `line` is the tail of the statement above it.

Observed calls (lexical order): `self.fixed_format.is_comment_or_control_line`, `self.fixed_format.is_sequence_artifact`, `self.fixed_format.logical`, `logical.upper`, `upper.split`, `len`, `upper.endswith`, `upper.startswith`, `any`, `words[0].rstrip`.

Control points:

- L202: `if self.fixed_format.is_comment_or_control_line(line)`
- L205: `if self.fixed_format.is_sequence_artifact(line)`
- L209: `if not logical`
- L216: `if upper == '.'`
- L220: `if len(words) == 1 and upper.endswith('.')`
- L224: `if upper.startswith('END-')`
- L228: `if any((token in words for token in DIVISION_TOKENS))`
- L232: `if words and words[0].rstrip('.') in STATEMENT_KEYWORDS`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
