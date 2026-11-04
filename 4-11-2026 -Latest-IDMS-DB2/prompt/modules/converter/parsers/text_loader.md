# `converter/parsers/text_loader.py`

Source: [converter/parsers/text_loader.py](../../../../converter/parsers/text_loader.py) | 12 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `ef1e78869e786015dabc40498dd9764312fef79bd789381f9fa3ea8001a4a7bf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.infrastructure.file_loader import FileLoader
```

## Local dependency notes

- [converter/infrastructure/file_loader.py](../infrastructure/file_loader.md)

## Symbol contracts and control points

### `TextLoader` - L4-L12

```python
class TextLoader(FileLoader)
```

Backward-compatible alias for FileLoader.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
