# `mainframe/zowe_settings.py`

Source: [mainframe/zowe_settings.py](../../../mainframe/zowe_settings.py) | 187 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `803b4515a76f8d11282d61269b94d95a1053c97e7a39852dfde22276a8cfec71`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Per-artifact connection and library resolution.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from mainframe.zowe_env import setting, setting_bool, setting_int
from mainframe.zowe_rules import APPLICATION_PLACEHOLDER, ARTIFACT_EXTENSIONS, ARTIFACT_LABELS, ARTIFACT_OUTPUT, BASE_URL_TEMPLATE, DEFAULT_APPLICATION, DEFAULT_LANDING_SUBFOLDERS, DEFAULT_PORT, DEFAULT_TIMEOUT_SECONDS, DEFAULT_VERIFY_TLS, LIBRARY_SEPARATOR, MANDATORY_ARTIFACTS, NAME_APPLICATION, NAME_DATASET, NAME_HOST, NAME_LANDING, NAME_LIBRARIES, NAME_PASSWORD, NAME_PORT, NAME_READ_ONLY, NAME_TIMEOUT, NAME_USER, NAME_VERIFY_TLS, ZOWE_ARTIFACT_KEYS, ZOWE_ERROR_MESSAGES
from mainframe.zowe_workspace import workspace_root
```

## Local dependency notes

- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/__init__.py](__init__.md)
- [mainframe/zowe_client.py](zowe_client.md)
- [mainframe/zowe_commands.py](zowe_commands.md)
- [mainframe/zowe_copybook_upload.py](zowe_copybook_upload.md)
- [mainframe/zowe_libraries.py](zowe_libraries.md)
- [mainframe/zowe_writer.py](zowe_writer.md)

## Symbol contracts and control points

### `application_code` - L49-L52

```python
application_code() -> str
```

XY - first two letters of the application being migrated.

Observed calls (lexical order): `setting`, `value.strip`, `value.strip().upper`.

### `expand` - L55-L58

```python
expand(template: str) -> str
```

BAS.{XY}.CPY -> BAS.VM.CPY

Observed calls (lexical order): `application_code`, `str`, `str(template or '').replace`, `text.strip`, `text.strip().upper`.

### `ZoweConnection` - L65-L81

```python
class ZoweConnection()
```

One endpoint. Two artifacts may point at different systems.

Declared class/data-model fields:

```python
host: str
port: int
user: str
password: str
verify_tls: bool
timeout_seconds: int
```

### `ZoweConnection.base_url` - L76-L77

```python
base_url(self) -> str
```

Observed calls (lexical order): `BASE_URL_TEMPLATE.format`.

### `ZoweConnection.fingerprint` - L80-L81

```python
fingerprint(self) -> str
```

### `ArtifactProfile` - L85-L100

```python
class ArtifactProfile()
```

One artifact: connection, ordered libraries, landing folder.

Declared class/data-model fields:

```python
key: str
label: str
connection: ZoweConnection
libraries: tuple[str, ...] = field(default_factory=tuple)
dataset: str = ''
landing_dir: Path = field(default_factory=workspace_root)
extension: str = ''
mandatory: bool = False
read_only: bool = False
```

### `ArtifactProfile.configured` - L99-L100

```python
configured(self) -> bool
```

Observed calls (lexical order): `bool`.

### `_connection` - L106-L114

```python
_connection(artifact: str) -> ZoweConnection
```

Observed calls (lexical order): `ZoweConnection`, `setting`, `setting_int`, `setting_bool`.

### `artifact_connection` - L117-L119

```python
artifact_connection(artifact: str) -> ZoweConnection
```

Public accessor so other modules do not rebuild whole profiles.

Observed calls (lexical order): `_connection`.

### `artifact_libraries` - L122-L133

```python
artifact_libraries(artifact: str) -> tuple[str, ...]
```

Ordered, de-duplicated library list. Empty when unset.

Observed calls (lexical order): `setting`, `raw.split`, `expand`, `out.append`, `tuple`.

Control points:

- L125: `if not raw`
- L129: `for token in raw.split(LIBRARY_SEPARATOR)`
- L131: `if dataset and dataset not in out`

### `require_libraries` - L136-L144

```python
require_libraries(artifact: str) -> tuple[str, ...]
```

Observed calls (lexical order): `artifact_libraries`, `ValueError`, `ZOWE_ERROR_MESSAGES['no_libraries'].format`.

Control points:

- L138: `if not libraries`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['no_libraries'].format(label=ARTIFACT_LABELS[artifact], artifact=artifact))`.

### `landing_root` - L147-L148

```python
landing_root() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `_landing_dir` - L151-L156

```python
_landing_dir(artifact: str) -> Path
```

Observed calls (lexical order): `setting`, `DEFAULT_LANDING_SUBFOLDERS.get`, `artifact.title`, `Path`, `candidate.is_absolute`, `workspace_root`.

### `_profile` - L159-L168

```python
_profile(artifact: str) -> ArtifactProfile
```

Observed calls (lexical order): `ArtifactProfile`, `_connection`, `artifact_libraries`, `_landing_dir`.

### `build_profiles` - L171-L173

```python
build_profiles() -> tuple[ArtifactProfile, ...]
```

The four input artifacts, each resolved independently.

Observed calls (lexical order): `_profile`, `tuple`.

### `build_output_profile` - L176-L187

```python
build_output_profile() -> ArtifactProfile
```

Write-back target. A single dataset, not a library list.

Observed calls (lexical order): `ArtifactProfile`, `_connection`, `expand`, `setting`, `_landing_dir`, `setting_bool`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
