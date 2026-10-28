#!/usr/bin/env python3
"""
sentinel.py
Autonomous Daily Activity Sentinel & Contribution Consistency Keeper for Avi Perera.
Maintains continuous verifiable repository telemetry and activity health.
"""

import os
import sys
import json
from datetime import datetime, timezone, date

HEARTBEAT_FILE = os.path.join(os.path.dirname(__file__), "heartbeat.json")

def load_heartbeat() -> dict:
    if os.path.exists(HEARTBEAT_FILE):
        try:
            with open(HEARTBEAT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] Notice: Reading heartbeat ({e}). Rebuilding.")
    return {
        "user": "Avi Perera",
        "email": "aviperera0@gmail.com",
        "streak_days": 0,
        "total_pulses": 0,
        "last_pulse": None,
        "history": []
    }

def record_pulse() -> dict:
    data = load_heartbeat()
    now_utc = datetime.now(timezone.utc)
    today_str = now_utc.strftime("%Y-%m-%d")
    now_iso = now_utc.isoformat()

    history = data.get("history", [])
    
    # Check if pulse already recorded today
    already_pulsed_today = False
    if history and history[-1].get("date") == today_str:
        already_pulsed_today = True

    if not already_pulsed_today:
        data["total_pulses"] = data.get("total_pulses", 0) + 1
        data["streak_days"] = data.get("streak_days", 0) + 1
        history.append({
            "date": today_str,
            "timestamp": now_iso,
            "status": "healthy"
        })
        # Keep recent 90 days in history list for compact size
        data["history"] = history[-90:]
    
    data["last_pulse"] = now_iso
    data["status"] = "active"

    with open(HEARTBEAT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[OK] Pulse recorded for {today_str} | Streak: {data['streak_days']} days | Total: {data['total_pulses']}")
    return data

def output_summary(data: dict):
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("## 🟢 Daily Activity Sentinel Pulse\n\n")
        f.write(f"- **Author:** `{data.get('user', 'Avi Perera')}` (`{data.get('email')}`)\n")
        f.write(f"- **Current Active Streak:** **{data.get('streak_days', 1)} Days**\n")
        f.write(f"- **Total Pulses Recorded:** `{data.get('total_pulses', 1)}`\n")
        f.write(f"- **Last Verified Pulse:** `{data.get('last_pulse')}`\n\n")
        f.write("✅ Verified daily contribution graph heartbeat.\n")

def main():
    data = record_pulse()
    output_summary(data)
    return 0

if __name__ == "__main__":
    sys.exit(main())
