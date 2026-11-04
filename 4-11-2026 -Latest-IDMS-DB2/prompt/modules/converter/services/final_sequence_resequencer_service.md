# `converter/services/final_sequence_resequencer_service.py`

Source: [converter/services/final_sequence_resequencer_service.py](../../../../converter/services/final_sequence_resequencer_service.py) | 210 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `7406b4098a2ff13e82c6dcd323865856e0c95846825771115aa128c6258a540e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Final sequence resequencer service.

## Import declarations

```python
from __future__ import annotations
from rules.fixed_format_rules import DEFAULT_LEFT_START, DEFAULT_LEFT_STEP, DEFAULT_RIGHT_START, DEFAULT_RIGHT_STEP, TOTAL_WIDTH
```

## Local dependency notes

- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)
- [converter/pipeline/conversion/conversion_layout_steps.py](../pipeline/conversion/conversion_layout_steps.md)
- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [converter/services/final_generated_output_service.py](final_generated_output_service.md)

## Symbol contracts and control points

### `FinalSequenceResequencerService` - L27-L210

```python
class FinalSequenceResequencerService()
```

Resequences final manual-style COBOL output.

Declared class/data-model fields:

```python
LEFT_START = 0
LEFT_END = 6
RIGHT_START = 72
RIGHT_END = 80
```

### `FinalSequenceResequencerService.resequence` - L46-L103

```python
resequence(self, text: str, left_start: int=DEFAULT_LEFT_START, left_step: int=DEFAULT_LEFT_STEP, right_start: int=DEFAULT_RIGHT_START, right_step: int=DEFAULT_RIGHT_STEP) -> str
```

Observed calls (lexical order): `str`, `int`, `source.splitlines`, `self._is_fixed_format_line`, `output.append`, `self._replace_sequence`, `line.strip`, `self._format_blank_line`, `self._is_cobol_line`, `self._format_and_sequence`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L56: `if not source`
- L63: `for line in source.splitlines()`
- L65: `if self._is_fixed_format_line(line)`
- L76: `if not line.strip()`
- L87: `if self._is_cobol_line(line)`

### `FinalSequenceResequencerService._is_fixed_format_line` - L105-L120

```python
_is_fixed_format_line(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[self.LEFT_START:self.LEFT_END].isdigit`, `text[self.RIGHT_START:self.RIGHT_END].isdigit`.

Control points:

- L111: `if len(text) != TOTAL_WIDTH`
- L114: `if not text[self.LEFT_START:self.LEFT_END].isdigit()`
- L117: `if not text[self.RIGHT_START:self.RIGHT_END].isdigit()`

### `FinalSequenceResequencerService._is_cobol_line` - L122-L137

```python
_is_cobol_line(self, line: str) -> bool
```

Check if line is a COBOL statement or comment that needs formatting.

Observed calls (lexical order): `str`, `text.strip`, `len`.

Control points:

- L130: `if not text.strip()`
- L134: `if len(text) < TOTAL_WIDTH`

### `FinalSequenceResequencerService._format_blank_line` - L139-L152

```python
_format_blank_line(self, left_value: int, right_value: int) -> str
```

Format a blank line as 80 chars with sequence numbers.

### `FinalSequenceResequencerService._format_and_sequence` - L154-L193

```python
_format_and_sequence(self, line: str, left_value: int, right_value: int) -> str
```

Format unformatted COBOL line to 80 chars with sequence numbers.

Observed calls (lexical order): `str`, `text.rstrip`, `code_content.startswith`, `len`, `code_content.ljust`.

Control points:

- L169: `if code_content.startswith('*')`
- L174: `if code_content.startswith('/')`
- L186: `if len(code_content) < code_area_width - 1`

### `FinalSequenceResequencerService._replace_sequence` - L195-L210

```python
_replace_sequence(self, line: str, left_value: int, right_value: int) -> str
```

Observed calls (lexical order): `str`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
