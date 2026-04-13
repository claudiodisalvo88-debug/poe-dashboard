import time
import random
from datetime import datetime
from db import init_db, insert_data

INTERVAL = 5
NODES = ["NODE_01", "NODE_02", "NODE_03"]

init_db()

print("LIVE DB START")

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    rows = []
    for n in NODES:
        watt = random.uniform(18, 25)
        energy = watt * (INTERVAL / 3600)

        rows.append((now, n, watt, energy))

    insert_data(rows)

    print("write DB")
    time.sleep(INTERVAL)
    