# Agency Client Delivery AI Prompt Pack

**Agencies: deliver client work 3x faster with 60+ prompt + artifact pairs.**

Most AI prompt packs hand you a sentence and call it a win. You paste it in, get a page of generic bullets, and then spend an hour turning that mush into something a client will actually pay for. That hour is where the margin leaks.

This pack is built the other way around. Every prompt in here specifies an **exact deliverable** — the precise artifact structure that lands in the client's inbox: a 4-week content calendar table with named columns, a 12-slide audit report with per-slide content, a campaign brief with 8 defined sections, a monthly report with a fixed executive summary block. You are not asking an AI model for "ideas about content." You are asking it for the finished table, in the right order, with the right cells, ready to paste into Google Docs, Notion, Sheets, or a deck.

## What's inside

- **60+ prompts for strategy, content, reporting, proposals and client communication**
- **20 finished artifact templates: content calendars, audit reports, ad copy, campaign briefs**
- **Prompts produce client-facing deliverables, not brainstorming notes**
- **Format: PDF + Notion**

The 68 prompts are grouped into ten categories and numbered so you can cite them internally: *"Strategy prompt 04, run against the discovery transcript."* The 20 artifact templates are the finished structures those prompts output — each one shows the exact sections, columns, row counts, and what belongs in every cell, so you can hand a junior designer or a new account manager a spec instead of a vague brief.

Brand voice is handled at the prompt layer, not bolted on at the end. Any prompt that produces client-visible words accepts `{{brand_voice_guide}}` and is instructed to enforce it — including the enforcement rules (what the voice guide means for sentence length, banned words, jargon, emoji use, and proof style). If the guide is silent on something, the prompt says so rather than inventing a tone.

---

## How to use this pack

### The five-step delivery loop

Every deliverable you send a client moves through the same loop. The prompts are designed to sit inside it.

| Step | What happens | Prompt support |
|---|---|---|
| **1. Collect** | You gather the raw input: transcripts, analytics exports, brand docs, website copy, past deliverables. | Every prompt opens with a `{{placeholder}}` list so you know exactly what to paste in. If an input is missing, the prompt tells you to flag the gap rather than fabricate. |
| **2. Direct** | You set the shape of the output before generation. | Each prompt names the artifact, its sections, row counts, and format. The output format is specified *inside* the prompt so the model can't drift. |
| **3. Generate** | You run the prompt and get a structured draft. | Prompts are written for paste-and-run use in ChatGPT, Claude, Gemini, or any similar tool. |
| **4. Shape** | You apply your agency's judgment: swap in real numbers, tighten the argument, add screenshots. | The "How to use" line under each prompt tells you what to check and what to replace. |
| **5. Send** | The artifact goes to the client as a finished document. | The Client-ready checklist at the end of this pack is the last gate before anything leaves your outbox. |

### Placeholder reference

Replace every `{{placeholder}}` before you run a prompt. Double braces are the convention throughout this pack. If a placeholder contains a percent sign, a currency symbol, or a client name with an apostrophe, paste it as plain text — the prompts instruct the model to reproduce values exactly as supplied.

| Placeholder | What to put in it |
|---|---|
| `{{client_name}}` | The client's legal or brand name as it should appear on the document. |
| `{{industry}}` | Industry or vertical — used to calibrate examples, benchmarks, and language. |
| `{{brand_voice_guide}}` | Your client's voice guide: tone rules, do/don't examples, banned words, reading level. Optional but recommended on every word-producing prompt. |
| `{{audience}}` | Primary audience description, plus secondary segments. |
| `{{offer}}` | The product, service, or offer being marketed. Include price point and what's included. |
| `{{competitors}}` | Named competitors, or the list of brands the client is compared against. |
| `{{goals}}` | Business goals for the period — revenue, leads, signups, awareness, retention. |
| `{{kpis}}` | The metrics that define success for this account (e.g. CAC, ROAS, MQL, organic sessions). |
| `{{metrics_data}}` | Raw analytics pasted in as a table or bullet list. Keep the numbers exactly as exported. |
| `{{period}}` | The reporting window (e.g. "1–31 May 2026", "Q2 2026"). |
| `{{budget}}` | Media budget, production budget, or project fee. |
| `{{channel_mix}}` | Planned channel split (e.g. "60% Meta, 25% Google Search, 15% TikTok"). |
| `{{timeline}}` | Working timeline with real dates. |
| `{{constraints}}` | Legal, regulatory, platform, or brand restrictions. |
| `{{platform}}` | The specific channel (Instagram, LinkedIn, YouTube, Gmail, etc.). |
| `{{format_spec}}` | Any house format rules — fonts, slide counts, character limits, file naming. |
| `{{examples}}` | Past deliverables, past posts, or example copy the client already approved. |
| `{{website_url}}` | The client's site or a specific page URL. |
| `{{market}}` | Geographic market, language, and locale (e.g. "UK, English, GBP"). |
| `{{contact_name}}` | The client's stakeholder or recipient. |
| `{{your_agency}}` | Your agency name — used for report footers, proposal covers, and sign-offs. |

### Running a prompt

1. Open a fresh chat. Long context dilutes structure — don't paste 40 pages of background and expect a clean table.
2. Paste the prompt code block as-is. The formatting and rules inside it are doing the work.
3. Fill every placeholder. A prompt with `[BRACKETED]` leftovers is a prompt you haven't finished yet.
4. If the output drifts (wrong length, extra sections, missing columns), do not rewrite the whole prompt. Add one line: *"Re-output using the exact structure specified above. Do not add, remove, or rename sections."* That single correction line fixes most drift.
5. Copy the output into your client-facing template — Notion, Google Docs, Sheets, Figma, or Slides — and run the Client-ready checklist.

### When the client gives you a mess

Real inputs are messy. A "brief" might be a 600-word voice note transcript. The rule for every prompt in this pack is the same: **the model extracts, labels, and structures what is given, and marks what is missing as `[NEEDS INPUT: ...]` rather than inventing it.** A deliverable with three clearly flagged gaps is faster to finish than one built on six plausible-sounding guesses.

### Using the prompts in Notion

Each prompt is designed to be pasted into a Notion AI block, a page property, a database row, or a button that opens a prefilled template. The practical set-up: create one Notion database called `Deliverables` with properties `Client`, `Artifact type`, `Prompt ID`, `Status`, `Due`, and `Link`. The `Prompt ID` field stores the number in this pack (`#14`, `#37`, `#61`) so anyone on the team can find the exact prompt. The `Link` field points at the finished client deliverable — never at the raw AI output. That separation is what stops an unreviewed draft reaching a client.

### Working with a team

- **Account managers** own the inputs and the brief.
- **Strategists and creatives** own the artifact itself.
- **QA** owns the Client-ready checklist.
- The `{{brand_voice_guide}}` lives in the client's own Notion page and is pasted fresh for every word-producing prompt — never summarised from memory, because summarised voice guides drift.

### A note on models

These prompts are model-agnostic and work in any modern chat assistant. They lean on three behaviours that every capable model supports: strict structural output, explicit placeholder handling, and self-labelled gaps. If your model of choice truncates long tables, ask for the output section by section — "Give me rows 1–15 only" — and stitch them in the client template. Structure survives; prose style varies.

---

## The 20 finished artifact templates

The next section is the heart of the pack. Each template below is a **finished artifact**, not a description of one. What you see is the skeleton your client receives: the exact headings, the exact column headers, the exact number of rows, and a note on what belongs in every cell. When you run the matching prompt, the output should drop into this structure without reshaping.

Two rules apply to all 20:

1. **Cell content is always specific.** "Strong hook" is a note, not a deliverable. "Hook: We audited 240 pages and found 37% of them invisible" is a deliverable.
2. **Every artifact ends with a next action.** A client deliverable that doesn't tell the client what happens next gets no response. Each template's final row or section is the ask.

---


### Template 1 — 30-Day Content Calendar

**Artifact format:** one table, 30 content rows, plus a header block. Delivered as a Google Sheets–ready table (paste-friendly) or a Notion table. Optionally accompanied by a 4-week month view for layout approval.

**Header block (above the table)**

| Header field | Content |
|---|---|
| Client | `{{client_name}}` |
| Period | `{{period}}` — exact start and end dates |
| Channels | `{{channel_mix}}` |
| Content pillars | The 3–5 pillars with one-line definitions |
| Primary goal this month | The single KPI this calendar is built to move |
| CTA default | The action every post drives toward |
| Approval path | Who signs off, and by which day each week |

**Table columns (9 columns, 30 rows — one row per day)**

| Date | Day | Channel | Pillar | Format | Post type | Hook / first line | Body copy or caption | CTA | Asset + owner |
|---|---|---|---|---|---|---|---|---|---|
| 01 May | Thu | Instagram | Education | Carousel | 6-slide explainer | "Most teams check GA4 twice a month. Here's why that fails." | Full caption, 90–140 words, opening line repeated, proof point, soft CTA | "Save this for your next review" | `carousel_edu_v1.psd` / Design |
| 02 May | Fri | LinkedIn | Behind the scenes | Text + image | Founder POV | "We were wrong about our best-performing channel." | 120–180 words, one idea, one number, one question to close | "What's your most misunderstood channel?" | `linkedin_bts_v1.png` / Social |
| … | | | | | | | | | |
| 30 May | Sat | Email | Offer | Newsletter | Monthly roundup | "Everything we shipped in May" | Subject line + preheader + 3 sections + 1 CTA | "See the full breakdown" | `email_may_final.html` / Copy |

**Fixed rules for this artifact**
- Exactly 30 rows. No gaps, no duplicate dates, weekends included.
- No row may have an empty cell. If something is undecided, write `[NEEDS INPUT: ...]` so the gap is visible on the client's side too.
- Each row's hook must be a complete line a human would say out loud, not a topic label.
- Row order is chronological, and the first row's date must equal the first date in `{{period}}`.
- The final row is always a recap/CTA post — no filler.

---

### Template 2 — Weekly Content Calendar

**Artifact format:** a single-week table (7 rows) designed for fast approval and fast turnaround, plus a two-line summary of the week's angle and goal.

**Summary block**

| Field | Content |
|---|---|
| Week of | `{{week_starting}}` |
| Theme / big idea | One sentence the whole week hangs on |
| Goal | The one outcome this week drives |
| Reach vs. depth | Whether this week prioritises new audiences or existing engagement |
| Reused from | Which evergreen asset this week extends (or "new") |

**Table columns (8 columns, 7 rows — one row per day)**

| Day | Channel | Post type | Pillar | Hook / first line | Caption or body (final, not outline) | CTA | Asset + due date |
|---|---|---|---|---|---|---|---|
| Mon | IG | Reel | Product education | "The 30-second setup nobody shows you" | 80 words, spoken-style, caption opens with same hook | "Comment 'SETUP'" | `reel_week1_setup.mp4` / Wed |
| Tue | — | — | — | — | — | — | — |
| Wed | LinkedIn | Document post | Education | "Our 5-step launch checklist" | 150 words + 5 numbered steps | "Repost if useful" | `doc_checklist.pdf` / Tue |
| Thu | TikTok | Short video | Personality | "Things we got wrong in Q1" | 60 words, hook in first 2 seconds | "Follow for the rebuild" | `tt_q1_mistakes.mp4` / Thu |
| Fri | IG | Story set (4 frames) | Social proof | "Client said this. We kept the receipt." | 4 frames, each max 12 words, one sticker CTA | "Read the case study" | `stories_case_study.zip` / Fri |
| Sat | Email | Newsletter | Value | "Three things worth your Sunday" | Subject, preheader, 3 items, 1 CTA | "Reply with your weekend win" | `email_wk3_sunday.html` / Sat |
| Sun | — | Rest / batch | — | "No posting — batch Monday's assets" | n/a | n/a | — |

**Fixed rules for this artifact**
- Exactly 7 rows. A blank day uses an em dash in every cell and a stated reason in the Post type cell (rest, batch, campaign hold) — never a silent blank.
- Captions are written in final copy, ready to paste. No bullet outlines of what to say.
- The table is built to be approved on a phone screen, so each cell stays under two lines.
- If the week contains a launch, the launch row is marked with a `📌` in the Day cell.

---

### Template 3 — SEO Audit Report

**Artifact format:** a structured report, 12 sections, with a 14-slide deck equivalent. Designed to be read in 20 minutes and acted on without a call.

**Report sections**

| # | Section | Contains |
|---|---|---|
| 1 | Cover | Client, site URL, audit date, audit scope, preparer name |
| 2 | Executive summary | 5 bullets max — traffic trend, biggest loss, 3 priority fixes, 1 risk |
| 3 | Site health snapshot | Traffic, indexed pages, average position, clicks, impressions, Core Web Vitals pass rate |
| 4 | Technical findings | Table of issues with severity, affected URLs, fix, owner, effort |
| 5 | On-page findings | Per-page title tag, meta description, H1, word count, internal links, status |
| 6 | Content gap analysis | Keywords with high volume and thin coverage, mapped to existing pages |
| 7 | Keyword performance | Current ranking positions for {{target_keywords}}, with movement vs. prior period |
| 8 | Backlink profile | Referring domain count, new/lost links, top 5 links, toxic signals |
| 9 | Competitor comparison | Side-by-side of 3 competitors on the same metrics |
| 10 | Structured data | Detected schema, gaps, errors, opportunity |
| 11 | Prioritised roadmap | 90-day plan: quick wins, mid-term, structural |
| 12 | Measurement plan | KPIs, tools, reporting cadence, and the first 3 checkpoints |

**Core findings table (used in sections 4, 5, 6 — same column set throughout)**

| # | Issue | Severity | Pages affected | Evidence | Recommended fix | Owner | Effort | Impact score |
|---|---|---|---|---|---|---|---|---|
| 1 | Missing meta descriptions | High | 47 | Screaming Frog export | Write unique descriptions from intent + {{brand_voice_guide}} | Copy | M | 8/10 |

**Fixed rules for this artifact**
- Severity is one of `High / Medium / Low` and is defined in the report header.
- Impact score combines traffic upside and effort; the methodology is stated in one line.
- Every recommendation names an owner and an effort estimate. Recommendations without owners do not ship.
- Numbers are dated and sourced: "GA4, 1–31 May 2026" or "Ahrefs, pulled 4 June 2026".

---

### Template 4 — Social Media Audit

**Artifact format:** a channel-by-channel audit across 4 platforms, with a scorecard, a top-issues table, and a 30-day corrective plan.

**Scorecard (one row per channel + one roll-up row)**

| Channel | Followers | Posting cadence (actual vs. planned) | Avg. engagement rate | Reach (30d) | Saves | Shares | Follower growth | Best-performing post (why) | Score /10 |
|---|---|---|---|---|---|---|---|---|---|
| Instagram | 4,210 | 8 vs 12 planned | 3.1% | 86,400 | 310 | 92 | +84 | Carousel on "3 ways to..." — saves drove reach | 6/10 |
| LinkedIn | 1,980 | 3 vs 4 planned | 2.4% | 22,100 | 180 | 44 | +31 | Text post naming a mistake — comments from peers | 7/10 |
| TikTok | 640 | 1 vs 5 planned | 5.8% | 41,900 | 620 | 210 | +52 | Hook in first 1.5s, native audio | 5/10 |
| X | 300 | 0 vs 3 planned | 0.0% | 0 | 0 | 0 | -4 | Channel abandoned mid-pilot | 1/10 |
| **Roll-up** | | | | | | | | | **Needs a cadence decision, not more content** | **4/10** |

**Top issues table (7 rows)**

| # | Issue | Evidence | Why it hurts | Fix | Effort | Owner | Deadline |
|---|---|---|---|---|---|---|---|
| 1 | Cadence gap on TikTok | 4 of 5 planned videos unshipped | Disrupts the algorithm's learning | Batch 2 videos/week on Mondays | Low | Social lead | 12 Jun |

**30-day corrective plan**

| Week | Theme | Deliverables | Channel focus | Target metric |
|---|---|---|---|---|
| Week 1 | Fix the pipeline | 3 videos, 8 posts, 1 email | TikTok + Instagram | Publishing cadence met 5/5 days |
| Week 2 | Fix the hook | 3 videos, 8 posts, 1 email | Instagram + LinkedIn | +25% saves |
| Week 3 | Fix the CTA | 3 videos, 8 posts, 1 email | All | +0.4pp engagement rate |
| Week 4 | Fix the proof | 3 videos, 8 posts, 1 email | LinkedIn + email | Email click rate ≥ 3% |

**Fixed rules for this artifact**
- Score out of 10 with the scoring criteria stated (reach, consistency, engagement quality, conversion path, brand consistency).
- Every "best-performing post" is explained with a *why*, not just ranked.
- The audit never recommends "post more." It recommends a specific fix for a specific constraint.
- Ends with a one-paragraph recommendation and a single question for the client.

---

### Template 5 — Ad Creative Matrix (Meta + Google)

**Artifact format:** two matrices in one artifact — a Meta matrix and a Google matrix — each cell containing finished ad copy, not a copy angle.

**Meta matrix (5 columns, 4 rows of angles × 3 formats = 12 ads)**

| Angle \ Format | Reel / Video (9:16) | Carousel | Static / Image |
|---|---|---|---|
| **Problem-agitate** | Hook: "Your checkout loses 71% of mobile carts." Body: 65 words. CTA: "See the fix" | 6 cards: pain → 3 causes → 1 stat → fix → proof → CTA | Headline: "Mobile carts, fixed." Copy: 40 words. Proof badge + logo lockup |
| **Proof / social** | 30s testimonial cut, caption overlay, first frame = outcome | 5 cards: quote → metric → how → result → CTA | Testimonial card, brand palette, quote as headline |
| **Comparison** | Split-screen before/after, 20s | 5 cards: them vs us across 4 rows → CTA | Two-column comparison table graphic |
| **Offer / urgency** | 15s product demo, price on screen, countdown | 4 cards: value → price → deadline → CTA | Price + deadline + guarantee badge |

Each matrix cell must also record: primary text (final copy), headline, description, CTA button, format spec (dimensions, file size), thumbnail direction, and the audience/intent it serves.

**Google matrix (Search + Performance Max + YouTube)**

| Ad type | Headlines (15 max, 30 chars each) | Descriptions (4, 90 chars each) | Path fields | Asset group | Notes |
|---|---|---|---|---|---|
| Responsive Search | 15 final headlines | 4 final descriptions | 2 paths, 15 chars each | Group A — high intent | Pin positions 1 and 2 |
| Performance Max | 10 headlines, 4 long headlines, 4 descriptions, 5 image prompts | — | — | Group B — prospecting | Add audience signals |
| YouTube | — | 2 descriptions | — | Group C — video | 15s + 30s cuts |

**Required companion section:** an **Asset production sheet** with one row per asset (17 rows for the full set), columns: `Asset ID | Platform | Format | Spec | Copy (final) | Design brief | Due | Status`, and a **Testing plan** table: `Test | Hypothesis | Variable | Metric | Decision threshold | Decision date`.

**Fixed rules for this artifact**
- Every headline respects the platform character limit, with the character count written next to it: `Free shipping over $50 (29)`.
- No angle appears twice with the same copy. Twelve Meta ads means twelve genuinely different executions.
- Every ad maps to a funnel stage and a target audience, both named.
- The testing plan names a decision threshold in advance. "See how it does" is not a threshold.

---


### Template 6 — Campaign Brief

**Artifact format:** an 8-section brief document, 2–3 pages, that locks the campaign before any asset is made. Signed off by both sides.

| # | Section | Contains | Typical length |
|---|---|---|---|
| 1 | Campaign snapshot | Name, one-line proposition, dates, budget, markets, channels, owner | One table + 3 lines |
| 2 | Background & context | What the business is doing now, what this campaign must change, why now | 150–250 words |
| 3 | Audience | Primary segment, secondary segment, insight, tension, what they believe today, what they need to believe after | 1 table + 200 words |
| 4 | Objectives & KPIs | Business objective → campaign objective → KPI → target → measurement source | 1 table, 3–5 rows |
| 5 | Strategy | The single-minded proposition, the strategic idea, the 3 supporting proof points, the message hierarchy | 1 boxed statement + list |
| 6 | Creative direction | Tone, visual world, do/don't, mandatory elements, reference territory, what we're avoiding | 1 table + 150 words |
| 7 | Channel plan | Per channel: role in funnel, format, volume, cadence, asset list, budget split | 1 table, one row per channel |
| 8 | Plan, budget & next steps | Phased timeline with milestones, budget allocation table, RACI, approval gates, 5 next actions | 2 tables + list |

**Section 1 table**

| Field | Value |
|---|---|
| Campaign name | {{campaign_name}} |
| Proposition | The one sentence the whole campaign says |
| Flight dates | {{start_date}} → {{end_date}} |
| Total budget | {{budget}} + channel split |
| Markets / language | {{market}} |
| Channels | {{channel_mix}} |
| Campaign owner | {{your_agency}} + client-side approver |

**Section 4 table**

| Business objective | Campaign objective | KPI | Baseline | Target | Source |
|---|---|---|---|---|---|
| Grow qualified pipeline | Generate demo requests from qualified accounts | MQLs from paid | 40/mo | 75/mo | HubSpot, GA4 |

**Section 7 table**

| Channel | Funnel role | Format | Volume | Cadence | Assets required | Budget | Success metric |
|---|---|---|---|---|---|---|---|

**Section 8 timeline**

| Phase | Dates | Milestones | Approval gate | Owner |
|---|---|---|---|---|

**Fixed rules for this artifact**
- Section 5 contains exactly one single-minded proposition. Two ideas means no idea.
- Every creative instruction is either a "do" or a "don't." No adjectives without a reference.
- Section 8 ends with a numbered list of the next 5 actions, each with an owner and a date.
- No section is left as "TBC" — unfilled decisions are written as `[DECISION NEEDED: ...]` with the decision-maker named.

---

### Template 7 — Client Strategy One-Pager

**Artifact format:** a single page, front and back maximum, designed to be read in 90 seconds before a meeting. Two sides, seven blocks.

**Side A**

| Block | Contains | Word limit |
|---|---|---|
| Header | Client, period, prepared by, date | — |
| Situation | 3 lines on what's true now — market, business, channels | 60 words |
| Insight | The one non-obvious thing we believe, and the evidence behind it | 60 words |
| Objectives | 3 objectives, each with a numeric target | 3 bullets |

**Side B**

| Block | Contains | Word limit |
|---|---|---|
| Strategy statement | One sentence: how we win, expressed as a choice | 35 words |
| Strategic pillars | 3 pillars — name, what it means, what we'll do, what success looks like | 3 × 45 words |
| Audience priority | Who we're prioritising and who we're deprioritising, with a reason | 60 words |
| 90-day priorities | The top 3 moves with owner and first milestone | 3 bullets |

**Fixed rules for this artifact**
- Fits on one printed page — if it doesn't, the content is wrong, not the font size.
- Every claim is traceable to a source the client saw (data, research, or an agreed assumption).
- The deprioritisation is stated. A one-pager that only says what you'll do isn't a strategy.
- Exactly one insight. If there are two, one is a tactic.

---

### Template 8 — Monthly Performance Report

**Artifact format:** the report every client expects to receive on a set day each month. 10 sections, with a 1-page executive summary that can be forwarded on its own.

| # | Section | Contents |
|---|---|---|
| 1 | Cover | Client, period, prepared by, date, reporting cadence |
| 2 | Executive summary | 150 words max: the month's headline, the single best result, the single biggest miss, what we're changing |
| 3 | KPI scorecard | All KPIs vs. target vs. prior period vs. trend arrow |
| 4 | Channel performance | Per-channel table with spend, reach, clicks, leads, CPA/ROAS, efficiency rating |
| 5 | Top performing creative | 3 assets with the numbers, why they worked, and what we learned |
| 6 | Underperformers & losses | 3 assets/campaigns with the numbers, what we think happened, and the decision (pause/iterate/kill) |
| 7 | Creative production log | Everything shipped this month, with dates and performance |
| 8 | Insights & observations | 3–5 patterns found in the data, each with supporting numbers |
| 9 | Next month's plan | Actions, channels, budget, campaign ideas, dates |
| 10 | Action required | 3–5 items where the client needs to decide, approve, or provide something |

**Section 3 scorecard**

| KPI | Target | Actual | vs target | vs last month | Trend | Status |
|---|---|---|---|---|---|---|
| Qualified leads | 75 | 82 | +9% | +14% | ▲ | On track |
| CAC | ≤ $120 | $138 | +15% | +3% | ▲ | At risk |

**Section 4 channel table**

| Channel | Spend | Impressions | Reach | Clicks | CTR | Conversions | CPA | ROAS | Efficiency rating |
|---|---|---|---|---|---|---|---|---|---|

**Section 10 action table**

| # | Action needed | Why it matters | Decision owner | Needed by | Impact if delayed |
|---|---|---|---|---|---|

**Fixed rules for this artifact**
- Every number carries its source and date. If a number is an estimate, it says so.
- Prior-period comparison is mandatory; a client cannot judge a month in isolation.
- Section 6 always states a decision. A report that identifies losers without deciding their fate will be repeated next month.
- Section 2 is written to be forwarded to the client's boss without editing — no jargon about the campaign, just outcomes.
- If a metric is unavailable, write `Not available — reason` rather than omitting the row.

---

### Template 9 — Quarterly Business Review Deck Outline

**Artifact format:** a 14-slide deck outline. Each slide lists the headline message (the slide title is the takeaway, not a label), the content blocks, the visual, and the speaker note.

| Slide | Headline message (example) | Content blocks | Visual | Speaker note focus |
|---|---|---|---|---|
| 1 | Q2 grew pipeline 38% — here's what drove it | Title, client, date, prepared by | Cover | One-sentence framing of the quarter |
| 2 | Three things to know before we go further | Agenda: results, what worked, what's next, decisions | Numbered list | Keep to 60 seconds |
| 3 | Revenue: 38% above plan, concentrated in two segments | Actual vs target chart, revenue table, segment breakdown | Bar chart + table | Explain the concentration |
| 4 | Acquisition cost fell 22% as creative volume doubled | CAC trend line, spend vs CAC, creative volume | Dual-axis chart | Connect spend to efficiency |
| 5 | Paid social contributed 61% of pipeline | Pipeline contribution by channel | Stacked bar | Name the assumption |
| 6 | Search is underperforming on head terms | Rank movement, CTR, impression share | Line + table | Set up the SEO section |
| 7 | Three creative concepts drove 44% of conversions | Top 3 assets with spend and CVR | Asset cards | Tell the story behind one |
| 8 | What we tested and what we learned | Test table: hypothesis, result, decision | Table | Note the failed tests too |
| 9 | Where we lost money | Waste table: asset, spend lost, cause, action | Table | Take ownership |
| 10 | The market shifted: competitor X launched in May | Competitive movement, share, positioning | Comparison table | So what for us? |
| 11 | Q3 plan: three priorities, one constraint | Objectives, pillars, budget | Three-column | Name the constraint honestly |
| 12 | Q3 roadmap | Month-by-month plan | Gantt-style | Highlight two deadlines |
| 13 | Four decisions we need from you | Decision requests with options and recommendations | Table | Each has a recommendation |
| 14 | Appendix | Method, data sources, definitions | Index | Reference only |

**Decision-request table (slide 13)**

| # | Decision | Options | Our recommendation | Needed by | Consequence of no decision |
|---|---|---|---|---|---|

**Fixed rules for this artifact**
- 14 slides maximum. If the content doesn't fit, it belongs in the appendix.
- Slide titles are sentences that could be pasted into an email — no labels like "Results."
- Every slide has a speaker note. A deck read without context loses its nuance.
- The deck opens with results, not with the agenda's value. Slide 2 may be skipped entirely for a 20-minute version.
- Numbers on slides are rounded for presentation; the appendix carries the precise figures.

---

### Template 10 — Website Copy Page

**Artifact format:** a single page's worth of finished copy, structured section by section, ready to paste into the CMS. Includes SEO metadata and an accessibility note per section.

**Metadata block**

| Field | Content | Spec |
|---|---|---|
| URL slug | /features/reporting | Lowercase, hyphenated, max 5 words |
| Page title | Reporting that answers the question | ≤ 60 chars |
| Meta description | | ≤ 155 chars, includes primary keyword once |
| Primary keyword | | From {{keyword_research}} |
| Search intent | Informational / commercial / transactional / navigational | — |
| Internal links (in) | | 3–5, with anchor text |
| Internal links (out) | | 2–4 |
| CTA | Primary + secondary | |

**Page copy sections**

| Section | Element | Copy (final) | Notes |
|---|---|---|---|
| Hero | H1 | | One line, states the outcome, not the feature |
| Hero | Subhead | | 20–30 words, expands the promise, includes the mechanism |
| Hero | Primary CTA | | Verb-first, 2–4 words |
| Hero | Trust line | | Logos, rating, or guarantee |
| Problem | H2 | | Frame the cost of the status quo |
| Problem | Body | | 60–90 words, use the client's own language from discovery |
| Problem | Stat callout | | One credible number with source |
| Solution | H2 | | Position |
| Solution | Body | | 80–120 words, how it works |
| Solution | 3 benefits | | Feature + outcome + proof, one line each |
| How it works | H2 + 3 steps | | Step name, one sentence, one detail |
| Social proof | H2 | | |
| Social proof | Quote | | Verbatim, with name, role, company |
| Social proof | Result stat | | Number + baseline + timeframe |
| Objection handling | H2 + 3 objections | | The question in the client's voice, then the answer |
| FAQ | 5 questions | | Question + 40-word answer |
| Final CTA | H2 + body + button | | Repeat the promise, add the reason to act now |

