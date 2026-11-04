# V128 six-program source/manual/generated parity evidence

This is iteration evidence, not a permanent migration rule. Manual DB2 is used as independent implementation evidence; source COBOL plus mapping/DCLGEN/copybook/subschema evidence remains necessary when the manual differs.

| Program | Scenario | Current structural review | Main business assessment |
|---|---|---|---|
| VMDZ1526 | Update + restart + insert/update | REJECTED | Restart/update structure exists, but undeclared FFRECAB references, scope defects, legacy status handling and the NR_IDGOOD 20/28 metadata conflict prevent equivalence. |
| VMDZ1567 | Update + restart + keyed update | ACCEPTED structurally | Generated restart/update shape is close to manual; semantic gate still cannot correlate seven source operations unambiguously, so runtime/business equivalence is not certified. |
| VMDZ4302 | Nested parent/child retrieval + conditional output | REJECTED | Cursor projection now includes downstream-used DB2 data, but business code still reads unmaterialized AM-CN-STOCK and DA-CR-EVENT-PROD; NR_IDGOOD representation also conflicts. Source child traversal is complete-to-EOS, so an artificial early-stop is not required. |
| VMDZ4310 | Keyed parent + bounded/latest child + output | REJECTED | SQL shape broadly follows the source/manual scenario, but raw CHAR(28) to packed/20-byte business group and mapping-vs-DCLGEN width conflict block correctness. Manual parent projection itself is not treated as authority where it omits a later-used amount. |
| VMDZ4420 | Nested parent/child retrieval | REJECTED | Cursor lifecycle/relationship checks pass; the shared NR_IDGOOD representation conflict remains a business-data blocker. |
| VMDZ7200 | Flat retrieval/archive output | ACCEPTED structurally | Date/category and materialized-record review false positives were corrected. Semantic operation correlation remains unresolved, so structural acceptance is not runtime proof. |

## Generic changes from this comparison

1. Mapping text delimiter is detected rather than assumed from `.csv` extension.
2. Unique unqualified legacy field usage contributes to cursor projection discovery.
3. Retrieval FINISH does not fabricate a COMMIT requirement.
4. Numeric/display legacy dates mapped to DB2 temporal hosts are treated as representation conversions, not generic category mismatches.
5. Nested-cursor early-stop is required only when the original source has an extra business stop condition.
6. A mapped legacy business field still used after conversion without declared/materialized storage fails review.
7. A declared materialized legacy-named record group is local COBOL storage and is not falsely classified as residual IDMS database access.

## Remaining generic gaps

- Generate/materialize compatible scalar, temporal and composite business values after FETCH without retaining undeclared legacy fields.
- Resolve LRF/schema identities strongly enough for the semantic gate to correlate source operations to SQL without manual assumptions.
- Resolve the NR_IDGOOD mapping/DCLGEN/legacy-layout conflict through authoritative metadata/business encoding evidence; do not guess.
- Repair VMDZ1526 scope/status/FFRECAB generation generically.
