"""Fail-closed semantic coverage gate for each generated program in a Zowe batch.

This is not a proof of DB2 runtime equivalence. It prevents the batch upload
path from silently ignoring missing file writes, emptied business paragraphs,
and direct UPDATEs whose original CALC not-found behavior is not yet proven.
There are no program IDs or filename timestamps in these rules.
"""
from __future__ import annotations

from pathlib import Path
import shutil

from converter.analyzers.program_flow.business_operation_parity_audit import BusinessOperationParityAuditor
from converter.parsers.cobol_parser import CobolParser
from converter.services.name_derivation_resolver import NameDerivationResolver
from mainframe.zowe_workspace import copybook_dir, dclgen_dir, mapping_dir, output_dir, program_dir, review_dir
from mainframe.zowe_writer import member_from_output_name
from mainframe.verification.record_write_contract import audit_fixed_record_writes
from mainframe.verification.record_population_contract import audit_record_population
from mainframe.verification.copybook_provenance import resolve_copybooks
from mainframe.verification.manual_direct_update_parity import manually_confirmed_direct_updates


REPORT_NAME = "semantic_release_gate.txt"


def _derive_db2_program_id(source_text: str) -> str:
    source_id = CobolParser().program_id(source_text)
    return NameDerivationResolver().derive(source_id) if source_id else ""


