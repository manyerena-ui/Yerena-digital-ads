# Local Service Business — Static Ad Template Library
## For use with Yerena Digital Ad Generator | Nano Banana 2 via FAL API

Each template is a Nano Banana 2 image generation prompt with [BRACKETED PLACEHOLDERS] to be filled in during Phase 2 using the Local Business DNA document.

**Aspect ratio key**: 1:1 = feed square, 4:5 = feed portrait, 9:16 = Stories/Reels
**Reference images**: `needs_reference_images` indicates whether to use the FAL `/edit` endpoint

---

## TEMPLATE 01 — Google Review Card
**Format**: 5-star review displayed over a softly blurred background of finished work
**Best for**: Any service business with strong Google reviews
**Aspect ratio**: 4:5
**Reference images**: finished_work

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Clean, high-trust static ad in the style of a premium Google review card. Background: softly blurred photo of [FINISHED WORK DESCRIPTION — e.g., "a freshly cut fade haircut", "a spotless kitchen after deep cleaning", "a newly landscaped backyard"] with a warm, slightly darkened overlay. Centered card element with white rounded rectangle, subtle drop shadow. Large gold five-star rating (★★★★★) at top. Bold sans-serif headline: "[TOP CUSTOMER REVIEW PHRASE — exact words, 10–20 words max]". Attribution line below in lighter weight: "— [FIRST NAME], [CITY] [PLATFORM] Review". Business name/logo lockup bottom center. Primary brand color [HEX] used as accent stripe at bottom. Aspect ratio 4:5. Ultra-realistic photography style, professional ad composition.
```

---

## TEMPLATE 02 — Before / After Split
**Format**: Side-by-side split screen showing transformation
**Best for**: Landscaping, cleaning, remodeling, auto detail, hair/beauty, restoration
**Aspect ratio**: 1:1
**Reference images**: before_after

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

High-impact before/after split ad. Exact vertical 50/50 split. LEFT SIDE: labeled "BEFORE" in white bold uppercase with subtle dark overlay — shows [BEFORE CONDITION DESCRIPTION]. RIGHT SIDE: labeled "AFTER" in [PRIMARY BRAND COLOR] bold uppercase — shows [AFTER RESULT DESCRIPTION]. Thin white dividing line with small circular badge at center reading "[BUSINESS NAME]". Bottom strip in [PRIMARY BRAND COLOR]: white text "[SERVICE NAME] | [CITY] | [PHONE OR URL]". Clean, professional, results-focused composition. Aspect ratio 1:1.
```

---

## TEMPLATE 03 — Owner Face + Guarantee
**Format**: Owner headshot with bold guarantee statement
**Best for**: Any service business where trust is the primary sales barrier
**Aspect ratio**: 4:5
**Reference images**: owner

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Premium trust-building static ad featuring a real business owner. Background: clean [BRAND SECONDARY COLOR OR NEUTRAL] with subtle texture. Left side: professional photo of [OWNER DESCRIPTION]. Right side: bold typographic treatment. Large display font headline: "[GUARANTEE STATEMENT — e.g., 'If You're Not 100% Happy, You Don't Pay. Period.']". Subhead in lighter weight: "[SUPPORTING LINE]". Owner signature or first name below. Business name and phone/URL at bottom in [PRIMARY BRAND COLOR]. Clean, direct-response ad aesthetic. No stock photo feel — real and personal. Aspect ratio 4:5.
```

---

## TEMPLATE 04 — Limited-Time Offer / Urgency Promo
**Format**: Bold offer callout with urgency and clear CTA
**Best for**: Seasonal promos, new customer offers, capacity-limited services
**Aspect ratio**: 1:1
**Reference images**: none

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

High-urgency direct response static ad. Bold graphic layout. Background: [PRIMARY BRAND COLOR] with subtle diagonal stripe texture. Large starburst or badge shape in contrasting [ACCENT COLOR] at top: "[OFFER HOOK — e.g., 'JUNE SPECIAL', 'NEW CUSTOMER OFFER', 'LIMITED SPOTS']". Main headline in white, heavy weight display font: "[OFFER HEADLINE]". Subhead: "[OFFER DETAILS]". Urgency line: "[SCARCITY ELEMENT — e.g., 'Only 8 spots left in June']". CTA button at bottom: "[CTA TEXT]" in white on dark background. Business logo top corner. Aspect ratio 1:1.
```

