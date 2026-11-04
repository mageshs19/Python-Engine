# `mainframe/zowe_rules_pipeline.py`

Source: [mainframe/zowe_rules_pipeline.py](../../../mainframe/zowe_rules_pipeline.py) | 81 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `7fd39ac01e4442296a02d27394df94cf6d9e67b500ccd842b6479c9c17f486d8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Workspace layout, pipeline steps, runners and console templates.

## Module-level bindings

`WORKSPACE_SUBFOLDERS` (L11), `STEP_FETCH` (L23), `STEP_CONVERT` (L24), `STEP_REVIEW` (L25), `STEP_UPLOAD` (L26), `STEP_ALL` (L27), `STEP_SHOW` (L28), `STEP_INIT` (L29), `STEP_CLEAN` (L30), `STEP_PLAN` (L31), `PIPELINE_STEPS` (L33), `PIPELINE_COMMANDS` (L34), `CONVERT_RUNNER` (L43), `REVIEW_RUNNER` (L44), `REVIEW_KIND` (L45), `IDMS_INPUT_DIR_KEY` (L47), `PYTHONPATH_KEY` (L48), `PYTHONPATH_ENTRIES` (L49), `UNBUFFERED_KEY` (L50), `STEP_TIMEOUT_SECONDS` (L51), `STATUS_OK` (L54), `STATUS_FAILED` (L55), `STATUS_SKIPPED` (L56), `STATUS_NOTHING` (L57), `EXIT_OK` (L59), `EXIT_NOTHING` (L60), `EXIT_ERROR` (L61), `PIPELINE_TITLE` (L64), `STEP_HEADER_TEMPLATE` (L65), `STEP_OK_TEMPLATE` (L66), `STEP_FAILED_TEMPLATE` (L67), `STEP_SKIPPED_TEMPLATE` (L68), `STEP_NOTHING_TEMPLATE` (L69), `SUMMARY_HEADER` (L70), `SUMMARY_ROW_TEMPLATE` (L71), `VERDICT_OK` (L72), `VERDICT_FAILED_TEMPLATE` (L73), `WORKSPACE_CREATED_TEMPLATE` (L74), `WORKSPACE_READY_TEMPLATE` (L75), `CLEAN_REMOVED_TEMPLATE` (L76), `MAPPING_MISSING_TEMPLATE` (L77), `RUNNER_MISSING_TEMPLATE` (L81)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_rules.py](zowe_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
