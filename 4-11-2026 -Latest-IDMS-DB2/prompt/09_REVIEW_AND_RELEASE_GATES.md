# Review and independent release gates

## Metadata-aware review is required

`mainframe.zowe_steps.run_review` invokes `review/runner/review_file.py` with
`--workspace`. `review/runner/workspace_inputs.py` resolves a per-program source,
program identity, scoped mapping/DCLGEN/copybook evidence and provenance. Earlier
reviews without that metadata skipped important checks; a report with no failed
checks did not mean those dependencies were verified.

The review registry contains checks 01 through 36. Families cover fixed layout,
DB2 infrastructure, residual IDMS, headers, SQL error routing, host/include
integrity, retrieval/update/commit conversion, declarations, EOC/nested cursors,
restart, SQL/select/INTO/predicates, naming/PIC/copybook use, ordering/lifecycle,
LR status/path expansion, scope balance, doubly driven paragraphs, generated
structure, group representation and production evidence.

The reviewer must preserve failures, blocked checks and exceptions for critical
or major obligations. Do not change acceptance merely to make the six fixtures
green. Static reports record their actual inputs and skipped checks; unresolved
external definitions do not become local proof.

## Independent semantic checks

`audit_generated_batch` pairs candidates with originals and manual references,
checks operation/table/field/key coverage and transaction/not-found questions,
checks output layouts/population and group-representation contracts, and produces
workspace `Review/semantic_release_gate.txt`. Structural review and this gate
both participate in step_review and standalone step_upload.

Independent verification modules include copybook provenance, fixed record
layout, write/population contracts, representation mismatch, manual direct UPDATE
parity, archive-date predicate modeling and fixed-record binary comparison.
Their scopes differ: equality of manual UPDATE assignments is not source IDMS
zero-row proof; equal record length is not correct record population.

## Current limitations must remain explicit

Do not collapse operation-local SQLCODE handlers, infer external SQLERROR or
USERABEN termination, waive mapping width conflicts, or infer compiler acceptance
from static parsers. Character-to-packed group checks expose an unsafe boundary;
they do not implement a serialization codec. The current baseline has rejected
candidates and no native compiler/runtime evidence.

## Source map

- [Review CLI](modules/review/runner/review_file.md)
- [Per-program metadata adapter](modules/review/runner/workspace_inputs.md)
- [Check registry](modules/review/engine/registry.md)
- [Acceptance engine](modules/review/engine/reviewer.md)
- [Representation review](modules/review/checks/chk_35_group_representation.md)
- [Evidence review](modules/review/checks/chk_36_production_evidence.md)
- [Batch semantic/upload gate](modules/mainframe/zowe_semantic_release_gate.md)
- [Record comparison utility](modules/mainframe/verification/fixed_record_diff.md)

## V128 business-aware review refinements

Review applicability must come from source obligations rather than generated-code accidents.

- Retrieval-only IDMS `FINISH` is run-unit cleanup, not evidence that DB2 `COMMIT` is mandatory. Require COMMIT only for source update/explicit transaction work.
- Numeric/display legacy dates mapped to DB2 DATE/TIME/TIMESTAMP are representation-conversion cases and are not rejected merely because the DCLGEN host is alphanumeric. The actual conversion still requires validation.
- A generated local materialized record may intentionally retain a legacy group name; `FIELD OF GROUP` is not residual IDMS access when GROUP is declared as generated/local COBOL storage.
- Conversely, a uniquely mapped legacy business field that remains referenced in generated PROCEDURE DIVISION without declared/materialized storage is a failure. Fetching its DB2 host elsewhere is insufficient.
- Nested cursor early-stop checks are source-driven; do not infer business-stop requirements from arbitrary generated flags.

These refinements reduce false failures while adding a stronger data-flow failure for unmaterialized business values.

## V129 review corrections
Scope balance recognizes separator periods as implicit scope terminators, handles multiple IF/END-IF tokens on a line, ignores comments/literals and embedded SQL tokens, and still reports unmatched explicit terminators or unterminated paragraph scopes. IBM documents implicit period termination at https://www.ibm.com/docs/en/cobol-zos/6.4?topic=division-scope-terminators . It is a static scope check, not an equivalence proof or complete COBOL parser.
The end-of-set criterion is source-driven: an LRF program that only checks singleton success/failure does not automatically require a cursor EOC test. Residual status and SQL handling checks still run. Missing source evidence retains the conservative old requirement.
All semantic mapping indexes now detect export delimiters. Resolving an operation/table association proves coverage only; affected-row checks, representation conflicts and external compiler/runtime evidence remain separate requirements.