---

## TEMPLATE 05 — Stat / Social Proof Callout
**Format**: Large number with supporting context and business branding
**Best for**: Businesses with strong review counts, years in business, or impressive output stats
**Aspect ratio**: 4:5
**Reference images**: none

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Clean, editorial-style static ad built around a single impressive statistic. Minimalist layout with generous white space. Background: [BRAND BACKGROUND COLOR]. Center-aligned composition. Enormous display number in [PRIMARY BRAND COLOR]: "[IMPRESSIVE STAT — e.g., '847', '12 Years', '4.9★']". Label below the stat: "[STAT CONTEXT — e.g., '5-Star Google Reviews']". Thin horizontal rule divider. Supporting line: "[CREDIBILITY LINE]". Business name and logo bottom center. Ultra-clean, confidence-building design. Aspect ratio 4:5.
```

---

## TEMPLATE 06 — Local Proof / Service Area
**Format**: Text-based ad emphasizing community roots and local service area
**Best for**: Businesses competing against national chains or regional franchises
**Aspect ratio**: 1:1
**Reference images**: none

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Warm, community-rooted static ad emphasizing local presence. Background: subtle topographic or abstract geographic texture in [LIGHT BRAND COLOR]. Text-forward layout. Top line in medium caps: "PROUDLY SERVING". Large bold display headline listing cities: "[CITY 1] · [CITY 2] · [CITY 3]". Body copy: "[LOCAL ROOTS LINE — e.g., 'Family-owned and operated in [City] since [YEAR]. Not a franchise. Not a call center. Just [OWNER FIRST NAME] and the crew, showing up on time and doing the job right.']". Bottom strip: business name, phone, URL in [PRIMARY BRAND COLOR]. Aspect ratio 1:1.
```

---

## TEMPLATE 07 — Problem / Solution
**Format**: Two-part ad identifying pain point then presenting the solution
**Best for**: Services that solve an obvious problem (HVAC, pest, plumbing, cleaning, etc.)
**Aspect ratio**: 4:5
**Reference images**: finished_work (optional)

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Direct response two-part static ad. Top half (60%): dark overlay with bold empathy-first headline in white: "[PROBLEM STATEMENT — e.g., 'Tired of your AC going out every August?']". Smaller italic subhead: "[DEEPENING LINE — e.g., 'You shouldn't have to deal with that.']". Horizontal brand-color divider. Bottom half (40%): [PRIMARY BRAND COLOR] background with solution: "[SOLUTION INTRO]" and "[SERVICE PROOF]". CTA: "[CALL TO ACTION]". Business logo bottom right. Aspect ratio 4:5.
```

---

## TEMPLATE 08 — Team / Crew Credibility
**Format**: Team photo with business credentials overlaid
**Best for**: Services where the crew showing up matters (landscaping, construction, cleaning, HVAC)
**Aspect ratio**: 1:1
**Reference images**: team

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Professional team credibility ad. Background: high-quality photo of [TEAM DESCRIPTION — e.g., "a uniformed 3-person landscaping crew standing in front of a branded truck"]. Dark-to-transparent gradient overlay from bottom 40%. Bottom text: Large white bold headline: "[CREDIBILITY HEADLINE — e.g., 'Licensed, Insured, and On Time.']". Subline: "[CREDENTIAL CALLOUT]". Credential badge strip: small icons for key trust signals (insurance, license, years in business, Google rating). Business logo and URL. Aspect ratio 1:1.
```

---

