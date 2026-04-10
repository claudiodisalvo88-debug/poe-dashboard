import pandas as pd
import random
import time
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "poe_data.csv")

nodes = ["NODE_01", "NODE_02", "NODE_03"]

# Ricrea file pulito se non esiste
if not os.path.exists(FILE):
    df_init = pd.DataFrame(columns=[
        "timestamp", "node_id", "volt", "ampere", "watt", "energy_wh", "state"
    ])
    df_init.to_csv(FILE, index=False, sep=";")
    print("Creato file:", FILE)

print("FILE PATH:", FILE)
print("Simulatore PoE avviato...")

while True:
    try:
        volt = round(random.uniform(12.0, 13.0), 2)
        ampere = round(random.uniform(2.0, 4.0), 2)
        watt = round(volt * ampere, 2)
        energy_wh = round(watt * (10 / 60), 2)

        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "node_id": random.choice(nodes),
            "volt": volt,
            "ampere": ampere,
            "watt": watt,
            "energy_wh": energy_wh,
            "state": random.choice(["carica", "scarica", "equilibrio"]),
        }

        df = pd.DataFrame([data])
        df.to_csv(FILE, mode="a", header=False, index=False, sep=";")

        print("Dato scritto:", data)
        time.sleep(3)

    except Exception as e:
        print("Errore:", e)
        break