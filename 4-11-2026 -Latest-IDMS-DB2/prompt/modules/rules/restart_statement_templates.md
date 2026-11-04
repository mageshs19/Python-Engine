# `rules/restart_statement_templates.py`

Source: [rules/restart_statement_templates.py](../../../rules/restart_statement_templates.py) | 283 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `5a19ccdb4a24bee77506d61bea666ad51b5e10ab1e7b8a643b203761a63bf002`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL statement templates for the restart / checkpoint family.

## Module-level bindings

`MAIN_FLOW_TEMPLATE` (L80), `CONTROL_TEMPLATE` (L100), `RESTART_FOUND_TEMPLATE` (L138), `WRITE_RESTART_TEMPLATE` (L158), `COMMIT_TEMPLATE` (L186), `ABEND_TEMPLATE` (L222), `PROCESS_TAIL_TEMPLATE` (L231), `READ_PARAGRAPH_TEMPLATE` (L243), `COMPLETE_RUN_MESSAGE` (L258), `COMMIT_ERROR_MESSAGE` (L263), `MINIMUM_CONTINUATION_INDENT` (L268), `__all__` (L271)

## Import declarations

```python
from __future__ import annotations
```

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/process_paragraph_injector.py](../converter/composers/restart/process_paragraph_injector.md)
- [converter/generators/restart/read_paragraph_builder.py](../converter/generators/restart/read_paragraph_builder.md)
- [converter/generators/restart/restart_config.py](../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_flow_builder.py](../converter/generators/restart/restart_flow_builder.md)
- [converter/generators/restart/restart_main_flow_builder.py](../converter/generators/restart/restart_main_flow_builder.md)
- [tests/restart/test_m1_restart_standards.py](../tests/restart/test_m1_restart_standards.md)
- [tests/restart/test_m2_restart_config.py](../tests/restart/test_m2_restart_config.md)
- [tests/restart/test_m5b_restart_found_nesting.py](../tests/restart/test_m5b_restart_found_nesting.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
