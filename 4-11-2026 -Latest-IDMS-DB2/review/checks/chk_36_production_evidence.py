"""A production review cannot silently skip missing source/schema evidence."""
import re
from review.engine.check_base import BOTH, CRITICAL, Check


class ProductionEvidenceCheck(Check):
    CHECK_ID = 'CHK-36'
    TITLE = 'Per-program production review evidence'
    SEVERITY = CRITICAL
    APPLIES_TO = BOTH
    ORDER = 360

    def relevant(self,ctx,view):
        return ctx.require_metadata

    def not_relevant_reason(self):
        return 'Structural-only review; production metadata was not requested.'

    def review(self,ctx,view,record):
        record.expect('01','Original source is paired by derived PROGRAM-ID',bool(ctx.source_cobol.strip()))
        has_sql = any(re.search(r'\bEXEC\s+SQL\b',line.logical) for line in view.code)
        record.expect('02','DB2 schema metadata is present',not has_sql or bool(ctx.dclgen_columns))
        record.expect('03','Relevant mapping metadata is present',not has_sql or bool(ctx.sheet_mapping_rows))
        has_copy = any(re.match(r'^COPY\s+',line.logical) for line in view.code)
        record.expect('04','Required COPY data metadata is present',not has_copy or bool(ctx.copybook_fields))
        record.expect_none('05','Input pairing and copybook provenance are unambiguous',ctx.metadata_diagnostics)
