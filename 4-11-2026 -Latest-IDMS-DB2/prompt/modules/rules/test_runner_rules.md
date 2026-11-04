# `rules/test_runner_rules.py`

Source: [rules/test_runner_rules.py](../../../rules/test_runner_rules.py) | 131 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `e261d6984d17085891d8508037988cbb1fb47cb0fa89a71c947a2a2460f13c9a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Test runner rules.

## Module-level bindings

`TESTS_FOLDER` (L18), `TEST_FILE_GLOB` (L19), `ALL_TESTS_LABEL` (L20), `PYTEST_MODULE` (L25), `PYTEST_BASE_ARGS` (L26), `JUNIT_ARG_TEMPLATE` (L32), `KEYWORD_ARG` (L33), `VERBOSE_ARG` (L34), `RUN_TIMEOUT_SECONDS` (L38), `PYTHONPATH_ENTRIES` (L43), `PYTHONPATH_SEPARATOR_KEY` (L44), `OUTCOME_PASSED` (L49), `OUTCOME_FAILED` (L50), `OUTCOME_ERROR` (L51), `OUTCOME_SKIPPED` (L52), `FAILING_OUTCOMES` (L54), `OUTCOME_ICONS` (L56), `UI_TAB_TITLE` (L66), `UI_HEADER` (L67), `UI_INTRO` (L68), `UI_RUN_BUTTON` (L72), `UI_RUNNING` (L73), `UI_TARGET_LABEL` (L74), `UI_KEYWORD_LABEL` (L75), `UI_KEYWORD_PLACEHOLDER` (L76), `UI_VERBOSE_LABEL` (L77), `UI_FAILURES_ONLY_LABEL` (L78), `UI_METRIC_TOTAL` (L80), `UI_METRIC_PASSED` (L81), `UI_METRIC_FAILED` (L82), `UI_METRIC_SKIPPED` (L83), `UI_METRIC_DURATION` (L84), `UI_TABLE_HEADER` (L86), `UI_DETAIL_HEADER` (L87), `UI_OUTPUT_HEADER` (L88), `UI_COMMAND_HEADER` (L89), `UI_NO_RESULT` (L91), `UI_NO_TESTS_FOUND` (L94), `UI_ALL_PASSED` (L97), `UI_SOME_FAILED` (L98), `UI_TIMED_OUT` (L99), `UI_RUN_ERROR` (L102), `UI_DOWNLOAD_CSV` (L104), `UI_DOWNLOAD_LOG` (L105), `UI_FILE_CSV` (L106), `UI_FILE_LOG` (L107), `UI_MIME_CSV` (L108), `UI_MIME_TEXT` (L109), `TIMESTAMP_FORMAT` (L111), `FILE_TIMESTAMP_FORMAT` (L112), `COLUMN_OUTCOME` (L117), `COLUMN_MODULE` (L118), `COLUMN_TEST` (L119), `COLUMN_DURATION` (L120), `COLUMN_MESSAGE` (L121), `TABLE_COLUMNS` (L123), `MESSAGE_PREVIEW_LENGTH` (L131)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_page.py](../converter/ui/main_page.md)
- [converter/ui/test_panel.py](../converter/ui/test_panel.md)
- [runners/pytest_runner.py](../runners/pytest_runner.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
