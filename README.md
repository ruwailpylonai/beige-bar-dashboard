# Beige Bar — Business Intelligence dashboard (preview)

Isolated **preview** of the Beige Bar analytics dashboard (a CRM-style interface layer over
GymMaster, modelled on Bullhorn Analytics). Built by Pylon AI.

- **Live preview:** GitHub Pages (root `index.html`).
- **Self-contained:** no build, no server, no dependencies — one HTML file, hand-rolled SVG charts.
- ⚠️ **SAMPLE DATA** — every number is an illustrative placeholder shaped like Beige Bar's real
  feeds. The banner reads `SAMPLE DATA · not connected` on purpose. Going live needs the
  GymMaster / Meta credentials + the `beige-bar-workspace` repo (not wired yet).
- **Railway-ready too:** `Dockerfile` + `server.py` + `railway.toml` serve the same file on
  `$PORT` if this moves to a Railway service later (e.g. once a live data backend is added).

Sources the data seam maps to: GymMaster Reporting API V2 + Member API, and Meta Ads via
`marketing_report.py`. Draft — gated by Ruwail before anything client-facing.
