import os
import time
import random
import threading
from datetime import datetime, timezone

from schemas import NodeIngestPayload
from services import ingest_node_data


SEND_INTERVAL_SECONDS = float(os.getenv("POE_INTERNAL_SEND_INTERVAL_SECONDS", "5"))
ENABLE_INTERNAL_GENERATOR = os.getenv("POE_ENABLE_INTERNAL_GENERATOR", "false").lower() == "true"

_generator_started = False


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


def build_payload(node: dict, watt: float) -> NodeIngestPayload:
    incremental_energy = watt * (SEND_INTERVAL_SECONDS / 3600.0)
    node["energy_wh"] += incremental_energy

    return NodeIngestPayload(
        timestamp=datetime.now(timezone.utc).isoformat(),
        node_id=node["node_id"],
        watt=watt,
        energy_wh=round(node["energy_wh"], 4),
    )


def generator_loop() -> None:
    print("[INFO] PoE internal generator started")
    print(f"[INFO] Internal interval: {SEND_INTERVAL_SECONDS} seconds")

    while True:
        for node in NODES:
            try:
                watt = generate_watt(node["base_watt"], node["variation"])
                payload = build_payload(node, watt)
                ingest_node_data(payload)

                print(
                    f"[INTERNAL OK] {payload.node_id} | "
                    f"watt={payload.watt} | "
                    f"energy_wh={payload.energy_wh} | "
                    f"ts={payload.timestamp}"
                )
            except Exception as exc:
                print(f"[INTERNAL ERROR] {node['node_id']}: {exc}")

        time.sleep(SEND_INTERVAL_SECONDS)


def start_internal_generator() -> None:
    global _generator_started

    if not ENABLE_INTERNAL_GENERATOR:
        print("[INFO] PoE internal generator disabled")
        return

    if _generator_started:
        print("[INFO] PoE internal generator already started")
        return

    _generator_started = True

    thread = threading.Thread(target=generator_loop, daemon=True)
    thread.start()
