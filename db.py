import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "poe.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS node_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                node_id TEXT NOT NULL,
                watt REAL NOT NULL,
                energy_wh REAL NOT NULL
            )
            """
        )
        conn.commit()


def insert_data(rows: list[tuple[str, str, float, float]]) -> None:
    with get_connection() as conn:
        conn.executemany(
            """
            INSERT INTO node_data (
                timestamp,
                node_id,
                watt,
                energy_wh
            ) VALUES (?, ?, ?, ?)
            """,
            rows,
        )
        conn.commit()


def read_data() -> list[tuple[str, str, float, float]]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT timestamp, node_id, watt, energy_wh
            FROM node_data
            ORDER BY id ASC
            """
        ).fetchall()

    return [
        (row["timestamp"], row["node_id"], row["watt"], row["energy_wh"])
        for row in rows
    ]


def clear_data() -> None:
    with get_connection() as conn:
        conn.execute("DELETE FROM node_data")
        conn.commit()