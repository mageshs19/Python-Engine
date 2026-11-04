"""Locate bundled integration inputs without historical timestamp assumptions."""
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1] / "mainframe" / "workspace"


def mapping_export():
    paths = sorted((WORKSPACE / "Mapping Sheet").glob("*.csv"))
    assert len(paths) == 1, "Integration tests need one unambiguous mapping export"
    return paths[0]


def generated_program(program):
    paths = list((WORKSPACE / "Output").glob(program + "_*.cbl"))
    assert paths, f"Run the offline converter first: no output for {program}"
    return max(paths, key=lambda p: (p.stat().st_mtime_ns, p.name))


def expanded_program(program):
    path = WORKSPACE / "Output" / "LRF" / (program + "_lrf_to_idms.cbl")
    assert path.is_file(), f"Run offline conversion first: missing {path.name}"
    return path
