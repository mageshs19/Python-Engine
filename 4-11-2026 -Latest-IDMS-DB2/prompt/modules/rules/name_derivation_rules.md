# `rules/name_derivation_rules.py`

Source: [rules/name_derivation_rules.py](../../../rules/name_derivation_rules.py) | 44 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `4eb9437dd35cf4adbc263a73e9951d6f20ebb839acba7a74fb91414a8c1f028d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`NAME_DERIVATION_RULES` (L24), `NAME_DERIVATION_PREFIX` (L32), `NAME_DERIVATION_SOURCE_MARKER` (L33), `NAME_DERIVATION_TARGET_MARKER` (L34), `VM_BD_NAME_PATTERN` (L39)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/name_derivation_resolver.py](../converter/services/name_derivation_resolver.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