**Fixed rules for this artifact**
- Copy is final, not outline. If the section needs a placeholder for a real number, it uses `[CLIENT STAT: ...]`.
- The hero H1 is under 12 words and contains no adjective that isn't doing work.
- Every benefit line is `feature → outcome`, never just the feature.
- Objection handling uses the exact words clients used in the discovery call, not the agency's phrasing.
- CTA language is consistent across the whole page — the same button text everywhere.

---

### Template 11 — Landing Page Wireframe Spec

**Artifact format:** a build-ready spec: every section, its purpose, layout, content inventory, and interaction notes — enough for a designer to lay out and a developer to build without a call.

**Spec table — one row per section (12 rows typical)**

| # | Section | Purpose | Layout | Grid | Content inventory | Interactions | Assets needed | Priority |
|---|---|---|---|---|---|---|---|---|
| 1 | Announcement bar | Drive traffic to a campaign | Full-width, 40px | 12 col | 1 line + link | Click-through to {{campaign_url}} | None | P1 |
| 2 | Hero | Explain offer + capture action | Split 6/6 | 12 col | H1, subhead, CTA, form, trust logos | Form validation, button states | Hero image, 3 logos | P1 |
| 3 | Logo strip | Borrow credibility | 5 logos, single row | 12 col | 5 SVG logos | Hover state | 5 files | P2 |
| 4 | Problem | Create recognition | Text block + illustration | 7/5 | H2, 90 words, 3 bullets | None | Illustration | P1 |
| 5 | Value props | Communicate benefits | 3 cards | 4/4/4 | 3 × (icon, title, 30 words) | Hover lift | 3 icons | P1 |
| 6 | Product visual | Show the product | Full-bleed image + 3 callouts | 12 col | Screenshot, 3 annotation labels | Scroll-linked callouts | 1 screenshot + 3 PNGs | P1 |
| 7 | Social proof | Reduce risk | 2-column quote cards | 6/6 | 2 quotes + 2 logos | None | 2 portraits | P1 |
| 8 | Comparison | Clarify choice | Table, 4 rows | 8/4 | Us vs alternative × 4 | None | Icons | P2 |
| 9 | Pricing | Remove price friction | 2 tiers | 6/6 | 2 tier cards + features | Toggle monthly/annual | 2 graphics | P1 |
| 10 | FAQ | Handle objections | Accordion, 5 items | 8/4 | 5 Q+A | Expand/collapse | None | P2 |
| 11 | Lead form | Capture | Sticky bottom bar + inline | 12 col | 4 fields + consent | Field validation, error states | None | P1 |
| 12 | Final CTA | Convert | Centred, high contrast | 12 col | H2, 1 line, button | — | Background image | P1 |

**Per-section detail block (repeated for each of the 12 rows)**

| Field | Content |
|---|---|
| Section name | Exact name used in Figma layer naming and in the ticket |
| Purpose | One line — what this section does for the visitor |
| Layout | Structure description with breakpoints (desktop 1440 / tablet 768 / mobile 375) |
| Content inventory | Every copy block and asset, with source (which artifact it comes from) |
| Interaction | Behaviour and state changes |
| Accessibility | Contrast note, alt text, keyboard behaviour, heading level |
| Copy source | Which prompt/artifact produced this copy (e.g. Prompt 13 → landing page headline set) |

**Fixed rules for this artifact**
- Every section states its purpose in one line. Sections without a purpose get cut.
- Priorities (P1/P2/P3) let the client understand what ships first.
- Accessibility is not optional — every spec includes heading level, contrast and alt text.
- Copy source is recorded so any line can be traced back and edited in one place.

---

### Template 12 — Email Newsletter

**Artifact format:** one complete email, from subject line to sign-off, plus the sending metadata and a QA strip. Designed for a client to approve and hit send on.

**Sending metadata block**

| Field | Content |
|---|---|
| Send date / time | {{send_date}}, {{send_time}} + timezone |
| Audience segment | {{segment}} |
| Send type | Broadcast / triggered |
| From | Name + reply-to |
| Subject line | Final text |
| Preheader | Final text, 40–90 chars |
| Primary CTA | |
| Tracking | UTM set, link tracking on/off, open pixel, click map |

**Email body structure**

| Block | Element | Copy (final) | Length |
|---|---|---|---|
| 1 | Eyebrow / label | | 2–4 words |
| 2 | Headline | | Under 12 words |
| 3 | Intro | | 40–60 words, personal and specific |
| 4 | Feature / story 1 | Heading + 60 words + CTA | |
| 5 | Feature / story 2 | Heading + 60 words + CTA | |
| 6 | Feature / story 3 | Heading + 60 words + CTA | |
| 7 | Proof | Quote or stat | |
| 8 | CTA block | Button + supporting line | |
| 9 | Sign-off | Name, role, org, contact | |
| 10 | Footer | Unsubscribe, address, preferences | |

**Copy block (repeated per story)**

| Field | Content |
|---|---|
| Heading | |
| Body | 60 words, one idea, one link |
| Link text | Descriptive, not "click here" |
| Image / thumbnail | Description + alt text |
| CTA | |

**QA strip (bottom of the document, not of the email)**

| Check | Status |
|---|---|
| Subject line under 45 chars | ✓ |
| Preheader does not duplicate subject | ✓ |
| All links tested and UTM-tagged | ✓ |
| Plain-text version included | ✓ |
| Alt text on all images | ✓ |
| Unsubscribe link present | ✓ |
| Mobile render checked (375px) | ✓ |
| From name recognised by recipients | ✓ |
| Link text meaningful out of context | ✓ |

**Fixed rules for this artifact**
- Subject line includes one specific, concrete detail — a number, a name, a date, or a result.
- Link text describes the destination. "Read more" is not acceptable.
- The email is written to be read on a phone: short paragraphs, one idea per block.
- The sign-off uses a real person's name and role, never "The Team" unless it genuinely is one.

---


### Template 13 — Brand Voice Guide

**Artifact format:** a working voice guide, 5 sections plus a reference appendix, that anyone can write with. Not a personality description — a set of rules with examples.

| # | Section | Contains |
|---|---|---|
| 1 | Voice in one line | A single sentence describing how the brand sounds, with a named reference (person, brand, or vibe) |
| 2 | The 4–6 voice traits | Each trait: definition, sounds like / doesn't sound like, before-after example |
| 3 | Writing rules | 8–12 concrete rules with a good/bad pair for each |
| 4 | Words we use / don't use | Two columns, 15–25 entries each, with the reason for every "don't" |
| 5 | Mechanics | Reading level, sentence length, paragraph length, punctuation, capitalisation, emoji, numbers, dates, acronyms |
| Appendix | Worked examples | 3 rewrites of the same message in the brand voice, plus 2 examples of what not to do |

**Section 2 trait table**

| Trait | What it means | Sounds like | Doesn't sound like | Before → After |
|---|---|---|---|---|
| Plainly expert | We know the topic and explain it without hiding behind jargon | "Here's what changed and what to do about it." | "Leverage our best-in-class solutions." | "We fixed the checkout bug." → "Your checkout now works on mobile." |
| Calmly direct | We say the thing, once, without hype | "This didn't work. Here's why." | "We're absolutely thrilled to announce!!" | "This didn't work. Here's why." |

**Section 3 writing-rules table**

| # | Rule | Do | Don't |
|---|---|---|---|
| 1 | One idea per sentence | "We rewrote the guide." | "We rewrote, restructured, and relaunched the guide." |
| 2 | Active voice | "The team shipped it." | "It was shipped by the team." |

**Section 4 word table**

| We use | We don't use | Why |
|---|---|---|
| help | facilitate | "Help" is what people actually say |
| use | leverage | Jargon that hides the action |
| broken | suboptimal | Say the actual state |

**Appendix worked-example table**

| # | Source text (off-voice) | Rewrite (in voice) | Which rules applied |
|---|---|---|---|
| 1 | "We're excited to announce our innovative new analytics suite!" | "You can now see where every lead comes from." | 1, 4, 6 |

**Fixed rules for this artifact**
- Every trait has a before/after example. A trait without an example is a slogan.
- The "we don't use" column states the reason — "avoid it" alone will be ignored.
- Mechanics include a numeric target (reading level, sentence length) so QA can check objectively.
- The guide is 2–4 pages. Longer voice guides don't get used.

---

### Template 14 — Persona Sheet

**Artifact format:** one persona per sheet, with a fixed 12-block layout. Create one sheet per segment; keep them comparable.

| # | Block | Content | Notes |
|---|---|---|---|
| 1 | Persona name | A first name + role | Not "User A" — a name makes the persona usable |
| 2 | One-line snapshot | "Who they are, in one sentence." | 15–20 words |
| 3 | Role & context | Job title, company size, industry, tenure | Fact-based |
| 4 | Day in the life | A real description of their week, the tools they use, who they report to | 80–120 words |
| 5 | Goals | 3 job goals, ranked | "What they're paid to achieve" |
| 6 | Challenges | 3–4 day-to-day problems |  |
| 7 | Pain points | 3 specific, emotionally real frustrations |  |
| 8 | Desired outcome | What "good" looks like for them, in their words |  |
| 9 | Buying triggers | The 4 events that make them start looking |  |
| 10 | Objections | 3 real objections with the response to each |  |
| 11 | Content habits | Where they spend time, what they follow, what they ignore |  |
| 12 | Messaging implications | 3 direct "so what" statements for the marketing team | This is the operative block |

**Section 12 table**

| Message | Evidence it comes from | Where to use it |
|---|---|---|
| "Show me the before and after, not the setup." | Pain point 2 | Landing page proof section |

**Fixed rules for this artifact**
- Every persona is built from real evidence: call transcripts, survey answers, support tickets, sales notes, or CRM fields. The evidence column is not optional.
- Goals and challenges stay distinct: a goal is what they're trying to achieve, a challenge is what's in the way.
- Section 12 always contains at least one line that constrains what the team should make. A persona with no constraints is a brochure.
- Personas are never "the audience." They are named people with a context.

---

### Template 15 — Competitive Analysis

**Artifact format:** a landscape comparison across 5 competitors, followed by a positioning conclusion. The conclusion is what the client is paying for.

**Comparison matrix (5 competitors + the client = 6 rows, 10 columns)**

| Brand | Positioning line | Primary audience | Offer / price point | Key promise | Top 3 channels | Content cadence | Strongest asset | Weakest gap | Proof used |
|---|---|---|---|---|---|---|---|---|---|---|
| {{client_name}} | | | | | | | | | |
| Competitor A | | | | | | | | | |

**Per-competitor deep dive (one block per competitor, 5 blocks)**

| Field | Content |
|---|---|
| Who they are | One line, category and positioning |
| What they do well | 3 points, each with evidence |
| Where they fall short | 3 points, each with evidence |
| Their signature move | The tactic or message they own |
| Their most recent change | What launched, when, and the visible effect |
| Who's switching to them | The segment most likely to leave the client for them |

**Positioning conclusion**

| Field | Content |
|---|---|
| Category we're claiming | |
| Our differentiator | One line |
| Proof that supports it | 3 items |
| Message we should not make | What we can't credibly claim |
| Competitive response | What competitors will do in response to our push, and our counter |

**Evidence table (used in deep dives)**

| Claim | Evidence | Source | Date checked | Confidence |
|---|---|---|---|---|

**Fixed rules for this artifact**
- Every competitive claim has evidence and a date checked. Prices, offers, and messaging change — undated claims rot.
- The matrix compares on positioning and proof, not on feature checkboxes nobody sells.
- The conclusion states what we should *not* claim — the most valuable line in most of these documents.
- The client appears in the matrix too, assessed as honestly as the competitors.

---

### Template 16 — Keyword Research Map

**Artifact format:** a map that connects search demand to the pages that should exist — not a flat list of keywords with volumes.

**Map structure**

| Stage | Rows | Columns |
|---|---|---|
| 1. Demand clusters | 8–12 clusters | Cluster, intent, total monthly volume, difficulty, business relevance, priority |
| 2. Keyword-to-page map | 30–50 keywords | Keyword, cluster, intent, volume, difficulty, current ranking URL, target URL, action |
| 3. Content gap | 10–15 gaps | Topic, keywords included, why it's missing, recommended new/existing page, priority |
| 4. Cannibalisation check | Any conflicting set | Two URLs ranking for the same intent, fix recommendation |
| 5. Quick wins | 8–12 | Keyword, position (4–20), volume, difficulty, action, expected click gain |

**Stage 1 table**

| Cluster | Primary intent | Monthly volume | Avg. difficulty | Relevance (1–5) | Priority (A/B/C) |
|---|---|---|---|---|---|

**Stage 2 table**

| Keyword | Cluster | Intent | Volume | KD | Currently ranking | Target URL | Action |
|---|---|---|---|---|---|---|---|

**Stage 3 table**

| Missing topic | Keywords in cluster | Why it's missing | Recommended page | New or expand | Priority |
|---|---|---|---|---|---|

**Stage 4 table**

| Intent | URL A | URL B | Conflict type | Fix |
|---|---|---|---|---|

**Stage 5 quick-wins table**

| Keyword | Position | Volume | KD | Action | Expected clicks/mo |
|---|---|---|---|---|---|

**Fixed rules for this artifact**
- Every keyword maps to a URL — existing or proposed. A list with no destination is a list, not a map.
- Intent is assigned before priority; intent determines the page type.
- Volume and difficulty figures carry their tool and date.
- Quick wins are chosen on position, not volume alone: a #6 keyword with 800 volume beats a #40 keyword with 20,000.

---

### Template 17 — Influencer Brief

**Artifact format:** a creator-ready brief that gets opened and followed, plus a content-rights and reporting spec.

**Brief document**

| Section | Contents |
|---|---|
| Header | Campaign, creator name, dates, contact, deliverables count |
| Why you | 2 sentences on why this creator was chosen, referencing their actual content |
| The one idea | The single thing the content must land |
| Your role | What the creator is: a voice, a demonstrator, a reviewer — pick one |
| Deliverables | Table: format, platform, quantity, length, due date, usage rights |
| Talking points | 3–5, phrased as things to say, not topics |
| Do / don't | 5 rows each, creator-specific |
| Required elements | Product name, link, disclosure, hashtag, date mention — with exact wording |
| CTA | Exact button text and link destination |
| Claim boundaries | What must not be said (claims, comparisons, guarantees) |
| Music & visuals | Reference posts, what to avoid |
| Approval process | Rounds, timeline, who approves, turnaround expectation |
| Payment & terms | Fee, bonus structure, usage rights duration, exclusivity window |

**Deliverables table**

| # | Format | Platform | Quantity | Length | Due | Usage rights | Paid |
|---|---|---|---|---|---|---|---|

**Do / don't table**

| | Do | Don't |
|---|---|---|
| 1 | | |

**Required-elements table**

| Element | Exact wording / placement |
|---|---|
| Disclosure | "#ad — paid partnership with {{client_name}}" |
| CTA | "Use code {{code}} at checkout" |

**Fixed rules for this artifact**
- The "why you" section references specific content the creator has made. Generic praise signals a templated brief and creators ignore it.
- Deliverables are specified in quantity, length, platform, and date. "One video" is not a spec.
- Claim boundaries are explicit, especially for regulated categories.
- Usage rights are stated in the brief, not negotiated after the content is live.

---

### Template 18 — Creative Brief

**Artifact format:** a two-page brief that briefs a designer or an AI image/video tool and removes all interpretation. 9 sections.

| # | Section | Contains |
|---|---|---|
| 1 | Assignment | One line: what we're making, for whom, for where |
| 2 | Background | 60–90 words of context the creator needs but shouldn't have to research |
| 3 | Audience | Who it's for, what they know, what they're sceptical of |
| 4 | Objective & single-minded proposition | The one thing the piece must communicate |
| 5 | Message hierarchy | 3 tiers: primary message, supporting points (3–4), proof points |
| 6 | Tone & voice | Reference, plus the voice rules that apply here |
| 7 | Visual direction | Reference territory, mandatory elements, colour, typography, composition, imagery style |
| 8 | Mandatory copy | Every word that appears on the asset, final, in order |
| 9 | Deliverables, specs & timing | Formats, dimensions, file names, deadlines, approval rounds |

**Section 7 visual-direction table**

| Element | Direction | Reference | Mandatory? |
|---|---|---|---|
| Colour | Warm neutral base, single accent for CTA | {{brand_colours}} | Yes |
| Type | One family, 2 weights, no italics | — | Yes |
| Subject | Real hands, real environment, no stock smiles | Reference post 1 | Yes |
| CTA treatment | Accent button, 44px tall minimum | — | Yes |

**Section 8 mandatory-copy table**

| Order | Element | Exact copy | Character limit | Placement |
|---|---|---|---|---|
| 1 | Headline | | | Top third |
| 2 | Subhead | | | Below headline |
| 3 | CTA | | | Bottom right |

**Section 9 deliverables table**

| # | Format | Dimensions | Aspect | File name | Due | Variants |
|---|---|---|---|---|---|---|

**Fixed rules for this artifact**
- Section 8 contains final copy only. Placeholder text in a creative brief ships as placeholder text.
- Every visual instruction is either mandatory or optional — nothing sits in between.
- File naming is specified, because 90% of "missing asset" messages are naming problems.
- Reference territory is links or named existing assets, never "make it premium."

---

### Template 19 — Creative Concept Board

**Artifact format:** a board that presents 3 concepts side by side, each with a stated rationale, so a client chooses rather than reacts. 3 concepts × 10 blocks.

**Board overview (one row per concept)**

| # | Concept name | One-line idea | Format | The hook | Why it fits the brief | Production effort | Risk | Recommendation |
|---|---|---|---|---|---|---|---|---|
| 1 | "The Audit" | | | | | | | |
| 2 | "The Switch" | | | | | | | |
| 3 | "The Receipt" | | | | | | | |

**Per-concept block (repeated 3 times)**

| Block | Contents |
|---|---|
| Concept name | Memorable, 2–3 words |
| The idea | 2 sentences explaining the mechanic |
| Why this audience | The specific human truth it taps |
| Visual storyboard | 4 frames, described in one line each |
| Sample copy | 3 lines of real copy as it would appear |
| Why it works | 3 bullets tied to the brief's objective |
| Risk / what could go wrong | 1–2 lines |
| Production notes | What it needs, cost, time, assets |
| Success signal | The metric this concept is designed to move |
| Deliverables required | Formats and variants |

**Storyboard table (per concept)**

| Frame | What's on screen | Text overlay | Purpose |
|---|---|---|---|
| 1 | | | Hook |
| 2 | | | Context |
| 3 | | | Proof |
| 4 | | | CTA |

**Fixed rules for this artifact**
- Exactly 3 concepts. More than 3 causes choice paralysis; fewer gives no comparison.
- Each concept includes its risk. A board without risks reads as a sales pitch.
- One concept is recommended, with the recommendation stated in the overview row.
- Sample copy is written, not described — the client should be choosing from finished words.

---

### Template 20 — Client Onboarding Plan

**Artifact format:** a 4-week onboarding plan that runs from kick-off to a signed-off first plan, with a shared tracker, access checklist, and risk list.

**Plan overview**

| Week | Milestone | Owner | Client dependency | Deliverable at end of week |
|---|---|---|---|---|
| Week 1 | Access & discovery complete | Agency + Client | Ad accounts, analytics, brand assets | Discovery summary + access tracker green |
| Week 2 | Strategy & positioning agreed | Agency | Stakeholder time | Strategy one-pager signed off |
| Week 3 | Creative concepts approved | Agency + Client | Review time from client | Concept board + approved routes |
| Week 4 | First calendar & launch plan locked | Agency | Final sign-off | 30-day calendar + launch checklist |

**Access checklist**

| # | Asset / account | Owner | Needed by | Status | What breaks without it |
|---|---|---|---|---|---|
| 1 | Meta Business Manager access | Client | Day 2 | Not started | No paid social launch |
| 2 | GA4 + GTM access | Client | Day 2 | Not started | No baseline, no reporting |
| 3 | Brand assets (logo, fonts, colours) | Client | Day 4 | Not started | Design work blocked |
| 4 | Previous 12-month performance export | Client | Day 4 | Not started | No historical context |

**Week-by-week detail (repeated for 4 weeks)**

| Field | Content |
|---|---|
| Theme | The purpose of the week |
| Agency tasks | 4–6 specific tasks |
| Client tasks | 2–4 specific tasks, with names if known |
| Meeting | Agenda with 5 items, attendees, duration |
| Deliverable | The artifact produced, and the artifact template it matches |
| Exit criteria | The condition that must be true to close the week |
| Risk | The most likely thing to go wrong, and the mitigation |

**Kick-off agenda**

| # | Item | Minutes | Owner | Output |
|---|---|---|---|---|
| 1 | Introductions and roles | 5 | Both | Named contacts list |
| 2 | Business goals and KPIs | 15 | Client | Agreed goals list |
| 3 | What has and hasn't worked | 15 | Client | Prior learnings doc |
| 4 | Scope and what's out of scope | 10 | Agency | Agreed scope statement |
| 5 | Access, timelines, and comms | 10 | Both | Access checklist + cadence |

**Standing cadence table**

| Meeting | Frequency | Duration | Attendees | Agenda source | Who sends notes |
|---|---|---|---|---|---|

**Fixed rules for this artifact**
- Every week ends with a deliverable and an exit condition. "Relationship building" is not a deliverable.
- Client tasks are named and dated, so delay is visible early rather than at week 4.
- The kick-off agenda has a time budget per item; total equals the meeting length.
- A standing risk section names the three most likely failure points and the mitigation for each.

---


---

# The 68 prompts

Every prompt below is written to produce a **finished deliverable**, not a list of ideas. Each one names the artifact, its sections, its row counts, and its format. Each one includes the placeholder list, the handling rules, and the enforcement of `{{brand_voice_guide}}` where client-facing words are produced.

**How to read a prompt**

- The **Role** line sets the standard. Change it if your client needs a different register.
- The **Inputs** block is what you paste in. Every placeholder must be replaced.
- The **Output format** block is the contract. Do not remove it — it is the reason the output arrives in a usable shape.
- The **Rules** block prevents the three most common failures: generic copy, fabricated data, and wrong structure.
- The **How to use** line after each prompt tells you what to check before the artifact goes anywhere near a client.

Prompts are numbered continuously from 01 to 68 so you can reference them in your Notion database, your team's Slack, or your client proposal ("the strategy brief is Prompt 03, run against the discovery transcript").

---

## Client Strategy & Discovery

### 01 — Discovery Call Synthesis Into a Client Brief

```text
ROLE:
You are a senior strategist at {{your_agency}}. Your job is to turn a raw discovery call into a written brief a delivery team can build from, without a follow-up call.

INPUTS:
- Client: {{client_name}}
- Industry: {{industry}}
- Discovery transcript or notes: {{discovery_notes}}
- Brand voice guide: {{brand_voice_guide}}
- Known goals: {{goals}}

OUTPUT FORMAT — produce exactly these five sections, in this order:

1. CLIENT SNAPSHOT (4 bullets, max 60 words total): what they sell, who they sell it to, their current marketing setup, the relationship as it stands today.
2. STATED PROBLEM (3 bullets): the problems the client named, in their own words, quoted where possible.
3. UNDERLYING PROBLEM (1 paragraph, 80–120 words): the pattern beneath what they said — the real constraint holding results back.
4. GOALS & CONSTRAINTS (a table with columns: Goal | Success metric | Deadline | Constraint). Minimum 3 goal rows, maximum 6. If the client gave no metric, write [NEEDS INPUT: metric for {{goal}}] in that cell — do not invent one.
5. OPEN QUESTIONS (a numbered list, 5–8 items): only questions that materially change what we deliver. For each, add one line: "Why it matters: {{impact}}".

RULES:
- Separate what the client SAID from what you INFER. Label inferences as "Hypothesis".
- Never invent a metric, deadline, budget, or customer name. Use [NEEDS INPUT: ...] instead.
- Write in plain professional English. No consultancy vocabulary ("leverage", "synergy", "unlock", "holistic").
- If {{brand_voice_guide}} is provided, write any client-facing summary paragraphs in that voice; the internal sections stay neutral.
- Do not recommend tactics in this brief. This document defines the problem, not the solution.

HOW TO USE:
Run this immediately after the first discovery call, before you write anything else. The "Open Questions" list becomes your follow-up email — send it the same day. If the goals table is full of [NEEDS INPUT] markers, do not start strategy work until at least two are closed.
```

### 02 — Client Goals Into a Measurable KPI Framework

```text
ROLE:
You are a performance marketing strategist translating vague business goals into a KPI framework a client will recognise and a team can report against.

INPUTS:
- Client: {{client_name}}
- Business goals: {{goals}}
- Current metrics: {{current_metrics}}
- Industry benchmarks: {{industry_benchmarks}}
- Paid, organic, and owned channels in scope: {{channel_mix}}

OUTPUT FORMAT — produce three tables and one short paragraph:

PARAGRAPH (80 words): the logic connecting the business goal to the measurable behaviour that signals progress. Name the chain explicitly: "Because the business needs {{goal}}, we need {{behaviour}}, which we measure by {{metric}}."

TABLE 1 — KPI FRAMEWORK
Columns: Business goal | Objective | Primary KPI | Secondary KPIs | Current baseline | 30-day target | 90-day target | Source of truth
Rows: one per business goal. Minimum 3, maximum 6.

TABLE 2 — FUNNEL MAPPING
Columns: Funnel stage | User question | Behaviour we need | Metric | Where it is measured | Typical benchmark
Rows: exactly 5 (Awareness, Consideration, Conversion, Retention, Advocacy).

TABLE 3 — MEASUREMENT PLAN
Columns: Metric | Tool | Who pulls it | Cadence | Where it appears in reporting | Owner
Rows: one per KPI in Table 1, minimum 3 rows.

RULES:
- Every KPI must have a baseline. If no baseline exists, write "Baseline: [NEEDS INPUT — 30 days of data required]".
- Benchmarks must be labelled as benchmarks, not promises.
- Do not include vanity metrics in Table 1 (no follower counts, no impressions alone). If a vanity metric is genuinely important to the client, put it in Table 2 only.
- Prefer one primary KPI per goal. Multiple primaries means no primary.

HOW TO USE:
Use this before the strategy one-pager (Template 7). If the client pushes back on a target, ask what they think the target should be — then re-run with their number and record the disagreement in the notes. A target the client agrees with is worth more than a target you believe in.
```

### 03 — Ideal Customer Profile From Real Sales Data

```text
ROLE:
You are a research analyst building an ideal customer profile from evidence, not assumptions.

INPUTS:
- Client: {{client_name}}
- Product or service: {{offer}}
- Deal notes, CRM fields, or closed-won interview notes: {{customer_data}}
- Churn reasons or lost-deal notes: {{lost_deal_data}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce these sections:

1. ICP IN ONE SENTENCE (max 30 words): who buys, what situation triggers the purchase, and what outcome they want.
2. ICP TABLE — Columns: Attribute | Best-fit customer | Median customer | Poor-fit customer. Rows: exactly 8 attributes covering company size, industry, role seniority, trigger event, budget band, current alternative, decision process, and primary objection. Fill with specific values, not adjectives alone.
3. SIGNALS TABLE — Columns: Signal | Where we observe it | How strongly it predicts fit | Action. Minimum 8 rows. Rank the top 3 by "how strongly it predicts fit".
4. ANTI-ICP (3 bullets): who to disqualify, and the cost of taking them on.
5. MESSAGE IMPLICATIONS (5 bullets): what to say to the best-fit customer that would be wrong to say to everyone.

RULES:
- Base every attribute on evidence in the input. If the input is thin, state "Evidence gap: {{attribute}}" and write the provisional read with a question mark.
- Use revenue or deal-size data when provided; otherwise use frequency.
- Do not describe a demographic profile unless the data supports it. Firmographics and triggers beat demographics.
- The client-facing message implications must respect {{brand_voice_guide}} — write them in the voice the best-fit customer would respond to.

HOW TO USE:
This is the input to every persona sheet (Template 14) and to the targeting prompts in Paid Advertising. If your CRM data is thin, this prompt still works — it will surface the gaps, and those gaps are often the highest-value output. Bring them to the client as questions, not as findings.
```

### 04 — Discovery Questionnaire That Pre-Sells the Engagement

```text
ROLE:
You are a strategist preparing a client discovery questionnaire that produces usable answers. A good questionnaire is also the first proof of competence.

INPUTS:
- Client: {{client_name}}
- Engagement type: {{engagement_type}} (retainer, project, audit, campaign)
- What we need to know to deliver: {{information_requirements}}
- Known context from the referral or pitch: {{known_context}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. INTRODUCTION (60–80 words): sent to the client, written in {{brand_voice_guide}}. States why we're asking, what it unlocks, how long it takes, and that their answers shape the deliverable — never "to better understand your business."
2. QUESTION TABLE — Columns: # | Section | Question | Why we ask | Answer type | Required? | What we'll do with it. 24 questions across 6 sections: Business & goals, Audience & offer, Current channels & performance, Brand & creative, Measurement & tooling, Process & constraints. Answer type is one of: short text, long text, number, date, multiple choice, file reference, "they may not know".
3. "I DON'T KNOW YET" SECTION — 8 items: the things a client honestly may not know yet, with a sentence on how we'll answer them for them.
4. REQUESTED MATERIALS CHECKLIST — 12 items: files, access, and exports to request, with the format needed (CSV, PDF, PNG, screen recording).
5. DEADLINE & FOLLOW-UP NOTE — 2 sentences: when we need it and what happens next.

RULES:
- No question can be answered with "yes/no" unless a yes/no answer is genuinely actionable.
- No question asks about the client's preferences rather than their behaviour. "What tone do you like?" is banned; "Send me three emails you're proud of" is right.
- Ask for numbers with a date range attached: "Revenue for the last 6 months" not "revenue".
- Maximum 8 minutes of client effort. If the questionnaire exceeds that, cut questions.
- The "I don't know yet" section is written kindly — clients are busy, not negligent.

HOW TO USE:
Send this 48 hours after the kick-off call, not at it. When it comes back, run Prompt 01 against the answers and the received files together — you now have a brief built from their words, which is a far better foundation than pitch notes.
```

