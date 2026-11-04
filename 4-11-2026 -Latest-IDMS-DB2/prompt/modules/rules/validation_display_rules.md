# `rules/validation_display_rules.py`

Source: [rules/validation_display_rules.py](../../../rules/validation_display_rules.py) | 206 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `596458fc7b87b5d1d5bca13147dfb68f5e1ff81f8e93653416a06d7be0b2789a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Validation and diagnostics presentation rules.

## Module-level bindings

`SEVERITY_ERROR` (L31), `SEVERITY_WARNING` (L32), `SEVERITY_INFO` (L33), `SEVERITY_ORDER` (L35), `SEVERITY_ICONS` (L37), `ERROR_PREFIXES` (L50), `WARNING_PREFIXES` (L57), `INFO_PREFIXES` (L62), `ERROR_KEYWORDS` (L94), `WARNING_KEYWORDS` (L104), `UNCATEGORISED` (L129), `CATEGORY_SEPARATOR` (L130), `MAX_CATEGORY_WORDS` (L131), `FALLBACK_CATEGORY` (L135), `UI_VALIDATION_HEADER` (L140), `UI_VALIDATION_INTRO` (L141), `UI_METRIC_ERRORS` (L146), `UI_METRIC_WARNINGS` (L147), `UI_METRIC_INFO` (L148), `UI_METRIC_TOTAL` (L149), `UI_CLEAN_RUN` (L151), `UI_NO_MESSAGES` (L152), `UI_ERRORS_HEADER` (L155), `UI_WARNINGS_HEADER` (L156), `UI_INFO_HEADER` (L157), `UI_INFO_CAPTION` (L158), `UI_FILTER_SEVERITY` (L162), `UI_FILTER_CATEGORY` (L163), `UI_FILTER_SEARCH` (L164), `UI_FILTER_SEARCH_PLACEHOLDER` (L165), `UI_NO_MATCH` (L166), `UI_DIAGNOSTICS_HEADER` (L171), `UI_DIAGNOSTICS_INTRO` (L172), `UI_FILES_HEADER` (L177), `UI_FILES_EMPTY` (L178), `UI_PARSER_HEADER` (L179), `UI_PARSER_EMPTY` (L180), `UI_RAW_HEADER` (L183), `COLUMN_ROLE` (L185), `COLUMN_FILE` (L186), `COLUMN_SEVERITY` (L187), `COLUMN_CATEGORY` (L188), `COLUMN_MESSAGE` (L189), `COLUMN_COUNT` (L190), `MESSAGE_TABLE_COLUMNS` (L192), `UI_DOWNLOAD_VALIDATION` (L201), `UI_DOWNLOAD_DIAGNOSTICS` (L202), `UI_FILE_VALIDATION` (L203), `UI_FILE_DIAGNOSTICS` (L204), `UI_MIME_CSV` (L205), `UI_MIME_TEXT` (L206)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/message_classifier.py](../converter/ui/message_classifier.md)
- [converter/ui/output_tabs.py](../converter/ui/output_tabs.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
