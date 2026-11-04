"""Production regression checks for lifecycle standardization across all six programs."""
from __future__ import annotations

import re
from pathlib import Path

import pytest

from converter.composers.lifecycle_standardization_composer import (
    LifecycleStandardizationComposer,
)
from converter.services.final_generated_output_service import FinalGeneratedOutputService

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = {
    "VMDZ1526": "VMDZ1526_26-10-2026_052547.cbl",
    "VMDZ1567": "VMDZ1567_26-10-2026_052548.cbl",
    "VMDZ4302": "VMDZ4302_26-10-2026_052550.cbl",
    "VMDZ4310": "VMDZ4310_26-10-2026_052551.cbl",
    "VMDZ4420": "VMDZ4420_26-10-2026_052553.cbl",
    "VMDZ7200": "VMDZ7200_26-10-2026_052554.cbl",
}


def _logical(line: str) -> str:
    if len(line) >= 7 and line[:6].isdigit():
        return line[7:72].strip()
    return line.strip()


def _paragraph_labels(text: str) -> list[str]:
    labels = []
    for line in text.splitlines():
        body = _logical(line)
        if re.fullmatch(r"[A-Z0-9][A-Z0-9-]*\.", body, re.I):
            labels.append(body.upper())
    return labels


def _diagnostic_lines(text: str) -> list[str]:
    return [
        _logical(line)
        for line in text.splitlines()
        if not line.lstrip().startswith(("*", "/"))
        and re.search(r"DISPLAY\s+.*(?:ERROR|NO DATA FOUND|SQLCODE|NOT FOUND)", _logical(line), re.I)
    ]


def _sql_location_lines(text: str) -> list[str]:
    result = []
    for line in text.splitlines():
        body = _logical(line)
        if "SQL-LOCATION" not in body.upper() or body.startswith(("*", "/")):
            continue
        # Cursor paragraph renumbering updates only the location number; the
        # location assignment itself and all error routing remain intact.
        body = re.sub(r"(\bMOVE\s+)\d{3,6}(\s+TO\s+SQL-LOCATION\b)", r"\g<1><NUMBER>\g<2>", body, flags=re.I)
        result.append(body)
    return result


@pytest.mark.parametrize("program,filename", OUTPUTS.items())
def test_lifecycle_standardization_preserves_sql_error_behavior(program: str, filename: str):
    path = ROOT / "tests" / "fixtures" / "legacy_generated" / filename
    source = path.read_text(encoding="utf-8", errors="replace")
    composer = LifecycleStandardizationComposer()
    output = composer.compose(source)

    assert output != source, f"{program} was not standardized"
    labels = _paragraph_labels(output)
    for paragraph in (
        "0000-MAIN-PROCEDURE.",
        "1000-INITIALIZE-PROGRAM.",
        "2000-PROCESS-PROGRAM.",
        "3000-FINALIZE-PROGRAM.",
    ):
        assert labels.count(paragraph) == 1, (program, paragraph)

    # The structural change must not rewrite SQL/error policy or diagnostics.
    assert output.count("PERFORM SQLERROR") == source.count("PERFORM SQLERROR"), program
    assert output.upper().count("EXEC SQL") == source.upper().count("EXEC SQL"), program
    assert output.upper().count("EVALUATE SQLCODE") == source.upper().count("EVALUATE SQLCODE"), program
    assert output.upper().count("WHEN OTHER") == source.upper().count("WHEN OTHER"), program
    assert output.upper().count("WHEN 100") == source.upper().count("WHEN 100"), program
    assert _sql_location_lines(output) == _sql_location_lines(source), program
    assert _diagnostic_lines(output) == _diagnostic_lines(source), program

    first_messages = list(composer.messages)
    # The transformed output must be stable on a second pass.
    assert composer.compose(output) == output, program

    if program == "VMDZ1567":
        # 1100 is already owned by an existing business paragraph. Do not
        # renumber that paragraph or create a duplicate number; retain timestamp.
        assert "1100-UPDATE-DZBFAR." in labels
        assert "600-GET-TIMESTAMP." in labels
        assert any("1100 is already used" in message for message in first_messages)
    else:
        assert "1100-GET-TIMESTAMP." in labels, program

    if program in {"VMDZ4302", "VMDZ4420"}:
        for label in (
            "2100-OPEN-DZBEFFC1.", "2200-FETCH-DZBEFFC1.", "2300-CLOSE-DZBEFFC1.",
            "3100-OPEN-DZEVEFC1.", "3200-FETCH-DZEVEFC1.", "3300-CLOSE-DZEVEFC1.",
        ):
            assert label in labels, (program, label)
    if program == "VMDZ7200":
        assert "1200-BEGIN-PROGRAMMA." in labels
        assert "1200-BEGIN-PROGRAMMA-EXIT." in labels
        assert "PERFORM 1200-BEGIN-PROGRAMMA THRU 1200-BEGIN-PROGRAMMA-EXIT." in output
        for label in ("2100-OPEN-DZBFASC1.", "2200-FETCH-DZBFASC1.", "2300-CLOSE-DZBFASC1."):
            assert label in labels, label
    else:
        # Do not invent a BEGIN paragraph in programs that do not have one.
        assert "1200-BEGIN-PROGRAMMA." not in labels, program


def test_final_output_service_keeps_all_six_programs_fixed_format():
    service = FinalGeneratedOutputService()
    for program, filename in OUTPUTS.items():
        path = ROOT / "tests" / "fixtures" / "legacy_generated" / filename
        source = path.read_text(encoding="utf-8", errors="replace")
        source_labels = _paragraph_labels(source)
        output = service.apply(source)
        assert all(len(line) == 80 for line in output.splitlines()), program
        labels = _paragraph_labels(output)
        # Final output formatting must not invent a universal main/initialize/
        # process/finalize lifecycle. Existing business paragraph structure is
        # preserved; cursor numbering is covered by the dedicated composer tests.
        for label in (
            "0000-MAIN-PROCEDURE.", "1000-INITIALIZE-PROGRAM.",
            "2000-PROCESS-PROGRAM.", "3000-FINALIZE-PROGRAM.",
        ):
            if label not in source_labels:
                assert label not in labels, (program, label)
