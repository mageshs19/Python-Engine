# `rules/sequence_artifact_rules.py`

Source: [rules/sequence_artifact_rules.py](../../../rules/sequence_artifact_rules.py) | 73 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `6eb8f1e525cd323956ac7b782aa8a9acdc0ef615ac6949a60d3cdfde3eec558e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sequence artifact cleanup rules.

## Module-level bindings

`ENFORCE_SEQUENCE_ARTIFACT_CLEANUP` (L15), `REPAIR_EXPOSED_SENTENCE` (L23), `PARAGRAPH_TERMINATOR` (L24), `SENTENCE_CARRIERS` (L29), `SEQUENCE_ARTIFACT_MESSAGES` (L61)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/sequence_artifact_cleanup_composer.py](../converter/composers/sequence_artifact_cleanup_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
