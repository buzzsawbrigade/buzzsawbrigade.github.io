#!/usr/bin/env python3
"""Builds the static Buzzsaw Brigade site from the page bodies in pages/.

Each pages/<name>.html file starts with three lines:
  title: ...
  description: ...
  nav: <nav key>
followed by a blank line and the body HTML. Run: python3 build.py
"""
import pathlib, html

ROOT = pathlib.Path(__file__).parent
SITE_URL = "https://buzzsawbrigade.github.io/"
EMAIL = "pcfixer@helpdeskmastercomputersupport.org"
UPDATED = "November 1, 2026"

NAV = [
    ("home", "index.html", "Home"),
    ("support", "support.html", "Support"),
    ("privacy", "privacy.html", "Privacy Policy"),
    ("delete", "delete-data.html", "Delete Data"),
    ("odds", "odds.html", "Summon Odds"),
    ("terms", "terms.html", "Terms"),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}img/og.jpg">
<meta name="theme-color" content="#0d0b09">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600;700&family=Big+Shoulders+Display:wght@800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/icon-192.png" alt="" width="34" height="34"><span>Buzzsaw Brigade</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div>Buzzsaw Brigade is made by the Buzzsaw Brigade team.<br>Contact: <a class="email" href="mailto:{email}">{email}</a></div>
    <nav aria-label="Footer">
      <a href="support.html">Support</a>
      <a href="privacy.html">Privacy Policy</a>
      <a href="delete-data.html">Delete Your Data</a>
      <a href="odds.html">Summon Odds</a>
      <a href="terms.html">Terms of Use</a>
    </nav>
  </div>
</footer>
<script>
  (function () {
    var b = document.querySelector(".menu-btn"), n = document.getElementById("nav");
    if (!b || !n) return;
    b.addEventListener("click", function () {
      var open = n.classList.toggle("open");
      b.setAttribute("aria-expanded", open ? "true" : "false");
    });
  })();
</script>
</body>
</html>
"""


def build():
    out = []
    for src in sorted((ROOT / "pages").glob("*.html")):
        raw = src.read_text()
        meta, body = raw.split("\n\n", 1)
        m = dict(line.split(": ", 1) for line in meta.splitlines())
        key = m["nav"]
        nav = "".join(
            f'<a href="{href}"{" aria-current=\"page\"" if k == key else ""}>{label}</a>' for k, href, label in NAV
        )
        name = src.name
        url = SITE_URL + ("" if name == "index.html" else name)
        body = body.replace("{{EMAIL}}", EMAIL).replace("{{UPDATED}}", UPDATED)
        page = HEAD.format(title=html.escape(m["title"]), desc=html.escape(m["description"]), url=url, site=SITE_URL, nav=nav) + body + FOOT.replace("{email}", EMAIL)
        (ROOT / name).write_text(page)
        out.append(name)
    urls = "".join(f"  <url><loc>{SITE_URL}{'' if n == 'index.html' else n}</loc></url>\n" for n in out)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    print("built", ", ".join(out))


if __name__ == "__main__":
    build()
