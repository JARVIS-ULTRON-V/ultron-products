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
| Copy source | Which prompt/artifact produced this copy (e.g. Prompt 44 → landing page headline set) |

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
This output feeds landing page copy (Prompt 44), ad copy (Prompt 23), the strategy one-pager (Template 7), and proposal covers. Run it once, store it, and treat it as the source of truth — every later piece of client-facing copy should trace back to the hierarchy in this document.
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
Generate, then run Prompt 57 (Editorial QA Pass) over the draft before it goes to the client. Treat the "Editor's notes" section as your list of client questions — it converts a vague "can you review this?" into a specific list of three things to check.
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
Pair this with Prompt 55 (Image Prompt Set for Product Photography) and you can ship a product page from a single spreadsheet of specs. Run Prompt 58 (Legal & Claims Check) before publishing anything with a performance or health claim.
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

ADD = """

---

## SEO

### SEO keyword map builder
```
You are an SEO strategist for a service business. For the client {{client_name}} in {{industry}}, build a 3-tier keyword map in a markdown table:
| Search intent | Target keyword | Monthly search estimate | Difficulty (low/med/high) | Suggested page |

Tier 1: head terms (high volume, generic). Tier 2: mid-tail commercial terms. Tier 3: long-tail, high-intent terms.
Include 4 rows per tier (12 total). For each row, add one line on why that page should target it.
```
**How to use:** Feed the client's service list and locale. **What good looks like:** 12 realistic, intent-sorted keywords with a page assigned to each.

### Technical SEO audit summary
```
List the top {{n}} technical SEO issues for {{client_name}}'s site likely to affect Core Web Vitals and crawlability:
1. Site speed (LCP/INP/CLS) - what to fix
2. Mobile rendering issues
3. Broken links / 404s
4. Duplicate content / canonical issues
5. Internal linking gaps
6. Structured data opportunities
For each: symptom, likely cause, fix, and priority (P0/P1/P2). Output as a table, then a 5-line executive summary.
```
**How to use:** Pair with a crawl tool (or the client's data). **What good looks like:** Prioritized, actionable fixes, not a vague "speed it up."

## Reporting & Analytics

### Monthly performance report
```
Build a client-ready monthly report for {{client_name}} covering {{period}}. Use exactly these sections:
1. Executive summary (3 sentences: headline result, what worked, what to do next)
2. KPI table: metric | goal | actual | % of goal | trend vs last month
3. Channel breakdown table: channel | spend | results | ROAS/CPL | notes
4. Wins (3 bullets) and risks (3 bullets)
5. Next month's plan (3 bullets with owners and dates)

Write in a confident, consultative tone. End with a recommendation in one line.
```
**How to use:** Give it the real numbers; never let the AI invent metrics. **What good looks like:** A report you'd send to the client with only light edits.

### Client QBR (quarterly business review) deck outline
```
Create a 12-slide deck outline for {{client_name}}'s quarterly review covering {{quarter}}:
Slide 1: Title + period, Slide 2: Snapshot (revenue, leads, spend, ROAS), Slide 3: vs last quarter table,
Slide 4: What worked, Slide 5: What didn't, Slide 6: Channel deep-dive, Slide 7: Top 3 wins,
Slide 8: Risks & issues, Slide 9: Next-quarter plan, Slide 10: Budget proposal, Slide 11: Strategic recommendation,
Slide 12: Q&A / discussion points.
For each slide give the headline, 3 bullet points, and any visual/chart suggestion.
```
**How to use:** Use as the skeleton for the actual deck. **What good looks like:** A complete, structured QBR the account lead can build from.

## Proposals, Pricing & Scope

### Scoped proposal draft
```
Draft a proposal for {{client_name}} for the project {{project}} at a target price of {{price}}.
Sections: Executive summary, Problem we solve, Our approach (3 phases), Deliverables list, Timeline table,
Investment & what's included, What's NOT included, Next steps.
Keep it one page if possible. Use a confident but consultative tone. True 3 pricing options (economy / recommended / premium) as a table.
```
**How to use:** Fill in real scope and price. **What good looks like:** A proposal the client can say yes to without a rewrite.

### Statement of work (SOW) builder
```
Turn the project {{project}} for {{client_name}} into a precise SOW:
1. Project overview, 2. Scope of work (numbered deliverables), 3. Out of scope,
4. Timeline with milestones and dates, 5. Payment schedule, 6. Revisions allowed,
7. Who does what (contact table), 8. Approval process.
Use exact, non-ambiguous language. Flag anything that needs client confirmation.
```
**How to use:** The deliverable is the contract annex. **What good looks like:** A SOW with no vague "etc." clauses.

## Client Communication & Account Management

### Client status update email
```
Write a weekly status email to {{client_name}} for {{project}}. Structure:
Subject: [Project] Weekly update - week of {{date}}
1. One-line summary of progress
2. What we completed this week (3 bullets)
3. What's happening next (2-3 bullets)
4. Any decisions needed from you (clear, numbered asks)
5. A note on timeline/schedule health
Keep it under 200 words. No jargon. No fluff.
```
**How to use:** Send as-is with your real progress. **What good looks like:** The client can act on it without a follow-up call.

### Scope-creep boundary message
```
The client {{client_name}} has asked for {{new_request}} which is outside the agreed scope of {{project}}. Draft a professional message that:
1. Thanks them for the request
2. Acknowledges its value
3. States clearly it's outside the current scope
4. Offers a path: a quote for the add-on, or deferring it
5. Keeps the relationship warm
Keep it 120-150 words. Do not be defensive.
```
**How to use:** When the client adds unplanned work. **What good looks like:** Firm but friendly, keeps the door open.

## Quality Control & QA

### Deliverable QA checklist
```
Generate a QA checklist for the deliverable {{deliverable}} type {{type}} for {{client_name}}. Include:
1. Completeness - does it meet the brief's requirements?
2. Brand accuracy - logo, colors, fonts, tone match the brand guide?
3. Facts & figures - all numbers verified against source?
4. Links & assets - every link works, all assets included?
5. Spelling & grammar
6. Formatting - exports cleanly to PDF/Docs/Sheets
7. Client-readiness - would you send this to the client as-is?
Output as a checkbox list with a pass/fail column.
```
**How to use:** Run on every deliverable before it ships. **What good looks like:** A checklist that catches real errors before the client does.

### Brand voice enforcement check
```
Check the text below against the client's brand voice guide {{brand_voice_guide}}:
{{text_to_check}}
Report: (1) which phrases violate the guide, (2) why, (3) a corrected version of each. Flag any jargon or tone shifts.
```
**How to use:** Paste any draft copy. **What good looks like:** Specific fixes, not a generic "make it more on-brand."

## Brand Voice & Tone

### Brand voice guide extractor
```
From the client's existing materials (website, emails, socials) listed here: {{source_materials}}, distill a reusable brand voice guide:
1. Three adjectives describing the voice
2. Do's (5) and Don'ts (5)
3. Sentence & paragraph rhythm guidance
4. Words to prefer / avoid
5. Emoji and formatting rules
6. Example: on-brand vs off-brand rewrite of the same line
Output in a clean reference format.
```
**How to use:** Run once per client to build their {{brand_voice_guide}}. **What good looks like:** A guide the whole team can follow.

### Voice-tone variant generator
```
Rewrite this copy for {{client_name}} in three tones: professional, friendly, and punchy. Keep meaning identical.
Original: {{copy}}
Output each as a labeled version, then a one-line note on which fits which use case.
```
**How to use:** When a single piece needs to suit different channels. **What good looks like:** Three genuinely different, usable variants.
"""

