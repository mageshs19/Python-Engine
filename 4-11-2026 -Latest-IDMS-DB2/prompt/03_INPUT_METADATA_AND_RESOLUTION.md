# Input metadata, parsers, repositories and resolution

## Shared input path

`runners/retrieval/retrieval_input_loader.load_shared_inputs` loads the selected
mapping file, all selected DCLGENs and selected copybooks. It returns mapping rows,
DCLGEN columns, copybook fields and diagnostics. Both batch routes use this shared
metadata. Each program converter separately reads its source and logical-record
subschema definitions and derives target identity from parsed PROGRAM-ID.

Mapping selection uses the configured folder and preference rules; do not assume
all spreadsheets are merged. DCLGEN loading supports `parse_many_texts` where
available. Copybook text is combined and parsed into fields; original copybook
member bodies are also needed by provenance/pruning paths. Check each route's
actual `ConversionInput` construction: retrieval and update currently do not
populate every optional field identically.

## Model contracts

`converter/domain/models.py` defines `SheetMappingRow`, `DclgenColumn`,
`CopybookField`, `IdmsOperation`, logical-record/path models, `ConversionInput`
and `ConversionResult`. Names and attributes are shared contracts; changing a
field requires updates to parsers, repositories, resolvers, generators and tests.

| Evidence | Meaning / do not infer |
|---|---|
| Source COBOL | Verbs, paragraphs, conditions, storage declarations and initial behavior |
| Mapping row | Source-to-target field/table/key relationship and declared conversion metadata |
| DCLGEN | Target SQL columns and host spelling, PIC/USAGE, nullable/type information |
| Copybook | Group hierarchy, aliases, REDEFINES, OCCURS and fixed-record receiving layout |
| Subschema/LRF | Access-path elements, verbs, parent/set relationships and status-return meanings |
| Manual DB2 | Comparison evidence; it may contain errors or unapproved choices |

Mapping and DCLGEN disagreement is a conflict to expose, not permission to choose
whichever value makes an example pass. Metadata scope filtering separates
unrelated workbook issues from tables referenced by the current program, without
turning an in-scope conflict into an informational note.

## Repositories and resolvers

Repositories offer indexed mapping/DCLGEN/copybook/LRF lookup. The component
factory wires those repositories into table, host, key, relation, cursor,
program-kind and restart resolvers. Reuse that shared authority: independently
deriving an IDMS record name as a DB2 table can produce mismatched SQL, cursor
identities and review findings.

Composite source fields can map to several target fields. Their ordering and
widths require mapping and destination layout evidence. A single serialized DB2
column containing a compound value is a different problem: a 28-character value
cannot be assumed equivalent to a 20-byte packed group.

## Refusal and diagnostics to preserve

Missing/ambiguous table mappings, missing hosts, ambiguous copybook origins,
conflicting widths, unknown physical layout, and unsupported logical paths must
remain visible. Do not catch a parse failure and substitute an empty successful
mapping. Likewise, a diagnostic list must actually reach the caller/reviewer;
constructing it in an unused analyzer does not enforce a gate.

Parsing is fixed-format and continuation-sensitive. Token searches must not read
sequence fields or comments as executable source. Do not treat a name mentioned
in a comment or literal as an assignment or dependency.

## Source map

- [Shared input loader](modules/runners/retrieval/retrieval_input_loader.md)
- [Input selector](modules/runners/retrieval/retrieval_input_selector.md)
- [Domain models](modules/converter/domain/models.md)
- [Component wiring](modules/converter/pipeline/conversion/conversion_component_factory.md)
- [Mapping parser](modules/converter/parsers/sheet_mapping_parser.md)
- [DCLGEN parser](modules/converter/parsers/dclgen_parser.md)
- [Copybook parser](modules/converter/parsers/copybook_parser.md)
- [Mapping scope](modules/converter/validators/mapping_scope_filter.md)

## V128 manual-parity evidence: mapping and unqualified business fields

Mapping files are content-driven, not extension-driven. A file named `.csv` may be tab-, comma-, semicolon- or pipe-delimited; delimiter detection must occur before header/row mapping. A mapping parse that produces zero useful rows is not equivalent to “no mappings exist”.

Legacy COBOL often uses globally unique record fields without `OF record`. For cursor projection analysis, an unqualified source field may be attributed to an IDMS record only when Sheet Mapping proves exactly one owning record. If several records own the same name, leave it unresolved; do not widen a guessed cursor.

This discovery rule determines which DB2 values must be available. It does not by itself prove that downstream COBOL has been converted to consume those values; BR-004 covers that separate materialisation obligation.

## V129 mapping export audit consistency
The business-operation audit reads comma, tab, semicolon and pipe text exports by detected delimiter for all three indexes: record/table aliases, primary keys and field/column mappings. A filename ending in CSV does not imply comma-separated content. The audit runner discovers one authoritative workspace CSV or accepts an explicit --mapping; missing and ambiguous exports fail rather than silently auditing with empty metadata.