def audit_generated_batch() -> tuple[bool, list[str]]:
    notes: list[str] = []
    sources = sorted(program_dir().glob("*.cbl"))
    generated = sorted(output_dir().glob("*.cbl"))
    if not sources or not generated:
        return False, ["Semantic gate: no source or generated COBOL programs found."]
    mapping_files = sorted(mapping_dir().glob("*.csv"))
    if len(mapping_files) != 1:
        return False, [f"Semantic gate: expected one authoritative mapping CSV; found {len(mapping_files)}."]
    auditor = BusinessOperationParityAuditor(mapping_csv=mapping_files[0], dclgen_dir=dclgen_dir())
    from review.runner.workspace_inputs import WorkspaceReviewInputs
    from mainframe.verification.group_representation_contract import (
        audit_character_group_moves, audit_target_character_widths,
    )
    review_inputs = WorkspaceReviewInputs(program_dir().parent)
    # Build only current-run COPY artifacts, never upload a stale orphan from
    # an earlier standalone review invocation.
    generated_copybooks = output_dir() / "Generated Copybooks"
    if generated_copybooks.exists():
        shutil.rmtree(generated_copybooks)
    seen_targets: set[Path] = set()
    seen_members: set[str] = set()
    passed = True
    for source in sources:
        source_text = source.read_text(encoding="utf-8", errors="replace")
        target = _derive_db2_program_id(source_text)
        if not target or target in {"[]", "UNKNOWN"}:
            passed = False
            notes.append(f"BLOCK {source.name}: no derived target PROGRAM-ID")
            continue
        candidates = sorted(output_dir().glob(f"{target}_*.cbl"))
        # Stable member filenames are supported too; ambiguous or historical
        # duplicates must not silently win by mtime.
        candidates += [p for p in (output_dir() / f"{target}.cbl",) if p.exists()]
        if len(candidates) != 1 or candidates[0] in seen_targets:
            passed = False
            notes.append(f"BLOCK {source.name}: expected one unique output for {target}, found {len(candidates)}")
            continue
        generated_member = candidates[0]
        seen_targets.add(generated_member)
        # A PDS member has an eight-character limit. The normal writer
        # truncates longer names; without this preflight, two distinct source
        # programs can overwrite the same target during a large batch.
        member = member_from_output_name(generated_member.stem)
        if member != target or member in seen_members:
            passed = False
            notes.append(
                f"BLOCK {source.name}: target {target} maps to unsafe or duplicate "
                f"PDS member {member}; refusing upload overwrite"
            )
            continue
        seen_members.add(member)
        generated_text = generated_member.read_text(encoding="latin1")
        # Resolve COPY through explicit source-program provenance. Missing
        # renamed DB2 copybooks are materialized as separate generated assets,
        # never replaced in the generated COBOL program. Unknown or ambiguous
        # origins are blockers, not guessed successful record layouts.
        copybooks = resolve_copybooks(
            source_text, generated_text, copybook_dir(), output_dir() / "Generated Copybooks"
        )
        for error in copybooks.errors:
            passed = False
            notes.append(f"BLOCK {generated_member.name} copybook: {error}")
        notes.extend(f"COPY {generated_member.name}: {note}" for note in copybooks.notes)
        checked_text = copybooks.expanded_text
        representation = review_inputs.for_program(generated_text, source_text)
        # Standalone upload calls this gate too. Missing metadata must not turn
        # an empty audit result into apparent proof of representation safety.
        for diagnostic in representation.diagnostics:
            passed = False
            notes.append(f"BLOCK {generated_member.name} review evidence: {diagnostic}")
        for issue in (
            *audit_character_group_moves(checked_text, representation.dclgen_columns),
            *audit_target_character_widths(checked_text, representation.mapping_rows, representation.dclgen_columns),
        ):
            passed = False
            notes.append(f"BLOCK {generated_member.name} {issue.code} line {issue.line}: "
                         f"{issue.source} -> {issue.target}: {issue.message}")
        # Independently check physical record lengths for WRITE sources when
        # their COBOL storage is fully resolvable. This catches dropped
        # mapping remainder/padding bytes before any upload, without names or
        # member-specific sizes. Unsupported copybook layouts are reported;
        # never fabricate a record length from incomplete input.
        for finding in audit_fixed_record_writes(checked_text):
            if finding.level == "FAIL":
                passed = False
                notes.append(
                    f"BLOCK {generated_member.name} output layout: "
                    f"{finding.record} FROM {finding.buffer}: {finding.reason}"
                )
            else:
                passed = False
                notes.append(
                    f"BLOCK UNVERIFIED {generated_member.name} output layout: "
                    f"{finding.record} FROM {finding.buffer}: {finding.reason}"
                )
        # Independent data-loss guard: an FD length match does not prove
        # all mapped numeric fields are assigned before a physical WRITE.
        for finding in audit_record_population(checked_text):
            if finding.level == "FAIL":
                passed = False
                notes.append(
                    f"BLOCK {generated_member.name} output population: "
                    f"{finding.buffer}.{finding.field}: {finding.reason}"
                )
            else:
                passed = False
                notes.append(
                    f"BLOCK UNVERIFIED {generated_member.name} output population: "
                    f"{finding.buffer}.{finding.field}: {finding.reason}"
                )
        result = auditor.audit(source, generated_member)
        unresolved_reviews = result.reviews
        # The manually converted target is an independent, read-only reference
        # for operation-local parity. It can resolve the narrow *manual DB2*
        # design comparison without declaring IDMS implicit zero-row semantics
        # or actual DB2 execution proven. Never choose between duplicates.
        manual_folder = program_dir().parent / "Manual Output"
        manuals = [candidate for suffix in (".cbl", ".txt")
                   if (candidate := manual_folder / f"{target}{suffix}").is_file()]
        if len(manuals) == 1 and result.reviews:
            confirmed, unresolved_reviews = manually_confirmed_direct_updates(
                source_text, generated_text, manuals[0].read_text(encoding="latin1"),
                result.reviews, auditor.mapping_tables,
            )
            for record in sorted(confirmed):
                notes.append(
                    f"MANUAL-PARITY {generated_member.name} {record}: "
                    "source CALC/MODIFY matches manual and generated direct keyed "
                    "UPDATE assignments, predicates, and SQLCODE actions; "
                    "IDMS implicit not-found and DB2 runtime behavior remain unverified"
                )
        elif len(manuals) > 1:
            passed = False
            notes.append(f"BLOCK {generated_member.name}: ambiguous manual references for {target}")
        if result.issues or unresolved_reviews:
            passed = False
            notes.append(f"BLOCK {source.name} -> {generated_member.name}: {len(result.issues)} defect(s), {len(unresolved_reviews)} unresolved semantic review(s)")
            notes.extend(f"  ERROR {item.code} line {item.line}: {item.message}" for item in result.issues)
            notes.extend(f"  REVIEW {item.family} line {item.line}: {item.message}" for item in unresolved_reviews)
        else:
            notes.append(f"PASS {source.name} -> {generated_member.name}: operation and file-write coverage")
    for orphan in sorted(set(generated) - seen_targets):
        passed = False
        notes.append(f"BLOCK unpaired generated member: {orphan.name}")
    report = review_dir() / REPORT_NAME
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(notes) + "\n", encoding="utf-8")
    return passed, notes
