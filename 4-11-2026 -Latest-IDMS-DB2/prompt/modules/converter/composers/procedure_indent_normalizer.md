# `converter/composers/procedure_indent_normalizer.py`

Source: [converter/composers/procedure_indent_normalizer.py](../../../../converter/composers/procedure_indent_normalizer.py) | 221 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `36c05a7459c86cd67826cecf4cd18fd1308b4244c878ae0f8c3901375c7eaa71`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Procedure Division indentation normalizer.

## Module-level bindings

`__all__` (L221)

## Import declarations

```python
from __future__ import annotations
from converter.composers.procedure_indent.indent_models import FrameStack, LineClassifier
from converter.composers.procedure_indent.indent_resolver import IndentResolver
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.procedure_indent_patterns import OTHER_DIVISION_PATTERN, PROCEDURE_DIVISION_PATTERN
from rules.procedure_indent_rules import AREA_A_INDENT, ENFORCE_PROCEDURE_INDENT, MAX_NESTING_DEPTH, PRESERVE_INDENT, PROCEDURE_INDENT_MESSAGES
```

## Local dependency notes

- [converter/composers/procedure_indent/indent_models.py](procedure_indent/indent_models.md)
- [converter/composers/procedure_indent/indent_resolver.py](procedure_indent/indent_resolver.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/procedure_indent_patterns.py](../../patterns/procedure_indent_patterns.md)
- [rules/procedure_indent_rules.py](../../rules/procedure_indent_rules.md)

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [converter/pipeline/registry.py](../pipeline/registry.md)
- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)
- [tests/test_condition_is_never_truncated.py](../../tests/test_condition_is_never_truncated.md)
- [tests/test_generic_flat_fetch_drive_normalizer.py](../../tests/test_generic_flat_fetch_drive_normalizer.md)

## Symbol contracts and control points

### `ProcedureIndentNormalizer` - L67-L219

```python
class ProcedureIndentNormalizer()
```

Depth-aware Area-B re-indentation for the PROCEDURE DIVISION.

### `ProcedureIndentNormalizer.__init__` - L70-L77

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `LineClassifier`, `IndentResolver`.

### `ProcedureIndentNormalizer.compose` - L82-L168

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `FrameStack`, `enumerate`, `self.classifier.is_untouchable`, `output.append`, `self.fixed_format.logical`, `logical.upper`, `PROCEDURE_DIVISION_PATTERN.match`, `stack.clear`, `OTHER_DIVISION_PATTERN.match`, `self.classifier.is_continuation`, `self.classifier.is_area_a_header`, `self._emit`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L85: `if not text or not ENFORCE_PROCEDURE_INDENT`
- L101: `for (number, line) in enumerate(lines, start=1)`
- L102: `if self.classifier.is_untouchable(line)`
- L107: `if not logical`
- L113: `if PROCEDURE_DIVISION_PATTERN.match(upper)`
- L120: `if OTHER_DIVISION_PATTERN.match(upper)`
- L127: `if not in_procedure`
- L133: `if self.classifier.is_continuation(upper, previous_upper)`
- Another 3 conditions/loops exist in this source span.

### `ProcedureIndentNormalizer._emit` - L173-L187

```python
_emit(self, line: str, indent: int, logical: str, output: list[str], counts: dict[str, int]) -> None
```

Observed calls (lexical order): `self._render`, `output.extend`, `len`.

Control points:

- L184: `if len(rendered) > 1`
- L186: `if rendered[0] != line`

### `ProcedureIndentNormalizer._render` - L189-L209

```python
_render(self, line: str, indent: int, logical: str) -> list[str]
```

Re-indent one statement, wrapping instead of truncating.

Observed calls (lexical order): `max`, `self.fixed_format.body`, `self.fixed_format.body(line).rstrip`, `self.fixed_format.body_fits`, `self.fixed_format.replace_body`, `self.fixed_format.replace_body_wrapped`.

Control points:

- L202: `if new_body == self.fixed_format.body(line).rstrip()`
- L205: `if self.fixed_format.body_fits(new_body)`

### `ProcedureIndentNormalizer._report` - L214-L219

```python
_report(self, counts: dict[str, int]) -> None
```

Observed calls (lexical order): `self.messages.append`, `PROCEDURE_INDENT_MESSAGES[key].format`.

Control points:

- L215: `for key in ('normalized', 'wrapped', 'preserved')`
- L216: `if counts[key]`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
