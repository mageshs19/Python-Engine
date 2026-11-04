# `mainframe/zowe_copybook_upload.py`

Source: [mainframe/zowe_copybook_upload.py](../../../mainframe/zowe_copybook_upload.py) | 47 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `42d378395180d6bf5e6765fec34b7411821087b692a41624f5421be530ba5f4c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Upload proven, separately generated DB2 COPY members before COBOL members.

## Module-level bindings

`DATASET_SETTING` (L15)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from mainframe.zowe_client import ZoweClient
from mainframe.zowe_env import raw_setting
from mainframe.zowe_settings import build_output_profile, expand
```

## Local dependency notes

- [mainframe/zowe_client.py](zowe_client.md)
- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_settings.py](zowe_settings.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)
- [tests/test_copybook_provenance_and_occurs.py](../tests/test_copybook_provenance_and_occurs.md)

## Symbol contracts and control points

### `staging_directory` - L18-L19

```python
staging_directory(output_dir: Path) -> Path
```

### `require_copybook_upload_configuration` - L22-L33

```python
require_copybook_upload_configuration(output_dir: Path) -> tuple[Path, ...]
```

Observed calls (lexical order): `sorted`, `staging_directory`, `staging_directory(output_dir).glob`, `tuple`, `raw_setting`, `raw_setting(DATASET_SETTING, '').strip`, `ValueError`, `len`, `member.stem.upper`, `any`, `name.isalnum`, `set`.

Control points:

- L24: `if members and (not raw_setting(DATASET_SETTING, '').strip())`
- L31: `if len(names) != len(set(names)) or any((len(name) > 8 or not name.isalnum() for name in names))`

Explicit raises: `ValueError(f'{len(members)} derived DB2 COPY member(s) require an explicit {DATASET_SETTING}. No program upload is allowed until the converted COPY assets ha...`; `ValueError('generated copybook members contain unsafe/duplicate PDS names')`.

### `upload_generated_copybooks` - L36-L47

```python
upload_generated_copybooks(output_dir: Path, diagnostics: list[str]) -> None
```

Observed calls (lexical order): `require_copybook_upload_configuration`, `build_output_profile`, `expand`, `raw_setting`, `ZoweClient`, `member.read_bytes`, `client.upload_member`, `member.stem.upper`, `client.verify_member`, `diagnostics.append`.

Control points:

- L38: `if not members`
- L43: `for member in members`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
