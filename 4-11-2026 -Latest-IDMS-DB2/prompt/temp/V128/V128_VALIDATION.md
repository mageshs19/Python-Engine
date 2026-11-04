# V128 manual/business parity validation

## Scope
Compared all six supplied IDMS source / manual DB2 / generated DB2 program triplets. Names and paragraph numbering were not required to match; review focused on business behavior, SQL/data flow, status handling, record representation, restart/transaction behavior and output wiring.

Programs reviewed: VMDZ1526, VMDZ1567, VMDZ4302, VMDZ4310, VMDZ4420, VMDZ7200.

## Generic engine/review changes

1. Detect mapping-file delimiter from content; the supplied `.csv` is tab-delimited and now loads 855 mapping rows.
2. Discover uniquely-owned unqualified legacy fields as downstream cursor projection requirements; ambiguous ownership is not guessed.
3. Retrieval FINISH no longer fabricates a COMMIT requirement.
4. Legacy numeric/display date mapped to DB2 temporal host is reviewed as a representation conversion rather than a generic numeric/alphanumeric mismatch.
5. Nested cursor business early-stop is required only when original source has an additional compound stop condition.
6. Review fails when a uniquely mapped legacy business field is still used after conversion without declared/materialized storage.
7. A declared generated/materialized group retaining a legacy record name is local COBOL storage, not residual IDMS access.

## Latest structural review

| Program | Result | Principal remaining issue |
|---|---|---|
| VMDZ1526 | REJECTED | FFRECAB references/scope/status defects plus NR_IDGOOD mapping-vs-DCLGEN 20/28 conflict. |
| VMDZ1567 | ACCEPTED | Structural checks pass; semantic gate still has unresolved source-operation correlation. |
| VMDZ4302 | REJECTED | AM-CN-STOCK and DA-CR-EVENT-PROD are fetched but not materialized into downstream business logic; NR_IDGOOD representation conflict also remains. |
| VMDZ4310 | REJECTED | CHAR(28) host copied into incompatible packed/20-byte group and mapping-vs-DCLGEN width conflict. |
| VMDZ4420 | REJECTED | Same serialized identifier representation conflict. |
| VMDZ7200 | ACCEPTED | Structural checks pass after recognizing declared materialized VMBFAS; semantic operation correlation remains unresolved. |

Review pipeline exits 2 because four programs remain rejected and semantic release evidence is unresolved. This is expected and is not a conversion-step crash.

## Tests

Targeted V128 business/review/parser tests: PASS.

Full uploaded-workspace suite:
- 2,073 passed
- 10 skipped
- 11 failed

All 11 failures depend on historical fixture/artifact paths absent from the uploaded workspace (for example `Validated Output/`, `_baseline/`, `_expanded/`, and an older mapping filename). The untouched uploaded baseline produces 15 failures, 2,042 passes and 12 skips; V128 therefore removes four baseline functional failures but does not fabricate missing fixtures.

`python -m compileall -q converter mainframe review rules patterns tests`: PASS.

Documentation-tool tests: 17 passed.
Documentation coverage/link/source-freshness check: PASS (1,028 Python files, 1,028 module notes).

## Asset integrity

SHA-256 comparison of all files in Program, Manual Output, DCLGen, Copybook, Subschema and Mapping Sheet: 30/30 byte-identical to the uploaded baseline.

## Evidence limits

No Zowe fetch or mainframe access was performed. No DB2 precompile, COBOL compile/link, DB2 runtime execution or file-output reconciliation was performed. Manual DB2 programs are comparison evidence and are not treated as automatically correct when they conflict with original source or metadata.
