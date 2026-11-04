# `converter/config/path_config.py`

Source: [converter/config/path_config.py](../../../../converter/config/path_config.py) | 46 lines.
Owning logic guide: [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../../11_CONFIGURATION_AND_ENTRYPOINTS.md).
Source SHA-256: `51bf00505acc07ad0dce3e3e906ea5055f213e89c3413883c0c398f3789b2ad0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Path settings for local command-line runs.

## Module-level bindings

`PROJECT_ROOT` (L13), `SRC_DIR` (L16), `LOGS_DIR` (L19), `DEFAULT_INPUT_DIR` (L22), `DEFAULT_OUTPUT_DIR` (L25), `DEFAULT_SHEET_MAPPING_PATH` (L28), `DEFAULT_RETRIEVAL_SOURCE_PATH` (L31), `DEFAULT_UPDATE_SOURCE_PATH` (L34), `DEFAULT_DCLGEN_CANDIDATE_PATHS` (L37), `DEFAULT_COPYBOOK_CANDIDATE_PATHS` (L44)

## Import declarations

```python
from pathlib import Path
```

## Change responsibility

After modifying this Python file, review [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../../11_CONFIGURATION_AND_ENTRYPOINTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
