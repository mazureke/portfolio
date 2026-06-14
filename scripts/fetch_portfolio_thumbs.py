#!/usr/bin/env python3
"""Pre-generate UX portfolio thumbnails via thum.io and save real screenshots
locally. thum.io serves an animated GIF placeholder while it captures, then a
real PNG/JPEG once ready — so we retry until we get a non-GIF, and only save
real screenshots. Anything that never resolves is skipped (the page falls back
to a live thum.io URL via img onerror)."""
import os, time, urllib.request, urllib.parse, ssl

# (portfolio url, display name) — names auto-derived from the domain; easy to correct later.
PORTFOLIOS = [
    ("https://www.ralla.studio/about", "Ralla Studio"),
    ("https://www.perryw.ca/", "Perry Wang"),
    ("https://www.strelioff.com/work", "Strelioff"),
    ("https://robin-noguier.com/", "Robin Noguier"),
    ("https://www.zaidsyed.com/", "Zaid Syed"),
    ("https://abdussalam.pk/", "Abdus Salam"),
    ("https://jaclynchao.com/", "Jaclyn Chao"),
    ("https://ivomynttinen.com/", "Ivo Mynttinen"),
    ("https://buzzusborne.com/", "Buzz Usborne"),
    ("https://www.huiranli.com/", "Huiran Li"),
    ("https://www.faithkaufman.com/", "Faith Kaufman"),
    ("https://www.itsjosie.com/", "Josie"),
    ("https://michaellatwersky.com/", "Michael Latwersky"),
    ("https://paniati.com/home", "Paniati"),
    ("https://www.kysondana.com/", "Kyson Dana"),
    ("https://www.thatedchao.com/", "Ed Chao"),
    ("https://joshglucas.com/", "Josh Lucas"),
    ("https://www.aretoo.design/", "Aretoo"),
    ("https://www.wenjing.io/", "Wenjing"),
    ("https://www.pratibhajoshi.com/", "Pratibha Joshi"),
    ("https://www.josephz.me/", "Joseph Z"),
    ("https://lolajiang.com/index.html", "Lola Jiang"),
    ("https://www.tparkes.com/", "Tom Parkes"),
    ("https://adrianharwood.com/", "Adrian Harwood"),
    ("https://www.elizabethwang.design/", "Elizabeth Wang"),
    ("https://heckhouse.com/", "Heck House"),
    ("https://aleksitappura.com/", "Aleksi Tappura"),
    ("https://www.chengsuchen.com/", "Chengsu Chen"),
    ("https://www.alexlakas.com/", "Alex Lakas"),
    ("https://uxfol.io/maxberger", "Max Berger"),
    ("https://www.audreychou.com/", "Audrey Chou"),
    ("https://ginachee.com/", "Gina Chee"),
    ("https://www.annadeu.com/", "Anna Deu"),
    ("https://www.sirirosa.co/", "Siri Rosa"),
    ("https://www.joekndy.design/", "Joe Kndy"),
    ("https://www.jonnyczar.com/", "Jonny Czar"),
    ("https://robyndang.github.io/Portfolio/index.html", "Robyn Dang"),
    ("https://www.leedave.com/", "Lee Dave"),
    ("https://www.yukiasakura.com/", "Yuki Asakura"),
    ("https://www.joannecho.me/", "Joanne Cho"),
    ("https://www.yichenxie.com/", "Yichen Xie"),
    ("https://www.rachelyhe.com/", "Rachel He"),
    ("https://www.kurtwinterdesign.com/", "Kurt Winter"),
    ("https://www.byelliotowen.com/", "Elliot Owen"),
    ("https://www.adamriddle.com/", "Adam Riddle"),
    ("https://www.jeremy-stokes.com/", "Jeremy Stokes"),
    ("https://michellegore.com/", "Michelle Gore"),
    ("https://verlichen.com/", "Verlichen"),
    ("https://www.leah-lee.com/", "Leah Lee"),
    ("https://www.rajivsancheti.com/", "Rajiv Sancheti"),
    ("https://nighot.com/", "Nighot"),
    ("https://www.ayushwanjari.com/", "Ayush Wanjari"),
    ("https://www.glorialo.design/", "Gloria Lo"),
    ("https://arrowww.space/", "Arrow"),
    ("https://www.oishee.io/", "Oishee"),
    ("https://www.ericatsou.com/projects", "Erica Tsou"),
    ("https://www.greg-wolff.com/", "Greg Wolff"),
    ("https://www.holyokehirsch.com/", "Holyoke Hirsch"),
    ("https://www.itssharl.ee/", "Sharlee"),
    ("https://www.lifeofpai.com/", "Life of Pai"),
]

OUT = os.path.join(os.path.dirname(__file__), "..", "ux-portfolios", "portfolio-thumbs")
os.makedirs(OUT, exist_ok=True)
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE


def slug(name):
    return "".join(c if c.isalnum() else "-" for c in name.lower()).strip("-")


def thumb_url(url):
    return "https://image.thum.io/get/width/800/crop/600/noanimate/" + url


def fetch(url, attempts=8, wait=4):
    for i in range(attempts):
        try:
            req = urllib.request.Request(thumb_url(url), headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=40, context=ctx).read()
        except Exception as e:
            print(f"    attempt {i+1} error: {e}"); time.sleep(wait); continue
        if data[:6] == b"GIF89a" or data[:6] == b"GIF87a":
            print(f"    attempt {i+1}: still generating…"); time.sleep(wait); continue
        if len(data) < 1500:
            print(f"    attempt {i+1}: too small ({len(data)}b)"); time.sleep(wait); continue
        return data
    return None


if __name__ == "__main__":
    ok, fail = [], []
    for url, name in PORTFOLIOS:
        s = slug(name)
        print(f"[{name}] {url}", flush=True)
        data = fetch(url)
        if data:
            ext = "png" if data[:8] == b"\x89PNG\r\n\x1a\n" else "jpg"
            path = os.path.join(OUT, f"{s}.{ext}")
            with open(path, "wb") as f:
                f.write(data)
            print(f"    saved {s}.{ext} ({len(data)} bytes)", flush=True)
            ok.append(s)
        else:
            print(f"    FAILED — will fall back to live thumbnail", flush=True)
            fail.append(name)

    print(f"\nDONE. {len(ok)} saved, {len(fail)} failed.", flush=True)
    if fail:
        print("Failed:", ", ".join(fail), flush=True)