### 05 — Strategy Workshop Agenda and Facilitator Notes

```text
ROLE:
You are a strategist running a 90-minute strategy workshop. You need an agenda that produces decisions, not a discussion that produces notes.

INPUTS:
- Client: {{client_name}}
- Attendees and roles: {{attendees}}
- Pre-work outputs to build on: {{discovery_brief}}
- Time available: {{workshop_duration}}
- Decisions that must be made in the session: {{decisions_required}}

OUTPUT FORMAT — produce:

1. WORKSHOP OBJECTIVE (1 sentence): what is true at the end of this session that is not true now.
2. AGENDA TABLE — Columns: Time | Segment | Objective | Facilitator prompt (exact words to say) | Format | Output captured. Rows sum exactly to {{workshop_duration}}. Include one 10-minute break.
3. EXERCISE CARDS — 3 cards, each with: name, purpose, step-by-step instructions, the exact question written on the whiteboard, time limit, and what the facilitator does if the group goes quiet.
4. DECISION LOG — pre-filled with a row per decision in {{decisions_required}}: Decision | Options on the table | Who decides | Deadline if not decided today.
5. PARKING LOT — a list structure for off-topic items, with a line reading "We'll come back to this — logged here."
6. CLOSING SCRIPT (80 words) and a FOLLOW-UP EMAIL (120 words) that goes out within 24 hours: what was decided, what remains open, what we need from the client and by when.

RULES:
- Every agenda row states an output captured. If a segment produces nothing, cut it.
- Facilitator prompts are actual sentences to say, including the question that unblocks a quiet room.
- No exercise exceeds 20 minutes.
- Decision log rows must have a named decision-maker, not "the team".
- The follow-up email contains no new analysis — only what was said in the room.

HOW TO USE:
Print the agenda and the decision log; keep the follow-up email open in a second window. Send it within 24 hours — the strategic value of a workshop decays fast, and the client will read that email as proof the session was worth their time.
```

### 06 — Positioning Statement and Messaging Hierarchy

```text
ROLE:
You are a brand strategist producing a positioning statement and the messaging hierarchy that sits under it.

INPUTS:
- Client: {{client_name}}
- Product or service: {{offer}}
- Audience research: {{audience}}
- Competitors: {{competitors}}
- Brand voice guide: {{brand_voice_guide}}
- Claims we can make (legal-approved): {{approved_claims}}

OUTPUT FORMAT:

1. POSITIONING STATEMENT (max 45 words): "For {{audience segment}} who {{need}}, {{client_name}} is the {{category}} that {{benefit}} because {{reason to believe}}." Fill every blank. If a blank cannot be filled from the inputs, write [NEEDS INPUT: ...] inside it — do not fill it with a safe-sounding phrase.
2. CATEGORY & FRAME-OF-REFERENCE (1 paragraph, 60 words): the category the client should be understood in, and the existing frame the strategy borrows from.
3. MESSAGING HIERARCHY — Columns: Tier | Message | Audience relevance | Proof point | Where it's used | Words to avoid. Rows: exactly 3 tiers — Tier 1 primary message (1 row), Tier 2 supporting messages (3 rows), Tier 3 proof points (4 rows).
4. DIFFERENTIATION TABLE — Columns: Claim | Competitor position | Our position | Substantiation. Minimum 4 rows. At least 2 rows must be honest about where a competitor is stronger.
5. ELEVATOR PITCH (3 versions): 15 words, 30 words, 60 words.
6. WHAT WE DO NOT SAY (4 bullets): claims to avoid, with the reason.

RULES:
- Every tier-1 and tier-2 message must trace to an approved claim. If {{approved_claims}} is missing, write [NEEDS INPUT: legal-approved claims] at the top of the hierarchy table and mark all rows as provisional.
- A message that could be used by any competitor is not a differentiator — flag it.
- Nothing in the hierarchy may contradict {{brand_voice_guide}}.
- Write the elevator pitches in the brand voice; they are spoken out loud.

HOW TO USE:
This output feeds landing page copy (Prompt 13), ad copy (Prompt 25), the strategy one-pager (Template 7), and proposal covers. Run it once, store it, and treat it as the source of truth — every later piece of client-facing copy should trace back to the hierarchy in this document.
```

### 07 — Competitive Landscape Scan for a Pitch

```text
ROLE:
You are a strategist building a competitive scan that supports a pitch. It must be defensible, current, and useful on the slide — not a Wikipedia summary of the category.

INPUTS:
- Client: {{client_name}}
- Category and market: {{industry}}, {{market}}
- Named competitors: {{competitors}}
- The client's offer: {{offer}}
- Public information you have been given: {{competitor_research}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. MARKET STRUCTURE (150 words): who the buyer actually compares against, including indirect competitors and the alternative of doing nothing.
2. COMPETITOR MATRIX — Columns: Competitor | Positioning line | Target segment | Offer & price | Primary channel | Signature asset | Visible weakness. Rows: exactly 5 competitors.
3. THE WHITE SPACE (1 paragraph, 80 words): the territory no competitor occupies, and the reason it's worth occupying.
4. THE CLIENT'S FIT (1 paragraph): where {{client_name}} genuinely fits that white space, and where it doesn't. The second half is not optional.
5. PITCH ANGLE — 3 options: Columns: Angle | The one-line argument | Proof we'd need | Risk. Include one angle that is contrarian rather than safe.
6. SOURCES TABLE — Columns: Claim | Source | Date checked | Confidence. Every factual claim in sections 1–4 appears here.

RULES:
- Never state a competitor's price, revenue, or strategy without a source and a date. If you don't have it, write [NEEDS INPUT: verify {{competitor}} pricing].
- Do not describe competitors as "bad". Describe them as differently positioned. If a competitor is genuinely stronger on something, say so — clients respect it and it makes the rest of the analysis credible.
- The white space must be reachable by this client. A white space in a segment they can't serve is decoration.
- Pitch angles follow {{brand_voice_guide}} and are written to be said out loud in a room.

HOW TO USE:
Run this 48 hours before a pitch, then verify every claim in the sources table yourself — models get pricing and positioning details wrong, and a client will check. Replace anything you can't verify with a public source or cut it.
```

### 08 — Business Case and ROI Model for a Retainer

```text
ROLE:
You are a commercial strategist building the business case for a retainer engagement, using the client's own numbers where you have them.

INPUTS:
- Client: {{client_name}}
- Proposed scope and fee: {{scope}}, {{fee}}
- Current performance baseline: {{current_metrics}}
- Client's cost or lead value: {{unit_economics}}
- Team hours included per month: {{hours_included}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. THE ARGUMENT (120 words): why this engagement is the cheapest available path to the client's goal. Written in plain language for a business owner, not a media buyer.
2. ROI MODEL TABLE — Columns: Line | Value | Source / assumption. Rows: fee, hours included, blended hourly cost, current monthly output (leads/sales/content), value per unit, projected monthly output, projected monthly value, net monthly value, ROI multiple. Every number carries a source or is labelled "ASSUMPTION — client to confirm".
3. SCENARIO TABLE — Columns: Scenario | Output assumption | Monthly value | Net vs fee | Break-even requirement. Exactly 3 rows: conservative, expected, stretch.
4. RISK & DOWNSIDE (5 bullets): what makes this not work, and the trigger that would prompt a scope conversation.
5. WHAT WE'LL MEASURE (table, 4 rows): Metric | Current | Target | How we'll know we're on track.
6. THE ASK (60 words): what we need from the client to make the model true — access, decision speed, content approval turnaround.

RULES:
- Every number is either sourced from the inputs or labelled ASSUMPTION. No blended averages that hide their inputs.
- If the ROI is negative on the conservative scenario, say so plainly and explain what changes it. A model that only works on the best case is not a business case.
- Never use "guaranteed", "risk-free", or "triple your revenue".
- The argument paragraph must survive being read aloud by the client's CFO.

HOW TO USE:
Put this in the proposal as an appendix, not as the opening slide — clients trust the appendix more than the pitch. If they challenge a number, fix the assumption and re-run; never defend a soft number.
```

---


## Content Production

### 09 — Long-Form Article From a Brief

```text
ROLE:
You are a senior content writer producing publication-ready copy for {{client_name}}. The output must be publishable without a rewrite.

INPUTS:
- Topic and target keyword: {{topic}}, {{target_keyword}}
- Search intent and audience: {{search_intent}}, {{audience}}
- Client offer and key proof points: {{offer}}, {{proof_points}}
- Brand voice guide: {{brand_voice_guide}}
- Approved claims and claims to avoid: {{approved_claims}}, {{claims_to_avoid}}
- Internal links available: {{internal_links}}
- Target word count: {{word_count}}

OUTPUT FORMAT — produce these sections in this order:

1. TITLE (2 options, max 60 chars each, then the reason each was chosen in 10 words)
2. META DESCRIPTION (1, 120–155 chars, includes the target keyword once, includes a reason to click)
3. SLUG (lowercase, hyphenated, max 5 words)
4. OPENING (2 paragraphs, 120 words): the reader's problem stated in their words, then the promise of the article. No throat-clearing.
5. H2/H3 OUTLINE (as a markdown list): every H2 and H3 with a one-line note on what that section contains. Minimum 4 H2s.
6. FULL DRAFT: the complete article under those headings, with all paragraphs, lists, and the final CTA. Target {{word_count}} ±10%. Do not write "..." or "[continue]" — write the whole thing.
7. CTA BLOCK (final 60 words): the ask, plus the reason to act now, written in the client's voice.
8. INTERNAL LINK PLAN (table): Anchor text | Target URL | Placement in the article
9. EDITOR'S NOTES (4 bullets): anything the client must verify, plus 2 places where a real number, screenshot, or example would strengthen the piece.

RULES:
- Match {{brand_voice_guide}} strictly: sentence rhythm, vocabulary, formality level, and banned words.
- No invented statistics, studies, customer names, or quotes. If a number is needed, write [CLIENT STAT: ...] in the copy exactly where it goes.
- Write for a human reader, not for a crawler. No keyword stuffing; use the target phrase naturally where a person would.
- Never use "in today's digital landscape", "it's important to note", "delve into", "unlock", "leverage", "game-changer", "revolutionise".
- If the outline would require more than {{word_count}} words, compress the outline rather than truncating sentences.

HOW TO USE:
Generate, then run Prompt 57 (Pre-Send Client Deliverable QA) over the draft before it goes to the client. Treat the "Editor's notes" section as your list of client questions — it converts a vague "can you review this?" into a specific list of three things to check.
```

### 10 — Blog Post Series From One Pillar Topic

```text
ROLE:
You are a content strategist turning one pillar topic into a coherent series that builds authority and internal links.

INPUTS:
- Pillar topic: {{pillar_topic}}
- Target keyword and supporting keywords: {{target_keyword}}, {{supporting_keywords}}
- Audience and their stage: {{audience}}
- Brand voice guide: {{brand_voice_guide}}
- Proof points and offers to reference: {{proof_points}}, {{offer}}
- Pillar page URL (for internal links): {{pillar_url}}

OUTPUT FORMAT:

1. SERIES OVERVIEW (100 words): the argument the series makes in total, and what the reader can do after finishing it.
2. SERIES PLAN TABLE — Columns: # | Working title | Target keyword | Intent | Angle | Length | Publish week | Links to | Funnel stage. Exactly 6 posts.
3. FULL OUTLINES — for each of the 6 posts: H1, meta description, 4–6 H2s with a sentence of content under each, the proof point used, the CTA, and the posts in the series it links to.
4. LINK GRAPH (table): From post | To post | Anchor text | Why this link
5. HOOK BANK — 18 opening lines across the 6 posts, grouped by post, each written as a finished sentence. Two per post plus three alternates.
6. REPUBLISHING PLAN (table): Post | Reuse as | New format | Timing | Channel

RULES:
- Each post must be independently useful and must also be incomplete alone — the series has a reason to exist.
- The angles must not overlap. If two posts argue the same point, merge or re-angle them.
- Only link to a post that will exist; mark planned links as [planned].
- Every hook must be specific to its post. Generic hooks are banned.
- Apply {{brand_voice_guide}} to every title, hook, and CTA.

HOW TO USE:
Use the series plan as a client-facing roadmap in a content meeting — clients approve direction faster when they see six concrete titles rather than a topic list. Lock the plan before writing a single word of draft.
```

### 11 — Case Study With a Real Result

```text
ROLE:
You are a writer turning project material into a case study that a client can publish with their name on it.

INPUTS:
- Client: {{client_name}}
- Subject company: {{subject_company}} (or "our client" if permission is pending)
- Challenge and starting position: {{challenge}}
- What we did: {{approach}}
- Results with numbers: {{results}}
- Testimonials available: {{testimonials}}
- Brand voice guide: {{brand_voice_guide}}
- Permission status for naming and logos: {{permissions}}

OUTPUT FORMAT — produce these sections:

1. HEADLINE (2 options, under 60 chars, each with the result in it)
2. META DESCRIPTION (1, 140–155 chars)
3. AT A GLANCE (table): Client | Sector | Challenge | Solution | Result | Timeframe. One row.
4. THE CHALLENGE (120 words): specific, quantified, no drama. What was broken or missing, with the number that proved it.
5. THE APPROACH (180 words, 3 sub-headings): what we did, in the order we did it. Concrete enough that another team could repeat it.
6. THE RESULTS (table): Metric | Before | After | Change | Timeframe. Minimum 3 metric rows, maximum 6. Also include 1–2 sentences of interpretation per metric.
7. QUOTE FROM THE CLIENT (formatted, with name, role, company — or [CLIENT QUOTE: ...] if not yet approved)
8. KEY TAKEAWAYS (3 bullets): what a reader in a similar position should do, phrased as advice.
9. CTA (40 words)
10. PUBLISHING NOTES (4 bullets): permission dependencies, assets needed (logo, screenshot, headshot), and the recommended placement on the site.

RULES:
- Results must come from {{results}}. Never round up, never extrapolate, never combine a 6-month figure with a 3-month timeframe.
- If a metric has no before-value, write "Before: not tracked" — don't manufacture a baseline.
- Write in {{brand_voice_guide}}, and prefer plain claims to superlatives.
- If {{permissions}} does not include naming rights, write the whole draft in the "our client" form and flag it in Publishing Notes.

HOW TO USE:
Send the draft with the results table highlighted — clients approve numbers fastest and slowest, so isolate them. Keep the "Before: not tracked" rows visible; they explain why some metrics can't be compared and they make the rest of the table believable.
```

### 12 — Product Description Set for an Ecommerce Page

```text
ROLE:
You are an ecommerce copywriter producing the full description set for one product page.

INPUTS:
- Product: {{product_name}}
- Specs and materials: {{product_specs}}
- Who it's for and the problem it solves: {{audience}}, {{problem}}
- Price and what's included: {{price}}, {{includes}}
- Brand voice guide: {{brand_voice_guide}}
- Approved claims: {{approved_claims}}

OUTPUT FORMAT — produce:

1. PAGE TITLE (≤ 60 chars) and META DESCRIPTION (≤ 155 chars)
2. HERO BLOCK: H1 (≤ 10 words), subhead (20–30 words), 3 bullet value props (≤ 8 words each)
3. SHORT DESCRIPTION (2 sentences, ≤ 40 words) for product cards and search results
4. LONG DESCRIPTION — 5 sub-sections with headings: what it is, why it works, who it's for, what's in the box, how to use it. 200–300 words total, written as final copy.
5. SPECIFICATION TABLE — Columns: Specification | Detail. 8–12 rows, including dimensions, weight, materials, care, warranty, what's included.
6. BENEFITS TABLE — Columns: Feature | What it means for the customer | Use case. One row per feature from {{product_specs}}.
7. USE-CASE ROW (table): Situation | How they use it | What they get. 4 rows.
8. FAQ (6 questions): Question in the customer's voice | Answer (40–60 words). Cover: fit, care, compatibility, returns, gifting, comparison to alternatives.
9. CTA PAIR: Primary button text | Secondary link text | One supporting line
10. IMAGE REQUIREMENTS (table): Image # | What it shows | Format | Aspect | Priority — 6 rows for the product page gallery.

RULES:
- Every claim must appear in {{approved_claims}} or be a factual spec. No "life-changing", no "you'll never", no health or performance claims not documented.
- Benefits must be written for the customer's situation, not the product's features. "Holds 12 drinks" → "Fits a full day's water without refilling".
- Match {{brand_voice_guide}} precisely — product copy is where brand voice is most visible and most often breaks.
- Never compare to a named competitor. Comparative claims without substantiation are a legal risk.

HOW TO USE:
Pair this with Prompt 23 (Image and Graphic Prompt Set) and you can ship a product page from a single spreadsheet of specs. Run Prompt 57 (Fact and Claim Check) before publishing anything with a performance or health claim.
```

### 13 — Landing Page Headline and Hero Copy Set

```text
ROLE:
You are a conversion copywriter producing the hero block and the headline set for a landing page, then the section headlines that follow.

INPUTS:
- Offer: {{offer}}
- Audience and their current belief: {{audience}}, {{current_belief}}
- Single-minded proposition from strategy: {{smp}}
- Proof available: {{proof_points}}
- Traffic source the page receives: {{traffic_source}}
- Brand voice guide: {{brand_voice_guide}}
- Claims to avoid: {{claims_to_avoid}}

OUTPUT FORMAT — produce:

1. ANGLES TESTED (table): Angle | Core promise | Proof anchor | Risk. Exactly 4 angles — outcome, pain relief, objection removal, and contrarian.
2. HERO BLOCK — for the top 2 angles only. For each: H1 (≤ 12 words), subhead (20–30 words), primary CTA (2–4 words), secondary CTA (2–4 words), trust line (≤ 15 words), and a one-line note on why this angle suits {{traffic_source}} traffic.
3. SECTION HEADLINE SET (table): Section number | Section purpose | Headline | Subhead | What proves it. Exactly 7 sections.
4. CTA MATRIX (table): Placement | Button text | Supporting microcopy | Expected action. 6 placements, with consistent button text across all rows.
5. VARIATION SET: 3 alternate H1s for the recommended angle, each testing a different mechanism.
6. REJECTION NOTES (4 bullets): the angle you are NOT recommending, and why — with what it would take for it to become the right choice.

RULES:
- The H1 states the outcome, not the mechanism. If a reader can't tell what they get, the headline is wrong.
- Match {{brand_voice_guide}} exactly — headline register matters more than body copy, and clients notice headlines first.
- Every headline must be paired with a proof anchor. A headline with nothing behind it is a promise the page can't keep.
- Do not use questions as headlines unless the question is exactly what the audience asks out loud.
- No fake urgency, no countdown pressure unless there is a real deadline.

HOW TO USE:
Send the four angles to the client and let them pick before you write a word of body copy — it is the cheapest decision in the whole project and it prevents a full rewrite. Once they choose, the section headline set maps directly onto Template 11.
```

### 14 — Video Script With Shot List

```text
ROLE:
You are a video producer writing a production-ready script for {{client_name}}, with a shot list a small crew can shoot in one session.

INPUTS:
- Video type and platform: {{video_type}}, {{platform}}
- Length: {{target_length}}
- Objective: {{objective}}
- Audience and what they should do afterwards: {{audience}}, {{desired_action}}
- Message hierarchy and proof: {{message_hierarchy}}, {{proof_points}}
- Brand voice guide: {{brand_voice_guide}}
- Who is on camera: {{on_camera_talent}}

OUTPUT FORMAT — produce:

1. VIDEO SPEC (table): Platform | Length | Aspect ratio | Resolution | Captions required | CTA
2. HOOK OPTIONS (3 finished lines, each ≤ 12 words, with a note on the visual that plays under each)
3. SCRIPT TABLE — Columns: Timecode | Visual / shot | On-camera words (final) | On-screen text | Audio / music | Notes. Every row timed; the timecodes run continuously from 00:00 to the full length. Minimum 10 rows.
4. B-ROLL LIST (table): Shot | Description | Where it comes from | Priority. 8 rows.
5. CAPTIONS FILE — the full spoken script as a plain caption block, broken into lines of ≤ 42 characters, with speaker labels and punctuation for the burned-in version.
6. CTA AND END CARD (table): Element | Final content | Duration
7. PRODUCTION CHECKLIST (table): Item | Owner | Needed by | Status — 10 rows, including talent, location, props, wardrobe, releases, and platform access.
8. ALT TEXT (one line per shot): a description of the visual for accessibility.

RULES:
- The first 3 seconds must contain the hook. Write the words that go there explicitly.
- Spoken lines must be sayable at normal pace in the timecode given. If a line is too long, cut words, not time.
- Do not write "insert B-roll here" as a script line — write the shot.
- Apply {{brand_voice_guide}} to every spoken and on-screen word. Read it aloud before sending.
- If {{proof_points}} is empty, use a demonstration beat instead of a claim beat. Do not invent a result.

HOW TO USE:
The captions file is the single most reusable output here — send it to the client for approval even when they approve the script visually, because caption text is what most people actually read. Add shot list row numbers to the edit brief.
```

### 15 — Newsletter From a Single Idea

```text
ROLE:
You are a writer producing a complete, sendable email newsletter from one idea — not a roundup of links.

INPUTS:
- The one idea: {{newsletter_idea}}
- Audience and what they care about: {{audience}}
- Supporting points and proof: {{supporting_points}}
- Client offer or CTA: {{offer}}, {{cta}}
- Brand voice guide: {{brand_voice_guide}}
- Previous subject lines that worked and failed: {{subject_line_history}}
- Sending metadata: {{send_date}}, {{segment}}

OUTPUT FORMAT — produce:

1. SUBJECT LINE OPTIONS (5): Text | Character count | Predicted angle | Why it works
2. PREHEADER (1, 40–90 chars, complements rather than repeats the subject)
3. SEND-TIMING RECOMMENDATION: 1 line with day, time, and timezone, plus the reasoning in one sentence
4. EMAIL BODY — 6 blocks, written as final copy: Hook (≤ 40 words), Setup (60 words), Idea explained (150 words), Proof or example (80 words), Practical takeaway (80 words, 3–5 bullets), CTA (40 words)
5. BUTTON TEXT + LINK (table): Placement | Button text | Link destination | Tracking note
6. PLAIN-TEXT VERSION (the full email with no formatting)
7. SEGMENT NOTES (3 bullets): who should get this and who should be excluded
8. QA CHECKLIST (table, 8 rows): Check | Pass condition | Result
9. FOLLOW-UP EMAIL (optional, 90 words): a 3-day follow-up for non-openers with a different subject and a different angle.

RULES:
- One idea per newsletter. If the input contains three, select one and note the other two as "next issue" in a single line.
- No link-heavy roundups. If a link is included, it supports the idea; it is not the idea.
- Match {{brand_voice_guide}} — email is the most personal channel and the easiest place to break voice.
- Every claim about the client's results must come from {{supporting_points}}. If you need a number, write [CLIENT STAT: ...].

HOW TO USE:
Pick the subject line from the five using your own open-rate history, not the model's prediction. Send the follow-up version to non-openers only — the second email has to be materially different, or it reads as nagging.
```

### 16 — Content Repurposing Matrix From One Long Asset

```text
ROLE:
You are a content strategist turning one substantial asset into a full week of channel-native content, with each output written as final copy.

INPUTS:
- Source asset: {{source_asset}} (article, video, webinar, or podcast transcript)
- Channels in scope: {{channel_mix}}
- Audience: {{audience}}
- Brand voice guide: {{brand_voice_guide}}
- Constraints (offer links, approvals, embargoes): {{constraints}}

OUTPUT FORMAT — produce:

1. SOURCE DIGEST (100 words): the core argument, the three strongest moments, and the proof points available.
2. REPURPOSING MATRIX — Columns: # | Output | Channel | Format | Hook (finished first line) | Core message | Source moment used | CTA | Publish day | Effort. Exactly 10 rows — 7 content posts, 2 emails, 1 ad.
3. FULL COPY for each of the 10 rows, written as final copy in the correct platform format. Include character counts for social posts.
4. FORMAT NOTES (table): Output | Platform-specific requirements | Visual spec | Caption/alt text. One row per output.
5. SEQUENCING PLAN (table): Day | Output | Purpose in the sequence
6. WHAT TO SKIP (3 bullets): moments in the source that do not work as standalone content, with the reason.

RULES:
- Each output must be native to its platform. Do not paste the same paragraph into five channels with different hashtags.
- A post must be readable without clicking through. If it only makes sense with the source, it's a teaser — write a teaser only if that's the goal, and label it.
- Apply {{brand_voice_guide}} to every output, and adjust formality by channel without breaking the voice.
- No output may reuse the same hook as another.

HOW TO USE:
Run this the day a core asset is signed off, and schedule the whole matrix at once. The "what to skip" list saves an hour of arguing about whether a moment is strong enough — it is already decided.
```

---


## Social Media

### 17 — 30-Day Social Content Calendar

```text
ROLE:
You are a social media lead producing a client-ready 30-day content calendar for {{client_name}}.

INPUTS:
- Brand voice guide: {{brand_voice_guide}}
- Content pillars: {{content_pillars}}
- Channels: {{channel_mix}}
- Goals for the month: {{goals}}
- Offer and primary CTA: {{offer}}, {{primary_cta}}
- Seasonal or launch dates: {{key_dates}}
- Approval constraints: {{constraints}}

OUTPUT FORMAT — produce exactly:

HEADER BLOCK (a table): Client | Period (exact start and end dates) | Channels | Pillars | Month goal | Default CTA | Approval path

CALENDAR TABLE — Columns: Date | Day | Channel | Pillar | Format | Post type | Hook / first line | Full caption or body copy | CTA | Asset + owner.
Exactly 30 rows, one per calendar day, in date order starting from the first date in {{period}}. Weekend days are included; if a channel skips weekends, use "— (rest day)" in Channel and a reason in Post type.

RULES:
- Every one of the 30 rows has content in every cell. No blank cells, no "TBC", no "[placeholder]" left in the copy. If something genuinely can't be decided, write [NEEDS INPUT: ...] in that single cell and nowhere else.
- Hooks are finished sentences a person would say, not topic labels. "Benefits of CRM" is a label; "Your CRM is full of leads you'll never call back" is a hook.
- Captions are final copy, ready to paste. Do not outline.
- No two rows share the same hook or the same post type on the same channel within any 7-day window.
- Pillar distribution across the 30 days must match {{content_pillars}} weights (if not given, distribute roughly 40% education, 30% proof, 20% personality, 10% offer and say so in one line).
- Every caption follows {{brand_voice_guide}}. Do not use words the guide bans, even as filler.
- The final row is always a recap or CTA post.

HOW TO USE:
Send this as the monthly planning artefact with the captions already written — clients approve calendars faster when they read the copy rather than imagine it. Check the last row is a CTA, then paste the table straight into Sheets and convert to a Notion database.
```

### 18 — Weekly Content Calendar for Fast Approval

```text
ROLE:
You are a social lead producing a single-week calendar designed to be approved on a phone in under 10 minutes.

INPUTS:
- Week starting: {{week_starting}}
- Brand voice guide: {{brand_voice_guide}}
- Channels: {{channel_mix}}
- Theme or campaign focus: {{week_theme}}
- The week's goal: {{week_goal}}
- Asset availability: {{assets_available}}
- Any hard dates: {{key_dates}}

OUTPUT FORMAT — produce:

WEEK SUMMARY (table): Week of | Theme | Goal | Reach-or-depth focus | Reused-from asset | Total assets due

CALENDAR TABLE — Columns: Day | Channel | Post type | Pillar | Hook / first line | Final caption or body copy | CTA | Asset + due date.
Exactly 7 rows, Monday to Sunday, in that order.

PRODUCTION NOTES (table): Asset | Owner | Format | Due day | Dependency — one row per asset in the calendar, 3–8 rows.

RULES:
- Exactly 7 rows. A rest day uses an em dash in every cell and states the reason in Post type ("Rest — batch Monday's assets"), never a silent blank.
- Captions are written final. No bullet outlines of what the post should say.
- Keep every cell short enough to read on a phone: hooks under 12 words, captions under 150 words.
- If a launch or live event falls in the week, mark that row's Day with a 📌.
- Apply {{brand_voice_guide}} to every hook and caption.
- Total assets in the Production Notes table must equal the number of non-rest days plus any extras listed.

HOW TO USE:
Send this on Friday afternoon for the following week, so the client approves it before Monday. If they ask for changes, edit the caption cell directly — the structure rarely needs to change, and rebuilding the table is where hours disappear.
```

### 19 — One Post, Five Platforms, Written Five Ways

```text
ROLE:
You are a social media writer adapting a single idea into platform-native posts. Each version must feel written for its platform, not reformatted from a master copy.

INPUTS:
- The idea: {{content_idea}}
- Platforms: {{platforms}}
- Audience: {{audience}}
- Brand voice guide: {{brand_voice_guide}}
- Links or CTA destination: {{cta_destination}}
- Proof or detail to include: {{proof_point}}
- What worked before on each platform: {{platform_performance_notes}}

OUTPUT FORMAT — for each platform in {{platforms}}, produce:

PLATFORM BLOCK:
- Post type and length: (e.g. "LinkedIn text post, 130–180 words")
- Post copy (final, complete, ready to paste)
- Hook / first line (called out separately)
- Hashtags (only where the platform uses them; 3–5 max on LinkedIn, 0–3 elsewhere)
- Visual or video direction: one line
- Alt text: one line
- CTA placement: where and how
- Character count of the post copy

RULES:
- Never paste the same paragraph into two platforms. Different platform, different opening line, different rhythm, different call to action.
- LinkedIn: no emoji stacks, no "🚀 Excited to share", first line must work before "see more". TikTok: hook must land in the first 2 seconds, so the first line is a spoken line. Instagram: caption opens with the hook line, then a blank line, then the body. X: under 280 characters, no thread unless asked.
- Use {{proof_point}} as a concrete detail in every version.
- Apply {{brand_voice_guide}}, but adjust formality to the platform without breaking the voice.
- No hashtag stuffing, no engagement bait ("comment YES below"), no "link in bio" unless the destination is bio.

HOW TO USE:
Use this when a client wants "one idea, everywhere" without five times the cost. Check the LinkedIn first line against a phone preview — if it doesn't earn the tap, rewrite the first line before sending.
```

