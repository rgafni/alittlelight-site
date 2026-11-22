#!/usr/bin/env python3
"""Checks every Hebrew line on the page against Sefaria's "Tanach with Nikkud" text, letter for letter.
The brand wordmark (class he-name) is the app's name, not a quotation, so it is skipped."""
import re, sys, json, urllib.request, urllib.parse, html

PAGE = sys.argv[1] if len(sys.argv) > 1 else "index.html"
src = open(PAGE, encoding="utf-8").read()
SOURCES = {  # text on the page -> Sefaria ref
    "Psalms.119.37": None, "Psalms.119.105": None, "Psalms.121.1": None,
}
found = [html.unescape(m) for m in re.findall(r'<div class="he" lang="he" dir="rtl"[^>]*>([^<]+)</div>', src)]
found = sorted(set(found))

def fetch(ref):
    url = "https://www.sefaria.org/api/v3/texts/%s?version=%s&return_format=text_only" % (ref, urllib.parse.quote("hebrew|Tanach with Nikkud"))
    return json.load(urllib.request.urlopen(url))["versions"][0]["text"]

truth = {ref: fetch(ref) for ref in SOURCES}
ok = True
for line in found:
    hit = [r for r, t in truth.items() if t == line]
    print(("OK   " if hit else "FAIL ") + (hit[0] if hit else "no exact match") + "  " + line)
    ok &= bool(hit)
# no Names of Hashem: the four-letter Name, with any vowels, and common substitutes
bare = lambda s: re.sub(r"[\u0591-\u05C7]", "", s)
for line in found:
    b = bare(line).replace("־", " ")
    for w in b.split():
        if w in ("יהוה", "יקוק", "אדני", "ידוד", "אלהים", "אלוהים"):
            print("NAME FOUND:", line); ok = False
print("all Hebrew matches Sefaria, no Names:" , ok)
sys.exit(0 if ok else 1)
