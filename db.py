import sqlite3
from datetime import datetime

DB_PATH = "poe.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS energy_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        node_id TEXT,
        watt REAL,
        energy_wh REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_data(rows):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.executemany("""
    INSERT INTO energy_data (timestamp, node_id, watt, energy_wh)
    VALUES (?, ?, ?, ?)
    """, rows)

    conn.commit()
    conn.close()


def read_data():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT timestamp, node_id, watt, energy_wh FROM energy_data")

    data = c.fetchall()
    conn.close()
    return data