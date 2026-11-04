# `mainframe/zowe_rules_connection.py`

Source: [mainframe/zowe_rules_connection.py](../../../mainframe/zowe_rules_connection.py) | 46 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `b0ca678c1cd85300e954242366767825e51edd0986731e256da46c4dc9905cdf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Connection defaults, URL assembly, headers and encoding.

## Module-level bindings

`DEFAULT_PORT` (L10), `DEFAULT_TIMEOUT_SECONDS` (L11), `DEFAULT_VERIFY_TLS` (L12), `URL_SCHEME` (L17), `URL_SCHEME_SEPARATOR` (L18), `ZOSMF_DATASETS_PATH` (L19), `BASE_URL_TEMPLATE` (L21), `CSRF_HEADER` (L28), `DATA_TYPE_HEADER` (L29), `TEXT_CONTENT_TYPE` (L30), `MEMBER_NAME_MAX_LENGTH` (L32), `UPLOAD_MEMBER_NAME_MAX_LENGTH` (L35), `TEXT_ENCODING` (L36), `MAX_ITEMS_HEADER` (L43), `HTTP_OK` (L45), `HTTP_NOT_FOUND` (L46)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_rules.py](zowe_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
