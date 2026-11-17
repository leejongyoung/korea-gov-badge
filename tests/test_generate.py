import importlib.util
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generate", ROOT / "scripts" / "generate.py")
generate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate)


class KoreaGovBadgeTests(unittest.TestCase):
    def test_agency_data_integrity(self):
        agencies = generate.load_agencies()
        self.assertGreaterEqual(len(agencies), 72)

        # Verify 19 ministries (부) exist
        ministries = [a for a in agencies if a.get("type") == "부"]
        self.assertEqual(len(ministries), 19)

        # Verify current governments separately from preserved legacy URLs
        local_govs = [a for a in agencies if a.get("type") == "광역자치단체"]
        self.assertEqual(len(local_govs), 16)
        self.assertEqual(sum(a.get("status") == "legacy" for a in agencies if a.get("replaced_by") == "jeonnam-gwangju"), 2)

        # Check key agencies
        agency_ids = {a["id"] for a in agencies}
        for expected in ("mois", "msit", "moef", "molit", "pps", "nts", "fsc", "mnd", "knpa", "nis", "ppo", "scia", "spo-legacy", "cio", "kasa"):
            self.assertIn(expected, agency_ids)

        # Check local government IDs
        local_ids = {
            "seoul", "busan", "daegu", "incheon", "gwangju", "daejeon", "ulsan",
            "sejong", "gyeonggi", "gangwon", "chungbuk", "chungnam", "jeonbuk",
            "jeonnam", "gyeongbuk", "gyeongnam", "jeju"
        }
        for lid in local_ids:
            self.assertIn(lid, agency_ids)

        # Verify custom logo agencies
        agency_map = {a["id"]: a for a in agencies}
        self.assertEqual(agency_map["mnd"]["logo"], "mnd")
        self.assertEqual(agency_map["knpa"]["logo"], "knpa")
        self.assertEqual(agency_map["nis"]["logo"], "nis")
        self.assertEqual(agency_map["nfa"]["logo"], "nfa")
        self.assertEqual(agency_map["kcg"]["logo"], "kcg")
        self.assertEqual(agency_map["spo-legacy"]["logo"], "spo")
        self.assertEqual(agency_map["president"]["logo"], "president")
        self.assertEqual(agency_map["bai"]["logo"], "bai")
        self.assertEqual(agency_map["kasa"]["logo"], "kasa")
        self.assertEqual(agency_map["cio"]["logo"], "cio")
        self.assertEqual(agency_map["ppo"]["logo"], "gov")
        self.assertEqual(agency_map["scia"]["logo"], "gov")
        self.assertEqual(agency_map["mois"]["logo"], "gov")

        # Verify all local governments have their dedicated logo
        for lid in local_ids:
            self.assertEqual(agency_map[lid]["logo"], lid)

    def test_pending_symbol_is_text_only_in_every_style_and_theme(self):
        logos = generate.load_logos()
        for style in generate.STYLES:
            for color in generate.COLOR_THEMES:
                with self.subTest(style=style, color=color):
                    svg = generate.render_badge("전남광주통합특별시", "JEONNAM-GWANGJU", style, None, logos, color_theme=color)
                    root = ET.fromstring(svg)
                    self.assertIn("JEONNAM-GWANGJU", root.get("aria-label"))
                    texts = [n.text for n in root.iter() if n.tag.endswith("}text")]
                    self.assertIn("전남광주통합특별시", texts)
                    self.assertNotIn('transform="translate(', svg)
                    self.assertIn('x="8"', svg)

    def test_null_logo_requires_explicit_pending_status(self):
        import json
        import tempfile
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "agencies.json"
            agency = {"id": "pending", "name": "확인 대기", "en_short": "PENDING", "logo": None}
            path.write_text(json.dumps([agency]))
            with patch.object(generate, "AGENCIES", path):
                with self.assertRaisesRegex(ValueError, "explicitly pending"):
                    generate.load_agencies()
                agency["logo_status"] = "pending_official_symbol"
                path.write_text(json.dumps([agency]))
                self.assertIsNone(generate.load_agencies()[0]["logo"])

    def test_badges_are_valid_accessible_svg(self):
        logos = generate.load_logos()
        sample_agencies = [
            a for a in generate.load_agencies()
            if a["id"] in ("mois", "mnd", "knpa", "nis", "ppo", "scia", "spo-legacy", "cio", "kasa")
        ]

        for agency in sample_agencies:
            for style in generate.STYLES:
                # Default blue theme
                svg = generate.render_badge(agency["name"], agency["en_short"], style, agency["logo"], logos)
                root = ET.fromstring(svg)
                self.assertEqual(root.attrib["role"], "img")
                self.assertIn(agency["en_short"], root.attrib["aria-label"])
                self.assertNotIn("<script", svg)

                # Color themes
                for c_name in ("navy", "black", "green", "red", "gray"):
                    svg_c = generate.render_badge(agency["name"], agency["en_short"], style, agency["logo"], logos, color_theme=c_name)
                    root_c = ET.fromstring(svg_c)
                    self.assertEqual(root_c.attrib["role"], "img")

    def test_official_logo_attribution_survives_badge_generation(self):
        logos = generate.load_logos()
        for style in generate.STYLES:
            svg = generate.render_badge("진천군", "JINCHEON", style, "chungbuk-jincheon", logos)
            root = ET.fromstring(svg)
            credits = [n.text or "" for n in root.iter() if n.tag.endswith("}desc")]
            self.assertTrue(any("진천군" in c and "공공누리 제1유형" in c and "https://www.jincheon.go.kr/" in c for c in credits))

    def test_custom_color_generation(self):
        logos = generate.load_logos()
        custom = {
            "message_color": "#7952b3",
            "label_color": "#f8f9fa",
            "text_color": "#1f2328",
            "version_color": "#ffffff",
            "stroke_color": "#7952b3",
        }
        svg = generate.render_badge("행정안전부", "MOIS", "flat", "gov", logos, custom_colors=custom)
        self.assertIn('fill="#7952b3"', svg)
        self.assertIn('fill="#f8f9fa"', svg)
        root = ET.fromstring(svg)
        self.assertEqual(root.attrib["role"], "img")

    def run_cli(self, *args):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "generate.py"), "--agency", "kasa", *args],
            capture_output=True, text=True, encoding="utf-8", check=True,
        )
        return result.stdout

    def test_cli_label_and_text_colors_apply_to_every_color_mode(self):
        label, text = "#f8f9fa", "#112233"
        navy = generate.COLOR_THEMES["navy"]["message_color"]
        blue = generate.COLOR_THEMES["blue"]["message_color"]
        for style in generate.STYLES:
            for color, message in ((None, blue), ("navy", navy), ("#8250df", "#8250df")):
                with self.subTest(style=style, color=color):
                    extra = ["--color", color] if color else []
                    svg = self.run_cli("--style", style, *extra, "--label-color", label, "--text-color", text)
                    ET.fromstring(svg)
                    self.assertIn(f'fill="{label}"', svg)
                    self.assertIn(f'fill="{text}"', svg)
                    if style != "outline":
                        self.assertIn(f'fill="{message}"', svg)

    def test_cli_preset_keeps_defaults_when_label_text_omitted(self):
        logos = generate.load_logos()
        for color in (None, "navy", "#8250df"):
            with self.subTest(color=color):
                extra = ["--color", color] if color else []
                expected = generate.render_badge(
                    "우주항공청", "KASA", "flat", "kasa", logos,
                    color_theme=color if color in generate.COLOR_THEMES else "blue",
                    custom_colors={"message_color": color, "stroke_color": color} if color and color not in generate.COLOR_THEMES else None,
                )
                self.assertEqual(self.run_cli(*extra), expected)

    def test_cli_label_color_only_keeps_preset_message_color_and_default_text(self):
        svg = self.run_cli("--color", "navy", "--label-color", "#f8f9fa")
        self.assertIn(f'fill="{generate.COLOR_THEMES["navy"]["message_color"]}"', svg)
        self.assertIn('fill="#f8f9fa"', svg)
        self.assertIn('fill="#003764"', svg)

    def test_logos_are_safe_self_contained_vector_art(self):
        drawable = {"path", "rect", "circle", "ellipse", "polygon", "polyline", "line", "text", "use"}
        for path in sorted(generate.LOGOS_DIR.glob("*.svg")):
            with self.subTest(logo=path.name):
                root = ET.parse(path).getroot()
                tags = {el.tag.split("}")[-1] for el in root.iter()}
                self.assertTrue(root.get("viewBox") or (root.get("width") and root.get("height")))
                self.assertTrue(tags & drawable, "logo has no drawable element")
                self.assertFalse(tags & {"script", "foreignObject"})
                for el in root.iter():
                    for key, value in el.attrib.items():
                        if key.endswith("href"):
                            self.assertTrue(value.startswith(("#", "data:image/")), f"external reference: {value[:60]}")

    def test_size_budget_flags_oversized_logos_and_total(self):
        import tempfile
        budget = {"logo_max_bytes": 100, "grandfathered": {"old.svg": 300}, "badges_total_max_bytes": 50}
        with tempfile.TemporaryDirectory() as tmp:
            logos_dir = Path(tmp)
            (logos_dir / "ok.svg").write_text("<svg/>" + " " * 50)
            (logos_dir / "old.svg").write_text("x" * 250)
            (logos_dir / "grown.svg").write_text("x" * 101)
            (logos_dir / "old-grew.svg").write_text("x" * 101)
            original = generate.LOGOS_DIR
            generate.LOGOS_DIR = logos_dir
            try:
                problems = generate.check_size_budget({Path("a"): "a" * 40, Path("b"): "b" * 20}, budget)
                budget["grandfathered"]["old.svg"] = 200
                grew = generate.check_size_budget({}, budget)
            finally:
                generate.LOGOS_DIR = original
        text = "\n".join(problems)
        self.assertIn("grown.svg", text)
        self.assertIn("old-grew.svg", text)
        self.assertNotIn("ok.svg", text)
        self.assertNotIn("old.svg ", text)
        self.assertIn("badges total 60", text)
        self.assertTrue(any("old.svg" in line for line in grew))

    def test_repository_stays_within_size_budget(self):
        agencies = generate.load_agencies()
        expected = generate.build_expected_badges(agencies, generate.load_logos())
        self.assertEqual(generate.check_size_budget(expected), [])

    def test_rejects_invalid_styles_or_logos(self):
        logos = generate.load_logos()
        with self.assertRaises(ValueError):
            generate.render_badge("행정안전부", "MOIS", "unknown_style", "gov", logos)

        with self.assertRaises(ValueError):
            generate.render_badge("행정안전부", "MOIS", "flat", "non_existent_logo", logos)


if __name__ == "__main__":
    unittest.main()
