import csv
import random
import time
from datetime import datetime

nodes = ["NODE_001", "NODE_002", "NODE_003"]
states = ["solar", "battery", "load"]

file = "poe_data.csv"

while True:
    with open(file, "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")

        node = random.choice(nodes)
        state = random.choice(states)

        watt = random.randint(50, 500)
        reputation = random.randint(10, 100)

        writer.writerow([
            datetime.now(),
            node,
            12,
            1.5,
            watt,
            reputation,
            state
        ])

    print("dato generato")
    time.sleep(2)
    