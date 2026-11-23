# A Little Light

Public website for the A Little Light Android app.

Live: https://rgafni.github.io/alittlelight-site/

The planned custom domain is **alittlelight.app**. There is no `CNAME` file in the repo yet, on purpose: adding one makes GitHub redirect the github.io site to the custom domain, which would take the site offline until DNS is in place. After the DNS records below are live, add a repo file named `CNAME` containing exactly `alittlelight.app`, then:

1. At the registrar (Porkbun), add four `A` records for the apex `alittlelight.app`:
   - 185.199.108.153
   - 185.199.109.153
   - 185.199.110.153
   - 185.199.111.153
2. Add a `CNAME` record for `www` pointing to `rgafni.github.io`.
3. In the repo's Settings, Pages, confirm the custom domain is `alittlelight.app` and turn on Enforce HTTPS once the certificate is ready.
4. Then update the `og:image` URLs in the HTML to `https://alittlelight.app/img/og.png`.

Until DNS is live, the working public URL is the GitHub Pages address above.

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
