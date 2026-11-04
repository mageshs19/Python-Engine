# `rules/generated_cobol_safety_rules.py`

Source: [rules/generated_cobol_safety_rules.py](../../../rules/generated_cobol_safety_rules.py) | 78 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `3287ef49a7a754f9f3435b278c62b9e767f1dc8e9f051e1c73b1b8b00331afe9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Constants for the generated-COBOL safety cleanup passes.

## Module-level bindings

`PARAGRAPH_TERMINATOR` (L20), `ENFORCE_PARAGRAPH_TERMINATION` (L21), `ENFORCE_OUTPUT_WRITE_AFTER_CHILD_LOOP` (L39), `EARLY_STOP_VALUE` (L42), `EARLY_STOP_GUARD_OPEN` (L46), `EARLY_STOP_GUARD_CLOSE` (L47), `IND_STATEMENT` (L50), `IND_NESTED` (L51), `WRITE_BLOCK_SCAN_LIMIT` (L54), `ALIGN_GENERATED_SQL_MARKERS_EVERYWHERE` (L61), `SQL_MARKER_MIN_INDENT` (L62), `SQL_MARKER_INDENT` (L63), `SAFETY_MESSAGES` (L66)

## Import declarations

```python
from __future__ import annotations
```

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