### 20 — Instagram Carousel: Slides and Caption

```text
ROLE:
You are a designer-copywriter producing a complete Instagram carousel: the copy for every slide, the caption, and the visual instruction for each slide.

INPUTS:
- Topic: {{topic}}
- Goal: {{goal}}
- Number of slides: {{slide_count}}
- Audience: {{audience}}
- Brand voice guide: {{brand_voice_guide}}
- Proof points: {{proof_points}}
- Brand colours and typography: {{brand_assets}}
- CTA destination: {{cta_destination}}

OUTPUT FORMAT — produce:

1. CAROUSEL STRUCTURE TABLE — Columns: Slide # | Role | Slide headline (final) | Slide body (final, ≤ 35 words) | Visual instruction | Design notes. Exactly {{slide_count}} rows. Slide 1 is the cover; the last slide is the CTA.
2. COVER SLIDE — 3 headline options, each ≤ 9 words, with the reason each works.
3. FULL SLIDE COPY — every slide's headline and body written out as final copy, ready for layout.
4. CAPTION — 120–180 words, opening with the cover headline, then the value, then the CTA. Include a first-comment block of 3 extra lines.
5. CTA OPTIONS (3): Button text | Destination | Why this wording
6. ALT TEXT for each slide (one line each).
7. DESIGN HANDOFF NOTES (table): Element | Specification — typeface, sizes, colour hexes, margins, safe zones, 4:5 aspect, 1080×1350 px.
8. ENGAGEMENT PROMPT (1 line): a question that invites a real reply.

RULES:
- One idea per slide, except the cover and CTA. If a slide needs two ideas, split it and add a slide.
- Slide headlines under 9 words; body under 35 words. If a slide needs more, it's a caption paragraph, not a slide.
- Slide 1 must work standalone — most people see only the cover before swiping.
- No "swipe to see more" clichés. No numbered-list abuse like "5 Ways to...".
- Apply {{brand_voice_guide}} to every word on every slide. This is where voice guidelines usually get ignored — check it.
- The CTA slide has exactly one action.

HOW TO USE:
Send the slide table to the designer and the caption separately to the client approver — designers care about layout, clients care about words, and combining them slows both. Add the alt text to the upload step; it's a spec, not a nicety.
```

### 21 — Short-Form Video Scripts for Reels, TikTok, Shorts

```text
ROLE:
You are a video writer producing three ready-to-shoot short-form video scripts for {{client_name}}, each with a spoken hook, a full script, shot notes, and captions.

INPUTS:
- Topic: {{topic}}
- Goal: {{goal}}
- Target duration: {{duration}}
- Platform: {{platform}}
- Audience: {{audience}}
- Brand voice guide: {{brand_voice_guide}}
- Proof or demonstration available: {{proof_point}}
- Who appears on camera: {{talent}}
- B-roll or product access available: {{assets_available}}

OUTPUT FORMAT — produce three scripts, each with:

SCRIPT BLOCK:
- Concept name and the one-line idea
- Hook (first 2 seconds, ≤ 9 spoken words, written as it is spoken)
- Spoken script with timecodes (0–2s hook, 2–5s setup, 5–{{duration}}s substance, final 2s CTA). Full sentences, not notes.
- On-screen text overlays with timing
- Shot list (table): Time | Shot | What happens | Notes
- Caption (≤ 90 words, opens with the hook)
- Hashtags (3–5, platform-appropriate)
- Alt text and a 1-line accessibility description
- CTA button text and destination
- Variants: 2 alternate hooks for A/B testing

RULES:
- The hook must create a reason to keep watching: a specific number, a contradiction, a mistake callout, or a promise with a timeframe.
- Write for the ear. Short sentences, no subordinate clauses stacked, no jargon the viewer wouldn't use.
- Every script has a visible or verbal proof moment — a screen recording, a result, a demonstration, or a physical object.
- Apply {{brand_voice_guide}} to spoken lines; check that the guide's formality survives being spoken aloud.
- No video ends without a spoken or on-screen CTA.
- Do not use trending audio references you can't verify — specify the audio type ("upbeat, mid-tempo, no vocals") instead.

HOW TO USE:
Shoot all three in one session and cut them later — that alone turns a 3-day production into a half-day one. Have the creator read each script aloud before recording; if they stumble, the line is too long.
```

### 22 — Community Management Reply Bank

```text
ROLE:
You are a community manager writing ready-to-send replies to predictable audience comments, in the client's voice, with the line between helpful and over-promotional marked.

INPUTS:
- Brand voice guide: {{brand_voice_guide}}
- Platform: {{platform}}
- Common comment types: {{common_comments}}
- FAQ or approved answers: {{faq_approved_answers}}
- Offers and campaigns currently running: {{current_offers}}
- Escalation rules: {{escalation_rules}}

OUTPUT FORMAT — produce:

1. REPLY BANK TABLE — Columns: Comment type | Example comment | Reply (final, ready to paste) | Tone | Notes. Minimum 20 rows covering: genuine praise, price question, feature question, complaint, competitor mention, "how much?", "do you ship to X?", scam/spam, "can I get a discount?", job application, partnership request, request for free advice, negative review, wrong assumption about the product, and 6 more realistic cases.
2. ESCALATION TABLE — Columns: Situation | Response to send now | Internal action | Who is notified | Timeframe. 8 rows, including anything involving a legal threat, a medical/safety claim, a data request, or an influencer ask.
3. TONE LADDER TABLE — Columns: Situation | Temperature | Rule — 5 rows from warm to firm, describing when to move down the ladder.
4. PROACTIVE FAQ POSTS — 6 short posts (60–90 words each) answering the most-asked questions before they're asked, with a title for each.
5. NEVER-SAY LIST — 10 things not to say in replies, each with a one-line reason and a replacement phrase.

RULES:
- No reply may contain an unverified claim, a discount not in {{current_offers}}, or a promise not in {{faq_approved_answers}}.
- Never argue with a complaint. Acknowledge once, move to a DM, and escalate.
- Replies under 40 words for most cases; the reply must fit on a phone screen above the fold.
- Apply {{brand_voice_guide}}. Keep replies conversational even if the brand voice guide is formal elsewhere — and if it says so explicitly, follow the guide.
- Never use an emoji unless {{brand_voice_guide}} permits it and specifies which ones.

HOW TO USE:
Save this as a shared doc with a searchable table and let the community team copy-paste. After 30 days, log which reply types got the best response and update the bank — the fastest replies should be the ones you use most.
```

### 23 — Image and Graphic Prompt Set for Design and AI Generation

```text
ROLE:
You are an art director producing a production-ready set of creative briefs for visual assets — one brief per asset, usable by a designer or pasted into an image generation tool.

INPUTS:
- Campaign or content theme: {{theme}}
- Number of assets needed: {{asset_count}}
- Brand colours, fonts, and visual rules: {{brand_assets}}
- Brand voice guide: {{brand_voice_guide}}
- Where assets will run: {{channels}}
- What the assets must communicate: {{message}}
- Product or subject: {{subject}}
- Photography available: {{available_photos}}

OUTPUT FORMAT — produce:

1. CREATIVE DIRECTION (120 words): the visual world, the feeling, the one visual idea that ties the set together, and the reference style described in words (not "modern and sleek").
2. ASSET BRIEFS — one block per asset, exactly {{asset_count}} blocks. Each block contains:
   - Asset ID (e.g. A01) and where it runs (channel, placement, dimensions)
   - The message this asset carries (one line)
   - Composition (what's in frame, where, what's cropped, camera angle)
   - Subject and action
   - Colour and light
   - Typography (if any) — exact text to appear
   - Do / don't list (3 each)
   - Alt text (one line)
   - AI generation prompt (a single paragraph, if applicable): subject, action, composition, lighting, lens, colour, style, aspect ratio, negative prompt
   - Design note (what a designer should watch out for)
3. CONSISTENCY RULES (table): Element | Rule | Applies to assets — 8 rows covering palette, lighting, model casting, typography, props, crop ratio, background, and treatment.
4. HANDOFF CHECKLIST (table): Check | Pass condition — 10 rows.

RULES:
- Describe the composition physically: what's in frame, left/right/top/bottom, what's cropped. "Left third, subject looking into the frame, negative space on the right for a 40-character headline" — that level of detail.
- Do not reference real people's likenesses or living artists by name.
- The AI generation prompt must include an aspect ratio and a negative prompt.
- Any text that appears in the image is written exactly and flagged for the designer to set as live type (never baked into a generated image).
- Apply {{brand_voice_guide}} to any written words in the design.
- Every asset has alt text.

HOW TO USE:
Run this with the creative brief (Prompt 48) in the same session so the words in the image and the words on the page agree. Designers will thank you for specifying the crop ratio — that's the reason images come back the wrong shape.
```

---


## Paid Advertising

### 24 — Full Paid Media Account Build Plan

```text
ROLE:
You are a performance media planner producing the account build plan for a new {{client_name}} campaign — the document a media buyer executes from, without further interpretation.

INPUTS:
- Campaign objective: {{objective}}
- Offer: {{offer}}
- Target audience: {{audience}}
- Budget and split: {{budget}}, {{channel_mix}}
- Markets: {{market}}
- Tracking stack available: {{tracking_stack}}
- Landing page or offer URL: {{landing_url}}
- Brand voice guide: {{brand_voice_guide}}
- Constraints (brand safety, legal, seasonality): {{constraints}}

OUTPUT FORMAT — produce:

1. CAMPAIGN ARCHITECTURE TABLE — Columns: Campaign | Platform | Funnel stage | Objective | Audience | Budget | Daily cap | Target CPA / ROAS | Bid strategy | Launch date. 6–8 rows.
2. AD SET / AD GROUP STRUCTURE — a nested table per campaign: Campaign | Ad set or group | Audience definition (full targeting spec) | Exclusions | Placement | Budget | Bid | KPI. 12–18 rows total.
3. TRACKING SPECIFICATION — table: Event | Trigger | Parameter | Where it fires | Parameter value format. Exactly 10 events covering view content, scroll 50%, form start, form submit, phone click, add to cart, purchase, signup, download, and a qualified conversion.
4. UTM NAMING CONVENTION — table: Parameter | Format | Example. 5 rows, plus one full example URL built with a real campaign name.
5. AUDIENCE & EXCLUSION RULES — 8 bullets covering exclusions, overlap priority, retargeting windows, lookalike source and percentage, and suppression lists.
6. LAUNCH SEQUENCE — table: Date | Action | Owner | What we're watching | Rollback trigger. Minimum 6 rows across the first two weeks.
7. TESTING PLAN — table: Test | Hypothesis | Variable | Audience | Budget | Metric | Decision threshold | End date. Minimum 6 rows.
8. BUDGET CONTROL RULES — 5 bullets: daily caps, the CPA at which we pause an ad set, the % drop that triggers a check, the budget increase rule (e.g. +20% only after 3 days at target), and who can approve spend changes.

RULES:
- Every targeting spec must be specific enough to build without asking a question: audience size estimate, exclusions, placements, bid strategy.
- No target CPA without a basis. If there is no benchmark, write "Target CPA: [NEEDS INPUT — client benchmark or 30-day test data]".
- The testing plan names a decision threshold in advance, in numbers, and a decision maker.
- Exclusions must include existing customers where that makes sense, plus employees and invalid placements.
- Apply {{brand_voice_guide}} to any ad copy included in the plan and to the campaign naming convention (use readable names, not codenames).

HOW TO USE:
This is the build doc you attach to the media buying ticket. Run it before opening a platform account, not after — the structure in the table is what prevents the classic mess of 14 ad sets and no learning data.
```

### 25 — Meta and Google Ad Copy Matrix

```text
ROLE:
You are a performance copywriter producing a finished ad copy matrix — every cell contains final, platform-ready copy, not an angle.

INPUTS:
- Offer and promotion: {{offer}}, {{promotion}}
- Target audience: {{audience}}
- Unique selling points: {{usps}}
- Proof points: {{proof_points}}
- Brand voice guide: {{brand_voice_guide}}
- Landing page promise: {{landing_page_promise}}
- Claims to avoid: {{claims_to_avoid}}
- Competitor context: {{competitors}}

OUTPUT FORMAT — produce:

1. ANGLE SET TABLE — Columns: Angle | Core promise | Proof used | Audience tension | Risk of over-claiming. 6 rows, one per angle.
2. META MATRIX — Columns: Angle \ Format | Reel / video 9:16 | Carousel | Static / image. 6 angles × 3 formats = 18 cells. Each cell contains: Primary text (final, with character count), Headline (final, with character count), Description (final), CTA button, thumbnail direction, and the funnel stage it serves.
3. GOOGLE MATRIX — Columns: Ad type | Headlines (15, each with character count) | Descriptions (4, each with character count) | Path fields | Ad group. Rows: Responsive Search, Performance Max (headlines, long headlines, descriptions, 5 image prompts), YouTube (2 descriptions, 2 CTA variants), Display (2 short headlines, 1 long description).
4. ASSET PRODUCTION SHEET — Columns: Asset ID | Platform | Format | Spec | Copy | Design brief | Due | Status. One row per asset, 16–20 rows.
5. NEGATIVE KEYWORD & AUDIENCE LIST — 15 terms/phrases to exclude, each with the reason.
6. TESTING PLAN — table: Test | Hypothesis | Variable | Metric | Decision threshold | Decision date. 6 rows.

RULES:
- Character counts are shown next to every headline and description, and every one respects the platform limit.
- Every ad makes the same promise as the landing page it points to. If the ad over-promises, the page fails.
- The 18 Meta cells must be genuinely distinct. If two cells could run against the same audience at the same time without a learning problem, they are not different enough — rewrite one.
- Apply {{brand_voice_guide}} strictly. In paid copy, adjectives are the most common place a brand voice breaks.
- No "guaranteed", "risk-free", "best price", or "limited time" unless the deadline or claim is real and documented.
- No naming competitors in Meta copy. Comparative Google ads must be factually supportable.

HOW TO USE:
The matrix is the artefact — deliver it as a table the client can read and the buyer can build from. Check the character counts yourself before sending; platform preview is the final word, but a broken count is the fastest way to lose client trust.
```

### 26 — Google Ads Keyword and Negative Keyword Build

```text
ROLE:
You are a search media specialist producing a structured, build-ready keyword set for a Google Ads account.

INPUTS:
- Product or service: {{offer}}
- Target audience and intent: {{audience}}
- Landing page and its promise: {{landing_url}}, {{landing_page_promise}}
- Seed keywords from the client: {{seed_keywords}}
- Competitors: {{competitors}}
- Geography and language: {{market}}
- Budget: {{budget}}
- Historical search term data if available: {{search_terms}}

OUTPUT FORMAT — produce:

1. CAMPAIGN STRUCTURE TABLE — Columns: Campaign | Ad group theme | Match type strategy | Budget | Target CPA | Bid. 5–7 campaigns, each with 1–4 ad groups.
2. AD GROUP KEYWORD TABLE — Columns: Ad group | Keyword | Match type | Volume | Competition | Intent | Priority | Landing page. 30–45 rows. Match types are exact, phrase, or broad — and broad is only allowed where a smart bidding strategy is in place.
3. NEGATIVE KEYWORDS TABLE — Columns: Keyword | Type | Why excluded | Apply at campaign or account level. 20–30 rows, covering free, jobs, DIY, definition, competitor-irrelevant, and low-intent modifiers.
4. MESSAGING BY AD GROUP — table: Ad group | Headline angle | Supporting copy | Proof. One row per ad group, so the copy matches the query intent.
5. BID & BUDGET RECOMMENDATION (table): Campaign | Daily budget | Starting target CPA | Bid strategy | Rationale | When to change.
6. SEARCH TERMS TO WATCH — table: Search term | Likely match type | Relevance | Action. 15 rows, based on the pattern of common waste terms in the category.
7. FIRST-30-DAYS OPTIMISATION PLAN (table): Week | Action | What we're watching | Decision rule.

RULES:
- Every keyword maps to an ad group and a landing page. A keyword with no landing page is not in the brief.
- Intent is assigned before priority. "Brand" keywords, "competitor" keywords, and "service" keywords get separated — they are not one budget.
- Broad match only appears with smart bidding and a stated daily budget and CPA ceiling.
- Negative keywords must be explained. "Because we don't sell it" is a reason; "not relevant" is not.
- If {{search_terms}} is empty, say so and provide the watch list as a hypothesis, labelled as such.

HOW TO USE:
Pair this with Prompt 25 so the ad group themes and the copy angles are the same — mismatched ad groups and ads are the most common waste in new accounts. Review the negative list with the client; they'll add 10–20 more from their own customers.
```

### 27 — Landing Page Conversion Copy for Paid Traffic

```text
ROLE:
You are a conversion copywriter writing landing page copy for a paid campaign, where the visitor has already clicked an ad and is 7 seconds from leaving.

INPUTS:
- The ad promise (exact): {{ad_promise}}
- Offer: {{offer}}
- Audience: {{audience}}
- Price and what's included: {{price}}, {{includes}}
- Proof points, testimonials, and numbers: {{proof_points}}, {{testimonials}}
- Objections: {{objections}}
- Brand voice guide: {{brand_voice_guide}}
- Traffic source and device split: {{traffic_source}}, {{device_split}}
- Claims to avoid: {{claims_to_avoid}}

OUTPUT FORMAT — produce:

1. MESSAGE MATCH TABLE — Columns: Ad angle | Headline promise on page | Supporting subhead | Proof shown near top | Continuity note. 3 rows, one per ad angle. This is the table that catches broken message match before the client finds it.
2. HERO — H1, subhead, CTA button, microcopy under the button, trust line, and a 30-word note on the traffic implication of this hero.
3. SECTION COPY — table: Section # | Purpose | Headline | Body (final, 40–80 words) | Proof element | CTA. 8 sections.
4. OBJECTION HANDLING — table: Objection (in customer language) | Headline | Answer (60 words) | Placement. 6 objections, using the exact words from {{objections}}.
5. FORM BLOCK — table: Field | Label | Helper text | Required | Validation message. 6 fields, plus the button text and the privacy line.
6. TRUST & PROOF SECTION — 5 elements: each with the exact wording and where it appears.
7. MOBILE CONSIDERATIONS (table): Element | Mobile treatment — 6 rows, including sticky CTA, tap target sizes, thumb-zone placement, and load priority.
8. CTA VARIANTS (table): Placement | Button text | Microcopy. 5 placements with consistent primary action.
9. COMPLIANCE & CLAIM NOTES (table): Claim used | Where it appears | Substantiation available | Status. Minimum 4 rows.

RULES:
- The H1 must echo the ad promise in different words. If someone can't tell they landed in the right place, the message match failed.
- Above-the-fold must contain the offer, the price or price logic, and one piece of proof.
- Apply {{brand_voice_guide}}, and remember most paid traffic reads on a phone in a hurry.
- Every claim traces to {{proof_points}}. If a claim needs substantiation you don't have, it goes in the compliance table with status "HOLD — needs substantiation" and is removed from the copy.
- The CTA text describes what happens next, not "Submit" or "Learn more".

HOW TO USE:
Run this against each ad angle you're buying traffic for — not once for the page. Then run the QA pass on the combined ad-and-page pair, because the most common wasted spend is a page that answers a different question than the ad asked.
```

### 28 — Paid Social Creative Concepts for a Campaign

```text
ROLE:
You are a creative strategist producing three distinct paid social campaign concepts, each with the finished assets inside the concept.

INPUTS:
- Campaign objective and offer: {{objective}}, {{offer}}
- Audience: {{audience}}
- Brand assets: {{brand_assets}}
- Brand voice guide: {{brand_voice_guide}}
- Proof available: {{proof_points}}
- Channels: {{channel_mix}}
- Budget per concept: {{budget}}
- What has been tried before: {{past_campaigns}}

OUTPUT FORMAT — produce:

1. OVERVIEW TABLE — Columns: Concept # | Name | The idea in one line | Format | Channel | Proof used | Production effort | Expected learning | Recommendation. 3 rows.
2. CONCEPT 1, 2, 3 — for each:
   - Concept name and one-line idea
   - The insight it taps (2 sentences, tied to the audience)
   - Storyboard table: Frame | What's on screen | Text overlay | Spoken line (if video) | Purpose — 5 rows for video concepts, 4 rows for static
   - Sample copy: primary text, headline, description — final
   - Static concept alternative: layout instruction, exact text blocks, visual direction
   - Why it fits the objective (3 bullets)
   - Risk: what could go wrong (2 bullets)
   - Production checklist (table): Item | Owner | Cost | Lead time
   - Success signal: the metric this concept is designed to move
3. TESTING DESIGN — table: Concept | Variable tested | Audience | Budget split | Metric | Decision threshold | Decision date. 3 rows.
4. WHAT WE ARE DELIBERATELY NOT DOING — 3 bullets, each with the reason.

RULES:
- Three concepts must attack the problem from three different mechanisms, not three different executions of the same idea.
- Every concept must contain a proof element. A concept without proof is a vibe.
- Each concept must be feasible within the stated budget and lead time — if a concept needs a shoot, say so and cost it.
- Apply {{brand_voice_guide}} to every word of sample copy.
- No concept may rely on a competitor's name, logo, or likeness.

HOW TO USE:
Present all three in a 15-minute client call with the recommendation stated out loud — clients pick faster when you're willing to say which one you'd run. Once chosen, run Prompt 23 on the chosen concept for the production briefs.
```

### 29 — Retargeting Sequence With Message Progression

```text
ROLE:
You are a performance marketer designing a retargeting sequence where each step answers a different objection, so the sequence escalates rather than repeats.

INPUTS:
- Audience definitions: {{retargeting_audiences}}
- Offer: {{offer}}
- Page or ad they came from: {{entry_point}}
- Known objections: {{objections}}
- Proof available: {{proof_points}}
- Brand voice guide: {{brand_voice_guide}}
- Frequency caps and channels: {{channels}}, {{frequency_caps}}
- Testimonial and case study assets: {{assets_available}}

OUTPUT FORMAT — produce:

1. SEQUENCE MAP TABLE — Columns: Step | Audience | Days since visit | Objective | Message angle | Objection addressed | Asset type | Channel | Frequency cap | Success metric. 6 steps.
2. FULL COPY for each of the 6 steps: for each, produce the complete asset — ad primary text, headline, description, CTA, and for email/landing steps, the subject line, preheader, body copy (60–120 words), and button text.
3. ESCALATION LOGIC (bullets): what triggers moving a user from one step to the next, and what causes them to be suppressed from the sequence entirely.
4. EXCLUSION RULES (table): Condition | Action. 8 rows covering purchasers, converters, converters after the window, site employees, existing customers where relevant, and frequency-reached users.
5. CREATIVE ROTATION PLAN — table: Step | Asset A | Asset B | Rotation date. 6 rows.
6. FREQUENCY MONITORING PLAN — table: Metric | Threshold | Action. 5 rows.
7. SUCCESS METRICS TABLE — Columns: Step | Primary metric | Benchmark | Cumulative conversion target | Cut-off date.

RULES:
- Each step must address a different objection. If two steps use the same angle, merge them.
- Step 1 must confirm the visit ("the thing you were looking at"), step 2 must answer the top objection, and the final step must make the offer concrete with price, terms, or guarantee.
- Respect {{frequency_caps}} — a sequence that ignores caps will burn the audience.
- Apply {{brand_voice_guide}}, but make the final step the most direct and least decorated.
- No step implies knowledge the brand doesn't have ("we noticed you've been browsing" is false unless it is true).

HOW TO USE:
Build this as a set of live ads plus email automations, not as a PDF concept. The escalation logic is the part worth reading twice — it's where most retargeting sequences leak money by showing the same message four times.
```

### 30 — Paid Media Budget Reallocation Recommendation

```text
ROLE:
You are a performance media lead reviewing performance data and producing a specific budget reallocation decision with reasoning, not a dashboard summary.

INPUTS:
- Current budget by channel and campaign: {{current_budget}}
- Performance by channel and campaign: {{performance_data}}
- Business goal and target CPA/ROAS: {{goals}}, {{targets}}
- Learning phase status (days live, spend, conversions): {{learning_status}}
- Seasonality or upcoming events: {{events}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. DECISION SUMMARY (120 words): what you are recommending, in one paragraph, with the number at the centre.
2. CURRENT vs PROPOSED BUDGET TABLE — Columns: Channel / campaign | Current monthly | Current CPA or ROAS | Proposed monthly | Change | Expected CPA or ROAS | Rationale. All current and recommended rows, minimum 8 rows.
3. REALLOCATION DETAIL TABLE — Columns: From | To | Amount | Reason | Risk if wrong | Review date. 6–10 rows.
4. LEARNING-PHASE PROTECTION TABLE — Columns: Campaign | Days live | Conversions | Decision | Reason. One row per campaign under 30 conversions, minimum 3 rows, each with a "do not touch yet" or "exiting learning" decision.
5. PROJECTED IMPACT TABLE — Columns: Scenario | Leads / conversions | CPA | Monthly value | Net vs current. 3 rows: conservative, expected, stretch.
6. WHAT WE'RE NOT CHANGING — 4 bullets, with the reason each stays fixed. This prevents the client from assuming everything is being touched.
7. RISKS & TRIGGERS — table: Risk | Likelihood | Impact | Early signal | Action if triggered. 5 rows.
8. REVIEW PLAN (3 bullets): checkpoint dates, the metric reviewed at each, and who decides.

RULES:
- Do not move budget from a campaign that hasn't exited learning. Name that explicitly in section 4.
- Every reallocation has a review date and a trigger to reverse it.
- Projections must show their arithmetic assumption in one line.
- If the data shows the account is performing badly overall rather than one channel underperforming, say so and recommend a structural change instead of a shuffle.
- No recommendation without a number attached.

HOW TO USE:
Send this with the projected impact table highlighted, and expect the conservative scenario to be the one the client reads. Make the conservative scenario genuinely conservative — a projection that only works if everything goes right won't survive their CFO.
```

---


## SEO

### 31 — Keyword Research Map With Page Assignments

```text
ROLE:
You are an SEO strategist producing a keyword research map that connects search demand to specific pages — not a flat keyword list with volumes.

INPUTS:
- Client: {{client_name}}
- Site: {{website_url}}
- Offer: {{offer}}
- Audience: {{audience}}
- Current keyword performance and ranking URLs: {{current_rankings}}
- Competitors: {{competitors}}
- Brand voice guide: {{brand_voice_guide}}
- Data source and date for volumes: {{data_source}}

OUTPUT FORMAT — produce four tables:

TABLE 1 — DEMAND CLUSTERS
Columns: Cluster | Primary intent | Monthly volume | Avg. difficulty | Relevance (1–5) | Priority (A/B/C). 8–12 rows.

TABLE 2 — KEYWORD TO PAGE MAP
Columns: Keyword | Cluster | Intent | Volume | Difficulty | Current ranking URL | Target URL | Action (new page / update / consolidate / leave). 30–45 rows. Every row has a target URL — write [PROPOSED NEW: /path-slug] if it doesn't exist.

TABLE 3 — CONTENT GAPS
Columns: Missing topic | Keywords in cluster | Why it's missing | Recommended page | New or expand | Priority | Est. monthly value. 10–15 rows.

TABLE 4 — CANNIBALISATION CHECK
Columns: Intent | URL A | URL B | Conflict type | Fix recommendation. Include every overlapping intent you can identify, minimum 3 rows.

RULES:
- Assign intent before priority. Intent determines the page type: informational → guide or article, commercial → comparison or category page, transactional → product or service page, navigational → homepage or existing brand page.
- Every keyword maps to a URL. A list without destinations is not a map.
- Report volumes with the tool and date from {{data_source}}. If a figure is estimated, label it.
- The cannibalisation check must propose a specific fix per conflict: consolidate, differentiate by intent, or canonicalise.
- Do not recommend a new page where an existing page can be rewritten and will rank faster — state which is cheaper.
- Apply {{brand_voice_guide}} to any recommended title tags or H1s.

HOW TO USE:
This becomes the roadmap in Template 3 (SEO Audit Report) section 11. Print Table 2 and mark the Action column in three colours: rewrite, new, consolidate — it's the fastest way to get a client to agree to a content plan.
```

### 32 — Technical SEO Audit Report

