# `converter/composers/cleanup/paragraph_terminator_cleanup.py`

Source: [converter/composers/cleanup/paragraph_terminator_cleanup.py](../../../../../converter/composers/cleanup/paragraph_terminator_cleanup.py) | 227 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `9f3b3f20b039dee3f0bde4a1afb6a2ced41f068a3defca0a3617ff9554666dd3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Paragraph sentence termination cleanup.

## Import declarations

```python
import re
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from patterns.cobol_cleanup_patterns import PARAGRAPH_HEADER_PATTERN, PROCEDURE_DIVISION_LINE_PATTERN, SECTION_HEADER_PATTERN
from patterns.sequence_patterns import strip_sequence_numbers
from rules.cobol_cleanup_rules import ENFORCE_PARAGRAPH_TERMINATION, NON_PARAGRAPH_SINGLE_WORDS, PARAGRAPH_TERMINATOR
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)
- [patterns/sequence_patterns.py](../../../patterns/sequence_patterns.md)
- [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [tests/test_paragraph_terminator_area_a.py](../../../tests/test_paragraph_terminator_area_a.md)

## Symbol contracts and control points

### `ParagraphTerminatorCleanup` - L53-L227

```python
class ParagraphTerminatorCleanup()
```

### `ParagraphTerminatorCleanup.__init__` - L54-L60

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `ParagraphTerminatorCleanup._logical` - L62-L63

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `ParagraphTerminatorCleanup._is_comment_or_blank` - L65-L66

```python
_is_comment_or_blank(self, logical: str) -> bool
```

Observed calls (lexical order): `self.line_utils.is_comment_or_blank`.

### `ParagraphTerminatorCleanup.ensure_paragraph_termination` - L71-L119

```python
ensure_paragraph_termination(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._procedure_division_index`, `list`, `len`, `range`, `self._logical`, `self._is_comment_or_blank`, `self._is_continuation_operand`, `self._is_paragraph_header`, `self._terminate`, `logical.rstrip`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L72: `if not text or not ENFORCE_PARAGRAPH_TERMINATION`
- L83: `if procedure_index < 0`
- L91: `for index in range(procedure_index + 1, len(output))`
- L94: `if self._is_comment_or_blank(logical)`
- L97: `if self._is_paragraph_header(logical, output[index]) and (not self._is_continuation_operand(output, index))`
- L116: `if not changed`

### `ParagraphTerminatorCleanup._terminate` - L124-L154

```python
_terminate(self, output: list[str], index: int, paragraph: str) -> bool
```

Append the sentence terminator when it is missing.

Observed calls (lexical order): `self._logical`, `logical.endswith`, `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).rstrip`, `body.strip`, `self.messages.add`.

Control points:

- L131: `if index < 0`
- L137: `if not logical`
- L140: `if logical.endswith(PARAGRAPH_TERMINATOR)`
- L145: `if not body.strip()`

### `ParagraphTerminatorCleanup._is_continuation_operand` - L159-L184

```python
_is_continuation_operand(self, lines: list[str], index: int) -> bool
```

Recognize a continued multi-target MOVE before a one-word operand.

Observed calls (lexical order): `self._logical`, `current.endswith`, `re.fullmatch`, `self._logical(lines[index - 1]).rstrip`, `previous.endswith`, `bool`, `re.match`.

Control points:

- L169: `if index <= 0`
- L172: `if not current or not current.endswith(PARAGRAPH_TERMINATOR)`
- L174: `if not re.fullmatch('[A-Z][A-Z0-9-]*\\.', current, re.I)`
- L177: `if previous.endswith(PARAGRAPH_TERMINATOR)`

### `ParagraphTerminatorCleanup._is_paragraph_header` - L186-L215

```python
_is_paragraph_header(self, logical: str, physical_line: str='') -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `len`, `raw[:6].isdigit`, `area.lstrip`, `text.endswith`, `SECTION_HEADER_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `text.rstrip`, `text.rstrip(PARAGRAPH_TERMINATOR).upper`, `bool`.

Control points:

- L197: `if len(raw) >= 7 and raw[:6].isdigit()`
- L202: `if leading > 3`
- L205: `if not text.endswith(PARAGRAPH_TERMINATOR)`
- L208: `if SECTION_HEADER_PATTERN.match(text)`
- L211: `if not PARAGRAPH_HEADER_PATTERN.match(text)`

### `ParagraphTerminatorCleanup._procedure_division_index` - L217-L227

```python
_procedure_division_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self._logical`, `self._is_comment_or_blank`, `PROCEDURE_DIVISION_LINE_PATTERN.match`.

Control points:

- L218: `for (index, line) in enumerate(lines)`
- L221: `if self._is_comment_or_blank(logical)`
- L224: `if PROCEDURE_DIVISION_LINE_PATTERN.match(logical)`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
