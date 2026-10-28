# Activity Sentinel & Contribution Consistency Keeper

Autonomous daily repository heartbeat for **Avi Perera** that maintains verifiable consistency on the GitHub contributions graph.

---

## ⚡ How It Works

1. **Daily Heartbeat**:
   - Runs automatically every day at `11:45 UTC` via GitHub Actions.
   - Computes streak telemetry, verified UTC timestamps, and logs system health to `heartbeat.json`.
2. **Author Attribution**:
   - Commits are signed with `Avi Perera <aviperera0@gmail.com>`, ensuring every daily pulse is credited to your personal GitHub activity heatmap.
3. **Zero Configuration**:
   - Uses built-in `GITHUB_TOKEN` permissions (`contents: write`). Requires no external tokens or secrets.
