#!/usr/bin/env python3
"""Generate the portfolio card HTML and inject it into ux-portfolios/index.html
(replacing the <!--PF_CARDS--> marker). Uses a locally-saved thumbnail when
present, otherwise a live thum.io URL; either way img onerror falls back to the
live thumbnail so a missing/blocked local file still shows something."""
import os, html
from fetch_portfolio_thumbs import PORTFOLIOS, slug, thumb_url, OUT

ROOT = os.path.join(os.path.dirname(__file__), "..")
PAGE = os.path.join(ROOT, "ux-portfolios", "index.html")


def domain(url):
    d = url.split("//", 1)[-1].split("/", 1)[0]
    return d[4:] if d.startswith("www.") else d


def local_thumb(s):
    for ext in ("png", "jpg"):
        if os.path.exists(os.path.join(OUT, f"{s}.{ext}")):
            return f"portfolio-thumbs/{s}.{ext}"
    return None


cards = []
missing = []
for url, name in PORTFOLIOS:
    s = slug(name)
    live = thumb_url(url)
    local = local_thumb(s)
    src = local or live
    if not local:
        missing.append(name)
    n, d = html.escape(name), html.escape(domain(url))
    cards.append(f'''        <a href="{html.escape(url)}" target="_blank" rel="noopener" class="pf-card">
          <div class="pf-thumb">
            <img src="{src}" alt="{n} — portfolio screenshot" loading="lazy" decoding="async"
                 onerror="this.onerror=null;this.src='{live}'">
          </div>
          <div class="pf-meta">
            <span class="pf-name">{n}</span>
            <span class="pf-cta">View →</span>
          </div>
          <p class="pf-domain">{d}</p>
        </a>''')

with open(PAGE, encoding="utf-8") as f:
    page = f.read()
page = page.replace("<!--PF_CARDS-->", "\n".join(cards))
with open(PAGE, "w", encoding="utf-8") as f:
    f.write(page)

print(f"Injected {len(cards)} cards. {len(missing)} using live fallback: {', '.join(missing) or 'none'}")
