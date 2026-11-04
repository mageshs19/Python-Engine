# `rules/cursor_close_guarantee_rules.py`

Source: [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.py) | 236 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b293d99b2e0958b7b00450ae5730a4f72802f0406bf3b428778d00977c6719db`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor close-guarantee rules.

## Module-level bindings

`ENFORCE_CURSOR_CLOSE_GUARANTEE` (L80), `SYNTHESISE_MISSING_DRIVING_LOOP` (L83), `ENFORCE_FETCH_DRIVES_BUSINESS_PARAGRAPH` (L87), `REFUSE_BIND_WHEN_EXTERNALLY_DRIVEN` (L92), `PREFER_THRU_EXIT_PARAGRAPH` (L95), `OPERATION_OPEN` (L100), `OPERATION_FETCH` (L101), `OPERATION_CLOSE` (L102), `REQUIRED_OPERATIONS` (L103), `PERFORM_FETCH_UNTIL_TEMPLATE` (L108), `PERFORM_CLOSE_TEMPLATE` (L109), `PERFORM_BUSINESS_TEMPLATE` (L110), `PERFORM_BUSINESS_THRU_TEMPLATE` (L111), `UNTIL_TEMPLATE` (L112), `EXIT_PARAGRAPH_SUFFIX` (L114), `STATEMENT_TERMINATOR` (L115), `UNTIL_LOOKAHEAD_LIMIT` (L123), `NON_PARAGRAPH_SINGLE_WORDS` (L126), `CURSOR_CLOSE_GUARANTEE_MESSAGES` (L144), `__all__` (L213)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_eoc_rules import EOC_CONDITION_SUFFIX, EOC_CONDITION_TEMPLATE, LEGACY_EOC_CONDITIONS
```

## Local dependency notes

- [rules/cursor_eoc_rules.py](cursor_eoc_rules.md)

## Importers (17)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/procedure_control_flow_graph.py](../converter/analyzers/program_flow/procedure_control_flow_graph.md)
- [converter/composers/cursor_close_guarantee/business_paragraph_resolver.py](../converter/composers/cursor_close_guarantee/business_paragraph_resolver.md)
- [converter/composers/cursor_close_guarantee/close_guarantor.py](../converter/composers/cursor_close_guarantee/close_guarantor.md)
- [converter/composers/cursor_close_guarantee/condition_normaliser.py](../converter/composers/cursor_close_guarantee/condition_normaliser.md)
- [converter/composers/cursor_close_guarantee/line_utils.py](../converter/composers/cursor_close_guarantee/line_utils.md)
- [converter/composers/cursor_close_guarantee/loop_finder.py](../converter/composers/cursor_close_guarantee/loop_finder.md)
- [converter/composers/cursor_close_guarantee/loop_synthesiser.py](../converter/composers/cursor_close_guarantee/loop_synthesiser.md)
- [converter/composers/cursor_close_guarantee/message_log.py](../converter/composers/cursor_close_guarantee/message_log.md)
- [converter/composers/cursor_close_guarantee/models.py](../converter/composers/cursor_close_guarantee/models.md)
- [converter/composers/cursor_close_guarantee/paragraph_index.py](../converter/composers/cursor_close_guarantee/paragraph_index.md)
- [converter/composers/cursor_close_guarantee_composer.py](../converter/composers/cursor_close_guarantee_composer.md)
- [converter/composers/cursor_guarantee/business_paragraph_resolver.py](../converter/composers/cursor_guarantee/business_paragraph_resolver.md)
- 5 further importers are recorded in [the source manifest](../../source_manifest.json).

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
