# `rules/output_write_paragraph_rules.py`

Source: [rules/output_write_paragraph_rules.py](../../../rules/output_write_paragraph_rules.py) | 112 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a860b92734d43c9c1b73bde4bc1d5b7cea64fd0a6578440bdc74bfcf9a5f96ff`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Output write paragraph extraction rules.

## Module-level bindings

`ENFORCE_OUTPUT_WRITE_PARAGRAPH` (L31), `WRITE_PARAGRAPH_TEMPLATE` (L38), `WRITE_PARAGRAPH_HEADER_TEMPLATE` (L39), `PERFORM_TEMPLATE` (L40), `REQUIRED_WRITE_COUNT` (L48), `MINIMUM_BODY_LINES` (L51), `IF_SCAN_LIMIT` (L54), `EXTRACTION_PASS_LIMIT` (L57), `SCOPE_TERMINATOR_WORDS` (L60), `IND_STATEMENT` (L71), `PARAGRAPH_TERMINATOR` (L72), `BLANK_LINE` (L73), `EMIT_PAGE_EJECT_BEFORE_PARAGRAPH` (L77), `PAGE_EJECT_INDICATOR` (L78), `EMIT_OUTPUT_COUNTER_INCREMENT` (L85), `OUTPUT_COUNTER_NAME` (L86), `COUNTER_ADD_TEMPLATE` (L87), `OUTPUT_WRITE_PARAGRAPH_MESSAGES` (L92)

## Import declarations

```python
from __future__ import annotations
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/output_write_eligibility.py](../converter/composers/output_write/output_write_eligibility.md)
- [converter/composers/output_write/output_write_line_utils.py](../converter/composers/output_write/output_write_line_utils.md)
- [converter/composers/output_write/output_write_renderer.py](../converter/composers/output_write/output_write_renderer.md)
- [converter/composers/output_write/output_write_scanner.py](../converter/composers/output_write/output_write_scanner.md)
- [converter/composers/output_write_paragraph_composer.py](../converter/composers/output_write_paragraph_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
