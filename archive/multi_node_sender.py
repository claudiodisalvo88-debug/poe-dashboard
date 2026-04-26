import time
import random
from datetime import datetime
import requests

API_URL = "http://127.0.0.1:8000/ingest"
INTERVAL_SECONDS = 5

NODES = [
    {"node_id": "NODE_01", "watt_min": 18.0, "watt_max": 24.0},
    {"node_id": "NODE_02", "watt_min": 20.0, "watt_max": 28.0},
    {"node_id": "NODE_03", "watt_min": 15.0, "watt_max": 22.0},
]


def build_payload(node: dict) -> dict:
    watt = round(random.uniform(node["watt_min"], node["watt_max"]), 2)
    energy_wh = round(watt * (INTERVAL_SECONDS / 3600), 4)

    return {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
        "node_id": node["node_id"],
        "watt": watt,
        "energy_wh": energy_wh,
    }


def send_payload(payload: dict) -> None:
    response = requests.post(API_URL, json=payload, timeout=5)
    response.raise_for_status()
    print("SENT:", payload["node_id"], "| API RESPONSE:", response.json())


def main() -> None:
    print("Multi-node sender avviato.")
    print(f"API target: {API_URL}")
    print(f"Nodi simulati: {[node['node_id'] for node in NODES]}")
    print("Premi CTRL+C per fermare.\n")

    while True:
        for node in NODES:
            payload = build_payload(node)

            try:
                send_payload(payload)
            except requests.RequestException as e:
                print(f"[ERROR] {payload['node_id']} -> {e}")

        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
    