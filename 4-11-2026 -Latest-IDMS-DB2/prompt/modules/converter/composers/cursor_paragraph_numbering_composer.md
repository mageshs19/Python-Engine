# `converter/composers/cursor_paragraph_numbering_composer.py`

Source: [converter/composers/cursor_paragraph_numbering_composer.py](../../../../converter/composers/cursor_paragraph_numbering_composer.py) | 41 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `b0d13be5eee74463c260bff4535312c59b240a1eaa18afc30f29602429220eb3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renumber cursor-operation paragraphs without restructuring COBOL control flow.

## Import declarations

```python
from __future__ import annotations
from converter.composers.lifecycle_standardization_composer import LifecycleStandardizationComposer
```

## Local dependency notes

- [converter/composers/lifecycle_standardization_composer.py](lifecycle_standardization_composer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/pipeline/test_single_owner_transformations.py](../../tests/pipeline/test_single_owner_transformations.md)

## Symbol contracts and control points

### `CursorParagraphNumberingComposer` - L16-L41

```python
class CursorParagraphNumberingComposer(LifecycleStandardizationComposer)
```

Apply only the shared cursor numbering rule; never wrap the mainline.

### `CursorParagraphNumberingComposer.compose` - L19-L41

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `source.splitlines`, `self._normalize_cursor_paragraph_numbers`, `self.messages.append`, `'\n'.join`, `source.endswith`.

Control points:

- L22: `if not source`
- L32: `if normalized == lines`
- L39: `if source.endswith(('\n', '\r'))`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
