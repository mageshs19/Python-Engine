# `converter/composers/sequence_artifact_cleanup_composer.py`

Source: [converter/composers/sequence_artifact_cleanup_composer.py](../../../../converter/composers/sequence_artifact_cleanup_composer.py) | 174 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `a535f6b40b9efc1e8426056b423caad7abcfbe8e0b0765e9c7c240bba8444f0a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sequence artifact cleanup composer.

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.sequence_artifact_rules import ENFORCE_SEQUENCE_ARTIFACT_CLEANUP, PARAGRAPH_TERMINATOR, REPAIR_EXPOSED_SENTENCE, SENTENCE_CARRIERS, SEQUENCE_ARTIFACT_MESSAGES
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [rules/sequence_artifact_rules.py](../../rules/sequence_artifact_rules.md)

## Symbol contracts and control points

### `SequenceArtifactCleanupComposer` - L75-L174

```python
class SequenceArtifactCleanupComposer()
```

Drops leaked sequence-number lines and repairs the sentence.

### `SequenceArtifactCleanupComposer.__init__` - L78-L83

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `SequenceArtifactCleanupComposer.compose` - L88-L128

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self.fixed_format.is_sequence_artifact`, `output.append`, `self.messages.append`, `SEQUENCE_ARTIFACT_MESSAGES['removed'].format`, `self.fixed_format.logical`, `self._terminate_previous`, `SEQUENCE_ARTIFACT_MESSAGES['summary'].format`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L91: `if not text or not ENFORCE_SEQUENCE_ARTIFACT_CLEANUP`
- L105: `for line in lines`
- L106: `if not self.fixed_format.is_sequence_artifact(line)`
- L117: `if REPAIR_EXPOSED_SENTENCE and self._terminate_previous(output)`
- L120: `if removed`

### `SequenceArtifactCleanupComposer._terminate_previous` - L133-L174

```python
_terminate_previous(self, output: list[str]) -> bool
```

Close the sentence the removed artifact was carrying.

Observed calls (lexical order): `len`, `range`, `self.fixed_format.is_comment_or_control_line`, `self.fixed_format.logical`, `logical.endswith`, `logical.split`, `logical.split()[0].upper`, `self.fixed_format.body`, `self.fixed_format.body(line).rstrip`, `self.fixed_format.replace_body`, `self.messages.append`, `SEQUENCE_ARTIFACT_MESSAGES['terminated'].format`.

Control points:

- L140: `for index in range(len(output) - 1, -1, -1)`
- L143: `if self.fixed_format.is_comment_or_control_line(line)`
- L147: `if not logical`
- L150: `if logical.endswith(PARAGRAPH_TERMINATOR)`
- L154: `if first_word not in SENTENCE_CARRIERS`
- L163: `if rebuilt == line`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
