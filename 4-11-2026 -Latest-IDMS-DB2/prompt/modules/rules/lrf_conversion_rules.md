# `rules/lrf_conversion_rules.py`

Source: [rules/lrf_conversion_rules.py](../../../rules/lrf_conversion_rules.py) | 452 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `6ea273ff2e5612dd51e04b0355004a88c4ab632da28775ef0a9978923aedc1c8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> LRF -> classic IDMS expansion rules.

## Module-level bindings

`ENABLE_LRF_PATH_EXPANSION` (L66), `REQUIRE_MAPPED_DRIVING_RECORD` (L69), `OBTAIN_FIRST_TEMPLATE` (L72), `OBTAIN_NEXT_TEMPLATE` (L73), `FIND_FIRST_TEMPLATE` (L74), `STATEMENT_TERMINATOR` (L75), `CALC_KEY_TOKEN` (L89), `CALC_SCOPE` (L90), `OBTAIN_CALC_TEMPLATE` (L91), `MULTILINE_WHERE_SCAN_LIMIT` (L98), `END_OF_SET_TOKEN` (L102), `RECORD_NOT_FOUND_TOKEN` (L103), `LRF_PARENT_NOT_FOUND_TOKEN` (L107), `RECORD_FOUND_TOKEN` (L110), `NOT_FOUND_LITERAL_FRAGMENTS` (L112), `END_OF_SET_LITERAL_FRAGMENTS` (L120), `FOUND_LITERAL_FRAGMENTS` (L128), `NEGATION_FRAGMENTS` (L134), `FOUND_NEGATION_FRAGMENTS` (L139), `TOKENS_OWNED_DOWNSTREAM` (L144), `STATUS_END_OF_SET` (L150), `STATUS_NOT_FOUND` (L151), `STATUS_SET_EMPTY` (L152), `LR_STATUS_FIELD` (L156), `LR_QUALIFIER` (L157), `COMMENT_PREFIX` (L160), `EXPANDED_OBTAIN_TEMPLATE` (L162), `EXPANDED_PARENT_TEMPLATE` (L166), `EXPANDED_CALC_PARENT_TEMPLATE` (L172), `SKIPPED_NO_PATH_TEMPLATE` (L175), `SKIPPED_NO_RECORD_TEMPLATE` (L179), `SKIPPED_UNMAPPED_TEMPLATE` (L183), `SKIPPED_CALC_PARENT_TEMPLATE` (L187), `SKIPPED_NO_KEYWORD_TEMPLATE` (L191), `REMOVED_LR_STATUS_TEMPLATE` (L195), `EXPANDED_FILTER_TEMPLATE` (L201), `MODIFY_TEMPLATE` (L207), `STORE_TEMPLATE` (L208), `EXPANDED_UPDATE_TEMPLATE` (L210), `SKIPPED_STORE_AMBIGUOUS_TEMPLATE` (L213), `UNMAPPED_DIAGNOSTIC_TEMPLATE` (L222), `UNRENDERABLE_DIAGNOSTIC_TEMPLATE` (L225), `LRF_UPDATE_MESSAGES` (L230), `LRF_EXPANSION_MESSAGES` (L280), `LR_STATUS_TOKEN_SQLCODE` (L361), `LR_STATUS_TOKEN_REPLACEMENT_ORDER` (L365), `ENABLE_LR_STATUS_TOKEN_REPLACEMENT` (L369), `LR_STATUS_TOKEN_MESSAGES` (L372), `__all__` (L393)

## Import declarations

```python
from __future__ import annotations
```

## Importers (10)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/lrf_key_binding_composer.py](../converter/composers/lrf_key_binding_composer.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py](../converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.md)
- [converter/resolvers/lrf_path_resolver.py](../converter/resolvers/lrf_path_resolver.md)
- [converter/transformers/lr_status_token_replacer.py](../converter/transformers/lr_status_token_replacer.md)
- [converter/transformers/lrf_path_expander.py](../converter/transformers/lrf_path_expander.md)
- [converter/transformers/lrf_update_expander.py](../converter/transformers/lrf_update_expander.md)
- [patterns/lrf_program_patterns.py](../patterns/lrf_program_patterns.md)
- [tests/lrf/test_lr_status_token_replacer.py](../tests/lrf/test_lr_status_token_replacer.md)
- [tests/lrf/test_status_token_classifier.py](../tests/lrf/test_status_token_classifier.md)
- [tests/test_lrf_path_expander.py](../tests/test_lrf_path_expander.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
