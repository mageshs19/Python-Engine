# `rules/counter_declaration_rules.py`

Source: [rules/counter_declaration_rules.py](../../../rules/counter_declaration_rules.py) | 123 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b27aa687090982d87b9758122ee6942aadff805c8462bf531aa2bd7becfd48f7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Row counter declaration rules.

## Module-level bindings

`TOTALS_ANCHOR_STATEMENT` (L26), `ENFORCE_COUNTER_DECLARATION` (L30), `COUNTER_DECLARATION_TEMPLATE` (L38), `COUNTER_PICTURE` (L39), `FALLBACK_CHILD_LEVEL` (L40), `EMIT_COUNTER_TOTALS` (L45), `COUNTER_DISPLAY_TEMPLATE` (L47), `COUNTER_LABEL_TEMPLATE` (L48), `COUNTER_LABEL_WIDTH` (L49), `TOTALS_INDENT` (L52), `COUNTER_DECLARATION_MESSAGES` (L57), `COUNTER_NAME_PREFIX` (L87), `COUNTER_NAME_SUFFIX` (L88), `COUNTER_OUTPUT_TOKEN` (L89), `TOTALS_DISPLAY_VERB` (L92), `TOTALS_LABEL_TOKEN` (L93), `ENFORCE_COUNTER_NAME_SHAPE` (L102), `ENFORCE_TOTALS_SUBSET_OF_DECLARED` (L108)

## Import declarations

```python
from __future__ import annotations
from rules.counter_rules import COUNTER_TOTALS_ANCHOR
```

## Local dependency notes

- [rules/counter_rules.py](counter_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/counter_totals_writer.py](../converter/composers/counter_declaration/counter_totals_writer.md)
- [converter/composers/counter_declaration_composer.py](../converter/composers/counter_declaration_composer.md)
- [converter/composers/counter_declaration_writer.py](../converter/composers/counter_declaration_writer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
