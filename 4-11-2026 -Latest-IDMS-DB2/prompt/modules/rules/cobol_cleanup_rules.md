# `rules/cobol_cleanup_rules.py`

Source: [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.py) | 276 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `5910e1e9369268b3dc5f6d4126ee5d82602ea5cdbe655bb1a0cf23ec6479a213`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL cleanup rule constants.

## Module-level bindings

`SW_STATUS_D_DECLARATION` (L49), `WS_DB2_FLAGS_GROUP` (L53), `REMOVE_GENERATED_NARRATION_COMMENTS` (L55), `NARRATION_COMMENT_PREFIXES` (L56), `NARRATION_COMMENT_KEEP_PREFIXES` (L57), `REMOVE_STRANDED_SECTION_BANNERS` (L59), `STRANDED_BANNER_LOOKAHEAD` (L60), `STOP_BACKWARD_SCAN_WORDS` (L67), `STATEMENT_CONTINUATION_TOKENS` (L87), `MOVE_N_LOOKBACK_WINDOW` (L103), `OUTPUT_MOVE_SCAN_WINDOW` (L104), `INITIALIZE_LOOKBACK_WINDOW` (L105), `ENFORCE_PARAGRAPH_TERMINATION` (L116), `PARAGRAPH_TERMINATOR` (L117), `NON_PARAGRAPH_SINGLE_WORDS` (L121), `ENFORCE_OUTPUT_WRITE_AFTER_CHILD_LOOP` (L154), `FETCH_PARAGRAPH_CURSOR_SEPARATOR` (L156), `NESTED_INDENT_STEP` (L157), `WHEN_ZERO_PERFORM_SCAN_LIMIT` (L158), `OUTPUT_WRITE_MOVE_PASS_LIMIT` (L159), `EARLY_STOP_VALUE` (L161), `EARLY_STOP_GUARD_OPEN` (L162), `EARLY_STOP_GUARD_CLOSE` (L163), `CLEANUP_MESSAGES` (L174)

## Import declarations

```python
from __future__ import annotations
```

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/cleanup_message_collector.py](../converter/composers/cleanup/cleanup_message_collector.md)
- [converter/composers/cleanup/cursor_nesting_analyser.py](../converter/composers/cleanup/cursor_nesting_analyser.md)
- [converter/composers/cleanup/db2_date_output_cleanup.py](../converter/composers/cleanup/db2_date_output_cleanup.md)
- [converter/composers/cleanup/error_status_flag_cleanup.py](../converter/composers/cleanup/error_status_flag_cleanup.md)
- [converter/composers/cleanup/initialize_before_output_cleanup.py](../converter/composers/cleanup/initialize_before_output_cleanup.md)
- [converter/composers/cleanup/output_write_placement_cleanup.py](../converter/composers/cleanup/output_write_placement_cleanup.md)
- [converter/composers/cleanup/paragraph_terminator_cleanup.py](../converter/composers/cleanup/paragraph_terminator_cleanup.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
