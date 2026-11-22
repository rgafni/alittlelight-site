# A Little Light: website

One-page static site for **A Little Light**, an Android app that shows a passage of Torah and a short reading pause just before an app or site you chose to guard opens.

Live: https://rgafni.github.io/alittlelight-site/

## What is here

- `index.html`, `styles.css`: the whole site. No build step, no JavaScript, no trackers, no external requests.
- `fonts/`: Frank Ruhl Libre, Newsreader and Libre Franklin as subsetted WOFF2, with their SIL Open Font License texts.
- `img/`: the app icon, the flame, the social preview image and favicons, all made from the app's existing icon.
- `tools/verify_hebrew.py`: checks every Hebrew line on the page, letter for letter, against Sefaria's "Tanach with Nikkud" text, and that no Names of Hashem appear. Run `python3 tools/verify_hebrew.py index.html`.

## Rules for the copy

- Describe only what the app does, as written in the app's PRODUCT.md and DECISIONS.md. No invented features, claims, testimonials or download counts.
- No em dashes.
- Any Hebrew is copied from Sefaria and checked with the script above. The site shows no Names of Hashem.
- The phone screens on the page are drawings made for the page, not screenshots, and the page says so.

## Domain note (not set up yet)

The planned domain is **alittlelight.app**. It is not bought yet, so there is **no `CNAME` file** in this repo on purpose.

When the domain is bought:

1. In the DNS provider, point the apex `alittlelight.app` at GitHub Pages with four `A` records (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) and add a `CNAME` record for `www` pointing to `rgafni.github.io`.
2. In the repo's Settings, Pages, enter `alittlelight.app` as the custom domain (GitHub then adds the `CNAME` file) and turn on Enforce HTTPS once the certificate is ready.
3. Update the `og:image` in `index.html` to an absolute URL on the new domain.

## Open items before launch

- The contact address in `index.html` (`#contact-line`) is a placeholder until the domain email exists.
- The download button is a "Coming soon to Google Play" placeholder. Replace it with the Play link when the listing exists.
