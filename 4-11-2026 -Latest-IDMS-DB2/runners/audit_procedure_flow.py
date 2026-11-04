"""Print a generic PROCEDURE DIVISION control-flow audit for COBOL files."""
from __future__ import annotations

import argparse
from pathlib import Path

from converter.analyzers.program_flow.procedure_control_flow_graph import (
    ProcedureControlFlowGraphBuilder,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="COBOL source files to inspect")
    args = parser.parse_args()
    builder = ProcedureControlFlowGraphBuilder()
    failed = False
    for raw in args.paths:
        path = Path(raw)
        if not path.is_file():
            print(f"ERROR {path}: file not found")
            failed = True
            continue
        graph = builder.build(path)
        local = sum(edge.resolution == "local" for edge in graph.edges)
        external = sum(edge.resolution == "external-or-copybook" for edge in graph.edges)
        unresolved = sum(edge.resolution in {"missing", "ambiguous"} for edge in graph.edges)
        print(f"{path}: nodes={len(graph.nodes)} performs={len(graph.edges)} local={local} external_or_copybook={external} unresolved={unresolved}")
        for diagnostic in graph.diagnostics:
            print(f"  REVIEW: {diagnostic}")
        failed = failed or bool(graph.diagnostics)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
