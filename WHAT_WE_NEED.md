# Beige Bar dashboard — what we need to go LIVE

The dashboard is a **read-only static site**. It shows SAMPLE data until one file exists next
to `index.html`:

```
data/dashboard.json
```

On load the page fetches that file. If it's present and valid, the dashboard renders the real
numbers and the top-right banner flips from **“SAMPLE DATA · not connected”** to
**“LIVE · synced <time>”**. If it's absent (today), it silently falls back to the built-in
SAMPLE data. **No backend, no server** — the sync agents just write a JSON file.

## The contract
`data/dashboard.json` must match the shape of **`data/dashboard.SAMPLE.json`** (committed next
to it — that's the exact SAMPLE, field-for-field). Add a `syncedAt` string (ISO timestamp or
friendly date) — it's shown in the LIVE banner. Minimal validity check the page runs: the object
has `kpis`, `revenue`, and `reviews`.

## Credentials the sync agents need (none are in the repo yet)
| Source | Credential | Powers |
|---|---|---|
| **GymMaster** | per-site **API key** (Settings → Integrations; needs a paid GymMaster plan) + site/company id | members, memberships, bookings, sales, class & KPI summaries, outstanding balances |
| **Meta Ads** | access token + ad-account id (feeds `marketing_report.py`) | ad spend, CAC, cost-per-new-member, ROAS, leads |
| **Google Business** *(optional)* | Place ID | review count + rating (the `reviews` block) |

## Field → source map (what fills each block of the JSON)
| JSON block | Real source |
|---|---|
| `kpis`, `revenue`, `streams`, `payments`, `packages` | GymMaster **Reporting API V2** (Report&Till → KPIs: sales / member / membership / booking / class summaries) |
| `funnel`, `memberStatus`, `retention`, `bookingsByDay`, `roster`, `drill.*` | GymMaster **Member API** (members, bookings, memberships, outstanding balances) |
| `marketing` | **Meta Ads** insights via `marketing_report.py` (agent #10) |
| `reviews` (rating, count, sources, sentiment, recent, needsResponse) | Google Places rating + the `review-reputation` agent |
| `insights` | derived by the 10 lifecycle agents (failed-payment / casual-to-member / win-back / first-timer / segmentation) |

## Go-live steps (once creds land)
1. Run the sync: `python tools/gymmaster_client.py sync` → local member store, and
   `python tools/marketing_report.py` → Meta metrics.
2. Emit `data/dashboard.json` in the SAMPLE shape (a small writer that maps the synced store →
   this JSON; `syncedAt` = now).
3. Publish it to wherever the static site is served (for GitHub Pages: commit the file to the
   repo; Pages serves `data/dashboard.json` automatically).
4. Reload — the banner flips to LIVE. Schedule the sync (cron / GitHub Action) to refresh it.

Until then the dashboard is a faithful, fully-interactive **SAMPLE** preview — safe to show,
clearly labelled not-connected.
