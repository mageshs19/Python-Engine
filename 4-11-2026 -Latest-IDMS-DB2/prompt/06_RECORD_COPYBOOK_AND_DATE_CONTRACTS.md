# Storage, copybooks, dates and helper-variable decisions

## Physical layout is part of business correctness

A same-named field or group does not establish byte compatibility. PIC, USAGE,
sign, REDEFINES, OCCURS, hierarchy and qualification determine receiving storage.
A raw character-to-packed group MOVE is not a field-by-field numeric conversion.
Do not change source storage or infer a serialization encoding from total length
alone. Conflicting mapping/DCLGEN declarations must remain blocked.

Record materialization replaces a source raw record field only when mapping and
copybook evidence establish the rendered layout and target capacity. Include
mapping-defined FILLER independently of the calculated trailing remainder. Emit a
positive remainder only to preserve the original size; refuse unknown or
overflowing sizes. In the archived 7200 case, a 432-byte mapped record inside a
478-byte field requires 46 further bytes; these are example measurements, not
engine constants. The complete output buffer is 530 bytes in that fixture.

## Copybook provenance and usage

Derived DB2 copybooks require a proven source COPY member and verified layout.
Do not manufacture a member by filename resemblance or silently change an
external record interface. The mainframe upload step has a separate derived
copybook preflight and staging path.

`UnusedCopybookPruner` uses source copybook bodies and reference evidence. It must
not delete required fields because the manual commented out a member, nor retain
an invented member solely because a naming rewrite produced it. Source COPY,
REPLACING, aliases and nested definitions require conservatism.

`record_write_contract`, `cobol_storage_layout` and `record_population_contract`
are independent static checks. Correct record length is insufficient: numeric
fields must be validly populated. `MOVE SPACES TO group` does not prove packed or
binary numeric initialization. Presence of a MOVE somewhere is not path-complete
assignment proof; inspect the relevant control flow.

## Dates and serialized groups

`SchemaDateTransferComposer` uses DCLGEN DATE metadata and receiving layout to
identify ten-character date-to-eight-position conversions. Existing composers
handle normal dates and configured minimum/maximum sentinels. Do not assume the
host date string format is identical across DB2 installations.

`LrfGroupMoveDecomposer` handles source-proven mapped components and destination
children. A one-column serialized compound identifier with a changed encoding
is not automatically solved by that decomposition. V123 detects the unresolved
CHAR(28)/packed-20/mapping-CHAR(20) conflict in 4310; it does not convert it safely.
See [current baseline](13_CURRENT_BASELINE_AND_OPEN_ISSUES.md).

## Minimal helpers, not zero helpers at any cost

Reuse a valid existing destination child field or group when it preserves type,
width, sign, truncation, leading zeroes, padding and lifetime. A direct move may
remove a needless staging area. Keep or generate a helper only when conversion,
state isolation or a saved value actually requires it. Never remove a helper by
program name, or add one merely to imitate the manual text.

The declaration, assignments, qualification, use sites and reset lifetime must
be generated together. Separate row fields from cursor EOC/early-stop state and
from program-level counters. A metadata-derived helper is still generic.

## Source map

- [Materialization owner](modules/converter/composers/record_materialisation_composer.md)
- [Layout geometry](modules/converter/composers/record_materialisation/record_layout_geometry.md)
- [Compound group transfers](modules/converter/composers/lrf_group_move_decomposer.md)
- [Schema date transfers](modules/converter/composers/schema_date_transfer_composer.md)
- [Unused copybook analysis](modules/converter/composers/unused_copybook_pruner.md)
- [Copybook provenance](modules/mainframe/verification/copybook_provenance.md)
- [Storage checker](modules/mainframe/verification/cobol_storage_layout.md)
- [Representation checker](modules/mainframe/verification/group_representation_contract.md)
- [Population checker](modules/mainframe/verification/record_population_contract.md)

## V129 regression fixes
Generated split-record level-05 declarations start at Area B (four source-area spaces); storage widths, hierarchy and representations are unchanged. Missing bare scalar/date references use the constraints described in the SQL/business-flow guide. The NR_IDGOOD CHAR(20)/CHAR(28)/packed-group conflict remains blocked; manual display-digit groups are evidence to reconcile, not an automatic serialization contract.

Date comparisons are rechecked after field-reference resolution, because a valid DCLGEN group qualifier can be on a COBOL continuation line. The date composer remains idempotent.
