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
        self.assertGreaterEqual(len(agencies), 40)

        # Verify 19 ministries (부) exist
        ministries = [a for a in agencies if a.get("type") == "부"]
        self.assertEqual(len(ministries), 19)

        # Check key agencies
        agency_ids = {a["id"] for a in agencies}
        for expected in ("mois", "msit", "moef", "molit", "pps", "nts", "fsc", "mnd", "knpa", "nis"):
            self.assertIn(expected, agency_ids)

        # Verify custom logo agencies
        agency_map = {a["id"]: a for a in agencies}
        self.assertEqual(agency_map["mnd"]["logo"], "mnd")
        self.assertEqual(agency_map["knpa"]["logo"], "knpa")
        self.assertEqual(agency_map["nis"]["logo"], "nis")
        self.assertEqual(agency_map["nfa"]["logo"], "nfa")
        self.assertEqual(agency_map["kcg"]["logo"], "kcg")
        self.assertEqual(agency_map["spo"]["logo"], "spo")
        self.assertEqual(agency_map["president"]["logo"], "president")
        self.assertEqual(agency_map["bai"]["logo"], "bai")
        self.assertEqual(agency_map["mois"]["logo"], "gov")

    def test_badges_are_valid_accessible_svg(self):
        logos = generate.load_logos()
        sample_agencies = [
            a for a in generate.load_agencies()
            if a["id"] in ("mois", "mnd", "knpa", "nis", "nfa", "spo")
        ]

        for agency in sample_agencies:
            for style in generate.STYLES:
                svg = generate.render_badge(agency["name"], agency["en_short"], style, agency["logo"], logos)
                root = ET.fromstring(svg)
                self.assertEqual(root.attrib["role"], "img")
                self.assertIn(agency["en_short"], root.attrib["aria-label"])
                self.assertNotIn("<script", svg)

    def test_rejects_invalid_styles_or_logos(self):
        logos = generate.load_logos()
        with self.assertRaises(ValueError):
            generate.render_badge("행정안전부", "MOIS", "unknown_style", "gov", logos)

        with self.assertRaises(ValueError):
            generate.render_badge("행정안전부", "MOIS", "flat", "non_existent_logo", logos)


if __name__ == "__main__":
    unittest.main()
