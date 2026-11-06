# Ultron Automation Vault — Setup Guide

Welcome! This pack contains **13 original, hand-built n8n automation workflows**.
They are our own designs — built from scratch, tested structurally, and ready
to import into any n8n instance.

---

## What's in this pack

| # | Workflow | What it does |
|---|---|---|
| 1 | Ultron Research Synthesizer | Chat → query expansion → parallel web search → AI-synthesized research report |
| 2 | Ultron Lead Prospector | Webhook intake → AI lead scoring → route hot leads to CRM / Sheet |
| 3 | Ultron Email Command Center | Gmail trigger → AI classification → auto-drafted replies |
| 4 | Ultron Content Distribution Engine | Scheduled → pull content queue → platform rewrite → post to X |
| 5 | Ultron Document Intake Engine | Google Drive file trigger → PDF extract → AI summary → Sheets |
| 6 | Ultron RAG Knowledge Assistant | Chat + memory + vector-store retrieval with score cutoff |
| 7 | Ultron Invoice Processor | Gmail → PDF invoice extract → structured fields → Sheet + Telegram alert |
| 8 | Ultron Meeting Scheduler | Booking webhook → calendar availability check → create event → confirm |
| 9 | Ultron YouTube Repurposer | New video trigger → transcript → article draft → Notion |
| 10 | Ultron Store Review Monitor | Daily poll reviews → AI sentiment → negative alerts |
| 11 | Ultron Support Triage | Ticket webhook → AI priority/category → on-call alert + auto-reply |
| 12 | Ultron SEO Brief Generator | Keyword → related keywords → SERP scan → full content brief |
| 13 | Ultron Site Sentinel | 15-min uptime probe → status-change detection → Telegram alert |

---

## Importing the workflows

1. Open your n8n instance (self-hosted or cloud).
2. Press `Ctrl/Cmd + O`, or drag the JSON file onto the canvas.
3. Each workflow loads with its nodes and connections intact.
4. Configure credentials where prompted (OpenAI, Gmail, Telegram, Google,
   Notion, etc.) — n8n will ask on first execution.

---

## What you need

- n8n (free, self-hosted — https://n8n.io)
- API keys / OAuth for the services each workflow touches:
  - OpenAI API key (chat/agent nodes)
  - Gmail OAuth (email workflows)
  - Telegram bot token (alert workflows)
  - Google Calendar / Sheets / Drive OAuth
  - Notion integration token
  - A search API (SERP) for research workflows

## Why these workflows are different

- Original architecture and prompt engineering — built by us, from scratch.
- Small, readable node counts — easy to audit and modify.
- Each has a clear trigger → process → output path.
- No hidden third-party services — you connect your own accounts.

---

*Ultron Server — curated AI toolkits built for real work.*
*Free lifetime updates: every future version is yours for free.*
