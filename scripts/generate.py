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
LOGOS_DIR = ROOT / "assets" / "logos"
OUTPUT = ROOT / "badges"
STYLES = ("flat", "flat-square", "plastic", "for-the-badge", "outline")
SLUG_PATTERN = re.compile(r"[a-z0-9_-]+\Z")
SVG_NS = "{http://www.w3.org/2000/svg}"

ET.register_namespace("", "http://www.w3.org/2000/svg")
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


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


def clean_inner_svg(element):
    raw = ET.tostring(element, encoding="unicode")
    return re.sub(r'\s+xmlns(:\w+)?="http://www\.w3\.org/2000/svg"', "", raw)


def load_logos():
    logos = {}
    for p in LOGOS_DIR.glob("*.svg"):
        root = ET.parse(p).getroot()
        vb = root.get("viewBox")
        if vb:
            parts = [float(x) for x in vb.split()]
            min_x, min_y, vb_w, vb_h = parts[0], parts[1], parts[2], parts[3]
        else:
            min_x = 0.0
            min_y = 0.0
            vb_w = float(root.get("width", 300))
            vb_h = float(root.get("height", 300))

        inner = []
        for child in root:
            tag = child.tag.split("}")[-1]
            if tag in ("metadata", "namedview"):
                continue
            inner.append(clean_inner_svg(child))

        content = "".join(inner)
        logos[p.stem] = (min_x, min_y, vb_w, vb_h, content)

    if "gov" not in logos:
        raise ValueError("assets/logos/gov.svg is required")

    return logos


def is_korean(text):
    return any(ord(c) >= 128 for c in text)


def render_badge(label_text, message_text, style, logo_key, logos):
    if style not in STYLES:
        raise ValueError(f"unsupported badge style: {style!r}")
    if logo_key not in logos:
        raise ValueError(f"unsupported logo key: {logo_key!r}")

    prominent = style == "for-the-badge"
    outlined = style == "outline"
    glossy = style == "plastic"
    squared = style in ("flat-square", "for-the-badge")

    height = 28 if prominent else 22 if outlined else 20
    max_icon_h = 18 if prominent else 14
    max_icon_w = 26 if prominent else 20

    min_x, min_y, vb_w, vb_h, content = logos[logo_key]
    scale = min(max_icon_w / vb_w, max_icon_h / vb_h)
    icon_w = vb_w * scale
    icon_h = vb_h * scale
    icon_x = 6
    icon_y = (height - icon_h) / 2
    tx = icon_x - min_x * scale
    ty = icon_y - min_y * scale

    text_x = round(icon_x + icon_w + (7 if prominent else 6), 2)
    is_ko_label = is_korean(label_text)
    is_ko_msg = is_korean(message_text)

    char_w_label = 12 if (prominent and is_ko_label) else 11 if is_ko_label else (9 if prominent else 8)
    label_width = round(text_x + len(label_text) * char_w_label + (14 if prominent else 10), 1)

    char_w_msg = 12 if (prominent and is_ko_msg) else 11 if is_ko_msg else (9 if prominent else 8)
    message_width = max(48 if not prominent else 58, round(len(message_text) * char_w_msg + (24 if prominent else 20), 1))

    width = label_width + message_width
    radius = 0 if squared else 4

    # for-the-badge도 다른 스타일들과 동일한 톤앤매너(화이트 레이블, 블루 메시지) 적용
    label_color = "#ffffff"
    message_color = "#ffffff" if outlined else "#134f8c"
    text_color = "#003764"
    version_color = "#134f8c" if outlined else "#ffffff"
    stroke_color = "#134f8c" if (outlined or prominent) else "#d0d7de"

    font_size_label = 11 if (prominent or is_ko_label) else 12
    font_size_msg = 11 if (prominent or is_ko_msg) else 12
    baseline = height / 2 + (4 if prominent else 4)

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
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{radius}" fill="none" stroke="{stroke_color}"/>
<g transform="translate({tx:.3f} {ty:.3f}) scale({scale:.6f})">{content}</g>
<text x="{text_x}" y="{baseline:g}" fill="{text_color}" font-family="{label_font}" font-size="{font_size_label}" font-weight="600">{escape(label_text)}</text>
<text x="{label_width + message_width / 2:g}" y="{baseline:g}" fill="{version_color}" text-anchor="middle" font-family="{msg_font}" font-size="{font_size_msg}" font-weight="700">{escape(message_text)}</text>
</svg>
'''


def build_expected_badges(agencies, logos):
    expected = {}
    for agency in agencies:
        agency_id = agency["id"]
        name = agency["name"]
        en_short = agency["en_short"]
        agency_logo = agency.get("logo", "gov")

        for style in STYLES:
            # 기관 고유 배지: [ 기관명 | 영문약칭 ]
            # (해당 기관 공식 엠블럼 또는 통합 정부상징 심벌 적용)
            badge = render_badge(name, en_short, style, agency_logo, logos)

            # 1. 영문 식별자 디렉터리 경로
            expected[OUTPUT / agency_id / f"{style}.svg"] = badge
            expected[OUTPUT / agency_id / f"{style}-abbr.svg"] = badge
            expected[OUTPUT / agency_id / f"{style}-agency.svg"] = badge

            # 2. 한글 기관명 디렉터리 경로
            expected[OUTPUT / name / f"{style}.svg"] = badge
            expected[OUTPUT / name / f"{style}-abbr.svg"] = badge
            expected[OUTPUT / name / f"{style}-agency.svg"] = badge

    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify committed badges match generated output")
    args = parser.parse_args()

    agencies = load_agencies()
    logos = load_logos()
    expected = build_expected_badges(agencies, logos)
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