## TEMPLATE 09 — Multi-Review Stack
**Format**: Three short reviews stacked vertically with star ratings
**Best for**: Any business with 10+ strong Google reviews
**Aspect ratio**: 9:16
**Reference images**: none

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Multi-review social proof ad in portrait/story format. Background: soft [BRAND COLOR] gradient. Semi-transparent white card layered over background. Top: business name and "What Our Customers Say" header in [PRIMARY BRAND COLOR]. Three stacked review blocks, each with: ★★★★★ gold stars, review text in italics ("[REVIEW 1 — 15 words max exact language]", "[REVIEW 2]", "[REVIEW 3]"), reviewer first name + city in small caps. Divider lines between reviews. Bottom: "[X]+ Google Reviews | [X.X]★ Average". CTA strip: "[PHONE OR URL]". Aspect ratio 9:16.
```

---

## TEMPLATE 10 — Us vs. Them Comparison
**Format**: Checklist comparison table showing advantages over generic competitors
**Best for**: Markets with low-quality or impersonal competition (franchises, Craigslist operators)
**Aspect ratio**: 4:5
**Reference images**: none

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Bold us-vs-them comparison ad. Clean two-column table layout. Left column header: "[COMPETITOR TYPE — e.g., 'The Other Guys']" in faded/gray tone. Right column header: "[BUSINESS NAME]" in [PRIMARY BRAND COLOR], bold. Six comparison rows:
Row 1: "Local & Family Owned" — ✗ vs ✓
Row 2: "[DIFFERENTIATOR 2]" — ✗ vs ✓
Row 3: "[DIFFERENTIATOR 3]" — ✗ vs ✓
Row 4: "[DIFFERENTIATOR 4]" — ✗ vs ✓
Row 5: "[DIFFERENTIATOR 5]" — ✗ vs ✓
Row 6: "[DIFFERENTIATOR 6]" — ✗ vs ✓
Bottom CTA: "[CALL TO ACTION]". Bold ✗ in red/gray, bold ✓ in [BRAND COLOR]. Aspect ratio 4:5.
```

---

## TEMPLATE 11 — Urgency / Seasonal Hook
**Format**: Seasonal or timely hook with service relevance and CTA
**Best for**: HVAC (summer/winter), landscaping (spring/fall), holiday cleaning, etc.
**Aspect ratio**: 1:1
**Reference images**: finished_work (optional)

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Seasonally relevant static ad with strong urgency. Background: [SEASONAL VISUAL] with [PRIMARY BRAND COLOR] tinted overlay. Top badge/ribbon: "[SEASON/TIMING — e.g., 'SUMMER 2025', 'SPRING CLEAN-UP']" in white on [PRIMARY BRAND COLOR]. Main headline: "[SEASONAL PROBLEM/HOOK]". Supporting copy: "[SERVICE + OFFER]". Urgency line: "[SCARCITY — e.g., 'Booking June now — only 11 slots left']". CTA button: "[CALL/BOOK CTA]". Aspect ratio 1:1.
```

---

## TEMPLATE 12 — Free Quote / Low-Friction Offer
**Format**: Soft CTA focused on reducing commitment barrier
**Best for**: High-consideration services (remodeling, HVAC, landscaping, roofing)
**Aspect ratio**: 4:5
**Reference images**: owner or finished_work

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Low-pressure, high-trust static ad focused on reducing friction. Background: warm [LIFESTYLE OR FINISHED WORK PHOTO] with soft overlay. Top left: business logo. Center: conversational headline: "[LOW-PRESSURE HEADLINE — e.g., 'No Pressure. No Obligation. Just a Free Quote.']". Subhead: "[REASSURANCE LINE]". Trust signal row: ✓ Licensed & Insured ✓ [X]★ on Google ✓ [X] Years Local ✓ Satisfaction Guaranteed. CTA: "[FREE QUOTE CTA]". Honest, approachable, zero-pressure aesthetic. Aspect ratio 4:5.
```

---