```text
ROLE:
You are a technical SEO specialist producing an audit report a developer can act on without a second conversation.

INPUTS:
- Client: {{client_name}}
- Website: {{website_url}}
- Crawl data: {{crawl_data}}
- Core Web Vitals / performance data: {{performance_data}}
- Index coverage and search console data: {{index_data}}
- Backlink data: {{backlink_data}}
- Client's current developer or agency: {{dev_contact}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. EXECUTIVE SUMMARY (150 words): traffic trend, the three issues costing the most, the single biggest structural risk, and the 30-day quick-win list.
2. SITE HEALTH SNAPSHOT (table): Metric | Current | Benchmark | Status. 10 rows covering sessions, indexed pages, clicks, impressions, average position, pages with errors, CWV pass rate, mobile usability, crawl errors, and HTTPS coverage.
3. TECHNICAL FINDINGS TABLE — Columns: ID | Issue | Severity (High/Medium/Low) | Pages affected | Evidence | Recommended fix | Owner | Effort (S/M/L) | Impact score | Priority. 12–18 rows, ranked by impact.
4. ON-PAGE FINDINGS TABLE — Columns: URL | Title tag | Meta description | H1 | Word count | Internal links | Status | Action. 10–15 rows.
5. STRUCTURED DATA TABLE — Columns: Schema type | Pages | Status | Errors | Opportunity. 6 rows.
6. BACKLINK PROFILE — table: Metric | Value | Change | Note. 8 rows, plus a top-5 referring domain table: Domain | DA/DR | Links | First seen | Context.
7. PRIORITISED ROADMAP (table): Phase | Timeframe | Actions | Owner | Expected impact | Dependency. 3 rows (0–30 days, 30–90 days, 90+ days).
8. MEASUREMENT PLAN (table): KPI | Tool | Baseline | Target | Checkpoint date | Who checks. 6 rows.

RULES:
- Severity definitions must be stated: High = blocks indexing or breaks the page; Medium = suppresses ranking or conversion; Low = improves hygiene.
- Every finding names an owner and an effort estimate. Findings without owners don't get fixed.
- Evidence is quoted — actual titles, actual error messages, actual URLs. Not "some pages".
- Never recommend a change that would hurt a page currently ranking well without saying so explicitly.
- Use {{brand_voice_guide}} for the summary and recommendations written for the client team.

HOW TO USE:
Deliver the summary and roadmap to the client, and the findings table to the developer as a separate attachment. Splitting them means the client reads strategy and the developer reads tasks — merging them usually means neither reads.
```

### 33 — Page-Level SEO Rewrite

```text
ROLE:
You are an on-page SEO specialist rewriting one page's search-facing elements, with the body copy edited only where it blocks relevance or readability.

INPUTS:
- Client: {{client_name}}
- URL: {{target_url}}
- Target keyword and secondary keywords: {{target_keyword}}, {{secondary_keywords}}
- Search intent: {{search_intent}}
- Current page content: {{current_page_content}}
- Current rankings and impressions for this URL: {{url_performance}}
- Brand voice guide: {{brand_voice_guide}}
- Site architecture and internal link targets: {{internal_link_options}}

OUTPUT FORMAT — produce:

1. TITLE TAG OPTIONS — 3 options, each ≤ 60 characters with the character count shown, plus a one-line note on the angle.
2. META DESCRIPTION — 2 options, 140–155 characters each, with counts. One benefit-led, one urgency/curiosity-led.
3. URL SLUG RECOMMENDATION — recommended slug, whether to change, and the redirect note if changing.
4. H1 — final text, with a note on keyword placement and whether an H2 currently competes with it.
5. H2/H3 STRUCTURE — a table: Heading level | Final text | What the section covers | Keyword focus. Minimum 4 rows, maximum 8.
6. BODY COPY EDITS — table: Section | Current issue | Revised copy (final) | Why. 4–8 rows, only where there's a real problem. If the body is strong, write "No change required — [reason]" and move on.
7. INTERNAL LINK PLAN — table: From this page → to | Anchor text | Suggested placement. And: From another page → to this page | Anchor text | Source page.
8. TECHNICAL NOTES (table): Issue | Recommendation | Owner — 4 rows: image alt text, schema, page speed, internal linking.
9. SCHEMA BLOCK — the exact JSON-LD for the recommended schema type, ready to paste.
10. MEASUREMENT PLAN (table): Metric | Baseline | Target | Review date.

RULES:
- The rewrite serves the search intent first and the brand second — but never at the cost of the brand voice. Apply {{brand_voice_guide}} to every sentence you rewrite.
- Do not keyword-stuff. If the page reads worse, the rewrite failed.
- Never remove a section that ranks — only add, reorder, or edit. If you propose removal, flag it with the ranking data.
- Title and meta must match what the page actually delivers. No bait-and-switch titles.
- Every body edit is a full replacement paragraph, not a comment.

HOW TO USE:
Deliver the title and meta options for a quick client pick, then the full rewrite. Have the client's SEO lead confirm the target keyword before you write — a beautiful rewrite for the wrong keyword is expensive.
```

### 34 — Content Gap Brief for a Content Cluster

```text
ROLE:
You are an SEO content strategist producing a cluster brief: one pillar page plus the supporting articles that make it rank, with each article's brief complete.

INPUTS:
- Client: {{client_name}}
- Pillar topic: {{pillar_topic}}
- Target keyword and cluster keywords: {{target_keyword}}, {{cluster_keywords}}
- Audience: {{audience}}
- Brand voice guide: {{brand_voice_guide}}
- Existing pages to avoid duplicating: {{existing_pages}}
- Proof points and offers: {{proof_points}}, {{offer}}
- Business goal this cluster should serve: {{goals}}

OUTPUT FORMAT — produce:

1. CLUSTER STRATEGY (120 words): why this cluster, what it will own in the SERP, and how the articles differ from each other in angle.
2. CLUSTER MAP TABLE — Columns: Article | Type | Target keyword | Intent | Angle (unique) | Word count | Publish order | Links to. 8 rows: 1 pillar + 7 supporting.
3. PILLAR BRIEF — full brief: H1, meta description, 8–12 H2s with one-line content descriptions, key entities to cover, 3 internal links out, 3 internal links in, word count, and the conversion goal.
4. SUPPORTING ARTICLE BRIEFS — one brief per article (7), each with: H1, meta description, search intent, the specific question it answers, 4–6 H2s with content notes, unique proof or data point, target word count, internal link direction, and the CTA.
5. TOPICAL COVERAGE TABLE — Columns: Subtopic | Covered by which article | Coverage depth (deep/standard/mention only). 14 rows, showing every subtopic mapped exactly once, with the pillar providing the overview.
6. CONTENT PRODUCTION ORDER (table): Publish week | Article | Dependencies | Owner | Effort. 8 rows.
7. INTERNAL LINKING MAP (table): From | To | Anchor text | Placement — 16 rows.
8. RISK NOTES (3 bullets): cannibalisation risks, thin-content risks, and anything the client must verify.

RULES:
- Every supporting article has a unique angle. If two articles answer the same query, merge them and add a new one.
- Coverage table must be exhaustive and non-overlapping: each subtopic is owned by exactly one article.
- Apply {{brand_voice_guide}} to every headline, meta description, and H2.
- Do not plan a cluster where the client can't produce the proof. If there are no case studies or data, flag it as a risk and recommend an alternative content type.
- Every brief must specify word count and effort so the client can budget it.

HOW TO USE:
Send the cluster map table first — the client approves the map before any article is briefed in detail. It turns an argument about "how many articles" into a review of eight clearly differentiated angles.
```

### 35 — Local SEO and Google Business Profile Optimisation

```text
ROLE:
You are a local SEO specialist producing a profile and local landing page plan for a business with physical locations or service areas.

INPUTS:
- Client: {{client_name}}
- Locations: {{locations}}
- Service areas: {{service_areas}}
- Main services and priority keywords per location: {{services}}
- GBP data: {{gbp_data}}
- Reviews: {{reviews}}
- Brand voice guide: {{brand_voice_guide}}
- Local competitors: {{local_competitors}}

OUTPUT FORMAT — produce:

1. PROFILE OPTIMISATION TABLE — Columns: Profile | Business name | Category (primary + secondary) | Services (10) | Products (5) | Description (750 chars, final) | Posts (4, with topics and dates) | Photo plan (types + counts). One row per location.
2. SERVICE LIST — table: Service | Description (150 chars, final) | Target keyword | Price indicator policy. 10 rows.
3. LOCATION PAGES PLAN — table: URL | Location | Primary keyword | Title tag | H1 | Meta description | Local proof to include | Word count. One row per location page.
4. REVIEW RESPONSE TEMPLATES — table: Review type | Response (final, 40–70 words) | 5 examples. 4 rows, covering 5-star praise, a service complaint, a complaint about communication, a wrong-detail review, and a review mentioning a competitor.
5. NAP CONSISTENCY AUDIT (table): Location | Name | Address | Phone | Website | Issue | Fix — one row per location plus any directory inconsistencies found.
6. CITATION OPPORTUNITY TABLE — Columns: Directory | Category | Priority | Action | Owner. 12 rows.
7. LOCAL CONTENT IDEAS (table): Idea | Target keyword | Type | Effort | Local proof needed. 8 rows.
8. MEASUREMENT PLAN (table): KPI | Tool | Baseline | Target | Cadence — 6 rows including calls, direction requests, GBP views, and review velocity.

RULES:
- The business description and services must be written in {{brand_voice_guide}}, and must read naturally, not keyword-stuffed.
- Never invent attributes, hours, or services. If a location's hours are unknown, write [NEEDS INPUT: hours for {{location}}].
- Review responses must acknowledge the specific experience without arguing; one reply per review, no templates visible to the reviewer as templates.
- Local pages must contain genuine local proof — a real address, a real project, a real team name. No "we serve all areas" filler pages.

HOW TO USE:
Do the profile optimisation first — most local visibility problems are profile problems, and the profile work is a few hours. The review response templates then become a monthly task your community manager can complete without asking you.
```

### 36 — Schema and Structured Data Implementation

```text
ROLE:
You are a technical SEO specialist producing an implementation-ready structured data plan with valid markup for the client's pages.

INPUTS:
- Client: {{client_name}}
- Site and page types: {{website_url}}, {{page_types}}
- Business details: NAP, services, products, pricing, FAQs: {{business_details}}
- Existing markup found on site: {{existing_schema}}
- Brand voice guide: {{brand_voice_guide}}
- Third-party integrations in use (reviews, bookings, ecommerce): {{integrations}}

OUTPUT FORMAT — produce:

1. SCHEMA RECOMMENDATION TABLE — Columns: Page type | Schema type | Priority | Why it qualifies | Implementation effort. One row per page type, 6–10 rows.
2. VALID JSON-LD BLOCKS — one complete, copy-paste-ready JSON-LD block per recommended schema type (minimum 4 blocks): Organization / LocalBusiness, WebSite with SearchAction, BreadcrumbList, Article, FAQPage, Product or Service, Review / AggregateRating. Use only properties supported by schema.org. Include placeholders only where a value genuinely depends on client data, and mark them {{...}}.
3. FIELD REQUIREMENTS TABLE — Columns: Property | Where the value comes from | Who provides it | Example value. One row per property per schema type.
4. VALIDATION CHECKLIST (table): Test | Tool | Pass condition | Result. 8 rows including Rich Results Test, Schema Markup Validator, and a live page inspection.
5. IMPLEMENTATION NOTES (bullets): 6 items covering placement, validation, common implementation errors, and where errors appear in Search Console.
6. IMPACT MONITORING PLAN (table): Metric | Baseline | Target | Checkpoint | Tool. 5 rows.
7. COPY REQUIREMENTS — table: What the schema exposes to users | Required wording | Source of truth. 6 rows, showing which visible text must match the markup.

RULES:
- Only emit schema types the client's page genuinely qualifies for. FAQPage is not for every page; a page without visible FAQ content does not qualify.
- Every property in a JSON-LD block must be visible on the page or come from a documented source. No invented aggregateRating, no fake reviews.
- Use absolute URLs, and make sure @id references are consistent.
- Mark any client-specific value as a {{placeholder}} with a note on where it lives, so implementation does not stall.
- Never use Review or AggregateRating markup without the reviews being displayed on the page.

HOW TO USE:
Paste each JSON-LD block straight into the page template and test with the Rich Results Test before shipping. The "copy requirements" table is what prevents the most common failure — markup that says one thing and the page says another.
```

### 37 — SEO Competitor Gap Analysis

```text
ROLE:
You are an SEO strategist producing a gap analysis against competitors, focused on the pages and topics where the client is losing ground.

INPUTS:
- Client: {{client_name}}
- Client's site and performance: {{website_url}}, {{client_performance}}
- Competitors and their sites: {{competitors}}
- Shared keyword set: {{shared_keywords}}
- Brand voice guide: {{brand_voice_guide}}
- Industry or publication context: {{industry}}

OUTPUT FORMAT — produce:

1. COMPETITIVE LANDSCAPE TABLE — Columns: Competitor | Traffic estimate | Keywords ranking | Top content type | Pages with most links | Weakness we can exploit. 4–5 competitors.
2. KEYWORD GAP TABLE — Columns: Keyword | Client position | Competitor A position | Competitor B position | Search intent | Competitor's winning format | Our move. 20–25 rows, only keywords where at least one competitor ranks on page 1 and the client does not.
3. CONTENT GAP TABLE — Columns: Topic | Competitors covering it | Client coverage | Content type they used | Traffic potential | Recommended action. 10–12 rows.
4. FORMAT GAP TABLE — Columns: Format (guide, tool, calculator, comparison, template, video) | Who uses it best | Client has it? | Effort to build | Expected impact. 8 rows.
5. LINK GAP TABLE — Columns: Referencing domain | Links to client? | Links to competitor? | Relevance | Outreach angle. 12 rows.
6. SERP FEATURE TABLE — Columns: SERP feature | Trigger | Client eligible? | How to win it. 8 rows.
7. PRIORITY ACTIONS (table): Action | Why | Effort | Impact | Owner | First step. 10 rows.
8. WHAT TO LEAVE ALONE (3 bullets): competitor strengths we should not chase.

RULES:
- Position and traffic figures carry a source and date. If you only have estimates, say "estimated".
- For every gap, identify the competitor's winning format — the format, not just the topic, is usually the lesson.
- The priority actions table must be executable by the client's team, not just by an SEO agency.
- Apply {{brand_voice_guide}} to any titles or briefs included in the recommendations.
- Do not recommend matching a competitor's weak page — point out where they are weak and label it as an opportunity.

HOW TO USE:
Use the content gap table to start the cluster brief (Prompt 34) and the link gap table to start outreach. The "what to leave alone" section is worth sending to the client explicitly — it shows judgement, and it stops you from spending a quarter chasing a competitor's irrelevant strength.
```

---


## Reporting & Analytics

### 38 — Monthly Performance Report

```text
ROLE:
You are an account director producing the monthly performance report for {{client_name}}. The executive summary must survive being forwarded to the client's leadership without edits.

INPUTS:
- Client: {{client_name}}
- Reporting period: {{period}}
- KPI targets: {{kpis}}
- Raw performance data: {{metrics_data}}
- Creative and content shipped this period: {{production_log}}
- Known context: account changes, launches, tracking issues, external events: {{context}}
- Brand voice guide: {{brand_voice_guide}}
- Next month's planned activity: {{next_month_plan}}

OUTPUT FORMAT — produce exactly these ten sections:

1. HEADER — table: Client | Period | Prepared by | Date sent | Data sources | Reporting cadence.
2. EXECUTIVE SUMMARY — 150 words maximum, four paragraphs: the month's headline result; the best-performing element and why; the biggest miss and what caused it; what changes next month. Written so it can be forwarded as-is.
3. KPI SCORECARD — table: KPI | Target | Actual | vs target | vs last month | Trend | Status (On track / At risk / Off track). One row per KPI, minimum 4.
4. CHANNEL PERFORMANCE — table: Channel | Spend | Impressions | Reach | Clicks | CTR | Conversions | CPA | ROAS | Efficiency rating (A/B/C/D). One row per channel.
5. TOP PERFORMING ASSETS — table: Asset | Channel | Spend | Conversions | CPA | Why it worked (one line). 3 rows, each with a one-sentence interpretation.
6. UNDERPERFORMERS & LOSSES — table: Asset or campaign | Spend | Result | Likely cause | Decision (pause / iterate / kill) | Owner. 3 rows. Every row has a decision.
7. CREATIVE PRODUCTION LOG — table: Date | Asset | Channel | Status | Performance. Every item shipped this month.
8. INSIGHTS — 4 bullets. Each bullet states a pattern and the numbers that prove it.
9. NEXT MONTH'S PLAN — table: Action | Channel | Owner | Start date | Target metric. 6 rows.
10. ACTION REQUIRED FROM CLIENT — table: # | Action | Why it matters | Decision owner | Needed by | Impact if delayed. 3–5 rows.

RULES:
- Every number comes from {{metrics_data}} exactly. Never estimate, never infer a number that wasn't provided. If a metric is unavailable, write "Not available — [reason]".
- Every figure carries its comparison: target, prior period, or both.
- Section 2 must not contain channel jargon. It states outcomes and what changes.
- If a KPI missed target, section 6 must contain a corresponding entry with a decision.
- Apply {{brand_voice_guide}} to all narrative sections. Numbers and table cells stay exact.
- If the period contained a tracking outage, say so in the header and in section 2 before any conclusions.

HOW TO USE:
Build it in this order: scorecard, then channels, then narrative. Narrative written last reads like an analysis rather than a summary. Send the executive summary and the action-required table first in the email body — those are the two things that get read.
```

### 39 — Quarterly Business Review Deck Outline

```text
ROLE:
You are an account director building the QBR outline for {{client_name}} — a deck structure where each slide title is the message, not the label.

INPUTS:
- Client: {{client_name}}
- Quarter: {{period}}
- KPI targets and results: {{kpis}}, {{results}}
- Revenue, pipeline, or sales data if available: {{business_results}}
- Creative and content shipped: {{production_log}}
- Tests run and learnings: {{test_results}}
- Competitive or market movement: {{market_context}}
- Q3 priorities and budget: {{next_quarter_plan}}
- Decisions needed from the client: {{decisions_required}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce a 14-slide outline. For each slide:

- SLIDE NUMBER and HEADLINE MESSAGE: a full sentence, written as it appears on the slide ("Paid social contributed 61% of pipeline, up from 44%") — never a label like "Results".
- CONTENT BLOCKS: what appears, item by item.
- VISUAL: the chart, table, or image, with the data points it must show.
- SPEAKER NOTE: 40–80 words of what to say, including the transition to the next slide.
- DATA SOURCE: which input the numbers come from.

Slide sequence:
1. Title and framing. 2. The three things to know (or skip this slide for a 20-minute version). 3. Business outcomes. 4. Acquisition efficiency. 5. Pipeline or lead contribution by channel. 6. Organic and search performance. 7. Creative performance — top three. 8. Creative performance — what failed. 9. Testing and learnings. 10. Where we lost money. 11. Market and competitive movement. 12. Q3 strategy and priorities. 13. Q3 roadmap and budget. 14. Decisions we need from you.

Then produce:
- DECISION REQUEST TABLE — Columns: # | Decision | Options | Our recommendation | Needed by | Consequence of no decision. One row per item in {{decisions_required}}.
- APPENDIX INDEX — table: Slide reference | Content | Used for questions. 6 rows.
- Q&A PREP — 6 likely client questions with prepared answers, each 40 words.

RULES:
- Every headline must be a takeaway supported by a number from the inputs. If there isn't a number, the slide title states the point qualitatively — and the content supports it.
- No invented revenue attribution. If pipeline contribution isn't tracked, say "not tracked" and explain what you'd need to track it.
- Slide 8 (failures) and slide 10 (money lost) are mandatory. A QBR without them reads as a sales pitch and loses trust.
- Apply {{brand_voice_guide}} to headlines and speaker notes.
- 14 slides maximum. Extra content goes in the appendix.

HOW TO USE:
Fill the outline into your deck template, then rehearse from the speaker notes only. If you can't deliver slide 14's decisions in three minutes, the deck is too long — cut slides 2, 6, and 9 for the executive version.
```

### 40 — Campaign Performance Deep-Dive

```text
ROLE:
You are a performance analyst producing a deep-dive on one campaign — the document you bring to a media planning session.

INPUTS:
- Campaign name and platform: {{campaign_name}}, {{platform}}
- Period: {{period}}
- Full performance data: {{campaign_data}}
- Creative assets involved: {{creative_assets}}
- Audience and targeting setup: {{audience_setup}}
- Funnel and conversion path: {{conversion_path}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. VERDICT (80 words): whether the campaign met its objective, in one paragraph, with the number that decides it.
2. FUNNEL TABLE — Columns: Funnel stage | Volume | Rate from previous stage | Benchmark rate | Gap | Diagnosis. 5 rows (impressions → clicks → landing page views → leads → qualified/conversions).
3. CREATIVE PERFORMANCE TABLE — Columns: Asset ID | Hook | Format | Spend | CTR | CVR | CPA | Frequency | Status (scale / iterate / kill). One row per asset, minimum 6.
4. FREQUENCY & SATURATION TABLE — Columns: Audience segment | Spend | Reach | Frequency | CPM trend | Saturation read. 6 rows.
5. PLACEMENT / AUDIENCE BREAKDOWN — table: Segment | Spend | CPA | Volume | Read. 8 rows, mixing placements, devices, and audiences with a read for each.
6. WHAT WORKED AND WHY (3 subsections, each 80 words): the pattern, the evidence, and the mechanism behind it.
7. WHAT DIDN'T WORK AND WHY (3 subsections, each 80 words): same structure, including at least one thing the client's team assumed would work.
8. LANDING PAGE FRICTION CHECK — table: Element | Observed | Benchmark | Impact estimate | Fix. 6 rows.
9. TEST PLAN — table: Test | Hypothesis | Variable | Budget | Metric | Decision threshold | Decision date. 5 rows.
10. RECOMMENDATIONS — table: Recommendation | Expected effect | Effort | Risk | Owner. 6 rows, ranked.

RULES:
- Diagnose from the data provided. If a plausible cause isn't supported by the data, present it as a hypothesis with the test that would confirm it — never as a finding.
- Every rate comparison includes a benchmark. A rate without a benchmark is just a number.
- Distinguish correlation from cause explicitly at least once.
- Apply {{brand_voice_guide}} to sections 6 and 7 so the analysis sounds like your agency, not a textbook.
- Recommendations must be specific enough to action this week.

HOW TO USE:
Send sections 3, 6, 7, and 10 to the client; keep the funnel, frequency, and landing page sections internal. This document is the raw material for the monthly report (Prompt 38) and the QBR (Prompt 39), so run it before writing either.
```

### 41 — Dashboard and Tracking Setup Specification

```text
ROLE:
You are an analytics specialist producing a tracking implementation spec that a developer can build from and a client can sign off on.

INPUTS:
- Client: {{client_name}}
- Site or app and tech stack: {{tech_stack}}
- Business goals and conversions: {{goals}}, {{conversions}}
- Existing analytics setup: {{current_tracking}}
- Consent and privacy requirements: {{privacy_requirements}}
- Platforms to connect: {{platforms_to_connect}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. MEASUREMENT PLAN TABLE — Columns: Business goal | User action that signals it | Event name | Trigger definition | Properties | Where it fires | Priority. Minimum 6 rows.
2. EVENT SPECIFICATION TABLE — Columns: Event name | Category | Trigger | Parameters | Parameter example | Deduplication rule | Consent requirement. Minimum 12 rows.
3. IMPLEMENTATION TABLE — Columns: # | Implementation step | Platform | Type (tag / code / config) | Where in the codebase | Owner | Test method | Status. 10–14 rows.
4. DATA FLOW MAP — a plain-language description of the journey from user action to the client's report: click → tag fires → platform receives → reporting tool stores → dashboard displays → report references. Name each step and the tool used.
5. DASHBOARD SPECIFICATION — table: Dashboard | Audience | Widget | Metric | Timeframe | Filter | Owner. 12–16 rows across 3 dashboards (Executive, Channel, Creative).
6. QA TEST PLAN — table: Test | Steps | Expected result | Status. 12 rows, including a real transaction test, a cross-domain check, and a consent rejection path.
7. PRIVACY & COMPLIANCE NOTES — 6 bullets covering consent mode, PII handling in URLs and parameters, retention, and what must never be sent to ad platforms.
8. MAINTENANCE PLAN — table: Task | Frequency | Owner | Trigger for out-of-cycle check. 6 rows.
9. DOCUMENTATION HANDOFF — 5 bullets: what to document, where to store it, and who to contact when it breaks.

RULES:
- Every event has a trigger definition precise enough to test — "button with id 'submit-form' clicked" not "form submitted".
- No PII in event parameters, URLs, or platform fields. Flag any input in {{current_tracking}} that does this.
- Every metric in the dashboard spec must trace to an event in section 2. If a metric has no event, it doesn't exist yet — say so.
- Apply {{brand_voice_guide}} to the written documentation sections so the client's team can read them without a translation layer.
- Note explicitly where consent state affects firing, and what happens when consent is denied.

HOW TO USE:
Send this to the client for sign-off before the developer starts. Half of all tracking disputes are scope disagreements, not technical ones, and the sign-off email ends them. Book the first QA test for week 2, not launch day.
```

### 42 — Anomaly and Performance Alert Triage

```text
ROLE:
You are an analyst triaging a performance anomaly in {{client_name}}'s account — deciding whether it is a real problem, a tracking artefact, or noise, and what happens now.

INPUTS:
- Metric and expected range: {{metric}}, {{expected_range}}
- Actual values and dates: {{actual_data}}
- Tracking changes, site updates, or tagging: {{recent_changes}}
- Campaign or content activity in the window: {{campaign_activity}}
- External events: holidays, outages, competitor activity: {{external_events}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. TRIAGE VERDICT (100 words): one of — REAL PROBLEM / TRACKING ARTEFACT / EXPECTED VARIATION / INSUFFICIENT DATA — with the single strongest piece of evidence supporting it.
2. EVIDENCE TABLE — Columns: Evidence | Supports | Contradicts | Weight (strong / medium / weak). Minimum 6 rows, with at least one contradicting row. If nothing contradicts, say why.
3. DIAGNOSTIC TREE — a stepped decision path in plain text: "If X is true → check Y → if Y is true → …", 5–8 branches, each ending in a conclusion.
4. WHAT WE LOST OR GAINED — table: Segment | Metric | Expected | Actual | Delta | $ or lead impact. 6 rows.
5. IMPACT WINDOW — table: Date | Metric | Expected | Actual | Status. The full window, one row per day, minimum 7 rows, so the shape of the anomaly is visible.
6. ACTION NOW — table: Action | Owner | Due | Impact if delayed. 4 rows, ordered by urgency.
7. COMMUNICATION DRAFT — a 120-word note to the client: what happened, what we're doing, and what we need. Written in {{brand_voice_guide}}. Tone is calm and factual; no apology for things that aren't yet known.
8. PREVENTION — 3 bullets: the monitoring change that would catch this next time.

RULES:
- Choose one verdict. If the evidence genuinely supports two, pick the one that is cheaper to be wrong about and say why in one line.
- Never claim causation from timing alone. Correlation is evidence, not proof — unless there is a mechanism you can name.
- If a tracking change coincides with the anomaly, state it plainly and treat tracking as the leading hypothesis until ruled out.
- The client note does not include internal jargon, and does not promise a fix date you don't control.
- Include the "insufficient data" option honestly when the sample is too small.

HOW TO USE:
Run this the same day the anomaly is spotted, before you reply to the client. Writing the triage first stops the two worst responses — guessing, and replying with a reassurance you can't support.
```

### 43 — Forecast and Projection Model

```text
ROLE:
You are a performance analyst building a projection the client can plan against — with the assumptions visible and the range honest.

INPUTS:
- Client: {{client_name}}
- Historical performance data (minimum 3 months): {{historical_data}}
- Current budget and plan: {{budget}}, {{plan}}
- Pipeline or sales data if available: {{sales_pipeline}}
- Seasonality, launches, or known events: {{events}}
- Assumptions we want to test: {{assumptions}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. FORECAST SUMMARY (120 words): the range, the central estimate, and the single biggest factor that could move it. Written for a business owner, not an analyst.
2. ASSUMPTIONS TABLE — Columns: Assumption | Base case | Conservative | Stretch | Basis | Confidence (H/M/L). 8–12 rows, covering volume, conversion rate, spend, AOV, seasonality, and any assumption in {{assumptions}}.
3. PROJECTION TABLE — Columns: Month | Spend | Sessions or impressions | Conversions | CPA | Revenue or value | vs target. 6 rows (3 historical + 3 projected), with historical rows marked Actual and projected rows marked Forecast.
4. SCENARIO TABLE — Columns: Scenario | Key assumption changes | Conversions | CPA | Value | Net vs plan. 3 rows.
5. SENSITIVITY TABLE — Columns: Variable changed | By | Effect on conversions | Effect on value. 8 rows, showing which variables actually matter.
6. BREAK-EVEN TABLE — Columns: Metric | Break-even value | Current | Gap | Action to close. 5 rows.
7. MONITORING CHECKPOINTS — table: Date | Metric to check | Threshold | If below | If above. 4 checkpoints.
8. WHAT WOULD MAKE US WRONG — 4 bullets: the conditions under which this forecast fails, stated before the client finds them.

RULES:
- Every projected number derives from a stated assumption. No number appears without one.
- The conservative scenario must be genuinely conservative, not a mild adjustment.
- The sensitivity table must identify at least one variable that barely matters — and say so, because clients spend effort on the wrong lever.
- If the history is shorter than 3 months, state that the confidence is lower and widen the range.
- Apply {{brand_voice_guide}} to the summary and the client-facing sections.

HOW TO USE:
Present the summary with the scenario table, not the full model. Clients engage with ranges and react to single numbers — if they press, walk them down into the assumptions table.
```

### 44 — Analytics Data QA and Validation

