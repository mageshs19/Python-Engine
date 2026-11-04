# `rules/statement_joiner_rules.py`

Source: [rules/statement_joiner_rules.py](../../../rules/statement_joiner_rules.py) | 121 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `15ab583efcb4488e130ce00822e9233aa5c0c671a930db8ee4da1880f9f69938`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Statement-joining vocabulary.

## Module-level bindings

`IDMS_STATEMENT_VERBS` (L38), `SCOPE_OPENERS` (L62), `EXEC_SQL_START` (L87), `EXEC_SQL_END` (L88), `SENTENCE_TERMINATOR` (L90), `JOIN_MAX_LINES` (L96), `JOINER_MESSAGES` (L98), `__all__` (L110)

## Import declarations

```python
from __future__ import annotations
from rules.program_flow_rules import CONTINUATION_OPENERS, CONTINUATION_TRAILERS, STATEMENT_VERBS
```

## Local dependency notes

- [rules/program_flow_rules.py](program_flow_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
