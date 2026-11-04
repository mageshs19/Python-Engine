# `mainframe/__init__.py`

Source: [mainframe/__init__.py](../../../mainframe/__init__.py) | 48 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `27eb895a6be8ec6a29fe160772f4e1f8d8825f9c8b3b8070567447785ba8adec`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Zowe input source for the IDMS to DB2 conversion pipeline.

## Module-level bindings

`__all__` (L29)

## Import declarations

```python
from __future__ import annotations
from mainframe.zowe_fetcher import ZoweFetcher, fetch_zowe_inputs
from mainframe.zowe_libraries import LibrarySearch, application_code, libraries_for
from mainframe.zowe_programs import selected_programs
from mainframe.zowe_resolver import ProgramDependencies, dclgen_member_for, resolve_dependencies
from mainframe.zowe_settings import ArtifactProfile, ZoweConnection, artifact_connection, build_output_profile, build_profiles
from mainframe.zowe_workspace import ensure_workspace, workspace_root
from mainframe.zowe_writer import upload_converted_folder, upload_converted_program
```

## Local dependency notes

- [mainframe/zowe_fetcher.py](zowe_fetcher.md)
- [mainframe/zowe_libraries.py](zowe_libraries.md)
- [mainframe/zowe_programs.py](zowe_programs.md)
- [mainframe/zowe_resolver.py](zowe_resolver.md)
- [mainframe/zowe_settings.py](zowe_settings.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)
- [mainframe/zowe_writer.py](zowe_writer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_zowe_semantic_release_gate.py](../tests/test_zowe_semantic_release_gate.md)

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
