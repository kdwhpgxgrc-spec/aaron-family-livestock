#!/usr/bin/env python3
"""
AFL Site Builder — feeds kit into Gemini, fills {{slots}}, writes index.html
Usage:  python3 build_site.py
Output: ~/Desktop/aaronfamilylivestock-kit/index.html (completed)
"""

import os
import re
from pathlib import Path
from google import genai
from google.genai import types

KIT_DIR = Path(__file__).parent


# ── Load kit files ────────────────────────────────────────────────────────────

def load_kit():
    brief    = (KIT_DIR / "builder-brief.md").read_text(encoding="utf-8")
    tokens   = (KIT_DIR / "tokens.json").read_text(encoding="utf-8")
    scaffold = (KIT_DIR / "scaffold.html").read_text(encoding="utf-8")
    return brief, tokens, scaffold


# ── Build Gemini prompt ───────────────────────────────────────────────────────

def build_prompt(brief, tokens, scaffold):
    return f"""\
You are an expert web developer completing a real website for Aaron Family Livestock LLC.

OPERATION
- Registered Angus seedstock + show cattle, Gladewater, TX, EST. 2024
- Owner: Bryan Aaron
- Market: Texas FFA students, show cattle buyers, ranchers targeting 2028 TX Majors
- Voice: Authoritative. Direct. Metric-focused. Short CTAs (≤4 words). No fluff.

BANNED WORDS — never use any of these:
revolutionary, seamless, unleash, empower, transform, game-changing, supercharge,
world-class, journey, experience, solutions

────────────────────────────────────────────────────────────────────────────────
DESIGN BRIEF
────────────────────────────────────────────────────────────────────────────────
{brief}

────────────────────────────────────────────────────────────────────────────────
TOKENS (already in scaffold :root — do not change values)
────────────────────────────────────────────────────────────────────────────────
{tokens}

────────────────────────────────────────────────────────────────────────────────
SCAFFOLD HTML — replace every {{{{SLOT}}}} with real AFL copy
────────────────────────────────────────────────────────────────────────────────
{scaffold}

────────────────────────────────────────────────────────────────────────────────
TASK
────────────────────────────────────────────────────────────────────────────────
Return the COMPLETE index.html with every {{{{SLOT}}}} replaced. Follow these rules:

SIRE CARDS (5 cards)
  Use authentic Angus naming style:
    MOXY 601, MOJO 7C, POWER STROKE 2D, CROSSFIRE 47X, GRANITE 9E
  Per card: one-line EPD highlight (BW +1.2  WW +65  YW +105 style).
  Roles: AI Sire, ET Sire, Show Bull, Herd Bull, Prospect

RANCH UPDATE CARDS (6 cards — Section 05)
  Content: show wins, new arrivals, sale announcements — Spring/Fall 2026 dates.
  Headlines ≤8 words. Categories: SHOW WIN · NEW ARRIVAL · SALE RESULTS · PROGRAM UPDATE

TWO-COLUMN (Section 04)
  Card 1 — Bull Sale: Fall 2026 date, Gladewater TX.
  Card 2 — Private Treaty: replacement heifers + show prospects.

CONTACT
  Email: contact@aaronfamilylivestock.com
  Phone: (903) 555-0100  ← placeholder Bryan will replace

STRICT RULES
  1. Keep ALL CSS, JavaScript, and HTML structure from the scaffold exactly as-is.
  2. Do not add new sections, styles, or scripts.
  3. Output ONLY the raw HTML — no markdown fences, no commentary, no explanation.
  4. First character of output must be < (start of DOCTYPE or html tag).
"""


# ── Extract HTML from response ────────────────────────────────────────────────

def extract_html(text: str) -> str:
    # Strip markdown fences if model ignored instructions
    m = re.search(r'```(?:html)?\s*(<!DOCTYPE.*?|<html.*?)</html>', text, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(0).lstrip('`').strip().lstrip('html').strip()

    # Find first < character
    start = text.find('<!DOCTYPE')
    if start == -1:
        start = text.find('<html')
    if start != -1:
        end = text.rfind('</html>') + len('</html>')
        return text[start:end]

    return text.strip()


# ── Main ──────────────────────────────────────────────────────────────────────

def get_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY", "")
    if key:
        return key
    # Fall back to ag-coach-app .env
    env = Path("/Volumes/Samsung PSSD T7/ag-coach-app/.env")
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("GEMINI_API_KEY=") and not line.startswith("#"):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("GEMINI_API_KEY not found in environment or .env")


def main():
    api_key = get_api_key()
    client  = genai.Client(api_key=api_key)

    brief, tokens, scaffold = load_kit()
    prompt = build_prompt(brief, tokens, scaffold)

    slots_found = re.findall(r'\{\{[A-Z_0-9]+\}\}', scaffold)
    print(f"Scaffold: {len(scaffold):,} chars  |  {len(set(slots_found))} unique slots to fill")
    print("Sending to Gemini (HIGH thinking)…\n")

    chunks = []

    for chunk in client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        contents=[
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            )
        ],
        config=types.GenerateContentConfig(
            temperature=0.9,
            thinking_config=types.ThinkingConfig(thinking_level="HIGH"),
        ),
    ):
        if text := chunk.text:
            print(text, end="", flush=True)
            chunks.append(text)

    print("\n\n── Extracting HTML ──")
    raw  = "".join(chunks)
    html = extract_html(raw)

    # Verify slots are gone
    remaining = re.findall(r'\{\{[A-Z_0-9]+\}\}', html)
    if remaining:
        print(f"⚠  Unfilled slots: {set(remaining)}")
    else:
        print("✓  All slots filled")

    out = KIT_DIR / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"✓  Written → {out}  ({len(html):,} chars)")
    print("   Preview: http://localhost:5555")


if __name__ == "__main__":
    main()
