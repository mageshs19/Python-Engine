# `converter/composers/output_write_paragraph_composer.py`

Source: [converter/composers/output_write_paragraph_composer.py](../../../../converter/composers/output_write_paragraph_composer.py) | 124 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `fcf63dc50116b7771fc942fd27288d87d8f2e99799ef52476bceef7ed3fd23b9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L124)

## Import declarations

```python
from __future__ import annotations
from converter.composers.output_write.output_write_block_finder import OutputWriteBlockFinder
from converter.composers.output_write.output_write_eligibility import OutputWriteEligibility
from converter.composers.output_write.output_write_extractor import OutputWriteExtractor
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from converter.composers.output_write.output_write_scanner import OutputWriteScanner
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.output_write_paragraph_rules import EMIT_OUTPUT_COUNTER_INCREMENT, ENFORCE_OUTPUT_WRITE_PARAGRAPH, EXTRACTION_PASS_LIMIT, OUTPUT_COUNTER_NAME, OUTPUT_WRITE_PARAGRAPH_MESSAGES
from rules.structural_safety_rules import ENFORCE_CONDITION_INTEGRITY, STRUCTURAL_SAFETY_MESSAGES
```

## Local dependency notes

- [converter/composers/output_write/output_write_block_finder.py](output_write/output_write_block_finder.md)
- [converter/composers/output_write/output_write_eligibility.py](output_write/output_write_eligibility.md)
- [converter/composers/output_write/output_write_extractor.py](output_write/output_write_extractor.md)
- [converter/composers/output_write/output_write_line_utils.py](output_write/output_write_line_utils.md)
- [converter/composers/output_write/output_write_scanner.py](output_write/output_write_scanner.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [rules/output_write_paragraph_rules.py](../../rules/output_write_paragraph_rules.md)
- [rules/structural_safety_rules.py](../../rules/structural_safety_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/registry.py](../pipeline/registry.md)
- [tests/output_write/conftest.py](../../tests/output_write/conftest.md)
- [tests/output_write/test_perform_thru_helper_safety.py](../../tests/output_write/test_perform_thru_helper_safety.md)
- [tests/test_condition_scanner_measures_multiline.py](../../tests/test_condition_scanner_measures_multiline.md)
- [tests/test_output_write_paragraph_composer.py](../../tests/test_output_write_paragraph_composer.md)

## Symbol contracts and control points

### `OutputWriteParagraphComposer` - L34-L121

```python
class OutputWriteParagraphComposer()
```

### `OutputWriteParagraphComposer.__init__` - L36-L48

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `OutputWriteLineUtils`, `FixedFormatLineService`, `OutputWriteScanner`, `OutputWriteBlockFinder`, `OutputWriteEligibility`, `OutputWriteExtractor`.

### `OutputWriteParagraphComposer.compose` - L50-L67

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `range`, `self._extract_once`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L53: `if not text or not ENFORCE_OUTPUT_WRITE_PARAGRAPH`
- L63: `for _pass in range(EXTRACTION_PASS_LIMIT)`
- L64: `if not self._extract_once(lines)`

### `OutputWriteParagraphComposer._extract_once` - L69-L93

```python
_extract_once(self, lines: list[str]) -> bool
```

Observed calls (lexical order): `self.lines.paragraph_names`, `self.finder.candidates`, `self.eligibility.assess`, `self._log`, `self._condition_unresolved`, `accepted.append`, `max`, `self.extractor.apply`, `self._log_success`.

Control points:

- L73: `for block in self.finder.candidates(lines)`
- L76: `if plan is None`
- L77: `if refusal is not None and refusal.is_reportable`
- L81: `if self._condition_unresolved(block)`
- L86: `if not accepted`

### `OutputWriteParagraphComposer._condition_unresolved` - L95-L106

```python
_condition_unresolved(self, block) -> bool
```

Observed calls (lexical order): `STRUCTURAL_SAFETY_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L96: `if not ENFORCE_CONDITION_INTEGRITY`
- L98: `if block.has_resolved_condition`
- L104: `if template`

### `OutputWriteParagraphComposer._log_success` - L108-L116

```python
_log_success(self, source: str, paragraph: str) -> None
```

Observed calls (lexical order): `self._log`.

Control points:

- L111: `if EMIT_OUTPUT_COUNTER_INCREMENT`

### `OutputWriteParagraphComposer._log` - L118-L121

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `OUTPUT_WRITE_PARAGRAPH_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L120: `if template`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
