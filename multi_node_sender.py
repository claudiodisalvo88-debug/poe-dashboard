import os
import time
import random
from datetime import datetime, timezone

import requests

API_BASE_URL = os.getenv("POE_API_URL", "http://127.0.0.1:8000").rstrip("/")
INGEST_URL = f"{API_BASE_URL}/ingest"
SEND_INTERVAL_SECONDS = float(os.getenv("POE_SEND_INTERVAL_SECONDS", "5"))

NODES = [
    {
        "node_id": "NODE_01",
        "base_watt": 22.0,
        "variation": 2.0,
        "energy_wh": 0.0,
    },
    {
        "node_id": "NODE_02",
        "base_watt": 18.0,
        "variation": 3.5,
        "energy_wh": 0.0,
    },
    {
        "node_id": "NODE_03",
        "base_watt": 27.0,
        "variation": 1.2,
        "energy_wh": 0.0,
    },
]


def generate_watt(base_watt: float, variation: float) -> float:
    watt = random.uniform(base_watt - variation, base_watt + variation)
    return round(max(watt, 0.1), 2)


def build_payload(node: dict, watt: float) -> dict:
    incremental_energy = watt * (SEND_INTERVAL_SECONDS / 3600.0)
    node["energy_wh"] += incremental_energy

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "node_id": node["node_id"],
        "watt": watt,
        "energy_wh": round(node["energy_wh"], 4),
    }


def send_payload(payload: dict) -> None:
    response = requests.post(INGEST_URL, json=payload, timeout=15)
    response.raise_for_status()


def main() -> None:
    print(f"[INFO] Sender attivo verso: {INGEST_URL}")
    print(f"[INFO] Intervallo invio: {SEND_INTERVAL_SECONDS} secondi")
    print("[INFO] Nodi attivi:", ", ".join(node["node_id"] for node in NODES))

    while True:
        for node in NODES:
            watt = generate_watt(node["base_watt"], node["variation"])
            payload = build_payload(node, watt)

            try:
                send_payload(payload)
                print(
                    f"[OK] {payload['node_id']} | "
                    f"watt={payload['watt']} | "
                    f"energy_wh={payload['energy_wh']} | "
                    f"ts={payload['timestamp']}"
                )
            except requests.RequestException as exc:
                print(f"[ERROR] Invio fallito per {payload['node_id']}: {exc}")

        time.sleep(SEND_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
    