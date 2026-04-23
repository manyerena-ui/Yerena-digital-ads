---
name: local-service-ad-generator
description: Generate production-ready static ad images for local service businesses using Claude + Nano Banana 2. End-to-end workflow from brand research → prompt generation → image generation via FAL API. No product photos required — uses service result imagery, owner photos, reviews, and trust assets instead. Trigger on requests to create static ads for local businesses, service companies, contractors, salons, restaurants, or any non-DTC brand. Also trigger when user drops a business name + URL and asks for ad creatives.
---

# Local Service Business Ad Generator
## Claude Code + Nano Banana 2 | Built for Yerena Digital

Generate 20–40 production-ready static ad images for any local service business — from brand research to finished creatives — entirely inside Claude Code. No product photos required.

---

## Overview

Local service ads are built on trust, proximity, and urgency — not product packaging. This pipeline is adapted from the DTC static ad workflow with three key differences:

1. **Brand DNA pulls different signals** — Google reviews, service area, trust markers, owner story, and social proof instead of packaging and typography
2. **Template library is built for local formats** — review cards, before/afters, owner-face trust ads, offer promos, local proof ads, stat callouts
3. **Reference images are service assets** — before/after photos, team photos, job site shots, or review screenshots instead of product packaging

### The Four Phases
0. **Winning Ad Research** (optional) → Claude scrapes Meta Ad Library + ad analysis sources for the top performers in the client's niche, reverse-engineers winning ad creatives into prompt templates. Uses niche-specific template libraries when available (see `skills/references/niche-templates/`).
1. **Brand Research** → Claude builds a Local Business DNA document via web search + site scrape
2. **Prompt Generation** → Claude fills template prompts with business-specific details. Uses niche templates from Phase 0 when available, otherwise falls back to the generic 20 templates.
3. **Image Generation** → Python script fires prompts to Nano Banana 2 via FAL API

---

## Prerequisites

- **FAL API key** set as environment variable: `export FAL_KEY="your-key-here"`
- **Python packages**: `requests`
- **Service asset images** dropped in the brand folder before running (see Asset Types below)

---

## Asset Types (Replaces Product Photos)

Unlike DTC brands, local service businesses don't have product packaging. Instead, collect:

| Asset Type | Use | Priority |
|---|---|---|
| Owner/team headshots | Owner-face trust ads, guarantee ads | HIGH |
| Before/after pairs | Split-screen service result ads | HIGH |
| Finished work photos | Lifestyle/result ads | HIGH |
| Google review screenshots | Review card ads | HIGH |
| Business exterior/interior | Location trust ads | MEDIUM |
| Team-in-action shots | Credibility/process ads | MEDIUM |
| Award/certification badges | Trust stack ads | LOW |

**1–3 images per asset type is enough.** Nano Banana 2 uses these as visual reference to match the real business aesthetic in generated ads.

---

## Phase 0: Winning Ad Research (Niche Template Discovery)

Before running the standard template library, check if a **niche-specific template library** exists or needs to be created. This phase reverse-engineers winning ads from top performers in the client's exact niche.

### When to Run Phase 0
- **Always** for a new niche/category we haven't served before
- **Skip** if `skills/references/niche-templates/{niche}.md` already exists for this category

### Available Niche Template Libraries
Check `skills/references/niche-templates/` for existing libraries:
- `meal-prep-delivery.md` — 12 templates reverse-engineered from Factor, HelloFresh, Trifecta, CookUnity, EveryPlate, Daily Harvest, Misfits Market, Huel

### How to Build a New Niche Library

**Step 1: Identify Top 8-10 Performers in the Niche**
Search for the biggest spenders and most recognized brands:
- Web search: "best [NICHE] Facebook ads", "top [NICHE] companies advertising", "[NICHE] ad examples"
- Look for: national brands, strong regional players, DTC disruptors
- Prioritize companies known for heavy paid social spend

**Step 2: Scrape Meta Ad Library for Winning Ads**
For each top performer, search the Meta Ad Library:
```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[COMPANY NAME]&search_type=keyword_unbranded
```
- Filter: Active ads only
- Key signal: **Longest-running ads are proven winners** — if someone pays to keep an ad live for 3-6+ months, it's profitable
- Extract: Ad copy, creative description, format, platforms, start date

**Step 3: Supplement with Ad Breakdown Articles**
Search for existing analyses of winning ads in the niche:
- "[NICHE] Facebook ad examples"
- "[NICHE] ad creative breakdown"
- "[NICHE] best performing ads"
These articles often include screenshots, copy, and analysis of what makes each ad work.

