# `converter/services/logical_statement_joiner.py`

Source: [converter/services/logical_statement_joiner.py](../../../../converter/services/logical_statement_joiner.py) | 635 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `ee327594b0f5544722ba5e7a54dbfd015288f975d73e0350d4af0968d2b60f4d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> LRF -> classic IDMS expansion rules, and LR access classification.

## Module-level bindings

`ENABLE_LRF_PATH_EXPANSION` (L126), `REQUIRE_MAPPED_DRIVING_RECORD` (L129), `OBTAIN_FIRST_TEMPLATE` (L132), `OBTAIN_NEXT_TEMPLATE` (L133), `FIND_FIRST_TEMPLATE` (L134), `STATEMENT_TERMINATOR` (L135), `CALC_KEY_TOKEN` (L147), `CALC_SCOPE` (L148), `OBTAIN_CALC_TEMPLATE` (L149), `MULTILINE_WHERE_SCAN_LIMIT` (L156), `END_OF_SET_TOKEN` (L160), `RECORD_NOT_FOUND_TOKEN` (L161), `RECORD_FOUND_TOKEN` (L164), `NOT_FOUND_LITERAL_FRAGMENTS` (L166), `END_OF_SET_LITERAL_FRAGMENTS` (L174), `FOUND_LITERAL_FRAGMENTS` (L182), `NEGATION_FRAGMENTS` (L188), `FOUND_NEGATION_FRAGMENTS` (L193), `STATUS_END_OF_SET` (L196), `STATUS_NOT_FOUND` (L197), `STATUS_SET_EMPTY` (L198), `LR_STATUS_FIELD` (L202), `LR_QUALIFIER` (L203), `ENABLE_LR_ACCESS_ANALYSIS` (L213), `ENABLE_FIRST_ONLY_RENDERING` (L214), `ENABLE_BOUNDED_SEARCH_RENDERING` (L215), `ENABLE_LOOP_REMOVAL` (L216), `KIND_KEYED_READ` (L234), `KIND_FIRST_ONLY` (L235), `KIND_BOUNDED_SEARCH` (L236), `KIND_SWEEP` (L237), `KIND_DEFAULT` (L240), `LOOP_INLINE` (L254), `LOOP_PARAGRAPH` (L255), `LOOP_THRU` (L256), `LOOP_NONE` (L257), `END_OF_SET_CONDITIONS` (L265), `END_OF_SET_STATUS_FIELDS` (L282), `END_OF_SET_FLAG_SUFFIX` (L289), `CONDITION_CONNECTORS` (L292), `COMMENT_PREFIX` (L295), `EXPANDED_OBTAIN_TEMPLATE` (L297), `EXPANDED_PARENT_TEMPLATE` (L301), `EXPANDED_CALC_PARENT_TEMPLATE` (L307), `SKIPPED_NO_PATH_TEMPLATE` (L310), `SKIPPED_NO_RECORD_TEMPLATE` (L314), `SKIPPED_UNMAPPED_TEMPLATE` (L318), `SKIPPED_CALC_PARENT_TEMPLATE` (L322), `SKIPPED_NO_KEYWORD_TEMPLATE` (L326), `REMOVED_LR_STATUS_TEMPLATE` (L330), `EXPANDED_FILTER_TEMPLATE` (L338), `MODIFY_TEMPLATE` (L344), `STORE_TEMPLATE` (L345), `EXPANDED_UPDATE_TEMPLATE` (L347), `SKIPPED_STORE_AMBIGUOUS_TEMPLATE` (L350), `UNMAPPED_DIAGNOSTIC_TEMPLATE` (L359), `UNRENDERABLE_DIAGNOSTIC_TEMPLATE` (L362), `LRF_UPDATE_MESSAGES` (L367), `LRF_EXPANSION_MESSAGES` (L398), `LR_ACCESS_MESSAGES` (L465), `LR_STATUS_TOKEN_SQLCODE` (L519), `LR_STATUS_TOKEN_REPLACEMENT_ORDER` (L523), `ENABLE_LR_STATUS_TOKEN_REPLACEMENT` (L527), `LR_STATUS_TOKEN_MESSAGES` (L529), `TOKENS_OWNED_DOWNSTREAM` (L553), `__all__` (L558)

## Import declarations

```python
from __future__ import annotations
```

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
