# `mainframe/zowe_rules_artifacts.py`

Source: [mainframe/zowe_rules_artifacts.py](../../../mainframe/zowe_rules_artifacts.py) | 53 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `0560130fd4e0d32ddf996806d75f1340b54db0b634e352cc9d231dfe8957762b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Artifact identity: keys, labels, extensions, landing folders.

## Module-level bindings

`ARTIFACT_PROGRAM` (L11), `ARTIFACT_COPYBOOK` (L12), `ARTIFACT_DCLGEN` (L13), `ARTIFACT_SUBSCHEMA` (L14), `ARTIFACT_OUTPUT` (L15), `ZOWE_ARTIFACT_KEYS` (L17), `ARTIFACT_LABELS` (L24), `MANDATORY_ARTIFACTS` (L33), `OPTIONAL_WARNING_KEYS` (L35), `ARTIFACT_EXTENSIONS` (L37), `DEFAULT_LANDING_SUBFOLDERS` (L47)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_rules.py](zowe_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
