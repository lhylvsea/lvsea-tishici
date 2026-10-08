import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageContractTests(unittest.TestCase):
    def test_root_entrypoint_and_frontmatter(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: lvsea-tishici", text)
        self.assertIn("/lvsea-tishici", text)
        self.assertIn("$lvsea-tishici", text)

    def test_manifest_identity_and_governance(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "lvsea-tishici")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(manifest["maturity_tier"], "governed")
        for field in ("review_due", "review_cadence", "release_gates"):
            self.assertTrue(manifest.get(field))

    def test_prompt_master_sync_preserves_safe_local_contract(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        sync = manifest["upstream_sync"]
        self.assertEqual(sync["prompt_master_reviewed_version"], "1.8.0")
        self.assertRegex(sync["prompt_master_reviewed_commit"], r"^[0-9a-f]{40}$")

        templates = (ROOT / "references/templates.md").read_text(encoding="utf-8")
        self.assertIn("Template E — Auditable Reasoning", templates)
        self.assertIn("Template M — Current Claude Task Brief", templates)
        self.assertNotIn("Template E — Chain of Thought", templates)
        self.assertNotIn("Before answering, think through this carefully", templates)

        patterns = (ROOT / "references/patterns.md").read_text(encoding="utf-8")
        self.assertIn("No audit contract for logic task", patterns)
        self.assertIn("Context rot on long sessions", patterns)
        self.assertNotIn("/rewind", patterns)

    def test_prompt_library_and_scene_routes_preserve_local_boundaries(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        sources = {item["name"]: item for item in manifest["additional_sources"]}
        self.assertRegex(sources["Luban-Labs/pp"]["reviewed_commit"], r"^[0-9a-f]{40}$")
        self.assertRegex(sources["wangmian0/prompt-opt"]["reviewed_commit"], r"^[0-9a-f]{40}$")

        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("提示词库", skill)
        self.assertIn("prompt-opt-routing.md", skill)
        self.assertIn("不扫描本机收藏目录", skill)
        self.assertIn("不执行", skill)

        library = (ROOT / "references/prompt-library-routing.md").read_text(encoding="utf-8")
        self.assertIn("1–3", library)
        self.assertIn("正文事实源", library)
        self.assertIn("不复制", library)
        self.assertIn("/pp", library)

        routing = (ROOT / "references/prompt-opt-routing.md").read_text(encoding="utf-8")
        for scene in ("排障 / 修 bug", "加功能", "重构", "调研 / 研究", "代码审查", "数据报告", "循环任务"):
            self.assertIn(scene, routing)
        self.assertIn("不超过 3 行", routing)
        self.assertIn("prompt-level", routing)

    def test_only_root_discoverable_skill_entrypoint(self):
        entrypoints = sorted(
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("SKILL.md")
            if ".git" not in path.parts and "__pycache__" not in path.parts
        )
        self.assertEqual(entrypoints, ["SKILL.md"])

    def test_references_and_evaluation_fixtures_exist(self):
        for relative in (
            "USAGE.zh-CN.md",
            "references/templates.md",
            "references/patterns.md",
            "references/model-routing.md",
            "references/output-contract.md",
            "references/prompt-library-routing.md",
            "references/prompt-opt-routing.md",
            "references/lyra-method.md",
            "evals/trigger_cases.json",
            "reports/prior-art-research.md",
            "reports/creation-handoff.md",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_lyra_method_contract(self):
        text = (ROOT / "references/lyra-method.md").read_text(encoding="utf-8")
        for phrase in (
            "解构",
            "诊断",
            "开发",
            "交付",
            "详细模式",
            "基础模式",
            "你好！我是Lyra，你的AI提示优化师。",
        ):
            self.assertIn(phrase, text)

    def test_no_private_absolute_paths_in_runtime_files(self):
        pattern = re.compile(r"(?:C:\\Users\\|/Users/|/home/|-----BEGIN .*PRIVATE KEY-----)", re.I)
        for path in (ROOT / "SKILL.md", ROOT / "README.md", ROOT / "manifest.json"):
            self.assertIsNone(pattern.search(path.read_text(encoding="utf-8")), path.name)


if __name__ == "__main__":
    unittest.main()
