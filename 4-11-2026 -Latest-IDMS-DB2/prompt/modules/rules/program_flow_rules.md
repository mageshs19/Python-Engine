# `rules/program_flow_rules.py`

Source: [rules/program_flow_rules.py](../../../rules/program_flow_rules.py) | 133 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `84dd52461e26425af8672b9d2030fd97ffdb00b964f22763f0653faef40b8dcc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Program flow analyzer rules.

## Module-level bindings

`IDMS_RETRIEVAL_VERBS` (L49), `LOOP_TYPE_CURSOR` (L55), `LOOP_TYPE_UNKNOWN` (L56), `WRITE_VERBS` (L64), `IDMS_WRITE_VERBS` (L71), `STATEMENT_TERMINATOR` (L77), `DATE_TOKENS` (L85), `DATE_TOKEN_PREFIXES` (L92), `USAGE_TYPE_DATE_TOKEN` (L94), `TOKEN_DELIMITERS` (L97), `LOOP_SAMPLE_LIMIT` (L102), `FLOW_MESSAGES` (L104), `__all__` (L128)

## Import declarations

```python
from __future__ import annotations
```

## Importers (11)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](../converter/analyzers/program_flow/flow_cursor_loop_scanner.md)
- [converter/analyzers/program_flow/flow_date_scanner.py](../converter/analyzers/program_flow/flow_date_scanner.md)
- [converter/analyzers/program_flow/flow_diagnostics.py](../converter/analyzers/program_flow/flow_diagnostics.md)
- [converter/analyzers/program_flow/flow_models.py](../converter/analyzers/program_flow/flow_models.md)
- [converter/analyzers/program_flow/flow_write_scanner.py](../converter/analyzers/program_flow/flow_write_scanner.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](../converter/analyzers/program_flow/program_flow_analyzer.md)
- [converter/services/program_cursor_loop_analyzer.py](../converter/services/program_cursor_loop_analyzer.md)
- [converter/services/program_date_usage_analyzer.py](../converter/services/program_date_usage_analyzer.md)
- [converter/services/program_output_write_analyzer.py](../converter/services/program_output_write_analyzer.md)
- [rules/cursor_spec/cursor_spec_rules.py](cursor_spec/cursor_spec_rules.md)
- [rules/statement_joiner_rules.py](statement_joiner_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
