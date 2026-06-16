import argparse
import time
import requests

from device_registry import SHELLY_DEVICES
from shelly_adapter import ShellyAdapter

POE_INGEST_URL = "http://127.0.0.1:8000/ingest"


def send_payload(payload: dict) -> dict:
    response = requests.post(
        POE_INGEST_URL,
        json=payload,
        timeout=5
    )
    response.raise_for_status()
    return response.json()


def collect_once(node_id: str) -> None:
    device = SHELLY_DEVICES[node_id]

    adapter = ShellyAdapter(
        ip=device["ip"],
        status_endpoint=device["status_endpoint"],
    )

    status = adapter.read_status()

    payload = adapter.to_poe_payload(
        status=status,
        node_id=node_id,
        power_channel=device["power_channel"],
        energy_channel=device["energy_channel"],
    )

    result = send_payload(payload)

    print("Payload sent:")
    print(payload)

    print("Ingest result:")
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--node",
        default="REAL_NODE_01_MAIN"
    )
    parser.add_argument(
        "--once",
        action="store_true"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=30
    )

    args = parser.parse_args()

    if args.once:
        collect_once(args.node)
        return

    while True:
        collect_once(args.node)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
