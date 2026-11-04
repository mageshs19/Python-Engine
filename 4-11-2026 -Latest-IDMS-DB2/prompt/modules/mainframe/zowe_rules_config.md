# `mainframe/zowe_rules_config.py`

Source: [mainframe/zowe_rules_config.py](../../../mainframe/zowe_rules_config.py) | 103 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `828c12c737f83866b1e33cf52f627f2a2db91e31a4f11c9fc8efa5cf57e4a46a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Configuration vocabulary: env keys, application, libraries, programs.

## Module-level bindings

`ARTIFACT_KEY_TEMPLATE` (L11), `SHARED_KEY_TEMPLATE` (L12), `NAME_HOST` (L14), `NAME_PORT` (L15), `NAME_USER` (L16), `NAME_PASSWORD` (L17), `NAME_VERIFY_TLS` (L18), `NAME_TIMEOUT` (L19), `NAME_DATASET` (L20), `NAME_LIBRARIES` (L21), `NAME_MEMBER` (L22), `NAME_LANDING` (L23), `NAME_READ_ONLY` (L24), `NAME_APPLICATION` (L25), `NAME_PROGRAMS` (L26), `NAME_PROGRAM_LIST_FILE` (L27), `WORKSPACE_ROOT_KEY` (L29), `WORKSPACE_DIR_NAME` (L30), `INPUT_SOURCE_ENV_KEY` (L33), `INPUT_SOURCE_LOCAL` (L34), `INPUT_SOURCE_UPLOAD` (L35), `INPUT_SOURCE_ZOWE` (L36), `SUPPORTED_INPUT_SOURCES` (L37), `APPLICATION_PLACEHOLDER` (L44), `DEFAULT_APPLICATION` (L45), `LIBRARY_SEPARATOR` (L46), `DEFAULT_PROGRAM_LIST_FILE` (L49), `PROGRAM_LIST_COMMENT` (L50), `DCLGEN_PREFIX` (L53), `DCLGEN_SUFFIX` (L54), `DCLGEN_RECORD_TAIL_LENGTH` (L55), `DCLGEN_MEMBER_TEMPLATE` (L56), `ENV_REFERENCE_MAX_DEPTH` (L61), `SENSITIVE_NAMES` (L64), `MASKED_VALUE` (L65), `SEQUENCE_AREA_WIDTH` (L66), `INDICATOR_COLUMN` (L67), `BODY_START_COLUMN` (L68), `BODY_END_COLUMN` (L69), `COMMENT_INDICATORS` (L70), `SUBSCHEMA_CLAUSE_KEYWORDS` (L79), `SUBSCHEMA_ELEMENT_NOISE` (L96), `ELEMENT_NAME_MIN_LENGTH` (L99), `NAME_RECORD_PREFIX` (L103)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_rules.py](zowe_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
