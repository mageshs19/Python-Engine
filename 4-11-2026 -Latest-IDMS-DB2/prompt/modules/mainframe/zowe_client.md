# `mainframe/zowe_client.py`

Source: [mainframe/zowe_client.py](../../../mainframe/zowe_client.py) | 197 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `d2d78aeb14decb4c4cada7521979f9ac9c9d21b261907d9f4fdfb09c1b066919`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> REST Files calls. One client instance per connection.

## Module-level bindings

`logger` (L43)

## Import declarations

```python
from __future__ import annotations
import logging
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
from mainframe.zowe_patterns import DATASET_NAME_PATTERN, MEMBER_PATH_PATTERN, UNSAFE_FILENAME_CHAR_PATTERN
from mainframe.zowe_rules import CSRF_HEADER, DATA_TYPE_HEADER, HTTP_OK, LOG_CONNECTION, LOG_DOWNLOAD, LOG_MEMBER_COUNT, LOG_UPLOAD, LOG_VERIFY_TRANSLATION, MAX_ITEMS_HEADER, MEMBER_NAME_MAX_LENGTH, TEXT_CONTENT_TYPE, ZOWE_ERROR_MESSAGES
from mainframe.zowe_settings import ZoweConnection
```

## Local dependency notes

- [mainframe/zowe_patterns.py](zowe_patterns.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_settings.py](zowe_settings.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_copybook_upload.py](zowe_copybook_upload.md)
- [mainframe/zowe_libraries.py](zowe_libraries.md)
- [mainframe/zowe_writer.py](zowe_writer.md)

## Symbol contracts and control points

### `ZoweClient` - L50-L197

```python
class ZoweClient()
```

Talks to exactly one endpoint.

### `ZoweClient.__init__` - L53-L58

```python
__init__(self, connection: ZoweConnection, artifact: str, label: str) -> None
```

Observed calls (lexical order): `self._validate`, `logger.info`.

### `ZoweClient._validate` - L61-L73

```python
_validate(self) -> None
```

Observed calls (lexical order): `ValueError`, `ZOWE_ERROR_MESSAGES['missing_host'].format`, `ZOWE_ERROR_MESSAGES['missing_credentials'].format`.

Control points:

- L62: `if not self.connection.host`
- L68: `if not self.connection.user or not self.connection.password`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['missing_host'].format(label=self.label, artifact=self.artifact))`; `ValueError(ZOWE_ERROR_MESSAGES['missing_credentials'].format(label=self.label, artifact=self.artifact))`.

### `ZoweClient.library_name` - L76-L86

```python
library_name(dataset: str) -> str
```

Observed calls (lexical order): `str`, `str(dataset or '').strip`, `str(dataset or '').strip().upper`, `MEMBER_PATH_PATTERN.search`, `ValueError`, `ZOWE_ERROR_MESSAGES['member_path_not_allowed'].format`, `DATASET_NAME_PATTERN.match`, `ZOWE_ERROR_MESSAGES['invalid_dataset'].format`.

Control points:

- L78: `if MEMBER_PATH_PATTERN.search(normalized)`
- L82: `if not DATASET_NAME_PATTERN.match(normalized)`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['member_path_not_allowed'].format(dataset=dataset))`; `ValueError(ZOWE_ERROR_MESSAGES['invalid_dataset'].format(dataset=dataset))`.

### `ZoweClient.member_name` - L89-L94

```python
member_name(name: str) -> str
```

Observed calls (lexical order): `UNSAFE_FILENAME_CHAR_PATTERN.sub`, `str`, `cleaned.strip`, `cleaned.strip('_').upper`, `ValueError`.

Control points:

- L92: `if not cleaned`

Explicit raises: `ValueError(f'Cannot derive a PDS member name from: {name}')`.

### `ZoweClient._auth` - L97-L98

```python
_auth(self) -> HTTPBasicAuth
```

Observed calls (lexical order): `HTTPBasicAuth`.

### `ZoweClient._member_url` - L100-L101

```python
_member_url(self, dataset: str, member: str) -> str
```

### `ZoweClient._members_url` - L103-L104

```python
_members_url(self, dataset: str) -> str
```

### `ZoweClient._get_member` - L106-L117

```python
_get_member(self, dataset: str, member: str) -> requests.Response
```

One GET on a member. Status is never raised on.

Observed calls (lexical order): `self.library_name`, `requests.get`, `self._member_url`, `self._auth`, `logger.info`.

### `ZoweClient.member_exists` - L120-L123

```python
member_exists(self, dataset: str, member: str) -> tuple[bool, int]
```

Probe ONE member. Returns (found, http_status).

Observed calls (lexical order): `self._get_member`.

### `ZoweClient.fetch_member` - L125-L130

```python
fetch_member(self, dataset: str, member: str) -> tuple[bytes, int]
```

Content and status. Empty bytes when the member is absent.

Observed calls (lexical order): `self._get_member`.

Control points:

- L128: `if response.status_code == HTTP_OK`

### `ZoweClient.download_member` - L133-L137

```python
download_member(self, dataset: str, member: str) -> bytes
```

Strict download. Raises on any non-200 status.

Observed calls (lexical order): `self._get_member`, `response.raise_for_status`.

### `ZoweClient.list_members` - L139-L155

```python
list_members(self, dataset: str) -> list[str]
```

Diagnostic only. Never used to decide whether a member exists.

Observed calls (lexical order): `self.library_name`, `requests.get`, `self._members_url`, `self._auth`, `response.raise_for_status`, `response.json`, `response.json().get`, `item.get`, `sorted`, `len`, `logger.info`, `ValueError`, `ZOWE_ERROR_MESSAGES['no_members'].format`.

Control points:

- L153: `if not members`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['no_members'].format(dataset=dataset))`.

### `ZoweClient.upload_member` - L157-L169

```python
upload_member(self, dataset: str, member: str, content: bytes) -> int
```

Observed calls (lexical order): `self.library_name`, `requests.put`, `self._member_url`, `self._auth`, `logger.info`, `response.raise_for_status`.

### `ZoweClient.verify_member` - L171-L197

```python
verify_member(self, dataset: str, member: str, expected: bytes) -> None
```

Observed calls (lexical order): `self.download_member`, `len`, `ValueError`, `ZOWE_ERROR_MESSAGES['verify_mismatch'].format`, `self.library_name`, `sum`, `zip`, `logger.debug`.

Control points:

- L173: `if retrieved == expected`
- L180: `if len(retrieved) != len(expected)`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['verify_mismatch'].format(dataset=self.library_name(dataset), member=member, sent=len(expected), received=len(retrieved)))`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
