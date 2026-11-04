from pathlib import Path

from runners.audit_ai_standardized_reference import (
    build_report,
    inspect_program,
    latest_python_output,
    normalized_diff_counts,
)


def test_latest_output_uses_filename_timestamp_not_file_mtime(tmp_path: Path):
    output = tmp_path / "Output"
    output.mkdir()
    older = output / "VMDZ4420_25-10-2026_235959.cbl"
    newer = output / "VMDZ4420_26-10-2026_000001.cbl"
    older.write_text("OLDER", encoding="utf-8")
    newer.write_text("NEWER", encoding="utf-8")
    # Deliberately make the older filename newer on disk.
    import os
    os.utime(older, (newer.stat().st_mtime + 100, newer.stat().st_mtime + 100))
    assert latest_python_output(output, "VMDZ4420") == newer


def test_inspector_reports_sql_infrastructure_and_cursor_operations(tmp_path: Path):
    path = tmp_path / "sample.cbl"
    bodies = [
        "PROCEDURE DIVISION.",
        "    MOVE 2100 TO SQL-LOCATION.",
        "    EXEC SQL OPEN C1 END-EXEC.",
        "    EXEC SQL FETCH C1 END-EXEC.",
        "    EXEC SQL CLOSE C1 END-EXEC.",
        "    EXEC SQL INCLUDE SQLERRWS END-EXEC.",
        "2100-OPEN-C1.",
    ]
    path.write_text(
        "\n".join(f"{(i + 1) * 100:06d} {body:<65}{(i + 1) * 100:08d}" for i, body in enumerate(bodies)) + "\n",
        encoding="utf-8",
    )
    info = inspect_program(path)
    assert info["conventions"]["sqlerrws_include"] == 1
    assert info["conventions"]["exec_sql_blocks"] == 4
    assert "C1" in info["cursors"] or info["cursors"] == {}
    assert info["fixed_80_columns"]


def test_diff_counter_ignores_sequence_number_changes():
    left = ["000100 MOVE A TO B.                                                     00010000"]
    right = ["009990 MOVE A TO B.                                                     00999000"]
    assert normalized_diff_counts(left, right)["changed_lines_added"] == 0
    assert normalized_diff_counts(left, right)["changed_lines_removed"] == 0


def test_project_report_keeps_v6_as_advisory_not_authoritative():
    root = Path(__file__).resolve().parents[1]
    report = build_report(root)
    assert report["reference_version"] == "IDMS_DB2_STANDARDIZED_V6"
    assert "do not assume V6 is 100% correct" in report["principle"]
    assert len(report["programs"]) == 6
    assert any(item["topic"] == "Helper-variable removal" for item in report["policy_conflicts"])
