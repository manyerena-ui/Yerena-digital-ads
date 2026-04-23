# Yerena Digital — Local Service Ad Generator
## Claude Code + Nano Banana 2 via FAL API

Generate 20–40 production-ready static ads for any local service business client in minutes.

### Setup

1. Set your FAL API key:
   ```bash
   export FAL_KEY="your-key-here"
   ```

2. Install Python dependency:
   ```bash
   pip install requests
   ```

### Running for a New Client

Tell Claude Code:
> "Read skills/SKILL.md and generate ads for [Business Name] at [URL]"

Claude will:
1. Scrape the business website across all pages
2. Pull Google/Yelp reviews and Meta Ad Library
3. Build a Brand DNA document → `brands/{business-name}/brand-dna.md`
4. Fill all 20 ad templates → `brands/{business-name}/prompts.json`
5. Run the image generation script → `brands/{business-name}/outputs/`
6. Open `brands/{business-name}/index.html` to view the gallery

### Selective Runs

```bash
# Test run — 3 templates, cheap and fast (1K resolution)
python generate_ads.py --templates 1,2,3 --resolution 1K

# Production run — all 20 templates
python generate_ads.py

# Specific templates only
python generate_ads.py --templates 1,3,7,12
```

### Folder Structure

```
yerena-digital-ads/
├── skills/
│   ├── SKILL.md                        # Skill definition — invoke this to start
│   └── references/
│       ├── template-prompts.md         # 20 ad template prompts
│       └── generate_ads.py             # FAL API image generation script
├── brands/
│   └── {business-name}/
│       ├── assets/
│       │   ├── owner/
│       │   ├── before-after/
│       │   ├── finished-work/
│       │   ├── team/
│       │   ├── review-screenshot/
│       │   └── social/
│       ├── brand-dna.md                # Phase 1 output
│       ├── prompts.json                # Phase 2 output
│       ├── generate_ads.py             # Copied from skills/references/
│       ├── index.html                  # Client gallery deliverable
│       └── outputs/
│           ├── 01-google-review-card/
│           ├── 02-before-after-split/
│           └── ...
└── README.md
```

### Cost Reference

| Resolution | Cost/Image | Full Run (80 images) | Test Run (12 images) |
|---|---|---|---|
| 1K | ~$0.08 | ~$6.40 | ~$0.96 |
| 2K | ~$0.12 | ~$9.60 | ~$1.44 |
| 4K | ~$0.16 | ~$12.80 | ~$1.92 |

### Before Running Phase 3 — Asset Checklist

Confirm the client has provided (drop in `brands/{client}/assets/`):
- [ ] Owner headshot (Templates 03, 12, 20)
- [ ] Before/after pair (Template 02)
- [ ] 2–3 finished work photos (Templates 14, 15, 17)
- [ ] Team photo (Template 08)
- [ ] Top 5 real Google reviews (exact text)
- [ ] Google Business profile screenshot (rating + review count)