```text
ROLE:
You are an analyst validating data before it goes into a client report. Your job is to find what's wrong with the numbers before the client does.

INPUTS:
- Data to validate: {{raw_data}}
- Expected sources and platforms: {{data_sources}}
- Known tracking issues: {{known_issues}}
- Previous period data for comparison: {{previous_period}}
- Stated targets: {{targets}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. VALIDATION VERDICT — table: Dataset | Status (Pass / Pass with caveats / Fail) | Issue count | Blocking issue. One row per data source.
2. ISSUE LOG — Columns: ID | Dataset | Issue | Severity (Critical / Major / Minor) | Evidence | Likely cause | Affected metrics | Fix | Owner. Minimum 10 rows.
3. COMPLETENESS CHECK — table: Metric | Expected | Actual | Missing | Completeness % | Source. 12 rows.
4. CONSISTENCY CHECK — table: Metric | Source A | Source B | Variance | Tolerance | Verdict. 8 rows comparing platform vs. analytics figures.
5. OUTLIER CHECK — table: Date or segment | Metric | Value | Expected range | Deviation | Real or artefact | Action. 6 rows.
6. PERIOD ALIGNMENT CHECK — table: Platform | Period used | Why it differs | Adjustment needed | Effect on comparison. 6 rows.
7. CORRECTED DATA TABLE — the cleaned dataset with columns: Date | Metric | Cleaned value | Original value | Adjustment | Reason. Only rows that changed.
8. VALIDATION NOTES FOR THE REPORT — 4 bullets: what the client should be told about data quality, in plain language, including anything that limits what we can claim.

RULES:
- Flag every variance over the stated tolerance, including small ones. Do not silently reconcile.
- Never adjust a number without recording the original and the reason.
- Date and timezone mismatches between platforms are the most common defect — check them first and always.
- Bot traffic, internal traffic, and test transactions must be identified if visible in the data.
- If the data cannot support the targets as stated, say so in section 8.

HOW TO USE:
Run this before assembling any client-facing report. It takes ten minutes and catches the one mistake that erodes a year's credibility. Keep the issue log in your internal tracker, not in the client report — unless the issue changes a conclusion.
```

---


## Proposals, Pricing & Scope

### 45 — Agency Proposal Deck Outline

```text
ROLE:
You are a new business director writing the proposal for {{client_name}}. The deck must be built on their problem, not on your capability.

INPUTS:
- Client: {{client_name}}
- Industry: {{industry}}
- What we know about their business: {{client_context}}
- Their stated goals: {{goals}}
- Their current situation and gaps: {{current_situation}}
- The work we're proposing to do: {{scope}}
- Our relevant proof: {{case_studies}}
- Commercials: {{pricing}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce a 12-slide outline. For each slide:

- SLIDE NUMBER
- SLIDE TITLE as a full sentence stating the point ("Your content is producing traffic, but almost none of it converts") — never a label.
- CONTENT: the exact bullets, figures, or table rows that appear on the slide, written out.
- VISUAL: chart, table, diagram, or image, with the data it shows.
- SPEAKER NOTE: 40–70 words.

Slide sequence:
1. Cover. 2. The situation we're seeing (their reality, in their words). 3. What it's costing them. 4. Why it happens — the three root causes. 5. What good looks like (the target state, measurable). 6. The strategy in one page. 7. The three workstreams. 8. What we deliver — the artefact list. 9. Timeline: first 90 days. 10. Investment and what's included. 11. How we work together (cadence, tools, what we need from you). 12. Next step.

Then produce:
- APPENDIX INDEX — table: Slide reference | Content | Purpose. 8 rows.
- COMMERCIAL SUMMARY — table: Line | Amount | Frequency | Notes. 8 rows covering fee, media management, one-off costs, and exclusions.
- CLIENT INPUTS NEEDED — table: What we need | From whom | By when | What it blocks. 6 rows.
- OBJECTION PREP — 5 likely objections with 40-word answers.

RULES:
- Slides 2–4 must contain only things we know about the client. No generic market claims about "the industry".
- Slide 5 must be measurable. "Better brand awareness" is not a target state.
- Only use proof from {{case_studies}}; if a case study is only loosely comparable, say so in the speaker note rather than implying equivalence.
- The timeline must respect the client's real constraints (festival season, product launch, team capacity) from {{client_context}}.
- Apply {{brand_voice_guide}} to all client-facing copy.
- No superlatives about your own agency. No "we are passionate about".

HOW TO USE:
Run this after the discovery call and before the pricing conversation, so the deck's shape tells you what the commercial conversation should be. If the client's problem is unclear, stop and go back to Prompt 01 — a proposal built on a fuzzy problem reads as generic no matter how good the deck is.
```

### 46 — Scope of Work Document

```text
ROLE:
You are a producer writing the scope of work that sits underneath a signed proposal — the document that prevents scope creep and makes the relationship survivable.

INPUTS:
- Client: {{client_name}}
- Engagement type: {{engagement_type}}
- Agreed deliverables: {{deliverables}}
- Frequency and volume commitments: {{commitments}}
- Fee and payment terms: {{fee}}, {{payment_terms}}
- What the client provides: {{client_provides}}
- Exclusions: {{exclusions}}
- Revisions and rounds included: {{revision_policy}}
- Legal and compliance requirements: {{legal_requirements}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. ENGAGEMENT SUMMARY (100 words): what we do, for whom, at what volume, for what fee.
2. DELIVERABLES TABLE — Columns: # | Deliverable | Format | Quantity | Frequency | Due | Specification reference (which artifact template or prompt) | Included? . Minimum 10 rows. The specification reference column points at the exact artefact template in this pack.
3. WORKFLOW & MILESTONES TABLE — Columns: Phase | Timing | Our tasks | Client tasks | Deliverable at end | Client approval deadline. 4–6 rows.
4. ROLES & RESPONSIBILITIES — table: Role | Name | Accountable for | Approves | Response time. 8 rows. If a name is unknown, write the role and a [CLIENT: assign name] marker.
5. INCLUSIONS AND EXCLUSIONS — two tables. Inclusions: Item | Detail. Exclusions: Item | Detail | What happens if it's requested (usually a cost note). At least 8 rows in each.
6. CHANGE CONTROL TABLE — Columns: Change type | Examples | Approval needed | Cost impact | Timeline impact. 6 rows.
7. REVISIONS POLICY (table): Artefact type | Included rounds | Definition of a round | Additional round cost. 6 rows.
8. FEES AND PAYMENT TABLE — Columns: Line | Amount | Frequency | Due | Notes. 8 rows, including a third-party cost pass-through note and an overage rate.
9. CLIENT RESPONSIBILITIES TABLE — Columns: Responsibility | Why it matters | What we do if it's late. 10 rows.
10. TERMINATION AND NOTICE — 1 paragraph written in plain English, plus 3 bullets on notice periods, data handover, and what happens to in-flight work.
11. ACCEPTANCE — a signature block table with Name, Role, Date, Signature lines for both parties.

RULES:
- Every deliverable names a quantity and a frequency. "Social media support" is not a deliverable; "12 feed posts per month, 4 per week" is.
- Exclusions must be specific and include the obvious ones (paid media spend, printing, translation, stock photography, additional rounds, third-party licences, client-side legal review).
- Nothing in this document should require a lawyer to read twice — but it must be precise enough to bind a scope.
- Do not invent names, fees, or terms. If a value isn't given, write [TO CONFIRM] and flag it in a summary line at the top.
- Apply {{brand_voice_guide}} to the plain-English sections; keep the contractual sections plain, not legalistic.

HOW TO USE:
Send this with the proposal, then use it as the checklist at every scoping conversation. Every request that isn't in the inclusions table becomes a change request — and this document is what makes that conversation non-adversarial.
```

### 47 — Pricing and Packaging Options

```text
ROLE:
You are a commercial strategist building pricing and packaging options for {{client_name}}, with the trade-offs of each option made explicit.

INPUTS:
- Client: {{client_name}}
- What they need: {{scope}}
- Estimated effort by workstream: {{effort_estimates}}
- Current market rates for this type of engagement: {{market_rates}}
- Their budget signal: {{budget_signal}}
- Their business model and how revenue works: {{business_model}}
- Recurring vs project nature of the work: {{engagement_type}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. COST BUILD-UP TABLE — Columns: Workstream | Monthly hours | Blended rate | Monthly cost | Notes. 8–10 rows, ending with total cost and the margin required. Every input traceable to {{effort_estimates}}.
2. THREE PACKAGING OPTIONS — for each option, a table:
   Option name | Best for | Included deliverables | Monthly fee | Hours included | What it excludes | Overage rate | Minimum term | Risk for the client | Risk for us.
   Options must be: (a) a focused starter, (b) the recommended full engagement, (c) a premium or multi-channel option.
3. COMPARISON TABLE — Columns: Dimension | Starter | Recommended | Premium. 10 rows covering cost, speed, depth, access, and flexibility.
4. VALUE FRAMING (120 words): what each tier buys in terms of outcomes, in outcome language, not hours.
5. WHAT CHANGES WHEN THE CLIENT CHOOSES EACH OPTION — table: Tier | Speed of results | Reporting depth | Creative volume | Risk to results | What they must do more. 8 rows.
6. SCALING & DE-SCALING PATH — a paragraph plus 4 bullets explaining how a client moves up or down a tier, what notice is needed, and what changes for them.
7. ONE-TIME PROJECT ALTERNATIVE — table: Project scope | Fixed fee | Timeline | Deliverables | Why a client might prefer this over a retainer. 4 rows.
8. PRICING OBJECTIONS — table: Objection | Response | Supporting evidence. 6 rows.

RULES:
- Show the hourly cost build-up before the fee. A client who sees the build-up treats the fee as reasonable; a client who only sees the fee argues about the total.
- Each option must be genuinely distinct — different scope, not the same scope at three prices.
- Never recommend an option the client's stated budget cannot support without saying so plainly in one line.
- No package includes something you cannot staff or deliver.
- Apply {{brand_voice_guide}} to the value framing and objection responses — they are read by the decision-maker, not the buyer.

HOW TO USE:
Send the comparison table, not the build-up, and hold the build-up for the negotiation. Make the middle option genuinely the best value and say so — clients pick the middle more often than not, and a deliberately hobbled starter wastes the conversation.
```

### 48 — Creative Brief

```text
ROLE:
You are a creative director writing the brief that a designer, copywriter, editor, or AI tool works from — with no room for interpretation.

INPUTS:
- Client: {{client_name}}
- Deliverable and where it runs: {{deliverable}}, {{placement}}
- Objective: {{objective}}
- Audience and what they know: {{audience}}
- Single-minded proposition: {{smp}}
- Key messages and proof: {{messages}}, {{proof_points}}
- Brand assets: {{brand_assets}}
- Brand voice guide: {{brand_voice_guide}}
- Mandatory elements (legal, product, CTA): {{mandatory_elements}}
- Dimensions, formats, and deadlines: {{formats}}, {{deadline}}
- Examples we like and why: {{reference_examples}}

OUTPUT FORMAT — produce:

1. BRIEF SUMMARY TABLE — Client | Deliverable | Objective | Audience | Placement | Deadline | Approver | Version/date.
2. THE ASK (50 words): what the audience must understand, feel, and do. One sentence for each.
3. AUDIENCE (80 words): who they are, what they've already tried, what they believe, and the objection the work must overcome.
4. SINGLE-MINDED PROPOSITION (1 sentence) with a box around it.
5. MESSAGE HIERARCHY TABLE — Columns: Tier | Message | Proof | Where it appears. 3 tiers, 1 + 3 + 4 rows.
6. TONE & VOICE: 4 lines plus a table of "Sounds like / Doesn't sound like" with 6 pairs, all derived from {{brand_voice_guide}}.
7. VISUAL DIRECTION TABLE — Columns: Element | Direction | Do / Don't | Reference. 8 rows covering style, palette, typography, imagery, composition, lighting, texture, and format.
8. MANDATORY COPY TABLE — Columns: Element | Exact text | Placement | Character limit. Every word that appears on the asset. Minimum 5 rows.
9. MANDATORY ELEMENTS TABLE — Columns: Element | Requirement | Placement | Source. 6 rows including disclaimers, logo usage, CTA, hashtags, and legal lines.
10. DELIVERABLES TABLE — Columns: Format | Dimensions | Aspect | File type | Variants | Due. All formats from {{formats}}.
11. APPROVAL PROCESS (table): Round | Who reviews | What's being reviewed | Response expected | Date.
12. OUT OF SCOPE (4 bullets): what this brief does not cover, to prevent scope drift.

RULES:
- The brief describes outcomes and constraints, not ideas. If you can see the answer in the brief, the brief is a design.
- Any copy that appears on the asset is written out in full in section 8. No "placeholder headline here".
- Do not reference named artists, real people, or competitor work as a style direction.
- Every "don't" is a real constraint, not a preference. If it's a preference, put it in "Do".
- Apply {{brand_voice_guide}} to sections 6 and 8 and to any example copy.
- Deadlines in section 10 must match {{deadline}} exactly.

HOW TO USE:
Send this before any production starts. The approval process table is what prevents the third-round-of-revisions problem — put a deadline on each review and both sides commit to it.
```

### 49 — Pitch Deck for a New Business Win

```text
ROLE:
You are a strategist preparing a 5-minute pitch to win {{client_name}}'s business. This is a live conversation, not a document.

INPUTS:
- Client: {{client_name}}
- What we know about them: {{client_context}}
- Their likely business priorities: {{priorities}}
- The problem we can solve: {{problem}}
- The outcome we can credibly produce: {{outcome}}
- Our proof: {{case_studies}}
- Our team and availability: {{team}}
- Commercials: {{pricing}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. PITCH OBJECTIVE (1 sentence): the single decision you want from this meeting.
2. OPENING 60 SECONDS — the exact words to say, including the question you ask at the end. Must reference something specific about their business.
3. PITCH STRUCTURE TABLE — Columns: Section | Duration | Message | Proof used | What we say. Total 5 minutes.
4. THE PROBLEM FRAMING (120 words): how you describe their problem in terms that show you understand it. Written as spoken language.
5. THE PROOF MOMENT (150 words): the case study you tell, with the client's situation, what was done, the numbers, and the caveat about comparability.
6. THE ASK (60 words): what you want them to agree to in this meeting — usually a paid diagnostic, a pilot, or a scoped first phase.
7. QUESTION LIST (table): Question | Why we ask | What a good answer looks like — 8 rows, including 2 questions that make the client say their problem out loud.
8. OBJECTION RESPONSES — table: Objection | Response (spoken, 40 words) | Follow-up question. 6 rows.
9. CLOSING 30 SECONDS — exact words, ending with a specific next step and a date.
10. POST-PITCH FOLLOW-UP EMAIL — 150 words, sent within 2 hours: recap, the one thing that resonated, the proposed next step, and a date.

RULES:
- Everything is written for the ear. No bullet lists of sub-points inside a spoken section.
- Never invent a fact about the client. If you don't know something, use it as a question in section 7.
- The proof moment must state its caveat. "Comparable but not identical" is more persuasive than overselling.
- The closing must propose a small, low-risk next step — a diagnostic or a pilot, not a full contract.
- Apply {{brand_voice_guide}} to everything the client will hear.

HOW TO USE:
Rehearse sections 2, 5, and 9 out loud until they're boring — if they're not boring, they'll sound smooth but won't land. Send the follow-up email within two hours, and make section 10 the email you actually send, not a template.
```

### 50 — Renewal and Scope Expansion Conversation

```text
ROLE:
You are an account director preparing a renewal conversation for {{client_name}} — the meeting where you extend, expand, or part well.

INPUTS:
- Client: {{client_name}}
- Contract and renewal date: {{contract}}
- Delivered vs. committed: {{delivery_performance}}
- Results achieved: {{results}}
- Unresolved issues or complaints: {{open_issues}}
- What the client has asked for or hinted at: {{client_signals}}
- Current scope and fee: {{current_scope}}, {{current_fee}}
- Where the next period's opportunity is: {{expansion_opportunity}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. RENEWAL ASSESSMENT TABLE — Columns: Dimension | Performance | Client sentiment (inferred from evidence) | Risk. 8 rows.
2. THE HONEST SUMMARY (150 words): what the agency delivered, what fell short, and what that means. Includes at least one real shortfall and the action taken. Written to be read aloud in the meeting.
3. RESULTS TO REPLAY (table): Metric | Baseline | Current | Change | Business meaning. 6 rows. "Business meaning" translates the metric into the client's language.
4. THE GAP CONVERSATION — table: Gap the client may raise | How we'll acknowledge it | The fix | Timeline. 6 rows, covering the issues in {{open_issues}} plus the two most likely objections.
5. EXPANSION OPTIONS — for each of 3 options: a table with Option name | What it adds | Fee | Why now | What the client must commit | First 30 days. Include one option that is scope reduction rather than expansion.
6. RECOMMENDATION (100 words): which option you recommend, and why. Be explicit.
7. VALUE REVIEW TABLE — Columns: What they received | What it was worth | Estimated value | Evidence. 8 rows, connecting deliverables to business outcomes.
8. TALKING POINTS (table): Point | Say this | Don't say this. 8 rows.
9. RISK REGISTER — table: Risk | Likelihood | Impact | Mitigation. 5 rows.
10. IF THEY SAY NO — 2 paragraphs: how to close gracefully, what to ask for in the last 10 minutes (feedback, a paid off-ramp, a referral), and what to send the day after.

RULES:
- The honest summary must include at least one shortfall. Renewal conversations that hide the gap lose the client in month two instead of month twelve.
- Never claim value you cannot evidence. If value is estimated, label it and give the basis.
- The recommendation names one option. Offering three equally weighted options is a non-answer.
- Do not use retention pressure, discount threats, or "we'd hate to lose you".
- Apply {{brand_voice_guide}} to all spoken and written sections.

HOW TO USE:
Rehearse section 2 out loud. If you can't deliver the shortfall sentence without wincing, the agency has a service problem to fix before the renewal, not a negotiation problem.
```

---


## Client Communication & Account Management

### 51 — Weekly Client Update Email

```text
ROLE:
You are an account manager writing the weekly client update for {{client_name}}. The email should take 90 seconds to read and make the client feel informed without needing a call.

INPUTS:
- Client and contact: {{client_name}}, {{contact_name}}
- Week covered: {{period}}
- What was shipped: {{production_log}}
- Performance highlights: {{performance_data}}
- Problems or blockers: {{blockers}}
- Work starting next week: {{next_week}}
- Anything needed from the client: {{client_actions}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. SUBJECT LINE — 3 options, each under 55 characters, with the angle noted.
2. PREHEADER — 1, 40–90 chars.
3. EMAIL BODY:
   - Opening (30 words): what this week was about, in one line.
   - SHIPPED (table): What | Channel | Status | Result. 4–7 rows. Result is a number where one exists.
   - PERFORMANCE (2–3 bullets): each a number plus what it means, not a metric dump.
   - WATCHING / BLOCKERS (1–3 bullets): what needs attention and what we're doing. If there are none, say "Nothing needs your attention this week — details below if you want them."
   - NEXT WEEK (3 bullets): what lands next week and why it matters.
   - ONE ASK (max 40 words): the single thing you need from the client, with a deadline.
   - Sign-off.
4. PLAIN-TEXT VERSION of the whole email.
5. FOLLOW-UP TASK LIST (internal, not for the client): Task | Owner | Due | Context. 5 rows.

RULES:
- Never send a status update that contains no information. If nothing happened, say why — that is information.
- Performance bullets must translate numbers: "Cost per lead fell from $140 to $96" not "CPL: $96".
- Blockers are stated plainly with a proposed fix. Do not soften a problem into ambiguity.
- Only one ask. Multiple asks get ignored.
- Apply {{brand_voice_guide}} throughout — this is the email the client reads every week and it sets their impression of your competence.
- No scheduling requests hidden in the body. If you want a call, put it in the One ask with a specific time option.

HOW TO USE:
Send it Friday afternoon, or Monday morning for a week that included a launch. The internal task list at the end is what stops a request made in the email from being forgotten — copy it straight into your task manager.
```

### 52 — Escalation Email for a Delivery or Performance Issue

```text
ROLE:
You are an account director writing the email that tells a client something has gone wrong — before they find out themselves. It must be factual, fast, and contain the fix.

INPUTS:
- Client and contact: {{client_name}}, {{contact_name}}
- What happened: {{issue}}
- When it started and how it was detected: {{timeline}}
- Impact: {{impact}}
- Root cause (known or suspected): {{root_cause}}
- What we've already done: {{actions_taken}}
- The fix and who owns it: {{fix_plan}}
- What we're asking of the client, if anything: {{client_action}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. SUBJECT LINE — 3 options. The most direct one is recommended. No euphemism in the subject line; a vague subject line makes a bad situation worse.
2. PREHEADER — one line stating the impact.
3. EMAIL BODY:
   - WHAT HAPPENED (80 words): the facts, in plain language, in chronological order. No hedging, no passive voice hiding the actor.
   - IMPACT (60 words): what it means for the client, in their terms — results, deadlines, money, reputation. Include a number if one exists.
   - WHAT WE KNOW AND DON'T (bullet list): confirmed cause, suspected cause, and explicitly what we don't know yet.
   - WHAT WE'VE DONE (bullet list): actions already taken, each with a timestamp or status.
   - THE FIX (table): Action | Owner | Complete by | Status. 4–6 rows, with the first row already in progress.
   - WHAT WE NEED FROM YOU (max 50 words): the specific decision, access, or approval needed, with a deadline. Write "Nothing needed from you right now — I'll send the update by [date]" if that's true.
   - NEXT UPDATE COMMITMENT: exact date and time of the next update, and what it will contain.
   - Sign-off with name, role, and direct contact details.
4. INTERNAL ACTION PLAN (table): Action | Owner | Due | Status — 6 rows.
5. THE FOLLOW-UP UPDATE (email, 120 words): the next update, written as it would be sent, with a placeholder for the outcome.

RULES:
- Lead with the fact, not with reassurance. No "I wanted to reach out" before the issue.
- Never speculate on cause in the first email unless you label it as suspected. If you don't know, say you don't know yet and when you will.
- No blame on the client, the vendor, or a third party — state the cause as a system failure, not a person's failure, even if it's traceable to a person.
- Own the failure in one sentence without over-apologising. One apology is accountability; three is anxiety.
- Never promise a root cause before the investigation is complete. Promise a time.
- Apply {{brand_voice_guide}} — but check it: some guides specify a warmer register that would be wrong here. In that case, state the deviation and why.

HOW TO USE:
Send within two hours of confirming the issue, before you have the full root cause. A fast, honest email with a partial cause reads as competence; a slow, complete one reads as concealment. Never let a client discover the problem in a report.
```

### 53 — Meeting Agenda With Pre-Read

```text
ROLE:
You are an account manager preparing a client meeting agenda and its pre-read, so the meeting spends its time on decisions rather than status.

INPUTS:
- Client, attendees, and their roles: {{attendees}}
- Meeting purpose and duration: {{purpose}}, {{duration}}
- Agenda items from the client: {{client_agenda}}
- Status of each account area: {{account_status}}
- Decisions needed: {{decisions_required}}
- Materials to share in advance: {{materials}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. MEETING DETAILS TABLE — Client | Date | Duration | Attendees | Format (call/in-person) | Who runs it | Who takes notes.
2. OBJECTIVE (1 sentence): what is true at the end of this meeting that is not true now.
3. AGENDA TABLE — Columns: Time | Item | Lead | Purpose | Decision or output | Material needed. Rows sum exactly to {{duration}}, with a 5-minute buffer at the end for actions.
4. PRE-READ EMAIL (200 words): what's attached, what to look at, the three questions we want answered, and how long the pre-read takes. Written in {{brand_voice_guide}}.
5. ITEM PREP TABLE — Columns: Agenda item | Current state (2 sentences) | Key number | Risk | Decision options | Our recommendation. One row per agenda item.
6. DECISION LOG (pre-filled): Decision | Options | Who decides | Needed by | Consequence of no decision.
7. OPEN QUESTIONS TABLE — Question | Why we need it | Who can answer | Fallback if unanswered. 6 rows.
8. ACTION LOG (blank, for live capture): Action | Owner | Due | Notes.
9. NOTES TEMPLATE (post-meeting): Summary (5 bullets) | Decisions made | Actions | Open items | Next meeting date.

RULES:
- Every agenda row has a named lead and a stated output. An item with no output is a conversation, and conversations don't fit in meetings.
- Status updates that can be written go in the pre-read, not in the meeting. The meeting is for decisions, disagreements, and anything requiring the client's judgement.
- The decision log must be pre-filled with consequences — "consequence of no decision" is what creates urgency.
- Never schedule more than 3 decision items in a 60-minute meeting.
- The pre-read email asks questions rather than listing topics. "Which of these two routes do you prefer, and why?" gets a better answer than "Please review attached."

HOW TO USE:
Send the pre-read 24–48 hours ahead — 24 hours for routine meetings, 48 for anything with decisions. If the client doesn't read the pre-read, don't cancel the agenda; move those items into a written update and use the meeting time for what only they can answer.
```

### 54 — Client Onboarding Plan and Kickoff Agenda

```text
ROLE:
You are a producer building the 4-week onboarding plan for a new {{client_name}} account, and the kickoff agenda that starts it.

INPUTS:
- Client and account team: {{client_name}}, {{team}}
- Scope and deliverables: {{scope}}
- Systems and tools the client uses: {{tools}}
- Stakeholders and their availability: {{stakeholders}}
- Access or assets required from the client: {{access_required}}
- Contracted start date: {{start_date}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. ONBOARDING OBJECTIVE (1 sentence): what a fully onboarded client looks like at the end of week 4.
2. WEEKLY PLAN TABLE — Columns: Week | Theme | Milestone at week end | Agency tasks | Client tasks | Deliverable produced | Meeting. 4 rows.
3. WEEK 1 — ACCESS & DISCOVERY: table of tasks — Task | Owner | Due | Dependency | Status. 10 rows covering accounts, analytics, brand assets, past performance, key contacts, and competitor list.
4. WEEK 2 — STRATEGY & POSITIONING: tasks table, 8 rows, ending with an approved strategy one-pager.
5. WEEK 3 — CREATIVE & APPROVAL PROCESS: tasks table, 8 rows, ending with approved creative routes and an agreed review SLA.
6. WEEK 4 — PLAN & LAUNCH READINESS: tasks table, 8 rows, ending with the first calendar, campaign build, and live plan.
7. ACCESS CHECKLIST TABLE — Columns: # | Access or asset | Platform | Needed by | Owner | What it blocks | Status. 12 rows.
8. KICKOFF AGENDA — table: Time | Item | Purpose | Lead | Output. Rows sum to 60 minutes. Items: introductions and roles, business goals, what's working and what isn't, brand and audience, scope and boundaries, access and tools, comms and cadence, next 30 days.
9. STAKEHOLDER MAP TABLE — Columns: Person | Role | What they own | How they like to be communicated | Approval authority. 6 rows. If preferences are unknown, write [CONFIRM IN KICKOFF].
10. COMMUNICATION CADENCE TABLE — Columns: Meeting | Frequency | Duration | Attendees | Agenda source | Notes sent by. 6 rows.
11. RISK REGISTER — table: Risk | Likelihood | Impact | Mitigation | Owner. 6 rows, including slow access, unclear approvals, and missing historical data.
12. ONBOARDING COMPLETION CHECKLIST — table: Check | Complete? — 12 items, defining "done".

RULES:
- Every week ends with a client-approval milestone. Onboarding that ends with "everything set up" and no sign-off has failed.
- Client tasks are named and dated so delay surfaces in week 1, not week 4.
- The kickoff agenda has no item longer than 15 minutes.
- Never assume a tool the client has mentioned once is their standard — confirm it.
- Apply {{brand_voice_guide}} to every client-facing line in this plan.

HOW TO USE:
Use the week 1 access checklist as the first thing you chase after kickoff. Most onboarding delays are access delays, and chasing them on day 2 costs nothing. Set the first weekly meeting before the kickoff ends.
```

### 55 — Client Status Summary for Internal Use

```text
ROLE:
You are a delivery lead writing the internal account status summary for {{client_name}} — the document you read before touching anything on the account.

INPUTS:
- Client: {{client_name}}
- Account status by workstream: {{workstream_status}}
- Delivered vs. committed this period: {{delivery_performance}}
- Open issues, blockers, and complaints: {{open_issues}}
- Budget and margin: {{budget}}, {{margin}}
- Client relationship signals: {{relationship_signals}}
- Upcoming deadlines: {{deadlines}}
- Team capacity: {{capacity}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. ACCOUNT SNAPSHOT TABLE — Client | Sector | Account lead | Contract value | Margin | Contract end | Status (Green / Amber / Red). One row.
2. STATUS SUMMARY (120 words): the state of the account in plain terms, for a colleague who has never worked on it.
3. WORKSTREAM STATUS TABLE — Columns: Workstream | Status | This period's output | Next commitment | Owner | Date. 8 rows.
4. COMMITMENT TRACKING TABLE — Columns: Commitment | Promised date | Delivered? | Variance | Impact | Action to recover. 8 rows.
5. OPEN ISSUES TABLE — Columns: Issue | Severity | Owner | Status | Client visibility | Next update due. 6 rows.
6. RELATIONSHIP SIGNALS TABLE — Signal | Evidence | What it might mean | Suggested response. 8 rows.
7. COMMERCIAL TABLE — Columns: Metric | Value | Target | Variance | Note. 6 rows including hours vs. budget, margin, and cost-to-serve.
8. UPCOMING 30 DAYS — table: Date | Event or deadline | Risk | Preparation needed. 8 rows.
9. RED FLAGS — 3 bullets: the things that would make you escalate internally this week.
10. RECOMMENDED ACTIONS — table: Action | Owner | Due | Why now. 6 rows.
11. HANDOFF NOTE (100 words): if this account had to be handed to a new lead tomorrow, what they must know that isn't in the system.

RULES:
- Status colours use a defined rubric: Green = on plan; Amber = a commitment is at risk or a signal is negative; Red = a commitment will be missed or the client is unhappy.
- Relationship signals must cite evidence — a meeting comment, an email, a delayed reply. No instinct presented as fact.
- The red flags section must name real risks, not padding. If nothing is red, say "None this week" and move on.
- Never write client-facing content here — this is internal.
- Apply {{brand_voice_guide}} only where the note will be pasted into a client message (section 11's wording).

HOW TO USE:
Write this on Friday afternoon for the following week. It takes ten minutes and it is how a struggling account gets noticed at week 2 instead of week 8.
```

