# Beige Bar — Dashboard Handoff (for Zayn)

Everything you need to **own this dashboard**, run it on **your own Vercel**, and later **wire
it to live data**. Client = **Beige Bar Tan Studio** (Brooke & Laura, Adelaide SA).

- **Live now (sample data):** Vercel → https://beige-bar-preview.vercel.app · GH Pages fallback → https://ruwailpylonai.github.io/beige-bar-dashboard/
- **Repo (public):** https://github.com/ruwailpylonai/beige-bar-dashboard

---

## 1. What it is + architecture (deliberately simple)
A self-contained, **read-only** analytics dashboard — a CRM-style interface layer over
GymMaster, modelled on Bullhorn Analytics. Five views (Overview, Revenue, Members,
Marketing, Reviews) with drill-down drawers (click any KPI tile or "needs attention" card),
sortable tables, mobile-responsive layout, CSV export, and Beige Bar's real logo + palette.

- **One file:** `index.html` — all HTML/CSS/JS inline, hand-rolled SVG charts, **no build
  step, no dependencies, no backend**. Open it in a browser and it works.
- **The data seam:** on load the page runs `fetch('data/dashboard.json')`.
  - File present + valid → renders the **real** numbers, banner flips to **"LIVE · synced …"**.
  - File absent (today) → falls back to the built-in **SAMPLE** dataset, banner shows
    **"SAMPLE DATA · not connected"**.
- **So going live = producing `data/dashboard.json`** — shape = `data/dashboard.SAMPLE.json`
  (the exact committed example). No server; nothing in the dashboard changes.
- Full go-live spec (credentials + field-by-field map) is in **`WHAT_WE_NEED.md`**.

---

## 2. PROMPT 1 — onboard a fresh Claude Code session to own it
Clone the repo, open it in Claude Code, and paste this:

```text
You are taking ownership of the Beige Bar analytics dashboard in this repo. It's a
self-contained static dashboard — a single index.html with inline CSS/JS, hand-rolled SVG
charts, no build step and no backend — for Beige Bar Tan Studio (client: Brooke & Laura),
modelled on Bullhorn Analytics.

First read, in order: index.html (the top `DATA` object is the data model; there's a
"DATA SEAM" comment explaining it), data/dashboard.SAMPLE.json (the exact JSON shape the
page fetches), and WHAT_WE_NEED.md (how it goes live).

Key facts to preserve:
- On load the page fetches data/dashboard.json; if present+valid it renders real data and
  flips the banner to "LIVE", otherwise it shows the built-in SAMPLE data with a
  "SAMPLE DATA · not connected" banner. Keep that behaviour — never present sample as live.
- 5 views (Overview/Revenue/Members/Marketing/Reviews), drill-down drawers on KPI tiles +
  "needs attention" cards, sortable tables, mobile layout, CSV export.
- It is read-only + static; deploying is just serving the files (Vercel or GitHub Pages).
- It must stay self-contained: no external CDNs, fonts, or network requests.

Confirm you understand the architecture, then wait for my instructions. Extend it, don't
rewrite it. Verify every change by opening it in a real browser with zero console errors.
```

---

## 3. PROMPT 2 — wire GymMaster + Meta → live data
When you have the GymMaster API key + Meta access, paste this into Claude Code in the repo:

```text
Wire this dashboard to real data. GOAL: produce data/dashboard.json (exact shape =
data/dashboard.SAMPLE.json) from Beige Bar's real systems, so the dashboard flips from
SAMPLE to LIVE. Do NOT change how the dashboard renders — only produce the data file.

Read WHAT_WE_NEED.md first — it has the full field-by-field source map. Summary:
- GymMaster Reporting API V2 (Report&Till → KPIs) → fills: kpis, revenue, streams,
  payments, packages  (sales / member / membership / booking / class summaries).
- GymMaster Member API → fills: funnel, memberStatus, retention, bookingsByDay, roster,
  drill.*  (members, bookings, memberships, outstanding balances).
- Meta Ads insights (via marketing_report.py) → fills: marketing (spend, CAC,
  cost-per-new-member, ROAS, leads).
- Google rating + the review-reputation agent → fills: reviews.
- The 10 lifecycle agents → fill: insights[] (the "needs attention" triggers).

Build a small sync script (e.g. tools/build_dashboard_json.py) that:
1. reads creds from a .env — GymMaster per-site API key + site id, Meta token + ad-account
   id, Google Place id — never hard-code secrets;
2. calls the APIs and maps responses into the data/dashboard.SAMPLE.json shape;
3. sets `syncedAt` to the current time and writes data/dashboard.json;
4. can run on a schedule (cron or a GitHub Action) to refresh.

Then: validate the output has the same keys/shape as data/dashboard.SAMPLE.json, commit
data/dashboard.json, redeploy, and confirm in a browser that the banner reads "LIVE".
```

---

## 4. Launch on YOUR Vercel
1. Clone/fork: `git clone https://github.com/ruwailpylonai/beige-bar-dashboard`
2. Deploy: `cd beige-bar-dashboard && vercel --prod` — or at vercel.com → **New Project** →
   import the repo. It's a static site; no build settings needed (a `vercel.json` is included).
3. ⚠️ **Make it publicly viewable** — new Vercel projects put a login wall on deployments:
   Vercel → your project → **Settings → Deployment Protection → Vercel Authentication →
   Disabled**. Without this, clients hit a Vercel login instead of the dashboard.
4. Share the URL with Brooke & Laura. For auto-deploy on every push, connect the repo under
   **Settings → Git**.

*(GitHub Pages also works — Settings → Pages → deploy from `main` / root — that's the
fallback URL above.)*

---
*Built by Pylon AI. Sample data until `data/dashboard.json` is wired (see WHAT_WE_NEED.md).*
