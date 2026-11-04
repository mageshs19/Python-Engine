# `rules/legacy_restart_rules.py`

Source: [rules/legacy_restart_rules.py](../../../rules/legacy_restart_rules.py) | 137 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `eb71f422709dac3b7a36875cfa990acaf42ff6b889101acc56249a621018e474`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Stand-down policy for the LEGACY restart generator.

## Module-level bindings

`LEGACY_RESTART_RULES` (L38), `ENABLE_LEGACY_RESTART_GENERATOR` (L70), `REPORT_LEGACY_RESIDUE` (L74), `STAND_DOWN_REASONS` (L79), `LEGACY_HANDLER_NUMBER_PREFIXES` (L101), `REPORT_DANGLING_PERFORM` (L105), `LEGACY_RESTART_MESSAGES` (L110), `__all__` (L129)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/select_paragraph_generator.py](../converter/generators/select_paragraph_generator.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
