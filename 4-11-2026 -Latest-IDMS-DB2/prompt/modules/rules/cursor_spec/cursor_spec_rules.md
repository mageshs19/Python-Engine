# `rules/cursor_spec/cursor_spec_rules.py`

Source: [rules/cursor_spec/cursor_spec_rules.py](../../../../rules/cursor_spec/cursor_spec_rules.py) | 117 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `461dc32dfa2f9d34fe1894053da11b62a5a2528e1b8d4992d21cc6f695f8ee17`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor specification rules.

## Module-level bindings

`CLASSIFY_PARENT_BY_ABSENT_WHERE` (L45), `PARENT_CURSOR_OPEN_NUMBER` (L48), `CHILD_CURSOR_MINIMUM_NUMBER` (L49), `PARAGRAPH_NUMBER_SEPARATOR` (L50), `BODY_START_INDEX` (L57), `BODY_END_INDEX` (L58), `SPEC_SET_NAME` (L65), `SPEC_RECORD_NAME` (L66), `SPEC_TABLE_NAME` (L67), `SPEC_CURSOR_NAME` (L68), `SPEC_SELECT_COLUMNS` (L69), `SPEC_HOST_VARIABLES` (L70), `SPEC_WHERE_CONDITIONS` (L71), `SPEC_ORDER_BY_COLUMNS` (L72), `SPEC_OPEN_PARAGRAPH` (L73), `SPEC_FETCH_PARAGRAPH` (L74), `SPEC_CLOSE_PARAGRAPH` (L75), `SPEC_CURSOR_ORDER` (L76), `SPEC_IS_PARENT_CURSOR` (L77), `RELATIONSHIP_PREDICATE_TEMPLATE` (L82), `DCLGEN_GROUP_PREFIX` (L88), `HOST_REFERENCE_PREFIX` (L89), `HOST_GROUP_SEPARATOR` (L90), `__all__` (L92)

## Import declarations

```python
from __future__ import annotations
from rules.program_flow_rules import IDMS_RETRIEVAL_VERBS
```

## Local dependency notes

- [rules/program_flow_rules.py](../program_flow_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [rules/cursor_spec/__init__.py](__init__.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
