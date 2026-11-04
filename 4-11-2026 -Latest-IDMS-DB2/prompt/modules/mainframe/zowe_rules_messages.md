# `mainframe/zowe_rules_messages.py`

Source: [mainframe/zowe_rules_messages.py](../../../mainframe/zowe_rules_messages.py) | 131 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `23af33e9631c4675cf3432ec73372e0090cd63e73d9cb963b0f413a8cf5117d0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Narrative, diagnostics, log formats, errors and warnings.

## Module-level bindings

`ZOWE_RULES` (L11), `DIAG_START_FETCH` (L24), `DIAG_END_FETCH` (L25), `DIAG_APPLICATION_TEMPLATE` (L26), `DIAG_PROGRAM_LIST_TEMPLATE` (L27), `DIAG_LIBRARY_ORDER_TEMPLATE` (L28), `DIAG_CONNECTION_TEMPLATE` (L29), `DIAG_FOUND_TEMPLATE` (L30), `DIAG_NOT_FOUND_TEMPLATE` (L31), `DIAG_DERIVED_DCLGEN_TEMPLATE` (L34), `DIAG_SUBSCHEMA_DETECTED_TEMPLATE` (L35), `DIAG_DEPENDENCIES_TEMPLATE` (L36), `DIAG_UPLOAD_TEMPLATE` (L39), `DIAG_VERIFIED_TEMPLATE` (L40), `DIAG_MAPPING_LOCAL` (L41), `DIAG_TOTAL_TEMPLATE` (L45), `LOG_CONNECTION` (L48), `LOG_DOWNLOAD` (L49), `LOG_UPLOAD` (L50), `LOG_MEMBER_COUNT` (L51), `LOG_VERIFY_TRANSLATION` (L54), `ZOWE_ERROR_MESSAGES` (L60), `ZOWE_WARNING_MESSAGES` (L109), `DIAG_ELEMENTS_TEMPLATE` (L127), `DIAG_NO_ELEMENTS_TEMPLATE` (L128)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_rules.py](zowe_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
