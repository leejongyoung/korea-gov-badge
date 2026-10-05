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
COLOR_THEMES = {
    "blue": {  # Default 공공 블루
        "message_color": "#134f8c",
        "stroke_color": "#134f8c",
    },
    "navy": {  # 국가상징 딥 네이비
        "message_color": "#003764",
        "stroke_color": "#003764",
    },
    "black": {  # 다크 차콜 / GitHub 다크
        "message_color": "#24292f",
        "stroke_color": "#24292f",
    },
    "green": {  # 포레스트 / 에메랄드 그린
        "message_color": "#1a7f37",
        "stroke_color": "#1a7f37",
    },
    "red": {  # 태극 레드 / 크림슨
        "message_color": "#cf222e",
        "stroke_color": "#cf222e",
    },
    "gray": {  # 클래식 그레이
        "message_color": "#57606a",
        "stroke_color": "#57606a",
    },
}
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


def render_badge(label_text, message_text, style, logo_key, logos, color_theme="blue", custom_colors=None):
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

    # 색상 결정 (커스텀 색상 우선, 프리셋 테마 기본)
    if custom_colors:
        raw_msg_col = custom_colors.get("message_color", "#134f8c")
        raw_lbl_col = custom_colors.get("label_color", "#ffffff")
        raw_txt_col = custom_colors.get("text_color", "#003764")
        raw_ver_col = custom_colors.get("version_color", "#ffffff")
        raw_strk_col = custom_colors.get("stroke_color", raw_msg_col)
    else:
        theme = COLOR_THEMES.get(color_theme, COLOR_THEMES["blue"])
        raw_msg_col = theme["message_color"]
        raw_lbl_col = "#ffffff"
        raw_txt_col = "#003764"
        raw_ver_col = "#ffffff"
        raw_strk_col = theme["stroke_color"]

    if outlined:
        label_color = raw_lbl_col
        message_color = raw_lbl_col
        text_color = raw_txt_col
        version_color = raw_msg_col
        stroke_color = raw_strk_col
    else:
        label_color = raw_lbl_col
        message_color = raw_msg_col
        text_color = raw_txt_col
        version_color = raw_ver_col
        stroke_color = raw_strk_col if (prominent or style == "flat-square") else "#d0d7de"

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
    preset_colors = ("navy", "black", "green", "red", "gray")

    for agency in agencies:
        agency_id = agency["id"]
        name = agency["name"]
        en_short = agency["en_short"]
        agency_logo = agency.get("logo", "gov")

        for style in STYLES:
            # 1. 기본 배지 (Blue 테마)
            badge_blue = render_badge(name, en_short, style, agency_logo, logos, "blue")

            expected[OUTPUT / agency_id / f"{style}.svg"] = badge_blue
            expected[OUTPUT / agency_id / f"{style}-abbr.svg"] = badge_blue
            expected[OUTPUT / agency_id / f"{style}-agency.svg"] = badge_blue
            expected[OUTPUT / name / f"{style}.svg"] = badge_blue
            expected[OUTPUT / name / f"{style}-abbr.svg"] = badge_blue
            expected[OUTPUT / name / f"{style}-agency.svg"] = badge_blue

            # 2. 색상 프리셋 테마 (<style>-<color>.svg)
            for c_name in preset_colors:
                badge_c = render_badge(name, en_short, style, agency_logo, logos, c_name)
                expected[OUTPUT / agency_id / f"{style}-{c_name}.svg"] = badge_c
                expected[OUTPUT / name / f"{style}-{c_name}.svg"] = badge_c

            # 3. spo-legacy 호환용 기존 spo 경로 에일리어스
            if agency_id == "spo-legacy":
                expected[OUTPUT / "spo" / f"{style}.svg"] = badge_blue
                expected[OUTPUT / "spo" / f"{style}-abbr.svg"] = badge_blue
                expected[OUTPUT / "spo" / f"{style}-agency.svg"] = badge_blue
                expected[OUTPUT / "검찰청" / f"{style}.svg"] = badge_blue
                expected[OUTPUT / "검찰청" / f"{style}-abbr.svg"] = badge_blue
                expected[OUTPUT / "검찰청" / f"{style}-agency.svg"] = badge_blue
                for c_name in preset_colors:
                    badge_c = render_badge(name, en_short, style, agency_logo, logos, c_name)
                    expected[OUTPUT / "spo" / f"{style}-{c_name}.svg"] = badge_c
                    expected[OUTPUT / "검찰청" / f"{style}-{c_name}.svg"] = badge_c

    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify committed badges match generated output")
    parser.add_argument("--agency", help="generate on-demand custom badge for specific agency id")
    parser.add_argument("--style", default="flat", choices=STYLES, help="badge style")
    parser.add_argument("--color", help="custom message background color (e.g. #8250df or red)")
    parser.add_argument("--label-color", default="#ffffff", help="custom label background color (hex)")
    parser.add_argument("--text-color", default="#003764", help="custom label text color (hex)")
    parser.add_argument("--out", help="output file path for custom badge")
    args = parser.parse_args()

    agencies = load_agencies()
    logos = load_logos()

    # CLI 임의 커스텀 색상 배지 생성 모드
    if args.agency:
        matched = [a for a in agencies if a["id"] == args.agency or a["name"] == args.agency]
        if not matched:
            print(f"Error: agency {args.agency!r} not found", file=sys.stderr)
            return 1
        agency = matched[0]
        custom_cols = None
        color_theme = "blue"
        if args.color:
            if args.color in COLOR_THEMES:
                color_theme = args.color
            else:
                custom_cols = {
                    "message_color": args.color,
                    "label_color": args.label_color,
                    "text_color": args.text_color,
                    "version_color": "#ffffff",
                    "stroke_color": args.color,
                }
        svg = render_badge(
            agency["name"],
            agency["en_short"],
            args.style,
            agency.get("logo", "gov"),
            logos,
            color_theme=color_theme,
            custom_colors=custom_cols,
        )
        if args.out:
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(svg, encoding="utf-8")
            print(f"Generated custom badge for {agency['name']} -> {out_path}")
        else:
            sys.stdout.write(svg)
        return 0

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

    print(f"Generated {len(expected)} badges across {len(agencies)} agencies (including color variants)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
