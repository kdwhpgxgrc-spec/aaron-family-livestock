# Builder brief — Aaron Family Livestock

> **Design language source:** prairiehillsgelbvieh.com (layout + type system)
> **Brand:** Aaron Family Livestock LLC — EST. 2024
> **Date:** 2026-05-27
>
> Structure, typography rhythm, and spacing extracted from Prairie Hills Gelbvieh.
> **Colors overridden** to AFL Aggie Maroon from the official AFL logo.
> Source copy, photography, and brand marks are NOT reproduced.

---

## What makes this site feel the way it does

Three invisible decisions carry the weight:

**Weight contrast is the hierarchy.** Nav links and CTAs run `font-weight: 700` in Barlow Condensed — bold, uppercase, letter-spaced `0.05em`. Body copy runs `400` in the same face. That gap between 400 and 700 creates strict command vs. explanation. Blur it with a `600` everywhere and the page goes flat.

**Birthstone Bounce script at `font-weight: 500`.** The ornamental script accent runs halfway between regular and medium. Keeps it handwritten-light rather than heavy-ink. Used sparingly — one phrase per section, never as a headline. If your stack only has 400 and 700, use 400.

**Pixel-locked section padding, not percentages.** Vertical rhythm is `125px / 85px / 65px` — locked in pixels so the beat never stretches or compresses with viewport width. Only horizontal column padding (`3%–5%`) uses percentages.

---

## Tokens — AFL brand system

Paste into `:root` exactly as written.

### Palette
| Token | Value | Role |
|---|---|---|
| `--canvas-bg` | `#0A0A0A` | Near-black canvas — logo white bg disappears |
| `--primary` | `#500000` | AFL Aggie Maroon — CTAs, badges, hover states |
| `--primary-dark` | `#380000` | Darker Aggie Maroon — btn hover, pressed state |
| `--primary-light` | `#800000` | Lighter Aggie Maroon — script accent, eyebrow |
| `--white` | `#FFFFFF` | Body text, headlines on dark |
| `--white-muted` | `rgba(255,255,255,0.66)` | Nav links default, lede text |
| `--overlay-dark` | `rgba(0,0,0,0.35)` | Video/photo overlays in hero |

### Typography
| Token | Value |
|---|---|
| `--font-heading` | `'fort-condensed', 'Barlow Condensed', sans-serif` |
| `--font-display` | `'Birthstone Bounce', cursive` |
| `--font-body` | `'fort-condensed', 'Barlow Condensed', sans-serif` |
| `--size-base` | `18px` |
| `--size-hero-script` | `6em` (≈108px) |
| `--size-h1` | `4em` (≈72px) |
| `--size-h2` | `3em` (≈54px) |
| `--size-h3` | `2em` (≈36px) |
| `--weight-body` | `400` |
| `--weight-nav` | `700` |
| `--weight-display` | `500` |
| `--ls-nav` | `0.05em` |
| `--lh-heading` | `1` |
| `--lh-body` | `1.4` |

### Spacing (pixel-locked)
| Token | Value | Use |
|---|---|---|
| `--section-y-lg` | `125px` | Hero + primary sections |
| `--section-y-md` | `85px` | Standard content sections |
| `--section-y-sm` | `65px` | Compact sections |
| `--col-pad-y` | `5%` | Card top/bottom |
| `--col-pad-x` | `3%` | Card left/right |
| `--gap` | `1rem` | Grid gap |

### Components
| Token | Value |
|---|---|
| `--radius-btn` | `0.35em` |
| `--btn-pad-y` | `0.8em` |
| `--btn-pad-x` | `1em` |

---

## Font setup

**Primary (headings + body):** Barlow Condensed — free Google Fonts substitute for Fort Condensed.
**Display (script accent):** Birthstone Bounce — Google Fonts, free.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;700&family=Birthstone+Bounce:wght@400;500&display=swap" rel="stylesheet">
```

**To use exact Fort Condensed** (matches Prairie Hills source):
```html
<!-- Requires Adobe Fonts subscription -->
<link rel="stylesheet" href="https://use.typekit.net/YOUR_KIT_ID.css">
```

---

## Three decisions to never change

1. **Weight contrast: 700 nav/CTA vs 400 body.** Never introduce 500 or 600 in headings — collapses hierarchy.
2. **Script at 500 (or 400 fallback).** Birthstone Bounce 500 for accents only. Not headlines.
3. **Pixel section padding.** `125px`, `85px`, `65px`. Do not convert to `rem` or `%`.

---

## Logo

AFL logo (`afl-logo.png`) uses white background. On dark nav use:
```css
img.nav-logo {
  mix-blend-mode: lighten;
  filter: brightness(1.1);
  height: 44px;
}
```
Drop `afl-logo.png` into the kit folder — wires into nav automatically.

---

## The 7 sections — in this order

### 01 · Nav (sticky, near-black + Aggie Maroon CTA)
- `rgba(0,0,0,0.92)` background, `backdrop-filter: blur(12px)`
- **Left:** AFL logo (img, mix-blend-mode: lighten) — fallback text wordmark
- **Center:** Barlow Condensed 700 uppercase nav links, `--white-muted` → `--white` hover, `--primary` active
- **Right:** Aggie Maroon filled pill CTA (`--primary` bg)
- Height: 64px

### 02 · Hero (full viewport, video loop behind)
- Vimeo muted autoplay loop OR dark Aggie Maroon-tinted gradient fallback
- Overlay: `rgba(0,0,0,0.35)`
- **Top:** Birthstone Bounce `6em` `500` in `--primary-light` — script phrase
- **Headline:** Barlow Condensed `4em` `700` uppercase white — typed animation + Aggie Maroon blinking cursor
- **Lede:** `1.125em` `--white-muted`, max `38ch`
- **CTAs:** Aggie Maroon filled primary + ghost secondary

### 03 · Sires carousel (horizontal scroll-snap)
- Eyebrow: Birthstone Bounce in `--primary-light`
- H2: Barlow Condensed `3em` 700 uppercase white
- Circular nav buttons: Aggie Maroon border, Aggie Maroon → filled on hover
- Cards `380px` wide, scroll-snap-align: start
- Per card: 16:10 cattle photo, Aggie Maroon pill badge, Barlow Condensed title `2em` 700, body text, Aggie Maroon "View Sire →" arrow link

### 04 · Two-column showpiece (sale CTAs)
- Two equal cards, `gap: 16px`, cattle photo or Aggie Maroon gradient bg
- Animated Aggie Maroon radial orb in bg at 0.35 opacity
- Card 1: Annual Bull Sale → "Register to Bid" (DVAuction link)
- Card 2: Private Treaty → "Inquire Now"

### 05 · Ranch updates slider
- Same carousel pattern — `320px` cards
- Cover photo (16:9), date + category pill, headline ≤8 words, "Read →" arrow
- Content: show wins, new arrivals, sale results

### 06 · Dark CTA band (full-width)
- `#0A0A0A` bg + optional cattle photo at `0.4` opacity
- Birthstone Bounce script accent in `--primary-light`
- Barlow Condensed headline `3em` 700 with typed animation + Aggie Maroon cursor
- One Aggie Maroon pill CTA

