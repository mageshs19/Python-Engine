# SQL, cursor ownership, status and business paragraph wiring

## SQL generation contract

SQL generators use resolved table/column/key metadata and exact DCLGEN host
names. SELECT and INTO/FETCH positions must correspond. Key predicates must be
complete for the resolved operation; unrelated foreign keys are not interchangeable
with a CALC key. SELECT projections also depend on downstream source field use,
not merely fields convenient to the access statement.

Source-proven keyed parent retrieval must populate hosts used by business MOVEs.
An UPDATE positioning read has different semantics and must not be mistaken for
an optional retrieval SELECT. Bounded first-row queries retain proven predicates,
ordering and row bounds; the compiler/runtime consequences are separate checks.

## One loop owner per cursor

The engine has several lifecycle composers because source shapes differ. A
successful rewrite must establish exactly one driver, one success-side business
invocation per row, appropriate EOC state, and a close path. Two FETCH call sites
can be a legitimate prime-and-tail pattern; their mere count does not prove a
bug. Converting that pattern to FETCH-owned business processing requires proof
of both edges, the enclosing PERFORM/THRU span and all exits.

`NestedParentFetchNormalizer` handles a proven nested-parent shape.
`FlatFetchDriveNormalizer` handles a proven flat priming/tail shape. Child early
stop reconciliation runs after lifecycle construction so it sees actual
paragraph/flag ownership. The proof must be structural, not based on words like
HOOFDVERWERKING, specific table names or paragraph number ranges.

Do not leave both FETCH-success -> business and business-tail -> FETCH driving
edges after normalization: that can introduce recursion or duplicate processing.
Do not attach a child's business stop flag to the parent cursor.

## Status lifecycle

FETCH sets its own EOC flag on `SQLCODE = 100`. CLOSE and later SQL replace
SQLCODE; an earlier fetch result must not be retested through stale SQLCODE.
Use the source-proven cursor state where needed. A required state flag is not an
unnecessary helper simply because a particular manual example names it differently.

Preserve source error/business branches and operation-local association. Two
source statuses collapsing into two identical `IF SQLCODE = 100` blocks are not
automatically equivalent to one manual EVALUATE. Nonreturning behavior of
USERABEN/SQLERROR must not be assumed without the site routines.

## Output-write placement and THRU safety

A conditional write extracted into a helper paragraph must be placed outside any
source PERFORM THRU range that would otherwise fall through into it. Its explicit
call must remain inside the business guard. Buffer initialization and counters
belong to their proven per-record/per-program lifetime, not whichever location
resembles the manual listing.

`ProcedureControlFlowGraphBuilder` supports local labels, sections, PERFORM calls
and ranges. It is a useful check but not proof of external error routines, field
representation or full data equivalence.

## Tests to require on changes

Cover empty set, one row, multiple rows, early business stop, nested parent/child,
prime/tail normalization, THRU boundaries, duplicate labels, ambiguous ownership,
and unchanged fallback on refused transformations. Use renamed synthetic programs
and paragraphs so a passing example cannot hide identifier-specific rules.

## Source map

- [Nested-parent normalizer](modules/converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.md)
- [Flat FETCH normalizer](modules/converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.md)
- [Child early stop](modules/converter/composers/cleanup/child_fetch_early_stop_cleanup.md)
- [Output-write extraction](modules/converter/composers/output_write_paragraph_composer.md)
- [Relationship key binding](modules/converter/composers/lrf_key_binding_composer.md)
- [Procedure graph](modules/converter/analyzers/program_flow/procedure_control_flow_graph.md)

## V128 business-parity rules

The source/manual/generated comparison adds two cursor obligations:

- Cursor projection includes every uniquely attributable source field consumed downstream by business logic, conditions, output or calls—not only relationship/key columns.
- Nested child traversal receives an extra business early-stop only when original source behavior has one. A source loop that runs until ordinary IDMS status/end-of-set means complete traversal and must not be rejected merely because unrelated generated code sets a `Y` flag.

After FETCH, downstream business fields must also satisfy [BR-004 legacy field materialization](business_rules/BR-004_LEGACY_FIELD_MATERIALISATION.md). A correct SELECT/FETCH column count does not establish business equivalence when PROCEDURE DIVISION still reads an undeclared legacy field.

## V129 bare-reference and mixed-reference resolution
FieldReferenceRewriter no longer skips an entire business statement because one operand is already DCLGEN-qualified. Qualified replacements remain token-specific and idempotent. A bare elementary field may fall back to a unique mapping owner without a paragraph-derived active record. Local declarations and supplied copybook field names are excluded; multiple mapping owners and protected work/control names are not guessed.
Bare mapped DATE operands are qualified only in complete IF condition spans when an actual DCLGEN DATE X(10) host is proven and the existing comparison converter supports its host naming. Assignment destinations and unsupported formats are unchanged. The existing date conversion stage then emits comparison helpers and sentinel handling. This does not establish an encoding for serialized packed-field groups.

Mapped date comparisons receive a second idempotent conversion after field references are resolved. This covers a host qualifier emitted on a fixed-format continuation line after the initial comparison pass.
