# cal-diy-build

Builds [Cal.diy](https://github.com/calcom/cal.diy) (MIT) container images from source and pushes them to GHCR:

- `ghcr.io/nimshkedy/cal-diy-web`: the web app (booking pages, settings, embed)
- `ghcr.io/nimshkedy/cal-diy-api-v2`: API v2 (slots and bookings)

Each image is tagged with the upstream commit it was built from, plus `latest`.

Why this exists: Cal.diy publishes no images, and its build needs 6–16 GB of memory, far more than the small server that runs it.

Run it from **Actions → Build Cal.diy images → Run workflow**. Pin `upstream_ref` to a commit SHA so a rebuild is reproducible.

The server runs it at `cal.tipline.ai`, from `/opt/cal-diy` on the n8n droplet.
