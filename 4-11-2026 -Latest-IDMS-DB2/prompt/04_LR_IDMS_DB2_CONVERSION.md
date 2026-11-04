# LR -> classic IDMS -> DB2 content generation

## Concrete orchestration

`ConversionService.convert` runs `InputValidator`, returns empty converted text
with diagnostics for invalid input, otherwise delegates to `_run_pipeline` and
then runs `ProductionValidator`. The program runner writes a candidate; release
approval is a later independent operation.

The active `_run_pipeline` orders the following responsibilities:

1. Construct repositories, resolvers, generators, transformers and composers.
2. Expand LRF reads/navigation through `LrfPathExpander`, expand LRF writes
   through `LrfUpdateExpander`, then replace LR status tokens. The status stage
   consumes tokens from the other two and therefore follows them.
3. Resolve program kind from expanded source before write verbs are removed.
   Validate scoped mapping; build source/metadata restart context.
4. Publish program kind and source-proven parent/key/select state to the nested
   IDMS statement transformer before `CobolTransformer.transform` runs.
5. Transform classic IDMS statements; handle source-proven STORE parent reads;
   normalize restart-skip markers at their owning boundary.
6. Analyze original expanded flow for diagnostics and rewrite record-field
   references into exact DCLGEN hosts.
7. Generate SQL infrastructure/cursors, timestamp support and SQLERROR include;
   apply gated legacy restart behavior, cleanup and kind-aware commit cleanup.
8. Bind relationship keys and decompose source-proven composite/group transfers.
9. Run the layout/record/restart finishing subphase.
10. Number generated cursor paragraphs, guarantee cursor lifecycle, reconcile
    child early-stop wiring, normalize proven nested/flat FETCH-driven loops,
    and lower proven FIRST-only accesses to bounded SELECTs.
11. Apply source-preserving storage composition, schema date transfers,
    schema numeric-key guards and unused-copybook analysis.
12. Run final generated-output processing with lifecycle standardization off,
    then final procedure indentation, SQL Area B alignment and resequencing.

See [formatting](08_POSTPROCESS_FORMATTING_NUMBERING.md) for the finishing phase
and route-specific operations after service return. Do not infer pipeline order
from file names, registry tuple order, or an isolated class being present.

## LRF access distinctions

An area sweep is not a parent-child relationship walk. Do not attach unrelated
foreign-key predicates to an area scan. A relationship path requires a separately
resolved keyed parent and the correct child-set predicates. Downstream parent
field use can require an actual parent SELECT, not just key positioning.

FIRST-only, bounded predicate search, unbounded FIRST/NEXT traversal, nested
access and unknown shape are distinct. The whole logical block, its exits and
side effects must justify cursor removal. A paragraph/THRU loop with a data
predicate is not automatically eligible for an inline bounded-search renderer.

The original source and subschema status metadata must distinguish parent
not-found, empty child set and end-of-set before lowering to SQLCODE. Do not merge
source meanings merely because DB2 later reports `100` for multiple situations.

## Failures and boundaries

`_lrf_stage` records missing transformers/methods and exceptions rather than
pretending an unexecuted stage was successful. Unsupported update expansion
must keep executable source/refusal evidence rather than comment out a business
operation. Full source-to-target review remains necessary.

`_dump_expanded` can write expanded classic IDMS under the configured intermediate
folder. It is a trace artifact, not a new authoritative input or manual reference.
Keep any Markdown analysis of it under `prompt/temp/`.

## Source map

- [Service](modules/converter/pipeline/conversion_service.md)
- [Full content order](modules/converter/pipeline/conversion/conversion_pipeline.md)
- [State handoff and infrastructure steps](modules/converter/pipeline/conversion/conversion_pipeline_steps.md)
- [LR read/navigation expansion](modules/converter/transformers/lrf_path_expander.md)
- [LR write expansion](modules/converter/transformers/lrf_update_expander.md)
- [LR status conversion](modules/converter/transformers/lr_status_token_replacer.md)
- [Bounded access lowering](modules/converter/composers/bounded_lrf_singleton_rewriter.md)
- [Stage registry](modules/converter/pipeline/registry.md)

## V129 field-reference safety
The conversion component factory supplies copybook field metadata to FieldReferenceRewriter so unique bare-source fallback does not rewrite local copybook fields. Mixed converted/unconverted operands are handled individually. Source ambiguity and composite encoding conflicts remain refusal cases.

The conversion pipeline rechecks date comparisons after DCLGEN field qualification. The comparison assembler treats a continued `OF DCL...` qualifier as part of the IF condition; the rewriter moves that qualifier with its host into the helper form while preserving fixed-format sequence columns.
