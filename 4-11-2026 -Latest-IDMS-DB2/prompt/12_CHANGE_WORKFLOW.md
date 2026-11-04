# Mandatory change and documentation workflow

## Placement rules

Root `readme.md` is the only Markdown outside `prompt/`. Durable descriptions,
source maps, contracts and current known issues belong under `prompt/`. Every
iteration plan, temporary audit, scratch analysis and draft Markdown belongs
under **`prompt/temp/`**. Use descriptive iteration/topic names and remove obsolete
scratch work when it is no longer useful. Do not recreate historical root reports
or an uppercase `PROMPT/` directory.

The documentation index is a navigation system: start with the task router, read
one guide and the relevant module notes, and inspect only the affected source,
callers and tests. Do not bulk-load the entire codebase or all generated notes.

## Before changing Python

Run `python prompt/tools/maintain_docs.py check`. Read the current baseline and
relevant guide. Reproduce the failure using immutable original inputs and manual
references; trace the actual pipeline owner and data contract. Missing metadata
is a visible blocker, not permission to infer a program-specific exception.

Record an iteration plan in `prompt/temp/` when useful. Identify affected
modules, generic behavior, refusal cases, tests and review expectations. Do not
manually patch candidate COBOL or change the manual reference to force a pass.

## Make code and documentation changes together

Update the corresponding owning guide for every changed parser, resolver, rule,
generator, pipeline boundary, review check, test contract or configuration.
Explain inputs, ordered transformations, outputs, error/refusal behavior and tests.
Use source symbols and paths, not just an iteration-number success statement.
Promote reusable findings out of `temp/` into these guides; retain unresolved
issues in the baseline guide until supported evidence resolves them.

Each Python file has a generated note under `prompt/modules/<source path>.md`.
Do not hand-edit those notes: the source-based refresh regenerates their symbols,
imports, lexical conditions and call lists. Full implementations are not copied
into Markdown. Bounded call/condition lists point to exact source spans when a
module needs deeper inspection.

## Refresh and validation

```bash
python prompt/tools/maintain_docs.py refresh
python prompt/tools/maintain_docs.py check
```

On a subsequent code change, refresh compares source hashes with the old manifest.
It requires each owning guide to have changed or to be explicitly reviewed. If a
guide remains accurate, use its exact path:

```bash
python prompt/tools/maintain_docs.py refresh \
  --reviewed-guide prompt/04_LR_IDMS_DB2_CONVERSION.md \
  --reviewed-guide prompt/10_TESTING_AND_VALIDATION.md
```

Only acknowledge guides actually reviewed. The tool writes a pending review list
to `prompt/temp/documentation_sync_needed.json` if review is missing, and exits
with code 2. Refresh itself is not a semantic verification of the narrative.

The checker validates full engine/test Python coverage, source and generated-note
hashes, documentation tooling hashes, required guides, root readme metadata,
Markdown placement and local links. It catches additions/removals, stale notes,
manual edits to generated notes and out-of-policy `.md` files. It does not execute
engine code, import its dependencies, or prove dynamic call graphs. Python cache
folders and virtual environments are excluded from source scanning; Markdown
placement still applies to generated cache READMEs.

## Documentation tooling ownership

`prompt/tools/maintain_docs.py` is a standard-library AST scanner/renderer/checker.
`prompt/tools/test_maintain_docs.py` tests it in isolated temporary repositories.
These two documentation-only Python files are excluded from the engine module
count and tracked separately in `prompt/source_manifest.json`. Changes to the
tooling require review of this workflow guide. The source-map `guide_for`
function assigns a primary guide by module location/name; cross-cutting changes
can require additional guides even if the tool lists only one.

## Complete an iteration

Run focused tests, shared regressions and conversion/review as appropriate; keep
all evidence's scope and exit code explicit. Confirm original source, copybooks,
DCLGENs, mappings and manual COBOL were not unintentionally changed. Preserve
release blockers instead of redefining acceptance. Record actual test results
in an iteration Markdown under `prompt/temp/`, update the durable baseline when
results change, and rerun documentation checks before packaging.

Do not imply mainframe compilation, DB2 execution, runtime equivalence or 2,000-
program scalability from Python/static tests alone. A documentation-only release
must explicitly say it did not change or recertify conversion behavior.

## AI and Human Review synchronization

Durable migration behavior has two documentation audiences:

- `prompt/` is the AI/implementation knowledge layer and may describe analyzers, generation contracts, validators and tests.
- `Human Review/` is the COBOL/business review layer. It explains the same observable migration rule as short COBOL-oriented logic/pseudocode and must not depend on Python module names.

When a Python change adds or changes observable IDMS-to-DB2 behavior, update the owning `prompt/` guide **and** the matching Human Review rule in the same iteration. Program-specific comparison evidence stays in `prompt/temp/`; only reusable scenario rules are promoted to the durable folders.
