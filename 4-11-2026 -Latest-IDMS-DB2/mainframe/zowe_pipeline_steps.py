# LOCATION: zowe/zowe_pipeline_steps.py
# ACTION: CREATE NEW FILE
"""The four executable pipeline steps.

Each returns a StepResult and never raises for a business condition.
"""

from __future__ import annotations

import time
from dataclasses import dataclass

from mainframe.zowe_console import bullets, row, warnings
from mainframe.zowe_fetcher import ZoweFetcher
from mainframe.zowe_rules import (
    MAPPING_MISSING_TEMPLATE,
    STATUS_FAILED,
    STATUS_NOTHING,
    STATUS_OK,
    STATUS_SKIPPED,
    STEP_CONVERT,
    STEP_FETCH,
    STEP_REVIEW,
    STEP_UPLOAD,
)
from mainframe.zowe_steps import run_convert, run_review
from mainframe.zowe_workspace import (
    count_files,
    clean_generated,
    mapping_dir,
    output_dir,
    program_dir,
)
from mainframe.zowe_writer import upload_converted_folder
from mainframe.zowe_copybook_upload import (
    require_copybook_upload_configuration, upload_generated_copybooks,
)
from mainframe.zowe_semantic_release_gate import audit_generated_batch

COBOL_GLOB = "*.cbl"


@dataclass
class StepResult:
    step: str
    status: str
    seconds: float = 0.0
    code: int = 0

    @property
    def failed(self) -> bool:
        return self.status == STATUS_FAILED


def step_fetch(quiet: bool) -> StepResult:
    started = time.perf_counter()
    result = ZoweFetcher().fetch_all()

    if not quiet:
        diagnostics = result.get("diagnostics", [])
        programs = next(
            (line for line in diagnostics if line.startswith("Programs selected:")),
            "",
        )
        fetched = next(
            (line for line in diagnostics if line.startswith("Zowe fetched ")),
            "",
        )

        if programs:
            row("Fetch progress", programs.replace("Programs selected:", "Programs"))
        if fetched:
            row("Fetch result", fetched.replace("Zowe fetched", "Files fetched"))

    warnings(result["warnings"])

    seconds = time.perf_counter() - started
    status = STATUS_OK if result["total_files"] else STATUS_NOTHING
    return StepResult(STEP_FETCH, status, seconds)


def step_convert(quiet: bool) -> StepResult:  # noqa: ARG001
    if count_files(mapping_dir()) == 0:
        print(MAPPING_MISSING_TEMPLATE.format(folder=mapping_dir()))
        return StepResult(STEP_CONVERT, STATUS_SKIPPED)

    if count_files(program_dir()) == 0:
        return StepResult(STEP_CONVERT, STATUS_NOTHING)

    # Prevent a previous run's outputs from satisfying the review/upload
    # selectors when only some current programs convert successfully.
    # Only managed Output and Review are cleared; manual references and all
    # IDMS input assets remain immutable.
    clean_generated()
    code, seconds = run_convert()
    status = STATUS_OK if code == 0 else STATUS_FAILED
    return StepResult(STEP_CONVERT, status, seconds, code)


def step_review(quiet: bool) -> StepResult:
    if count_files(output_dir(), COBOL_GLOB) == 0:
        return StepResult(STEP_REVIEW, STATUS_NOTHING)

    code, seconds = run_review(quiet)
    semantic_passed, semantic_notes = audit_generated_batch()
    if not semantic_passed:
        warnings(["Semantic release gate blocked: see Review/semantic_release_gate.txt"])
        if not quiet:
            bullets(semantic_notes)
    # A successful review is insufficient without source-to-output business
    # operation coverage; both independent gates must succeed.
    if code == 0 and not semantic_passed:
        code = 1
    status = STATUS_OK if code == 0 else STATUS_FAILED
    return StepResult(STEP_REVIEW, status, seconds, code)


def step_upload(quiet: bool) -> StepResult:  # noqa: ARG001
    started = time.perf_counter()

    if count_files(output_dir(), COBOL_GLOB) == 0:
        return StepResult(STEP_UPLOAD, STATUS_NOTHING)

    # The standalone `upload` command must not bypass review. Fail closed
    # before opening a network connection if even one generated member is
    # rejected or the review runner fails.
    code, _review_seconds = run_review(quiet=True)
    semantic_passed, _semantic_notes = audit_generated_batch()
    if code != 0 or not semantic_passed:
        warnings(["Upload blocked: structural review or semantic parity gate failed."])
        return StepResult(STEP_UPLOAD, STATUS_FAILED,
                          time.perf_counter() - started, code or 1)

    # Preflight *before* network access; COPY must be staged in the DB2
    # compile library before the COBOL member that references it.
    try:
        require_copybook_upload_configuration(output_dir())
    except ValueError as exc:
        warnings([f"Upload blocked: {exc}"])
        return StepResult(STEP_UPLOAD, STATUS_FAILED,
                          time.perf_counter() - started, 1)
    diagnostics: list[str] = []
    upload_generated_copybooks(output_dir(), diagnostics)
    uploaded = upload_converted_folder(output_dir(), diagnostics=diagnostics)
    bullets(diagnostics)

    seconds = time.perf_counter() - started
    status = STATUS_OK if uploaded else STATUS_NOTHING
    return StepResult(STEP_UPLOAD, status, seconds)


STEP_FUNCTIONS = {
    STEP_FETCH: step_fetch,
    STEP_CONVERT: step_convert,
    STEP_REVIEW: step_review,
    STEP_UPLOAD: step_upload,
}