## TEMPLATE 13 — Service Menu / What We Do
**Format**: Clean service list with visual hierarchy
**Best for**: Multi-service businesses where people don't know the full offering
**Aspect ratio**: 4:5
**Reference images**: none

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Clean, menu-style service list ad. Background: [BRAND BACKGROUND — white or light neutral]. Top: "[BUSINESS NAME]" in large brand font, followed by "[TAGLINE OR DESCRIPTOR]". Horizontal [PRIMARY BRAND COLOR] divider. Service list: 4–6 services each with a small [BRAND COLOR] icon or bullet:
• [SERVICE 1] [PRICE IF SHOWN]
• [SERVICE 2] [PRICE IF SHOWN]
• [SERVICE 3]
• [SERVICE 4]
• [SERVICE 5]
• [SERVICE 6]
Small print: "[SERVICE AREA]". Bottom CTA: "[CALL TO ACTION]". Clean, informational, well-organized. Aspect ratio 4:5.
```

---

## TEMPLATE 14 — Finished Work Showcase
**Format**: Full-bleed hero photo of a completed job with minimal text overlay
**Best for**: Visually impactful services — landscaping, remodeling, detailing, cleaning, painting, haircuts
**Aspect ratio**: 4:5
**Reference images**: finished_work

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Stunning full-bleed results ad. Background: full-frame photo of [FINISHED WORK RESULT — e.g., "a magazine-quality freshly landscaped backyard with perfect edges and lush green lawn"]. Very minimal text overlay — letting the work speak for itself. Bottom 20% has a gradient fade to [PRIMARY BRAND COLOR]. Bottom text: Business name in large, confident display font. Single subline: "[CONFIDENCE LINE — e.g., 'This is the standard. Every time.']". Website or phone in small text at bottom. Aspect ratio 4:5.
```

---

## TEMPLATE 15 — Testimonial with Photo
**Format**: Customer quote paired with a relatable lifestyle photo
**Best for**: Services with emotional or lifestyle outcomes (house cleaning, landscaping, home improvement)
**Aspect ratio**: 4:5
**Reference images**: finished_work or owner

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Warm, editorial testimonial ad. Background: [LIFESTYLE PHOTO — e.g., "a happy family in a clean, bright living room"] with warm [BRAND COLOR] tint. Top: large quotation mark graphic in [ACCENT COLOR]. Main testimonial text in italic: "[FULL CUSTOMER TESTIMONIAL — exact words, 20–35 words from real review]". Attribution: "— [FIRST NAME] [LAST INITIAL]. | [NEIGHBORHOOD] | [PLATFORM] Review". Small ★★★★★ gold stars. Bottom: [BUSINESS NAME] logo + "[TRUST LINE]". CTA in [PRIMARY BRAND COLOR] strip. Aspect ratio 4:5.
```

---

## TEMPLATE 16 — Speed / Responsiveness Ad
**Format**: Focus on fast response time as the key differentiator
**Best for**: Emergency or urgent services — HVAC, plumbing, pest, locksmith, water damage
**Aspect ratio**: 1:1
**Reference images**: none

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Urgency-first speed ad. Background: dark [PRIMARY BRAND COLOR] or near-black. Large clock or lightning bolt icon in [ACCENT COLOR]. Massive white display headline: "[SPEED CLAIM — e.g., '2 HOURS', 'SAME DAY', 'TODAY']". Subhead: "[CONTEXT — e.g., 'AC repair. Anywhere in San Diego.']". Supporting line: "[REASSURANCE — e.g., 'No waiting 3 days for a callback. We pick up.']". CTA button: "[CALL NOW CTA — e.g., 'Call (760) 555-0192 — We Answer 24/7']". High urgency, bold, no fluff. Aspect ratio 1:1.
```

---

## TEMPLATE 17 — Price Anchor / Value Frame
**Format**: Reframes the price by showing what the customer actually gets
**Best for**: Services that compete on value, not lowest price
**Aspect ratio**: 4:5
**Reference images**: finished_work

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Value-framing static ad that justifies premium pricing. Background: [CLEAN FINISHED WORK PHOTO] with elegant dark overlay. Top eyebrow: "[PRICE CONTEXT — e.g., 'For less than a restaurant dinner for two...']". Large display headline: "[VALUE REFRAME]". Itemized value list: "✓ [DELIVERABLE 1] ✓ [DELIVERABLE 2] ✓ [DELIVERABLE 3] ✓ [DELIVERABLE 4]". Price callout: "[PRICE — e.g., 'Starting at $149']". Bottom CTA in [PRIMARY BRAND COLOR] strip. Aspect ratio 4:5.
```

---

## TEMPLATE 18 — FAQ / Objection Buster
**Format**: Directly addresses the #1 objection or question in the market
**Best for**: Services with a specific barrier to conversion (pricing concern, timing, trust gap)
**Aspect ratio**: 4:5
**Reference images**: none or owner

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Direct, conversational objection-handling ad. Clean editorial layout. Background: white or [LIGHT BRAND COLOR]. Bold hook framed as a customer question: "[CUSTOMER OBJECTION/FAQ — e.g., 'Are you actually going to show up on time?']" in italic, larger size, [ACCENT COLOR]. Below: honest direct answer paragraph: "[DIRECT ANSWER — 3–4 sentences, conversational tone, pulls from brand voice and guarantee language]". Owner first name sign-off or small headshot. Business name, phone/URL at bottom. Feels like a real person wrote it. Aspect ratio 4:5.
```

