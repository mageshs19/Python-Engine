# Rules, regex grammars, catalogs and generic behavior

## Roles and boundaries

`rules/` holds shared constants, policies, statement templates and conventions.
`patterns/` holds matching grammars and extraction patterns. `catalogs/` provides
catalog/selection structures. `converter/rules/` is an additional converter-local
layer. Locate the actual importer in the module note before changing a similarly
named definition or introducing a duplicate constant.

A generic rule is selected using source syntax, access/flow structure and
metadata contracts. It is not generic merely because its implementation lives
in a shared file. Program-id-specific field rewriting or hidden table constants
can still violate that contract. Existing source business literals such as event
codes are inputs to preserve, not automatically hardcoded engine defects.

## Match logical statements, not raw lines

COBOL statements can span fixed-format records. Sequence columns, indicators,
comments and string literals must not be interpreted as executable syntax.
Multi-line MOVE, PERFORM/THRU, IF, SQL and IDMS accesses require bounded collectors
and correct statement boundaries. A permissive regex can consume the next WRITE
or END-IF and silently drop behavior.

Update grammar and owning parser/transformer together. Test positive forms,
wrapped forms, comments/literals containing keywords, unsupported extra clauses,
and negative/refusal cases. Changing a pattern without the matching collector
and code-generation contracts is not a complete fix.

## Stage catalog is not the whole pipeline

`converter/pipeline/registry.py` creates factories for nine registered stages.
The actual content/layout call sites still determine when each stage executes.
Do not reorder its tuple and claim every direct invocation moved. A disabled
registered stage can suppress a delegated call; existence of a factory does not
prove it is reached. Inspect the pipeline and stage wiring tests.

## Rules to preserve during future fixes

Keep mapping-driven table/host/key resolution, source-preserved business flow,
explicit unsupported/ambiguous diagnostics, minimum justified helpers and no
hand-patched generated COBOL. Never weaken a release gate to compensate for a
conversion rule that does not implement the source semantics. Validate aliases,
record widths, date formats, SQLCODE lifetime and PERFORM THRU spans independently.

## Source map

- [All rule/module package indexes](MODULE_INDEX.md)
- [Stage registry](modules/converter/pipeline/registry.md)
- [Stage execution](modules/converter/pipeline/run.md)
- [Cursor conventions](modules/rules/cursor_rules.md)
- [Record materialization conventions](modules/rules/record_materialisation_rules.md)
- [Shared converter rules](modules/converter/rules/common_rules.md)

## V129 generic resolution boundary
New bare-field resolution uses mapping uniqueness, declaration exclusion and DCLGEN DATE evidence; it adds no program, record, table or field exception list. Existing site-specific catalogs and naming conventions are unchanged and still require site validation.

The DB2 date condition continuation pattern includes a continued OF/IN DCLGEN qualifier. A continued host is substituted by the date helper as one logical operand and its now-empty qualifier line is blanked without changing fixed-format sequence data.
