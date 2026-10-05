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
        for expected in ("mois", "msit", "moef", "molit", "pps", "nts", "fsc"):
            self.assertIn(expected, agency_ids)

    def test_badges_are_valid_accessible_svg(self):
        paths = generate.logo_paths()
        sample_agencies = [a for a in generate.load_agencies() if a["id"] in ("mois", "msit", "pps")]

        for agency in sample_agencies:
            for style in generate.STYLES:
                svg = generate.render_badge("대한민국", agency["name"], style, paths)
                root = ET.fromstring(svg)
                self.assertEqual(root.attrib["role"], "img")
                self.assertIn(agency["name"], root.attrib["aria-label"])

                # Check icon path presence
                icon_paths = root.findall(
                    ".//{http://www.w3.org/2000/svg}g[@transform]/{http://www.w3.org/2000/svg}path"
                )
                self.assertEqual(len(icon_paths), 3)
                self.assertNotIn("http://", svg.replace('xmlns="http://www.w3.org/2000/svg"', ""))
                self.assertNotIn("<script", svg)

    def test_rejects_invalid_styles(self):
        paths = generate.logo_paths()
        with self.assertRaises(ValueError):
            generate.render_badge("대한민국", "행정안전부", "unknown_style", paths)


if __name__ == "__main__":
    unittest.main()
