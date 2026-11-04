# `rules/fixed_format_wrap_rules.py`

Source: [rules/fixed_format_wrap_rules.py](../../../rules/fixed_format_wrap_rules.py) | 53 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `ed196eaafd300d267862da119f96a90dfa70348fb41b61a9052b80f5f3d9b030`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format statement wrapping rules.

## Module-level bindings

`BODY_START_COLUMN` (L19), `BODY_END_COLUMN` (L20), `BODY_WIDTH` (L21), `CONTINUATION_INDENT` (L24), `TOKEN_MOVE` (L27), `TOKEN_TO` (L28), `TOKEN_OF_DCL` (L29), `PERIOD` (L32), `SENTENCE_TERMINATORS` (L35), `DIAG_WRAPPED_TEMPLATE` (L46), `DIAG_PERIOD_RESTORED` (L50)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/fixed_format_statement_wrapper.py](../converter/services/fixed_format_statement_wrapper.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
