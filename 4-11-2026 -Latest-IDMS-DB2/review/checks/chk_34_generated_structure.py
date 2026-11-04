"""Independent structural release gate over the final generated COBOL."""
from __future__ import annotations

from converter.validators.generated_cobol_release_validator import validate_generated_cobol
from review.engine.check_base import BOTH, CRITICAL, Check


class GeneratedStructureCheck(Check):
    CHECK_ID = "CHK-34"
    TITLE = "Generated COBOL release structure and semantic safety"
    SEVERITY = CRITICAL
    APPLIES_TO = BOTH
    ORDER = 340

    def review(self, ctx, view, record):
        issues = validate_generated_cobol(ctx.converted_cobol)
        record.expect_none(
            "01", "Generated COBOL has no independent structural release blockers",
            [f"{issue.code} at line {issue.line}: {issue.message}" for issue in issues],
        )
