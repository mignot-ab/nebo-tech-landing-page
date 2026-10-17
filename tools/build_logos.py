"""Generate the Nebo product logo family into assets/logos/.

Every product icon shares the parent brand's signature — the horizon arc and
four-point star from the Nebo Tech mark — over a single-hue tile, with one
white glyph for the product. Lockups pair the icon with the geometric NEBO
wordmark (E drawn as three bars, middle bar in accent) and a tracked product line.

Run: python3 tools/build_logos.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "logos"
NAVY = "#0A1633"
BLUE = "#1F6BFF"
FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Inter', 'Helvetica Neue', Arial, sans-serif"

PRODUCTS = {
    "erp": dict(name="ERP", line="ENTERPRISE RESOURCE PLANNING", top="#3D86FF", bottom="#0B3FC4", ink="#0B3FC4"),
    "bsms": dict(name="BSMS", line="BUSINESS & SALON MANAGEMENT", top="#FF8A5B", bottom="#E0402A", ink="#E0402A"),
    "dental": dict(name="Dental", line="DENTAL PRACTICE SUITE", top="#2DD4BF", bottom="#0F766E", ink="#0F766E"),
    "pharmacy": dict(name="Pharmacy", line="PHARMACY & DISPENSARY", top="#34D27B", bottom="#11803F", ink="#11803F"),
    "hospital": dict(name="Hospital & Clinic", line="HOSPITAL & CLINIC", top="#FF5C7A", bottom="#C4163C", ink="#C4163C"),
    "kiraypay": dict(name="KirayPay", line="PROPERTY & RENT", top="#8B7BFF", bottom="#4A32D9", ink="#4A32D9"),
}


def star(cx, cy, r):
    """Four-point star with concave sides, matching the Nebo Tech mark."""
    k = r * 0.16
    return (
        f"M{cx} {cy - r} C{cx + k} {cy - k} {cx + k} {cy - k} {cx + r} {cy} "
        f"C{cx + k} {cy + k} {cx + k} {cy + k} {cx} {cy + r} "
        f"C{cx - k} {cy + k} {cx - k} {cy + k} {cx - r} {cy} "
        f"C{cx - k} {cy - k} {cx - k} {cy - k} {cx} {cy - r}Z"
    )


GLYPHS = {
    # Three stacked modules: finance, inventory, people on one ledger.
    "erp": lambda c: (
        '<path d="M60 50 L84 62 L60 74 L36 62 Z" fill="#fff"/>'
        '<path d="M36 72 L60 84 L84 72" stroke="#fff" stroke-opacity=".85" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
        '<path d="M36 83 L60 95 L84 83" stroke="#fff" stroke-opacity=".6" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    ),
    # Shears: salon + retail counter.
    "bsms": lambda c: (
        '<path d="M45 52 L72 84" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M75 52 L48 84" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
        '<circle cx="44" cy="91" r="8" stroke="#fff" stroke-width="5" fill="none"/>'
        '<circle cx="76" cy="91" r="8" stroke="#fff" stroke-width="5" fill="none"/>'
        '<circle cx="60" cy="69.5" r="3" fill="' + c["bottom"] + '"/>'
    ),
    # Molar silhouette.
    "dental": lambda c: (
        '<path d="M60 56 C54 50 44 48 38.5 53 C32 59 34 70 37 78 C39.5 85 39.5 93 43 99 '
        'C46 103.5 50.5 101 51.5 95.5 C52.5 89.5 55 84 60 84 C65 84 67.5 89.5 68.5 95.5 '
        'C69.5 101 74 103.5 77 99 C80.5 93 80.5 85 83 78 C86 70 88 59 81.5 53 C76 48 66 50 60 56Z" fill="#fff"/>'
    ),
    # Two-tone capsule.
    "pharmacy": lambda c: (
        '<g transform="rotate(-40 60 76)">'
        '<rect x="31.5" y="63.5" width="57" height="25" rx="12.5" stroke="#fff" stroke-width="5" fill="none"/>'
        '<path d="M60 63.5 H44 A12.5 12.5 0 0 0 44 88.5 H60 Z" fill="#fff"/>'
        "</g>"
    ),
    # House with a coin for a door: rent collected.
    "kiraypay": lambda c: (
        '<path d="M32 73 L60 51 L88 73" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
        '<path d="M40 71 L60 56 L80 71 V97 A3 3 0 0 1 77 100 H43 A3 3 0 0 1 40 97 Z" fill="#fff"/>'
        '<circle cx="60" cy="85" r="8" fill="' + c["bottom"] + '"/>'
        '<path d="M60 80.5 V89.5" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    ),
    # Rounded cross cut by a pulse line.
    "hospital": lambda c: (
        '<path d="M53 50 H67 A3 3 0 0 1 70 53 V66 H83 A3 3 0 0 1 86 69 V83 A3 3 0 0 1 83 86 H70 V99 '
        'A3 3 0 0 1 67 102 H53 A3 3 0 0 1 50 99 V86 H37 A3 3 0 0 1 34 83 V69 A3 3 0 0 1 37 66 H50 V53 A3 3 0 0 1 53 50Z" fill="#fff"/>'
        '<path d="M28 76 H47 L53 65 L61 89 L67 76 H92" stroke="' + c["bottom"] + '" stroke-width="4.5" '
        'stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    ),
}


def icon_group(key, c, uid):
    """The 120×120 app-icon tile."""
    return f"""<defs>
    <linearGradient id="{uid}-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c['top']}"/><stop offset="1" stop-color="{c['bottom']}"/>
    </linearGradient>
    <linearGradient id="{uid}-sheen" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="{uid}-arc"><rect width="120" height="120" fill="#fff"/><circle cx="60" cy="30" r="9" fill="#000"/></mask>
  </defs>
  <rect width="120" height="120" rx="27" fill="url(#{uid}-bg)"/>
  <rect width="120" height="120" rx="27" fill="url(#{uid}-sheen)"/>
  <path d="M27 43 Q60 17 93 43" stroke="#fff" stroke-width="3" stroke-linecap="round" fill="none" mask="url(#{uid}-arc)"/>
  <path d="{star(60, 30, 7.5)}" fill="#fff"/>
  {GLYPHS[key](c)}"""


def nebo_wordmark(x, y, h, ink, accent):
    """Geometric NEBO at cap height h. Base design is 40 units tall, 190 wide."""
    s = h / 40
    return f"""<g transform="translate({x} {y}) scale({s})" fill="{ink}">
    <rect x="0" y="0" width="7" height="40" rx="1"/><rect x="33" y="0" width="7" height="40" rx="1"/>
    <path d="M0 0 H7.5 L40 40 H32.5 Z"/>
    <rect x="52" y="0" width="34" height="7" rx="1.5"/>
    <rect x="52" y="16.5" width="33" height="7" rx="1.5" fill="{accent}"/>
    <rect x="52" y="33" width="34" height="7" rx="1.5"/>
    <path d="M101.5 3.5 V36.5 M101.5 3.5 H120 A8.25 8.25 0 0 1 120 20 H101.5 M101.5 20 H122 A8.25 8.25 0 0 1 122 36.5 H101.5" fill="none" stroke="{ink}" stroke-width="7" stroke-linejoin="miter"/>
    <path d="M155 0 H178 A12 12 0 0 1 190 12 V28 A12 12 0 0 1 178 40 H155 A12 12 0 0 1 143 28 V12 A12 12 0 0 1 155 0 Z M157 7 A7 7 0 0 0 150 14 V26 A7 7 0 0 0 157 33 H176 A7 7 0 0 0 183 26 V14 A7 7 0 0 0 176 7 Z" fill-rule="evenodd"/>
  </g>"""


def svg(w, h, body, label):
    label = label.replace("&", "&amp;")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'fill="none" role="img" aria-label="{label}">\n  <title>{label}</title>\n  {body}\n</svg>\n'
    )


def write(name, text):
    (OUT / name).write_text(text)
    print("wrote", name)


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    for key, c in PRODUCTS.items():
        label = f"NEBO {c['name']}"
        write(f"nebo-{key}-icon.svg", svg(120, 120, icon_group(key, c, key), label))

        # Horizontal lockup: icon | NEBO over tracked product line.
        line = c["name"].upper().replace("&", "&amp;")
        width = round(150 + max(209, len(c["name"]) * 17.5) + 16)
        for variant, ink, sub in (("", NAVY, c["ink"]), ("-dark", "#FFFFFF", "#FFFFFF")):
            body = (
                icon_group(key, c, key + variant)
                + nebo_wordmark(150, 26, 44, ink, BLUE if variant == "" else "#5B93FF")
                + f'<text x="151" y="99" font-family="{FONT}" font-size="17" font-weight="600" '
                f'letter-spacing="5.5" fill="{sub}">{line}</text>'
            )
            write(f"nebo-{key}{variant}.svg", svg(width, 120, body, label))

    # Parent mark, redrawn as vector from the official PNG.
    for variant, ink, accent in (("", NAVY, BLUE), ("-dark", "#FFFFFF", "#5B93FF")):
        body = (
            f'<defs><mask id="nt{variant}-arc"><rect width="420" height="200" fill="#fff"/><circle cx="210" cy="26" r="16" fill="#000"/></mask></defs>'
            f'<path d="M86 78 Q210 -14 334 78" stroke="{accent}" stroke-width="4" stroke-linecap="round" mask="url(#nt{variant}-arc)"/>'
            f'<path d="{star(210, 26, 14)}" fill="{accent}"/>'
            + nebo_wordmark(20, 90, 60, ink, accent)
            + f'<text x="210" y="190" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="500" '
            f'letter-spacing="9" fill="{ink}">TECH SOLUTION PLC.</text>'
        )
        write(f"nebo-tech{variant}.svg", svg(420, 200, body, "Nebo Tech Solution PLC"))

    # Compact parent mark for favicon / nav.
    mark = (
        f'<rect width="120" height="120" rx="27" fill="{NAVY}"/>'
        f'<defs><mask id="nm-arc"><rect width="120" height="120" fill="#fff"/><circle cx="60" cy="34" r="10" fill="#000"/></mask></defs>'
        f'<path d="M24 50 Q60 18 96 50" stroke="{BLUE}" stroke-width="3.5" stroke-linecap="round" mask="url(#nm-arc)"/>'
        f'<path d="{star(60, 34, 8.5)}" fill="{BLUE}"/>'
        '<rect x="36" y="58" width="48" height="9" rx="2" fill="#fff"/>'
        f'<rect x="36" y="74" width="46" height="9" rx="2" fill="{BLUE}"/>'
        '<rect x="36" y="90" width="48" height="9" rx="2" fill="#fff"/>'
    )
    write("nebo-mark.svg", svg(120, 120, mark, "Nebo Tech"))


if __name__ == "__main__":
    build()