**Step 4: Reverse-Engineer into Prompt Templates**
For each winning ad pattern identified, create a Nano Banana 2 prompt template:
1. Describe the **visual layout** (split, full-bleed, grid, text-forward, comparison, etc.)
2. Describe the **photography style** (overhead, lifestyle, close-up, studio, etc.)
3. Include `[BRACKETED PLACEHOLDERS]` for all business-specific details
4. Tag the **source pattern** (which company/ad this is modeled after)
5. Note the **aspect ratio** and whether it **needs reference images**
6. Include a **"Why It Works"** note explaining the conversion psychology

**Step 5: Save as Niche Template Library**
Save to: `skills/references/niche-templates/{niche-slug}.md`

Format should match the existing `meal-prep-delivery.md` structure:
- Template number (N01, N02, etc.)
- Source pattern attribution
- Format description
- Aspect ratio and reference image needs
- Full prompt with placeholders
- Priority table by sub-niche

### Using Niche Templates in Phase 2

When a niche template library exists:
1. Run **all niche templates** (N01-N12 for meal prep = 12 templates)
2. Add the **5 best generic templates** that still apply (usually #07 Problem/Solution, #09 Multi-Review, #10 Us vs Them, #18 FAQ Buster, #20 Risk Reversal)
3. Total: 15-17 templates instead of the generic 20
4. Fill all `[PLACEHOLDERS]` using the Brand DNA document (same as standard Phase 2)

---

## Folder Structure

```
~/brands/{business-name}/
├── assets/
│   ├── logo/                    # Scraped logo files (PNG/SVG preferred)
│   ├── scraped/                 # All other images scraped from website
│   ├── owner/                   # Owner + team headshots
│   ├── before-after/            # Before/after pairs
│   ├── finished-work/           # Completed job photos
│   ├── team/                    # Crew/team photos
│   ├── review-screenshot/       # Google review screenshots
│   └── social/                  # Manual Instagram screenshots (client-provided)
├── brand-dna.md                 # Generated by Phase 1
├── prompts.json                 # Generated by Phase 2
├── generate_ads.py              # Copied from skills/references/ before Phase 3
└── outputs/
    ├── 01-google-review-card/
    ├── 02-before-after-split/
    ├── 03-owner-guarantee/
    └── ...
```

---

## Phase 1: Local Business Brand Research & DNA Generation

When the user provides a business name and URL, execute the Brand Research prompt below. Use web search and web fetch extensively. This phase takes 5–10 minutes.

### Brand Research System Prompt

**Role**: Act as a Senior Direct Response Creative Strategist specializing in local service business advertising. Conduct a full reverse-engineering of the target business's identity, trust signals, and competitive positioning.

**Objective**: Create a Local Business DNA document that will be used to write highly specific AI image generation prompts. Every detail matters — the output feeds directly into an image model that needs exact specifications to produce on-brand, trust-building ads for local audiences.

**RESEARCH STEPS**:

**1. DEEP WEBSITE SCRAPE** (fetch and analyze every relevant page of the business URL):

Start here — the website is the richest single source of truth. Don't just fetch the homepage. Crawl all reachable pages:
- Homepage: Hero headline, subhead, primary CTA, value proposition
- About/Our Story page: Owner name, founding year, background, mission, family-owned status
- Services page(s): Every service listed, descriptions, pricing if shown, any guarantees per service
- Contact/Service Area page: Cities, zip codes, regions served — extract every location mentioned
- Testimonials/Reviews page: Pull every review or testimonial shown on-site, exact wording
- Gallery/Portfolio/Before-After page: Note what types of finished work photos exist
- Blog or FAQ page (if present): Pull customer questions — these are the real objections and pain points
- Footer: Business address, phone, license numbers, certifications, trust badges

**Extract and document:**
- Every trust signal mentioned anywhere on the site (licensed, insured, bonded, certified, guaranteed, background-checked, BBB, etc.)
- Every differentiator claim ("no hidden fees," "same-day service," "family owned," "satisfaction guarantee")
- All CTAs used and their exact wording — these reveal how they sell
- Visual identity: primary colors (describe precisely or find hex), font style (serif/sans/script/slab), logo description, overall layout density
- Photography style: clinical or warm? polished studio shots or real candid photos? do they show team, before/afters, job sites?
- Tone: describe in 5 adjectives based on the copy voice

**2. GOOGLE & REVIEW RESEARCH** (use web search for each):
- Reviews: Search "[Business Name] Google reviews", "[Business Name] Yelp reviews" — extract 5–10 of the most specific, emotional, results-focused reviews with exact customer language. Do not paraphrase — pull word-for-word.
- Reputation: Search "[Business Name] [City]" — confirm star rating, total review count, common praise themes
- Press/awards: Search "[Business Name] award", "[Business Name] best [service] [city]", "[Business Name] featured in"
- Owner story: Search "[Business Name] owner story", "[Business Name] founder", "[Business Name] about us" — cross-reference with website About page

**3. META AD LIBRARY** (fetch directly — public, no login required):
- Fetch: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[BUSINESS NAME]&search_type=keyword_unbranded`
- Also try: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[BUSINESS NAME]`
- Extract: Are they running ads? What formats (image, video, carousel)? What offers or hooks are they leading with? What CTAs? How long have ads been running (longer = working)?
- If no ads found: note this — it means either they're not doing paid social yet (opportunity) or the name search didn't match

> **Note on Instagram**: Instagram requires login and blocks scraping. Skip it. Instead, ask the client to manually screenshot 3–5 of their best-performing posts and drop them in `assets/social/` before Phase 3. The client knows which posts performed — better signal than anything scrapable.

**4. COMPETITIVE CONTEXT**:
- Search for 2–3 direct local competitors in the same city/service area
- Fetch each competitor's homepage — extract their primary headline, offer, and CTA
- Note how the target business differentiates: where competitors are clinical/corporate, is the target warm/personal? Where competitors are vague, is the target specific?
- Check Meta Ad Library for competitor ads: `https://www.facebook.com/ads/library/?q=[COMPETITOR NAME]`
- Identify the biggest visual and verbal gap the target business can own

**5. IMAGE & LOGO SCRAPING** (download directly — do this during the website crawl):

While fetching each page, extract and download all image assets to the brand folder:

**Logo** → save to `assets/logo/`:
- Look for `<img>` tags with "logo" in the src, alt, or class attribute
- Check `<link rel="icon">` and `<link rel="apple-touch-icon">` for favicon/logo variants
- Check for SVG logos inline or linked — SVG is preferred over PNG
- Try common paths: `/logo.png`, `/logo.svg`, `/images/logo.png`, `/assets/logo.png`
- If the site uses a CSS background-image for the logo, note the URL and download it
- Save the highest-resolution version found. Rename to `logo.png` or `logo.svg`

**All other site images** → save to `assets/scraped/`:
- Download every `<img>` src found across all pages (skip icons < 100px, skip generic stock photos if identifiable)
- Prioritize: hero images, gallery/portfolio photos, team/staff photos, before/after photos, owner photos, job site shots
- Skip: UI icons, button graphics, social media share icons, generic stock imagery
- Rename files descriptively as you save: `hero-homepage.jpg`, `team-photo-1.jpg`, `before-kitchen.jpg`, `after-kitchen.jpg`, etc.
- After downloading, sort into the correct subfolders (`owner/`, `before-after/`, `finished-work/`, `team/`) based on visual content

**Scraping instructions**:
- Use `requests` or web fetch to download each image URL directly
- Resolve relative URLs against the base domain before fetching
- Skip images that return 403/404
- Log every downloaded file path in the brand-dna.md under ASSET INVENTORY

**6. AD ASSET INVENTORY**:
- List every file downloaded in step 5, sorted by subfolder
- Flag the top 3 asset types most critical for their service category
- Note any gaps — asset types not found on the site that the client will need to provide manually before Phase 3

**OUTPUT FORMAT**:

```
LOCAL BUSINESS DNA DOCUMENT
============================

BUSINESS OVERVIEW
Business Name / Service Category / Location / Years in Business / Owner Name (if known) / Tone Adjectives [5] / Unique Positioning / Competitive Differentiation

TRUST & SOCIAL PROOF
Star Rating / Total Reviews / Review Platform / Top 5 Customer Phrases (exact language) / Awards or Press Mentions / Certifications or Licenses / Guarantees Offered

VISUAL IDENTITY
Primary Color [hex or precise description] / Secondary Color / Font Style / Logo Description / Photography Style

SERVICE DETAILS
Primary Services / Pricing (if shown) / Service Area / Before/After Potential (high/medium/low)

LOCAL TRUST SIGNALS
Years in business / Family-owned (Y/N) / Local vs. franchise / Specific neighborhood mentions / Community involvement

CURRENT AD ACTIVITY
Running paid ads (Y/N) / Ad formats observed / Hooks and offers being tested / Competitor ad activity

AD CREATIVE DIRECTION
Best-performing ad formats for this category / Recommended asset types to use as image reference / Key offer structure / Urgency angles / Seasonal opportunities

SCRAPED ASSETS
Logo: [filename + format] / Logo source URL
Scraped images: [list each file with descriptive name and which subfolder it was sorted into]
Total downloaded: [count]

ASSET INVENTORY
Auto-scraped: [list subfolders populated] / Needed from client: [list gaps — asset types not found on site]

IMAGE GENERATION PROMPT MODIFIER
[50–75 word paragraph to prepend to every image prompt — include exact colors, font style, photography mood, and emotional tone for local audience trust]
```

Save output as: `brands/{business-name}/brand-dna.md`

---

## Phase 2: Prompt Generation

After Brand DNA is complete, generate business-specific prompts from the 20 templates.

### Prompt Generation Instructions

Read `skills/references/template-prompts.md` and fill in all 20 templates with specific details for [BUSINESS NAME] based on the Brand DNA document — especially the Image Generation Prompt Modifier, the Trust & Social Proof section, and the top customer review phrases.

**For each template**:
1. Replace all [BRACKETED PLACEHOLDERS] with business-specific details from the Brand DNA
2. Prepend the Image Generation Prompt Modifier
3. Use exact customer language from the Top 5 Customer Phrases wherever copy appears
4. Set the correct `aspect_ratio` (1:1, 4:5, or 9:16 per template spec)
5. Set `needs_reference_images: true/false`
   - Templates showing owner, team, before/after, or finished work = `true`
   - Templates that are graphic/typographic with no real people or work = `false`
6. Set `reference_asset_type`: `owner`, `before_after`, `finished_work`, `team`, `review_screenshot`, or `none`

**Output as JSON** — save to `brands/{business-name}/prompts.json`:
```json
{
  "business": "Business Name",
  "category": "Service Category",
  "location": "City, State",
  "generated_at": "ISO timestamp",
  "prompts": [
    {
      "template_number": 1,
      "template_name": "google-review-card",
      "prompt": "Full completed prompt text...",
      "aspect_ratio": "4:5",
      "needs_reference_images": true,
      "reference_asset_type": "finished_work",
      "copy": {
        "headline": "Exact headline text",
        "subhead": "Subhead or review text",
        "cta": "Call to action"
      },
      "notes": "Generation notes or copy refinement suggestions"
    }
  ]
}
```

---

## Phase 3: Image Generation via FAL API

Copy `skills/references/generate_ads.py` into the brand folder, then run it.

```bash
cp skills/references/generate_ads.py brands/{business-name}/generate_ads.py
cd brands/{business-name}

# Full run — all 20 templates
python generate_ads.py

# Selective run — specific templates
python generate_ads.py --templates 1,3,7,12

# Test run — cheap, fast validation
python generate_ads.py --templates 1,2,3 --resolution 1K
```

### FAL API Details

**Text-to-Image**: `fal-ai/nano-banana-2`
- Input: `prompt`, `aspect_ratio`, `num_images`, `output_format`, `resolution`

**Edit/Image-Reference**: `fal-ai/nano-banana-2/edit`
- Input: same + `image_urls` (array, up to 14 reference images)
- Product images must be uploaded to FAL storage first

---

## User Interaction Flows

**"Generate ads for [business]"** → Ask for name, URL, city. Run Phase 1 → 2 → 3.
**"Just run templates 1, 3, 7"** → Confirm prompts.json exists. Run Phase 3 with --templates filter.
**"New client, same templates"** → New brand folder. Run Phase 1 → 2 → 3.
**"Re-run with new offer"** → Skip Phase 1. Re-run Phase 2 with updated offer. Run Phase 3.

---

## Key Technical Notes

- Reference images dramatically improve trust ad quality — owner headshots and before/after photos make the model match real identity instead of stock aesthetics
- `/edit` endpoint for identity-specific ads; standard text-to-image for graphic/typographic ads
- Aspect ratios: `1:1` feed, `4:5` feed portrait, `9:16` Stories/Reels
- Default resolution: `2K`. Use `1K` for test runs, `4K` for hero assets
- Full 20-template run = 80 images at ~$9.60 (2K). Test run of 5 = ~$2.40

---

## Yerena Digital Delivery Notes

- Present `index.html` gallery as the client deliverable
- Flag top 3–5 recommended ads to test first: review card, owner trust, best before/after
- Provide `prompts.json` for client copy review and refinement
- Offer round 2 after client feedback: updated copy, swapped assets, new template variations
- Positions naturally as a Content Machine deliverable or standalone "Ad Creative Sprint"
