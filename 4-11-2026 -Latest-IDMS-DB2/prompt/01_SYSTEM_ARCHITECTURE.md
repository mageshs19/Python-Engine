# End-to-end architecture and ownership

## Actual primary path

```text
mainframe.zowe_pipeline
  -> zowe_pipeline_steps (fetch / convert / review / upload)
     -> zowe_steps subprocess environment
        -> runners/convert_programs.py
           -> load shared mapping + DCLGEN + copybook metadata
           -> measure source program kind
           -> retrieval or update program converter
              -> load logical-record/subschema definitions
              -> ConversionInput
              -> ConversionService.convert
                 -> validate input
                 -> ConversionPipeline._run_pipeline
                    -> LRF read expansion + write expansion + status lowering
                    -> classic-IDMS-to-DB2 statement and field transformations
                    -> SQL infrastructure + layout + source-proven flow cleanup
                    -> final formatting and production validator
              -> route-specific final processing and candidate file
        -> review/runner/review_file.py --workspace ...
           -> per-program original + metadata pairing
           -> 36 registered structural/evidence checks
     -> zowe_semantic_release_gate.audit_generated_batch
     -> upload only after structural + semantic + copybook preflight
```

The Python converter runs locally or in the configured batch environment. The
produced artifact is embedded-SQL COBOL; this pipeline is not a COBOL compiler or
a DB2 runtime. `main.py` is empty in this snapshot and is not the primary command.

## Directory ownership

| Directory | Responsibility |
|---|---|
| `mainframe/` | CLI orchestration, workspace I/O, Zowe transport, semantic/upload gates |
| `runners/` | CLI adapters, shared input loading, per-program routing, standalone audits |
| `converter/domain/` | Parsed metadata and conversion input/result data models |
| `converter/parsers/` | Source, mapping, DCLGEN, copybook and LRF extraction |
| `converter/repositories/` | Queryable metadata stores |
| `converter/resolvers/` | Names, hosts, keys, relationships, program kind and restart context |
| `converter/analyzers/` | Field usage, access classification and procedure-flow analysis |
| `converter/transformers/` | Logical-record expansion and IDMS/field rewriting |
| `converter/generators/` | SQL, cursors, DB2 infrastructure, initialization/timestamps |
| `converter/composers/` | Structure-aware composition, layouts, business/cursor normalization |
| `converter/pipeline/` | Actual orchestration order and selected registry-backed stages |
| `converter/postprocess/`, `converter/services/` | Final candidate processing and supporting services |
| `converter/validators/` | Input, metadata, output and safety checks |
| `review/` | Independent review engine, checks, reports and workspace metadata adapter |
| `rules/`, `patterns/`, `catalogs/` | Declarative conventions, grammars and rule/catalog selection |
| `config/`, `converter/config/` | Several path/settings layers; resolve the actual import path |
| `converter/ui/`, `tool/` | UI/controller code and UI entrypoints |
| `tests/` | Python regression evidence, not mainframe runtime proof |

## Critical ownership boundaries

`ConversionPipeline._run_pipeline` owns content order. `ConversionLayoutPipeline`
owns its finishing subphase, but additional content rewrites run after that
subphase. Final alignment must therefore occur after the entire content pipeline.
The registry defines selected stage factories; it is not the sole executable
ordering authority. Its introductory docstring contains older wording; actual
call positions take precedence.

Program kind is measured before IDMS write verbs disappear. The same measured
kind must reach the statement transformer and restart/commit consumers. A kind
resolver existing in the codebase does not prove its result reaches every consumer.

Source business paragraphs and generated infrastructure are different ownership
classes. Do not rewrite all business labels into a universal template. A helper,
flag, cursor or SQL predicate is justified by source/metadata and flow, never
solely by the example program's name.

## Data and failure contracts

`ConversionInput` carries raw source, parsed mappings, hosts, copybooks, logical
records and target identity; `ConversionResult` carries generated text,
validation messages and recognized operations. A returned string or saved `.cbl`
is not acceptance. The independent review and semantic release gates must examine
it using the correct source and metadata.

Some existing conversion paths catch failures and retain diagnostics, and source
kind reading has a retrieval fallback. These are current limitations to preserve
in documentation, not blanket fail-closed guarantees. See the current baseline.

## Source map

- [CLI](modules/mainframe/zowe_pipeline.md)
- [Batch dispatcher](modules/runners/convert_programs.md)
- [Conversion service](modules/converter/pipeline/conversion_service.md)
- [Content pipeline](modules/converter/pipeline/conversion/conversion_pipeline.md)
- [Layout subphase](modules/converter/pipeline/conversion/conversion_layout_pipeline.md)
- [Review engine](modules/review/engine/reviewer.md)
- [Semantic batch gate](modules/mainframe/zowe_semantic_release_gate.md)
