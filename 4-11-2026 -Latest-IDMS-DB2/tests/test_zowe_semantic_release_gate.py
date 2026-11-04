"""Batch-wide semantic release checks have no per-program exceptions."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from mainframe import zowe_semantic_release_gate as gate


@pytest.fixture
def workspace(tmp_path: Path, monkeypatch):
    roots = {name: tmp_path / name for name in ("Program", "Output", "Review", "Mapping Sheet", "DCLGen")}
    for item in roots.values():
        item.mkdir(parents=True)
    (roots["Mapping Sheet"] / "mapping.csv").write_text(
        "Cobol Recrd IDMS,New DB2 Record\nRECORD,DZRECORD\n", encoding="utf-8"
    )
    for symbol, location in (
        ("program_dir", "Program"), ("output_dir", "Output"),
        ("review_dir", "Review"), ("mapping_dir", "Mapping Sheet"),
        ("dclgen_dir", "DCLGen"),
    ):
        monkeypatch.setattr(gate, symbol, lambda p=roots[location]: p)
    return roots


def add_program(roots, source_id, target_id=None):
    target_id = target_id or gate.NameDerivationResolver().derive(source_id)
    (roots["Program"] / f"{source_id}.cbl").write_text(
        f"000100 IDENTIFICATION DIVISION.\n000200 PROGRAM-ID. {source_id}.\n"
        "000300 PROCEDURE DIVISION.\n000400 1000-MAIN.\n"
        "000500     DISPLAY 'TEST'.\n", encoding="utf-8"
    )
    output = roots["Output"] / f"{target_id}_batch.cbl"
    output.write_text(f"000100 PROGRAM-ID. {target_id}.\n", encoding="utf-8")
    return output


def test_generic_batch_matches_multiple_inputs_and_records_success(workspace):
    add_program(workspace, "VM4BD420")
    add_program(workspace, "VM7BD200")
    passed, notes = gate.audit_generated_batch()
    assert passed
    assert len(notes) == 2 and all(item.startswith("PASS") for item in notes)
    assert "PASS" in (workspace["Review"] / gate.REPORT_NAME).read_text()


def test_unresolved_semantic_review_blocks_entire_batch(workspace, monkeypatch):
    add_program(workspace, "VM4BD420")
    add_program(workspace, "VM7BD200")
    real_auditor = gate.BusinessOperationParityAuditor

    class FakeAuditor(real_auditor):
        def audit(self, source, target):
            if Path(source).stem == "VM7BD200":
                return SimpleNamespace(issues=(), reviews=(SimpleNamespace(
                    family="UPDATE", line=30, message="unproven zero row handling"
                ),))
            return super().audit(source, target)

    monkeypatch.setattr(gate, "BusinessOperationParityAuditor", FakeAuditor)
    passed, notes = gate.audit_generated_batch()
    assert not passed
    assert any("BLOCK VM7BD200" in item for item in notes)
    assert any("unproven zero row" in item for item in notes)


def test_unpaired_output_blocks_batch(workspace):
    add_program(workspace, "VM4BD420")
    (workspace["Output"] / "ORPHAN_batch.cbl").write_text("test", encoding="utf-8")
    passed, notes = gate.audit_generated_batch()
    assert not passed
    assert any("unpaired generated member" in item for item in notes)


def test_duplicate_target_outputs_block_batch(workspace):
    add_program(workspace, "VM4BD420")
    (workspace["Output"] / "VMDZ4420_other.cbl").write_text("test", encoding="utf-8")
    passed, notes = gate.audit_generated_batch()
    assert not passed
    assert any("expected one unique output" in item for item in notes)


def test_missing_mapping_source_or_generated_blocks_batch(workspace):
    passed, notes = gate.audit_generated_batch()
    assert not passed and "no source" in notes[0]
    add_program(workspace, "VM4BD420")
    (workspace["Mapping Sheet"] / "mapping.csv").unlink()
    passed, notes = gate.audit_generated_batch()
    assert not passed and "mapping CSV" in notes[0]


def test_overlong_program_id_is_never_silently_truncated_on_upload(workspace):
    add_program(workspace, "VM123BD4567")
    passed, notes = gate.audit_generated_batch()
    assert not passed
    assert any("unsafe or duplicate PDS member" in item for item in notes)


def test_unverified_copybook_output_blocks_release(workspace, monkeypatch):
    from mainframe.verification.record_write_contract import RecordWriteFinding
    add_program(workspace, "VM7BD200")
    monkeypatch.setattr(gate, "audit_fixed_record_writes", lambda _: (
        RecordWriteFinding("UNVERIFIED", "OUT", "OUT-GROUP", "missing layout"),))
    passed, notes = gate.audit_generated_batch()
    assert not passed
    assert any("BLOCK UNVERIFIED" in note and "missing layout" in note for note in notes)


def test_unpopulated_numeric_fields_block_release(workspace, monkeypatch):
    from mainframe.verification.record_population_contract import PopulationFinding
    add_program(workspace, "VM7BD200")
    monkeypatch.setattr(gate, "audit_record_population", lambda _: (
        PopulationFinding("FAIL", "OUT-GROUP", "AMOUNT", "no MOVE"),))
    passed, notes = gate.audit_generated_batch()
    assert not passed
    assert any("output population" in note and "AMOUNT" in note for note in notes)
