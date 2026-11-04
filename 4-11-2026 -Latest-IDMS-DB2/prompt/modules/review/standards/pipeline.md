# `review/standards/pipeline.py`

Source: [review/standards/pipeline.py](../../../../review/standards/pipeline.py) | 45 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `f66bab79629182dc89f65f359425306ecb5022bbda0251738f80ed6f73d80b48`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Controls which checks run. Edit this file only.

## Module-level bindings

`ENABLED_CHECKS` (L12), `DISABLED_CHECKS` (L15), `CHECK_ORDER` (L20), `BLOCKING_SEVERITIES` (L40), `EVIDENCE_LIMIT` (L43)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/engine/registry.py](../engine/registry.md)
- [review/engine/reviewer.py](../engine/reviewer.md)

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