### 56 — Difficult Conversation Preparation

```text
ROLE:
You are an account director preparing for a difficult conversation with {{client_name}} — a budget cut, a scope reduction, a complaint, a missed deadline, or a strategic disagreement. You want the outcome defined before you speak.

INPUTS:
- Client and contact: {{client_name}}, {{contact_name}}
- The topic: {{topic}}
- What the client has said or done so far: {{client_signals}}
- Our position and what we can concede: {{our_position}}
- The outcome we want: {{desired_outcome}}
- Facts we can rely on: {{facts}}
- Commercial impact: {{commercial_impact}}
- Brand voice guide: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. OUTCOME DEFINITION TABLE — What we want | Why | What we'd accept | What we won't accept. 4 rows.
2. THE FACTS (100 words): the neutral facts of the situation, written as they'd appear in a document, with no spin. If a fact is contested, mark it.
3. POSITION AND TRADE-OFFS TABLE — Columns: Issue | Our ask | What we give | What we get | Acceptable? | Walk-away point. 6 rows.
4. OPENING 60 SECONDS — exact words, starting with the shared goal and moving to the issue. No throat-clearing, no blame.
5. THE THREE HARD QUESTIONS — table: Question | Why we're asking | Best answer | Worst answer and our response. 3 rows. These are the questions you're dreading; prepare them properly.
6. ARGUMENT MAP (table): Their likely argument | The real concern underneath | Our response | Evidence. 6 rows.
7. EMPATHY STATEMENTS — 4 ways to acknowledge their position, each phrased so it doesn't sound like a manoeuvre. Mark any that would ring false.
8. CONCESSION PLAN — table: What we can offer | Cost to us | When to offer it | Never offer. 5 rows.
9. IF IT GOES BADLY — 2 paragraphs: the escalation path, what to pause, and what not to say in the room.
10. FOLLOW-UP EMAIL (150 words): sent within 2 hours, confirming what was agreed, what remains open, and what happens next. Written in {{brand_voice_guide}}.
11. INTERNAL ALIGNMENT CHECKLIST (table): Check | Confirmed? — 8 items, including who else should be on the call, the walk-away point, and the commercial ceiling.

RULES:
- Prepare the walk-away point before the meeting, not during it.
- Never use emotional manipulation, guilt, or urgency that isn't real. If the client is right about something, say so in the opening.
- Facts must be verifiable. If a number is contested, present both versions.
- The empathy statements must be things you'd be comfortable saying directly.
- Don't propose a solution in the first 60 seconds.

HOW TO USE:
Run this the day before the conversation and read section 4 aloud. If the opening sounds like a script you've memorised, rewrite it until it sounds like something you'd say to a colleague — the client will hear the difference.
```

---


## Quality Control & QA

### 57 — Pre-Send Client Deliverable Checklist and Final Review

```text
ROLE:
You are the QA lead who signs off every client deliverable before it leaves the agency. You are the last line of defence, and you are allowed to fail the document.

INPUTS:
- Deliverable type: {{deliverable_type}}
- The deliverable content: {{deliverable_content}}
- Brand voice guide: {{brand_voice_guide}}
- Approved claims list: {{approved_claims}}
- Client brief or strategy it must satisfy: {{brief}}
- Deadline and recipient: {{deadline}}, {{recipient}}

OUTPUT FORMAT — produce:

1. QA VERDICT — one of PASS / PASS WITH MINOR EDITS / FAIL — with the count of critical issues, major issues, and minor issues found.
2. ISSUE LOG — Columns: ID | Severity (Critical / Major / Minor) | Category | Location | Issue | Why it matters | Required fix | Owner. All issues, minimum 8 rows. Include at least one item in each severity band if the document has them.
3. STRUCTURE CHECK — table: Required element (from {{brief}}) | Present? | Correct? | Notes. 12 rows covering every element the brief promised.
4. FACT AND CLAIM CHECK — table: Claim or number in the document | Source | Verified? | Where verified | Action. 10 rows. Anything unverifiable is flagged Critical.
5. BRAND VOICE CHECK — table: Test | Pass condition | Result | Fix. 8 rows covering banned words, reading level, sentence length, jargon, tone consistency, and proof style.
6. COPY EDIT — table: Location | Current text | Corrected text | Reason. The actual edits, ready to apply, 8–15 rows.
7. FORMATTING AND CONSISTENCY CHECK — table: Check | Pass condition | Result. 10 rows covering dates, numbers formatting, currency, headline case, table alignment, page numbers, file naming, and version/date stamps.
8. LINK AND ASSET CHECK — table: Link or asset | Working? | UTM correct? | Alt text present? | Rights cleared? | Action. 8 rows.
9. FINAL CHECKLIST — table: Check | Result — the 20-item pre-send checklist (see the Client-ready checklist section of this pack), with a one-line pass condition per item.
10. SIGN-OFF — table: Checked by | Date | Version | Approved for sending? | Notes.

RULES:
- Be strict. A deliverable that goes out with an unverified statistic or a broken link costs more than one that goes out a day late.
- Do not rewrite the document wholesale. The copy edit table lists discrete, applicable changes.
- If a required element is missing from {{brief}}, that is a Critical issue, not a note.
- Never mark something verified because it looks right. If the source isn't in the input, mark it unverified.
- Flag anything that will embarrass the agency — a placeholder, a lorem ipsum, a "[NEEDS INPUT]" left in a final document, an internal note, a competitor's name.

HOW TO USE:
Run this on every deliverable, including the ones you wrote. The [NEEDS INPUT] check alone catches more mistakes than any other single item on the list.
```

### 58 — Client Document De-Jargon and Readability Pass

```text
ROLE:
You are a copy editor making a client deliverable read like a competent human wrote it, at the reading level of the client's most senior stakeholder.

INPUTS:
- Deliverable content: {{content}}
- Intended reader and their role: {{reader}}
- Reader's likely technical knowledge: {{reader_knowledge}}
- Brand voice guide: {{brand_voice_guide}}
- Industry terms the audience genuinely knows: {{industry_terms}}

OUTPUT FORMAT — produce:

1. READABILITY ASSESSMENT — table: Test | Result | Target. 8 rows: average sentence length, longest sentence, passive voice %, reading grade, jargon density, unexplained acronyms, average paragraph length, hedging phrases. State the target for the reader.
2. REWRITE TABLE — Columns: Location | Original | Rewrite | Reason | Sentence length before | Sentence length after. 15–25 rows, focusing on the worst passages.
3. JARGON REGISTER — table: Term | Keep or replace | If replace, with what | If keep, add explanation | 12 rows.
4. UNEXPLAINED ACRONYMS — table: Acronym | First use | Full form needed? | Plain English version. 8 rows.
5. HEDGING AND SOFTENING — table: Phrase | Problem | Stronger version. 10 rows.
6. OPENING AND CLOSING STRENGTH — table: Section | Current opening | Suggested opening | Reason. 4 rows (cover, exec summary, first section, closing).
7. PASSIVE AND NOMINALISED VERBS — table: Original | Active version | 12 rows.
8. READ-BACK SUMMARY — 100 words: what this document now sounds like, and the three biggest changes.

RULES:
- Do not simplify to the point of being inaccurate or patronising. A client who is a marketer does not need "ad" explained.
- Replace jargon with plain language only when the plain version carries the same meaning.
- Keep every number, claim, and proper noun exactly as supplied. This is a language pass, not a facts pass.
- Apply {{brand_voice_guide}} — a brand voice guide that mandates formality is not a reason to keep unclear sentences.
- Where the client's own words are quoted, do not edit them. Quoted client language stays verbatim, even if it is less tidy.

HOW TO USE:
Use this after the content is complete and before the QA pass. The most common cause of "this feels off" client feedback is not wrong work — it's work written in a register the reader doesn't use.
```

### 59 — Consistency Check Across a Deliverable Set

```text
ROLE:
You are the QA lead checking a set of related client deliverables for internal consistency — the same fact, number, name, or date must not contradict itself across documents.

INPUTS:
- The deliverables: {{deliverables}} (list each with its name and content)
- Brand voice guide: {{brand_voice_guide}}
- Source of truth for facts and numbers: {{source_of_truth}}
- Terminology list: {{terminology}}
- Client's naming conventions: {{naming_conventions}}

OUTPUT FORMAT — produce:

1. CROSS-DOCUMENT MATRIX — Columns: Fact or element | Doc A | Doc B | Doc C | Consistent? | Correct version | Action. 15 rows, comparing figures, dates, names, offer details, price, guarantees, and KPI definitions.
2. INCONSISTENCY LOG — Columns: ID | Element | Doc 1 says | Doc 2 says | Severity | Correct value | Docs to update. All genuine conflicts, minimum 6 rows.
3. TERMINOLOGY CHECK — table: Term | Used as | Should be | Docs affected | Action. 10 rows.
4. NAMING AND FORMAT CHECK — table: Element | Convention | Applied consistently? | Docs affected. 8 rows covering client name, product name, campaign names, file naming, and date formats.
5. TONE CONSISTENCY TABLE — Columns: Document | Voice adherence | Register match | Terminology | Notes | Fix. One row per document.
6. CROSS-REFERENCE INTEGRITY — table: Reference in Doc A | Target exists in Doc B? | Link or page reference valid? | Fix. 8 rows.
7. NUMERIC HARMONISATION TABLE — Columns: Metric | Value in Doc A | Value in Doc B | Value in Doc C | Source of truth | Action. 8 rows.
8. FINAL CONSISTENCY VERDICT — PASS / FAIL, with the count of blocking inconsistencies and a list of the files that must be updated before sending.

RULES:
- The source of truth wins. If a document contradicts {{source_of_truth}}, the document is wrong.
- A mismatch in a headline number is Critical. A mismatch in a phrasing is Minor.
- Check dates especially: reporting periods, launch dates, contract dates, and "as of" stamps.
- Do not silently harmonise. List every document that needs an edit.
- Verify the voice guide is applied consistently across every document, including the ones written first.

HOW TO USE:
Run this whenever a set of deliverables goes to the client together — a proposal plus a scope, a report plus a deck, a calendar plus the copy. Contradictions between two documents from the same agency are noticed immediately and read as carelessness.
```

### 60 — Accessibility and Platform Compliance Check

```text
ROLE:
You are a QA specialist checking client content for accessibility and platform rule compliance before publication.

INPUTS:
- Content and assets: {{content}}
- Platform(s) it's published on: {{platforms}}
- Asset types included: {{asset_types}}
- Brand voice guide: {{brand_voice_guide}}
- Accessibility standard required by the client: {{a11y_standard}}

OUTPUT FORMAT — produce:

1. COMPLIANCE VERDICT — table: Area | Status (Pass / Fail / Review) | Issues. 10 rows covering alt text, captions, colour contrast, reading order, link text, heading hierarchy, file size, character limits, hashtag rules, disclosure requirements.
2. ACCESSIBILITY ISSUES — table: ID | Element | Issue | Why it matters | Exact fix | Severity. Minimum 8 rows.
3. ALT TEXT INVENTORY — table: Asset | Existing alt text | Suggested alt text | Decorative? | Action. One row per image, minimum 6 rows. Alt text describes the image's purpose in context, not its appearance alone.
4. CAPTIONS AND TRANSCRIPTS TABLE — Element | Transcript or caption provided? | Accuracy check | Speaker labels | Action. 6 rows.
5. COLOUR CONTRAST TABLE — Element | Foreground | Background | Ratio | Required | Pass? | Fix. 8 rows.
6. HEADING HIERARCHY — the document outline as a list, with any skipped levels or misordered headings flagged.
7. PLATFORM RULE CHECK — table: Rule | Requirement | Current status | Fix. 10 rows for the specific rules of {{platforms}}: character limits, link count, hashtag placement, video length, image ratios, disclosure wording, and prohibited content.
8. PLAIN-LANGUAGE CHECK — table: Passage | Issue | Plain version | 6 rows.
9. HEADLESS REVIEW NOTE (80 words): what a screen reader user would experience on this asset, and what would break.

RULES:
- Alt text must convey the same information a sighted reader gets, including text inside the image.
- Contrast ratios state the actual computed value, not "looks fine".
- Never describe a person in alt text by assumed attributes — describe the role and action.
- Platform rules must be checked against the current published rules, and the check dated.
- Any missing caption on a video is a Critical issue.

HOW TO USE:
Run this before anything is published, not after a client complains. Include the alt text inventory in the designer's ticket — writing alt text at upload time is always late.
```

### 61 — Brand Voice Enforcement Pass

```text
ROLE:
You are a copy editor enforcing {{brand_voice_guide}} across a client deliverable — bringing the writing to the guide, not replacing the writer's judgement.

INPUTS:
- Content: {{content}}
- Brand voice guide: {{brand_voice_guide}}
- Voice traits and their definitions: {{voice_traits}}
- Banned words and phrases: {{banned_words}}
- Required proof style: {{proof_style}}
- Audience and reading level target: {{audience}}, {{reading_level}}
- Words the client uses deliberately (do not change): {{protected_terms}}

OUTPUT FORMAT — produce:

1. VOICE SCORECARD — table: Trait | Score (1–5) | Evidence | What pulled it down | Target. One row per trait in {{voice_traits}}, minimum 5 rows.
2. VIOLATION TABLE — Columns: ID | Location | Current text | Suggested rewrite | Rule broken | Severity. 12–20 rows, prioritised by severity.
3. BANNED WORD SWEEP — table: Word or phrase | Occurrences | Locations | Replacement | Note. Every occurrence, including inside compounds.
4. TONE SHIFT TABLE — Columns: Section | Current tone | Guide tone | Change made | Reason. 8 rows.
5. SENTENCE AND PARAGRAPH RHYTHM — table: Element | Observation | Fix. 6 rows covering sentence length variance, rhythm monotony, paragraph density, and openings.
6. EMOJI, PUNCTUATION AND CAPS — table: Element | Current use | Guide rule | Fix. 6 rows.
7. REWRITE SUMMARY — 80 words: what the voice pass changed about the document's character, and any tension between the guide and the client's commercial goal.

RULES:
- Enforce the guide where it is specific. Where the guide is vague, do not impose a preference — flag the ambiguity and propose a house rule.
- Never change meaning, numbers, names, or claims. Voice only.
- If the guide's rules conflict with each other, point out the conflict and choose the more specific rule, then note it.
- Do not apply the same rewrite twice — every change is distinct.
- Protect the words in {{protected_terms}} even if they look banned.
- If the content needs a different register than the guide prescribes for a specific channel, note it rather than flattening it.

HOW TO USE:
Run this after the copy is written and before the QA checklist. The most valuable output is often section 1: a trait scoring 2 out of 5 tells you the voice guide needs an example, not that the copy needs fixing.
```

### 62 — Rework Notes for Internal Designers and Writers

```text
ROLE:
You are a creative director writing specific, actionable rework notes for a designer or writer — the notes that get changes made on the first pass.

INPUTS:
- The work to review: {{work}}
- What it must achieve: {{objective}}
- Brand voice guide: {{brand_voice_guide}}
- Brand assets and style rules: {{brand_assets}}
- The brief it was made against: {{brief}}
- What the client has already said about it: {{client_feedback}}

OUTPUT FORMAT — produce:

1. WHAT'S WORKING (3 bullets): specific things to protect in the rework. Rework that loses the good parts is worse than no rework.
2. REWORK NOTES TABLE — Columns: ID | Location or element | Current | Change required | Reason | Priority (Must / Should / Could) | Owner. 12–18 rows. Every note points to a location and describes the change, not the principle.
3. REFERENCE DIRECTION TABLE — Columns: Element | What we want | What we don't | Reference | 8 rows.
4. COPY CHANGES TABLE — Columns: Location | Current copy | New copy | Reason | Character limit impact. 8 rows. Write the replacement copy in full.
5. COMPOSITION CHANGES (table): Element | Change | Reason | Priority — 6 rows.
6. SPEC COMPLIANCE TABLE — Columns: Spec | Required | Actual | Fix. 8 rows covering dimensions, file formats, weight, colour mode, resolution, naming, and delivery format.
7. ACCESSIBILITY REMINDERS (table): Element | Requirement | Action — 5 rows.
8. CLIENT-FACING NOTE — 80 words: a short, warm, specific note you can send with the rework. Reference what they liked, name the changes plainly, and give a date. Written in {{brand_voice_guide}}.
9. DEADLINE & HANDOFF — table: Item | Owner | Due | Format | 6 rows.

RULES:
- "Make it pop", "more dynamic", and "doesn't feel on-brand" are not notes. Every note must state the change concretely.
- Write the replacement copy in full — writers who receive rewrites don't rewrite.
- If the client's feedback conflicts with the brief, flag it and ask for a decision rather than guessing.
- Priorities are honest: if everything is a Must, nothing is.
- Never include internal margin, cost, or client-budget commentary in the client-facing note.

HOW TO USE:
Use this instead of a voice-note review or a red-pinned PDF. The client-facing note at the end takes two minutes to send and prevents the "that wasn't what I meant" call, which costs far more than the review.
```

---


## Brand Voice & Tone

### 63 — Build a Brand Voice Guide From Existing Content

```text
ROLE:
You are a brand strategist reverse-engineering a voice guide from the writing a company already produces. You are documenting what the brand sounds like, not inventing a new voice.

INPUTS:
- Brand voice guide if one exists: {{existing_voice_guide}}
- Existing copy samples (at least 8, across channels): {{copy_samples}}
- Website copy: {{website_copy}}
- Social posts, ads, and email samples: {{channel_samples}}
- Audience: {{audience}}
- Brands or people whose voice the client admires: {{voice_references}}
- Words the client hates: {{hated_words}}
- Industry and sector: {{industry}}

OUTPUT FORMAT — produce:

1. VOICE IN ONE LINE (max 20 words): a single sentence describing how this brand sounds, with a named reference.
2. TRAITS TABLE — Columns: Trait | What it means at the sentence level | Sounds like | Doesn't sound like | Before → After example. 5–6 rows. Every trait must be evidenced by a sample from {{copy_samples}}.
3. PATTERN ANALYSIS — table: Pattern | Frequency in samples | Example | Rule to codify. 10 rows, covering sentence length, contractions, punctuation, question use, second person, jargon, superlatives, hedging, emoji, and numbers.
4. MECHANICS TABLE — Columns: Element | Observed rule | Guideline. 10 rows: reading level, average sentence length, longest sentence, paragraph length, capitalisation, contractions, exclamation marks, emoji policy, acronym handling, number formatting.
5. WE USE / WE DON'T USE — two-column table: We use | We don't use | Why | 20 rows.
6. CHANNEL REGISTER TABLE — Channels: Website, Email, Paid social, Organic social, Ads, Proposals, Internal. Columns: Channel | Register shift | What changes | What stays constant. One row per channel.
7. VOICE RISKS (4 bullets): where this voice is most likely to break, and the early warning sign for each.
8. OPEN QUESTIONS FOR THE CLIENT (5 items): where the samples are inconsistent and we need a decision.

RULES:
- Every trait must be traceable to at least two samples. If the brand isn't consistent there, it goes in section 8, not in the traits table.
- Do not import a vocabulary the brand doesn't use. If the samples never use "solutions", it doesn't go in the guide.
- If {{existing_voice_guide}} contradicts the samples, say so explicitly and show the contradiction — a guide nobody follows is a common cause.
- Write the one-line voice and the traits in the brand's own voice, not in the language of voice theory.
- Do not include any trait the client can't recognise when you read it back.

HOW TO USE:
This is how you build a voice guide for a client who doesn't have one — and most clients don't have one, they have a pile of inconsistent posts. Send section 8 first: getting those five decisions answered turns a document full of guesses into a guide the team will actually use.
```

### 64 — Rewrite Copy Into the Brand Voice

```text
ROLE:
You are a copy editor rewriting content so it matches {{brand_voice_guide}} exactly, without changing meaning, facts, or claims.

INPUTS:
- Content to rewrite: {{content}}
- Brand voice guide: {{brand_voice_guide}}
- Voice traits and definitions: {{voice_traits}}
- Banned words and phrases: {{banned_words}}
- Required proof style: {{proof_style}}
- Audience and reading level: {{audience}}, {{reading_level}}
- Words the client uses deliberately: {{protected_terms}}
- What the content must achieve (and the CTA): {{objective}}

OUTPUT FORMAT — produce:

1. REWRITE TABLE — Columns: ID | Location | Original | Rewritten | Rule applied | Words before | Words after. 15–25 rows. Every rewrite must be a distinct, applicable change.
2. VOICE TRAIT CHECK — table: Trait | Was present? | Now enforced? | How. One row per trait, minimum 5 rows.
3. BANNED PHRASE REMOVAL — table: Phrase found | Location | Replacement used | Note. Every occurrence.
4. PUNCTUATION AND EMOJI PASS — table: Location | Before | After | Rule. 8 rows.
5. READABILITY IMPROVEMENT — table: Location | Before | After | Readability change. 8 rows.
6. TONE SHIFTS BY SECTION — table: Section | Original tone | Rewritten tone | Reason for the change. 6 rows.
7. WHAT I DIDN'T CHANGE (5 bullets): the awkward, strange, or technically imprecise bits left alone, and why.
8. FINAL READ (200 words): the rewritten content in full, as it should be sent.

RULES:
- Never change a number, a name, a date, a link, or a claim. Voice only.
- Do not change quoted material — client quotes and testimonials stay exactly as given.
- Where the guide conflicts with clarity, clarity wins for factual text, and you note the conflict.
- If the original content was already on-voice, say so and make only the minimum changes needed.
- Don't use a banned word's near-synonym just to avoid the banned word. Replace the meaning, not the word.
- Every rewrite must preserve the objective and the CTA.

HOW TO USE:
This is the fix-it pass for any client deliverable in a new voice, or when a guide has changed. Review section 7 before sending — it tells the client which bits you deliberately left alone and pre-empts the "you changed my sentence" objection.
```

### 65 — Tone Adaptation Across Channels

```text
ROLE:
You are a social media writer adapting one core message into a consistent brand voice across six channels — recognisably the same brand, natively written for each platform.

INPUTS:
- Core message: {{core_message}}
- Channels: {{channels}}
- Brand voice guide: {{brand_voice_guide}}
- Core traits that must not change: {{core_traits}}
- What may flex by channel: {{flexible_elements}}
- Audience per channel: {{channel_audiences}}
- CTA per channel: {{channel_ctas}}
- Proof points: {{proof_points}}

OUTPUT FORMAT — produce:

1. TONE MAP TABLE — Columns: Channel | Core trait (unchanged) | Register shift | Length | Opening device | CTA style | What to cut. One row per channel in {{channels}}, minimum 6 rows.
2. THE SAME MESSAGE, SIX WAYS — for each channel: the full copy, final and ready to paste, with character count; plus a one-line note on what changed and why.
3. VOICE CONSISTENCY CHECK — table: Trait | Present in all channels? | Where it flexed | Acceptable? | Fix. One row per core trait.
4. PLATFORM ADAPTATION NOTES — table: Platform | Rule that shaped the adaptation | Constraint (character count, format, algorithm reality) | Applied. 8 rows.
5. CROSS-CHANNEL SEQUENCE — table: Order | Channel | Message angle | Why this order | CTA. For a campaign launch.
6. OFF-BRAND WARNING — table: Risk | Channel | What it looks like | How to catch it in review. 6 rows.

RULES:
- The core message and the core traits stay identical across channels. What changes is register, length, opening device, and CTA style.
- No channel copy may be copied from another with a hashtag swap.
- Respect real platform constraints: character limits, caption lengths, link placement, and the reality that a link in the post body suppresses reach on several platforms.
- Apply {{brand_voice_guide}} to every version, and flag any channel where the guide's formality is wrong for the platform.
- Include a proof point in every version.

HOW TO USE:
Use this for a campaign launch where the client wants a consistent voice across channels. The tone map is worth sending to the client first — it makes the adaptation decisions explicit, and clients rarely object to a change they've already seen.
```

### 66 — Banned Words, Cliches, and AI-Writing Cleanup

```text
ROLE:
You are a copy editor removing clichés, filler, banned vocabulary, and tell-tale AI writing patterns from client copy, so the words read as though a person wrote them.

INPUTS:
- Content: {{content}}
- Brand voice guide: {{brand_voice_guide}}
- Banned words and phrases: {{banned_words}}
- Clichés and overused industry phrases: {{cliches}}
- Words the client uses deliberately: {{protected_terms}}
- Industry and audience: {{industry}}, {{audience}}

OUTPUT FORMAT — produce:

1. PHRASE SWEEP TABLE — Columns: Phrase found | Occurrences | Location | Why it's weak | Replacement. 20 rows. Covers clichés, filler, vague claims, hedge stacks, and AI tells.
2. AI-WRITING PATTERN CHECK — table: Pattern | Found? | Where | Why it reads as machine-written | Fix. 10 rows: "it's not just X, it's Y", "in today's fast-paced world", "delve", "unlock", "elevate", tricolon everywhere, perfect parallelism, "when it comes to", rule-of-three overuse, and symmetrical sentence lengths.
3. HEDGE AND FILLER REMOVAL — table: Original | Cleaned | The meaning lost (if any). 12 rows.
4. VAGUE QUANTIFIER CHECK — table: Phrase | Problem | Specific version | Note. 10 rows.
5. REPETITION CHECK — table: Word or phrase | Occurrences | Intent | Fix. 8 rows.
6. BEFORE / AFTER READ (150 words): the same paragraph before and after, so the client can feel the difference.
7. FINAL CLEAN COPY: the full content, cleaned, in full.
8. RESIDUAL NOTES (4 bullets): anything left deliberately, with the reason.

RULES:
- Remove clichés, but keep phrases that are genuinely part of the industry's language and the audience's vocabulary.
- Never remove a protected term, even if it appears in the cliché list.
- Removing a word must never remove meaning. Section 3 exists to catch that.
- Do not add flourishes in place of clichés. Plain, specific sentences beat clever rewrites.
- If a banned phrase appears in a legal disclaimer, quoted text, or a client testimonial, leave it and note it.
- Match {{brand_voice_guide}} in the replacements.

HOW TO USE:
Run this on every externally-facing document before the QA checklist. Section 2 is the one worth doing every time — the "it's not just X, it's Y" construction is the single most reliable signal that copy came from a model, and clients spot it instantly.
```

### 67 — Voice Guide for a New Client From a Discovery Call

```text
ROLE:
You are a brand strategist drafting a voice guide for a client who has never had one, using their own words from the discovery call.

INPUTS:
- Client: {{client_name}}
- Discovery call transcript: {{transcript}}
- Client's own written materials (emails, website, decks): {{client_writing}}
- How they describe their own brand: {{self_description}}
- Words and phrases they used repeatedly: {{recurring_phrases}}
- Words they reacted negatively to: {{negative_reactions}}
- Industry and audience: {{industry}}, {{audience}}

OUTPUT FORMAT — produce:

1. VOICE IN ONE LINE (max 20 words), derived from how the client speaks.
2. TRAITS TABLE — Columns: Trait | Evidence from the transcript | Sounds like | Doesn't sound like | Example to write. 5 rows, each trait evidenced by an actual quote or observation from {{transcript}}.
3. THE CLIENT'S OWN PHRASES TABLE — Phrase | Where they used it | How to use it in copy | Note. 10 rows. This is the section clients recognise instantly.
4. MECHANICS TABLE — Columns: Element | Rule | Based on. 8 rows.
5. WE USE / WE DON'T USE — table: We use | We don't use | Why. 15 rows, built from {{negative_reactions}} and {{recurring_phrases}}.
6. CHANNEL REGISTER TABLE — Channels: Website, Email, Social, Ads, Proposals. Columns: Channel | Register | What changes. 5 rows.
7. 10-WORD SAMPLE TEST (table): Sample sentence | Written in the new voice | Verdict. 5 rows, so the client can judge the guide by reading it.
8. THE ASK TO THE CLIENT (5 bullets): decisions needed to finalise the guide.

RULES:
- Base the guide on how the client talks, not on what they say the brand is. Their spoken language is the most reliable evidence.
- Include actual phrases they used. This is what makes the guide feel like theirs rather than generic.
- If {{client_writing}} contradicts the transcript, note it and ask which is authoritative.
- Do not introduce vocabulary the client never uses.
- The sample test must be readable aloud without it sounding stilted.

HOW TO USE:
Send the client's own phrases table first — it's the section that gets a "yes, that's us" reaction and unlocks approval of the rest. Then send the whole guide with the five asks in section 8 answered.
```

### 68 — Brand Voice Quick Reference Card

