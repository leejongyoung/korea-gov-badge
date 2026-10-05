import importlib.util
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

        # Verify 17 metropolitan local governments exist
        local_govs = [a for a in agencies if a.get("type") == "광역자치단체"]
        self.assertEqual(len(local_govs), 17)

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

    def test_rejects_invalid_styles_or_logos(self):
        logos = generate.load_logos()
        with self.assertRaises(ValueError):
            generate.render_badge("행정안전부", "MOIS", "unknown_style", "gov", logos)

        with self.assertRaises(ValueError):
            generate.render_badge("행정안전부", "MOIS", "flat", "non_existent_logo", logos)


if __name__ == "__main__":
    unittest.main()
