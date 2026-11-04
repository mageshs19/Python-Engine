# `rules/initialization_placement_rules.py`

Source: [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.py) | 158 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `e4b7f6998afbeca14aeb1ba28e4269ceeec5240ff20689cd7858fc6611fa7671`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`ENFORCE_CURSOR_SCOPED_INITIALIZATION` (L7), `EMIT_STARTUP_INITIALIZE_PARAGRAPH` (L8), `REMOVE_LEGACY_STARTUP_PARAGRAPH` (L9), `SALVAGE_LEGACY_STARTUP_STATEMENTS` (L10), `EMIT_INITIALIZE_PERIOD` (L11), `STARTUP_PARAGRAPH_NAME` (L13), `TIMESTAMP_PARAGRAPH_NAME` (L14), `INITIALIZE_TEMPLATE` (L17), `PERFORM_TEMPLATE` (L18), `STATEMENT_TERMINATOR` (L20), `LINE_WIDTH` (L22), `SEQUENCE_WIDTH` (L23), `BODY_START` (L24), `BODY_END` (L25), `STATEMENT_INDENT` (L26), `ACTIVE_INDICATORS` (L27), `COMMENT_INDICATORS` (L28), `DCLGEN_GROUP_PREFIX` (L30), `CURSOR_SCOPE_LOOKAHEAD` (L31), `NON_PARAGRAPH_WORDS` (L33), `SCOPE_RUN` (L39), `SCOPE_ROW` (L40), `SCOPE_UNKNOWN` (L41), `ENFORCE_INITIALIZATION_PLACEMENT` (L43), `INITIALIZATION_PARAGRAPH_PREFIX` (L44), `INITIALIZATION_PARAGRAPH_TEMPLATE` (L45), `INITIALIZATION_FORBIDDEN_AFTER` (L46), `INITIALIZATION_PLACEMENT_ANCHORS` (L51), `DCLGEN_INITIALIZATION_PATTERNS` (L55), `INITIALIZATION_PLACEMENT_MESSAGES` (L60), `__all__` (L124)

## Import declarations

```python
from __future__ import annotations
from rules.timestamp_audit_rules import CS_PROGRAM_FIELD as PROGRAM_CONSTANT_FIELD, PROGRAM_NAME_FIELD, PROGRAM_NAME_MOVE_TEMPLATE
```

## Local dependency notes

- [rules/timestamp_audit_rules.py](timestamp_audit_rules.md)

## Importers (11)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/enhancement/output_validator.py](../converter/generators/enhancement/output_validator.md)
- [converter/generators/initialization/cursor_scope_scanner.py](../converter/generators/initialization/cursor_scope_scanner.md)
- [converter/generators/initialization/diagnostics.py](../converter/generators/initialization/diagnostics.md)
- [converter/generators/initialization/initialize_placer.py](../converter/generators/initialization/initialize_placer.md)
- [converter/generators/initialization/initialize_remover.py](../converter/generators/initialization/initialize_remover.md)
- [converter/generators/initialization/legacy_paragraph_remover.py](../converter/generators/initialization/legacy_paragraph_remover.md)
- [converter/generators/initialization/line_geometry.py](../converter/generators/initialization/line_geometry.md)
- [converter/generators/initialization/paragraph_index.py](../converter/generators/initialization/paragraph_index.md)
- [converter/generators/initialization/population_site_scanner.py](../converter/generators/initialization/population_site_scanner.md)
- [converter/generators/initialization/scope_initializer.py](../converter/generators/initialization/scope_initializer.md)
- [tests/initialization_scope/test_population_scope.py](../tests/initialization_scope/test_population_scope.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
