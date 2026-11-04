# UPDATE route, restart context and transactions

## Route and metadata handoff

`runners/convert_programs.measure_program_kind` examines source before conversion.
The selected update runner still invokes the shared `ConversionService`, then
calls `enhance_update_program`. Inside the shared pipeline, kind is measured
again from expanded LRF source and handed to consumers before the classic IDMS
transform. Do not remove a keyed read or commit because a caller omitted this
handoff.

The top-level kind reader currently catches a source OSError and falls back to
retrieval with a printed warning. That is an observed limitation, not a safe
production fallback guarantee. The documentation-only reorganization does not
alter it.

## Operation contracts

MODIFY/STORE/ERASE lowering must preserve target table, complete predicates,
changed fields, source not-found branches and transaction boundaries. Audit-host
population is part of update processing; the existence of DCLGEN declarations
alone is not assignment evidence.

A source OBTAIN CALC followed by MODIFY can become a keyed UPDATE in a manual
reference, but the absence of a matching row is not proved by merely observing
a successful-path counter. `manual_direct_update_parity` distinguishes matching
a supplied manual implementation from proving original IDMS missing-record
semantics. Neither scope should silently overwrite the other.

## Restart ownership

`RestartContextBuilder` uses expanded source and authoritative metadata before
source statements disappear. The finishing phase receives this run-scoped context
because text-only finishing cannot rediscover all source information. Metadata-
driven restart injection owns the modern path; the older SELECT-paragraph restart
generator is gated when the context exists, preventing duplicate declarations
and calls.

Restart payload layout, checkpoint key, last processed row, counters, COMMIT,
ROLLBACK, reopen and cursor hold behavior are separate obligations. Do not insert
a hardcoded checkpoint size/table or assume a generated restart paragraph
implements the whole source business path. `update_restart_skip` explicitly
replaces some unmappable blocks with a comment/CONTINUE; such generation needs
an independent release check, not a completion claim.

## Required change evidence

Test both retrieval and update programs for any shared cleanup change. Prove
which component owns every transaction/restart insertion. Exercise first run,
restart, empty checkpoint lookup, zero-row update, failure before/after commit,
and repeated batch invocation where relevant. Runtime transaction semantics
remain outside Python unit-test proof.

## Source map

- [Kind dispatcher](modules/runners/convert_programs.md)
- [Update program runner](modules/runners/update/update_program_converter.md)
- [Update enhancer](modules/converter/postprocess/update_program_enhancer.md)
- [Restart context](modules/converter/resolvers/restart_context_builder.md)
- [Pipeline context/handoff](modules/converter/pipeline/conversion/conversion_pipeline_steps.md)
- [Restart finishing injection](modules/converter/pipeline/conversion/conversion_layout_steps.md)
- [Manual direct-update parity](modules/mainframe/verification/manual_direct_update_parity.md)
