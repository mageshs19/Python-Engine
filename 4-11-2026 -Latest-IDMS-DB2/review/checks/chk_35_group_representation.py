"""Source-derived data representation safety, independent of paragraph names."""
from mainframe.verification.group_representation_contract import (
    audit_character_group_moves, audit_target_character_widths,
)
from review.engine.check_base import BOTH, CRITICAL, Check


class GroupRepresentationCheck(Check):
    CHECK_ID = 'CHK-35'
    TITLE = 'Character-host group representation and mapping agreement'
    SEVERITY = CRITICAL
    APPLIES_TO = BOTH
    ORDER = 350

    def relevant(self, ctx, view):
        return bool(ctx.dclgen_columns)

    def not_relevant_reason(self):
        return 'No DCLGEN supplied; representation safety has NOT been verified.'

    def review(self, ctx, view, record):
        found = audit_character_group_moves(ctx.converted_cobol,ctx.dclgen_columns)
        record.expect_none('01','Character hosts are not raw-copied into packed/binary groups',
            [f'{f.code} line {f.line}: {f.source} -> {f.target}: {f.message}' for f in found])
        conflicts = audit_target_character_widths(ctx.converted_cobol,ctx.sheet_mapping_rows,ctx.dclgen_columns)
        record.expect_none('02','Used target character widths agree between mapping and DCLGEN',
            [f'{f.code}: {f.source}: {f.message}' for f in conflicts])
