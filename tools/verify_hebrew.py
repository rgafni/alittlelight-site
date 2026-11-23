#!/usr/bin/env python3
"""Checks public pages: the only Hebrew is the app name מְעַט אוֹר, and no Names of Hashem appear."""
import re, sys, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGES = [ROOT / n for n in ("index.html", "about.html", "app.html", "contact.html", "privacy.html")]
NAME = "מְעַט אוֹר"
HEBREW = re.compile(r"[\u0590-\u05FF]+(?:[\u0590-\u05FF\s־׳״]*[\u0590-\u05FF]+)?")
# four-letter Name and common substitutes, after stripping vowels
NAMES = {"יהוה", "יקוק", "אדני", "ידוד", "אלהים", "אלוהים"}

def bare(s: str) -> str:
    return re.sub(r"[\u0591-\u05C7]", "", s)

ok = True
for page in PAGES:
    src = html.unescape(page.read_text(encoding="utf-8"))
    # ignore latin-only; collect Hebrew runs
    runs = HEBREW.findall(src)
    # filter out empty / marks-only
    words_ok = []
    for run in runs:
        letters = bare(run).replace("־", " ").replace("׳", "").replace("״", "")
        letters = " ".join(letters.split())
        if not letters:
            continue
        if letters.replace(" ", "") == bare(NAME).replace(" ", ""):
            words_ok.append(run)
            continue
        print(f"UNEXPECTED HEBREW in {page.name}: {run}")
        ok = False
        for w in letters.split():
            if w in NAMES:
                print(f"NAME FOUND in {page.name}: {run}")
                ok = False
    if "—" in src or "\u2014" in src:
        print(f"EM DASH in {page.name}")
        ok = False
    if "For Roni" in src or "Preview" in src and "preview" not in page.name:
        # Preview word should not appear on live pages
        if "For Roni" in src or re.search(r">Preview<", src) or "The live site is unchanged" in src:
            print(f"INTERNAL PREVIEW COPY in {page.name}")
            ok = False
    print(f"{page.name}: Hebrew runs allowed={len(words_ok)}")

print("ok" if ok else "FAILED")
sys.exit(0 if ok else 1)
