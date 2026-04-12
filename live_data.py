import os
import time
import random
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "poe_data.csv")

INTERVAL_SECONDS = 5

EXPECTED_COLUMNS = [
    "timestamp",
    "node_id",
    "volt",
    "ampere",
    "watt",
    "energy_wh",
    "state",
]

NODE_CONFIG = {
    "NODE_01": {"volt": 230, "watt_min": 18, "watt_max": 24},
    "NODE_02": {"volt": 230, "watt_min": 16, "watt_max": 22},
    "NODE_03": {"volt": 230, "watt_min": 19, "watt_max": 26},
}


def detect_separator(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        first_line = f.readline()
    if ";" in first_line:
        return ";"
    return ","


def load_csv_structure(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError("poe_data.csv non trovato")

    sep = detect_separator(file_path)
    df = pd.read_csv(file_path, sep=sep)
    df.columns = df.columns.str.strip().str.lower()

    missing = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Colonne mancanti nel CSV: {missing}")

    return df, sep


def build_new_rows():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = []

    for node_id, cfg in NODE_CONFIG.items():
        volt = float(cfg["volt"])
        watt = round(random.uniform(cfg["watt_min"], cfg["watt_max"]), 2)
        ampere = round(watt / volt, 4)
        energy_wh = round(watt * (INTERVAL_SECONDS / 3600), 4)

        if watt < 19:
            state = "low"
        elif watt <= 23:
            state = "normal"
        else:
            state = "high"

        rows.append(
            {
                "timestamp": now,
                "node_id": node_id,
                "volt": volt,
                "ampere": ampere,
                "watt": watt,
                "energy_wh": energy_wh,
                "state": state,
            }
        )

    return rows


def append_rows(file_path: str, sep: str, rows: list):
    new_df = pd.DataFrame(rows, columns=EXPECTED_COLUMNS)
    new_df.to_csv(file_path, mode="a", header=False, index=False, sep=sep)


def main():
    _, sep = load_csv_structure(FILE_PATH)
    print("Live writer avviato. Premi CTRL + C per fermarlo.")

    while True:
        rows = build_new_rows()
        append_rows(FILE_PATH, sep, rows)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Aggiunte {len(rows)} righe")
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
    