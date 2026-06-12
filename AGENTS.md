# Aaron Family Livestock Site Memory

## Repository

- GitHub: `kdwhpgxgrc-spec/aaron-family-livestock`
- Production: `https://aaronfamilylivestock.com`
- Deployment: Vercel deploys pushes to `main`.
- This is a static HTML/CSS/JavaScript site. It is not the separate Next.js workspace at `~/Desktop/aaronfamilylivestock-kit`.

## Current Site

- Homepage: `/index.html`
- Shared content-page styles: `/content.css`
- AEO pages:
  - `/angus-genetics/`
  - `/sires/`
  - `/embryo-calves/`
  - `/show-cattle/`
  - `/show-record/`
  - `/about/`
  - `/contact/`
- Operations checklist: `/AEO-RUNBOOK.md`

## Verified Business Facts

- Business: Aaron Family Livestock LLC
- Location: Gladewater, Texas
- Established: 2005
- Focus: Registered Angus genetics and show cattle
- Circle S 5707 x Colburn Primo 5153 embryo calves are due in early 2027.
- Do not invent addresses, hours, awards, reviews, availability, registrations, or other business claims.

## Design Decisions

- Preserve the cinematic homepage hero, video, 3D headline, rounded logo, and deep maroon/black visual identity.
- The award image is a wide banner and must retain its natural aspect ratio.
- The family portrait retains a 3:4 portrait ratio and becomes one column on mobile.
- The AF cattle-brand image appears behind the contact information as a watermark.
  - Desktop opacity: `0.25`
  - Mobile opacity: `0.21`
  - Keep the soft maroon glow without reducing contact readability.
- Explicit image `width` and `height` attributes are used for SEO/layout stability. Corresponding responsive CSS must include `height: auto`.
- Do not reintroduce the removed spinning logo, duplicate white brand, FAQ section, or excessive black spacing.
- Scrolling must work over the hero video in Safari, Chrome, mobile browsers, and the Codex browser.

## SEO and AEO

- Keep one clear H1, unique titles/descriptions, correct canonicals, and factual JSON-LD on every page.
- Maintain `/robots.txt`, `/sitemap.xml`, `/llms.txt`, and `/llms-full.txt`.
- `OAI-SearchBot`, GPTBot, ClaudeBot, PerplexityBot, GoogleOther, and standard crawlers are currently allowed.
- Treat `llms.txt` as optional crawler guidance, not a ranking shortcut.
- Add FAQ schema only when visible, factual questions and answers are present and eligible.
- Update sitemap `lastmod` only when a page materially changes.

## Validation and Publishing

Before pushing:

1. Run `git diff --check`.
2. Run:
   `python3 ~/.codex/skills/seo-site-auditor/scripts/audit_html.py /tmp/aaron-family-livestock`
3. Verify desktop and mobile layouts, image proportions, scrolling, links, and console errors.
4. Confirm new local routes return HTTP 200.
5. Commit and push `main`.
6. Confirm the production URL serves the new change.

## Recent Stable Commits

- `844eb1d` Increase contact brand visibility
- `d6fc14f` Fix homepage image proportions
- `372a7c6` Build AEO content architecture
- `f901490` Optimize homepage SEO and performance
