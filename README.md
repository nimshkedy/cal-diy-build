# cal-diy-build

Builds [Cal.diy](https://github.com/calcom/cal.diy) (MIT) container images from source and pushes them to GHCR:

- `ghcr.io/nimshkedy/cal-diy-web`: the web app (booking pages, settings, embed)
- `ghcr.io/nimshkedy/cal-diy-api-v2`: API v2 (slots and bookings)

The web image is tagged `<upstream commit>-b<this repo's commit>` (the second part pins the branding), plus `latest`. API v2 is tagged with the upstream commit.

**Branding.** The web build swaps in Tipline's icons from `branding/public/` (favicons, touch and tile icons, the in-app icon SVG, the web manifest) and sets the product name with the `app_name` input (default "Tipline Scheduling"). Both are baked in at build time, so changing either means a rebuild. The icons are generated from `tipline.ai/assets/tipline-icon-256.png` and `tipline.ai/favicon.ico`.

Why this exists: Cal.diy publishes no images, and its build needs 6–16 GB of memory, far more than the small server that runs it.

Run it from **Actions → Build Cal.diy images → Run workflow**. Pin `upstream_ref` to a full 40-character commit SHA (a short SHA fails checkout) so a rebuild is reproducible.

The server runs it at `cal.tipline.ai`, from `/opt/cal-diy` on the n8n droplet.
