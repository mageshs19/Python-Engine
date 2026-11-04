# `converter/composers/unnecessary_comments_cleanup_composer.py`

Source: [converter/composers/unnecessary_comments_cleanup_composer.py](../../../../converter/composers/unnecessary_comments_cleanup_composer.py) | 209 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `3769ada1d2f680877b66f1559a57f7f7db75e958c96103583a83413ff0b42290`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Composer that applies unnecessary comments cleanup to generated COBOL.

## Module-level bindings

`__all__` (L209)

## Import declarations

```python
from __future__ import annotations
import re
from converter.transformers.unnecessary_comments_cleanup import UnnecessaryCommentsCleanup
from patterns.cobol_cleanup_patterns import GENERATED_DB2_NARRATION_COMMENT_PATTERN, GENERATED_DB2_NARRATION_CONTINUATION_PATTERN, RESIDUAL_IDMS_COMMENT_PATTERN, TRACE_MARKER_COMMENT_PATTERN
from patterns.sequence_patterns import strip_sequence_numbers
from rules.unnecessary_comments_rules import MARKER_CLEANUP_MESSAGE, REMOVE_NOISE_MARKERS, REMOVE_TRACE_MARKERS
```

## Local dependency notes

- [converter/transformers/unnecessary_comments_cleanup.py](../transformers/unnecessary_comments_cleanup.md)
- [patterns/cobol_cleanup_patterns.py](../../patterns/cobol_cleanup_patterns.md)
- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [rules/unnecessary_comments_rules.py](../../rules/unnecessary_comments_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/pipeline/registry.py](../pipeline/registry.md)
- [converter/services/final_generated_output_service.py](../services/final_generated_output_service.md)
- [tests/test_generated_output_final_formatting.py](../../tests/test_generated_output_final_formatting.md)

## Symbol contracts and control points

### `UnnecessaryCommentsCleanupComposer` - L42-L206

```python
class UnnecessaryCommentsCleanupComposer()
```

Removes unnecessary comment blocks from COBOL programs.

### `UnnecessaryCommentsCleanupComposer.__init__` - L57-L59

```python
__init__(self) -> None
```

Observed calls (lexical order): `UnnecessaryCommentsCleanup`.

### `UnnecessaryCommentsCleanupComposer.compose` - L64-L73

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `self._remove_marker_comments`, `self._remove_comment_blocks`.

Control points:

- L68: `if not source`

### `UnnecessaryCommentsCleanupComposer.cleanup_generated_narration` - L75-L117

```python
cleanup_generated_narration(self, text: str) -> str
```

Remove only converter narration comments from final generated text.

Observed calls (lexical order): `str`, `source.splitlines`, `UnnecessaryCommentsCleanup.DB2_KEEP_PATTERN.search`, `output.append`, `self._logical`, `GENERATED_DB2_NARRATION_COMMENT_PATTERN.match`, `re.match`, `GENERATED_DB2_NARRATION_CONTINUATION_PATTERN.match`, `MARKER_CLEANUP_MESSAGE.format`, `self.messages.append`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L84: `if not source`
- L90: `for line in source.splitlines()`
- L91: `if UnnecessaryCommentsCleanup.DB2_KEEP_PATTERN.search(line)`
- L102: `if re.match('^\\*\\s*DB2:\\s*', logical, re.IGNORECASE) or GENERATED_DB2_NARRATION_COMMENT_PATTERN.match(logical)`
- L107: `if skip_generated_continuation`
- L108: `if GENERATED_DB2_NARRATION_CONTINUATION_PATTERN.match(logical)`
- L115: `if removed`

### `UnnecessaryCommentsCleanupComposer._remove_marker_comments` - L122-L179

```python
_remove_marker_comments(self, text: str) -> str
```

Drop generated *DB2: marker comments.

Observed calls (lexical order): `str`, `str(text or '').split`, `UnnecessaryCommentsCleanup.DB2_KEEP_PATTERN.search`, `output.append`, `self._logical`, `GENERATED_DB2_NARRATION_COMMENT_PATTERN.match`, `GENERATED_DB2_NARRATION_CONTINUATION_PATTERN.match`, `RESIDUAL_IDMS_COMMENT_PATTERN.match`, `TRACE_MARKER_COMMENT_PATTERN.match`, `MARKER_CLEANUP_MESSAGE.format`, `self.messages.append`, `'\n'.join`.

Control points:

- L144: `for line in lines`
- L146: `if UnnecessaryCommentsCleanup.DB2_KEEP_PATTERN.search(line)`
- L153: `if GENERATED_DB2_NARRATION_COMMENT_PATTERN.match(logical)`
- L158: `if skip_generated_continuation`
- L159: `if GENERATED_DB2_NARRATION_CONTINUATION_PATTERN.match(logical)`
- L166: `if REMOVE_NOISE_MARKERS and RESIDUAL_IDMS_COMMENT_PATTERN.match(logical)`
- L170: `if REMOVE_TRACE_MARKERS and TRACE_MARKER_COMMENT_PATTERN.match(logical)`
- L176: `if removed`

### `UnnecessaryCommentsCleanupComposer._remove_comment_blocks` - L184-L198

```python
_remove_comment_blocks(self, text: str) -> str
```

Hand off to UnnecessaryCommentsCleanup.

Observed calls (lexical order): `self.cleanup.apply`, `isinstance`, `self.messages.extend`, `str`.

Control points:

- L193: `if isinstance(result, tuple)`

### `UnnecessaryCommentsCleanupComposer._logical` - L204-L206

```python
_logical(line: str) -> str
```

Body only, sequence areas removed.

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
