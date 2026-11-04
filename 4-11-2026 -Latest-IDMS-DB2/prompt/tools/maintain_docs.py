#!/usr/bin/env python3
"""Build/check source-linked Markdown without importing or running the engine.

Run from the repository root:
    python prompt/tools/maintain_docs.py refresh
    python prompt/tools/maintain_docs.py check

On later source changes, update the owning guide first. If that guide remains
accurate, explicitly record its review with refresh --reviewed-guide PATH.
Generated module notes are AST navigation aids, not semantic correctness proofs.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import sys
import tokenize
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = "prompt/source_manifest.json"
SKIP_DIRS = {".git", ".venv", "venv", "env", "__pycache__", ".pytest_cache", ".mypy_cache", "site-packages", "node_modules"}
GUIDES = {
    "mainframe": "prompt/02_MAINFRAME_PIPELINE.md",
    "metadata": "prompt/03_INPUT_METADATA_AND_RESOLUTION.md",
    "conversion": "prompt/04_LR_IDMS_DB2_CONVERSION.md",
    "cursor": "prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md",
    "storage": "prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md",
    "update": "prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md",
    "format": "prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md",
    "review": "prompt/09_REVIEW_AND_RELEASE_GATES.md",
    "tests": "prompt/10_TESTING_AND_VALIDATION.md",
    "config": "prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md",
    "maintenance": "prompt/12_CHANGE_WORKFLOW.md",
    "rules": "prompt/14_RULES_PATTERNS_AND_CATALOGS.md",
    "ui": "prompt/15_UI_AND_LOGGING.md",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources(root: Path) -> list[Path]:
    """Cover every engine/test Python file; documentation tooling is separate."""
    return sorted(p for p in root.rglob("*.py")
                  if not set(p.relative_to(root).parts) & SKIP_DIRS
                  and p.relative_to(root).parts[0] != "prompt")


def guide_for(name: str) -> str:
    low = name.lower()
    if low.startswith("tests/"):
        return GUIDES["tests"]
    if low.startswith(("review/", "mainframe/verification/")) or "semantic_release_gate" in low:
        return GUIDES["review"]
    if low.startswith("mainframe/"):
        return GUIDES["mainframe"]
    if low.startswith(("rules/", "patterns/", "catalogs/", "converter/rules/")):
        return GUIDES["rules"]
    if low.startswith(("config/", "converter/config/")) or low == "main.py":
        return GUIDES["config"]
    if low.startswith(("tool/", "converter/ui/", "converter/logging_utils/")) or low == "converter/app.py" or "logger" in low or "logging" in low:
        return GUIDES["ui"]
    if "restart" in low or low.startswith(("runners/update/", "converter/composers/update", "converter/postprocess/update")) or "update_program" in low or "commit" in low:
        return GUIDES["update"]
    if low.startswith(("converter/parsers/", "converter/repositories/", "converter/resolvers/", "converter/domain/", "converter/analyzers/", "converter/infrastructure/")) or "input_loader" in low or "input_selector" in low:
        return GUIDES["metadata"]
    if any(x in low for x in ("date_", "copybook", "materialisation", "group_move", "schema_numeric", "storage_include", "manual_storage", "field_reference")):
        return GUIDES["storage"]
    if any(x in low for x in ("cursor", "business_control", "output_write", "key_binding", "bounded_lrf", "generators/sql", "sql_generator", "sql_error")):
        return GUIDES["cursor"]
    if low.startswith("converter/postprocess/") or any(x in low for x in ("format", "indent", "sequence", "cleanup", "numbering", "structural_safety", "layout", "style", "counter_declaration")):
        return GUIDES["format"]
    if low.startswith("converter/validators/") or low.startswith("runners/audit_"):
        return GUIDES["review"]
    return GUIDES["conversion"]


def short(text: str, limit: int = 380) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit - 3] + "..."


def safe(text: str) -> str:
    return str(text).replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")


def inline(text: str) -> str:
    return str(text).replace("`", "'").replace("\n", " ")


def link(from_doc: str, target: str, label: str | None = None) -> str:
    rel = Path(os.path.relpath(target, Path(from_doc).parent)).as_posix()
    return f"[{label or target}]({quote(rel, safe='/._-')})"


def doc_for(source: str) -> str:
    return "prompt/modules/" + str(Path(source).with_suffix(".md")).replace("\\", "/")


def module_name(source: str) -> str:
    parts = list(Path(source).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def local_imports(tree: ast.AST, name: str, modules: dict[str, str]) -> list[str]:
    found: set[str] = set()
    package = module_name(name).split(".")
    if Path(name).name != "__init__.py":
        package = package[:-1]
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:
                prefix = package[:len(package) - node.level + 1]
                base = ".".join(prefix + ([base] if base else []))
            names = [base] + [base + "." + a.name for a in node.names if a.name != "*"]
        for candidate in names:
            if candidate in modules and modules[candidate] != name:
                found.add(modules[candidate])
    return sorted(found)


def symbol_nodes(tree: ast.AST) -> list[tuple[str, ast.AST]]:
    result: list[tuple[str, ast.AST]] = []
    def collect(body: list, prefix: str = "") -> None:
        for node in body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                label = prefix + node.name
                result.append((label, node))
                collect(node.body, label + ".")
            elif isinstance(node, (ast.If, ast.Try)):
                collect(node.body, prefix)
                collect(node.orelse, prefix)
                if isinstance(node, ast.Try):
                    collect(node.finalbody, prefix)
                    for handler in node.handlers:
                        collect(handler.body, prefix)
    collect(tree.body)
    return result


class Behavior(ast.NodeVisitor):
    """Lexical facts inside one callable; not runtime dispatch or path analysis."""
    def __init__(self) -> None:
        self.calls: list[tuple[int, str]] = []
        self.branches: list[tuple[int, str]] = []
        self.raises: list[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        return

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        return

    def visit_Call(self, node: ast.Call) -> None:
        self.calls.append((node.lineno, short(ast.unparse(node.func), 110)))
        self.generic_visit(node)

    def visit_If(self, node: ast.If) -> None:
        self.branches.append((node.lineno, "if " + short(ast.unparse(node.test), 180)))
        self.generic_visit(node)

    def visit_For(self, node: ast.For) -> None:
        self.branches.append((node.lineno, "for " + short(ast.unparse(node.target) + " in " + ast.unparse(node.iter), 180)))
        self.generic_visit(node)

    visit_AsyncFor = visit_For

    def visit_While(self, node: ast.While) -> None:
        self.branches.append((node.lineno, "while " + short(ast.unparse(node.test), 180)))
        self.generic_visit(node)

    def visit_Raise(self, node: ast.Raise) -> None:
        self.raises.append(short(ast.unparse(node.exc) if node.exc else "re-raise", 160))
        self.generic_visit(node)


def unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def inspect_source(root: Path, path: Path, modules: dict[str, str]) -> dict:
    name = path.relative_to(root).as_posix()
    with tokenize.open(path) as stream:
        text = stream.read()
    tree = ast.parse(text, filename=name)
    top = ast.get_docstring(tree) or ""
    description = short(top.split("\n\n")[0], 620) if top else ""
    symbols = []
    for label, node in symbol_nodes(tree):
        body = Behavior()
        if isinstance(node, ast.ClassDef):
            signature = "class " + node.name + "(" + ", ".join(ast.unparse(b) for b in node.bases) + ")"
            kind = "class"
        else:
            signature = node.name + "(" + ast.unparse(node.args) + ")"
            if node.returns:
                signature += " -> " + ast.unparse(node.returns)
            kind = "async function" if isinstance(node, ast.AsyncFunctionDef) else "function/method"
            for stmt in node.body:
                body.visit(stmt)
        symbols.append({"name": label, "kind": kind, "line": node.lineno,
                        "end_line": node.end_lineno, "signature": short(signature, 350),
                        "description": short((ast.get_docstring(node) or "").split("\n\n")[0], 380),
                        "fields": [short(ast.unparse(child), 300) for child in node.body
                                   if isinstance(node, ast.ClassDef) and isinstance(child, (ast.AnnAssign, ast.Assign))],
                        "calls": unique([x[1] for x in sorted(body.calls)]),
                        "branches": sorted(body.branches), "raises": unique(body.raises)})
    constants = []
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name):
                    constants.append((target.id, node.lineno))
    external_imports = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            external_imports.append(ast.unparse(node))
    return {"source": name, "sha256": digest(path), "lines": len(text.splitlines()),
            "description": description, "symbols": symbols, "constants": constants,
            "imports": local_imports(tree, name, modules), "import_statements": unique(external_imports),
            "guide": guide_for(name), "doc": doc_for(name)}


def render_module(info: dict, reverse: dict[str, list[str]]) -> str:
    name, doc = info["source"], info["doc"]
    lines = [f"# `{name}`", "", f"Source: {link(doc, name)} | {info['lines']} lines.",
             f"Owning logic guide: {link(doc, info['guide'])}.",
             f"Source SHA-256: `{info['sha256']}`.", "",
             "Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.", "", "## Responsibility", ""]
    if info["description"]:
        lines += ["Source-declared description (not an independently verified runtime claim):", "", "> " + safe(info["description"]), ""]
    elif not info["symbols"] and not info["constants"] and not info["import_statements"]:
        lines += ["Empty module/package marker; no executable definitions were found.", ""]
    elif not info["symbols"]:
        lines += ["Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.", ""]
    else:
        lines += ["No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.", ""]
    if info["constants"]:
        lines += ["## Module-level bindings", "", ", ".join(f"`{n}` (L{line})" for n, line in info["constants"]), ""]
    if info["import_statements"]:
        lines += ["## Import declarations", "", "```python", *info["import_statements"], "```", ""]
    if info["imports"]:
        lines += ["## Local dependency notes", ""]
        lines += ["- " + link(doc, doc_for(n), n) for n in info["imports"]]
        lines += [""]
    callers = reverse.get(name, [])
    if callers:
        tests = [x for x in callers if x.startswith("tests/")]
        others = [x for x in callers if not x.startswith("tests/")]
        lines += [f"## Importers ({len(callers)})", "", "Static imports only; dependency injection, string imports and runtime dispatch can add edges.", ""]
        shown = (others[:12] + tests[:12])
        lines += ["- " + link(doc, doc_for(n), n) for n in shown]
        if len(shown) < len(callers):
            lines += [f"- {len(callers)-len(shown)} further importers are recorded in {link(doc, MANIFEST, 'the source manifest')}."]
        lines += [""]
    if info["symbols"]:
        lines += ["## Symbol contracts and control points", ""]
        for symbol in info["symbols"]:
            lines += [f"### `{symbol['name']}` - L{symbol['line']}-L{symbol['end_line']}", "",
                      "```python", symbol["signature"], "```", ""]
            if symbol["description"]:
                lines += [safe(symbol["description"]), ""]
            if symbol["fields"]:
                lines += ["Declared class/data-model fields:", "", "```python", *symbol["fields"], "```", ""]
            if symbol["calls"]:
                shown = symbol["calls"][:16]
                lines += ["Observed calls (lexical order): " + ", ".join(f"`{inline(c)}`" for c in shown) + "."]
                if len(symbol["calls"]) > len(shown):
                    lines += [f"Another {len(symbol['calls'])-len(shown)} call expressions are in this source span; the list is intentionally bounded."]
                lines += [""]
            if symbol["branches"]:
                shown = symbol["branches"][:8]
                lines += ["Control points:", ""]
                lines += [f"- L{line}: `{inline(expr)}`" for line, expr in shown]
                if len(symbol["branches"]) > len(shown):
                    lines += [f"- Another {len(symbol['branches'])-len(shown)} conditions/loops exist in this source span."]
                lines += [""]
            if symbol["raises"]:
                lines += ["Explicit raises: " + "; ".join(f"`{inline(x)}`" for x in symbol["raises"][:8]) + ".", ""]
    lines += ["## Change responsibility", "", f"After modifying this Python file, review {link(doc, info['guide'])}, update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.", ""]
    return "\n".join(lines)


def write_if_changed(root: Path, name: str, text: str) -> None:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    if not path.is_file() or path.read_bytes() != data:
        path.write_bytes(data)


def load_manifest(root: Path) -> dict:
    path = root / MANIFEST
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def tooling(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): digest(p)
            for p in sorted((root / "prompt/tools").glob("*.py"))}


def build(root: Path, reviewed: list[str]) -> int:
    paths = sources(root)
    modules = {module_name(p.relative_to(root).as_posix()): p.relative_to(root).as_posix() for p in paths}
    infos = [inspect_source(root, p, modules) for p in paths]
    old = load_manifest(root)
    old_sources = old.get("sources", {})
    current = {i["source"]: i for i in infos}
    changed = sorted(n for n in set(old_sources) | set(current)
                     if n not in old_sources or n not in current or old_sources[n]["sha256"] != current[n]["sha256"])
    required = {guide_for(n) for n in changed}
    if old and old.get("tooling") != tooling(root):
        required.add(GUIDES["maintenance"])
    missing_guides = sorted(g for g in set(GUIDES.values()) if not (root / g).is_file())
    if missing_guides:
        raise ValueError("Missing guides: " + ", ".join(missing_guides))
    reviewed_set = {Path(p).as_posix() for p in reviewed}
    invalid_review = reviewed_set - set(GUIDES.values())
    if invalid_review:
        raise ValueError("Unknown reviewed guide: " + ", ".join(sorted(invalid_review)))
    pending = []
    if old:
        pending = sorted(g for g in required if g not in reviewed_set and old.get("guides", {}).get(g) == digest(root / g))
    if pending:
        report = {"changed_sources": changed, "guides_requiring_review": pending,
                  "action": "Update each guide, or explicitly acknowledge that its behavior explanation is still accurate with --reviewed-guide PATH."}
        write_if_changed(root, "prompt/temp/documentation_sync_needed.json", json.dumps(report, indent=2) + "\n")
        print(json.dumps(report, indent=2))
        return 2
    reverse: dict[str, list[str]] = defaultdict(list)
    for info in infos:
        for imported in info["imports"]:
            reverse[imported].append(info["source"])
    generated = {}
    for info in infos:
        write_if_changed(root, info["doc"], render_module(info, reverse))
        generated[info["doc"]] = digest(root / info["doc"])
    groups: dict[str, list[dict]] = defaultdict(list)
    for info in infos:
        groups[str(Path(info["source"]).parent)].append(info)
    index_root = "prompt/MODULE_INDEX.md"
    index = ["# Python module index", "", f"Coverage: **{len(infos)} Python files** (including tests and empty package markers). Documentation tooling in `prompt/tools/` is maintained separately in the change workflow guide.", "", "Start with the architecture/task router. Open the relevant package below; do not load every module note at once.", "", "| Source directory | Files | Package index |", "|---|---:|---|"]
    for group, items in sorted(groups.items()):
        idx = "prompt/index/" + (group if group != "." else "_root") + ".md"
        index.append(f"| `{group}` | {len(items)} | {link(index_root, idx, 'Open')} |")
        contents = [f"# `{group}` module map", "", f"{len(items)} Python files. {link(idx, index_root, 'All packages')}.", "", "| Python source | Logic note | Owning guide |", "|---|---|---|"]
        for item in items:
            contents.append(f"| `{item['source']}` | {link(idx, item['doc'], 'Module')} | {link(idx, item['guide'], Path(item['guide']).stem)} |")
        write_if_changed(root, idx, "\n".join(contents) + "\n")
        generated[idx] = digest(root / idx)
    write_if_changed(root, index_root, "\n".join(index) + "\n")
    generated[index_root] = digest(root / index_root)
    for name in set(old.get("generated_docs", {})) - set(generated):
        if name.startswith(("prompt/modules/", "prompt/index/")) and (root / name).is_file():
            (root / name).unlink()
    data = {
        "schema_version": 1,
        "basis": "Static AST inspection; no engine imports or runtime proof.",
        "python_count": len(infos),
        "source_scope": "All repository Python except prompt/ documentation tooling and cache/environment directories.",
        "sources": {i["source"]: {"sha256": i["sha256"], "lines": i["lines"], "doc": i["doc"],
                    "guide": i["guide"], "imports": i["imports"], "imported_by": reverse.get(i["source"], [])} for i in infos},
        "guides": {g: digest(root / g) for g in sorted(set(GUIDES.values()))},
        "generated_docs": generated,
        "tooling": tooling(root),
        "last_source_changes": changed if old else [],
        "explicitly_reviewed_guides": sorted(reviewed_set),
    }
    write_if_changed(root, MANIFEST, json.dumps(data, indent=2, sort_keys=True) + "\n")
    pending_path = root / "prompt/temp/documentation_sync_needed.json"
    if pending_path.exists():
        pending_path.unlink()
    print(json.dumps({"result": "refreshed", "python_files": len(infos), "module_notes": len(infos),
                      "package_indexes": len(groups), "changed_sources": len(changed) if old else 0}, indent=2))
    return 0


def markdown_links(root: Path, path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "", text)
    errors = []
    for target in re.findall(r"(?<!!)\[[^\]\n]*(?<!\\)\]\(([^\s)]+)\)", text):
        parsed = urlsplit(target)
        if parsed.scheme or not parsed.path:
            continue
        resolved = (path.parent / unquote(parsed.path)).resolve()
        if not resolved.is_relative_to(root.resolve()):
            errors.append(f"Link leaves repository: {path.relative_to(root)} -> {target}")
        elif not resolved.exists():
            errors.append(f"Broken link: {path.relative_to(root)} -> {target}")
    return errors


def check(root: Path) -> int:
    manifest = load_manifest(root)
    if not manifest:
        raise ValueError("Missing prompt/source_manifest.json; run refresh first.")
    errors = []
    current = {p.relative_to(root).as_posix(): digest(p) for p in sources(root)}
    saved = manifest.get("sources", {})
    for name in sorted(set(current) | set(saved)):
        if name not in saved:
            errors.append(f"Undocumented Python file: {name}")
        elif name not in current:
            errors.append(f"Removed Python file still documented: {name}")
        elif current[name] != saved[name]["sha256"]:
            errors.append(f"Stale source note: {name} -> {saved[name]['doc']}")
    for name, expected in manifest.get("generated_docs", {}).items():
        if not (root / name).is_file():
            errors.append(f"Missing generated note/index: {name}")
        elif digest(root / name) != expected:
            errors.append(f"Generated note/index modified; refresh it: {name}")
    for name in set(GUIDES.values()):
        if not (root / name).is_file():
            errors.append(f"Missing owning guide: {name}")
    if tooling(root) != manifest.get("tooling"):
        errors.append("Documentation tooling changed; review the maintenance guide and refresh.")
    markdown = sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() == ".md")
    for p in markdown:
        name = p.relative_to(root).as_posix()
        if (
            name != "readme.md"
            and not name.startswith("prompt/")
            and not name.startswith("Human Review/")
        ):
            errors.append(f"Markdown outside policy location: {name}")
        errors.extend(markdown_links(root, p))
    if not (root / "readme.md").is_file():
        errors.append("Missing root readme.md")
    project = root / "pyproject.toml"
    if project.is_file() and 'readme = "readme.md"' not in project.read_text(encoding="utf-8-sig"):
        errors.append("pyproject.toml does not point to root readme.md")
    if (root / "prompt/temp/documentation_sync_needed.json").is_file():
        errors.append("Unresolved documentation guide review in prompt/temp/documentation_sync_needed.json")
    summary = {"result": "PASS" if not errors else "FAIL", "python_files": len(current),
               "module_notes": len(saved), "markdown_files": len(markdown), "errors": errors}
    print(json.dumps(summary, indent=2))
    return 0 if not errors else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("refresh", "check"))
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root (also useful for isolated tests).")
    parser.add_argument("--reviewed-guide", action="append", default=[], help="Acknowledge that a named owning guide was reviewed and remains accurate.")
    args = parser.parse_args()
    try:
        return build(args.root.resolve(), args.reviewed_guide) if args.command == "refresh" else check(args.root.resolve())
    except (OSError, ValueError, SyntaxError, UnicodeError) as exc:
        print(f"Documentation maintenance failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
