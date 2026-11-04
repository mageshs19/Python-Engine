# `rules/cobol_standard_initialization_rules.py`

Source: [rules/cobol_standard_initialization_rules.py](../../../rules/cobol_standard_initialization_rules.py) | 302 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `20f575cb60abc9c6e0e2e2adfa92a63cd19df3de3b76482924e8882a42b69e7c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL Standard Initialization and Validation Rules (Issue #5).

## Module-level bindings

`ENFORCE_COBOL_STANDARD_INITIALIZATION` (L162), `EMIT_PROCESSING_COUNTERS` (L163), `EMIT_TIMESTAMP_FIELDS` (L164), `EMIT_PROGRAM_NAME_CONSTANT` (L165), `EMIT_COUNTER_TOTALS_DISPLAY` (L166), `COUNTER_DECLARATION_PARENT` (L171), `COUNTER_DECLARATION_LEVEL` (L172), `COUNTER_NAME_TEMPLATE` (L173), `COUNTER_PICTURE` (L174), `OUTPUT_COUNTER_NAME` (L175), `OUTPUT_COUNTER_LABEL` (L176), `TIMESTAMP_SECTION_TEMPLATE` (L181), `TIMESTAMP_CAPTURE_TIMING` (L189), `PROGRAM_CONSTANT_NAME` (L197), `PROGRAM_CONSTANT_PICTURE` (L198), `PROGRAM_CONSTANT_TEMPLATE` (L199), `PROGRAM_NAME_MOVE_TEMPLATE` (L202), `INITIALIZATION_PARAGRAPH_NAME` (L207), `INITIALIZATION_PARAGRAPH_RULE` (L208), `COUNTER_INCREMENT_TEMPLATE` (L216), `COUNTER_INCREMENT_PLACEMENT` (L217), `COUNTER_DISPLAY_TEMPLATE` (L222), `TOTALS_DISPLAY_ANCHOR` (L223), `TOTALS_DISPLAY_INDENT` (L224), `VALIDATION_DISPLAY_OPTIONS` (L229), `VALIDATION_DISPLAY_STATUS` (L236), `COBOL_STANDARD_CHECKLIST` (L241), `COBOL_STANDARD_MESSAGES` (L268), `DEPENDS_ON_RULES` (L296)

## Import declarations

```python
from __future__ import annotations
```

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