### 07 · Footer
- 4-col grid: AFL tagline/desc + 3 link columns (Genetics, Operation, Contact)
- Middle: giant AFL wordmark `font-size: clamp(3rem, 10vw, 8rem)`, `line-height: 0.85`, white
- Bottom: small mark + legal links + "Gladewater, TX"
- Column headers: `--primary` uppercase small caps

---

## House rules

- No drop shadows. Dark bg + photo layers create depth.
- Ranch photography only — your cattle, your land. No stock.
- AFL Aggie Maroon is ink — one accent. Never introduce blue, gold, or green.
- All headlines uppercase.
- Body line length ≤ 60ch.
- Sections ≥ 85px vertical padding desktop; primary sections 125px.
- No scroll-jacking. Native scroll only.
- CTAs ≤ 4 words.
- Every section `min-height: 100vh`, content vertically centered. Mobile drops to `min-height: auto`. Footer exempt.
- Exactly 7 sections. No extras.
- **Banned words:** revolutionary, seamless, unleash, empower, transform, game-changing, supercharge, world-class, journey, experience, solutions.

---

## Copy slots — fill before building

```
NAV
  Logo:           afl-logo.png  (fallback: Aaron Family Livestock)
  Links:          Sires, Sales, Program, Gallery, Contact
  CTA:            View Sale

HERO
  Script accent:  Angus · Show Cattle · Gladewater TX
  Headline:       Built for the Show Ring.
  Lede:           Registered Angus genetics bred for the 2028 TX Majors.
  Primary CTA:    View Our Sires
  Secondary CTA:  Our Program

SIRES CAROUSEL
  Eyebrow:        Our Genetics
  Headline:       Proven Sire Lineup
  Card badges:    ANGUS / ET / AI / SHOW / SEEDSTOCK
  Card roles:     [Sire name] — [primary trait, e.g. "Moxy AI Bull"]
  Card body:      [EPD highlight + breeding note, 1-2 sentences]

TWO-COLUMN
  Card 1 badge:   BULL SALE
  Card 1 head:    Annual Bull Sale
  Card 1 lede:    [Date] — Gladewater, TX
  Card 1 CTAs:    Register to Bid  /  View Catalog

  Card 2 badge:   PRIVATE TREATY
  Card 2 head:    Females Available
  Card 2 lede:    Replacement heifers and show prospects year-round.
  Card 2 CTAs:    Inquire Now  /  View Program

RANCH UPDATES
  Headline:       From the Ranch
  Cards (6):      [date · category · title ≤8 words]

DARK CTA
  Script accent:  The Aaron Family
  Headline:       Ready to Raise Your Program?
  CTA:            Get in Touch

FOOTER
  Tagline:        Registered Angus · Gladewater, TX
  Wordmark:       AARON FAMILY LIVESTOCK
  Contact email:  [your email]
  Contact phone:  [your phone]
```

---

## Acceptance criteria

A. All palette tokens in `:root` verbatim — no rounding.
B. Hero headline: Barlow Condensed 700 uppercase `4em`, typed animation with Aggie Maroon cursor.
C. Birthstone Bounce `500` script visible in hero + dark CTA.
D. Video loop (or Aggie Maroon-tint gradient fallback) visible in hero.
E. Sire carousel: scroll-snap, ≥5 cards, Aggie Maroon badges + arrow links.
F. Footer wordmark `≥ 8vw`, `line-height: 0.85`.
G. Mobile: headline scales to `~3em`, columns stack, carousels swipeable.
H. 7 sections in order. No extras.
I. AFL logo renders clean on dark nav via `mix-blend-mode: lighten`.

---

## Files in this kit

| File | What it is |
|---|---|
| `builder-brief.md` | This file — paste into v0 / Lovable / Claude to generate the full site |
| `tokens.json` | All `:root` CSS variables — drop into any stylesheet |
| `scaffold.html` | Working 7-section HTML with `{{slots}}` — fill and deploy |
| `afl-logo.png` | **Drop your logo here** — wires into nav automatically |
| `preview.png` | Prairie Hills reference screenshot — design A/B target |

---

*Design language from prairiehillsgelbvieh.com. AFL Aggie Maroon from official AFL logo EST. 2024. Copy, photography, and brand marks are yours.*
