# `review/standards/wording.py`

Source: [review/standards/wording.py](../../../../review/standards/wording.py) | 168 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `7deaff1b92f707a82cbac283e21fe7c9e816b41b2efbb5337a3a54c9513241a9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Display text only.

## Module-level bindings

`SYMBOL` (L11), `VALUE_UNNAMED` (L19), `VALUE_UNKNOWN` (L20), `VALUE_IN_MEMORY` (L21), `REPORT_TITLE` (L24), `RULE` (L25), `F_PROGRAM` (L27), `F_KIND` (L28), `F_SOURCE` (L29), `F_WHEN` (L30), `F_TOTALS` (L31), `F_CRITERIA` (L35), `F_RESULT` (L39), `F_BLOCKING` (L40), `ACCEPTED` (L42), `REJECTED` (L43), `H_DETAIL` (L46), `H_FAILURES` (L47), `NO_FAILURES` (L48), `F_CHECK` (L50), `F_CRIT` (L51), `F_FIND` (L52), `F_NOTE` (L53), `F_FAIL_CHECK` (L55), `F_FAIL_CRIT` (L56), `F_FAIL_NOTE` (L57), `CSV_HEADER` (L60), `CSV_SUMMARY_HEADER` (L64), `CSV_TIMESTAMP_FORMAT` (L68), `CSV_LINE_SEPARATOR` (L69), `UI_TITLE` (L72), `UI_NOT_READY` (L73), `UI_RUN` (L74), `UI_RUN_HINT` (L75), `UI_ACCEPTED` (L76), `UI_REJECTED` (L77), `UI_UNAVAILABLE` (L78), `UI_TARGET` (L80), `UI_STALE` (L81), `UI_SCOPE` (L85), `UI_PROGRAM` (L90), `UI_METRIC_PASSED` (L91), `UI_METRIC_FAILED` (L92), `UI_METRIC_SKIPPED` (L93), `UI_METRIC_BLOCKED` (L94), `UI_CRITERIA` (L95), `UI_FILTER_FAILURES` (L100), `UI_FILTER_SKIPS` (L101), `UI_CHECK_LABEL` (L102), `UI_CRITERION` (L103), `UI_MARK_PASS` (L104), `UI_DOWNLOAD_TEXT` (L106), `UI_DOWNLOAD_CSV` (L107), `UI_FILE_TEXT` (L108), `UI_FILE_CSV` (L109), `UI_MIME_TEXT` (L110), `UI_MIME_CSV` (L111), `UI_DEFAULT_STEM` (L112), `H_RUN_FILE` (L115), `H_RUN_RETRIEVAL` (L116), `H_RUN_UPDATE` (L117), `MSG_REVIEWED_FOLDER` (L119), `MSG_PROGRAM_FOLDER` (L120), `MSG_PROGRAM_COUNT` (L121), `MSG_OUTPUT_FOLDER` (L122), `MSG_REPORT_FOLDER` (L123), `MSG_FILE_COUNT` (L124), `MSG_PROGRAM_KIND` (L125), `MSG_SUMMARY` (L128), `MSG_CONVERSION_FAILED` (L129), `MSG_REPORTS_WRITTEN` (L130), `MSG_QUIET_LINE` (L131), `MSG_QUIET_BLOCKING` (L132), `MSG_ERROR` (L135), `MSG_FILE_NOT_FOUND` (L136), `MSG_FOLDER_NOT_FOUND` (L137), `MSG_PATH_NOT_FOLDER` (L138), `MSG_SOURCE_NOT_FOUND` (L139), `MSG_CONVERSION_ERROR` (L140), `MSG_NO_OUTPUT_TITLE` (L143), `MSG_NO_OUTPUT_FOUND` (L144), `MSG_NO_OUTPUT_HINT` (L148), `MSG_NO_PROGRAMS_TITLE` (L156), `MSG_NO_PROGRAMS_FOUND` (L157), `MSG_NO_PROGRAMS_HINT` (L161), `KIND_LABEL_RETRIEVAL` (L166), `KIND_LABEL_UPDATE` (L167), `MSG_PROGRAM_KIND_AUTO` (L168)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/report/csv_writer.py](../report/csv_writer.md)
- [review/report/text_writer.py](../report/text_writer.md)
- [review/runner/review_file.py](../runner/review_file.md)
- [review/ui/review_panel.py](../ui/review_panel.md)

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
