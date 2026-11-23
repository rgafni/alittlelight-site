# A Little Light

Public website for the A Little Light Android app.

Live: https://alittlelight.app/

The custom domain is **alittlelight.app**. A `CNAME` file in this repo tells GitHub Pages to serve the site there. DNS at the registrar (Porkbun):

1. Four `A` records for the apex `alittlelight.app`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
2. A `CNAME` record for `www` pointing to `rgafni.github.io`
3. In the repo's Settings, Pages, the custom domain is `alittlelight.app`. Enforce HTTPS once the certificate is ready.

The github.io address, https://rgafni.github.io/alittlelight-site/, redirects to the custom domain.

## What is here

- `index.html`, `about.html`, `app.html`, `contact.html`, `privacy.html`, `styles.css`: the public site. No build step, no JavaScript, no trackers, no external requests except links you choose to follow.
- `fonts/`: Frank Ruhl Libre, Newsreader and Libre Franklin as subsetted WOFF2, with their SIL Open Font License texts.
- `img/`: the app icon, the flame, drawings of the app screens, the social preview image and favicons.
- `preview/`: short redirects from the earlier review URLs to the live pages.
- `tools/verify_hebrew.py`: checks that the only Hebrew on the public pages is the app's name, and that no Names of Hashem appear. Run `python3 tools/verify_hebrew.py`.

## Rules for the copy

- Describe only what the app does, as written in the app's PRODUCT.md and DECISIONS.md. No invented features, claims, testimonials or download counts.
- Plain public language only. No internal development wording.
- No em dashes.
- Any Hebrew is checked with the script above. The site shows no Names of Hashem, and does not quote licensed editions until a license is settled.
- The phone screens on the page are drawings made for the page, not screenshots.
