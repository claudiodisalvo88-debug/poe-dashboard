import requests
from datetime import datetime, timezone


class ShellyAdapter:
    def __init__(self, ip: str, status_endpoint: str):
        self.url = f"http://{ip}{status_endpoint}"

    def read_status(self) -> dict:
        response = requests.get(self.url, timeout=5)
        response.raise_for_status()
        return response.json()

    def to_poe_payload(
        self,
        status: dict,
        node_id: str,
        power_channel: str,
        energy_channel: str,
    ) -> dict:
        sys_data = status["sys"]
        power_data = status[power_channel]
        energy_data = status[energy_channel]

        return {
            "timestamp": datetime.fromtimestamp(sys_data["unixtime"], tz=timezone.utc).isoformat(),
            "node_id": node_id,
            "watt": float(power_data["act_power"]),
            "energy_wh": float(energy_data["total_act_energy"]),
        }
