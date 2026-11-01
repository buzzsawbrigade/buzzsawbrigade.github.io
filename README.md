# Buzzsaw Brigade website

The public site for the Buzzsaw Brigade Android game. Google Play needs these pages.

Live at https://buzzsawbrigade.github.io/

| Page | File | Use it for |
| --- | --- | --- |
| Home | index.html | Play Console "Website" field |
| Privacy Policy | privacy.html | Play Console privacy policy URL, and the PRIVACY POLICY button in the game |
| Delete your data | delete-data.html | Data safety form, data deletion URL |
| Support | support.html | Support link, SUPPORT AND CONTACT button in the game |
| Summon odds | odds.html | Loot box odds disclosure |
| Terms of Use | terms.html | TERMS OF USE button in the game |

## Editing

Page text lives in `pages/`. Shared header, footer, contact email and the "last updated" date are in `build.py`.

```
python3 build.py
```

Then commit and push. GitHub Pages republishes in about a minute.

## Copy rules

Plain English. No dashes as punctuation, no emoji, no marketing language, and no names from other games.

## Own domain (Squarespace)

To use a domain bought on Squarespace, add a `CNAME` file here with the domain (for example `buzzsawbrigade.com`), then in Squarespace Domains add these DNS records:

- `A` records for `@`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- `CNAME` record for `www`: `buzzsawbrigade.github.io`

Then in this repo's Settings, Pages, enter the domain and tick Enforce HTTPS. Update `SITE_URL` in `build.py` and `SITE_BASE` in the game's `src/game/siteLinks.ts`.
