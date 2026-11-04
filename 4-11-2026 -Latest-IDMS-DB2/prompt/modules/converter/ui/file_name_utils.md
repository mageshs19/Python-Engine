# `converter/ui/file_name_utils.py`

Source: [converter/ui/file_name_utils.py](../../../../converter/ui/file_name_utils.py) | 36 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `b8b7f85aac704d6bded0c77bdc52c5aa9bbe76b087232d70e92c81526ea55e77`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from pathlib import Path
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](conversion_actions.md)

## Symbol contracts and control points

### `build_converted_cobol_file_name` - L7-L24

```python
build_converted_cobol_file_name(target_program_id: str, source_file_name: str) -> str
```

Observed calls (lexical order): `sanitize_file_stem`, `str`, `str(source_file_name or '').strip`, `Path`.

Control points:

- L13: `if target_stem`
- L18: `if source_name`
- L21: `if source_stem`

### `sanitize_file_stem` - L27-L36

```python
sanitize_file_stem(value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `re.sub`, `text.strip`.

Control points:

- L30: `if not text`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
