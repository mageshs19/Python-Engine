# `converter/services/procedure_block_indent_service.py`

Source: [converter/services/procedure_block_indent_service.py](../../../../converter/services/procedure_block_indent_service.py) | 252 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `29ab2202d3372344d906350d7bd0064f8edd0f43bcbf4fcb9d83f5696764236e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Procedure block indent service.

## Import declarations

```python
from __future__ import annotations
from patterns.final_feedback_fix_patterns import DIVISION_PATTERN, ELSE_PATTERN, END_EVALUATE_PATTERN, END_IF_PATTERN, EVALUATE_START_PATTERN, EXEC_SQL_END_LINE_PATTERN, EXEC_SQL_START_PATTERN, IF_START_PATTERN, PARAGRAPH_PATTERN, PROCEDURE_DIVISION_PATTERN, SECTION_PATTERN, WHEN_PATTERN
from rules.cobol_statement_rules import NON_PARAGRAPH_SINGLE_WORDS
from rules.final_feedback_fix_rules import FINAL_FIX_AREA_B_INDENT, FINAL_FIX_NESTED_INDENT
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/cobol_statement_rules.py](../../rules/cobol_statement_rules.md)
- [rules/final_feedback_fix_rules.py](../../rules/final_feedback_fix_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)

## Symbol contracts and control points

### `ProcedureBlockIndentService` - L34-L252

```python
class ProcedureBlockIndentService()
```

### `ProcedureBlockIndentService.__init__` - L35-L39

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `ProcedureBlockIndentService.apply` - L41-L204

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `self.fixed_format.logical`, `str(logical or '').strip`, `stripped.upper`, `output.append`, `PROCEDURE_DIVISION_PATTERN.match`, `DIVISION_PATTERN.match`, `self.fixed_format.is_comment_or_control_line`, `self._is_area_a_header`, `EXEC_SQL_START_PATTERN.match`, `self._replace_body_when_fits`, `self._readable_body`, `self._effective_depth`, `EXEC_SQL_END_LINE_PATTERN.match`, `END_IF_PATTERN.match`.
Another 10 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L42: `if not text`
- L53: `for line in lines`
- L58: `if not stripped`
- L62: `if PROCEDURE_DIVISION_PATTERN.match(upper)`
- L69: `if not in_procedure_division`
- L73: `if DIVISION_PATTERN.match(upper) and (not PROCEDURE_DIVISION_PATTERN.match(upper))`
- L82: `if self.fixed_format.is_comment_or_control_line(line)`
- L86: `if self._is_area_a_header(upper)`
- Another 11 conditions/loops exist in this source span.

### `ProcedureBlockIndentService._effective_depth` - L206-L213

```python
_effective_depth(self, block_depth: int, evaluate_stack: list[bool]) -> int
```

Control points:

- L211: `if evaluate_stack and evaluate_stack[-1]`

### `ProcedureBlockIndentService._readable_body` - L215-L226

```python
_readable_body(self, logical: str, block_depth: int) -> str
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `max`.

### `ProcedureBlockIndentService._is_area_a_header` - L228-L241

```python
_is_area_a_header(self, logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `str(logical or '').strip().upper`, `SECTION_PATTERN.match`, `PARAGRAPH_PATTERN.match`, `upper.rstrip`.

Control points:

- L231: `if not upper`
- L234: `if SECTION_PATTERN.match(upper)`
- L237: `if PARAGRAPH_PATTERN.match(upper)`

### `ProcedureBlockIndentService._replace_body_when_fits` - L243-L252

```python
_replace_body_when_fits(self, line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `self.fixed_format.is_fixed_line`, `len`, `self.fixed_format.replace_body`.

Control points:

- L246: `if not self.fixed_format.is_fixed_line(line)`
- L249: `if len(clean_body) > self.fixed_format.BODY_WIDTH`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
