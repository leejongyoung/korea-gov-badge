#!/usr/bin/env python3
"""Generate self-contained Republic of Korea government agency SVG badges."""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENCIES = ROOT / "agencies.json"
LOGO = ROOT / "assets" / "korea-gov-mark.svg"
OUTPUT = ROOT / "badges"
STYLES = ("flat", "flat-square", "plastic", "for-the-badge", "outline")
SLUG_PATTERN = re.compile(r"[a-z0-9_-]+\Z")
SVG_NS = "{http://www.w3.org/2000/svg}"


def load_agencies():
    data = json.loads(AGENCIES.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("agencies.json must contain a nonempty list of agencies")
    ids = set()
    names = set()
    for item in data:
        agency_id = item.get("id")
        name = item.get("name")
        en_short = item.get("en_short")
        if not agency_id or not SLUG_PATTERN.fullmatch(agency_id):
            raise ValueError(f"invalid agency id: {agency_id!r}")
        if not name or not en_short:
            raise ValueError(f"agency missing required fields: {item!r}")
        if agency_id in ids:
            raise ValueError(f"duplicate agency id: {agency_id}")
        if name in names:
            raise ValueError(f"duplicate agency name: {name}")
        ids.add(agency_id)
        names.add(name)
    return data


def logo_paths():
    root = ET.parse(LOGO).getroot()
    paths = root.findall(f"{SVG_NS}path")
    if root.get("viewBox") != "0 0 173.282 173.282" or len(paths) != 3:
        raise ValueError("unexpected Korea Government logo structure")
    return "".join(
        f'<path fill="{escape(path.attrib["fill"], quote=True)}" '
        f'd="{escape(path.attrib["d"], quote=True)}"/>'
        for path in paths
    )


def is_korean(text):
    return any(ord(c) >= 128 for c in text)


def render_badge(label_text, message_text, style, paths):
    if style not in STYLES:
        raise ValueError(f"unsupported badge style: {style!r}")

    prominent = style == "for-the-badge"
    outlined = style == "outline"
    glossy = style == "plastic"
    squared = style in ("flat-square", "for-the-badge")

    height = 28 if prominent else 22 if outlined else 20
    icon_size = 20 if prominent else 16
    icon_x = 6
    icon_y = (height - icon_size) / 2
    icon_scale = icon_size / 173.282
    text_x = icon_x + icon_size + 7

    is_ko_label = is_korean(label_text)
    is_ko_msg = is_korean(message_text)

    char_w_label = 11 if is_ko_label else (9 if prominent else 8)
    label_width = text_x + len(label_text) * char_w_label + (12 if prominent else 10)

    char_w_msg = 11 if is_ko_msg else (9 if prominent else 8)
    message_width = max(48, len(message_text) * char_w_msg + (24 if prominent else 20))

    width = label_width + message_width
    radius = 0 if squared else 4

    label_color = "#003764" if prominent else "#ffffff"
    message_color = "#e4032e" if prominent else "#ffffff" if outlined else "#134f8c"
    text_color = "#ffffff" if prominent else "#003764"
    version_color = "#134f8c" if outlined else "#ffffff"

    font_size_label = 11 if (prominent or is_ko_label) else 12
    font_size_msg = 11 if (prominent or is_ko_msg) else 12
    baseline = height / 2 + (3.7 if prominent else 4)

    font_family_ko = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', 'Malgun Gothic', Arial, sans-serif"
    font_family_en = "Arial, Helvetica, sans-serif"

    label_font = font_family_ko if is_ko_label else font_family_en
    msg_font = font_family_ko if is_ko_msg else font_family_en

    title_text = f"{label_text} {message_text} ({style})"
    aria_label = f"{label_text} {message_text}"

    gloss = (
        f'<defs><linearGradient id="gloss" x2="0" y2="100%">'
        f'<stop offset="0" stop-color="#fff" stop-opacity=".7"/>'
        f'<stop offset=".1" stop-color="#aaa" stop-opacity=".1"/>'
        f'<stop offset=".9" stop-color="#000" stop-opacity=".3"/>'
        f'<stop offset="1" stop-color="#000" stop-opacity=".5"/>'
        f'</linearGradient></defs>\n'
        f'<rect width="{width}" height="{height}" rx="{radius}" fill="url(#gloss)"/>\n'
    ) if glossy else ""

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(aria_label, quote=True)}">
<title>{escape(title_text)}</title>
<defs><clipPath id="badge-shape"><rect width="{width}" height="{height}" rx="{radius}"/></clipPath></defs>
<g clip-path="url(#badge-shape)">
<rect width="{width}" height="{height}" rx="{radius}" fill="{label_color}"/>
<path d="M{label_width} 0h{message_width}v{height}h-{message_width}z" fill="{message_color}"/>
{gloss}</g>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{radius}" fill="none" stroke="{'#134f8c' if outlined else '#d0d7de' if not prominent else '#003764'}"/>
<g transform="translate({icon_x} {icon_y:g}) scale({icon_scale:.8f})">{paths}</g>
<text x="{text_x}" y="{baseline:g}" fill="{text_color}" font-family="{label_font}" font-size="{font_size_label}" font-weight="600">{escape(label_text)}</text>
<text x="{label_width + message_width / 2:g}" y="{baseline:g}" fill="{version_color}" text-anchor="middle" font-family="{msg_font}" font-size="{font_size_msg}" font-weight="700">{escape(message_text)}</text>
</svg>
'''


def build_expected_badges(agencies, paths):
    expected = {}
    for agency in agencies:
        agency_id = agency["id"]
        name = agency["name"]
        en_short = agency["en_short"]

        for style in STYLES:
            # 1. 국문 기본: [ 대한민국 | 부처명 ]
            ko_badge = render_badge("대한민국", name, style, paths)
            expected[OUTPUT / agency_id / f"{style}.svg"] = ko_badge
            expected[OUTPUT / agency_id / f"{style}-ko.svg"] = ko_badge
            expected[OUTPUT / agency_id / "ko" / f"{style}.svg"] = ko_badge
            expected[OUTPUT / name / f"{style}.svg"] = ko_badge

            # 2. 영문 기본: [ Gov.kr | EN_SHORT ]
            en_badge = render_badge("Gov.kr", en_short, style, paths)
            expected[OUTPUT / agency_id / f"{style}-en.svg"] = en_badge
            expected[OUTPUT / agency_id / "en" / f"{style}.svg"] = en_badge
            expected[OUTPUT / name / f"{style}-en.svg"] = en_badge

            # 3. 기관명-약칭 배지: [ 부처명 | EN_SHORT ]
            abbr_badge = render_badge(name, en_short, style, paths)
            expected[OUTPUT / agency_id / f"{style}-abbr.svg"] = abbr_badge
            expected[OUTPUT / name / f"{style}-abbr.svg"] = abbr_badge

    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify committed badges match generated output")
    args = parser.parse_args()

    agencies = load_agencies()
    paths = logo_paths()
    expected = build_expected_badges(agencies, paths)
    existing = set(OUTPUT.glob("**/*.svg"))

    if args.check:
        mismatches = [p for p, content in expected.items() if not p.exists() or p.read_text(encoding="utf-8") != content]
        extras = existing - expected.keys()
        if mismatches or extras:
            for p in sorted([*mismatches, *extras]):
                print(f"out of date: {p.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print(f"Verified {len(expected)} badges")
        return 0

    for path in existing - expected.keys():
        path.unlink()
        curr = path.parent
        while curr != OUTPUT and curr != ROOT:
            try:
                curr.rmdir()
            except OSError:
                break
            curr = curr.parent

    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    print(f"Generated {len(expected)} badges across {len(agencies)} agencies")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