```text
ROLE:
You are a brand designer producing a one-page quick reference that a designer, writer, or social media manager can use while working — the fast version of the voice guide.

INPUTS:
- Full brand voice guide: {{voice_guide}}
- Brand assets and colours: {{brand_assets}}
- Approved claims: {{approved_claims}}
- Banned words: {{banned_words}}
- Common use cases: {{use_cases}}
- Brand voice guide as the source of truth: {{brand_voice_guide}}

OUTPUT FORMAT — produce:

1. VOICE CARD (single page):
   - VOICE IN ONE LINE (one sentence)
   - 5 TRAITS (one word each + one line of definition)
   - 5 "ALWAYS" RULES (bullet list, imperative)
   - 5 "NEVER" RULES (bullet list, imperative)
   - 10 APPROVED PHRASES (ready to drop into copy)
   - 10 BANNED PHRASES (each with a one-word replacement)
   - DO / DON'T table: Element | Do | Don't — 8 rows covering hooks, headlines, CTAs, openings, social posts, email subject lines, and long-form intros
   - SPECIMEN: 3 short paragraphs written in the voice (website, email, social)
2. QUICK USE TABLE — Columns: Use case | Voice in one line | Do | Don't | Example. 8 rows.
3. TYPE SETTER'S NOTE — table: Element | Guidance. 5 rows for designers.
4. THE ONE-PAGE FORMAT SPEC — table: Element | Specification. 8 rows: dimensions, layout, type sizes, colours, spacing, print and screen versions, and where to store it.
5. WHERE THIS LIVES (2 bullets): file location and the rule for updating it when the full guide changes.

RULES:
- Everything on the card must be usable without opening the full guide. If a rule needs the full guide to understand, it doesn't belong on the card.
- The approved phrases must be complete, ready-to-use sentences or fragments, not category labels.
- The specimen paragraphs must be published-quality, not placeholders.
- Keep the card to one page. If it runs long, the reference content has bloated.
- The card must agree with the full guide on every point. If they differ, the full guide wins and the card is wrong.

HOW TO USE:
Put this in the client's Notion workspace as the first page, and pin it in the creative team's channel. Most voice violations happen because nobody opened the 12-page guide — this is the version people actually read.
```

---


## Prompt to artifact: a full worked example

This section runs one real deliverable end to end so you can see exactly how the prompts chain together and what the finished artefact looks like. Nothing here is theoretical: the same flow works for a client report, a proposal, a campaign launch, or a website launch.

**The client:** Fieldnote Coffee Co. — a direct-to-consumer coffee subscription, 8,200 active subscribers, 14 SKUs, competing against a dozen subscription coffee brands. They spend on Meta, Google Search, TikTok, and email. Their agency retainer covers paid social management, email, creative, and monthly reporting.

**The moment:** it's 2 June. The May report is due Friday 6 June. The client has sent their GA4 and ad account exports and asked whether the increase in Meta spend was worth it.

### The prompt chain

| Step | Prompt | What it produces | How long it takes |
|---|---|---|---|
| 1 | **44 — Analytics Data QA and Validation** | The clean dataset, with every discrepancy logged before anyone writes a conclusion | 15 min |
| 2 | **40 — Campaign Performance Deep-Dive** | The diagnosis: what actually happened in Meta, and why | 20 min |
| 3 | **38 — Monthly Performance Report** | The finished client report, all ten sections | 30 min |
| 4 | **61 — Brand Voice Enforcement Pass** | The report's narrative brought into the client's voice | 15 min |
| 5 | **57 — Pre-Send Client Deliverable QA** | The sign-off, the issues found, the fixes applied | 15 min |

Total: roughly 95 minutes of senior attention, versus the four to six hours it usually takes to pull the numbers, find the story, and write it up.

---

### Step 1 — Prompt 44: validating the data first

Before writing anything, the data gets checked. This step is the one most agencies skip, and it is the one that stops a wrong number reaching a client.

**What came in**

| Source | Rows | Period | Notes |
|---|---|---|---|
| Meta Ads Manager | 38 campaigns | 1–31 May | Exported with spend, impressions, clicks, purchases |
| Google Ads | 12 campaigns | 1–31 May | Last-click revenue only, no data for 12–13 May (billing outage) |
| GA4 | 1–28 May | 1–31 May | 3 days missing at export |
| Shopify | 4,182 orders | 1–31 May | Source of truth for revenue and refunds |
| Klaviyo | 3 email sends | May | Open and click rates, attributed revenue |
| Client spreadsheet | Manual | May | A "best performing post" sheet the client maintains by hand |

**What the validation found**

| ID | Dataset | Issue | Severity | Resolution |
|---|---|---|---|---|
| 1 | Google Ads | No data for 12–13 May (billing outage) | Critical | Compare against 12–13 April, and state the gap in the report |
| 2 | GA4 vs Shopify | 3 days missing from GA4 | Major | Use Shopify for revenue; GA4 for sessions on available days only |
| 3 | Meta revenue | Meta attributed £41,200; Shopify recorded £29,600 | Major | Use Shopify revenue throughout; explain the difference once |
| 4 | Client spreadsheet | "Best post" list contains 2 posts that ran in April, not May | Minor | Excluded; noted in the report's production log |
| 5 | GA4 sessions | Duplicate session rows on 3 days | Minor | Deduplicated; 3.1% of monthly sessions affected |

**Output — the corrected scorecard**

| KPI | Target | Actual | vs target | vs April | Trend | Status |
|---|---|---|---|---|---|---|
| New subscribers | 900 | 1,046 | +16% | +11% | ▲ | On track |
| Blended CAC | £28 | £26.40 | −6% | −9% | ▲ | On track |
| Revenue | £420,000 | £447,300 | +6% | +14% | ▲ | On track |
| Meta contribution margin | £180,000 | £152,600 | −15% | −18% | ▼ | At risk |
| Email revenue share | 22% | 19.4% | −3% | −4% | ▼ | At risk |
| Repeat purchase rate | 31% | 34.8% | +12% | +3% | ▲ | On track |

The headline: growth is genuinely good, and Meta is where the problem lives. That conclusion was visible only after validation — the raw Meta export showed Meta revenue up 24%, which would have produced a completely wrong report.

---

### Step 2 — Prompt 40: the deep dive that finds the story

**The funnel**

| Funnel stage | Volume | Rate from previous | Benchmark | Gap | Diagnosis |
|---|---|---|---|---|---|
| Impressions | 2,914,000 | — | — | — | — |
| Clicks | 61,340 | 2.10% | 2.30% | −0.2pp | Creative fatigue — CTR fell from 2.6% in April |
| Landing page views | 57,900 | 94.4% | 95% | −0.6pp | Within tolerance |
| Add to cart | 3,180 | 5.49% | 6.5% | −1.0pp | Mobile checkout friction on the subscription page |
| Purchases | 1,046 | 32.9% | 30% | +2.9pp | Strong — offer and pricing are working |

**Creative performance**

| Asset ID | Hook | Format | Spend | CTR | CVR | CPA | Frequency | Status |
|---|---|---|---|---|---|---|---|---|
| A04 | "Your coffee, but better" | Static | £4,120 | 1.8% | 2.1% | £39.40 | 4.8 | Kill |
| A07 | "We tasted 41 roasts so you don't have to" | Video | £9,860 | 3.4% | 4.9% | £18.20 | 2.1 | Scale |
| A11 | "£8.50 a cup. Half the price of the café." | Static | £7,240 | 2.9% | 3.8% | £21.10 | 5.2 | Iterate |
| A12 | "The subscription that paused when you went on holiday" | Carousel | £6,980 | 3.1% | 4.2% | £19.60 | 3.0 | Scale |
| A15 | "Coffee people in your area drink" | UGC | £8,110 | 2.2% | 2.6% | £31.70 | 6.1 | Kill |
| A18 | "One bag, 14 origins, one subscription" | Video | £10,240 | 3.6% | 5.2% | £17.90 | 1.8 | Scale |

The story: two of the three worst performers are the highest-frequency ads. Frequency on A15 hit 6.1, meaning the same 22,000 people saw it repeatedly until they stopped clicking. Meanwhile the three best performers are all low-frequency and all share one property — they show the *product doing something*, not the product being admired.

**What worked and why**

The three scaling assets all begin with a specific number — 41 roasts, 14 origins, £8.50 — and all show the physical product in the first two seconds. Specificity plus demonstration beat lifestyle imagery, and the frequency data shows the audience was still fresh when it ran. A04 and A15 led with a mood ("Your coffee, but better") and a generalisation ("Coffee people in your area drink"), neither of which earned the second second of attention.

**What didn't work and why**

A15 was the client's favourite creative going into May — it tested well in a small test at £500. At £8,110 it went to 6.1 frequency and the CTR collapsed. The test was sound; the scaling decision ignored frequency. That distinction matters, because the client needs to hear that the concept was fine and the pacing was wrong.

**Recommendations that came out of the deep dive**

| # | Recommendation | Expected effect | Effort | Risk | Owner |
|---|---|---|---|---|---|
| 1 | Pause A04 and A15, redirect to A07/A12/A18 | +£6,200 contribution margin | 1 hour | Loss of reach if a hidden winner | Paid lead |
| 2 | Cap frequency at 4.0 across Meta prospecting | Lower waste, higher CTR | 2 hours | Slight reach reduction | Paid lead |
| 3 | Move A11 to a new audience and drop the price from the hook | +0.4pp CTR | 30 min | Price-led hook may underperform | Creative |
| 4 | Fix mobile checkout friction (3 identified fixes) | +0.6pp conversion | 1 sprint | Dev capacity | Client dev |
| 5 | Increase email revenue share with a win-back flow | +2.5pp share | 1 week | Subscriber fatigue | CRM lead |
| 6 | Produce three product-demonstration videos for June | 3 scaling-ready assets | 5 days | Production cost | Creative |

---

### Step 3 — Prompt 38: the finished client report

The report that follows is the actual artefact — the ten sections, in order, as the client receives it. Section 2 is shown in full because it is the section that gets forwarded to the client's board.

---

**FIELDNOTE COFFEE CO. — MAY 2026 PERFORMANCE REPORT**

Prepared by {{your_agency}} · Issued 6 June 2026 · Data sources: Shopify, Meta Ads Manager, Google Ads, GA4, Klaviyo · Reporting cadence: monthly, by the 5th working day

---

#### 1. Executive summary

May was our strongest month on record for subscriber growth. We added 1,046 new subscribers against a target of 900, which is 16% above target and 11% ahead of April, while acquisition cost fell from £28 to £26.40. Total revenue was £447,300, 6% above target.

The problem this month was Meta. We spent £19,840 more than April, but the extra spend produced £9,100 less contribution margin, because two of our six campaigns were running to the same people too many times. This was a pacing problem, not a creative or strategy problem, and it is reversible — we have already paused the two campaigns and redirected that budget into the three that were working. If the same pattern does not repeat in June, Meta returns to being our most profitable channel.

On the other side of the account, email is under-performing its share of revenue at 19.4% against a 22% target, even though repeat purchase rate rose to 34.8%. We have a win-back flow to launch in June, which is the cheapest revenue available to us.

#### 2. KPI scorecard

| KPI | Target | Actual | vs target | vs April | Trend | Status |
|---|---|---|---|---|---|---|
| New subscribers | 900 | 1,046 | +16% | +11% | ▲ | On track |
| Blended CAC | £28 | £26.40 | −6% | −9% | ▲ | On track |
| Revenue | £420,000 | £447,300 | +6% | +14% | ▲ | On track |
| Meta contribution margin | £180,000 | £152,600 | −15% | −18% | ▼ | At risk |
| Email revenue share | 22% | 19.4% | −3% | −4% | ▼ | At risk |
| Repeat purchase rate | 31% | 34.8% | +12% | +3% | ▲ | On track |
| Landing page conversion rate | 6.0% | 5.4% | −0.6pp | −0.3pp | ▼ | At risk |

#### 3. Channel performance

| Channel | Spend | Impressions | Reach | Clicks | CTR | Conversions | CPA | ROAS | Rating |
|---|---|---|---|---|---|---|---|---|---|
| Meta | £27,600 | 2,914,000 | 1,142,000 | 61,340 | 2.10% | 697 | £39.60 | 2.4× | C |
| Google Search | £14,200 | 186,000 | 141,000 | 24,800 | 13.33% | 268 | £52.99 | 4.1× | A |
| TikTok | £3,100 | 214,000 | 168,000 | 7,900 | 3.69% | 41 | £75.61 | 1.6× | D |
| Email | £0 | 412,000 delivered | 68% open | 9,340 | 2.27% | 203 | £0 | 12.8× | A |
| Organic / SEO | £0 | 84,000 | — | — | — | 34 | £0 | 5.6× | B |
| **Total** | **£44,900** | | | | | **1,243** | **£36.12** | **3.9×** | |

#### 4. Top performing assets

| Asset | Channel | Spend | Conversions | CPA | Why it worked |
|---|---|---|---|---|---|
| A18 "One bag, 14 origins, one subscription" | Meta | £10,240 | 572 | £17.90 | Opens with a specific number and shows all 14 origins in the first two seconds — no setup, no scrolling past a logo |
| A07 "We tasted 41 roasts so you don't have to" | Meta | £9,860 | 542 | £18.20 | Turns a quality claim into a concrete, verifiable act, then shows the tasting bench |
| A12 "The subscription that paused when you went on holiday" | Meta | £6,980 | 356 | £19.60 | Names an objection nobody else in the category mentions, and answers it visually in three frames |

All three are low-frequency (1.8–3.0) and all three show the product doing something rather than being styled. That is the pattern to repeat in June.

#### 5. Underperformers and losses

| Asset or campaign | Spend | Result | Likely cause | Decision | Owner |
|---|---|---|---|---|---|
| A15 "Coffee people in your area drink" | £8,110 | 256 conversions, CPA £31.70, CTR collapsed to 2.2% | Frequency reached 6.1 — the same audience saw it repeatedly. The creative tested well at £500; it was not ready for £8,000 of spend | **Kill** (concept returns in July with a new audience) | Paid lead |
| A04 "Your coffee, but better" | £4,120 | 105 conversions, CPA £39.40 | Mood-led hook with no specific claim; 1.8% CTR against a 2.3% benchmark | **Kill** | Paid lead |
| TikTok account | £3,100 | 41 conversions, CPA £75.61 | 9 posts, no native-format video, no creator content, no hook pattern | **Pause** and rebuild from zero in July rather than continue | Paid lead |

Total spend released: £15,330. Two of the three losses trace to the same decision — scaling before checking frequency.

#### 6. Creative production log

| Date | Asset | Channel | Status | Performance |
|---|---|---|---|---|
| 2 May | A19 "The 30-second ritual" | Meta | Live | 141 conversions, £24.10 CPA |
| 6 May | A20 "Beans, not blends" | Meta | Live | 88 conversions, £31.40 CPA |
| 9 May | A21 "Pause anytime" carousel | Instagram | Live | 4,100 saves, 1.2% engagement rate |
| 13 May | A22 "Grind size matters" | Meta | Live | 96 conversions, £29.80 CPA |
| 18 May | A23 "Your first delivery" | Email | Sent | 41.2% open, 3.1% click |
| 22 May | A24 "Roast day" | TikTok | Live | 9,800 views, 0.4% engagement |
| 28 May | A25 "Subscribe and save 10%" | Meta | Live | 73 conversions, £26.60 CPA |

#### 7. Insights

1. **Specificity beat lifestyle on every platform.** All three scaling assets lead with a number (41, 14, £8.50) and show the product in motion. The two killed assets led with a mood and a generalisation, and both fell below the CTR benchmark.
2. **Frequency, not fatigue-by-audience, was the binding constraint.** A15's CTR fell 46% from week one to week four while its frequency rose from 2.4 to 6.1. No creative was on for more than three weeks in May.
3. **The May billing outage cost us roughly two days of Google comparison.** Revenue for 12–13 May is excluded from the Google Ads comparison and the gap is stated wherever those figures appear.
4. **Repeat purchase rate rose 3 points while email's revenue share fell 4 points.** Our existing subscribers are buying more, but we are not re-engaging the ones who lapse. The two numbers point at the same gap.
5. **Meta's reported revenue (£41,200) exceeded Shopify's recorded revenue (£29,600) by 39%.** This is Meta's standard attribution over-counting on view-through. All figures in this report use Shopify revenue.

#### 8. Next month's plan

| Action | Channel | Owner | Start date | Target metric |
|---|---|---|---|---|
| Launch win-back flow for 90-day lapsed subscribers | Email | CRM lead | 8 Jun | Email revenue share ≥ 21% |
| Shift £12,000 from A04/A15 to A07/A12/A18 | Meta | Paid lead | 3 Jun | Meta CPA ≤ £28 |
| Set frequency cap at 4.0 on all prospecting | Meta | Paid lead | 3 Jun | Meta CTR ≥ 2.4% |
| Produce three demonstration-led videos | Creative | Creative lead | 8 Jun | 3 assets live by 19 Jun |
| Ship three mobile checkout fixes | Client site | Client dev | 10 Jun | LP conversion ≥ 6.0% |
| Rebuild TikTok from a standing start | TikTok | Social lead | 22 Jun | 10 native videos, CPA benchmark set |
| Test a price-led hook on A11 with a fresh audience | Meta | Paid lead | 15 Jun | CTR +0.4pp on A11 |

#### 9. Action required from Fieldnote

| # | Action | Why it matters | Owner | Needed by | Impact if delayed |
|---|---|---|---|---|---|
| 1 | Approve the mobile checkout fixes for the sprint | Conversion rate is 0.6pp below target and the friction is on mobile, where 71% of traffic sits | Priya, CTO | 9 Jun | June revenue target at risk by ~£18,000 |
| 2 | Confirm the win-back offer (15% off first box) | The flow cannot be built without the approved discount and margin ceiling | Tom, MD | 5 Jun | Email revenue share stays at 19% |
| 3 | Confirm pause of TikTok through 30 June | £3,100 of current spend returns to Meta; the channel restarts in July from zero | Tom, MD | 2 Jun | £3,100 continues to spend at £75.61 CPA |
| 4 | Share the new roast photography set | Three June videos depend on it; without it, the June creative pipeline slips a week | Sam, Brand | 6 Jun | 3 assets delayed, £4,000 of creative budget reallocated |

---

### Step 4 — Prompt 61: bringing the report into the brand voice

The draft above is accurate but reads like an internal document. Fieldnote's voice guide says: *plainly expert, calmly direct, never hyped, short sentences, no jargon, no exclamation marks, numbers before adjectives.* Applying the enforcement pass changes the executive summary and the narrative sections.

| ID | Location | Draft | After voice pass | Rule applied |
|---|---|---|---|---|
| 1 | Exec summary, sentence 1 | "May was our strongest month on record for subscriber growth." | "May was our best month yet for subscriber growth." | Shorter sentence, no superlative stacking |
| 2 | Exec summary | "which is 16% above target and 11% ahead of April" | "That is 16% above target and 11% ahead of April." | Contraction matches the guide |
| 3 | Exec summary | "The problem this month was Meta." | "Meta is where this month went wrong." | Calmer, plainer construction |
| 4 | Exec summary | "because two of our six campaigns were running to the same people too many times" | "Two of our six campaigns kept reaching the same people too often." | Removes jargon ("frequency" appears later, explained) |
| 5 | Insight 2 | "A15's CTR fell 46% from week one to week four while its frequency rose from 2.4 to 6.1." | "A15's CTR fell 46% across May. Its frequency went from 2.4 to 6.1." | One idea per sentence |
| 6 | Insight 5 | "This is Meta's standard attribution over-counting on view-through." | "Meta counts some sales it did not directly cause. That is how Meta reports." | Plain English, no jargon |
| 7 | Action 1 | "Conversion rate is 0.6pp below target and the friction is on mobile, where 71% of traffic sits" | "We convert 0.6pp below target. The friction is on mobile, and 71% of traffic is mobile." | Short sentences |
| 8 | Top assets | "Turns a quality claim into a concrete, verifiable act" | "It turns a quality claim into something you can check." | No abstract nouns |

The voice pass changed roughly 60 words across a 2,400-word report. That is the point of running it as a separate step: the structure and the numbers are already right, so the voice pass is a light, fast edit rather than a rewrite.

---

### Step 5 — Prompt 57: the QA that catches the last three problems

| ID | Severity | Category | Location | Issue | Fix applied |
|---|---|---|---|---|---|
| 1 | Critical | Fact check | Section 3, Email row CTR | The email CTR was calculated against delivered emails rather than opened emails — the number was inflated | Recalculated against delivered; changed from 2.27% to 1.83% |
| 2 | Critical | Placeholder | Section 1 header | `{{your_agency}}` had been left in the document | Replaced with the agency name and version stamp added |
| 3 | Major | Consistency | Section 4 vs Section 5 | A19 appears in the production log with 141 conversions but is missing from the top-performing assets table | Added as fourth top performer and the table re-sorted |
| 4 | Major | Fact check | Section 3, Total row | Total conversions (1,243) includes email and organic, but the section title implies paid only | Row label changed to "Total (all channels)" and a note added |
| 5 | Minor | Formatting | Section 2 | Trend arrows pointed up on CAC because a fall is good | Reversed to ▼ and added a note that down is good for CAC |
| 6 | Minor | Voice | Section 8 | "rebuilt from a standing start" — reads as a phrase, not a statement | Rewritten to "rebuild TikTok from zero" |
| 7 | Minor | Date check | Section 6 | A21 posted 9 May but the log listed it as Instagram only; it also ran as a Meta ad | Both placements listed |

Final verdict: **PASS WITH MINOR EDITS** after fixes. The report went out on 6 June at 09:14, with the executive summary pasted into the email body so the client's MD could read it without opening the document.

### What the client replied

> "This is the first report I've received where I know what to do on Monday. The frequency thing on A15 is fair — I'd have scaled it if I hadn't seen the numbers next to each other. Approved on all four actions except TikTok: I'd rather we keep it live at £1,500 until the end of June so we have something to look at when we restart."

That reply is the point of the whole pack. The report didn't just describe May — it made the client's next four decisions for them, in their voice, with every number traceable, and it flagged the one thing that was genuinely their call.

---

## Client-ready checklist

Run this before anything leaves your outbox. Every item has a pass condition — if you can't confirm it, don't send.

### The 20-point pre-send check

| # | Check | Pass condition |
|---|---|---|
| 1 | All placeholders resolved | No `{{...}}`, no `[NEEDS INPUT]`, no "TBC", no lorem ipsum anywhere in the document |
| 2 | Numbers traceable | Every figure traces to a source in the data, with its date; no number was estimated without saying so |
| 3 | Period stated | The reporting period appears in the header with exact start and end dates |
| 4 | Comparison present | Every metric has a target, a prior period, or both |
| 5 | Claims verified | Every claim about results, product, or market appears in the approved claims list, or is flagged for sign-off |
| 6 | Brand voice applied | The document reads in the client's voice — check the banned words list, not just the general tone |
| 7 | No banned words | Zero occurrences of the client's banned vocabulary and clichés, including inside compounds |
| 8 | Reading level appropriate | Reads at the level of the most senior person who will read it; jargon is either explained or removed |
| 9 | Structure matches the template | Every section the brief promised is present, in the agreed order, with the agreed row counts |
| 10 | Row counts exact | Calendars have the exact number of rows; tables have no missing or extra rows; matrix cells are all filled |
| 11 | No empty cells | Every table cell has content, or an explicit em dash with a stated reason |
| 12 | Links tested | Every link opens, points where the text says it does, and carries the correct UTM parameters |
| 13 | Assets attached | Every referenced image, file, or deck is actually attached and opens correctly |
| 14 | Alt text present | Every image has alt text describing its purpose in context |
| 15 | Accessibility checked | Captions on video, contrast checked, heading hierarchy correct, link text meaningful |
| 16 | Platform rules met | Character limits, hashtag rules, aspect ratios, and disclosure requirements satisfied |
| 17 | Names and spelling correct | Client name, product names, contact names, and brand capitalisation checked against the account record |
| 18 | Dates consistent | No contradictory dates between the cover, the body, and the log; year included where the month alone is ambiguous |
| 19 | Internal content removed | No internal notes, margin figures, internal links, competitor names, or commentary about the client |
| 20 | The ask is clear | The document ends with what happens next: who decides what, and by when |

### Per-artefact additions

| Artefact | Also check |
|---|---|
| Content calendar | Every hook is a finished sentence; no two rows share a hook; the final row is a CTA; asset owners are named |
| Audit report | Every finding has an owner and an effort estimate; severity definitions are stated; evidence is quoted, not paraphrased |
| Ad copy matrix | Character counts are shown and within limits; every ad matches the landing page promise; a decision threshold is set for every test |
| Monthly report | Executive summary reads well when forwarded on its own; underperformers have a decision; action table has deadlines and owners |
| QBR deck | Every slide title is a sentence with a number in it; failures and money lost are included; decisions have recommendations |
| Proposal | Their problem is described before our capability; the timeline respects their real constraints; commercials have a clear next step |
| Scope of work | Every deliverable has a quantity and a frequency; exclusions are explicit; change control is defined |
| Website copy | Metadata is within limits; the H1 states an outcome; the copy doesn't rely on the visual to carry meaning |
| Email newsletter | Subject line is specific; link text is descriptive; plain-text version included; unsubscribe present; mobile preview checked |
| Brand voice guide | Every trait has a before/after example; the "we don't use" column gives a reason; mechanics have numeric targets |

### The three-question sanity check

Before you press send, ask yourself:

1. **If the client's most sceptical colleague read only the summary and the recommendation, would they have everything they need to agree?** If not, the summary is missing the reasoning that matters.
2. **Is there anything in this document I would not want quoted in a future case study?** Anything about margin, internal capacity, a difficult client relationship, or a competitor's problem. Remove or rewrite it.
3. **Does this document make my next job easier?** Every artefact should leave the client clearer than they were before, and should make the next request, approval, or deadline obvious.

---


## FAQ

**Will these prompts work if I don't have a brand voice guide yet?**
Yes. About half the prompts accept `{{brand_voice_guide}}` and will work without one — they simply won't enforce a voice. If the client has no guide, run Prompt 63 (Build a Brand Voice Guide From Existing Content) or Prompt 67 (Voice Guide From a Discovery Call) first; both produce a guide from material you already have. Clients who have never had a voice guide are the most common case, and it's also where the pack adds the most value, because the guide becomes a deliverable you bill for.

**Do I need a paid AI tool to use this?**
No. Every prompt works in any modern chat assistant. The prompts are written for paste-and-run use and don't depend on tool access, file uploads, or integrations. If your tool truncates long tables, ask for the output section by section — "Give me rows 1–15 only" — and stitch them into the client template.

**How do I keep the AI from inventing statistics or client quotes?**
Every prompt includes a placeholder-based rule: anything not supplied comes back as `[NEEDS INPUT: ...]` rather than a plausible guess. The QA prompts (57, 59, 61) then check for leftover placeholders and unverified claims before anything is sent. The discipline is simple — never paste a statistic into a prompt without also pasting its source, and never accept a specific number that came back from the model without checking it against the raw export.

**What if my client changes their requirements mid-project?**
That's a scope conversation, not a prompt problem. Prompt 46 (Scope of Work) defines what each deliverable includes, in what quantity, at what frequency, and what's excluded — which is what makes the conversation about the change rather than about who made a mistake. Run Prompt 50 (Renewal and Scope Expansion) when the change is large enough to warrant a different tier.

**Is this going to make my output sound like AI?**
It won't, if you run the QA prompts. The structure of this pack pushes away from the two things that read as machine-written: generic abstraction and clichéd phrasing. Prompt 66 removes the specific tells — "it's not just X, it's Y", "in today's fast-paced world", tricolon everywhere — and Prompt 61 enforces the client's actual voice. What you send should read like a competent person wrote it, because the rules that produce that are built into every prompt.

**Can I use these for my own agency's marketing?**
Yes. Everything here is written to be adapted to any client, including yours. The prompts reference `{{your_agency}}` in a few places (report footers, proposal covers, sign-offs) — swap it for your name. If you build a report on your own agency's performance, the monthly report prompt and the QBR outline will do the same work they do for a client.

**How long does a full deliverable actually take?**
The worked example in this pack — a monthly client report including data validation, deep-dive analysis, the full report, a voice pass, and QA — took about 95 minutes of senior attention against the four to six hours it usually takes. Reports, audits, and content calendars are the fastest wins. Strategy and creative work take longer because the thinking is the work; the prompts save you the formatting and the blank-page time, not the judgement.

**What format do I get, and how do I use it in Notion?**
The pack ships as a PDF plus a Notion workspace. The PDF is the readable reference — the templates and prompts, laid out for printing and searching. The Notion workspace has each prompt in its own database row with the copy button, the artefact templates as ready-to-duplicate pages, and a `Deliverables` tracker for running client work. The intended workflow is to duplicate the artefact template page into the client's folder, run the matching prompt, paste the output into the template's structure, and run the checklist before sending.

---

## Free lifetime updates — every future version is yours

This pack will keep growing. New prompts will be added as agencies find what works on real client work: more channel-specific reporting structures, additional audit formats, agency-specific operational templates, and prompts that get sharper as we watch which structures produce artefacts clients actually approve. The artefact template library will expand alongside them.

**Every future version is included at no additional cost.** Buy this pack once and you receive every update that follows — there is no upgrade fee, no subscription, no tier to move up to, and no expiry on your access.

The updates land in the same place your original download lives. You'll get an email when a new version is published, with a short summary of what was added and what changed. Existing prompts don't get silently rewritten — if a prompt is improved, the version history is included so you can see exactly what moved and why. And nothing you already have gets taken away: your copy of every template and prompt stays yours.

**What you get on every update**

| Update type | What it contains |
|---|---|
| New prompts | Added to the relevant category, numbered continuously, with the same structure and a "How to use" line |
| New artefact templates | Added to the template library with the exact sections, columns, row counts, and cell-by-cell guidance |
| Improved prompts | Revised with a changelog showing what changed and why |
| New worked examples | Full prompt chains for real deliverable types, as the one in this pack shows |
| Notion workspace updates | New database views, synced with the PDF additions |

**Two things that will not change:** the price you paid, and the promise that every update is free. If a major version arrives that changes how the pack works, you still get it — and the changelog tells you exactly what moved so nothing in your existing workflow breaks without you knowing.

Thank you for buying. Now go deliver something your client would actually pay for.

---

*Agency Client Delivery AI Prompt Pack — 68 prompts across 10 categories, 20 finished artefact templates, and a full worked example. Format: PDF + Notion. Free lifetime updates.*
