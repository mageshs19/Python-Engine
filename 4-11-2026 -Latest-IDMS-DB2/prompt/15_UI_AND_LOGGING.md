# UI, logging and operational adapters

## UI route

`converter/app.py` configures Streamlit and calls `converter.ui.main_page`.
Upload/parsing/controller panels eventually construct conversion inputs or invoke
review functions. The UI is an adapter, not a second source of business rules.
Any behavior introduced only in UI actions must also be considered for the batch
route; a successful UI demonstration does not prove `mainframe.zowe_pipeline`
uses the same metadata or ordering.

The UI advertises mapping, DCLGEN, optional copybooks and source upload. A missing
optional upload can still prevent a required output-layout or provenance check.
Do not interpret optional UI wording as a release waiver.

## Logging and diagnostics

The batch subprocess adapter captures full output in workspace Logs and prints
a digest. `LoggerFactory` and the logging modules support converter diagnostics;
messages from components must be propagated into conversion/review evidence.
A log line saying a stage is configured is not proof it executed or that its
candidate passed validation.

Avoid per-record debug DISPLAY insertion merely to make output look traceable;
operational verbosity and business logic are different concerns. Preserve actual
error context and SQL location semantics rather than inventing an SQLCODE for a
non-SQL input-validation failure.

Scratch analysis of logs belongs in `prompt/temp/`; original `.log` evidence
remains in its runtime folder. Do not put secrets or actual mainframe credentials
in Markdown, copied diagnostics, examples or generated module descriptions.

## Source map

- [Streamlit entry](modules/converter/app.md)
- [Main UI page](modules/converter/ui/main_page.md)
- [Logger factory](modules/converter/infrastructure/logger_factory.md)
- [Batch transcript/digest adapter](modules/mainframe/zowe_steps.md)
- [Console rendering](modules/mainframe/zowe_console.md)
- [Review UI](modules/review/ui/review_panel.md)
