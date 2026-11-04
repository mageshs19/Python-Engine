# `mainframe/zowe_writer.py`

Source: [mainframe/zowe_writer.py](../../../mainframe/zowe_writer.py) | 100 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `fc8f955d98a55cbbdab47d6ab6742b6e3c0efb6697cd2ef9e204564d7763475d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Write converted DB2 COBOL back to the configured output library.

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from mainframe.zowe_client import ZoweClient
from mainframe.zowe_patterns import OUTPUT_STEM_PATTERN
from mainframe.zowe_rules import DIAG_UPLOAD_TEMPLATE, DIAG_VERIFIED_TEMPLATE, ZOWE_ERROR_MESSAGES
from mainframe.zowe_settings import ArtifactProfile, build_output_profile
```

## Local dependency notes

- [mainframe/zowe_client.py](zowe_client.md)
- [mainframe/zowe_patterns.py](zowe_patterns.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_settings.py](zowe_settings.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/__init__.py](__init__.md)
- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)
- [mainframe/zowe_semantic_release_gate.py](zowe_semantic_release_gate.md)

## Symbol contracts and control points

### `member_from_output_name` - L19-L22

```python
member_from_output_name(stem: str) -> str
```

VMDZ7201_29-09-2026_143000 -> VMDZ7201

Observed calls (lexical order): `OUTPUT_STEM_PATTERN.match`, `str`, `ZoweClient.member_name`, `match.group`.

### `upload_converted_program` - L25-L65

```python
upload_converted_program(source_file: Path, profile: ArtifactProfile | None=None, diagnostics: list[str] | None=None) -> tuple[str, str]
```

Upload one generated file and verify it byte for byte.

Observed calls (lexical order): `build_output_profile`, `source_file.exists`, `source_file.is_file`, `FileNotFoundError`, `ValueError`, `PermissionError`, `ZOWE_ERROR_MESSAGES['read_only'].format`, `ZoweClient`, `member_from_output_name`, `source_file.read_text`, `raw_content.replace`, `raw_content.replace('\r\n', '\n').replace`, `normalized_content.encode`, `client.upload_member`, `client.verify_member`, `diagnostics.append`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L33: `if not source_file.exists() or not source_file.is_file()`
- L35: `if not profile.dataset`
- L37: `if profile.read_only`
- L54: `if diagnostics is not None`

Explicit raises: `FileNotFoundError(f'Source file does not exist: {source_file}')`; `ValueError(ZOWE_ERROR_MESSAGES['output_not_configured'])`; `PermissionError(ZOWE_ERROR_MESSAGES['read_only'].format(dataset=profile.dataset))`.

### `upload_converted_folder` - L68-L100

```python
upload_converted_folder(folder: Path, extension: str='', diagnostics: list[str] | None=None) -> list[tuple[str, str]]
```

Upload the latest generated program for each member.

Observed calls (lexical order): `build_output_profile`, `folder.exists`, `folder.is_dir`, `FileNotFoundError`, `folder.glob`, `member_from_output_name`, `latest_by_member.get`, `current.stat`, `path.stat`, `sorted`, `results.append`, `upload_converted_program`.

Control points:

- L83: `if not folder.exists() or not folder.is_dir()`
- L87: `for path in folder.glob(f'*{suffix}')`
- L90: `if current is None or path.stat().st_mtime > current.stat().st_mtime`
- L94: `for member in sorted(latest_by_member)`

Explicit raises: `FileNotFoundError(f'Output folder does not exist: {folder}')`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
