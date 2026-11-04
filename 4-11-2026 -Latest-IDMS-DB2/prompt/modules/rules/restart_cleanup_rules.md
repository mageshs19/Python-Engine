# `rules/restart_cleanup_rules.py`

Source: [rules/restart_cleanup_rules.py](../../../rules/restart_cleanup_rules.py) | 139 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `dbe446f34ec2b7719e0fe98ed5eef0950d0c35abf1d326e4262a1eb586b1de1e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Constants for removing legacy restart residue.

## Module-level bindings

`RESTART_CLEANUP_RULES` (L25), `LEGACY_RESTART_DETECTION_TOKENS` (L40), `LEGACY_DECLARATION_NAMES` (L55), `LEGACY_ABEND_MARKER_PREFIX` (L64), `NON_PARAGRAPH_DOTTED_LINES` (L66), `VALUE_CONTINUATION_SCAN_LIMIT` (L76), `SECTION_SUFFIX` (L84), `DIVISION_SUFFIX` (L85), `PARAGRAPH_SPAN_LIMIT` (L89), `CLEANUP_MESSAGES` (L95), `__all__` (L128)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/legacy_restart_cleanup.py](../converter/composers/restart/legacy_restart_cleanup.md)
- [converter/composers/restart/restart_injection_geometry.py](../converter/composers/restart/restart_injection_geometry.md)
- [tests/restart/test_m9a_legacy_cleanup.py](../tests/restart/test_m9a_legacy_cleanup.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
