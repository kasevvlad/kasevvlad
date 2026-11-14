#!/usr/bin/env python3
"""Builds the SVG images used in the profile README: python3 scripts/build_assets.py"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
MONO_CHAR = 0.61

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "card": "#161b22",
        "border": "#30363d",
        "text": "#e6edf3",
        "muted": "#8b949e",
        "faint": "#21262d",
        "accent": "#2dd4bf",
        "accent_soft": "#2dd4bf22",
        "warn": "#f0b429",
    },
    "light": {
        "bg": "#ffffff",
        "card": "#f6f8fa",
        "border": "#d0d7de",
        "text": "#1f2328",
        "muted": "#59636e",
        "faint": "#e6eaef",
        "accent": "#0f766e",
        "accent_soft": "#0f766e1a",
        "warn": "#b7791f",
    },
}

LANG_COLORS = {
    "Swift": "#F05138",
    "PHP": "#777BB4",
    "Go": "#00ADD8",
    "Notes": "#8b949e",
}

PROJECTS = [
    {
        "name": "prostor",
        "lang": "Swift",
        "new": True,
        "desc": [
            "Free disk cleaner and space analyzer for",
            "macOS: caches, leftovers of removed apps,",
            "large files. Everything goes to the Trash.",
        ],
        "tags": ["SwiftUI", "FileManager", "safe cleanup"],
    },
    {
        "name": "wave-bar",
        "lang": "Swift",
        "desc": [
            "Yandex Music player for the macOS menu bar:",
            "My Wave and liked tracks, media keys and",
            "Now Playing in Control Center.",
        ],
        "tags": ["SwiftUI", "AVFoundation", "MenuBarExtra"],
    },
    {
        "name": "cs16-launcher",
        "lang": "Swift",
        "desc": [
            "Native Counter-Strike 1.6 launcher for",
            "Apple Silicon Macs: SwiftUI + Xash3D FWGS,",
            "game data comes from your Steam copy.",
        ],
        "tags": ["SwiftUI", "arm64", "macOS 13+"],
    },
    {
        "name": "idempotency",
        "lang": "PHP",
        "desc": [
            "Idempotency-Key header for Laravel and",
            "Symfony: a retried POST returns the stored",
            "response instead of charging twice.",
        ],
        "tags": ["Laravel", "Symfony", "Packagist"],
    },
    {
        "name": "webhook-relay",
        "lang": "Go",
        "desc": [
            "Webhook delivery service with HMAC",
            "signatures, exponential backoff and",
            "a PostgreSQL queue.",
        ],
        "tags": ["PostgreSQL", "SKIP LOCKED", "HMAC"],
    },
    {
        "name": "outbox-relay",
        "lang": "Go",
        "desc": [
            "Transactional outbox: events go from",
            "PostgreSQL to NATS JetStream without",
            "being lost or duplicated.",
        ],
        "tags": ["NATS", "JetStream", "PostgreSQL"],
    },
    {
        "name": "rate-limiter",
        "lang": "Go",
        "desc": [
            "Token bucket in memory and sliding window",
            "in Redis, written from scratch, with",
            "net/http middleware on top.",
        ],
        "tags": ["Redis", "net/http", "middleware"],
    },
    {
        "name": "learning-notes",
        "lang": "Notes",
        "lang_label": "Notes · RU",
        "desc": [
            "Go for PHP developers in 16 lessons, plus",
            "notes on idempotency, queues, webhooks,",
            "rate limiting and the outbox pattern.",
        ],
        "tags": ["Go course", "backend", "reliability"],
    },
]

STACK = [
    ("backend", ["PHP", "Laravel", "Symfony", "API Platform"]),
    ("data", ["PostgreSQL", "MySQL", "Redis", "Manticore"]),
    ("infra", ["Docker", "NATS JetStream", "GitHub Actions"]),
    ("frontend", ["Vue", "TypeScript"]),
    ("learning", ["Go"]),
]

STACK_COLORS = {
    "PHP": "#777BB4",
    "Laravel": "#FF2D20",
    "Symfony": "#8b949e",
    "API Platform": "#38A9B4",
    "PostgreSQL": "#4169E1",
    "MySQL": "#00758F",
    "Redis": "#DC382D",
    "Manticore": "#4DB6AC",
    "Docker": "#2496ED",
    "NATS JetStream": "#27AAE1",
    "GitHub Actions": "#2088FF",
    "Vue": "#42B883",
    "TypeScript": "#3178C6",
    "Go": "#00ADD8",
}


def mono_width(text, size):
    return len(text) * size * MONO_CHAR


def svg(width, height, body, label):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(label)}">\n'
        f"{body}\n</svg>\n"
    )


def header(t):
    w, h = 1000, 300
    nodes = [("client", 590), ("api", 700), ("outbox", 810), ("worker", 920)]
    line_y = 150
    parts = [
        "<defs>",
        '<pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse">'
        f'<circle cx="2" cy="2" r="1.3" fill="{t["border"]}"/></pattern>',
        '<linearGradient id="fade" x1="0" x2="1" y1="0" y2="0">'
        '<stop offset="0.35" stop-color="#fff" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#fff" stop-opacity="1"/></linearGradient>',
        f'<mask id="fadeMask"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>',
        f'<clipPath id="frame"><rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="16"/></clipPath>',
        "<style>"
        f"@keyframes blink {{ 0%, 49% {{ opacity: 1 }} 50%, 100% {{ opacity: 0 }} }}"
        ".cursor { animation: blink 1.1s steps(1) infinite }"
        f"@keyframes pulse {{ 0%, 100% {{ opacity: .35 }} 50% {{ opacity: 1 }} }}"
        ".live { animation: pulse 2.4s ease-in-out infinite }"
        "</style>",
        "</defs>",
        f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="16" fill="{t["card"]}" stroke="{t["border"]}"/>',
        f'<g clip-path="url(#frame)"><rect width="{w}" height="{h}" fill="url(#dots)" mask="url(#fadeMask)"/>',
        f'<rect width="{w}" height="40" fill="{t["bg"]}" opacity="0.55"/>'
        f'<line x1="0" y1="40" x2="{w}" y2="40" stroke="{t["border"]}"/></g>',
    ]
    for i, color in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        parts.append(f'<circle cx="{26 + i * 20}" cy="20" r="6" fill="{color}"/>')
    parts.append(
        f'<text x="{w / 2}" y="25" text-anchor="middle" font-family="{MONO}" font-size="13" '
        f'fill="{t["muted"]}">kasevvlad@github: ~</text>'
    )

    parts += [
        f'<text x="48" y="92" font-family="{MONO}" font-size="15" fill="{t["accent"]}">$ whoami</text>',
        f'<text x="48" y="144" font-family="{SANS}" font-size="46" font-weight="700" '
        f'fill="{t["text"]}" letter-spacing="-0.5">Vladislav Kasev</text>',
        f'<text x="48" y="182" font-family="{SANS}" font-size="20" fill="{t["muted"]}">'
        "Backend developer · Uzbekistan</text>",
        f'<text x="48" y="222" font-family="{MONO}" font-size="14" fill="{t["text"]}">'
        "PHP · Laravel · Symfony · PostgreSQL · Go</text>",
        f'<text x="48" y="256" font-family="{MONO}" font-size="14" fill="{t["muted"]}">'
        f'<tspan fill="{t["accent"]}">&gt;</tspan> retries · queues · outbox · idempotency'
        f'<tspan class="cursor" fill="{t["accent"]}"> ▍</tspan></text>',
    ]

    first, last = nodes[0][1], nodes[-1][1]
    parts.append(
        f'<line x1="{first}" y1="{line_y}" x2="{last}" y2="{line_y}" stroke="{t["border"]}" '
        'stroke-width="2" stroke-dasharray="4 5"/>'
    )
    retry = (
        f"M {nodes[3][1] - 8} {line_y - 16} C {nodes[3][1] - 20} {line_y - 62}, "
        f"{nodes[2][1] + 20} {line_y - 62}, {nodes[2][1] + 8} {line_y - 16}"
    )
    parts.append(
        f'<path d="{retry}" fill="none" stroke="{t["warn"]}" stroke-width="1.5" '
        'stroke-dasharray="3 5" opacity="0.8"/>'
        f'<text x="{(nodes[2][1] + nodes[3][1]) / 2}" y="{line_y - 60}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="11" fill="{t["warn"]}">retry · backoff</text>'
    )

    for label, cx in nodes:
        parts.append(
            f'<circle cx="{cx}" cy="{line_y}" r="13" fill="{t["bg"]}" stroke="{t["border"]}" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{line_y}" r="4" fill="{t["muted"]}"/>'
            f'<text x="{cx}" y="{line_y + 38}" text-anchor="middle" font-family="{MONO}" '
            f'font-size="13" fill="{t["text"]}">{label}</text>'
        )

    path = f"M {first} {line_y} L {last} {line_y}"
    for offset in (0, 1.4, 2.8):
        parts.append(
            f'<rect x="-5" y="-5" width="10" height="10" rx="2.5" fill="{t["accent"]}">'
            f'<animateMotion dur="4.2s" begin="-{offset}s" repeatCount="indefinite" path="{path}"/></rect>'
        )
    parts.append(
        f'<rect x="-4" y="-4" width="8" height="8" rx="2" fill="{t["warn"]}" opacity="0">'
        f'<animateMotion dur="6s" begin="0s" repeatCount="indefinite" '
        f'keyPoints="0;0;1;1" keyTimes="0;0.5;0.8;1" calcMode="linear" path="{retry}"/>'
        '<animate attributeName="opacity" values="0;0;1;1;0;0" '
        'keyTimes="0;0.49;0.51;0.79;0.81;1" dur="6s" begin="0s" repeatCount="indefinite"/></rect>'
    )

    parts.append(
        f'<text x="{first - 13}" y="{line_y + 86}" font-family="{MONO}" font-size="11.5" '
        f'fill="{t["muted"]}"><tspan fill="{t["accent"]}">POST</tspan> /payments  Idempotency-Key: 8e03…f324</text>'
        f'<circle class="live" cx="{last + 13}" cy="{line_y + 82}" r="4" fill="{t["accent"]}"/>'
    )
    return svg(w, h, "\n".join(parts), "Vladislav Kasev, backend developer: PHP, Laravel, Symfony, PostgreSQL, Go")


def card(p, t):
    pad = 8
    w, h = 480, 200
    cw, ch = w - pad * 2, h - pad * 2
    color = LANG_COLORS[p["lang"]]
    label = p.get("lang_label", p["lang"])
    parts = [
        f'<defs><clipPath id="c"><rect x="{pad}" y="{pad}" width="{cw}" height="{ch}" rx="12"/></clipPath></defs>',
        f'<rect x="{pad + 0.5}" y="{pad + 0.5}" width="{cw - 1}" height="{ch - 1}" rx="12" '
        f'fill="{t["card"]}" stroke="{t["border"]}"/>',
        f'<rect x="{pad}" y="{pad}" width="{cw}" height="3" fill="{color}" clip-path="url(#c)"/>',
        f'<text x="{pad + 22}" y="{pad + 42}" font-family="{SANS}" font-size="20" font-weight="600" '
        f'fill="{t["text"]}">{escape(p["name"])}</text>',
    ]

    right = pad + cw - 22
    lw = mono_width(label, 12)
    parts.append(
        f'<text x="{right}" y="{pad + 39}" text-anchor="end" font-family="{MONO}" font-size="12" '
        f'fill="{t["muted"]}">{escape(label)}</text>'
        f'<circle cx="{right - lw - 10}" cy="{pad + 35}" r="5" fill="{color}"/>'
    )
    if p.get("new"):
        bx = right - lw - 26 - 44
        parts.append(
            f'<rect x="{bx}" y="{pad + 24}" width="44" height="20" rx="10" fill="{t["accent_soft"]}" '
            f'stroke="{t["accent"]}" stroke-opacity="0.5"/>'
            f'<text x="{bx + 22}" y="{pad + 38}" text-anchor="middle" font-family="{MONO}" '
            f'font-size="11" font-weight="600" fill="{t["accent"]}">new</text>'
        )

    for i, line in enumerate(p["desc"]):
        parts.append(
            f'<text x="{pad + 22}" y="{pad + 76 + i * 22}" font-family="{SANS}" font-size="14.5" '
            f'fill="{t["muted"]}">{escape(line)}</text>'
        )

    x = pad + 22
    y = pad + ch - 40
    for tag in p["tags"]:
        tw = mono_width(tag, 11) + 18
        parts.append(
            f'<rect x="{x}" y="{y}" width="{tw:.1f}" height="22" rx="6" fill="{t["bg"]}" stroke="{t["border"]}"/>'
            f'<text x="{x + tw / 2:.1f}" y="{y + 15}" text-anchor="middle" font-family="{MONO}" '
            f'font-size="11" fill="{t["muted"]}">{escape(tag)}</text>'
        )
        x += tw + 8
    return svg(w, h, "\n".join(parts), f'{p["name"]}: {" ".join(p["desc"])}')


def stack(t):
    w = 1000
    row_h = 46
    top = 28
    h = top * 2 + row_h * len(STACK) - 10
    parts = [
        f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="16" fill="{t["card"]}" stroke="{t["border"]}"/>'
    ]
    for r, (group, items) in enumerate(STACK):
        y = top + r * row_h
        parts.append(
            f'<text x="36" y="{y + 22}" font-family="{MONO}" font-size="13" fill="{t["muted"]}">'
            f'<tspan fill="{t["accent"]}">#</tspan> {group}</text>'
        )
        x = 170
        for item in items:
            tw = mono_width(item, 13) + 40
            parts.append(
                f'<rect x="{x}" y="{y}" width="{tw:.1f}" height="32" rx="8" fill="{t["bg"]}" stroke="{t["border"]}"/>'
                f'<circle cx="{x + 16}" cy="{y + 16}" r="5" fill="{STACK_COLORS[item]}"/>'
                f'<text x="{x + 28}" y="{y + 21}" font-family="{MONO}" font-size="13" '
                f'fill="{t["text"]}">{escape(item)}</text>'
            )
            x += tw + 10
        if r < len(STACK) - 1:
            parts.append(
                f'<line x1="36" y1="{y + row_h - 7}" x2="{w - 36}" y2="{y + row_h - 7}" '
                f'stroke="{t["faint"]}"/>'
            )
    label = "Stack: " + "; ".join(f"{g}: {', '.join(i)}" for g, i in STACK)
    return svg(w, h, "\n".join(parts), label)


def main():
    OUT.mkdir(exist_ok=True)
    for name, t in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(header(t))
        (OUT / f"stack-{name}.svg").write_text(stack(t))
        for p in PROJECTS:
            (OUT / f"card-{p['name']}-{name}.svg").write_text(card(p, t))


if __name__ == "__main__":
    main()
