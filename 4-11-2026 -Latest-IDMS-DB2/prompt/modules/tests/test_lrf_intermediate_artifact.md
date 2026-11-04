# `tests/test_lrf_intermediate_artifact.py`

Source: [tests/test_lrf_intermediate_artifact.py](../../../tests/test_lrf_intermediate_artifact.py) | 43 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `91aea8e4a41e197f70d40fa4788a8e3846f5d1c2c2d5460cf052e28fbfa7c33b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The LRF-to-ordinary-IDMS stage is persisted as an inspectable artifact.

## Import declarations

```python
from pathlib import Path
from converter.domain.models import ConversionInput
from converter.pipeline.conversion.conversion_pipeline import ConversionPipeline
import converter.pipeline.conversion.conversion_pipeline as module
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/pipeline/conversion/conversion_pipeline.py](../converter/pipeline/conversion/conversion_pipeline.md)

## Symbol contracts and control points

### `test_lrf_intermediate_is_written_to_configured_directory` - L8-L21

```python
test_lrf_intermediate_is_written_to_configured_directory(monkeypatch, tmp_path)
```

Observed calls (lexical order): `monkeypatch.setenv`, `str`, `monkeypatch.delenv`, `ConversionInput`, `ConversionPipeline._dump_expanded`, `artifact.is_file`, `artifact.read_text`.

### `test_lrf_intermediate_sanitizes_program_id` - L24-L31

```python
test_lrf_intermediate_sanitizes_program_id(monkeypatch, tmp_path)
```

Observed calls (lexical order): `monkeypatch.setenv`, `str`, `monkeypatch.delenv`, `ConversionInput`, `ConversionPipeline._dump_expanded`, `(tmp_path / 'BAD_PROGRAM_ID_lrf_to_idms.cbl').read_text`.

### `test_default_intermediate_folder_is_mainframe_output_lrf` - L34-L43

```python
test_default_intermediate_folder_is_mainframe_output_lrf(monkeypatch)
```

Guard the agreed output location when no override is configured.

Observed calls (lexical order): `monkeypatch.delenv`, `Path`, `Path(module.__file__).resolve`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
