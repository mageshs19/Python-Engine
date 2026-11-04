# `converter/infrastructure/local_uploaded_file.py`

Source: [converter/infrastructure/local_uploaded_file.py](../../../../converter/infrastructure/local_uploaded_file.py) | 26 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `62da96460898b59a4667fb12875f28549652102a79c50a6b49276c17bf9c1e5a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
```

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/runner/workspace_inputs.py](../../review/runner/workspace_inputs.md)
- [runners/batch/program_converter.py](../../runners/batch/program_converter.md)
- [runners/batch/shared_input_loader.py](../../runners/batch/shared_input_loader.md)
- [runners/retrieval/retrieval_input_loader.py](../../runners/retrieval/retrieval_input_loader.md)
- [runners/retrieval/retrieval_program_converter.py](../../runners/retrieval/retrieval_program_converter.md)
- [runners/update/update_input_loader.py](../../runners/update/update_input_loader.md)
- [runners/update/update_program_converter.py](../../runners/update/update_program_converter.md)

## Symbol contracts and control points

### `LocalUploadedFile` - L4-L26

```python
class LocalUploadedFile()
```

Local file wrapper.

### `LocalUploadedFile.__init__` - L16-L21

```python
__init__(self, file_path: Path) -> None
```

Observed calls (lexical order): `Path`.

### `LocalUploadedFile.getvalue` - L23-L26

```python
getvalue(self) -> bytes
```

Observed calls (lexical order): `self.file_path.read_bytes`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
