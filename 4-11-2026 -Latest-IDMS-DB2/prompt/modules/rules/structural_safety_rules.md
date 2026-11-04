# `rules/structural_safety_rules.py`

Source: [rules/structural_safety_rules.py](../../../rules/structural_safety_rules.py) | 292 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `7cefe9a2ab0fbe97d79c28152ad6c4137b7c0f87fd8243f56afa1c244b408543`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Structural safety constants.

## Module-level bindings

`MARKER_BODY_WIDTH` (L83), `ENFORCE_MARKER_BODY_WIDTH` (L87), `ENFORCE_CONDITION_INTEGRITY` (L92), `CONDITION_SCAN_LIMIT` (L93), `CONDITION_CONTINUATION_TOKENS` (L95), `CONDITION_TERMINATING_VERBS` (L101), `ENFORCE_ORPHANED_RECORD_GUARD` (L112), `ORPHANED_RECORD_MARKER_TEMPLATE` (L119), `ORPHANED_RECORD_MARKER_DETAIL` (L125), `ORPHANED_LINE_PREFIX` (L129), `ENFORCE_UNREACHABLE_STATEMENT_GUARD` (L134), `UNREACHABLE_MARKER` (L137), `PARAGRAPH_EXIT_WORDS` (L141), `MAX_UNREACHABLE_STATEMENTS` (L147), `ENFORCE_SAFE_COUNTER_GROUP` (L152), `PREFER_GENERATED_COUNTER_GROUP` (L153), `UNIFY_GENERATED_FIELD_GROUP` (L155), `PREFERRED_WORK_GROUP_NAMES` (L157), `GENERATED_FIELD_GROUP_NAME` (L161), `GENERATED_FIELD_GROUP_ALIASES` (L162), `GENERATED_FIELD_GROUP_TEMPLATE` (L166), `GENERATED_FIELD_GROUP_MARKER` (L171), `GENERATED_FIELD_CHILD_INDENT` (L173), `GENERATED_FIELD_CHILD_LEVEL` (L174), `GENERATED_COUNTER_GROUP_NAME` (L176), `GENERATED_COUNTER_GROUP_TEMPLATE` (L177), `GENERATED_COUNTER_GROUP_MARKER` (L180), `GENERATED_COUNTER_CHILD_INDENT` (L182), `RECORD_LAYOUT_VERBS` (L187), `STRUCTURAL_SAFETY_MESSAGES` (L198), `__all__` (L261)

## Import declarations

```python
from __future__ import annotations
from catalogs.output_sections import DB2_GENERATED_ROW_COUNTERS_MARKER, DB2_GENERATED_WORKING_STORAGE_MARKER
```

## Local dependency notes

- [catalogs/output_sections.py](../catalogs/output_sections.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/counter_anchor_resolver.py](../converter/composers/counter_declaration/counter_anchor_resolver.md)
- [converter/composers/output_write_paragraph_composer.py](../converter/composers/output_write_paragraph_composer.md)
- [converter/composers/structural_safety_composer.py](../converter/composers/structural_safety_composer.md)
- [converter/services/cobol_condition_scanner.py](../converter/services/cobol_condition_scanner.md)
- [converter/services/generated_field_anchor.py](../converter/services/generated_field_anchor.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