---

## TEMPLATE 19 — Referral / Community Social Proof
**Format**: Ad focused on word-of-mouth and neighborhood trust
**Best for**: Businesses that grow through referrals (house services, landscaping, cleaning, handyman)
**Aspect ratio**: 1:1
**Reference images**: none or team

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Community and referral-driven social proof ad. Warm neighborhood aesthetic. Background: [WARM COMMUNITY VISUAL — e.g., "aerial view of a suburban San Diego neighborhood in golden hour"] with soft [PRIMARY BRAND COLOR] tint overlay. Center bold headline: "[WORD-OF-MOUTH HOOK — e.g., 'Your Neighbors Recommended Us.', 'The Most Referred Lawn Service in [Neighborhood].']". Body: "[SOCIAL PROOF STATEMENT]". Subline: "[NAMES LIST OR AREAS]". Trust badges: Google stars + review count. CTA: "[CALL/BOOK CTA]". Aspect ratio 1:1.
```

---

## TEMPLATE 20 — Risk Reversal / Guarantee Ad
**Format**: Bold satisfaction guarantee as the entire ad hook
**Best for**: Any service where fear of disappointment is the #1 barrier to booking
**Aspect ratio**: 4:5
**Reference images**: owner

```
[IMAGE GENERATION PROMPT MODIFIER FROM BRAND DNA]

Bold, confidence-forward guarantee ad. Background: clean [PRIMARY BRAND COLOR] with subtle texture. Large bold display headline in white: "[GUARANTEE STATEMENT — e.g., '100% Satisfaction. Or You Don't Pay.']". Below: supporting paragraph: "[GUARANTEE DETAILS — 3–4 sentences, honest tone, explains the guarantee concretely]". Owner headshot in circle frame, bottom left. Signature treatment: "[OWNER NAME], Owner — [BUSINESS NAME]". Trust signal row: ★[X.X] Google | [X]+ Reviews | Licensed & Insured | [YEARS] Years Local. Bottom: phone/URL CTA. Aspect ratio 4:5.
```

---

## TEMPLATE PRIORITY BY BUSINESS TYPE

| Business Type | Top Templates to Run First |
|---|---|
| Barbershop / Salon | 14, 01, 03, 02, 05 |
| Landscaping / Lawn Care | 02, 14, 06, 11, 19 |
| House Cleaning | 02, 09, 15, 17, 12 |
| HVAC / Plumbing / Electrical | 16, 07, 20, 03, 10 |
| Auto Detailing | 02, 14, 04, 05, 01 |
| Remodeling / Handyman | 12, 20, 08, 15, 10 |
| Pest Control | 07, 16, 04, 20, 09 |
| Real Estate / Property Mgmt | 05, 12, 10, 03, 15 |

## ASSET COLLECTION CHECKLIST FOR NEW CLIENTS

Before running Phase 3, confirm client has provided:
- [ ] Owner headshot (for Templates 03, 12, 20)
- [ ] At least 1 before/after pair (for Template 02)
- [ ] 2–3 finished work photos (for Templates 14, 15, 17)
- [ ] Team photo (for Template 08)
- [ ] Google Business profile screenshot (to confirm rating + review count)
- [ ] Top 5 real Google reviews (exact text, not paraphrased)
- [ ] 3–5 Instagram screenshots of best posts (optional, drop in assets/social/)
