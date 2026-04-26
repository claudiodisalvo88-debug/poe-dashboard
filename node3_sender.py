import time
from datetime import datetime
import requests

API_URL = "http://127.0.0.1:8000/ingest"
NODE_ID = "NODE_03"
INTERVAL = 10


def build_payload():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    payload = {
        "timestamp": now,
        "node_id": NODE_ID,
        "watt": 38.0,
        "energy_wh": 3.8
    }

    return payload


def send_payload(payload):
    response = requests.post(API_URL, json=payload, timeout=5)
    response.raise_for_status()
    return response.json()


print("NODE_03 HTTP sender start")

while True:
    payload = build_payload()

    try:
        result = send_payload(payload)
        print("sent:", payload, "->", result)
    except Exception as e:
        print("error:", e)

    time.sleep(INTERVAL)
    