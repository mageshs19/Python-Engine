"""Isolated tests for documentation maintenance, not converter validation."""
from __future__ import annotations
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("maintain_docs.py")
SPEC = importlib.util.spec_from_file_location("maintain_docs", MODULE_PATH)
docs = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(docs)


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        parent = MODULE_PATH.parents[1] / "temp"
        parent.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix="doc_test_", dir=parent)
        self.root = Path(self.tmp.name)
        (self.root / "prompt/tools").mkdir(parents=True)
        (self.root / "prompt/temp").mkdir()
        (self.root / "readme.md").write_text("# Test repository\n")
        (self.root / "pyproject.toml").write_text('[project]\nreadme = "readme.md"\n')
        for guide in docs.GUIDES.values():
            (self.root / guide).write_text("# Reviewed guide\n")
        self.put("mainframe/__init__.py", "")
        self.put("mainframe/worker.py", '"""Worker contract."""\ndef run(value: int) -> int:\n    if value < 0:\n        raise ValueError("negative")\n    return value + 1\n')
        self.put("tests/test_worker.py", "from mainframe.worker import run\ndef test_run():\n    assert run(1) == 2\n")

    def tearDown(self):
        self.tmp.cleanup()

    def put(self, name: str, text: str):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def build(self, reviewed=None):
        with contextlib.redirect_stdout(io.StringIO()):
            return docs.build(self.root, reviewed or [])

    def check(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            code = docs.check(self.root)
        return code, json.loads(output.getvalue())

    def test_complete_coverage_and_valid_navigation(self):
        self.assertEqual(self.build(), 0)
        code, result = self.check()
        self.assertEqual(code, 0)
        self.assertEqual(result["module_notes"], 3)
        note = (self.root / "prompt/modules/mainframe/worker.md").read_text()
        self.assertIn("Worker contract.", note)
        self.assertIn("tests/test_worker.py", note)
        self.assertIn("if value < 0", note)

    def test_stale_python_detected(self):
        self.build()
        self.put("mainframe/worker.py", "def run(value):\n    return value + 2\n")
        code, report = self.check()
        self.assertEqual(code, 2)
        self.assertTrue(any("Stale source note" in e for e in report["errors"]))

    def test_guide_review_required_before_refresh(self):
        self.build()
        self.put("mainframe/worker.py", "def run(value):\n    return value + 2\n")
        self.assertEqual(self.build(), 2)
        self.assertTrue((self.root / "prompt/temp/documentation_sync_needed.json").exists())
        self.assertEqual(self.build([docs.GUIDES["mainframe"]]), 0)
        self.assertEqual(self.check()[0], 0)

    def test_changed_guide_satisfies_review(self):
        self.build()
        self.put("mainframe/worker.py", "def run(value):\n    return value + 2\n")
        self.put(docs.GUIDES["mainframe"], "# Updated behavior\nReturns value plus two.\n")
        self.assertEqual(self.build(), 0)
        self.assertEqual(self.check()[0], 0)

    def test_new_source_requires_documentation(self):
        self.build()
        self.put("mainframe/extra.py", "VALUE = 1\n")
        code, report = self.check()
        self.assertEqual(code, 2)
        self.assertTrue(any("Undocumented Python file" in e for e in report["errors"]))

    def test_removed_module_note_is_pruned(self):
        self.build()
        (self.root / "tests/test_worker.py").unlink()
        self.assertEqual(self.build([docs.GUIDES["tests"]]), 0)
        self.assertFalse((self.root / "prompt/modules/tests/test_worker.md").exists())
        self.assertEqual(self.check()[0], 0)

    def test_markdown_outside_prompt_rejected(self):
        self.build()
        self.put("unapproved.md", "# Scratch\n")
        code, report = self.check()
        self.assertEqual(code, 2)
        self.assertTrue(any("Markdown outside policy" in e for e in report["errors"]))

    def test_temporary_markdown_allowed(self):
        self.build()
        self.put("prompt/temp/iteration.md", "# Temporary analysis\n")
        self.assertEqual(self.check()[0], 0)

    def test_human_review_markdown_allowed(self):
        self.build()
        self.put("Human Review/Business Rules/BR-001.md", "# Human rule\n")
        self.assertEqual(self.check()[0], 0)

    def test_broken_local_link_rejected(self):
        self.build()
        self.put("prompt/temp/iteration.md", "[missing](nowhere.md)\n")
        code, report = self.check()
        self.assertEqual(code, 2)
        self.assertTrue(any("Broken link" in e for e in report["errors"]))

    def test_manual_edit_of_generated_note_rejected(self):
        self.build()
        self.put("prompt/modules/mainframe/worker.md", "# Untracked edit\n")
        code, report = self.check()
        self.assertEqual(code, 2)
        self.assertTrue(any("Generated note/index modified" in e for e in report["errors"]))

    def test_relative_import_resolution(self):
        self.put("mainframe/runner.py", "from .worker import run\n")
        self.build()
        data = docs.load_manifest(self.root)
        self.assertIn("mainframe/worker.py", data["sources"]["mainframe/runner.py"]["imports"])

    def test_data_model_fields_documented(self):
        self.put("mainframe/model.py", "class Result:\n    value: int = 0\n")
        self.build()
        note = (self.root / "prompt/modules/mainframe/model.md").read_text()
        self.assertIn("value: int = 0", note)

    def test_malformed_python_fails_refresh(self):
        self.put("mainframe/bad.py", "def broken(\n")
        with self.assertRaises(SyntaxError):
            self.build()

    def test_tool_changes_require_maintenance_review(self):
        self.build()
        self.put("prompt/tools/checker.py", "VALUE = 1\n")
        self.assertEqual(self.build(), 2)
        self.assertEqual(self.build([docs.GUIDES["maintenance"]]), 0)
        self.assertEqual(self.check()[0], 0)

    def test_engine_python_is_never_modified(self):
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in docs.sources(self.root)}
        self.build()
        self.check()
        after = {str(p.relative_to(self.root)): p.read_bytes() for p in docs.sources(self.root)}
        self.assertEqual(before, after)

    def test_inline_code_is_not_a_markdown_link(self):
        self.build()
        self.put("prompt/temp/example.md", "`[not-a-link](unavailable.md)`\n")
        self.assertEqual(self.check()[0], 0)


if __name__ == "__main__":
    unittest.main()
