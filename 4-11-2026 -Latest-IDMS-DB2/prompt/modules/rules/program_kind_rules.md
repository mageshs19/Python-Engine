# `rules/program_kind_rules.py`

Source: [rules/program_kind_rules.py](../../../rules/program_kind_rules.py) | 103 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `e9e817bfbfcfc0c42d9609eea7ae999610231ef897456a3d32c411e5ae7e8826`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Program-kind policy: is this an UPDATE program or a RETRIEVAL program?

## Module-level bindings

`PROGRAM_KIND_RULES` (L32), `KIND_UPDATE` (L44), `KIND_RETRIEVAL` (L45), `MEASURE_KIND_FROM_SOURCE` (L52), `INPUT_MAY_PROMOTE_ONLY` (L56), `IDMS_WRITE_VERBS` (L59), `EVIDENCE_SAMPLE_LIMIT` (L62), `PROGRAM_KIND_MESSAGES` (L67), `__all__` (L94)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/obtain_calc_remover.py](../converter/composers/update_sql_cleanup/obtain_calc_remover.md)
- [converter/pipeline/conversion/conversion_pipeline_steps.py](../converter/pipeline/conversion/conversion_pipeline_steps.md)
- [converter/resolvers/program_kind_resolver.py](../converter/resolvers/program_kind_resolver.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
