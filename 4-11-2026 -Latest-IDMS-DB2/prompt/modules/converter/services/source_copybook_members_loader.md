# `converter/services/source_copybook_members_loader.py`

Source: [converter/services/source_copybook_members_loader.py](../../../../converter/services/source_copybook_members_loader.py) | 12 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `09eb317d6a6e1fc5d893a223a1844f0790a6a4cc156fdbc289d5f473518d7538`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Configured source copybook metadata, with no program-specific paths.

## Import declarations

```python
from __future__ import annotations
from config.path_settings import copybook_paths
```

## Local dependency notes

- [config/path_settings.py](../../config/path_settings.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch/program_converter.py](../../runners/batch/program_converter.md)
- [runners/retrieval/retrieval_program_converter.py](../../runners/retrieval/retrieval_program_converter.md)

## Symbol contracts and control points

### `read_source_copybook_members` - L7-L12

```python
read_source_copybook_members() -> dict[str, str]
```

Observed calls (lexical order): `copybook_paths`, `path.read_text`, `path.stem.upper`.

Control points:

- L9: `for path in copybook_paths()`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
