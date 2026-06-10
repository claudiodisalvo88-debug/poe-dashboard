import os
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = os.getenv("POE_DB_PATH", str(BASE_DIR / "poe.db"))


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS node_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER NOT NULL,
            node_id TEXT NOT NULL,
            watt REAL NOT NULL,
            energy_wh REAL NOT NULL
        )
        """)

        conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_node_time
        ON node_data(node_id, timestamp)
        """)

        conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_time
        ON node_data(timestamp)
        """)

        conn.commit()


def insert_data(rows: list[tuple[int, str, float, float]]) -> None:
    with get_connection() as conn:
        conn.executemany("""
            INSERT INTO node_data (
                timestamp,
                node_id,
                watt,
                energy_wh
            ) VALUES (?, ?, ?, ?)
        """, rows)
        conn.commit()
