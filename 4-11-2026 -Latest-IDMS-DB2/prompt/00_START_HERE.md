# Start here: minimal context for the next change

Read the root [readme.md](../readme.md) for the two mandatory documentation rules.
This folder is the maintained source map; `temp/` is scratch, not a permanent
knowledge base. The engine is not production-certified merely because it has
comprehensive notes or passing Python tests.

## Efficient reading sequence

1. Read [current baseline](13_CURRENT_BASELINE_AND_OPEN_ISSUES.md) and the one
   owning guide matching the task below.
2. Open [MODULE_INDEX](MODULE_INDEX.md), then the relevant package index and
   per-file module notes. These include exact source paths, signatures, source
   line spans, observed calls, conditions, imports and available importing tests.
3. Run `python prompt/tools/maintain_docs.py check`. If stale, inspect the changed
   Python source before relying on its note. Read only that source and necessary
   dependencies, not the entire repository.
4. After the change, update its owning guide, refresh its notes, run appropriate
   regression tests, and rerun the documentation check. Scratch Markdown goes
   only in `prompt/temp/`.

## Task router

| Task | Read first |
|---|---|
| Understand the whole system | [Architecture](01_SYSTEM_ARCHITECTURE.md) |
| Batch command, clean, fetch, review, upload | [Mainframe pipeline](02_MAINFRAME_PIPELINE.md) |
| Mapping, DCLGEN, copybook parsing, names and keys | [Metadata](03_INPUT_METADATA_AND_RESOLUTION.md) |
| Logical record to IDMS to DB2 conversion/order | [Conversion](04_LR_IDMS_DB2_CONVERSION.md) |
| SQL, cursor loops, status, FETCH/business wiring | [Cursor and flow](05_SQL_CURSOR_AND_BUSINESS_FLOW.md) |
| Field widths, packed groups, FILLER, dates, helper variables | [Storage contracts](06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md) |
| UPDATE, checkpoint, COMMIT, restart | [Update/restart](07_UPDATE_RESTART_AND_TRANSACTIONS.md) |
| Fixed format, paragraph numbering, final output passes | [Postprocessing](08_POSTPROCESS_FORMATTING_NUMBERING.md) |
| A review accepts/skips/rejects incorrectly | [Review/release](09_REVIEW_AND_RELEASE_GATES.md) |
| Regressions, compiler limits, file comparison | [Validation](10_TESTING_AND_VALIDATION.md) |
| Paths, environment, CLI vs UI, installation | [Configuration](11_CONFIGURATION_AND_ENTRYPOINTS.md) |
| Change process or Markdown maintenance | [Workflow](12_CHANGE_WORKFLOW.md) |
| Rule constants, regex grammar or registries | [Rules/catalogs](14_RULES_PATTERNS_AND_CATALOGS.md) |
| Streamlit or logs | [UI/logging](15_UI_AND_LOGGING.md) |

## Evidence hierarchy

Python implementation and actual input metadata are authoritative for what the
converter does. Original IDMS defines the starting behavior. Manual DB2 is a
comparison reference, not proof that every manual statement is correct. Generated
COBOL and review results are evidence to inspect, not instructions to weaken a
rule. Historical reports, source comments and automatically extracted docstrings
can be stale; notes explicitly label source-declared descriptions as such.

A module note is not a complete interprocedural control-flow proof. Runtime
injection, dynamically imported classes, external copybooks and mainframe error
routines require additional inspection. Never infer production approval from
source hashes or an AST inventory.
